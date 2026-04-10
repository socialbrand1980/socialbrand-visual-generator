#!/usr/bin/env python3
"""
MCP Server for Socialbrand 1980 — Visual Content Generator
Powered by Replicate — generates product photos, campaign visuals,
product videos, and storyboard frames.
"""

import os
import json
import base64
import httpx
import asyncio
import replicate
from pathlib import Path
from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# ─── INIT ───
load_dotenv(Path(__file__).parent / ".env")

mcp = FastMCP("socialbrand_photo_mcp")

BRANDS_DIR         = Path(__file__).parent.parent / "brands"
_REPLICATE_TOKEN   = os.getenv("REPLICATE_API_TOKEN", "")


# ─── ENUMS ───

class OutputType(str, Enum):
    PRODUCT    = "product"    # img2img → clean product photo
    CAMPAIGN   = "campaign"   # img2img → campaign ad photo
    VIDEO      = "video"      # img2video → product video clip
    STORYBOARD = "storyboard" # text2img → storyboard frame

class ProductPhotoStyle(str, Enum):
    CLEAN_WHITE  = "clean white studio background, professional product photography"
    MINIMAL_GREY = "minimal light grey background, soft shadows, professional product shot"
    NATURAL      = "natural light, lifestyle setting, warm tones"
    DARK_MOODY   = "dark moody background, dramatic lighting, luxury feel"
    FLAT_LAY     = "flat lay, top-down view, styled arrangement, clean background"
    CONTEXTUAL   = "contextual setting, in-use lifestyle shot, natural environment"

class StoryboardSize(str, Enum):
    SQUARE      = "square_hd"       # 1:1  — Instagram Feed / TikTok
    LANDSCAPE   = "landscape_16_9"  # 16:9 — Presentation / YouTube
    PORTRAIT    = "portrait_16_9"   # 9:16 — Story / Reels / TikTok
    WIDE        = "landscape_4_3"   # 4:3  — General use

class VideoAspectRatio(str, Enum):
    AUTO       = "auto"
    VERTICAL   = "9:16"   # Reels / TikTok / Story
    HORIZONTAL = "16:9"   # YouTube / Banner
    SQUARE     = "1:1"    # Feed


# ─── MODEL CATALOGS ───

IMG2IMG_MODELS = {
    "black-forest-labs/flux-1.1-pro":      "FLUX 1.1 Pro — high quality img2img (default)",
    "black-forest-labs/flux-dev":           "FLUX Dev — balanced quality & speed",
    "black-forest-labs/flux-schnell":       "FLUX Schnell — fastest, good for drafts",
    "stability-ai/sdxl":                    "SDXL — alternative architecture",
}

IMG2VIDEO_MODELS = {
    "minimax/video-01-live":                "Minimax Video-01 Live — cinematic motion (default)",
    "kwaivgi/kling-v1.6-standard":          "Kling 1.6 Standard — reliable, smooth motion",
    "stability-ai/stable-video-diffusion":  "SVD — Stability AI, subtle/short motion",
}

TEXT2IMG_MODELS = {
    "black-forest-labs/flux-dev":           "FLUX Dev — detailed & creative (default)",
    "black-forest-labs/flux-1.1-pro":       "FLUX 1.1 Pro — premium quality",
    "black-forest-labs/flux-schnell":       "FLUX Schnell — fastest drafts",
    "recraft-ai/recraft-v3":                "Recraft V3 — excellent for brand & illustration",
    "ideogram-ai/ideogram-v2":              "Ideogram V2 — great typography & graphic design",
    "google-deepmind/imagen-3":             "Imagen 3 — Google's state-of-the-art model",
}


# ─── HELPERS ───

def _get_brand_info(brand_name: str) -> dict:
    """Read brand-info.md and return parsed key info as dict."""
    brand_dir = BRANDS_DIR / brand_name
    info_file = brand_dir / "brand-info.md"
    if not info_file.exists():
        return {}
    content = info_file.read_text()
    return {"raw": content, "name": brand_name}


def _get_brand_list() -> list[str]:
    """List all available brand folders."""
    if not BRANDS_DIR.exists():
        return []
    return [
        d.name for d in BRANDS_DIR.iterdir()
        if d.is_dir() and d.name != "_template"
    ]


def _encode_image(image_path: str) -> str:
    """Encode image to base64 data URI."""
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    ext = path.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "jpeg")
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/{mime};base64,{encoded}"


def _save_file(brand_name: str, output_type: OutputType, file_url: str, filename: str) -> str:
    """Download generated file (image or video) and save to correct brand folder."""
    folder = BRANDS_DIR / brand_name / "generated" / output_type.value
    folder.mkdir(parents=True, exist_ok=True)
    output_path = folder / filename
    with httpx.Client() as client:
        response = client.get(file_url, timeout=120.0)
        response.raise_for_status()
        output_path.write_bytes(response.content)
    return str(output_path)


def _build_product_prompt(style: ProductPhotoStyle, extra: str, brand_info: dict) -> str:
    """Build optimized product photography prompt."""
    brand_context = ""
    if brand_info.get("raw"):
        raw = brand_info["raw"]
        for line in raw.split("\n"):
            if "Photography Style" in line or "Lighting" in line or "Background" in line:
                brand_context += line.strip().lstrip("#- ") + ". "

    prompt = (
        f"{style.value}. "
        f"Commercial product photography, ultra high quality, sharp focus, "
        f"professional lighting, detailed texture, color accurate, "
        f"shot on medium format camera, 85mm lens, "
        f"no shadows on background, clean composition. "
    )
    if brand_context:
        prompt += f"Brand style: {brand_context.strip()} "
    if extra:
        prompt += extra.strip()
    return prompt.strip()


def _build_campaign_prompt(product_desc: str, mood: str, platform: str, extra: str, brand_info: dict) -> str:
    """Build optimized campaign/ad creative prompt."""
    brand_context = ""
    if brand_info.get("raw"):
        raw = brand_info["raw"]
        for line in raw.split("\n"):
            if any(k in line for k in ["Mood", "Tone", "Campaign Style", "Colors"]):
                brand_context += line.strip().lstrip("#- ") + ". "

    platform_specs = {
        "Instagram Feed":  "vertical composition 4:5, instagram optimized, scroll-stopping visual",
        "Instagram Story": "vertical 9:16, story format, bold visual hierarchy",
        "TikTok":          "vertical 9:16, dynamic visual, youthful energy",
        "Facebook Ad":     "square or landscape, clear focal point, ad-optimized composition",
        "Banner":          "horizontal composition, clean layout, ad banner format",
    }
    plat_hint = platform_specs.get(platform, "social media optimized composition")

    prompt = (
        f"Professional advertising campaign photo featuring {product_desc}. "
        f"{mood} mood and atmosphere. "
        f"{plat_hint}. "
        f"High-end commercial photography, cinematic quality, "
        f"brand-forward visual, aspirational lifestyle, "
        f"perfect exposure and color grading. "
    )
    if brand_context:
        prompt += f"Brand aesthetic: {brand_context.strip()} "
    if extra:
        prompt += extra.strip()
    return prompt.strip()


def _build_video_prompt(product_desc: str, motion_desc: str, platform: str, extra: str, brand_info: dict) -> str:
    """Build optimized image-to-video prompt."""
    brand_context = ""
    if brand_info.get("raw"):
        raw = brand_info["raw"]
        for line in raw.split("\n"):
            if any(k in line for k in ["Mood", "Tone", "Campaign Style"]):
                brand_context += line.strip().lstrip("#- ") + ". "

    platform_motion = {
        "Instagram Reels": "smooth cinematic motion, vertical orientation, dynamic pacing",
        "TikTok":          "energetic motion, vertical format, eye-catching movement",
        "Instagram Story": "subtle elegant motion, vertical format, clean movement",
        "YouTube":         "cinematic wide motion, horizontal format, professional pacing",
        "Facebook":        "smooth motion, universal format, clear product focus",
    }
    motion_hint = platform_motion.get(platform, "smooth cinematic motion")

    prompt = (
        f"{product_desc} in motion. "
        f"{motion_desc}. "
        f"{motion_hint}. "
        f"Professional product video, high quality, smooth movement, "
        f"brand-forward visual storytelling. "
    )
    if brand_context:
        prompt += f"Brand aesthetic: {brand_context.strip()} "
    if extra:
        prompt += extra.strip()
    return prompt.strip()


def _build_storyboard_prompt(scene_desc: str, frame_type: str, platform: str, extra: str, brand_info: dict) -> str:
    """Build optimized text-to-image prompt for storyboard frames."""
    brand_context = ""
    if brand_info.get("raw"):
        raw = brand_info["raw"]
        for line in raw.split("\n"):
            if any(k in line for k in ["Colors", "Typography", "Photography Style", "Mood", "Tone"]):
                brand_context += line.strip().lstrip("#- ") + ". "

    frame_styles = {
        "product_hero":    "hero product shot, commercial photography style, centered composition",
        "lifestyle":       "lifestyle scene, aspirational setting, model interaction",
        "detail_closeup":  "extreme close-up detail shot, macro photography, texture focus",
        "behind_scenes":   "behind the scenes candid style, authentic feel",
        "brand_moment":    "brand lifestyle moment, emotional storytelling",
        "comparison":      "before/after or comparison layout, split composition",
        "text_overlay":    "clean background leaving space for text overlay, minimal composition",
    }
    frame_hint = frame_styles.get(frame_type, "professional commercial photography")

    prompt = (
        f"Storyboard frame: {scene_desc}. "
        f"{frame_hint}. "
        f"High quality concept visualization, professional lighting, "
        f"clear composition, suitable for {platform} content. "
    )
    if brand_context:
        prompt += f"Brand style: {brand_context.strip()} "
    if extra:
        prompt += extra.strip()
    return prompt.strip()


async def _replicate_request(model: str, payload: dict, api_token: str) -> dict:
    """Call Replicate API and return normalized output dict."""
    client = replicate.Client(api_token=api_token)

    # Replicate library is synchronous — run in thread pool to avoid blocking
    output = await asyncio.to_thread(client.run, model, input=payload)

    if output is None:
        return {}

    # Normalize output → consistent {"images": [...]} or {"video": {...}} format
    def _to_url(item) -> str:
        """Extract URL string from Replicate FileOutput or plain string."""
        return item.url if hasattr(item, "url") else str(item)

    # List output → multiple images
    if isinstance(output, list):
        urls = [_to_url(u) for u in output if u]
        # Detect video by extension
        if urls and any(u.split("?")[0].endswith((".mp4", ".mov", ".webm")) for u in urls):
            return {"video": {"url": urls[0]}, "output": urls}
        return {"images": [{"url": u} for u in urls], "output": urls}

    # Single output
    url = _to_url(output)
    if url.split("?")[0].endswith((".mp4", ".mov", ".webm")):
        return {"video": {"url": url}, "output": url}
    return {"images": [{"url": url}], "output": url}


def _handle_error(e: Exception) -> str:
    if isinstance(e, FileNotFoundError):
        return f"Error: {e}. Check that the image path is correct."
    if isinstance(e, replicate.exceptions.ReplicateError):
        return f"Error: Replicate API error — {e}"
    if isinstance(e, httpx.HTTPStatusError):
        if e.response.status_code == 401:
            return "Error: Invalid Replicate API token. Check REPLICATE_API_TOKEN in mcp/.env"
        if e.response.status_code == 402:
            return "Error: Insufficient Replicate credits. Top up at replicate.com/account/billing"
        if e.response.status_code == 429:
            return "Error: Rate limit hit. Wait a moment before retrying."
        return f"Error: Replicate returned {e.response.status_code}: {e.response.text}"
    if isinstance(e, TimeoutError):
        return "Error: Generation timed out. Try again or use a faster model."
    return f"Error: {type(e).__name__}: {e}"


# ─── TOOLS ───

# ── 1. LIST BRANDS ──────────────────────────────────────────────────────────

class ListBrandsInput(BaseModel):
    model_config = ConfigDict(extra="forbid")


@mcp.tool(
    name="list_brands",
    annotations={
        "title": "List Available Brands",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def list_brands(params: ListBrandsInput) -> str:
    """
    List all available brand folders with their asset counts.
    Shows counts for raw photos, generated images, videos, and storyboard frames.
    Use this before generating content to confirm which brand names are valid.
    """
    brands = _get_brand_list()
    if not brands:
        return json.dumps({
            "brands": [],
            "message": "No brands found. Create a folder in brands/ by copying _template."
        }, indent=2)

    result = []
    for brand in brands:
        bd = BRANDS_DIR / brand

        def _count(subfolder):
            p = bd / subfolder
            return len(list(p.glob("*.*"))) if p.exists() else 0

        result.append({
            "brand_name":          brand,
            "has_brand_info":      (bd / "brand-info.md").exists(),
            "raw_photos":          _count("raw"),
            "moodboard_files":     _count("moodboard"),
            "generated_product":   _count("generated/product"),
            "generated_campaign":  _count("generated/campaign"),
            "generated_video":     _count("generated/video"),
            "generated_storyboard": _count("generated/storyboard"),
        })

    return json.dumps({"brands": result, "total": len(result)}, indent=2)


# ── 2. GET BRAND INFO ────────────────────────────────────────────────────────

class GetBrandInfoInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    brand_name: str = Field(..., description="Brand folder name", min_length=1)


@mcp.tool(
    name="get_brand_info",
    annotations={
        "title": "Get Brand Info",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def get_brand_info(params: GetBrandInfoInput) -> str:
    """
    Read and return the brand-info.md for a specific brand.
    Returns brand guidelines, visual identity, photography style, and available raw photos.
    """
    brand_dir = BRANDS_DIR / params.brand_name
    if not brand_dir.exists():
        return f"Error: Brand '{params.brand_name}' not found. Use list_brands to see available brands."

    info_file = brand_dir / "brand-info.md"
    if not info_file.exists():
        return f"Error: brand-info.md not found for '{params.brand_name}'."

    content = info_file.read_text()
    raw_photos = list((brand_dir / "raw").glob("*.*")) if (brand_dir / "raw").exists() else []

    return json.dumps({
        "brand_name":           params.brand_name,
        "brand_info":           content,
        "available_raw_photos": [p.name for p in raw_photos],
    }, indent=2)


# ── 3. LIST AVAILABLE MODELS ─────────────────────────────────────────────────

class ListModelsInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    category: str = Field(
        default="all",
        description=(
            "Filter by category: 'all', 'image-to-image', 'image-to-video', 'text-to-image'. "
            "Use 'all' to see the full catalog with recommended models highlighted."
        )
    )


@mcp.tool(
    name="list_available_models",
    annotations={
        "title": "List Available AI Models",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True
    }
)
async def list_available_models(params: ListModelsInput) -> str:
    """
    List available Replicate models for image, video, and storyboard generation.

    Returns a curated catalog of recommended models organized by use case.

    Args:
        category: 'all', 'image-to-image', 'image-to-video', or 'text-to-image'

    Returns:
        str: JSON catalog of models with descriptions and use case guidance
    """
    cat = params.category.lower()
    catalog = {}

    if cat in ("all", "image-to-image"):
        catalog["image_to_image"] = {
            "description": "Transform an existing product photo into a new style.",
            "use_for": ["generate_product_photo", "generate_campaign_photo"],
            "models": IMG2IMG_MODELS
        }

    if cat in ("all", "image-to-video"):
        catalog["image_to_video"] = {
            "description": "Animate a product photo into a short video clip.",
            "use_for": ["generate_video_from_image"],
            "models": IMG2VIDEO_MODELS
        }

    if cat in ("all", "text-to-image"):
        catalog["text_to_image"] = {
            "description": "Generate storyboard frames purely from text description.",
            "use_for": ["generate_storyboard_frame"],
            "models": TEXT2IMG_MODELS
        }

    return json.dumps({
        "platform":     "Replicate (replicate.com)",
        "catalog":      catalog,
        "usage_tip":    (
            "Pass any model's ID as the 'model' parameter in generate_* tools. "
            "Browse more models at replicate.com/explore"
        )
    }, indent=2)


# ── 4. GENERATE PRODUCT PHOTO ────────────────────────────────────────────────

class GenerateProductPhotoInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    brand_name: str = Field(
        ...,
        description="Brand folder name in brands/ directory. Use list_brands to see options.",
        min_length=1
    )
    product_image_path: str = Field(
        ...,
        description="Absolute or relative path to the raw product photo (e.g. 'brands/brand-abc/raw/product.jpg')"
    )
    style: ProductPhotoStyle = Field(
        default=ProductPhotoStyle.CLEAN_WHITE,
        description="Photography style preset for the generated photo"
    )
    model: str = Field(
        default="black-forest-labs/flux-1.1-pro",
        description=(
            "Replicate model to use. Recommended: "
            "'black-forest-labs/flux-1.1-pro' (default, high quality), "
            "'black-forest-labs/flux-dev' (balanced), "
            "'black-forest-labs/flux-schnell' (fastest draft), "
            "'stability-ai/sdxl' (alternative). "
            "Use list_available_models to discover more."
        )
    )
    extra_prompt: Optional[str] = Field(
        default=None,
        description="Optional extra detail, e.g. 'water droplets on bottle' or 'floating in mid-air'",
        max_length=300
    )
    strength: float = Field(
        default=0.75,
        description="Transformation strength (0.1 = subtle, 0.95 = strong). Default 0.75.",
        ge=0.1, le=0.95
    )
    api_key: Optional[str] = Field(
        default=None,
        description="Replicate API token. Leave empty to use token from .env file."
    )


@mcp.tool(
    name="generate_product_photo",
    annotations={
        "title": "Generate Product Photo",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True
    }
)
async def generate_product_photo(params: GenerateProductPhotoInput) -> str:
    """
    Generate a professional product photo from a raw product image using Replicate.

    Transforms an existing product photo into a clean, commercial image
    using the specified style and brand context.
    Output saved to brands/{brand_name}/generated/product/.
    """
    try:
        api_token = params.api_key or _REPLICATE_TOKEN
        if not api_token:
            return "Error: No API token found. Add REPLICATE_API_TOKEN to mcp/.env or pass it as api_key."

        brand_info = _get_brand_info(params.brand_name)
        prompt = _build_product_prompt(params.style, params.extra_prompt or "", brand_info)

        # Pass image as open file — Replicate handles upload
        img_path = Path(params.product_image_path)
        if not img_path.exists():
            return f"Error: Image not found: {params.product_image_path}"

        with open(img_path, "rb") as img_file:
            payload = {
                "prompt":          prompt,
                "image":           img_file,
                "prompt_strength": params.strength,
                "num_outputs":     1,
            }
            result = await _replicate_request(params.model, payload, api_token)

        images = result.get("images", [])
        if not images:
            return f"Error: Replicate returned no images. Full response: {result}"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{params.brand_name}_product_{timestamp}.jpg"
        saved_path = _save_file(params.brand_name, OutputType.PRODUCT, images[0]["url"], filename)

        return json.dumps({
            "status":      "success",
            "saved_to":    saved_path,
            "prompt_used": prompt,
            "model":       params.model,
            "tip":         "Adjust 'strength', 'style', or 'extra_prompt' to refine the result."
        }, indent=2)

    except Exception as e:
        return _handle_error(e)


# ── 5. GENERATE CAMPAIGN PHOTO ───────────────────────────────────────────────

class GenerateCampaignPhotoInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    brand_name: str = Field(
        ...,
        description="Brand folder name in brands/ directory",
        min_length=1
    )
    product_image_path: str = Field(
        ...,
        description="Path to the product photo to feature in the campaign image"
    )
    product_description: str = Field(
        ...,
        description="Short description, e.g. 'matte black water bottle' or 'brightening serum'",
        max_length=200
    )
    mood: str = Field(
        ...,
        description="Campaign mood/vibe, e.g. 'energetic and sporty', 'luxurious and minimalist'",
        max_length=200
    )
    platform: str = Field(
        default="Instagram Feed",
        description="Target platform: 'Instagram Feed', 'Instagram Story', 'TikTok', 'Facebook Ad', 'Banner'"
    )
    model: str = Field(
        default="black-forest-labs/flux-1.1-pro",
        description=(
            "Replicate model to use. Recommended: "
            "'black-forest-labs/flux-1.1-pro' (default, high quality), "
            "'black-forest-labs/flux-dev' (balanced), "
            "'stability-ai/sdxl' (alternative). "
            "Use list_available_models to discover more."
        )
    )
    extra_prompt: Optional[str] = Field(
        default=None,
        description="Extra scene detail, e.g. 'golden hour lighting' or 'urban street background'",
        max_length=400
    )
    strength: float = Field(
        default=0.85,
        description="Transformation strength (0.7–0.95 recommended for campaign photos). Default 0.85.",
        ge=0.5, le=0.95
    )
    api_key: Optional[str] = Field(
        default=None,
        description="Replicate API token. Leave empty to use token from .env file."
    )


@mcp.tool(
    name="generate_campaign_photo",
    annotations={
        "title": "Generate Campaign / Ad Photo",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True
    }
)
async def generate_campaign_photo(params: GenerateCampaignPhotoInput) -> str:
    """
    Generate a campaign or advertisement photo from a product image using Replicate.

    Combines product photo with brand context and campaign brief to produce
    a polished campaign visual for ads or social media.
    Output saved to brands/{brand_name}/generated/campaign/.
    """
    try:
        api_token = params.api_key or _REPLICATE_TOKEN
        if not api_token:
            return "Error: No API token found. Add REPLICATE_API_TOKEN to mcp/.env or pass it as api_key."

        brand_info = _get_brand_info(params.brand_name)
        prompt = _build_campaign_prompt(
            params.product_description,
            params.mood,
            params.platform,
            params.extra_prompt or "",
            brand_info
        )

        img_path = Path(params.product_image_path)
        if not img_path.exists():
            return f"Error: Image not found: {params.product_image_path}"

        with open(img_path, "rb") as img_file:
            payload = {
                "prompt":          prompt,
                "image":           img_file,
                "prompt_strength": params.strength,
                "num_outputs":     1,
            }
            result = await _replicate_request(params.model, payload, api_token)

        images = result.get("images", [])
        if not images:
            return f"Error: Replicate returned no images. Full response: {result}"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        platform_slug = params.platform.lower().replace(" ", "_")
        filename = f"{params.brand_name}_campaign_{platform_slug}_{timestamp}.jpg"
        saved_path = _save_file(params.brand_name, OutputType.CAMPAIGN, images[0]["url"], filename)

        return json.dumps({
            "status":      "success",
            "saved_to":    saved_path,
            "prompt_used": prompt,
            "model":       params.model,
            "tip":         "For stronger brand look, refine 'extra_prompt' or update brand-info.md"
        }, indent=2)

    except Exception as e:
        return _handle_error(e)


# ── 6. GENERATE VIDEO FROM IMAGE ─────────────────────────────────────────────

class GenerateVideoInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    brand_name: str = Field(
        ...,
        description="Brand folder name in brands/ directory.",
        min_length=1
    )
    product_image_path: str = Field(
        ...,
        description="Path to the product photo to animate into a video"
    )
    product_description: str = Field(
        ...,
        description="What the product is, e.g. 'brightening face serum in glass bottle'",
        max_length=200
    )
    motion_description: str = Field(
        ...,
        description=(
            "Describe the motion/animation, e.g. 'product rotating slowly with light shimmer', "
            "'bottle floating with water ripple effect', 'product being picked up by hand'"
        ),
        max_length=300
    )
    platform: str = Field(
        default="Instagram Reels",
        description="Target platform: 'Instagram Reels', 'TikTok', 'Instagram Story', 'YouTube', 'Facebook'"
    )
    model: str = Field(
        default="minimax/video-01-live",
        description=(
            "Replicate image-to-video model. Options: "
            "'minimax/video-01-live' (cinematic motion, default), "
            "'kwaivgi/kling-v1.6-standard' (reliable, smooth motion), "
            "'stability-ai/stable-video-diffusion' (subtle motion, SVD). "
            "Use list_available_models to discover more."
        )
    )
    duration: str = Field(
        default="5",
        description="Video duration in seconds. Options: '2', '3', '4', '5', '6', '8', '10'. Default '5'. Not all models support all durations."
    )
    resolution: str = Field(
        default="720p",
        description="Video resolution: '480p' (fast), '720p' (balanced, default), '1080p' (best quality)"
    )
    aspect_ratio: VideoAspectRatio = Field(
        default=VideoAspectRatio.AUTO,
        description="Aspect ratio: 'auto' (match source), '9:16' (Reels/TikTok), '16:9' (YouTube), '1:1' (Feed)"
    )
    extra_prompt: Optional[str] = Field(
        default=None,
        description="Extra prompt detail for the video, e.g. 'soft bokeh background', 'luxury golden lighting'",
        max_length=300
    )
    api_key: Optional[str] = Field(
        default=None,
        description="Replicate API token. Leave empty to use token from .env file."
    )


@mcp.tool(
    name="generate_video_from_image",
    annotations={
        "title": "Generate Product Video from Image",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True
    }
)
async def generate_video_from_image(params: GenerateVideoInput) -> str:
    """
    Animate a product photo into a short video clip using Replicate image-to-video models.

    Supports Minimax Video-01 Live, Kling, and Stable Video Diffusion.
    Output is saved as MP4 to brands/{brand_name}/generated/video/.
    Great for creating Reels, TikTok product videos, and motion ads.

    Note: Video generation takes 30–120 seconds depending on model and resolution.
    """
    try:
        api_token = params.api_key or _REPLICATE_TOKEN
        if not api_token:
            return "Error: No API token found. Add REPLICATE_API_TOKEN to mcp/.env or pass it as api_key."

        brand_info = _get_brand_info(params.brand_name)
        prompt = _build_video_prompt(
            params.product_description,
            params.motion_description,
            params.platform,
            params.extra_prompt or "",
            brand_info
        )

        img_path = Path(params.product_image_path)
        if not img_path.exists():
            return f"Error: Image not found: {params.product_image_path}"

        image_data_uri = _encode_image(params.product_image_path)

        # Replicate video models use image_url (data URI) and vary in params
        payload = {
            "prompt":    prompt,
            "image_url": image_data_uri,
        }

        # Add aspect_ratio only when not auto
        if params.aspect_ratio != VideoAspectRatio.AUTO:
            payload["aspect_ratio"] = params.aspect_ratio.value

        result = await _replicate_request(params.model, payload, api_token)

        video = result.get("video", {})
        if not video or not video.get("url"):
            return f"Error: Replicate returned no video. Full response: {result}"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        platform_slug = params.platform.lower().replace(" ", "_")
        filename = f"{params.brand_name}_video_{platform_slug}_{timestamp}.mp4"
        saved_path = _save_file(params.brand_name, OutputType.VIDEO, video["url"], filename)

        return json.dumps({
            "status":      "success",
            "saved_to":    saved_path,
            "prompt_used": prompt,
            "model":       params.model,
            "tip":         "For cinematic motion try minimax/video-01-live. For smooth motion try kling-v1.6."
        }, indent=2)

    except Exception as e:
        return _handle_error(e)


# ── 7. GENERATE STORYBOARD FRAME ─────────────────────────────────────────────

class GenerateStoryboardInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    brand_name: Optional[str] = Field(
        default=None,
        description="Brand folder name to include brand style in the generation. Optional but recommended."
    )
    scene_description: str = Field(
        ...,
        description=(
            "Describe the scene you want to visualize, e.g. "
            "'woman applying serum in soft morning light, bathroom setting, peaceful mood', "
            "'product on marble surface with dried flowers around it'"
        ),
        min_length=10,
        max_length=500
    )
    frame_type: str = Field(
        default="product_hero",
        description=(
            "Type of storyboard frame: "
            "'product_hero' (centered hero shot), "
            "'lifestyle' (model in scene), "
            "'detail_closeup' (macro/texture detail), "
            "'behind_scenes' (candid authentic), "
            "'brand_moment' (emotional storytelling), "
            "'comparison' (before/after layout), "
            "'text_overlay' (leave space for copy)"
        )
    )
    platform: str = Field(
        default="Instagram Feed",
        description="Target platform: 'Instagram Feed', 'Instagram Story', 'TikTok', 'YouTube', 'Print'"
    )
    image_size: StoryboardSize = Field(
        default=StoryboardSize.SQUARE,
        description=(
            "Output image size: "
            "'square_hd' (1:1, Instagram Feed/TikTok), "
            "'landscape_16_9' (16:9, YouTube/presentation), "
            "'portrait_16_9' (9:16, Story/Reels), "
            "'landscape_4_3' (4:3, general)"
        )
    )
    model: str = Field(
        default="black-forest-labs/flux-dev",
        description=(
            "Replicate text-to-image model. Options: "
            "'black-forest-labs/flux-dev' (FLUX Dev, balanced, default), "
            "'black-forest-labs/flux-1.1-pro' (FLUX Pro, premium quality), "
            "'black-forest-labs/flux-schnell' (FLUX Schnell, fastest drafts), "
            "'recraft-ai/recraft-v3' (great for brand/illustration), "
            "'ideogram-ai/ideogram-v2' (great typography & graphic design), "
            "'google-deepmind/imagen-3' (Google's state-of-the-art). "
            "Use list_available_models to discover more."
        )
    )
    extra_prompt: Optional[str] = Field(
        default=None,
        description="Extra detail to add, e.g. 'golden hour light', 'minimalist Korean aesthetic'",
        max_length=300
    )
    num_frames: int = Field(
        default=1,
        description="Number of storyboard frames to generate in one call (1–4). Default 1.",
        ge=1, le=4
    )
    api_key: Optional[str] = Field(
        default=None,
        description="Replicate API token. Leave empty to use token from .env file."
    )


@mcp.tool(
    name="generate_storyboard_frame",
    annotations={
        "title": "Generate Storyboard Frame (Text-to-Image)",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True
    }
)
async def generate_storyboard_frame(params: GenerateStoryboardInput) -> str:
    """
    Generate storyboard frames from text descriptions using Replicate text-to-image models.

    No source image needed — generates visual concepts purely from your scene description.
    Great for campaign storyboarding, content planning, and concept visualization.
    Output saved to brands/{brand_name}/generated/storyboard/.

    Supports FLUX, Recraft, Ideogram, and Imagen 3 models.
    """
    try:
        api_token = params.api_key or _REPLICATE_TOKEN
        if not api_token:
            return "Error: No API token found. Add REPLICATE_API_TOKEN to mcp/.env or pass it as api_key."

        brand_info = _get_brand_info(params.brand_name) if params.brand_name else {}
        prompt = _build_storyboard_prompt(
            params.scene_description,
            params.frame_type,
            params.platform,
            params.extra_prompt or "",
            brand_info
        )

        # Map StoryboardSize → Replicate aspect_ratio
        size_to_ratio = {
            "square_hd":       "1:1",
            "landscape_16_9":  "16:9",
            "portrait_16_9":   "9:16",
            "landscape_4_3":   "4:3",
        }
        aspect_ratio = size_to_ratio.get(params.image_size.value, "1:1")

        payload = {
            "prompt":       prompt,
            "aspect_ratio": aspect_ratio,
            "num_outputs":  params.num_frames,
        }

        result = await _replicate_request(params.model, payload, api_token)

        images = result.get("images", [])
        if not images:
            return f"Error: Replicate returned no images. Full response: {result}"

        saved_paths = []
        brand_save = params.brand_name or "general"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        for i, img in enumerate(images):
            suffix = f"_{i+1}" if len(images) > 1 else ""
            filename = f"storyboard_{params.frame_type}{suffix}_{timestamp}.jpg"
            path = _save_file(brand_save, OutputType.STORYBOARD, img["url"], filename)
            saved_paths.append(path)

        return json.dumps({
            "status":        "success",
            "saved_to":      saved_paths if len(saved_paths) > 1 else saved_paths[0],
            "frames_count":  len(saved_paths),
            "prompt_used":   prompt,
            "model":         params.model,
            "frame_type":    params.frame_type,
            "tip":           "Generate multiple frame types to build a full storyboard for your campaign."
        }, indent=2)

    except Exception as e:
        return _handle_error(e)


# ── 8. POLISH PROMPT ─────────────────────────────────────────────────────────

class PolishPromptInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    content_type: str = Field(
        ...,
        description=(
            "Type of content to polish for: "
            "'product' (clean product shot), "
            "'campaign' (ad/social media visual), "
            "'video' (image-to-video motion description), "
            "'storyboard' (text-to-image scene)"
        )
    )
    brand_name: Optional[str] = Field(
        default=None,
        description="Brand folder name to include brand context in prompt"
    )
    raw_prompt: str = Field(
        ...,
        description="Your rough idea, e.g. 'serum bottle floating with sparkles around it'",
        min_length=5,
        max_length=500
    )
    platform: Optional[str] = Field(
        default=None,
        description="Target platform (Instagram Feed, TikTok, Reels, YouTube, etc.)"
    )


@mcp.tool(
    name="polish_prompt",
    annotations={
        "title": "Polish Content Generation Prompt",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def polish_prompt(params: PolishPromptInput) -> str:
    """
    Polish a rough idea into an optimized fal.ai prompt.

    Supports product photos, campaign visuals, video motion descriptions,
    and storyboard scene descriptions. Includes brand context if brand_name is provided.
    """
    brand_info = _get_brand_info(params.brand_name) if params.brand_name else {}
    ct = params.content_type.lower()

    if ct == "product":
        polished = _build_product_prompt(ProductPhotoStyle.CLEAN_WHITE, params.raw_prompt, brand_info)
        tool_hint = "generate_product_photo"

    elif ct == "campaign":
        polished = _build_campaign_prompt(
            product_desc=params.raw_prompt,
            mood="aspirational and engaging",
            platform=params.platform or "Instagram Feed",
            extra="",
            brand_info=brand_info
        )
        tool_hint = "generate_campaign_photo"

    elif ct == "video":
        polished = _build_video_prompt(
            product_desc=params.raw_prompt,
            motion_desc="smooth cinematic motion",
            platform=params.platform or "Instagram Reels",
            extra="",
            brand_info=brand_info
        )
        tool_hint = "generate_video_from_image"

    elif ct == "storyboard":
        polished = _build_storyboard_prompt(
            scene_desc=params.raw_prompt,
            frame_type="product_hero",
            platform=params.platform or "Instagram Feed",
            extra="",
            brand_info=brand_info
        )
        tool_hint = "generate_storyboard_frame"

    else:
        return f"Error: Unknown content_type '{ct}'. Use: product, campaign, video, or storyboard."

    return json.dumps({
        "content_type":   ct,
        "polished_prompt": polished,
        "word_count":     len(polished.split()),
        "usage":          f"Use this as the main prompt in {tool_hint}",
    }, indent=2)


if __name__ == "__main__":
    mcp.run()
