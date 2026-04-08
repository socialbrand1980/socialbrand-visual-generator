# Upload ke GitHub — Quick Start (5 Menit)

Kamu siap! Ini panduan cepat untuk upload Socialbrand Visual Generator ke GitHub.

---

## ⚡ Fastest Path (Command-by-Command)

### 1. Buat Repository di GitHub (2 menit)

1. Go ke [github.com](https://github.com)
2. Klik "+" (top right) → "New repository"
3. Repository name: `socialbrand-visual-generator`
4. Description: `MCP server untuk automated visual content generation powered by fal.ai`
5. Visibility: **Public**
6. **JANGAN** initialize dengan README, .gitignore, atau license (kita punya)
7. Click "Create repository"

### 2. Copy These Commands (macOS/Linux)

Setelah GitHub create repository, kamu akan lihat screen dengan commands. Copy-paste ini ke Terminal:

```bash
# Navigate ke folder kamu
cd /path/to/socialbrand-visual-generator

# Initialize git & add files
git init
git add .
git commit -m "Initial commit: Socialbrand Visual Generator v1.0.0

- MCP server dengan 8 tools
- Image-to-image, image-to-video, text-to-image support
- Flexible model selection (FLUX, SDXL, Seedance, Kling, etc.)
- Complete documentation & installation guides
- MIT License
"

# Add remote & push
git remote add origin https://github.com/YOUR_USERNAME/socialbrand-visual-generator.git
git branch -M main
git push -u origin main
```

### 3. Windows Command Prompt

```bash
cd C:\path\to\socialbrand-visual-generator
git init
git add .
git commit -m "Initial commit: Socialbrand Visual Generator v1.0.0"
git remote add origin https://github.com/YOUR_USERNAME/socialbrand-visual-generator.git
git branch -M main
git push -u origin main
```

### 4. Done! ✅

GitHub akan ask untuk credentials (use personal access token, not password).

---

## 📋 What Gets Uploaded?

```
✅ All these files:
- README.md
- INSTALLATION.md
- CONTRIBUTING.md
- CHANGELOG.md
- LICENSE (MIT)
- .gitignore
- GITHUB_SETUP.md
- GITHUB_READINESS.md
- UPLOAD_TO_GITHUB.md (this file)
- CLAUDE.md
- mcp/server.py
- mcp/requirements.txt
- mcp/.env.example
- brands/ (template + 2bShine example)
- docs/Socialbrand_Visual_Generator_Guide.pdf

❌ These are IGNORED (tidak upload):
- mcp/.env (secret API key)
- brands/*/generated/ (too large, can regenerate)
- __pycache__
- .DS_Store
- Cache files
```

---

## 🔑 Important: API Key Security

Pastikan `mcp/.env` **TIDAK** di-commit:

```bash
# This file already excludes .env (check .gitignore)
cat .gitignore | grep ".env"
# Output: .env
```

✅ Safe — API key will NOT be uploaded.

Users akan copy `.env.example` → `.env` dan add their own key.

---

## 🎯 After Upload (Next 5 Steps)

### Step 1: Create Release (1 min)

```bash
# In your local folder:
git tag v1.0.0
git push origin v1.0.0
```

Then go to GitHub → Releases → "Create a release" → Fill form → Publish.

### Step 2: Add Repository Topics (1 min)

GitHub repo page → Settings:
- Click "Topics"
- Add: `mcp`, `claude`, `anthropic`, `ai-tools`, `image-generation`, `fal-ai`

### Step 3: Enable Discussions (30 sec)

Settings → Features → Check "Discussions" ✅

### Step 4: Update Your Links (2 min)

Update anywhere you reference Socialbrand:
- Portfolio
- LinkedIn
- Instagram
- Website
- Email signature

Add: [GitHub link] or "Now available on GitHub!"

### Step 5: Announce! (2 min)

Post somewhere:

```
🔧 New Release: Socialbrand Visual Generator

Generate product photos, campaign visuals, product videos, 
and storyboard frames using Claude + fal.ai AI models.

✨ Features:
- 8 MCP tools
- 14 supported AI models
- Complete documentation
- Easy 5-minute setup

📖 Get started:
github.com/YOUR_USERNAME/socialbrand-visual-generator

#AI #ContentCreation #MCP #Claude
```

---

## ❓ Common Issues

### GitHub Says "Nothing to commit"

```bash
# Make sure you're in right folder
pwd  # Should show .../socialbrand-visual-generator

# Check git status
git status

# If empty, files might not exist
ls -la README.md  # Should exist
```

### "fatal: not a git repository"

```bash
# Run this first
git init

# Then try again
git add .
git commit -m "..."
```

### "Permission denied" atau "Authentication failed"

**Use Personal Access Token:**
1. GitHub → Settings → Developer settings → Personal access tokens → Generate new
2. Select `repo` scope only
3. Copy token
4. When git asks for password, paste token instead

**Or use SSH:**
```bash
# Generate key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to GitHub (Settings → SSH Keys)
cat ~/.ssh/id_ed25519.pub  # Copy output

# Clone repo using SSH URL instead:
git remote add origin git@github.com:YOUR_USERNAME/socialbrand-visual-generator.git
```

### "branch -M main" error

```bash
# Just use default branch:
git push -u origin master  # atau wapever your default is
```

---

## 📚 Full Documentation

Want more details? Read:
- **GITHUB_SETUP.md** — Complete step-by-step guide
- **INSTALLATION.md** — Installation for users
- **CONTRIBUTING.md** — For developers

---

## ✅ Checklist

- [ ] GitHub account created
- [ ] Repository created on GitHub
- [ ] `git` installed on computer
- [ ] `mcp/.env` file DELETED (leave only .env.example)
- [ ] Commands copy-pasted & executed
- [ ] Push successful (check GitHub website)
- [ ] Release created
- [ ] Topics added
- [ ] Discussions enabled
- [ ] Links updated
- [ ] Announcement posted

---

## 🎉 You're Done!

Socialbrand Visual Generator sekarang available untuk public installation:

```
https://github.com/YOUR_USERNAME/socialbrand-visual-generator
```

Users bisa:
1. Clone repository
2. Install dependencies
3. Add API key
4. Integrate dengan Claude Desktop
5. Start generating!

---

## Quick Stats

**What You Have:**
- 1 MCP Server (fully functional)
- 8 Tools (all working)
- 14 AI Models (flexible selection)
- 9 Documentation Files
- 1 PDF Guide (29 pages, professional)
- 2+ Brand Examples
- Complete Installation Guides
- Contributing Guidelines
- MIT License

**Distribution:** Ready untuk production use
**Time to Setup:** 5-10 minutes for most users
**Cost:** Free tier sufficient untuk many use cases

---

## Need Help?

- **Installation issues?** → Read INSTALLATION.md
- **Integration issues?** → Check FAQ in PDF guide
- **Contributing?** → Read CONTRIBUTING.md
- **Questions?** → Use GitHub Discussions (after upload)

---

**Sekarang: Run commands di atas, dan done!** 🚀

```bash
cd /path/to/socialbrand-visual-generator
git init
git add .
git commit -m "Initial commit: Socialbrand Visual Generator v1.0.0"
git remote add origin https://github.com/YOUR_USERNAME/socialbrand-visual-generator.git
git branch -M main
git push -u origin main
```

**Enjoy! 🎨📸🎬**
