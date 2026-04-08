# Installation Guide

Complete step-by-step installation guide untuk Socialbrand Visual Generator.

## Prerequisites

- **Python 3.12+** ([download](https://www.python.org/downloads/))
- **Claude Desktop** (latest version, [download](https://claude.ai/download))
- **fal.ai API Key** (free, [get here](https://fal.ai))
- **Git** (for cloning repository)

## Platform-Specific Installation

### macOS

#### 1. Clone Repository

```bash
# Buka Terminal
cd ~/Documents
git clone https://github.com/yourusername/socialbrand-visual-generator.git
cd socialbrand-visual-generator
```

#### 2. Install Python Dependencies

```bash
# Check Python version
python3 --version  # Should be 3.12 or higher

# Install dependencies
pip3 install -r mcp/requirements.txt
```

#### 3. Setup API Key

```bash
cd mcp
cp .env.example .env
nano .env  # Or: open -a TextEdit .env
```

Ganti `your_fal_api_key_here` dengan API key kamu dari [fal.ai](https://fal.ai).

Save file (Ctrl+O, Enter, Ctrl+X).

#### 4. Integrate ke Claude Desktop

```bash
# Edit Claude config
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Tambahkan MCP server configuration:

```json
{
  "mcpServers": {
    "socialbrand-visual-generator": {
      "command": "python3",
      "args": ["/path/to/socialbrand-visual-generator/mcp/server.py"]
    }
  }
}
```

**Replace `/path/to/` dengan absolute path ke folder kamu.** Contoh:

```bash
# Check absolute path
pwd  # e.g. /Users/jhordi/Documents/socialbrand-visual-generator

# Full path: /Users/jhordi/Documents/socialbrand-visual-generator/mcp/server.py
```

Save & exit (Cmd+O, Enter, Cmd+X).

#### 5. Restart Claude Desktop

- Close Claude Desktop completely
- Reopen Claude Desktop
- MCP tools akan tersedia dalam sidebar

---

### Windows

#### 1. Clone Repository

```bash
# Buka Command Prompt atau PowerShell
cd Documents
git clone https://github.com/yourusername/socialbrand-visual-generator.git
cd socialbrand-visual-generator
```

#### 2. Install Python Dependencies

```bash
# Check Python version
python --version  # Should be 3.12 or higher

# Install dependencies
pip install -r mcp/requirements.txt
```

Jika pip tidak recognized:
- Add Python ke PATH: [Setup Python PATH](https://docs.python.org/3/using/windows.html#configuring-python)
- Or: Use full path `C:\Python312\Scripts\pip install ...`

#### 3. Setup API Key

```bash
cd mcp
copy .env.example .env
notepad .env
```

Ganti `your_fal_api_key_here` dengan API key dari [fal.ai](https://fal.ai).

Save & close.

#### 4. Integrate ke Claude Desktop

```bash
# Edit Claude config
notepad %APPDATA%\Claude\claude_desktop_config.json
```

Tambahkan MCP server configuration:

```json
{
  "mcpServers": {
    "socialbrand-visual-generator": {
      "command": "python",
      "args": ["C:\\path\\to\\socialbrand-visual-generator\\mcp\\server.py"]
    }
  }
}
```

**Replace `C:\path\to\` dengan absolute path ke folder kamu.** Contoh:

```bash
# Check path (dalam Command Prompt)
cd socialbrand-visual-generator
cd mcp
echo %cd%  # e.g. C:\Users\jhordi\Documents\socialbrand-visual-generator\mcp
```

Full path: `C:\Users\jhordi\Documents\socialbrand-visual-generator\mcp\server.py`

Save & close.

#### 5. Restart Claude Desktop

- Close Claude Desktop completely
- Reopen Claude Desktop
- MCP tools akan tersedia

---

### Linux

#### 1. Clone Repository

```bash
# Buka Terminal
cd ~
git clone https://github.com/yourusername/socialbrand-visual-generator.git
cd socialbrand-visual-generator
```

#### 2. Install Python Dependencies

```bash
# Check Python version
python3 --version  # Should be 3.12 or higher

# Install dependencies
pip3 install -r mcp/requirements.txt
```

#### 3. Setup API Key

```bash
cd mcp
cp .env.example .env
nano .env
```

Ganti `your_fal_api_key_here` dengan API key dari [fal.ai](https://fal.ai).

Save & exit (Ctrl+O, Enter, Ctrl+X).

#### 4. Integrate ke Claude Desktop

```bash
# Edit Claude config
nano ~/.config/Claude/claude_desktop_config.json
```

Tambahkan MCP server configuration:

```json
{
  "mcpServers": {
    "socialbrand-visual-generator": {
      "command": "python3",
      "args": ["/path/to/socialbrand-visual-generator/mcp/server.py"]
    }
  }
}
```

**Replace `/path/to/` dengan absolute path.** Contoh:

```bash
# Check absolute path
pwd  # e.g. /home/jhordi/socialbrand-visual-generator

# Full path: /home/jhordi/socialbrand-visual-generator/mcp/server.py
```

Save & exit.

#### 5. Restart Claude Desktop

- Close Claude Desktop
- Reopen Claude Desktop
- MCP tools akan tersedia

---

## Get fal.ai API Key

1. **Create Account** → Buka [fal.ai](https://fal.ai)
2. **Sign Up** → Email atau OAuth
3. **Go to Dashboard** → [api.fal.ai](https://api.fal.ai)
4. **Create API Key** → Click "Create Key"
5. **Copy Key** → Save ke `.env` file

Free tier includes:
- ✅ 100 image generations/month
- ✅ 10 video generations/month
- ✅ Full access semua models
- ✅ Perfect untuk development & testing

Upgrade anytime ke paid plan untuk production use.

---

## Verify Installation

Setelah restart Claude Desktop, test MCP tools:

```
Dalam Claude Desktop:
"list brands"
```

Jika tools tersedia, kamu akan melihat:
```
MCP Servers: 1 running
- socialbrand-visual-generator (8 tools available)
```

Jika tidak muncul:
1. Check `claude_desktop_config.json` file path
2. Verify `server.py` path (gunakan absolute path)
3. Check Python path (gunakan `python3` di macOS/Linux)
4. Review Terminal/PowerShell untuk error messages

---

## Troubleshooting

### Python Not Found

**macOS/Linux:**
```bash
# Try full path
which python3
which python

# If not found, install via Homebrew (macOS)
brew install python@3.12
```

**Windows:**
```bash
# Try full path
where python

# If not found, add Python ke PATH via System Settings
# Or reinstall Python dengan "Add Python to PATH" checked
```

### MCP Server Not Appearing

**Check config file location:**
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

**Verify JSON syntax:**
```bash
# Check JSON validity (use online JSON validator)
# Common issue: trailing commas, missing quotes
```

**Use correct path:**
```bash
# Wrong: server.py (relative path)
# Correct: /full/path/to/server.py (absolute path)
```

### API Key Error

**Check `.env` file:**
```bash
# File must be in: mcp/.env (not root directory)
# Content must be: FAL_API_KEY=your_actual_key_here
# No spaces, no quotes around key
```

**Verify API key:**
- Login ke [fal.ai](https://fal.ai)
- Check Dashboard → API Keys
- Key should be active (not revoked)

**Restart Claude Desktop:**
```bash
# Claude reads .env on startup
# After editing .env, must restart Claude Desktop
```

### Permission Errors

**macOS/Linux:**
```bash
# Make server executable
chmod +x /path/to/socialbrand-visual-generator/mcp/server.py

# Or run with python3 explicitly (recommended)
# In config: "args": ["python3", "/path/to/server.py"]
```

### Model Not Found

```bash
# Update available models list
# In Claude: "list available models"
# Or: "list available models for image-to-video"
```

---

## Post-Installation

### 1. Create First Brand

```bash
cd socialbrand-visual-generator
cp -r brands/_template brands/my-first-brand
cd brands/my-first-brand
```

### 2. Edit Brand Guidelines

```bash
# Open brand-info.md
nano brand-info.md  # macOS/Linux
notepad brand-info.md  # Windows
```

Fill dengan:
- Brand name & description
- Target audience
- Visual identity (colors, typography, style)
- Content pillars & mood

### 3. Upload Sample Images

```bash
# Copy product photos ke raw/ folder
cp /path/to/your/photos/* raw/
```

### 4. Generate Content

Dalam Claude Desktop:

```
"Generate product photo untuk brand my-first-brand,
foto: sample-product.jpg,
style: clean white background"
```

Done! ✨

---

## Next Steps

- **Read Full Guide:** [Comprehensive Guide](docs/Socialbrand_Visual_Generator_Guide.pdf) (29 pages)
- **Check FAQ:** [FAQ.md](FAQ.md)
- **Explore Models:** `list available models` dalam Claude
- **Join Community:** [GitHub Discussions](https://github.com/yourusername/socialbrand-visual-generator/discussions)

## Support

- 📖 Documentation in `/docs/`
- 🐛 Report bugs: [GitHub Issues](https://github.com/yourusername/socialbrand-visual-generator/issues)
- 💬 Ask questions: [GitHub Discussions](https://github.com/yourusername/socialbrand-visual-generator/discussions)
- 📧 Email: support@socialbrand1980.com

---

**Happy generating! 🎨📸🎬**
