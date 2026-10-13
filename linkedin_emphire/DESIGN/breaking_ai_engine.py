"""Breaking AI series visual engine.

One reusable engine for all 21 articles, matching the article 1 system:

Light system (article 1 templates):
  - save card       1080x1350  light "SAVE THIS CARD" checklist
  - hero portrait   1080x1350  photo + cyan banner + headline with cyan highlight
  - hero landscape  1600x900   photo + name tag + headline with cyan band

Dark system (the dark navy card system, article 2 teaser style):
  - cover           1200x628
  - fig modes       1200x675
  - fig metric      1200x675
  - quote card      1080x1350
  - checklist card  1080x1350
  - share post      1200x675

Usage for any future article:
  from breaking_ai_engine import build_article
  cfg = copy.deepcopy(ARTICLE_2)
  cfg["num"] = 3
  cfg["cards_dir"] = ".../article-3/cards"
  cfg["save_card"]["title_lines"] = [...]
  # ... edit copy, set photo paths ...
  build_article(cfg)

Rules baked in: no em dashes in any copy, the "||" footer separator, one
accent word or number per dark card, no faces on generated assets.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

# ---------------------------------------------------------------- system
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
F_BOLD = f"{FONT_DIR}/DejaVuSans-Bold.ttf"
F_REG = f"{FONT_DIR}/DejaVuSans.ttf"

# dark system
D_BG = (12, 26, 44)
D_GRID = (19, 37, 61)
D_ACCENT = (143, 182, 224)
D_WHITE = (255, 255, 255)
D_MUTED = (130, 150, 172)
D_PANEL = (18, 35, 59)
D_DIVIDER = (26, 44, 70)
D_FOOTER_BG = (166, 193, 225)
D_FOOTER_FG = (12, 26, 44)

# light system (article 1)
L_BG = (244, 246, 249)
L_HEADLINE = (20, 24, 29)
L_SUB = (92, 107, 122)
L_NUM = (169, 199, 228)
L_ROW = (26, 37, 48)
L_HDR_L = (132, 148, 166)
L_HDR_R = (143, 182, 217)
L_DIVIDER = (227, 233, 239)
L_UNDERLINE = (157, 191, 224)
L_FOOTER = (15, 23, 34)
L_HASHTAG = (77, 159, 219)

# hero (shared)
CYAN = (5, 198, 224)  # landscape band, measured from article 1 reference
CYAN_P = (8, 183, 225)  # portrait banner
CYAN_BOX_P = (4, 170, 212)  # portrait highlight boxes
HERO_BLACK = (11, 15, 20)
HERO_WHITE = (255, 255, 255)

SERIES = "BREAKING AI"
AUTHOR = "Olusanya Timothy"
HASHTAG = "#BreakingAI"
FOOTER_TEXT = "OLUSANYA TIMOTHY || SOFTWARE ENGINEER \u00b7 AI RED TEAMING"


def font(size, bold=True):
    return ImageFont.truetype(F_BOLD if bold else F_REG, size)


def spaced_text(draw, xy, text, fnt, fill, spacing=4):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + spacing
    return x


def spaced_width(draw, text, fnt, spacing=4):
    return sum(draw.textlength(ch, font=fnt) for ch in text) + spacing * (len(text) - 1)


def wrap(draw, text, fnt, max_w):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def save(img, cards_dir, name):
    path = Path(cards_dir) / name
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    print("wrote", path.name, img.size)


# ---------------------------------------------------------------- helpers
def dark_base(width, height, grid_every=54):
    img = Image.new("RGB", (width, height), D_BG)
    d = ImageDraw.Draw(img)
    x = grid_every
    while x < width:
        d.line([(x, 0), (x, height)], fill=D_GRID, width=1)
        x += grid_every
    return img, d


def dark_header(d, width, num, total, size=24, y=52, spacing=6):
    left = f"AI RED TEAM LOG \u00b7 EP {num:03d}"
    right = f"BREAKING AI / {num:02d} OF {total:02d}"
    fnt = font(size)
    spaced_text(d, (64, y), left, fnt, D_ACCENT, spacing)
    rw = spaced_width(d, right, fnt, spacing)
    spaced_text(d, (width - 64 - rw, y), right, fnt, D_MUTED, spacing)


def dark_footer(img, width, height, num, total, size=22, bar_h=76, spacing=6):
    d = ImageDraw.Draw(img)
    d.rectangle([(0, height - bar_h), (width, height)], fill=D_FOOTER_BG)
    fnt = font(size)
    spaced_text(d, (64, height - bar_h + (bar_h - size) // 2 - 6), FOOTER_TEXT, fnt, D_FOOTER_FG, spacing)


def cover_photo(photo_path, width, height, darken=0.18):
    img = Image.open(photo_path).convert("RGB")
    scale = max(width / img.width, height / img.height)
    img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
    x = (img.width - width) // 2
    y = (img.height - height) // 2
    img = img.crop((x, y, x + width, y + height))
    img = ImageEnhance.Brightness(img).enhance(1.0 - darken)
    # left-to-right legibility gradient
    grad = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    steps = 60
    for i in range(steps):
        x0 = int(width * i / steps)
        x1 = int(width * (i + 1) / steps)
        a = int(190 * max(0.0, 1.0 - i / (steps * 0.75)))
        gd.rectangle([(x0, 0), (x1, height)], fill=(8, 12, 18, a))
    img = Image.alpha_composite(img.convert("RGBA"), grad).convert("RGB")
    return img


def ink_top_y(fnt, ink_top, bold=True):
    """PIL draws at the em-box top; caps start ~0.203em (bold) or
    ~0.208em (regular) lower in DejaVu. Returns the draw y for a
    desired ink (cap) top."""
    k = 0.203 if bold else 0.208
    return ink_top - int(fnt.size * k)


def render_save_card(cfg):
    c = cfg["save_card"]
    W, H = 1080, 1350
    num, total = cfg["num"], cfg["total"]
    img = Image.new("RGB", (W, H), L_BG)
    d = ImageDraw.Draw(img)
    fnt = font(26)
    spaced_text(d, (64, 72), f"{SERIES} / ARTICLE {num} OF {total}", fnt, L_HDR_L, 4)
    rw = spaced_width(d, "SAVE THIS CARD", fnt, 4)
    spaced_text(d, (W - 64 - rw, 72), "SAVE THIS CARD", fnt, L_HDR_R, 4)

    hf = font(104)
    y = 148
    for line in c["title_lines"]:
        d.text((64, y), line.upper(), font=hf, fill=L_HEADLINE)
        y += 122
    y += 8
    sf = font(38, bold=False)
    for ln in wrap(d, c["subtitle"], sf, W - 128):
        d.text((64, y), ln, font=sf, fill=L_SUB)
        y += 50
    d.rectangle([(64, y + 16), (204, y + 26)], fill=L_UNDERLINE)
    y += 84

    nf, tf = font(36), font(36)
    for i, row in enumerate(c["rows"]):
        d.text((64, y), f"{i + 1:02d}", font=nf, fill=L_NUM)
        lines = wrap(d, row, tf, W - 64 - 150)
        for ln in lines:
            d.text((150, y + 2), ln, font=tf, fill=L_ROW)
            y += 48
        y += 30
        if i < len(c["rows"]) - 1:
            d.line([(64, y - 16), (W - 64, y - 16)], fill=L_DIVIDER, width=2)

    bar_h = 132
    d.rectangle([(0, H - bar_h), (W, H)], fill=L_FOOTER)
    cf = font(30)
    spaced_text(d, (64, H - bar_h + (bar_h - 30) // 2 - 4), c["footer_cta"].upper(), cf, (255, 255, 255), 3)
    hf2 = font(30)
    htw = spaced_width(d, HASHTAG, hf2, 2)
    spaced_text(d, (W - 64 - htw, H - bar_h + (bar_h - 30) // 2 - 4), HASHTAG, hf2, L_HASHTAG, 2)
    save(img, cfg["cards_dir"], f"art{num}_save_card_1080x1350.png")


def render_hero_portrait(cfg):
    """Portrait hero 1122x1402, measured pixel-perfect from the published
    article 1 visual: banner polygon y 68-140 (right edge slants 586 to 534),
    white headline lines x 57 with ink tops 215/334/445, cyan boxes from
    x 46 (text x 69, top pad 27, box h 126, boxes touching), sub lines x 65
    with 60px ink-top pitch starting 51px below the last box."""
    c = cfg["hero_portrait"]
    W, H = 1122, 1402
    img = cover_photo(c["photo"], W, H)
    d = ImageDraw.Draw(img)
        # banner
    d.polygon([(0, 68), (586, 68), (534, 140), (0, 140)], fill=CYAN_P)
    bt = f"{SERIES} \u00b7 ARTICLE {cfg['num']} IS LIVE"
    bs = 30
    while spaced_width(d, bt, font(bs), 4) > 460 and bs > 16:
        bs -= 1
    f_b = font(bs)
    spaced_text(d, (40, 68 + (73 - bs) // 2 - int(bs * 0.203)), bt, f_b, HERO_BLACK, 4)
    for x in (600, 618):
        d.line([(x, 68), (x - 52, 140)], fill=CYAN_P, width=9)
    # headline
    f_head = font(108)
    y_tops = [215, 334, 445]
    for i, line in enumerate(c["white_lines"][:3]):
        d.text((57, ink_top_y(f_head, y_tops[i])), line, font=f_head, fill=HERO_WHITE)
    box_top = 573
    for line in c["box_lines"][:2]:
        tw = d.textlength(line, font=f_head)
        d.rectangle([(46, box_top), (46 + int(tw) + 46, box_top + 126)], fill=CYAN_BOX_P)
        d.text((69, box_top + 27 - int(108 * 0.203)), line, font=f_head, fill=HERO_BLACK)
        box_top += 127
    # sub lines
    f_sub = font(45, bold=False)
    y = box_top + 51
    for ln in c["sub_lines"]:
        d.text((65, ink_top_y(f_sub, y, bold=False)), ln, font=f_sub, fill=HERO_WHITE)
        y += 60
    save(img, cfg["cards_dir"], f"art{cfg['num']}_hero_portrait_1122x1402.png")


def render_hero_landscape(cfg):
    """Landscape hero 1586x992, measured pixel-perfect from the published
    article 1 visual: white name tag box (55,192,510,281), top-right label
    (ink top 49, right margin 60), headline line 1 x 57 ink top 352, cyan
    band (54,447,1272,562) with text ink top 475, sub rule x 54-60 and text
    x 84 with 73px ink-top pitch from 626. Headline font 74 for both lines
    (fits the reference line widths exactly in DejaVu)."""
    c = cfg["hero_landscape"]
    W, H = 1586, 992
    img = cover_photo(c["photo"], W, H)
    d = ImageDraw.Draw(img)
    f_head = font(74)
    f_tag = font(41)
    f_sub = font(53, bold=False)
    f_lab = font(32)
    # name tag
    d.rectangle([(55, 192), (510, 281)], fill=(254, 254, 254))
    d.text((76, ink_top_y(f_tag, 219)), AUTHOR, font=f_tag, fill=HERO_BLACK)
    # top-right label
    label = f"{SERIES} \u00b7 #{cfg['num']:02d}/{cfg['total']}"
    lw = spaced_width(d, label, f_lab, 1)
    spaced_text(d, (W - 60 - lw, ink_top_y(f_lab, 49)), label, f_lab, HERO_WHITE, 1)
    # headline line 1
    lines = c["headline_lines"]
    d.text((57, ink_top_y(f_head, 352)), lines[0], font=f_head, fill=HERO_WHITE)
    # band + line 2
    d.rectangle([(54, 447), (1272, 562)], fill=CYAN)
    d.text((74, ink_top_y(f_head, 475)), lines[1], font=f_head, fill=HERO_BLACK)
    # sub block with left rule
    subs = []
    for s in c["sub_lines"]:
        subs.extend(wrap(d, s, f_sub, W - 84 - 60))
    subs = subs[:3]
    rule_top = 618
    rule_bot = 626 + (len(subs) - 1) * 73 + 50
    d.rectangle([(54, rule_top), (60, rule_bot)], fill=HERO_WHITE)
    for i, ln in enumerate(subs):
        d.text((84, ink_top_y(f_sub, 626 + i * 73, bold=False)), ln, font=f_sub, fill=HERO_WHITE)
    save(img, cfg["cards_dir"], f"art{cfg['num']}_hero_landscape_1586x992.png")


# ---------------------------------------------------------------- dark system
def render_dark_cover(cfg):
    c = cfg["dark_cover"]
    W, H = 1200, 628
    img, d = dark_base(W, H, grid_every=56)
    dark_header(d, W, cfg["num"], cfg["total"])
    f1 = font(76)
    x, y = 64, 130
    for word, accent in c["title_words"]:
        d.text((x, y), word, font=f1, fill=D_ACCENT if accent else D_WHITE)
        x += d.textlength(word, font=f1) + 18
    d.text((64, 236), c["subtitle"], font=font(40, bold=False), fill=D_MUTED)
    cf = font(22)
    x, cy = 64, 356
    for num, label in c["chips"]:
        box_w = 200
        d.rounded_rectangle([(x, cy), (x + box_w, cy + 92)], radius=10, outline=D_ACCENT, width=2)
        d.text((x + 18, cy + 16), num, font=cf, fill=D_ACCENT)
        d.text((x + 18, cy + 50), label, font=cf, fill=D_WHITE)
        x += box_w + 16
    dark_footer(img, W, H, cfg["num"], cfg["total"])
    save(img, cfg["cards_dir"], f"art{cfg['num']}_cover_1200x628.png")


def render_dark_fig_rows(cfg):
    c = cfg["dark_fig_rows"]
    W, H = 1200, 675
    img, d = dark_base(W, H, grid_every=56)
    dark_header(d, W, cfg["num"], cfg["total"], y=50)
    d.text((64, 96), c["title"], font=font(52), fill=D_WHITE)
    nf, tf, df = font(34), font(30), font(26, bold=False)
    y = 184
    rows = c["rows"]
    for i, (num, title, desc) in enumerate(rows):
        d.text((64, y), num, font=nf, fill=D_ACCENT)
        d.text((150, y + 2), title, font=tf, fill=D_WHITE)
        d.text((150, y + 40), desc, font=df, fill=D_MUTED)
        if i < len(rows) - 1:
            d.line([(64, y + 78), (W - 64, y + 78)], fill=D_DIVIDER, width=1)
        y += 82
    dark_footer(img, W, H, cfg["num"], cfg["total"])
    save(img, cfg["cards_dir"], f"art{cfg['num']}_fig1_five_modes_1200x675.png")


def render_dark_fig_metric(cfg):
    c = cfg["dark_fig_metric"]
    W, H = 1200, 675
    img, d = dark_base(W, H, grid_every=56)
    dark_header(d, W, cfg["num"], cfg["total"], y=50)
    d.text((64, 108), c["title"], font=font(52), fill=D_WHITE)
    spaced_text(d, (64, 200), c["left_label"], font(22), D_MUTED)
    body = font(26, bold=False)
    y = 250
    for item in c["left_items"]:
        d.ellipse([(68, y + 12), (80, y + 24)], fill=D_MUTED)
        for ln in wrap(d, item, body, 452):
            d.text((104, y), ln, font=body, fill=D_WHITE)
            y += 34
        y += 26
    px0, px1, py0, py1 = 620, W - 64, 196, 576
    d.rounded_rectangle([(px0, py0), (px1, py1)], radius=12, fill=D_PANEL)
    d.line([(px0, py0 + 12), (px0, py1 - 12)], fill=D_ACCENT, width=4)
    spaced_text(d, (px0 + 40, py0 + 30), c["panel_label"], font(22), D_ACCENT)
    d.text((px0 + 40, py0 + 76), c["panel_stat"], font=font(88), fill=D_ACCENT)
    sf = font(27, bold=False)
    for i, ln in enumerate(wrap(d, c["panel_text"], sf, 480)):
        d.text((px0 + 40, py0 + 196 + i * 38), ln, font=sf, fill=D_WHITE)
    sub = font(24, bold=False)
    for i, ln in enumerate(wrap(d, c["panel_sub"], sub, 480)):
        d.text((px0 + 40, py0 + 300 + i * 34), ln, font=sub, fill=D_MUTED)
    dark_footer(img, W, H, cfg["num"], cfg["total"])
    save(img, cfg["cards_dir"], f"art{cfg['num']}_fig2_metric_1200x675.png")


def render_dark_quote(cfg):
    c = cfg["dark_quote"]
    W, H = 1080, 1350
    img, d = dark_base(W, H)
    dark_header(d, W, cfg["num"], cfg["total"], size=22, y=64, spacing=4)
    big = font(56)
    line_h, x0, max_w = 72, 64, W - 128
    y = 190
    for ln in wrap(d, c["lead"], big, max_w):
        d.text((x0, y), ln, font=big, fill=D_WHITE)
        y += line_h
    y += 24
    words = []
    for t, accent in c["body_parts"]:
        for w in t.split(" "):
            if w:
                words.append((w, D_ACCENT if accent else D_WHITE))
    space_w = d.textlength(" ", font=big)
    lines, cur, cur_w = [], [], 0.0
    for w, col in words:
        wlen = d.textlength(w, font=big)
        need = (space_w if cur else 0) + wlen
        if cur and cur_w + need > max_w:
            lines.append(cur)
            cur, cur_w = [(w, col)], wlen
        else:
            cur.append((w, col))
            cur_w += need
    if cur:
        lines.append(cur)
    for line in lines:
        x = x0
        for j, (w, col) in enumerate(line):
            d.text((x, y), w, font=big, fill=col)
            x += d.textlength(w, font=big)
            if j < len(line) - 1:
                x += space_w
        y += line_h
    y += 40
    lab = font(18)
    spaced_text(d, (x0, H - 210), c["label"], lab, D_ACCENT, 3)
    dark_footer(img, W, H, cfg["num"], cfg["total"], size=20, bar_h=96, spacing=3)
    save(img, cfg["cards_dir"], f"art{cfg['num']}_card2_quote_1080x1350.png")


def render_dark_checklist(cfg):
    c = cfg["dark_checklist"]
    W, H = 1080, 1350
    img, d = dark_base(W, H)
    dark_header(d, W, cfg["num"], cfg["total"], size=22, y=64, spacing=4)
    t = font(80)
    d.text((64, 150), c["title_top"], font=t, fill=D_WHITE)
    d.text((64, 250), c["title_accent"], font=t, fill=D_ACCENT)
    uw = d.textlength(c["title_accent"], font=t)
    d.rectangle([(64, 356), (64 + uw, 366)], fill=D_ACCENT)
    nf, tf = font(40), font(34)
    y = 440
    for i, item in enumerate(c["items"], 1):
        d.text((64, y), f"{i:02d}", font=nf, fill=D_ACCENT)
        for ln in wrap(d, item, tf, W - 64 - 150):
            d.text((150, y + 2), ln, font=tf, fill=D_WHITE)
            y += 46
        y += 34
    dark_footer(img, W, H, cfg["num"], cfg["total"], size=20, bar_h=96, spacing=3)
    save(img, cfg["cards_dir"], f"art{cfg['num']}_card3_checklist_1080x1350.png")


def render_dark_share(cfg):
    c = cfg["dark_share"]
    W, H = 1200, 675
    img, d = dark_base(W, H, grid_every=56)
    dark_header(d, W, cfg["num"], cfg["total"], y=50)
    t = font(92)
    d.text((64, 140), c["title_main"], font=t, fill=D_WHITE)
    d.text((64 + d.textlength(c["title_main"], font=t) + 20, 140), c["title_accent"], font=t, fill=D_ACCENT)
    f2 = font(36)
    y = 272
    for ln in wrap(d, c["subtitle"], f2, W - 128):
        d.text((64, y), ln, font=f2, fill=D_WHITE)
        y += 48
    f3 = font(29, bold=False)
    for i, line in enumerate(c["sub_lines"]):
        d.text((64, y + 30 + i * 46), line, font=f3, fill=D_MUTED)
    for i in range(5):
        col = D_ACCENT if i == 0 else D_DIVIDER
        d.ellipse([(64 + i * 44, y + 30 + len(c["sub_lines"]) * 46 + 40),
                   (64 + i * 44 + 18, y + 30 + len(c["sub_lines"]) * 46 + 58)], fill=col)
    dark_footer(img, W, H, cfg["num"], cfg["total"])
    save(img, cfg["cards_dir"], f"art{cfg['num']}_share_post_1200x675.png")


# ---------------------------------------------------------------- builder
def build_article(cfg, systems=("light", "dark")):
    if "light" in systems:
        render_save_card(cfg)
        render_hero_portrait(cfg)
        render_hero_landscape(cfg)
    if "dark" in systems:
        render_dark_cover(cfg)
        render_dark_fig_rows(cfg)
        render_dark_fig_metric(cfg)
        render_dark_quote(cfg)
        render_dark_checklist(cfg)
        render_dark_share(cfg)
    print("article", cfg["num"], "complete")


# ---------------------------------------------------------------- article 2 config
def _art2_cards_dir():
    return str(
        Path(__file__).resolve().parent.parent
        / "ARTICLES" / "2026-10-13_article-2_five-boring-failure-modes" / "cards"
    )


ARTICLE_2 = {
    "num": 2,
    "total": 21,
    "cards_dir": _art2_cards_dir(),
    "save_card": {
        "title_lines": ["The five-point", "checklist"],
        "subtitle": "Run all five on your own AI feature this week.",
        "rows": [
            "Secrets are out of the prompt. Test three direct injections.",
            "Every retrieved document is data, not instructions. Test one poisoned document.",
            "Tool descriptions are reviewed and pinned. Test one hidden instruction.",
            "Test your refusals in the languages your users use, mixed in one message.",
            "Track the three failures that hurt most, with sample sizes.",
        ],
        "footer_cta": "Test before the customer does.",
    },
    "hero_portrait": {
        "photo": _art2_cards_dir() + "/photos/art2_hero_portrait.jpg",
        "white_lines": ["Five Boring", "Failures", "Ship With Your"],
        "box_lines": ["AI Feature"],
        "sub_lines": ["Tested on my own support bot.", "The five failure modes, live now."],
    },
    "hero_landscape": {
        "photo": _art2_cards_dir() + "/photos/art2_hero_landscape.jpg",
        "headline_lines": ["Your AI Feature Will Not Die", "In a Movie-Style Hack"],
        "sub_lines": [
            "It will die on a boring Tuesday.",
            "The five boring failure modes.",
            "Article 2 of 21. Live today.",
        ],
    },
    "dark_cover": {
        "title_words": [("The", False), ("five", False), ("boring", True), ("failures", False)],
        "subtitle": "that will ship with your AI feature",
        "chips": [("01", "The prompt"), ("02", "The retrieval"), ("03", "The tools"),
                  ("04", "The language"), ("05", "The metric")],
    },
    "dark_fig_rows": {
        "title": "The five, in the order I check them",
        "rows": [
            ("01", "The prompt is not a wall", "A protection paragraph is a suggestion."),
            ("02", "Your retrieval is untrusted input", "A retrieved chunk can carry instructions."),
            ("03", "Your tools are trusted unread", "The description itself is an attack surface."),
            ("04", "Your bot speaks one language well", "Safety tested in English, used in three languages."),
            ("05", "You are measuring the wrong thing", "Three hundred tests and twelve issues is not progress."),
        ],
    },
    "dark_fig_metric": {
        "title": "The metric that matters",
        "left_label": "WHAT WASTES YOUR TIME",
        "left_items": [
            "The raw number of tests run, with no risk weighting",
            "Total vulnerabilities found, as if more is better",
            "A pass rate with no sample size behind it",
        ],
        "panel_label": "THE NUMBER THAT PAYS",
        "panel_stat": "1 in 40",
        "panel_text": "a bug that fires one time in forty for Pidgin speakers is more useful than any total",
        "panel_sub": "Track the three failures that would hurt most, with sample sizes.",
    },
    "dark_quote": {
        "lead": "Your AI feature will not die in a movie-style hack.",
        "body_parts": [
            ("It will die on a ", False),
            ("boring Tuesday,", True),
            (" when a customer pastes something you never tested and your bot does exactly what it was never supposed to do.", False),
        ],
        "label": "THE FIVE BORING FAILURES THAT WILL SHIP WITH YOUR AI FEATURE",
    },
    "dark_checklist": {
        "title_top": "The five-point",
        "title_accent": "checklist.",
        "items": [
            "Secrets are out of the prompt. Test three direct injections.",
            "Every retrieved document is data, not instructions. Test one poisoned document.",
            "Tool descriptions are reviewed and pinned. Test one hidden instruction.",
            "Test your refusals in the languages your users use, mixed in one message.",
            "Track the three failures that hurt most, with sample sizes.",
        ],
    },
    "dark_share": {
        "title_main": "Article 2 is",
        "title_accent": "live.",
        "subtitle": "The five boring failures that will ship with your AI feature.",
        "sub_lines": [
            "Four real lab results from my own support bot. Nothing smoothed.",
            "Run the five tests this week. Tell me which one broke first.",
        ],
    },
}


if __name__ == "__main__":
    build_article(copy.deepcopy(ARTICLE_2))
