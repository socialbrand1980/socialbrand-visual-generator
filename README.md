# Socialbrand Visual Generator

Socialbrand 1980 MCP (Model Context Protocol) server untuk **automated visual content generation** di Claude Desktop. Generate product photos, campaign visuals, product videos, dan storyboard frames untuk brand Anda—semuanya powered by fal.ai.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Fitur Utama

✨ **8 Powerful Tools:**
- 📸 **Product Photo Generator** — Clean studio shots dari raw product images
- 🎨 **Campaign Photo Generator** — Ad/social media visuals dengan mood & platform specificity
- 🎬 **Product Video Generator** — MP4 videos untuk Instagram Reels, TikTok, YouTube Shorts
- 📋 **Storyboard Frame Generator** — Text-to-image untuk campaign planning
- 📊 **Model Selection** — Access ke FLUX, SDXL, Seedance, Kling, PixVerse, Nano Banana, Recraft, Ideogram
- 🔍 **Brand Context Extraction** — Otomatis parse brand guidelines dari markdown
- 💡 **Smart Prompt Enhancement** — Polish kasar ide jadi optimal AI prompts
- 📚 **Model Discovery** — Live access ke fal.ai model catalog

## Quick Start

### 1. Install MCP Server

```bash
git clone https://github.com/yourusername/socialbrand-visual-generator.git
cd socialbrand-visual-generator
pip install -r mcp/requirements.txt
```

### 2. Setup API Key

```bash
cd mcp
cp .env.example .env
# Edit .env dan masukkan FAL_API_KEY=your_key_here
```

Dapatkan API key gratis di [fal.ai](https://fal.ai).

### 3. Integrate ke Claude Desktop

**macOS:**
```json
// ~/Library/Application Support/Claude/claude_desktop_config.json
{
  "mcpServers": {
    "socialbrand-visual-generator": {
      "command": "python",
      "args": ["/path/to/mcp/server.py"]
    }
  }
}
```

**Windows/Linux:** Edit `%APPDATA%\Claude\claude_desktop_config.json` atau `~/.config/Claude/claude_desktop_config.json` dengan format yang sama.

### 4. Restart Claude Desktop

Tools akan tersedia sekarang!

## Basic Usage

### Setup Brand Baru

```bash
cp -r brands/_template brands/my-brand
cd brands/my-brand
# Edit brand-info.md dengan brand guidelines
# Upload raw photos ke raw/ folder
```

### Generate Product Photo

```
Dalam Claude Desktop:
"Generate product photo untuk brand my-brand,
foto: photo.jpg,
style: clean white background"
```

### Generate Campaign Visual

```
"Generate campaign photo untuk brand my-brand,
produk: luxury skincare serum,
mood: luxurious,
platform: Instagram Feed"
```

### Generate Video

```
"Generate video untuk brand my-brand,
foto: photo.jpg,
produk: skincare bottle,
motion: botol berputar dengan cahaya,
platform: Instagram Reels,
durasi: 5 detik"
```

**Lebih banyak contoh?** Lihat [Comprehensive Guide](docs/Socialbrand_Visual_Generator_Guide.pdf) (29 pages).

## Folder Structure

```
socialbrand-visual-generator/
├── mcp/
│   ├── server.py              # MCP server
│   ├── requirements.txt        # Dependencies
│   └── .env.example           # Environment template
├── brands/
│   ├── _template/             # Brand template
│   │   ├── raw/               # Raw product photos
│   │   ├── moodboard/         # Reference images
│   │   ├── generated/
│   │   │   ├── product/       # Generated product photos
│   │   │   ├── campaign/      # Generated campaign visuals
│   │   │   ├── video/         # Generated videos (MP4)
│   │   │   └── storyboard/    # Generated storyboard frames
│   │   └── brand-info.md      # Brand guidelines
│   └── [brand-name]/          # Brand instances
└── docs/
    ├── Socialbrand_Visual_Generator_Guide.pdf
    ├── INSTALLATION.md
    └── FAQ.md
```

## Available Models

### Image-to-Image
- FLUX Dev (balanced, default)
- FLUX Pro (premium quality)
- FLUX Realism (photorealistic)
- SDXL (fast alternative)

### Image-to-Video
- Seedance Pro (cinematic, best quality)
- Kling 1.6 (reliable, smooth)
- PixVerse (stylized effects)

### Text-to-Image
- FLUX Dev (creative detail)
- Nano Banana (state-of-the-art)
- Recraft V3 (brand consistency)
- Ideogram (typography)

Use `list_available_models` dalam Claude untuk full catalog.

## Documentation

| Resource | Content |
|----------|---------|
| **README.md** | Installation & quick start |
| **Comprehensive Guide** | Full workflows & best practices (29 pages) |
| **INSTALLATION.md** | Advanced setup & troubleshooting |
| **FAQ.md** | Common questions |

## Environment Setup

```env
# mcp/.env
FAL_API_KEY=your_fal_api_key_here
```

## Support

- 📖 **Documentation:** [Comprehensive Guide](docs/Socialbrand_Visual_Generator_Guide.pdf)
- 🐛 **Issues:** [GitHub Issues](https://github.com/yourusername/socialbrand-visual-generator/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/yourusername/socialbrand-visual-generator/discussions)

## License

MIT License — See [LICENSE](LICENSE) for details.

## Made by

**Socialbrand 1980** — Strategic Digital Agency  
[Instagram](https://instagram.com/socialbrand1980)

