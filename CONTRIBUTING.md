# Contributing to Socialbrand Visual Generator

Terima kasih untuk interest kamu berkontribusi! Semua kontribusi welcome — dari bug fixes hingga feature ideas.

## Ways to Contribute

- 🐛 **Report bugs** — Find & report issues
- ✨ **Suggest features** — Share product ideas
- 📝 **Improve documentation** — Fix typos, add examples
- 💻 **Submit code** — New features, bug fixes, refactoring
- 🧪 **Test & feedback** — Beta test new models & features

## Development Setup

### 1. Fork Repository

Klik "Fork" di GitHub untuk create copy di akun kamu.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/socialbrand-visual-generator.git
cd socialbrand-visual-generator
```

### 3. Create Feature Branch

```bash
# Create branch dengan nama deskriptif
git checkout -b feature/awesome-feature
# atau: git checkout -b fix/bug-name
# atau: git checkout -b docs/improve-docs
```

Branch naming convention:
- `feature/` — New features
- `fix/` — Bug fixes
- `docs/` — Documentation improvements
- `refactor/` — Code refactoring
- `test/` — Test additions

### 4. Install Dependencies

```bash
pip install -r mcp/requirements.txt

# Optional: Install dev dependencies (linting, formatting)
pip install black flake8 pytest
```

### 5. Make Changes

Edit code, add tests, improve docs. Pastikan:
- ✅ Code follows existing style
- ✅ Changes tested (jika applicable)
- ✅ Documentation updated
- ✅ No breaking changes (atau explain in PR)

### 6. Commit Changes

```bash
# Stage changes
git add .

# Commit dengan clear message
git commit -m "Add awesome feature: brief description"

# Or multiple commits for complex changes:
git commit -m "Add feature part 1: setup"
git commit -m "Add feature part 2: implementation"
```

Commit message guidelines:
- Use present tense ("Add feature" not "Added feature")
- Be specific ("Add video generation" not "Update stuff")
- Reference issues if applicable ("#123: Fix")
- Keep it under 50 characters on first line

### 7. Push to Your Fork

```bash
git push origin feature/awesome-feature
```

### 8. Create Pull Request

1. Go to [GitHub repo](https://github.com/yourusername/socialbrand-visual-generator)
2. Click "Compare & pull request"
3. Fill PR template:

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change)
- [ ] New feature (non-breaking change)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
Explain how you tested this change.

## Screenshots (if applicable)
Add screenshots for UI/visual changes.

## Related Issues
Closes #123
```

4. Click "Create pull request"

---

## Code Style

### Python Code

Follow PEP 8 conventions:

```python
# Good: descriptive names, clear logic
def generate_product_photo(brand_name, image_path, style):
    """Generate clean product photo from raw image."""
    prompt = _build_product_prompt(brand_name, style)
    return _fal_request("image-to-image", prompt, image_path)

# Bad: unclear variable names
def gpp(bn, ip, st):
    p = bp(bn, st)
    return fr("img2img", p, ip)
```

Guidelines:
- Max 100 characters per line
- Use descriptive variable names
- Add docstrings to functions
- Use type hints where applicable

Format dengan Black:
```bash
black mcp/server.py
```

### Commit Messages

```
# Good
Add video generation support for Seedance API

Support multiple video generation models with
configurable motion descriptions and platform
targeting. Includes proper error handling and
async/await patterns.

Closes #45

# Bad
fix stuff
update code
changes
```

---

## Testing

### Manual Testing

```bash
# Setup test environment
cp mcp/.env.example mcp/.env
# Edit .env dengan test API key

# Test in Claude Desktop
# Try each tool:
# - list brands
# - generate product photo
# - generate campaign photo
# - generate video
# - generate storyboard frame
# - list available models
```

### Automated Tests (Future)

Akan di-add soon. Format: pytest

```bash
# Run tests
pytest tests/

# Run with coverage
pytest --cov=mcp tests/
```

---

## Documentation

Help kami improve docs! Areas yang butuh help:

- **CLAUDE.md** — Update model catalogs
- **INSTALLATION.md** — Add troubleshooting steps
- **FAQ.md** — Common questions from users
- **Comprehensive Guide** — Add workflow examples
- **README.md** — Clarify instructions

Untuk docs changes:
1. Edit relevant `.md` file
2. Preview formatting (use Markdown viewer)
3. Submit PR dengan "docs/" prefix

---

## Bug Reports

Found a bug? Report di [GitHub Issues](https://github.com/yourusername/socialbrand-visual-generator/issues).

Template:

```markdown
## Description
Clear description of the bug.

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Environment
- OS: [e.g., macOS 13.0]
- Python: [e.g., 3.12.1]
- Claude: [e.g., latest]

## Screenshots
If applicable, add screenshots.

## Additional Context
Any other relevant info.
```

---

## Feature Requests

Have an idea? Share di [GitHub Discussions](https://github.com/yourusername/socialbrand-visual-generator/discussions) atau open an issue.

Template:

```markdown
## Feature Description
Clear description of the feature.

## Use Case
Why this feature is needed. Who would benefit?

## Proposed Solution
How you envision this working.

## Alternatives Considered
Other approaches you've thought about.

## Additional Context
Any other relevant info.
```

---

## Review Process

1. **Automated checks:**
   - Code formatting (Black)
   - Linting (Flake8)
   - Type checking (mypy) — future

2. **Manual review:**
   - Code quality & style
   - Functionality & correctness
   - Documentation clarity
   - Backward compatibility

3. **Approval:**
   - At least 1 maintainer approval
   - All CI checks passing
   - Discussions resolved

4. **Merge:**
   - Squash commits (keep history clean)
   - Add to CHANGELOG.md
   - Close related issues

---

## Community Guidelines

- Be respectful & inclusive
- Assume good intent
- Focus on code, not person
- Help others learn
- Report harassment to maintainers

---

## Questions?

- 📧 **Email:** support@socialbrand1980.com
- 💬 **Discussions:** [GitHub Discussions](https://github.com/yourusername/socialbrand-visual-generator/discussions)
- 🐛 **Issues:** [GitHub Issues](https://github.com/yourusername/socialbrand-visual-generator/issues)

---

## Recognition

Contributors will be recognized in:
- **README.md** → Contributors section
- **CHANGELOG.md** → Version credits
- **Website** → Team page (future)

Thank you for contributing! 🙌
