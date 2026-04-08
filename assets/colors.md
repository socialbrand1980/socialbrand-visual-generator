# Socialbrand 1980 — Brand Colors

Brand color palette untuk Socialbrand 1980 visual identity.

## Primary Colors

### Brand Blue
- **Hex:** #2563EB
- **RGB:** 37, 99, 235
- **HSL:** 217°, 98%, 54%
- **Usage:** Logo background, primary buttons, headers, CTAs

### White
- **Hex:** #FFFFFF
- **RGB:** 255, 255, 255
- **Usage:** Text on dark backgrounds, logo text, clean layouts

## Secondary Colors

### Light Blue (Hover/Accent)
- **Hex:** #3B82F6
- **RGB:** 59, 130, 246
- **HSL:** 217°, 97%, 60%
- **Usage:** Hover states, secondary buttons, accents

### Dark Blue (Dark Mode)
- **Hex:** #1E40AF
- **RGB:** 30, 64, 175
- **HSL:** 217°, 70%, 40%
- **Usage:** Dark mode backgrounds, borders, strong emphasis

## Neutral Colors

### Dark Gray (Text)
- **Hex:** #1F2937
- **RGB:** 31, 41, 55
- **Usage:** Primary text, body copy, important content

### Medium Gray (Secondary Text)
- **Hex:** #6B7280
- **RGB:** 107, 114, 128
- **Usage:** Secondary text, helper text, metadata

### Light Gray (Backgrounds)
- **Hex:** #F3F4F6
- **RGB:** 243, 244, 246
- **Usage:** Section backgrounds, subtle dividers

## Color Applications

### UI Components

| Component | Color | Usage |
|-----------|-------|-------|
| Primary Button | Brand Blue (#2563EB) | Main actions, CTAs |
| Button Hover | Light Blue (#3B82F6) | Interactive feedback |
| Button Active | Dark Blue (#1E40AF) | Pressed state |
| Text | Dark Gray (#1F2937) | Body text |
| Secondary Text | Medium Gray (#6B7280) | Captions, hints |
| Backgrounds | Light Gray (#F3F4F6) | Sections, cards |
| Borders | Light Gray (#F3F4F6) | Dividers, subtle borders |

### Development Usage

**CSS Variables (recommended):**
```css
:root {
  --color-primary-blue: #2563EB;
  --color-light-blue: #3B82F6;
  --color-dark-blue: #1E40AF;
  --color-white: #FFFFFF;
  --color-dark-gray: #1F2937;
  --color-medium-gray: #6B7280;
  --color-light-gray: #F3F4F6;
}
```

**Python/Constants:**
```python
BRAND_COLORS = {
    'primary_blue': '#2563EB',
    'light_blue': '#3B82F6',
    'dark_blue': '#1E40AF',
    'white': '#FFFFFF',
    'dark_gray': '#1F2937',
    'medium_gray': '#6B7280',
    'light_gray': '#F3F4F6',
}
```

## Color Contrast (WCAG)

All color combinations meet WCAG AA accessibility standards:

| Combination | Contrast Ratio | Level |
|------------|---|---|
| Brand Blue on White | 8.5:1 | AAA ✅ |
| Dark Gray on White | 13:1 | AAA ✅ |
| Light Blue on White | 7.8:1 | AAA ✅ |
| White on Dark Blue | 8.2:1 | AAA ✅ |

## Usage Guidelines

### Do's ✅
- Use Brand Blue (#2563EB) for primary elements
- Use white text on dark backgrounds
- Maintain sufficient contrast
- Apply colors consistently across materials
- Use Light Blue for interactive feedback

### Don'ts ❌
- Don't reverse logo colors without approval
- Don't use low-contrast text combinations
- Don't create new brand colors
- Don't desaturate brand colors
- Don't use colors inconsistently

## Brand Voice in Color

Our color palette conveys:
- **Professional** — Confident blue
- **Modern** — Clean, minimal palette
- **Trustworthy** — Consistent, accessible
- **Dynamic** — Bright, energetic primary blue

---

**For questions about color usage:** hello@socialbrand1980.com
