# Creative-P — Workspace Guide
## Socialbrand 1980 | Strategic Digital Agency

Ini adalah working directory utama untuk **visual content generation** dan **campaign planning** Socialbrand 1980.

---

## Siapa yang Pakai Ini

**Owner:** Jhordi (Socialbrand 1980)
**Use case:** Generate foto produk, campaign visual, product video, dan storyboard untuk client brands menggunakan AI.

---

## Struktur Folder

```
Creative-P/
├── brands/
│   ├── _template/              ← Template kosong untuk brand baru
│   │   ├── raw/                ← Foto produk mentah dari client
│   │   ├── moodboard/          ← Referensi visual & brand mood
│   │   ├── generated/
│   │   │   ├── product/        ← Clean product photos (img2img)
│   │   │   ├── campaign/       ← Campaign/ad photos (img2img)
│   │   │   ├── video/          ← Product videos MP4 (img2video)
│   │   │   └── storyboard/     ← Storyboard frames (text2img)
│   │   └── brand-info.md       ← Brand guidelines & visual identity
│   │
│   └── [nama-brand]/           ← Satu folder per brand client
│
├── mcp/
│   ├── server.py               ← MCP server (fal.ai integration)
│   ├── .env                    ← API key fal.ai (jangan di-share)
│   └── requirements.txt        ← Python dependencies
│
└── CLAUDE.md                   ← File ini
```

---

## MCP: Socialbrand Visual Generator

MCP sudah terpasang dan terconnect. Ada **8 tools** yang bisa dipakai langsung:

| Tool | Fungsi | Output |
|------|--------|--------|
| `list_brands` | Lihat semua brand + asset count | Info |
| `get_brand_info` | Baca brand-info.md suatu brand | Info |
| `list_available_models` | Lihat semua model fal.ai yang bisa dipakai | Info |
| `polish_prompt` | Ubah ide kasar jadi prompt optimal | Info |
| `generate_product_photo` | Clean studio shot dari foto mentah | JPG |
| `generate_campaign_photo` | Campaign/ad visual dari foto produk | JPG |
| `generate_video_from_image` | Product video dari foto produk | MP4 |
| `generate_storyboard_frame` | Storyboard frame dari deskripsi teks | JPG |

**API:** fal.ai — key tersimpan di `mcp/.env`

---

## Model yang Tersedia

### Image-to-Image (untuk product & campaign photo)
| Model ID | Keterangan |
|----------|-----------|
| `fal-ai/flux/dev/image-to-image` | FLUX Dev — fast & balanced **(default)** |
| `fal-ai/flux/pro/image-to-image` | FLUX Pro — higher quality, slower |
| `fal-ai/flux-realism/image-to-image` | FLUX Realism — photorealistic |
| `fal-ai/flux/schnell/image-to-image` | FLUX Schnell — fastest, untuk draft |
| `fal-ai/sdxl/image-to-image` | SDXL — alternatif |

### Image-to-Video (untuk generate product video)
| Model ID | Keterangan |
|----------|-----------|
| `fal-ai/bytedance/seedance/v1/pro/image-to-video` | Seedance 1.0 Pro — cinematic, best quality **(default)** |
| `fal-ai/bytedance/seedance/v1/lite/image-to-video` | Seedance 1.0 Lite — faster |
| `fal-ai/kling-video/v1.6/standard/image-to-video` | Kling 1.6 — reliable, smooth motion |
| `fal-ai/pixverse/v3.5/image-to-video` | PixVerse v3.5 — stylized, anime/3D support |

### Text-to-Image (untuk storyboard)
| Model ID | Keterangan |
|----------|-----------|
| `fal-ai/flux/dev` | FLUX Dev — detailed & creative **(default)** |
| `fal-ai/flux/pro` | FLUX Pro — premium quality |
| `fal-ai/flux/schnell` | FLUX Schnell — fastest, quick draft |
| `fal-ai/nano-banana` | Nano Banana 2 — Google's state-of-the-art |
| `fal-ai/recraft-v3` | Recraft V3 — brand & illustration |
| `fal-ai/ideogram/v2` | Ideogram V2 — typography & graphic design |

> **Tip:** Semua model field menerima string bebas — kamu bisa pass model ID fal.ai apapun, tidak terbatas list di atas. Pakai `list_available_models` dengan `search_fal: true` untuk discover model terbaru.

---

## Cara Generate Konten

### Product Photo (clean studio shot)
```
"Generate product photo untuk brand [nama],
foto: brands/[nama]/raw/[nama-file],
style: clean white / flat lay / dark moody / dll"
```

### Campaign Photo (untuk iklan)
```
"Generate campaign photo untuk brand [nama],
produk: [deskripsi produk],
mood: [vibe],
platform: Instagram Feed / Story / TikTok"
```

### Product Video (untuk Reels / TikTok)
```
"Generate video untuk brand [nama],
foto: brands/[nama]/raw/[nama-file],
produk: [deskripsi produk],
motion: [deskripsi gerakan, e.g. 'produk berputar perlahan dengan efek cahaya'],
platform: Instagram Reels / TikTok,
durasi: 5 detik,
resolusi: 720p"
```

### Storyboard Frame (dari teks, tanpa foto)
```
"Generate storyboard frame untuk brand [nama],
scene: [deskripsi scene, e.g. 'wanita mengaplikasikan serum di pagi hari, suasana bathroom bersih'],
frame type: lifestyle / product_hero / detail_closeup,
platform: Instagram Feed,
ukuran: portrait 9:16"
```

### Polish Prompt Dulu
```
"Polish prompt ini untuk [product/campaign/video/storyboard]:
[deskripsi kasar kamu]"
```

### Lihat Model yang Tersedia
```
"List model yang tersedia untuk image-to-video"
"List semua model fal.ai" (search_fal: true untuk live search)
```

---

## Brands yang Sudah Ada

| Brand | Produk | Status |
|-------|--------|--------|
| 2bShine | Brightening DNA GEL Essence | ✅ Active — campaign plan ready |

---

## Campaign Plan

Setiap brand yang aktif punya `campaign-plan.md` di folder brand-nya.

Untuk generate campaign plan baru:
```
"Buatkan campaign plan untuk brand [nama]"
```

---

## Common Tasks

| Perintah | Aksi |
|----------|------|
| "Lihat brand yang ada" | list semua brand + asset count |
| "Baca info brand X" | tampilkan brand-info.md |
| "Model apa saja yang tersedia?" | list model per kategori |
| "Generate product photo brand X" | clean studio shot |
| "Generate campaign photo brand X" | ad/social media visual |
| "Generate video brand X" | product video MP4 (Reels/TikTok) |
| "Generate storyboard brand X" | storyboard frame dari deskripsi |
| "Polish prompt ini: ..." | optimize prompt sebelum generate |
| "Buatkan campaign plan brand X" | full 4-minggu campaign strategy |
| "Tambah brand baru: [nama]" | setup folder + brand-info template |

---

## Cara Tambah Brand Baru

1. Duplikat folder `brands/_template`
2. Rename dengan nama brand (huruf kecil, tanpa spasi, contoh: `brand-abc`)
3. Isi `brand-info.md` dengan detail brand:
   - Tone & industry
   - Target audience
   - Warna, typography, photography style
   - Mood campaign
   - Platform target
4. Upload foto mentah ke `raw/`
5. Upload moodboard ke `moodboard/`
6. Siap generate

---

## Output Locations

| Content Type | Folder | Format |
|-------------|--------|--------|
| Product Photo | `generated/product/` | JPG |
| Campaign Photo | `generated/campaign/` | JPG |
| Product Video | `generated/video/` | MP4 |
| Storyboard | `generated/storyboard/` | JPG |

Naming convention otomatis: `[brand]_[type]_[platform]_[timestamp].[ext]`

---

## Tech Stack

- **Image Generation:** fal.ai (FLUX variants, SDXL)
- **Video Generation:** fal.ai (Seedance, Kling, PixVerse)
- **Storyboard:** fal.ai (FLUX, Nano Banana, Recraft, Ideogram)
- **MCP Framework:** Python FastMCP
- **Language:** Python 3.12
- **Key dependencies:** `mcp[cli]`, `httpx`, `pydantic`, `fal-client`, `python-dotenv`

> **Note:** Claude Desktop perlu di-restart setelah perubahan di `server.py` atau `.env`.
