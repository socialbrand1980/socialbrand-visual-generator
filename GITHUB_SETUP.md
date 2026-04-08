# GitHub Setup & Distribution Guide

Panduan lengkap untuk upload Socialbrand Visual Generator ke GitHub dan bikin available untuk public installation.

## Step 1: Create GitHub Repository

### 1a. Create GitHub Account (if needed)
- Go to [github.com](https://github.com)
- Sign up atau login
- Verify email

### 1b. Create New Repository

1. Click "+" icon (top right) → "New repository"
2. Fill details:

```
Repository name: socialbrand-visual-generator
Description: MCP server untuk automated visual content generation powered by fal.ai
Visibility: Public (untuk community access)
```

3. **Initialize with:**
   - ❌ No README (kita punya sendiri)
   - ❌ No .gitignore (kita punya sendiri)
   - ❌ No license (kita punya sendiri)

4. Click "Create repository"

### 1c. Get Repository URL

Setelah create, GitHub akan show:

```bash
git remote add origin https://github.com/YOUR_USERNAME/socialbrand-visual-generator.git
git branch -M main
git push -u origin main
```

Save informasi ini — kita butuh di Step 3.

---

## Step 2: Prepare Local Repository

### 2a. Initialize Git (if not already)

```bash
cd /path/to/socialbrand-visual-generator
git init
```

### 2b. Verify File Structure

Pastikan semua files ada:

```
socialbrand-visual-generator/
├── README.md                          ✅
├── INSTALLATION.md                    ✅
├── CONTRIBUTING.md                    ✅
├── GITHUB_SETUP.md                    ✅ (this file)
├── CHANGELOG.md                       ✅
├── LICENSE                            ✅
├── .gitignore                         ✅
│
├── mcp/
│   ├── server.py                      ✅
│   ├── requirements.txt               ✅
│   └── .env.example                   ✅
│
├── brands/
│   ├── _template/                     ✅
│   │   ├── raw/
│   │   ├── moodboard/
│   │   ├── generated/
│   │   │   ├── product/
│   │   │   ├── campaign/
│   │   │   ├── video/
│   │   │   └── storyboard/
│   │   └── brand-info.md
│   │
│   └── [existing-brands]/             ✅
│
└── docs/
    ├── Socialbrand_Visual_Generator_Guide.pdf  ✅
    ├── FAQ.md                         (create next)
    └── DEPLOYMENT.md                  (create next)
```

### 2c. Create Missing Files (Optional but Recommended)

Create `/docs/FAQ.md`:

```markdown
# Frequently Asked Questions

## Installation

### Q: Can I use on Windows?
A: Yes! See INSTALLATION.md for Windows-specific steps.

### Q: Do I need paid fal.ai account?
A: No, free tier includes 100 images/month and 10 videos/month.

## Usage

### Q: How long does generation take?
A: Product photos: ~30 seconds. Videos: 30-90 seconds.

### Q: Can I use custom models?
A: Yes! list_available_models shows all available models.

### Q: How do I update brand info?
A: Edit brand-info.md in your brand folder.

## Troubleshooting

### Q: MCP tools not appearing in Claude
A: Check claude_desktop_config.json path and restart Claude.

### Q: API key errors
A: Verify .env file in mcp/ folder (not root).

### Q: Model generation fails
A: Check fal.ai account status and API key validity.
```

### 2d. Create `.github/workflows/ci.yml` (Optional)

Create `/path/to/socialbrand-visual-generator/.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - run: pip install black flake8
      - run: black --check mcp/
      - run: flake8 mcp/ --max-line-length=100
```

This automatically checks code quality on every push.

---

## Step 3: Push to GitHub

### 3a. Stage Files

```bash
cd /path/to/socialbrand-visual-generator
git add .
```

Verify staged files:
```bash
git status
```

### 3b. Initial Commit

```bash
git commit -m "Initial commit: Socialbrand Visual Generator v1.0.0

- MCP server with 8 tools for visual content generation
- Support for product photos, campaign visuals, videos, storyboards
- Flexible model selection (FLUX, Seedance, Kling, PixVerse, etc.)
- Comprehensive documentation & installation guides
- MIT License
"
```

### 3c. Add GitHub Remote

Replace `YOUR_USERNAME` dengan GitHub username kamu:

```bash
git remote add origin https://github.com/YOUR_USERNAME/socialbrand-visual-generator.git
git branch -M main
```

### 3d. Push to GitHub

```bash
git push -u origin main
```

If prompt untuk credentials:
- macOS/Linux: Use personal access token (not password)
- Windows: Use GitHub CLI or personal access token

**Create Personal Access Token (if needed):**
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token
3. Select `repo` scope
4. Copy token → paste when git prompts

---

## Step 4: GitHub Repository Settings

### 4a. Add Repository Description

1. Go ke repository page
2. Click "⚙️ Settings" (repository settings, not account)
3. Edit "Description" → "Socialbrand Visual Generator - MCP for AI visual content"
4. Edit "Website" → https://socialbrand1980.com (if applicable)
5. Save

### 4b. Add Topics

Settings → Topics → Add:
- `mcp`
- `claude`
- `anthropic`
- `image-generation`
- `video-generation`
- `fal-ai`
- `ai-tools`
- `content-generation`

### 4c. Enable Discussions

1. Settings → Features
2. Check "Discussions" ✅
3. Save

### 4d. Setup Branch Protection (Optional)

1. Settings → Branches
2. Add rule untuk `main`:
   - Require pull request reviews ✅
   - Require status checks to pass ✅
   - Require branches to be up to date ✅

---

## Step 5: Create Release

### 5a. Create GitHub Release

1. Go ke Code tab
2. Click "Releases" (right sidebar)
3. Click "Create a new release"
4. Fill:

```
Tag version: v1.0.0
Release title: Socialbrand Visual Generator v1.0.0
Description: 

## ✨ Initial Release

Socialbrand Visual Generator - MCP server for automated visual content generation.

### Features
- 8 tools for product photos, campaign visuals, videos, storyboards
- Flexible model selection (FLUX, SDXL, Seedance, Kling, PixVerse, Nano Banana, Recraft, Ideogram)
- Brand context extraction from markdown
- Comprehensive documentation & installation guides

### Getting Started
1. Clone: git clone https://github.com/YOUR_USERNAME/socialbrand-visual-generator.git
2. Install: pip install -r mcp/requirements.txt
3. Setup: cp mcp/.env.example mcp/.env
4. Integrate: Add to claude_desktop_config.json
5. Generate: Use in Claude Desktop!

### Documentation
- [README](README.md) - Quick start
- [Installation Guide](INSTALLATION.md) - Platform-specific setup
- [Comprehensive Guide](docs/Socialbrand_Visual_Generator_Guide.pdf) - Full workflows
- [FAQ](docs/FAQ.md) - Common questions

### Contributors
- Jhordi (Socialbrand 1980)
```

5. Click "Publish release"

---

## Step 6: Documentation Checklist

Pastikan semua docs siap:

- ✅ **README.md** — Quick start & overview
- ✅ **INSTALLATION.md** — Step-by-step installation
- ✅ **CONTRIBUTING.md** — How to contribute
- ✅ **CHANGELOG.md** — Version history
- ✅ **LICENSE** — MIT License
- ✅ **docs/Socialbrand_Visual_Generator_Guide.pdf** — Full guide (29 pages)
- ✅ **docs/FAQ.md** — Common questions
- ✅ **.gitignore** — What not to commit
- ✅ **.env.example** — Configuration template

---

## Step 7: Share & Promote

### 7a. Update Personal Links

Update di:
- Portfolio/website
- LinkedIn profile
- Twitter/X
- Instagram
- Email signature

Example:
```
🔧 New: Socialbrand Visual Generator - MCP for Claude Desktop
Generate product photos, campaign visuals, videos, & storyboards powered by fal.ai
→ https://github.com/YOUR_USERNAME/socialbrand-visual-generator
```

### 7b. Create Launch Post

Share announcement:
- What problem it solves
- Key features
- How to get started
- Link ke GitHub

### 7c. Submit to GitHub Trending

Create file `/docs/PROMOTION.md` with:

```markdown
# How This Project Helps

## Problem Solved
- Automating visual content creation untuk brands
- Using AI untuk generate product photos, campaign visuals, videos
- Managing brand consistency across multiple content formats
- Reducing time & cost untuk content production

## Target Audience
- Digital agencies
- Brand marketers
- E-commerce businesses
- Content creators
- SMBs looking untuk AI-powered content generation

## Key Features
1. Flexible model selection (FLUX, SDXL, Seedance, etc.)
2. Brand context extraction
3. Multiple content formats (photos, videos, storyboards)
4. Easy integration dengan Claude Desktop
5. Comprehensive documentation

## Tech Stack
- Python 3.12+
- MCP (Model Context Protocol)
- fal.ai API
- Claude AI

## Installation
One-command setup para sa most users.
```

---

## Step 8: Ongoing Maintenance

### 8a. Regular Updates

```bash
# When adding features atau fixes:
git add .
git commit -m "Description of changes"
git push origin main

# Create release tag:
git tag v1.1.0
git push origin v1.1.0
```

### 8b. Monitor Issues & Discussions

1. Check GitHub Issues regularly
2. Respond to pull requests
3. Answer questions in Discussions
4. Update documentation based pada user feedback

### 8c. Update CHANGELOG

Every release:
1. Update CHANGELOG.md dengan new features
2. Commit dengan message "Release v1.x.x"
3. Create GitHub release

---

## Advanced: Setup Distribution

### Option A: pip Package (Future)

For future releases, kamu bisa publish ke PyPI:

```bash
# Create setup.py
python -m pip install setuptools wheel
python setup.py bdist_wheel
python -m twine upload dist/*
```

Then users bisa: `pip install socialbrand-visual-generator`

### Option B: Conda Package (Future)

Para sa scientific community users.

### Option C: Direct Installation (Now)

Current users install dengan:
```bash
git clone https://github.com/YOUR_USERNAME/socialbrand-visual-generator.git
pip install -r mcp/requirements.txt
```

---

## Troubleshooting GitHub

### Issue: Commits show as "unknown author"

```bash
# Configure git globally
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Issue: Can't push (authentication)

**Option 1: Personal Access Token**
- GitHub → Settings → Developer settings → Personal access tokens
- Generate token dengan `repo` scope
- Use token as password when pushing

**Option 2: SSH Key**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add ke GitHub → Settings → SSH Keys
cat ~/.ssh/id_ed25519.pub
```

### Issue: Large files rejected

GitHub has 100MB file limit. Jika ada large files:
```bash
# Use .gitignore untuk exclude
# Atau use Git LFS para large files
git lfs install
git lfs track "*.mp4"
```

---

## Checklist for Launch

- [ ] Repository created & configured
- [ ] All files pushed to GitHub
- [ ] README has clear instructions
- [ ] INSTALLATION.md covers all platforms
- [ ] License file present (MIT)
- [ ] CONTRIBUTING.md encouraging
- [ ] First release created & tagged
- [ ] Topics added untuk discoverability
- [ ] Discussions enabled
- [ ] Links updated di social/website
- [ ] Launch announcement posted

---

## After Launch

1. **Monitor:** Check GitHub Issues & Discussions daily (first week)
2. **Respond:** Reply to questions & bug reports quickly
3. **Improve:** Fix bugs, address feedback
4. **Document:** Update docs based pada user questions
5. **Release:** Create releases regularly untuk improvements

---

## Questions?

- 📖 Read GitHub's MCP documentation
- 💬 Use GitHub Discussions untuk Q&A
- 📧 Email: support@socialbrand1980.com
- 🐛 Report issues: GitHub Issues

---

**Ready to share dengan world? 🚀**

Next step: `git push origin main` dan enjoy!
