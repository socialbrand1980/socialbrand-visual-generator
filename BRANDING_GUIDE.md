# Socialbrand 1980 — MCP Branding Guide

Panduan lengkap untuk integrate Socialbrand 1980 branding ke Socialbrand Visual Generator MCP.

---

## 📋 Branding Assets Needed

### 1. Logo Files (Multiple Formats)

Save logo kamu dalam formats ini:

| Format | Size | Purpose | Filename |
|--------|------|---------|----------|
| **PNG** | 1000x400px | README & docs | `logo.png` |
| **PNG (square)** | 400x400px | GitHub avatar | `logo-square.png` |
| **SVG** | Vector | Web (scalable) | `logo.svg` |
| **Favicon** | 32x32px | Browser tab | `favicon.ico` |

**Folder:** Create `/assets/` folder:
```
socialbrand-visual-generator/
├── assets/
│   ├── logo.png              (1000x400px)
│   ├── logo-square.png       (400x400px)
│   ├── logo.svg              (vector)
│   ├── favicon.ico           (32x32px)
│   └── colors.md             (brand colors reference)
```

---

## 🎨 Where to Use Logo

### 1. GitHub Repository Avatar

1. Go ke repository → Settings
2. Click repo avatar area
3. Upload `logo-square.png` (400x400px)
4. Save

**Result:** Logo muncul di GitHub repo header

### 2. README.md Header

Add di top of README.md:

```markdown
<div align="center">
  <img src="assets/logo.png" alt="Socialbrand Visual Generator" width="600">
  
  **Your Dynamic Digital Partner**
  
  MCP server untuk automated visual content generation powered by fal.ai
  
  ![Version](https://img.shields.io/badge/version-1.0.0-blue)
  ![Python](https://img.shields.io/badge/python-3.12%2B-blue)
  ![License](https://img.shields.io/badge/license-MIT-green)
</div>
```

**Result:** Professional header dengan logo

### 3. Documentation (Markdown Files)

Add logo di setiap main documentation file:

```markdown
# [Document Title]

<img src="../assets/logo-square.png" alt="Socialbrand" width="100" align="right">

Content...
```

### 4. PDF Guide Header

Update `generate_guide.py` untuk include logo di PDF cover page:

```python
# Dalam generate_guide.py - updatecover page section:
doc.add_image("assets/logo.png", width=4*inch)
```

Nanti saya update script-nya.

---

## 🎨 Brand Colors Reference

Create `/assets/colors.md`:

```markdown
# Socialbrand 1980 — Brand Colors

## Primary Colors
- **Brand Blue:** #2563EB (logo background)
- **White:** #FFFFFF (text on blue)

## Secondary Colors
- **Light Blue:** #3B82F6 (accents, hover states)
- **Dark Blue:** #1E40AF (dark mode, borders)

## Neutral Colors
- **Dark Gray:** #1F2937 (text)
- **Light Gray:** #F3F4F6 (backgrounds)

## Usage
- Brand Blue: Primary backgrounds, strong CTAs
- White: Primary text on dark backgrounds
- Light Blue: Secondary buttons, hover states
- Gray: Supporting text, borders, dividers

## Hex Codes for Development
```
PRIMARY_BLUE = #2563EB
LIGHT_BLUE = #3B82F6
DARK_BLUE = #1E40AF
WHITE = #FFFFFF
DARK_GRAY = #1F2937
LIGHT_GRAY = #F3F4F6
```
```

---

## 📝 Update README with Logo

Here's template untuk di-replace di README.md:

```markdown
<div align="center">
  <img src="assets/logo.png" alt="Socialbrand Visual Generator" width="500" margin="0 auto">
  
  # Socialbrand Visual Generator
  
  ### Your Dynamic Digital Partner
  
  MCP (Model Context Protocol) server untuk **automated visual content generation** di Claude Desktop. 
  
  Generate product photos, campaign visuals, product videos, dan storyboard frames untuk brand Anda—semuanya powered by fal.ai.

  ![Version](https://img.shields.io/badge/version-1.0.0-blue)
  ![Python](https://img.shields.io/badge/python-3.12%2B-blue)
  ![License](https://img.shields.io/badge/license-MIT-green)
  ![Socialbrand](https://img.shields.io/badge/by-Socialbrand%201980-blue)

  [Features](#features) • [Installation](#quick-start) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

---

## ✨ Features
[rest of content...]
```

---

## 🌐 GitHub Profile Integration

Optional: Add link ke Socialbrand profile:

```markdown
### Made by Socialbrand 1980

**Strategic Digital Agency**

[Website](https://socialbrand1980.com) • [Instagram](https://instagram.com/socialbrand1980) • [Email](mailto:hello@socialbrand1980.com)

---
```

---

## 📊 Favicon Setup (Optional)

Add favicon untuk browser tab:

1. Create `favicon.ico` (32x32px)
2. Add ke `assets/` folder
3. Add line ke top of HTML docs (if applicable):

```html
<link rel="icon" type="image/x-icon" href="assets/favicon.ico">
```

---

## 🎯 Social Media Card (OG Tags)

For better sharing on social media, add to README:

```markdown
<!-- Social Media Preview Tags -->
<meta property="og:title" content="Socialbrand Visual Generator">
<meta property="og:description" content="MCP server untuk automated visual content generation powered by fal.ai">
<meta property="og:image" content="https://raw.githubusercontent.com/YOUR_USERNAME/socialbrand-visual-generator/main/assets/logo.png">
<meta property="og:url" content="https://github.com/YOUR_USERNAME/socialbrand-visual-generator">
```

---

## 📦 .gitignore Update

Make sure logo files ARE committed (add ke .gitignore exceptions):

```bash
# assets/ folder SHOULD be committed
# Only exclude generated files, not logos
# Current .gitignore is correct - includes assets/
```

---

## 🚀 Implementation Steps

### Step 1: Prepare Logo Files

```bash
# Create assets folder
mkdir -p assets

# Copy logo files:
cp /path/to/logo.png assets/logo.png              (1000x400px)
cp /path/to/logo-square.png assets/logo-square.png  (400x400px)
cp /path/to/logo.svg assets/logo.svg              (vector)
cp /path/to/favicon.ico assets/favicon.ico        (32x32px)
```

### Step 2: Update README.md

Add logo section di top (sebelum description).

### Step 3: Update GitHub Settings

1. Repo Settings
2. Upload square logo as repo avatar
3. Save

### Step 4: Commit Changes

```bash
git add assets/
git commit -m "Add Socialbrand 1980 branding assets (logo, colors)"
git push origin main
```

### Step 5: (Optional) Update PDF

If want logo di PDF guide juga:
- Update `generate_guide.py` untuk include logo
- Regenerate PDF
- Commit

---

## 🎨 Brand Guidelines Document

Create `/assets/BRAND_GUIDELINES.md`:

```markdown
# Socialbrand 1980 — Brand Guidelines

## Logo Usage

### Primary Logo
Use full logo (`logo.png`) di:
- Website header
- GitHub repositories
- Documentation
- Marketing materials
- Email signature

### Square Logo
Use square version (`logo-square.png`) di:
- Social media profiles
- GitHub repository avatar
- Favicon
- Small spaces where horizontal doesn't fit

### Minimum Size
- Horizontal: 200px wide minimum
- Square: 100px minimum
- Do not scale below minimum sizes

### Clear Space
- Maintain 20px clear space around logo
- Don't crop or modify logo shape
- Keep white space for readability

## Colors

### Primary Brand Color
- Hex: #2563EB
- RGB: 37, 99, 235
- Usage: Headers, CTAs, primary buttons

### Supporting Colors
- White: #FFFFFF
- Light Blue: #3B82F6
- Dark Blue: #1E40AF
- Gray: #1F2937

## Typography

- Primary: Sans-serif (Helvetica, Poppins)
- Headline: Bold, modern
- Body: Regular weight, high readability

## Tone of Voice

- Professional but approachable
- Modern & innovative
- Client-focused
- Action-oriented

## Contact

For branding questions: hello@socialbrand1980.com
```

---

## 📋 Checklist

- [ ] Create `assets/` folder
- [ ] Save logo.png (1000x400px)
- [ ] Save logo-square.png (400x400px)
- [ ] Save logo.svg (vector)
- [ ] Save favicon.ico (32x32px)
- [ ] Update README.md dengan logo
- [ ] Upload square logo ke GitHub Settings
- [ ] Create `assets/BRAND_GUIDELINES.md`
- [ ] Commit all branding files
- [ ] Push to GitHub
- [ ] Verify logo shows on GitHub

---

## 🔗 Final Result

After implementation, kamu akan have:

✅ Professional GitHub repository dengan logo
✅ Branded documentation
✅ Clear brand identity
✅ Consistent visual presence
✅ Social media-ready sharing

---

## Examples

### GitHub Repository Header
```
[Logo] Socialbrand Visual Generator
       Your Dynamic Digital Partner
       ⭐ Stars | 📦 Releases | 📖 Docs
```

### README Top
```
[Full Logo Image]

# Socialbrand Visual Generator

MCP server untuk automated visual content generation...
```

### Social Media Share
```
Image: [Logo Square]
Title: Socialbrand Visual Generator
Description: MCP server for AI-powered visual content generation
Link: github.com/...
```

---

## Support

Questions about branding integration?
- Email: hello@socialbrand1980.com
- Check: BRAND_GUIDELINES.md (once created)

---

**Ready to brand your MCP? Lanjut! 🚀**
