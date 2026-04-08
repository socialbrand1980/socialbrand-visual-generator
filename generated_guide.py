#!/usr/bin/env python3
"""
Socialbrand 1980 Visual Generator — Complete User Guide
Professional PDF Documentation for Content Creators
"""

import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.platypus.flowables import Flowable
from reportlab.graphics.shapes import (
    Drawing, Rect, RoundRect, String, Line, Polygon, Group, Circle
)
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas as cv

# ─── COLOR PALETTE ──────────────────────────────────────────────────────────
BLUE_DARK    = HexColor('#1E3A8A')
BLUE         = HexColor('#2563EB')
BLUE_MID     = HexColor('#3B82F6')
BLUE_LIGHT   = HexColor('#60A5FA')
BLUE_BG      = HexColor('#EFF6FF')
BLUE_BORDER  = HexColor('#BFDBFE')
GRAY_DARK    = HexColor('#1E293B')
GRAY_MID     = HexColor('#64748B')
GRAY_LIGHT   = HexColor('#F8FAFC')
GRAY_BORDER  = HexColor('#E2E8F0')
GREEN        = HexColor('#059669')
GREEN_BG     = HexColor('#ECFDF5')
GREEN_BORDER = HexColor('#6EE7B7')
ORANGE       = HexColor('#D97706')
ORANGE_BG    = HexColor('#FFFBEB')
ORANGE_BORDER= HexColor('#FCD34D')
WHITE        = white

PAGE_W, PAGE_H = A4
MARGIN = 1.8 * cm
CONTENT_W = PAGE_W - 2 * MARGIN

# ─── PAGE TEMPLATE ──────────────────────────────────────────────────────────
def on_page(canvas, doc):
    """Header and footer on every page except cover."""
    page = doc.page
    if page == 1:
        return

    canvas.saveState()

    # ── Header ──
    canvas.setFillColor(BLUE)
    canvas.rect(0, PAGE_H - 1.2 * cm, PAGE_W, 1.2 * cm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(MARGIN, PAGE_H - 0.75 * cm, "SOCIALBRAND 1980")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.75 * cm,
                           "Visual Generator — User Guide")

    # ── Footer ──
    canvas.setStrokeColor(BLUE_BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 1.2 * cm, PAGE_W - MARGIN, 1.2 * cm)
    canvas.setFillColor(GRAY_MID)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(MARGIN, 0.7 * cm, "Powered by fal.ai  •  Socialbrand 1980")
    canvas.drawRightString(PAGE_W - MARGIN, 0.7 * cm, f"Page {page}")

    canvas.restoreState()


def on_page_cover(canvas, doc):
    """Full-bleed cover page."""
    canvas.saveState()
    # Blue gradient background (two rects)
    canvas.setFillColor(BLUE_DARK)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(BLUE)
    canvas.rect(0, 0, PAGE_W, PAGE_H * 0.55, fill=1, stroke=0)
    # Decorative diagonal band
    from reportlab.graphics.shapes import Polygon as Poly
    canvas.setFillColor(HexColor('#1D4ED8'))
    p = canvas.beginPath()
    p.moveTo(0, PAGE_H * 0.55)
    p.lineTo(PAGE_W, PAGE_H * 0.62)
    p.lineTo(PAGE_W, PAGE_H * 0.55)
    p.close()
    canvas.drawPath(p, fill=1, stroke=0)
    canvas.restoreState()


# ─── STYLE FACTORY ──────────────────────────────────────────────────────────
def make_styles():
    base = getSampleStyleSheet()

    styles = {
        "cover_title": ParagraphStyle(
            "cover_title",
            fontName="Helvetica-Bold",
            fontSize=34,
            textColor=WHITE,
            alignment=TA_LEFT,
            spaceAfter=10,
            leading=42,
        ),
        "cover_subtitle": ParagraphStyle(
            "cover_subtitle",
            fontName="Helvetica",
            fontSize=16,
            textColor=HexColor('#BFDBFE'),
            alignment=TA_LEFT,
            spaceAfter=6,
        ),
        "cover_tag": ParagraphStyle(
            "cover_tag",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=BLUE_LIGHT,
            alignment=TA_LEFT,
            spaceAfter=4,
        ),
        "h1": ParagraphStyle(
            "h1",
            fontName="Helvetica-Bold",
            fontSize=22,
            textColor=BLUE_DARK,
            spaceBefore=16,
            spaceAfter=8,
            leading=28,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName="Helvetica-Bold",
            fontSize=15,
            textColor=BLUE,
            spaceBefore=14,
            spaceAfter=6,
            leading=20,
        ),
        "h3": ParagraphStyle(
            "h3",
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=GRAY_DARK,
            spaceBefore=10,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=10,
            textColor=GRAY_DARK,
            spaceAfter=6,
            leading=16,
            alignment=TA_JUSTIFY,
        ),
        "body_left": ParagraphStyle(
            "body_left",
            fontName="Helvetica",
            fontSize=10,
            textColor=GRAY_DARK,
            spaceAfter=6,
            leading=16,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Helvetica",
            fontSize=10,
            textColor=GRAY_DARK,
            spaceAfter=4,
            leading=15,
            leftIndent=14,
            bulletIndent=0,
        ),
        "small": ParagraphStyle(
            "small",
            fontName="Helvetica",
            fontSize=9,
            textColor=GRAY_MID,
            spaceAfter=4,
            leading=13,
        ),
        "code": ParagraphStyle(
            "code",
            fontName="Courier",
            fontSize=9,
            textColor=GRAY_DARK,
            spaceAfter=3,
            leading=13,
            leftIndent=10,
        ),
        "tip_title": ParagraphStyle(
            "tip_title",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=GREEN,
            spaceAfter=3,
        ),
        "warn_title": ParagraphStyle(
            "warn_title",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=ORANGE,
            spaceAfter=3,
        ),
        "info_title": ParagraphStyle(
            "info_title",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=BLUE,
            spaceAfter=3,
        ),
        "box_body": ParagraphStyle(
            "box_body",
            fontName="Helvetica",
            fontSize=10,
            textColor=GRAY_DARK,
            spaceAfter=3,
            leading=15,
        ),
        "toc_item": ParagraphStyle(
            "toc_item",
            fontName="Helvetica",
            fontSize=10,
            textColor=GRAY_DARK,
            spaceAfter=4,
            leftIndent=12,
        ),
        "toc_section": ParagraphStyle(
            "toc_section",
            fontName="Helvetica-Bold",
            fontSize=11,
            textColor=BLUE,
            spaceBefore=8,
            spaceAfter=3,
        ),
        "label": ParagraphStyle(
            "label",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=BLUE,
            spaceAfter=2,
        ),
        "center": ParagraphStyle(
            "center",
            fontName="Helvetica",
            fontSize=10,
            textColor=GRAY_DARK,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
    }
    return styles

S = make_styles()

# ─── HELPER FLOWABLES ────────────────────────────────────────────────────────
def divider(color=BLUE_BORDER, thickness=0.7):
    return HRFlowable(width="100%", thickness=thickness,
                      color=color, spaceAfter=8, spaceBefore=4)

def sp(h=6):
    return Spacer(1, h)

def h1(text):
    return Paragraph(text, S["h1"])

def h2(text):
    return Paragraph(text, S["h2"])

def h3(text):
    return Paragraph(text, S["h3"])

def body(text):
    return Paragraph(text, S["body"])

def body_left(text):
    return Paragraph(text, S["body_left"])

def bullet(text):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", S["bullet"])

def small(text):
    return Paragraph(text, S["small"])

def label(text):
    return Paragraph(text, S["label"])

def code_block(lines):
    """Gray background code block."""
    rows = [[Paragraph(line, S["code"])] for line in lines]
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GRAY_LIGHT),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [4, 4, 4, 4]),
        ("BOX", (0, 0), (-1, -1), 0.5, GRAY_BORDER),
    ]))
    return t

def info_box(title, lines, box_type="info"):
    """Colored info/tip/warning box."""
    if box_type == "tip":
        bg, border, title_style = GREEN_BG, GREEN, S["tip_title"]
        icon = "✓ TIP"
    elif box_type == "warn":
        bg, border, title_style = ORANGE_BG, ORANGE, S["warn_title"]
        icon = "! PERHATIAN"
    else:
        bg, border, title_style = BLUE_BG, BLUE, S["info_title"]
        icon = "ℹ INFO"

    display_title = title if title else icon
    content = [Paragraph(f"<b>{display_title}</b>", title_style)]
    for line in lines:
        content.append(Paragraph(line, S["box_body"]))

    inner = Table([[c] for c in content], colWidths=[CONTENT_W - 28])
    inner.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))

    outer = Table([[inner]], colWidths=[CONTENT_W])
    outer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("BOX", (0, 0), (-1, -1), 1.2, border),
        ("LINEBEFORE", (0, 0), (0, -1), 4, border),
    ]))
    return outer

def styled_table(headers, rows, col_widths=None):
    """Professional styled table with blue header."""
    all_rows = [headers] + rows
    t = Table(all_rows, colWidths=col_widths)
    style = [
        # Header row
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        # Body rows
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("TOPPADDING", (0, 1), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 7),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, GRAY_LIGHT]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        # Grid
        ("GRID", (0, 0), (-1, -1), 0.5, GRAY_BORDER),
        ("BOX", (0, 0), (-1, -1), 1, BLUE_BORDER),
    ]
    t.setStyle(TableStyle(style))
    return t

def section_band(title, subtitle=None):
    """Blue band for chapter/section start."""
    inner = [Paragraph(f"<font color='white'><b>{title}</b></font>",
                       ParagraphStyle("sb_t", fontName="Helvetica-Bold",
                                      fontSize=16, textColor=WHITE,
                                      leading=20))]
    if subtitle:
        inner.append(Paragraph(
            f"<font color='#BFDBFE'>{subtitle}</font>",
            ParagraphStyle("sb_s", fontName="Helvetica", fontSize=10,
                           textColor=HexColor('#BFDBFE'), leading=14)))

    content = Table([[p] for p in inner], colWidths=[CONTENT_W])
    content.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))

    wrapper = Table([[content]], colWidths=[CONTENT_W])
    wrapper.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("ROUNDEDCORNERS", [6, 6, 6, 6]),
    ]))
    return wrapper

def workflow_steps(steps):
    """Numbered workflow steps with blue numbers."""
    rows = []
    for i, (title, desc) in enumerate(steps, 1):
        num_cell = Paragraph(
            f"<font color='white'><b>{i}</b></font>",
            ParagraphStyle("stepnum", fontName="Helvetica-Bold",
                           fontSize=13, alignment=TA_CENTER, textColor=WHITE)
        )
        content_cell = [
            Paragraph(f"<b>{title}</b>", S["h3"]),
            Paragraph(desc, S["body_left"]),
        ]
        t_inner = Table([[c] for c in content_cell], colWidths=[CONTENT_W - 50])
        t_inner.setStyle(TableStyle([
            ("TOPPADDING", (0, 0), (-1, -1), 1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ]))
        rows.append([num_cell, t_inner])

    t = Table(rows, colWidths=[38, CONTENT_W - 50])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), BLUE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (1, 0), (-1, -1), 12),
        ("ROWBACKGROUNDS", (1, 0), (-1, -1), [WHITE, BLUE_BG]),
        ("BOX", (0, 0), (-1, -1), 1, BLUE_BORDER),
        ("LINEBEFORE", (1, 0), (-1, -1), 0.5, BLUE_BORDER),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, BLUE_BORDER),
    ]))
    return t

def flow_diagram(nodes, arrows=True):
    """Simple horizontal flowchart."""
    n = len(nodes)
    box_w = (CONTENT_W - (n - 1) * 12) / n
    box_h = 40
    total_w = CONTENT_W
    total_h = box_h + 10

    d = Drawing(total_w, total_h)
    for i, (label_text, sub) in enumerate(nodes):
        x = i * (box_w + 12)
        # Box
        r = RoundRect(x, 5, box_w, box_h, radius=4,
                      fillColor=BLUE_BG, strokeColor=BLUE, strokeWidth=1)
        d.add(r)
        # Label
        s = String(x + box_w / 2, 5 + box_h * 0.55,
                   label_text,
                   fontName="Helvetica-Bold", fontSize=8,
                   fillColor=BLUE_DARK, textAnchor="middle")
        d.add(s)
        if sub:
            s2 = String(x + box_w / 2, 5 + box_h * 0.28,
                        sub,
                        fontName="Helvetica", fontSize=7,
                        fillColor=GRAY_MID, textAnchor="middle")
            d.add(s2)
        # Arrow
        if arrows and i < n - 1:
            ax = x + box_w + 2
            ay = 5 + box_h / 2
            d.add(Line(ax, ay, ax + 8, ay, strokeColor=BLUE_MID, strokeWidth=1.5))
            d.add(Polygon([ax + 8, ay, ax + 5, ay + 3, ax + 5, ay - 3],
                          fillColor=BLUE_MID, strokeColor=BLUE_MID))
    return d


# ─── CONTENT SECTIONS ────────────────────────────────────────────────────────

def build_cover():
    """Cover page — content is mostly drawn in on_page_cover callback."""
    story = []
    story.append(sp(PAGE_H * 0.15))
    story.append(Paragraph(
        "<font color='#93C5FD'>SOCIALBRAND 1980</font>",
        S["cover_tag"]
    ))
    story.append(sp(6))
    story.append(Paragraph("Visual Generator", S["cover_title"]))
    story.append(Paragraph("Complete User Guide", S["cover_title"]))
    story.append(sp(16))
    story.append(Paragraph(
        "Panduan lengkap untuk content creators dalam menggunakan\n"
        "sistem AI visual generation Socialbrand 1980.",
        S["cover_subtitle"]
    ))
    story.append(sp(24))

    # Feature pills
    pill_data = [["Product Photo", "Campaign Visual", "Product Video", "Storyboard"]]
    pill_t = Table(pill_data, colWidths=[CONTENT_W / 4] * 4)
    pill_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor('#1D4ED8')),
        ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("BOX", (0, 0), (-1, -1), 0.5, BLUE_LIGHT),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, BLUE_LIGHT),
        ("ROUNDEDCORNERS", [4, 4, 4, 4]),
    ]))
    story.append(pill_t)
    story.append(sp(PAGE_H * 0.12))

    # Version block
    story.append(Paragraph(
        f"<font color='#93C5FD'>Version 2.0  &nbsp;|&nbsp;  {datetime.now().strftime('%B %Y')}  &nbsp;|&nbsp;  Powered by fal.ai</font>",
        ParagraphStyle("ver", fontName="Helvetica", fontSize=9,
                       textColor=HexColor('#93C5FD'), alignment=TA_LEFT)
    ))
    return story


def build_toc():
    story = []
    story.append(sp(10))
    story.append(h1("Table of Contents"))
    story.append(divider())
    story.append(sp(8))

    sections = [
        ("1", "Introduction & System Overview", [
            "Apa itu Socialbrand Visual Generator",
            "Cara Kerja Sistem",
            "Yang Bisa Kamu Buat",
        ]),
        ("2", "Quick Start Guide", [
            "Mulai dalam 5 Menit",
            "First Content Generation",
        ]),
        ("3", "Tool Reference: generate_product_photo", [
            "Parameter & Opsi",
            "Style Presets",
            "Contoh Penggunaan",
        ]),
        ("4", "Tool Reference: generate_campaign_photo", [
            "Parameter & Opsi",
            "Platform Optimization",
            "Contoh Penggunaan",
        ]),
        ("5", "Tool Reference: generate_video_from_image", [
            "Parameter & Opsi",
            "Duration & Resolution Guide",
            "Contoh Penggunaan",
        ]),
        ("6", "Tool Reference: generate_storyboard_frame", [
            "Apa itu Storyboard & Kenapa Penting",
            "7 Frame Types Dijelaskan",
            "Step-by-Step Membuat Storyboard",
            "Storyboard untuk Berbagai Brand",
        ]),
        ("7", "Supporting Tools", [
            "polish_prompt, list_brands, get_brand_info, list_available_models",
        ]),
        ("8", "Model Selection Guide", [
            "Image-to-Image Models",
            "Image-to-Video Models",
            "Text-to-Image (Storyboard) Models",
            "Decision Guide: Kapan Pakai Model Apa",
        ]),
        ("9", "Best Practices & Pro Tips", [
            "Prompt Engineering",
            "Brand Consistency",
            "Platform Optimization",
            "Common Mistakes to Avoid",
        ]),
        ("10", "Workflow Examples", [
            "Skincare Brand Workflow",
            "Parfume & Fragrance Brand Workflow",
            "Fashion Brand Workflow",
            "Content Creator Affiliate Workflow",
            "Storyboard Campaign Planning Workflow",
        ]),
        ("11", "Brand Setup Guide", [
            "Setup Brand Baru Step-by-Step",
            "Template brand-info.md",
        ]),
        ("12", "FAQ & Troubleshooting", [
            "Pertanyaan Umum",
            "Error Messages & Solutions",
        ]),
    ]

    left_items = sections[:6]
    right_items = sections[6:]

    def toc_cell(items):
        cell_content = []
        for num, title, sub in items:
            cell_content.append(
                Paragraph(f"<b><font color='#2563EB'>{num}.</font> {title}</b>",
                          S["toc_section"])
            )
            for s in sub:
                cell_content.append(
                    Paragraph(f"&nbsp;&nbsp;&nbsp;— {s}", S["toc_item"])
                )
        t = Table([[c] for c in cell_content], colWidths=[(CONTENT_W - 16) / 2])
        t.setStyle(TableStyle([
            ("TOPPADDING", (0, 0), (-1, -1), 1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ]))
        return t

    toc_table = Table(
        [[toc_cell(left_items), toc_cell(right_items)]],
        colWidths=[(CONTENT_W - 16) / 2, (CONTENT_W - 16) / 2]
    )
    toc_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(toc_table)
    return story


def build_intro():
    story = []
    story.append(section_band(
        "1. Introduction & System Overview",
        "Kenali sistem yang akan mengubah cara kamu membuat konten"
    ))
    story.append(sp(10))

    story.append(h2("Apa itu Socialbrand Visual Generator?"))
    story.append(body(
        "Socialbrand Visual Generator adalah sistem AI berbasis fal.ai yang terintegrasi langsung "
        "ke dalam workflow Socialbrand 1980. Sistem ini memungkinkan content creators untuk "
        "menghasilkan foto produk profesional, campaign visual, product video, dan storyboard "
        "<b>tanpa perlu photoshoot fisik</b> — hanya dengan foto mentah produk dan deskripsi "
        "yang tepat."
    ))
    story.append(sp(4))
    story.append(body(
        "Berbeda dengan tools AI generik, sistem ini dirancang khusus untuk kebutuhan brand management: "
        "setiap generate sudah mempertimbangkan <b>brand identity, target platform, dan visual guideline</b> "
        "yang tersimpan di brand profile masing-masing brand."
    ))
    story.append(sp(10))

    story.append(h2("Yang Bisa Kamu Buat"))
    caps = [
        ["Konten", "Deskripsi", "Format Output"],
        ["Product Photo", "Clean studio shot dari foto mentah produk", "JPG"],
        ["Campaign Photo", "Ad visual dengan mood & brand aesthetic", "JPG"],
        ["Product Video", "Animasi produk untuk Reels & TikTok", "MP4"],
        ["Storyboard Frame", "Visual blueprint campaign dari teks saja", "JPG"],
    ]
    story.append(styled_table(
        caps[0], caps[1:],
        col_widths=[CONTENT_W * 0.25, CONTENT_W * 0.55, CONTENT_W * 0.2]
    ))
    story.append(sp(10))

    story.append(h2("Cara Kerja Sistem"))
    story.append(body(
        "Setiap kali kamu meminta generate konten, sistem akan melakukan 4 hal secara otomatis:"
    ))
    story.append(sp(6))
    flow = flow_diagram([
        ("Baca Brand Info", "brand-info.md"),
        ("Build Prompt", "AI-optimized"),
        ("Kirim ke fal.ai", "API request"),
        ("Simpan Output", "ke folder brand"),
    ])
    story.append(flow)
    story.append(sp(8))
    story.append(info_box("Mengapa ini penting?", [
        "Kamu tidak perlu menulis prompt yang panjang dan teknikal setiap saat. "
        "Sistem sudah menyimpan brand context di brand-info.md, sehingga setiap generate "
        "sudah konsisten dengan brand identity secara otomatis.",
        "Kamu hanya perlu menentukan: <b>brand mana, foto apa, mood seperti apa, "
        "dan platform mana</b>."
    ], box_type="info"))

    story.append(sp(10))
    story.append(h2("Brand yang Tersimpan di Sistem"))
    story.append(body(
        "Setiap brand memiliki folder sendiri berisi raw photos, moodboard, brand-info.md, "
        "dan folder generated yang terpisah per content type. Ini memastikan output tetap "
        "terorganisir dan mudah dikelola."
    ))
    return story


def build_quickstart():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "2. Quick Start Guide",
        "Generate konten pertamamu dalam 3 menit"
    ))
    story.append(sp(10))
    story.append(body(
        "Belum pernah pakai sistem ini sebelumnya? Ikuti 5 langkah di bawah untuk "
        "menghasilkan foto produk pertamamu."
    ))
    story.append(sp(8))

    story.append(workflow_steps([
        ("Lihat brand yang tersedia",
         "Ketik: 'Lihat brand yang ada' — sistem akan menampilkan semua brand beserta jumlah "
         "raw photo, campaign, video, dan storyboard yang sudah digenerate."),
        ("Pilih brand dan baca info-nya",
         "Ketik: 'Baca info brand [nama-brand]' — ini menampilkan brand-info.md berisi "
         "photography style, mood, target audience, dan platform yang sudah dikonfigurasi."),
        ("Cek foto mentah yang tersedia",
         "Di hasil get_brand_info, lihat bagian 'available_raw_photos' untuk tahu foto "
         "mana saja yang bisa digunakan sebagai input."),
        ("Generate konten pertama",
         "Ketik misalnya: 'Generate product photo untuk brand 2bShine, "
         "foto: brands/2bShine/raw/serum.jpg, style: clean white' — sistem akan "
         "generate dan simpan otomatis."),
        ("Cek hasilnya",
         "File tersimpan di brands/[nama-brand]/generated/product/ dengan timestamp. "
         "Jika hasil belum sesuai, coba adjust strength atau tambah extra_prompt."),
    ]))
    story.append(sp(10))
    story.append(info_box("Pro Tip: Polish Prompt Dulu", [
        "Sebelum generate, kamu bisa gunakan polish_prompt untuk mengubah ide kasar "
        "jadi prompt yang optimal. Contoh: 'Polish prompt ini untuk campaign: "
        "serum botol kaca dengan efek cahaya pagi hari' — hasilnya bisa langsung "
        "dipakai di extra_prompt."
    ], box_type="tip"))
    return story


def build_tool_product_photo():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "3. generate_product_photo",
        "Ubah foto mentah menjadi studio shot profesional"
    ))
    story.append(sp(10))

    story.append(body(
        "Tool ini mengambil foto produk mentah (raw photo) dan mengubahnya menjadi foto "
        "produk berkualitas studio profesional. Cocok untuk e-commerce listing, product "
        "catalog, dan konten organik yang butuh foto produk bersih dan konsisten."
    ))
    story.append(sp(8))

    story.append(h2("Parameter Tool"))
    params = [
        ["Parameter", "Wajib?", "Default", "Keterangan"],
        ["brand_name", "Ya", "—", "Nama folder brand (lihat list_brands)"],
        ["product_image_path", "Ya", "—", "Path ke raw photo produk"],
        ["style", "Tidak", "clean_white", "Style preset foto (lihat tabel di bawah)"],
        ["model", "Tidak", "FLUX Dev", "Model AI yang digunakan"],
        ["extra_prompt", "Tidak", "—", "Detail tambahan untuk foto"],
        ["strength", "Tidak", "0.75", "Kekuatan transformasi (0.1–0.95)"],
    ]
    story.append(styled_table(params[0], params[1:],
                              col_widths=[CONTENT_W*0.22, CONTENT_W*0.12,
                                          CONTENT_W*0.18, CONTENT_W*0.48]))
    story.append(sp(10))

    story.append(h2("Style Presets"))
    styles_data = [
        ["Style", "Hasil Visual", "Cocok Untuk"],
        ["clean_white", "Background putih bersih, cahaya profesional", "E-commerce, product catalog"],
        ["minimal_grey", "Background abu muda, shadow lembut", "Lifestyle brand, premium feel"],
        ["natural", "Natural light, warm tones, lifestyle setting", "Skincare, food, wellness"],
        ["dark_moody", "Background gelap, dramatic lighting, mewah", "Parfume, fashion, luxury"],
        ["flat_lay", "Top-down view, arranged composition", "Fashion accessories, beauty"],
        ["contextual", "Setting nyata, in-use shot, natural env.", "Lifestyle, FMCG, everyday brand"],
    ]
    story.append(styled_table(styles_data[0], styles_data[1:],
                              col_widths=[CONTENT_W*0.2, CONTENT_W*0.42, CONTENT_W*0.38]))
    story.append(sp(10))

    story.append(h2("Contoh Penggunaan"))
    story.append(body_left("<b>Basic — Foto produk dengan style default:</b>"))
    story.append(code_block([
        '"Generate product photo untuk brand 2bShine,',
        ' foto: brands/2bShine/raw/serum.jpg,',
        ' style: clean white"',
    ]))
    story.append(sp(6))
    story.append(body_left("<b>Advanced — Dengan extra detail dan model spesifik:</b>"))
    story.append(code_block([
        '"Generate product photo untuk brand 2bShine,',
        ' foto: brands/2bShine/raw/serum.jpg,',
        ' style: dark moody,',
        ' model: fal-ai/flux-realism/image-to-image,',
        ' extra_prompt: glossy glass bottle with light refraction,',
        '               water mist effect on surface,',
        ' strength: 0.8"',
    ]))
    story.append(sp(8))

    story.append(h2("Strength Guide"))
    story.append(body(
        "Parameter <b>strength</b> menentukan seberapa besar AI mengubah foto aslimu:"
    ))
    strength_data = [
        ["Strength", "Efek", "Kapan Digunakan"],
        ["0.3 – 0.5", "Minimal, produk hampir sama", "Hanya ganti background, produk harus sama persis"],
        ["0.6 – 0.75", "Balanced (default)", "Standard product photos, tetap mirip asli tapi lebih clean"],
        ["0.8 – 0.95", "Transformasi kuat", "Campaign photos, perlu perbedaan mood yang signifikan"],
    ]
    story.append(styled_table(strength_data[0], strength_data[1:],
                              col_widths=[CONTENT_W*0.2, CONTENT_W*0.4, CONTENT_W*0.4]))
    return story


def build_tool_campaign_photo():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "4. generate_campaign_photo",
        "Buat campaign & ad visual dari foto produk"
    ))
    story.append(sp(10))

    story.append(body(
        "Tool ini mengambil foto produk dan mengubahnya menjadi visual campaign yang siap "
        "publish di social media atau iklan. Berbeda dari product_photo yang fokus pada "
        "produk saja, campaign_photo menggabungkan produk dengan <b>mood, atmosfer, dan "
        "aesthetic yang sesuai platform target</b>."
    ))
    story.append(sp(8))

    story.append(h2("Parameter Tool"))
    params = [
        ["Parameter", "Wajib?", "Keterangan"],
        ["brand_name", "Ya", "Nama folder brand"],
        ["product_image_path", "Ya", "Path ke foto produk (bisa hasil generate_product_photo)"],
        ["product_description", "Ya", "Deskripsi singkat produk, mis: 'brightening face serum'"],
        ["mood", "Ya", "Mood/vibe campaign, mis: 'luxurious and minimalist'"],
        ["platform", "Tidak", "Target platform: Instagram Feed, Story, TikTok, Facebook Ad, Banner"],
        ["model", "Tidak", "Model AI (default: FLUX Dev)"],
        ["extra_prompt", "Tidak", "Detail extra scene, mis: 'golden hour lighting'"],
        ["strength", "Tidak", "0.85 default — lebih tinggi untuk campaign vs product photo"],
    ]
    story.append(styled_table(params[0], params[1:],
                              col_widths=[CONTENT_W*0.28, CONTENT_W*0.12, CONTENT_W*0.6]))
    story.append(sp(10))

    story.append(h2("Platform-Specific Settings"))
    plat = [
        ["Platform", "Komposisi", "Mood yang Cocok"],
        ["Instagram Feed", "4:5 vertical, scroll-stopping", "Aspirasional, clean, lifestyle"],
        ["Instagram Story", "9:16 full vertical, bold visual", "Dynamic, engaging, FOMO"],
        ["TikTok", "9:16, energetic, youthful", "Fun, authentic, trending, before-after"],
        ["Facebook Ad", "Square/landscape, clear CTA", "Trust-building, informative, benefit-led"],
        ["Banner", "Horizontal, clean layout", "Professional, minimal, informational"],
    ]
    story.append(styled_table(plat[0], plat[1:],
                              col_widths=[CONTENT_W*0.22, CONTENT_W*0.32, CONTENT_W*0.46]))
    story.append(sp(10))

    story.append(h2("Contoh Penggunaan"))
    story.append(body_left("<b>Campaign photo untuk Instagram Feed:</b>"))
    story.append(code_block([
        '"Generate campaign photo untuk brand 2bShine,',
        ' produk: brightening DNA gel essence serum,',
        ' mood: glowing skin, dewy fresh, morning skincare ritual,',
        ' platform: Instagram Feed,',
        ' extra_prompt: soft morning light, white marble surface"',
    ]))
    story.append(sp(6))
    story.append(body_left("<b>Campaign photo untuk TikTok (energetic):</b>"))
    story.append(code_block([
        '"Generate campaign photo untuk brand 2bShine,',
        ' produk: brightening face serum,',
        ' mood: energetic, youthful, before-after glow transformation,',
        ' platform: TikTok,',
        ' strength: 0.9"',
    ]))
    story.append(sp(8))
    story.append(info_box("Best Practice", [
        "Gunakan foto hasil generate_product_photo sebagai input campaign_photo — "
        "bukan raw photo langsung. Foto yang sudah clean akan memberikan hasil campaign "
        "yang jauh lebih konsisten dan profesional.",
        "Strength 0.85 adalah sweet spot untuk campaign: cukup transformatif untuk "
        "menciptakan mood baru, tapi produk masih clearly recognizable."
    ], box_type="tip"))
    return story


def build_tool_video():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "5. generate_video_from_image",
        "Animasikan foto produk menjadi video untuk Reels & TikTok"
    ))
    story.append(sp(10))

    story.append(body(
        "Tool ini mengubah foto produk statis menjadi video pendek yang siap publish di "
        "Instagram Reels, TikTok, atau platform video lainnya. Video dihasilkan menggunakan "
        "model AI khusus video yang memahami physics gerakan dan sinematografi."
    ))
    story.append(sp(4))
    story.append(info_box("Waktu Generate", [
        "Video generation membutuhkan waktu lebih lama dari foto — biasanya 30 hingga 90 detik "
        "tergantung model dan resolusi yang dipilih. Ini normal. Sistem akan menunggu otomatis "
        "sampai video selesai dan menyimpannya."
    ], box_type="warn"))
    story.append(sp(8))

    story.append(h2("Parameter Tool"))
    params = [
        ["Parameter", "Wajib?", "Default", "Keterangan"],
        ["brand_name", "Ya", "—", "Nama folder brand"],
        ["product_image_path", "Ya", "—", "Path ke foto produk yang akan dianimasikan"],
        ["product_description", "Ya", "—", "Deskripsi produk, mis: 'glass serum bottle'"],
        ["motion_description", "Ya", "—", "Describe gerakannya! Lihat contoh di bawah"],
        ["platform", "Tidak", "Instagram Reels", "Platform target"],
        ["model", "Tidak", "Seedance Pro", "Model video (lihat model guide)"],
        ["duration", "Tidak", "5", "Durasi dalam detik: 2, 3, 4, 5, 6, 8, 10"],
        ["resolution", "Tidak", "720p", "480p (draft), 720p (publish), 1080p (premium)"],
        ["aspect_ratio", "Tidak", "auto", "auto / 9:16 / 16:9 / 1:1"],
    ]
    story.append(styled_table(params[0], params[1:],
                              col_widths=[CONTENT_W*0.25, CONTENT_W*0.1,
                                          CONTENT_W*0.17, CONTENT_W*0.48]))
    story.append(sp(10))

    story.append(h2("Motion Description: Cara Mendeskripsikan Gerakan"))
    story.append(body(
        "Kualitas video sangat bergantung pada seberapa baik kamu mendeskripsikan "
        "gerakannya. Semakin spesifik, semakin baik hasilnya:"
    ))
    motion = [
        ["Contoh Motion Description", "Efek yang Dihasilkan"],
        ["'produk berputar perlahan 360 derajat dengan efek cahaya shimmer'",
         "Produk rotate dengan light glint — cocok untuk skincare/parfume"],
        ["'botol jatuh perlahan di atas permukaan air dengan cipratan halus'",
         "Product drop dengan water physics — dramatic, premium feel"],
        ["'produk mengapung di udara dengan partikel cahaya di sekitarnya'",
         "Floating product dengan particle effect — dreamy, luxurious"],
        ["'tangan mengangkat produk dari meja dengan pencahayaan golden hour'",
         "Lifestyle motion, in-hand shot — authentic, relatable"],
        ["'kamera zoom in perlahan ke detail tekstur produk'",
         "Ken Burns effect + detail reveal — educational, texture-focused"],
    ]
    story.append(styled_table(motion[0], motion[1:],
                              col_widths=[CONTENT_W*0.5, CONTENT_W*0.5]))
    story.append(sp(10))

    story.append(h2("Resolution & Platform Guide"))
    res = [
        ["Resolusi", "Generate Time", "Cocok Untuk"],
        ["480p", "~30 detik", "Draft dan preview, jangan publish"],
        ["720p (default)", "~60 detik", "Instagram Reels, TikTok, standar publish"],
        ["1080p", "~90 detik", "YouTube, Facebook premium, presentation"],
    ]
    story.append(styled_table(res[0], res[1:],
                              col_widths=[CONTENT_W*0.22, CONTENT_W*0.2, CONTENT_W*0.58]))
    return story


def build_tool_storyboard():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "6. generate_storyboard_frame",
        "Buat blueprint visual campaign tanpa foto — hanya dari deskripsi teks"
    ))
    story.append(sp(10))

    story.append(h2("Apa itu Storyboard dan Kenapa Sangat Penting?"))
    story.append(body(
        "Storyboard adalah <b>blueprint visual sebuah campaign</b>. Sebelum melakukan "
        "photoshoot nyata, rekaman video, atau generate konten dalam jumlah besar, "
        "kamu merencanakan terlebih dahulu setiap scene dalam bentuk static image."
    ))
    story.append(sp(6))

    reasons = [
        ["Manfaat Storyboard", "Tanpa Storyboard", "Dengan Storyboard"],
        ["Waktu", "Langsung execute, sering revisi", "Plan dulu, execute sekali dengan benar"],
        ["Client Buy-in", "Klien susah visualize", "Klien bisa lihat dan approve visual dulu"],
        ["Konsistensi", "Visual tidak terhubung antar konten", "Setiap konten terasa bagian dari campaign"],
        ["Biaya Produksi", "Banyak reshoot karena tidak terencana", "Shoot sekali, hasilnya sesuai"],
        ["Kreativitas", "Terbatas oleh apa yang ada", "Eksplorasi ide dulu, baru execute"],
    ]
    story.append(styled_table(reasons[0], reasons[1:],
                              col_widths=[CONTENT_W*0.25, CONTENT_W*0.375, CONTENT_W*0.375]))
    story.append(sp(10))

    story.append(h2("7 Frame Types — Panduan Lengkap"))
    story.append(body(
        "Sistem menyediakan 7 jenis frame yang masing-masing memiliki fungsi spesifik "
        "dalam campaign. Gunakan kombinasi frame types untuk membangun campaign yang "
        "lengkap dan variatif."
    ))
    story.append(sp(8))

    frame_types = [
        ("product_hero",
         "Fokus penuh pada produk. Background clean atau gradient. "
         "Tidak ada distraksi. Produk jadi pusat perhatian.",
         "E-commerce listing, product launch, feed hero post"),
        ("lifestyle",
         "Model atau talent sedang menggunakan produk dalam setting "
         "aspirasional. Emosi dan aspirasi diutamakan.",
         "GRWM content, routine videos, inspirational posts"),
        ("detail_closeup",
         "Macro shot yang menampilkan tekstur, detail, dan ingredient. "
         "Membuktikan kualitas produk secara visual.",
         "Ingredient education, quality proof, premium positioning"),
        ("behind_scenes",
         "Gaya candid dan authentic. Tidak overly-produced. "
         "Menciptakan feel UGC (User Generated Content).",
         "Brand transparency, relatability, community building"),
        ("brand_moment",
         "Storytelling emosional. Visual yang merepresentasikan "
         "nilai dan personality brand secara menyeluruh.",
         "Brand awareness, emotional connection, values communication"),
        ("comparison",
         "Layout sebelum/sesudah, atau perbandingan dua situasi. "
         "Sangat efektif untuk konten edukasi dan konversi.",
         "Before-after, with/without, product benefits visualization"),
        ("text_overlay",
         "Background minimal dengan ruang kosong (negative space) "
         "yang cukup untuk teks, caption, atau CTA.",
         "Quote posts, announcement, copywriting-heavy content"),
    ]

    for i, (name, desc, use) in enumerate(frame_types):
        row_bg = BLUE_BG if i % 2 == 0 else WHITE
        t = Table([
            [Paragraph(f"<b>{name}</b>", S["label"]),
             Paragraph(f"<i>Gunakan untuk:</i> {use}", S["small"])],
            [Paragraph(desc, S["body_left"]), ""]
        ], colWidths=[CONTENT_W * 0.38, CONTENT_W * 0.62])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), row_bg),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("BOX", (0, 0), (-1, -1), 0.5, BLUE_BORDER),
            ("SPAN", (0, 1), (-1, 1)),
            ("LINEBEFORE", (0, 0), (0, -1), 3, BLUE),
        ]))
        story.append(t)
        story.append(sp(3))

    story.append(sp(10))
    story.append(h2("Step-by-Step: Membuat Campaign Storyboard Lengkap"))
    story.append(body(
        "Berikut cara membangun storyboard campaign yang komprehensif dari nol:"
    ))
    story.append(sp(6))

    story.append(workflow_steps([
        ("Definisikan Campaign Objective",
         "Tentukan tujuan campaign: Awareness (perkenalan brand), Education (jelaskan produk), "
         "atau Conversion (dorong pembelian). Setiap objective butuh frame types yang berbeda."),
        ("Breakdown Content per Platform",
         "List platform target (Instagram Feed, Reels, TikTok, dll) dan berapa konten "
         "yang dibutuhkan per platform per minggu. Ini menentukan jumlah frame yang perlu dibuat."),
        ("Tentukan Frame Types per Konten",
         "Map setiap konten ke frame type yang tepat: Awareness pakai brand_moment + lifestyle. "
         "Education pakai detail_closeup + comparison. Conversion pakai product_hero + text_overlay."),
        ("Generate Storyboard Frames",
         "Generate 1 frame sekaligus atau hingga 4 frame sekaligus (num_frames: 4). "
         "Deskripsikan scene dengan detail — semakin spesifik, semakin akurat hasilnya."),
        ("Review, Iterate, dan Approve",
         "Review semua frame bersama tim atau klien. Regenerate frame yang belum sesuai "
         "dengan mengubah deskripsi scene atau model yang digunakan."),
        ("Gunakan sebagai Production Reference",
         "Frame yang sudah approved menjadi visual reference untuk photoshoot nyata, "
         "brief untuk talent/photographer, atau langsung sebagai posting jika sudah sesuai."),
    ]))
    story.append(sp(10))

    story.append(h2("Contoh: Storyboard untuk Skincare Campaign 4 Minggu"))
    story.append(code_block([
        '// Week 1: Awareness — Perkenalkan brand',
        '"Generate storyboard untuk brand 2bShine,',
        ' scene: woman waking up, gentle morning light, reaching for serum on nightstand,',
        '        peaceful bedroom, soft white aesthetic,',
        ' frame_type: lifestyle, platform: Instagram Feed, num_frames: 2"',
        '',
        '// Week 2: Education — Jelaskan produk',
        '"Generate storyboard untuk brand 2bShine,',
        ' scene: extreme closeup of DNA gel serum texture, golden liquid droplet falling,',
        '        macro photography, ingredient focus,',
        ' frame_type: detail_closeup, platform: TikTok"',
        '',
        '// Week 3: Social Proof — Before/after',
        '"Generate storyboard untuk brand 2bShine,',
        ' scene: split frame comparison, dull skin vs glowing dewy skin after serum,',
        '        clean clinical white setting,',
        ' frame_type: comparison, platform: Instagram Feed"',
        '',
        '// Week 4: Conversion — Push pembelian',
        '"Generate storyboard untuk brand 2bShine,',
        ' scene: product hero shot on marble surface, clean background space on right',
        '        for text overlay, premium feel,',
        ' frame_type: text_overlay, platform: Instagram Feed"',
    ]))
    story.append(sp(8))
    story.append(info_box("Model Terbaik untuk Storyboard", [
        "<b>FLUX Dev</b> — Pilihan default. Versatile, bagus untuk lifestyle dan product scenes.",
        "<b>Nano Banana 2</b> — Google model. Coba ini untuk storyboard yang butuh feel lebih artistic.",
        "<b>Recraft V3</b> — Terbaik jika storyboard punya elemen illustrated atau graphic-heavy.",
        "<b>Ideogram V2</b> — Gunakan jika scene memerlukan teks yang readable dalam gambar (quote frames, announcement).",
    ], box_type="info"))
    return story


def build_supporting_tools():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "7. Supporting Tools",
        "Tools pendukung untuk workflow yang lebih efisien"
    ))
    story.append(sp(10))

    tools = [
        ("polish_prompt",
         "Sebelum generate, gunakan tool ini untuk mengubah ide kasar menjadi prompt yang "
         "terstruktur dan optimal. Sangat berguna ketika kamu ingin generate konten yang "
         "tidak biasa dan perlu prompt yang lebih precise.",
         ["Tentukan content_type: product, campaign, video, atau storyboard",
          "Masukkan raw_prompt berisi ide kasarmu",
          "Optionally: tambahkan brand_name untuk include brand context",
          "Hasilnya: prompt yang sudah dioptimasi, siap dipakai di extra_prompt"]),
        ("list_brands",
         "Tampilkan semua brand yang terdaftar di sistem beserta jumlah asset masing-masing. "
         "Gunakan ini untuk mengecek brand mana yang sudah siap digunakan dan berapa konten "
         "yang sudah digenerate.",
         ["Tidak perlu parameter apapun",
          "Output: daftar brand + raw photos, campaign, video, storyboard count",
          "Gunakan brand_name yang muncul di sini untuk semua tool lainnya"]),
        ("get_brand_info",
         "Baca brand-info.md dari brand tertentu. Ini menampilkan semua brand guidelines, "
         "photography style, mood, target audience, dan daftar raw photo yang tersedia.",
         ["Input: brand_name",
          "Output: brand-info.md content + available raw photos",
          "Baca ini dulu sebelum generate untuk memastikan kamu paham brand aesthetics"]),
        ("list_available_models",
         "Tampilkan katalog model yang tersedia per kategori. Set search_fal: true untuk "
         "live search ke fal.ai API dan discover model-model terbaru yang baru dirilis.",
         ["Parameter: category (all/image-to-image/image-to-video/text-to-image)",
          "Parameter: search_fal (true = live search fal.ai API untuk model terbaru)",
          "Output: model IDs + deskripsi yang bisa langsung dipakai di tool generate"]),
    ]

    for name, desc, steps in tools:
        story.append(h2(name))
        story.append(body(desc))
        story.append(sp(4))
        for step in steps:
            story.append(bullet(step))
        story.append(sp(8))
        story.append(divider(color=BLUE_BORDER, thickness=0.5))
        story.append(sp(4))

    return story


def build_model_guide():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "8. Model Selection Guide",
        "Kapan pakai model mana — panduan lengkap"
    ))
    story.append(sp(10))

    story.append(body(
        "Memilih model yang tepat adalah kunci mendapatkan hasil yang sesuai harapan. "
        "Setiap model memiliki karakteristik berbeda — ada yang lebih cepat, ada yang "
        "lebih detailed, ada yang lebih cinematic. Panduan ini membantumu memilih dengan tepat."
    ))
    story.append(sp(10))

    story.append(h2("Image-to-Image Models (Product & Campaign Photo)"))
    img2img = [
        ["Model", "Speed", "Quality", "Terbaik Untuk", "Harga"],
        ["FLUX Dev\n(default)", "Fast\n30-60s", "Excellent", "Semua use case umum,\nstandard product photos", "Murah"],
        ["FLUX Pro", "Slow\n60-120s", "Outstanding", "Premium brand, klien besar,\nfinal hero shots", "Sedang"],
        ["FLUX Realism", "Medium\n45-80s", "Excellent", "Foto yang harus terlihat\nseperti foto nyata", "Sedang"],
        ["FLUX Schnell", "Fastest\n15-30s", "Good", "Draft dan testing\nkomposisi, jangan publish", "Sangat Murah"],
        ["SDXL", "Medium", "Good", "Eksperimen style berbeda,\nalternatif ketika FLUX tidak pas", "Murah"],
    ]
    story.append(styled_table(img2img[0], img2img[1:],
                              col_widths=[CONTENT_W*0.2, CONTENT_W*0.12,
                                          CONTENT_W*0.12, CONTENT_W*0.38, CONTENT_W*0.18]))
    story.append(sp(10))

    story.append(h2("Image-to-Video Models"))
    img2vid = [
        ["Model", "Kualitas", "Kecepatan", "Karakteristik"],
        ["Seedance 1.0 Pro\n(default)", "Cinematic\nTerbaik", "~60-90s", "Motion paling smooth. Mendukung 1080p.\nTerbaik untuk premium brand content."],
        ["Seedance 1.0 Lite", "Very Good", "~40-60s", "Versi lebih cepat dari Pro. Bagus untuk\ndraft atau konten daily volume tinggi."],
        ["Kling 1.6 Standard", "Excellent", "~40-70s", "Paling reliable untuk product videos.\nMotion physics sangat natural."],
        ["PixVerse v3.5", "Stylized", "~30-60s", "Cocok untuk fashion & editorial.\nMendukung style modes: anime, 3D, cinematic."],
    ]
    story.append(styled_table(img2vid[0], img2vid[1:],
                              col_widths=[CONTENT_W*0.25, CONTENT_W*0.15,
                                          CONTENT_W*0.15, CONTENT_W*0.45]))
    story.append(sp(10))

    story.append(h2("Text-to-Image Models (Storyboard)"))
    t2i = [
        ["Model", "Karakteristik", "Terbaik Untuk"],
        ["FLUX Dev\n(default)", "Balanced, detailed, versatile", "General storyboard, semua frame types"],
        ["FLUX Pro", "Highest quality output", "Client presentation, final storyboard deck"],
        ["FLUX Schnell", "Fastest, draft quality", "Quick concept testing, volume brainstorm"],
        ["Nano Banana 2", "Google model, artistic feel", "Lifestyle & brand_moment frames"],
        ["Recraft V3", "Brand & illustration style", "Brand visual identity, editorial aesthetic"],
        ["Ideogram V2", "Typography & graphic design", "Text-in-image, quote frames, announcements"],
    ]
    story.append(styled_table(t2i[0], t2i[1:],
                              col_widths=[CONTENT_W*0.25, CONTENT_W*0.35, CONTENT_W*0.4]))
    story.append(sp(10))

    story.append(h2("Decision Guide: Pilih Model dengan Cepat"))
    story.append(sp(4))
    story.append(flow_diagram([
        ("Butuh\nfoto bersih?", "product_photo"),
        ("Butuh\ncampaign ad?", "campaign_photo"),
        ("Butuh\nvideo?", "video_from_image"),
        ("Butuh\nstoryboard?", "storyboard_frame"),
        ("Pilih model\nsesuai tabel", ""),
    ]))
    story.append(sp(8))

    story.append(info_box("Strategy Umum", [
        "<b>Start dengan FLUX Dev.</b> Ini default yang bagus untuk 80% kebutuhan.",
        "<b>Upgrade ke FLUX Pro</b> jika: klien premium, final hero shots, atau kualitas Dev belum cukup.",
        "<b>Pakai FLUX Schnell</b> hanya untuk: draft internal, testing komposisi, brainstorm cepat.",
        "<b>Untuk video:</b> Seedance Pro untuk quality, Kling untuk reliability, PixVerse untuk editorial style.",
        "<b>Untuk storyboard:</b> FLUX Dev untuk umum, Nano Banana untuk artistic, Recraft untuk brand-heavy.",
    ], box_type="tip"))
    return story


def build_best_practices():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "9. Best Practices & Pro Tips",
        "Cara mendapatkan hasil terbaik dari setiap generate"
    ))
    story.append(sp(10))

    story.append(h2("1. Prompt Engineering: Cara Menulis Deskripsi yang Efektif"))
    story.append(body(
        "Kualitas output sangat bergantung pada kualitas deskripsi yang kamu berikan. "
        "Gunakan formula berikut untuk extra_prompt yang efektif:"
    ))
    story.append(sp(6))
    story.append(code_block([
        "[Subject/Produk] + [Action/Kondisi] + [Setting/Background] + [Lighting] + [Mood/Aesthetic]",
        "",
        "Contoh BAD:  'foto serum yang bagus'",
        "Contoh GOOD: 'glass serum bottle with golden liquid visible inside,",
        "              placed on white marble surface with dried flowers,",
        "              soft diffused natural lighting from left,",
        "              clean minimal Korean skincare aesthetic'",
    ]))
    story.append(sp(8))

    story.append(h2("2. Brand Consistency: Menjaga Visual Tetap Konsisten"))
    story.append(body(
        "Untuk memastikan semua konten brand terlihat cohesive:"
    ))
    tips_cons = [
        "Selalu isi brand-info.md dengan detail: photography style, color palette, dan mood yang spesifik",
        "Gunakan style preset yang sama untuk product photos dalam satu koleksi (misalnya selalu 'clean_white')",
        "Simpan strength yang berhasil dan gunakan kembali (note di brand-info.md atau di campaign plan)",
        "Gunakan extra_prompt yang sama untuk sesi generate dalam satu campaign agar visual konsisten",
        "Generate batch (beberapa foto sekaligus) dengan setting yang sama untuk konsistensi maksimal",
    ]
    for tip in tips_cons:
        story.append(bullet(tip))
    story.append(sp(8))

    story.append(h2("3. Platform Optimization"))
    plat_opt = [
        ["Platform", "Aspect Ratio", "Resolution", "Best Style"],
        ["Instagram Feed", "4:5 atau 1:1", "Minimum 1080px", "clean_white, minimal_grey"],
        ["Instagram Reels", "9:16", "720p atau 1080p", "dynamic motion, strong color"],
        ["TikTok", "9:16", "720p minimum", "energetic, authentic look"],
        ["Facebook Ad", "1:1 atau 16:9", "Minimum 1080px", "trust-building, clear product"],
        ["E-commerce", "1:1 (square)", "High res, white bg", "clean_white selalu"],
    ]
    story.append(styled_table(plat_opt[0], plat_opt[1:],
                              col_widths=[CONTENT_W*0.25, CONTENT_W*0.18,
                                          CONTENT_W*0.22, CONTENT_W*0.35]))
    story.append(sp(10))

    story.append(h2("4. Common Mistakes & Cara Menghindarinya"))
    mistakes = [
        ["Mistake", "Masalah", "Solusi"],
        ["Pakai raw photo langsung untuk campaign",
         "Hasil tidak bersih, background asli masih kelihatan",
         "Generate product_photo dulu, baru pakai hasilnya untuk campaign_photo"],
        ["Strength terlalu rendah (< 0.5) untuk campaign",
         "Foto tidak berubah cukup, mood tidak terasa",
         "Campaign photo idealnya strength 0.8–0.9"],
        ["Motion description terlalu singkat untuk video",
         "Video tidak bergerak sesuai harapan",
         "Deskripsikan gerakan dengan detail: arah, kecepatan, efek, atmosfer"],
        ["Tidak mengisi brand-info.md dengan detail",
         "Output tidak konsisten dengan brand identity",
         "Isi brand-info.md dengan photography style, color palette, dan mood spesifik"],
        ["Langsung pakai 1080p untuk video (draft)",
         "Waktu tunggu lama hanya untuk draft",
         "Draft dengan 480p dulu, publish dengan 720p atau 1080p"],
    ]
    story.append(styled_table(mistakes[0], mistakes[1:],
                              col_widths=[CONTENT_W*0.3, CONTENT_W*0.33, CONTENT_W*0.37]))
    return story


def build_workflows():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "10. Workflow Examples",
        "Step-by-step workflow untuk berbagai jenis brand dan content creator"
    ))
    story.append(sp(10))

    # ── SKINCARE ──
    story.append(h2("Workflow A: Skincare Brand"))
    story.append(body(
        "Skincare adalah kategori yang sangat visual dan education-driven. Konten harus membangun "
        "<b>trust</b>, membuktikan <b>efficacy</b>, dan menciptakan <b>aspirasi glow</b>. "
        "Kombinasi product hero, lifestyle routine, dan ingredient education adalah formula yang proven."
    ))
    story.append(sp(6))
    story.append(workflow_steps([
        ("Clean Product Photo",
         "generate_product_photo dengan style: clean_white atau natural. "
         "Ini jadi base asset untuk semua konten. Model: FLUX Dev atau FLUX Realism."),
        ("Morning Routine Campaign",
         "generate_campaign_photo dengan mood: 'dewy fresh skin, morning skincare ritual, "
         "soft glow'. Platform: Instagram Feed. Gunakan foto dari step 1 sebagai input."),
        ("Ingredient Detail Storyboard",
         "generate_storyboard_frame, frame_type: detail_closeup. "
         "Scene: 'serum texture closeup, golden liquid, science-meets-nature aesthetic'."),
        ("Before-After Storyboard",
         "generate_storyboard_frame, frame_type: comparison. "
         "Scene: 'dull tired skin vs radiant glowing skin after serum treatment'."),
        ("Product Video untuk Reels",
         "generate_video_from_image. Motion: 'serum bottle floating with golden shimmer particles, "
         "slow rotation, soft bokeh background'. Model: Seedance Pro. Duration: 5s, 720p."),
    ]))
    story.append(sp(6))
    story.append(info_box("Skincare Content Calendar (Weekly)", [
        "<b>Monday:</b> Product hero photo (feed post)",
        "<b>Wednesday:</b> Lifestyle campaign / morning routine (feed + story)",
        "<b>Friday:</b> Product video (Reels + TikTok)",
        "<b>Saturday:</b> Ingredient education storyboard / before-after (story)",
    ], box_type="info"))
    story.append(sp(12))

    # ── PARFUME ──
    story.append(h2("Workflow B: Parfume & Fragrance Brand"))
    story.append(body(
        "Parfume adalah produk yang tidak bisa 'dirasakan' melalui layar — sehingga visual "
        "harus <b>menciptakan sensasi</b>. Visual harus dreamy, aspirasional, dan penuh atmosphere. "
        "Focus pada storytelling dan emotional connection, bukan feature produk."
    ))
    story.append(sp(6))
    story.append(workflow_steps([
        ("Premium Product Shot",
         "generate_product_photo dengan style: dark_moody atau natural. "
         "Model: FLUX Pro atau FLUX Realism untuk detail botol yang presisi."),
        ("Dreamy Campaign Visual",
         "generate_campaign_photo dengan mood: 'ethereal, dreamlike, sensory experience, "
         "luxury lifestyle, golden twilight atmosphere'. Platform: Instagram Feed."),
        ("Cinematic Scene Storyboard",
         "generate_storyboard_frame, frame_type: brand_moment. "
         "Scene: 'woman in silk dress reaching for perfume on vanity, soft candlelight, "
         "film-like atmosphere' — no product in frame, pure emotion."),
        ("Bottle Detail Storyboard",
         "generate_storyboard_frame, frame_type: detail_closeup. "
         "Scene: 'perfume bottle extreme closeup, light refracting through glass, "
         "rainbow spectrum on dark surface, macro photography'."),
        ("Cinematic Product Video",
         "generate_video_from_image. Motion: 'perfume bottle rising from smoke, "
         "dramatic reveal with light flares, cinematic slow motion'. "
         "Model: Seedance Pro. Resolution: 1080p untuk premium feel."),
    ]))
    story.append(sp(12))

    # ── FASHION ──
    story.append(h2("Workflow C: Fashion Brand"))
    story.append(body(
        "Fashion membutuhkan visual yang menampilkan produk dalam konteks <b>wearable dan aspirasional</b>. "
        "Kombinasi detail produk, editorial lifestyle, dan collection narrative adalah kunci "
        "untuk konten fashion yang engaging dan converting."
    ))
    story.append(sp(6))
    story.append(workflow_steps([
        ("Multi-Angle Product Photos",
         "Jalankan generate_product_photo beberapa kali dengan style berbeda: "
         "flat_lay untuk detail texture, clean_white untuk e-commerce, "
         "contextual untuk lifestyle feel. Ini memberi variety aset."),
        ("Editorial Campaign Visual",
         "generate_campaign_photo dengan mood: 'editorial, seasonal, on-trend, "
         "[sesuai koleksi: e.g. boho summer / minimal winter / urban street]'. "
         "Gunakan extra_prompt untuk environment yang spesifik."),
        ("Collection Narrative Storyboard",
         "generate_storyboard_frame, frame_type: lifestyle. "
         "Generate 2-4 frames sekaligus (num_frames: 4) untuk ceritakan "
         "story koleksi dari opening scene sampai product reveal."),
        ("Styling Detail Storyboard",
         "generate_storyboard_frame, frame_type: detail_closeup. "
         "Scene: 'stitching detail of [produk], extreme closeup, artisanal craftsmanship feel'."),
        ("Fashion Film Video",
         "generate_video_from_image. Motion: 'fabric flowing in slow motion breeze, "
         "editorial lighting, model hand smoothing material'. "
         "Model: PixVerse untuk stylized look atau Seedance Pro untuk cinematic."),
    ]))
    story.append(sp(12))

    # ── AFFILIATE ──
    story.append(h2("Workflow D: Content Creator Affiliate"))
    story.append(body(
        "Content creator affiliate harus balancing antara <b>authenticity</b> (agar audience trust) "
        "dan <b>kualitas visual</b> (agar brand mau collaborate). "
        "Fokus pada review jujur, tutorial, dan personal recommendation yang terasa genuine."
    ))
    story.append(sp(6))
    story.append(workflow_steps([
        ("Authentic Product Photo",
         "generate_product_photo dengan style: natural atau contextual. "
         "Hindari terlalu studio-polished — audience affiliate lebih respond ke authentic feel. "
         "extra_prompt: 'personal vanity table, natural window light, everyday setting'."),
        ("Tutorial Storyboard Series",
         "generate_storyboard_frame, frame_type: lifestyle, num_frames: 4. "
         "Scene setiap frame: step 1 cleanse, step 2 serum, step 3 moisturizer, step 4 result. "
         "Ini jadi visual outline untuk tutorial video."),
        ("Comparison Content",
         "generate_storyboard_frame, frame_type: comparison. "
         "Scene: 'before skin with dullness vs after skin with glow, honest realistic comparison'. "
         "Authentic comparison sangat high-converting untuk affiliate."),
        ("Review Video Asset",
         "generate_video_from_image. Motion: 'hand picking up product, natural lighting, "
         "close inspection of product details, casual authentic movement'. "
         "Model: Kling 1.6 untuk natural motion yang realistic."),
        ("Caption-Ready Visual",
         "generate_storyboard_frame, frame_type: text_overlay. "
         "Buat frame dengan negative space di satu sisi untuk ditambahkan review text, "
         "rating, atau affiliate link CTA."),
    ]))
    story.append(sp(6))
    story.append(info_box("Untuk Content Creator Affiliate", [
        "Jangan terlalu 'perfect' — audience affiliate trust konten yang authentic.",
        "Gunakan style 'natural' atau 'contextual' lebih sering dari 'clean_white'.",
        "80% konten harus genuinely helpful (tutorial, review jujur) — 20% promotional.",
        "Comparison dan before-after content selalu high-converting untuk affiliate niche.",
    ], box_type="tip"))
    story.append(sp(12))

    # ── STORYBOARD CAMPAIGN PLANNING ──
    story.append(h2("Workflow E: Full Campaign Storyboard Planning"))
    story.append(body(
        "Gunakan storyboard untuk planning campaign lengkap sebelum eksekusi. "
        "Workflow ini cocok untuk content team yang perlu present campaign plan ke klien "
        "atau internal team approval."
    ))
    story.append(sp(6))
    story.append(workflow_steps([
        ("Define 3-Phase Campaign Structure",
         "Phase 1 - Awareness (Week 1-2): brand_moment + lifestyle frames. "
         "Phase 2 - Education (Week 2-3): detail_closeup + comparison frames. "
         "Phase 3 - Conversion (Week 3-4): product_hero + text_overlay frames."),
        ("Generate Awareness Phase Frames",
         "3-4 frames: brand story opening, lifestyle aspirational, emotional connection scene. "
         "Model: Nano Banana 2 atau FLUX Dev untuk creative interpretation."),
        ("Generate Education Phase Frames",
         "3-4 frames: ingredient detail, how-to usage visual, benefit proof. "
         "Model: FLUX Dev. Pastikan visual clean dan educational."),
        ("Generate Conversion Phase Frames",
         "3-4 frames: product hero shot, before-after, text overlay untuk promo. "
         "Model: FLUX Pro untuk kualitas tertinggi di final phase."),
        ("Compile dan Present",
         "10-15 frames total menjadi complete campaign storyboard deck. "
         "Presentasikan ke klien untuk approval sebelum eksekusi produksi."),
    ]))
    return story


def build_brand_setup():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "11. Brand Setup Guide",
        "Cara menambahkan brand baru ke sistem"
    ))
    story.append(sp(10))

    story.append(body(
        "Setiap brand client memiliki folder tersendiri di sistem. Setup yang baik di awal "
        "akan memastikan semua generate konten konsisten dengan brand identity. "
        "Ikuti langkah berikut untuk onboarding brand baru:"
    ))
    story.append(sp(8))

    story.append(workflow_steps([
        ("Buat folder brand baru",
         "Duplikat folder brands/_template dan rename dengan nama brand "
         "(huruf kecil, tanpa spasi, contoh: brand-abc, skincare-xyz)."),
        ("Isi brand-info.md",
         "File ini adalah 'brain' brand di sistem. Isi dengan: nama brand, "
         "deskripsi produk utama, target audience, tone & personality, "
         "photography style (contoh: 'clean white, soft light, minimal'), "
         "color palette, mood campaign, dan platform target."),
        ("Upload raw photos ke folder raw/",
         "Foto mentah produk dari klien. Format JPG atau PNG. "
         "Pastikan foto cukup terang dan produk terlihat jelas — "
         "AI akan bekerja lebih baik dengan input berkualitas."),
        ("Upload moodboard ke folder moodboard/",
         "Referensi visual: kompetitor yang bagus, aesthetic references, "
         "foto inspirasi. Moodboard membantu kamu saat menulis extra_prompt."),
        ("Verifikasi setup",
         "Jalankan get_brand_info untuk memastikan brand terbaca dengan benar. "
         "Lalu coba generate satu product photo sebagai test."),
    ]))
    story.append(sp(10))

    story.append(h2("Template brand-info.md"))
    story.append(code_block([
        "# [Nama Brand]",
        "",
        "## Brand Overview",
        "- Industry: [Skincare / Fashion / Parfume / FMCG / dll]",
        "- Produk Utama: [Nama dan deskripsi produk]",
        "- Brand Positioning: [Premium / Mass Market / Niche / dll]",
        "",
        "## Target Audience",
        "- Usia: [range usia]",
        "- Gender: [pria / wanita / semua]",
        "- Lifestyle: [deskripsi lifestyle target]",
        "- Pain points: [masalah yang produk ini solve]",
        "",
        "## Visual Identity",
        "- Color Palette: [warna utama dan accent, dengan hex code]",
        "- Photography Style: [clean white / dark moody / natural / editorial]",
        "- Lighting: [soft diffused / dramatic / natural / studio]",
        "- Background: [white / marble / dark / contextual]",
        "",
        "## Campaign Mood",
        "- Tone: [luxurious / playful / professional / authentic]",
        "- Mood Keywords: [glow / fresh / premium / minimal / dll]",
        "- Reference Brands: [brand yang visual aestheticnya mirip]",
        "",
        "## Platform Target",
        "- Primary: [Instagram Feed / TikTok / dll]",
        "- Secondary: [platform lain]",
        "- Content Mix: [% product photo / % lifestyle / % video]",
    ]))
    return story


def build_faq():
    story = []
    story.append(PageBreak())
    story.append(section_band(
        "12. FAQ & Troubleshooting",
        "Jawaban untuk pertanyaan umum dan solusi untuk masalah teknis"
    ))
    story.append(sp(10))

    faqs = [
        ("Berapa lama waktu generate?",
         "Foto: 30-120 detik tergantung model. Video: 30-90 detik. "
         "FLUX Schnell paling cepat. Seedance Pro paling lama tapi kualitas terbaik."),
        ("Kenapa hasilnya tidak sesuai harapan?",
         "Ada 3 hal yang bisa coba: (1) Naikkan strength untuk perubahan lebih besar, "
         "(2) Tambahkan extra_prompt yang lebih spesifik, "
         "(3) Coba model yang berbeda — FLUX Pro atau FLUX Realism sering memberikan hasil berbeda."),
        ("Boleh pakai foto yang sama berkali-kali?",
         "Boleh! Bahkan disarankan. Generate foto yang sama dengan style, mood, atau model berbeda "
         "untuk mendapatkan variasi aset yang kaya untuk satu produk."),
        ("Bagaimana cara mendapatkan hasil yang konsisten?",
         "Gunakan brand-info.md yang terisi lengkap, strength yang sama, dan simpan extra_prompt "
         "yang berhasil di notes untuk digunakan kembali."),
        ("Apakah bisa generate tanpa foto produk?",
         "Ya — generate_storyboard_frame tidak butuh foto sama sekali. "
         "Hanya dari deskripsi teks, sistem akan generate visual concept."),
        ("Error: 'Insufficient credits'",
         "Saldo fal.ai habis. Top up di fal.ai/dashboard/billing. "
         "Minimum $5 untuk mulai generate kembali."),
        ("Error: 'Image not found'",
         "Path foto salah. Pastikan format path benar: brands/[nama-brand]/raw/[nama-file.jpg]. "
         "Gunakan get_brand_info untuk melihat nama file yang tersedia."),
        ("Bagaimana cara discover model terbaru fal.ai?",
         "Gunakan list_available_models dengan search_fal: true. "
         "Sistem akan query langsung ke fal.ai API untuk model terbaru yang tersedia."),
        ("Video output tidak smooth?",
         "Coba: (1) Gunakan Seedance Pro daripada Lite, "
         "(2) Deskripsikan motion yang lebih smooth ('gentle slow motion' bukan 'fast movement'), "
         "(3) Pastikan foto input sudah clean dan terang."),
        ("Apakah output tersimpan otomatis?",
         "Ya. Semua output tersimpan otomatis ke brands/[nama]/generated/[type]/ "
         "dengan naming convention: [brand]_[type]_[platform]_[timestamp].[ext]"),
    ]

    for i, (q, a) in enumerate(faqs):
        bg = BLUE_BG if i % 2 == 0 else WHITE
        t = Table([
            [Paragraph(f"<b>Q: {q}</b>", S["h3"])],
            [Paragraph(f"A: {a}", S["body_left"])],
        ], colWidths=[CONTENT_W])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), bg),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING", (0, 0), (-1, -1), 14),
            ("RIGHTPADDING", (0, 0), (-1, -1), 14),
            ("BOX", (0, 0), (-1, -1), 0.5, BLUE_BORDER),
            ("LINEBEFORE", (0, 0), (0, -1), 3, BLUE),
        ]))
        story.append(t)
        story.append(sp(4))

    story.append(sp(10))
    story.append(divider())
    story.append(sp(8))
    story.append(Paragraph(
        "<b>Socialbrand 1980 Visual Generator</b> — Dibuat untuk mendukung operasional "
        "kreative Socialbrand 1980 dan klien brandnya. "
        f"Dokumentasi ini berlaku untuk Version 2.0 ({datetime.now().strftime('%B %Y')}).",
        ParagraphStyle("footer_note", fontName="Helvetica", fontSize=9,
                       textColor=GRAY_MID, alignment=TA_CENTER, leading=14)
    ))
    story.append(sp(4))
    story.append(Paragraph(
        "Powered by fal.ai  •  Built with FastMCP  •  Socialbrand 1980",
        ParagraphStyle("footer_note2", fontName="Helvetica-Bold", fontSize=9,
                       textColor=BLUE, alignment=TA_CENTER)
    ))
    return story


# ─── BUILD PDF ──────────────────────────────────────────────────────────────
def build_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=2.0 * cm,
        bottomMargin=2.0 * cm,
        title="Socialbrand 1980 — Visual Generator User Guide",
        author="Socialbrand 1980",
        subject="AI Visual Content Generation Guide",
    )

    story = []

    # ── Cover ──
    story.extend(build_cover())
    story.append(PageBreak())

    # ── TOC ──
    story.extend(build_toc())
    story.append(PageBreak())

    # ── Content Sections ──
    story.extend(build_intro())
    story.extend(build_quickstart())
    story.extend(build_tool_product_photo())
    story.extend(build_tool_campaign_photo())
    story.extend(build_tool_video())
    story.extend(build_tool_storyboard())
    story.extend(build_supporting_tools())
    story.extend(build_model_guide())
    story.extend(build_best_practices())
    story.extend(build_workflows())
    story.extend(build_brand_setup())
    story.extend(build_faq())

    def on_first_page(canvas, doc):
        on_page_cover(canvas, doc)

    def on_later_pages(canvas, doc):
        on_page(canvas, doc)

    doc.build(story,
              onFirstPage=on_first_page,
              onLaterPages=on_later_pages)

    print(f"PDF generated: {output_path}")
    import os
    size = os.path.getsize(output_path)
    print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")


if __name__ == "__main__":
    out = "/sessions/exciting-bold-fermi/mnt/Creative-P/Socialbrand_Visual_Generator_Guide.pdf"
    build_pdf(out)