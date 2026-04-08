# Changelog

Semua perubahan penting di project ini dokumentasikan di file ini.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
dan project ini follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-04-08

### Added
- **MCP Server** — Model Context Protocol server integration dengan Claude Desktop
- **8 Core Tools:**
  - `list_brands` — List semua brand + asset counts
  - `get_brand_info` — Extract brand guidelines from markdown
  - `list_available_models` — Discover fal.ai models catalog
  - `polish_prompt` — Optimize AI prompts dengan smart enhancements
  - `generate_product_photo` — Clean studio shots (image-to-image)
  - `generate_campaign_photo` — Campaign/ad visuals (image-to-image)
  - `generate_video_from_image` — Product videos (image-to-video)
  - `generate_storyboard_frame` — Storyboard frames (text-to-image)

- **Image-to-Image Models:**
  - FLUX Dev (balanced quality, default)
  - FLUX Pro (premium quality)
  - FLUX Realism (photorealistic)
  - SDXL (fast alternative)

- **Image-to-Video Models:**
  - Seedance Pro (cinematic, default)
  - Seedance Lite (faster generation)
  - Kling 1.6 (reliable, smooth motion)
  - PixVerse v3.5 (stylized, anime/3D support)

- **Text-to-Image Models:**
  - FLUX Dev (creative detail, default)
  - FLUX Pro (premium quality)
  - FLUX Schnell (fastest generation)
  - Nano Banana (Google's state-of-the-art)
  - Recraft V3 (brand consistency)
  - Ideogram V2 (typography & graphic design)

- **Documentation:**
  - Comprehensive 29-page PDF guide with workflows
  - Detailed installation guide (macOS, Windows, Linux)
  - FAQ & troubleshooting guide
  - Contributing guidelines
  - CLAUDE.md workspace guide

- **Brand System:**
  - Brand template with folder structure
  - Brand guidelines (brand-info.md) support
  - Automatic asset organization (raw, moodboard, generated)
  - Support untuk multiple brands

- **Features:**
  - Flexible model selection (user-configurable)
  - Brand context extraction dari markdown files
  - Async/await API polling untuk long-running tasks
  - Error handling & validation
  - Environment variable configuration

- **Configuration:**
  - .env.example template
  - Configurable API endpoint
  - Customizable request timeouts
  - Debug logging support

### Documentation
- README.md dengan quick start
- INSTALLATION.md dengan platform-specific guides
- CONTRIBUTING.md untuk developers
- LICENSE (MIT)
- CHANGELOG.md (this file)
- Complete 29-page professional PDF guide

### Repository
- .gitignore untuk Python & secrets
- GitHub-ready structure
- MIT License
- Contributing guidelines

### Tested With
- Python 3.12+
- Claude Desktop (latest)
- fal.ai API (production)

---

## Planned Features (Roadmap)

### [1.1.0] - Q2 2026
- [ ] Batch generation support (multiple images/videos in one run)
- [ ] Advanced color grading options
- [ ] Asset organization dashboard
- [ ] Performance metrics & analytics
- [ ] Extended workflow examples (5+ brand types)

### [1.2.0] - Q3 2026
- [ ] Web dashboard untuk manage brands
- [ ] Video editing tools (cuts, transitions, effects)
- [ ] Custom model fine-tuning support
- [ ] Integration dengan social media scheduling platforms
- [ ] Advanced prompt templates library

### [2.0.0] - Q4 2026
- [ ] Team collaboration features
- [ ] Asset version control & history
- [ ] Multi-user project management
- [ ] Advanced analytics & performance tracking
- [ ] API endpoint untuk programmatic access
- [ ] Custom model training support

---

## Version History

### [1.0.0] - 2026-04-08
**Initial Public Release**

Core MCP server dengan 8 tools, 4 image-to-image models, 4 image-to-video models, 6 text-to-image models. Comprehensive documentation, platform-specific installation guides, dan brand management system.

- ✅ Production-ready
- ✅ Fully documented
- ✅ MIT Licensed
- ✅ Community-friendly (Contributing guide)

**Contributors:**
- Jhordi (Socialbrand 1980) — Creator & Maintainer
- Claude (Anthropic) — MCP framework & documentation

---

## How to Report Issues

Found a bug atau issue? Open di [GitHub Issues](https://github.com/yourusername/socialbrand-visual-generator/issues):

1. Check existing issues first
2. Use clear, descriptive title
3. Include steps to reproduce
4. Share your environment (OS, Python version, Claude version)
5. Add relevant logs atau screenshots

---

## How to Request Features

Have an idea? Share di [GitHub Discussions](https://github.com/yourusername/socialbrand-visual-generator/discussions):

1. Describe feature & use case
2. Explain why it would be valuable
3. Propose how it might work
4. Vote existing feature requests

---

## Release Process

Versions follow [Semantic Versioning](https://semver.org/):
- **MAJOR** (X.0.0) — Breaking changes
- **MINOR** (1.Y.0) — New features (backward compatible)
- **PATCH** (1.0.Z) — Bug fixes

Releases:
1. Update version di relevant files
2. Add CHANGELOG entry
3. Create git tag
4. Push to GitHub
5. Publish release notes

---

## Credits

Made dengan ❤️ oleh **Socialbrand 1980** — Strategic Digital Agency

Special thanks:
- **fal.ai** — Amazing image & video generation API
- **Anthropic** — Claude & MCP framework
- **Community** — Feedback, ideas, & contributions

---

## License

All code & documentation under MIT License. See [LICENSE](LICENSE) for details.

---

**Latest Update:** 2026-04-08  
**Current Version:** 1.0.0  
**Status:** ✅ Production Ready
