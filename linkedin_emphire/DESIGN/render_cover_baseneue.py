"""Render the Article 2 landscape hero cover in Basis Neue (Expanded).

The Drive folder only holds the TRIAL Base Neue, and the trial watermarks
certain punctuation glyphs (hyphen, slash, middle dot, #) with foundry
text. So letters and digits are drawn in Base Neue, and only the non
alphanumeric symbols fall back to DejaVu (visually identical). This keeps
the locked copy exact and clean. Geometry + background treatment are the
locked template from breaking_ai_engine. Does not modify the engine.
"""
import sys
sys.path.insert(0, "/home/user/linkedin_emphire/linkedin_emphire/DESIGN")
from PIL import Image, ImageDraw, ImageFont
from breaking_ai_engine import (
    cover_photo, wrap, CYAN, CYAN_P, CYAN_BOX_P, HERO_BLACK, HERO_WHITE,
    AUTHOR, SERIES,
)

FONT_BOLD = "/home/user/linkedin_emphire/linkedin_emphire/DESIGN/fonts/BasisNeueExpanded-Bold.ttf"
FONT_REG = "/home/user/linkedin_emphire/linkedin_emphire/DESIGN/fonts/BasisNeueExpanded-Regular.ttf"
DEJAVU_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
DEJAVU_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
PHOTO = ("/home/user/linkedin_emphire/linkedin_emphire/ARTICLES/"
         "2026-10-13_article-2_five-boring-failure-modes/cards/photos/art2_hero_landscape_v3.jpg")
OUT = ("/home/user/linkedin_emphire/linkedin_emphire/ARTICLES/"
       "2026-10-13_article-2_five-boring-failure-modes/cards/"
       "art2_hero_landscape_baseneue_1586x992.png")

NUM, TOTAL = 2, 21


def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def fbfont(size, bold=True):
    return ImageFont.truetype(DEJAVU_BOLD if bold else DEJAVU_REG, size)


def use_bn(ch):
    return ch.isalnum() or ch == " "


def mixed_width(d, text, fnt, fnt_fb, spacing=0):
    tot = 0.0
    for ch in text:
        f = fnt if use_bn(ch) else fnt_fb
        tot += d.textlength(ch, font=f)
    return tot + spacing * (len(text) - 1)


def draw_mixed(d, x, y, text, fnt, fill, fnt_fb, spacing=0):
    for ch in text:
        f = fnt if use_bn(ch) else fnt_fb
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + spacing
    return x


_cap_cache = {}


def cap_top_offset(fnt, sample="HI"):
    key = (fnt.path, fnt.size)
    if key in _cap_cache:
        return _cap_cache[key]
    w = max(10, int(fnt.getlength(sample)) + 40)
    h = int(fnt.size) * 2
    im = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(im)
    ydraw = h // 2
    d.text((20, ydraw), sample, font=fnt, fill=255)
    bb = im.getbbox()
    off = (bb[1] - ydraw) if bb else 0
    _cap_cache[key] = off
    return off


def ink_top_y(fnt, ink_top):
    return ink_top - cap_top_offset(fnt)


def fit(d, text, start, min_size, max_width, bold=True, spacing=0):
    size = start
    while size > min_size:
        f, fb = font(size, bold), fbfont(size, bold)
        if mixed_width(d, text, f, fb, spacing) <= max_width:
            return size, f, fb
        size -= 1
    return min_size, font(min_size, bold), fbfont(min_size, bold)


def fit_two(d, t1, w1, t2, w2, start, min_size, bold=True):
    size = start
    while size > min_size:
        f, fb = font(size, bold), fbfont(size, bold)
        if (mixed_width(d, t1, f, fb) <= w1 and mixed_width(d, t2, f, fb) <= w2):
            return size, f, fb
        size -= 1
    return min_size, font(min_size, bold), fbfont(min_size, bold)


HEADLINE = ["Your AI Feature Will Not Die", "In A Movie-Style Hack"]
SUBS = [
    "It will die on a boring Tuesday.",
    "The five boring failure modes.",
    "Article 2 of 21. Live today.",
]
FACE_LEFT = 1147  # woman's face left edge in canvas px (measured from v3 bg)


def render(clear):
    W, H = 1586, 992
    img = cover_photo(PHOTO, W, H)
    d = ImageDraw.Draw(img)

    # name tag (fixed white box)
    d.rectangle([(55, 192), (510, 281)], fill=(254, 254, 254))
    _, f_tag, fb_tag = fit(d, AUTHOR, 41, 24, 510 - 76 - 21, bold=True)
    draw_mixed(d, 76, ink_top_y(f_tag, 219), AUTHOR, f_tag, HERO_BLACK, fb_tag)

    # top-right label (right aligned, 1px spacing)
    label = f"{SERIES} \u00b7 #{NUM:02d}/{TOTAL}"
    _, f_lab, fb_lab = fit(d, label, 32, 18, 640, bold=True, spacing=1)
    lw = mixed_width(d, label, f_lab, fb_lab, 1)
    draw_mixed(d, W - 60 - lw, ink_top_y(f_lab, 49), label, f_lab, HERO_WHITE, fb_lab, 1)

    # headline: line 1 white, line 2 in the cyan box, common size
    if clear:
        l1cap = (FACE_LEFT - 47) - 57  # keep line 1 clear of the face
    else:
        l1cap = W - 57 - 60
    h_size, f_head, fb_head = fit_two(d, HEADLINE[0], l1cap,
                                      HEADLINE[1], 1272 - 74 - 20, 74, 40, bold=True)
    draw_mixed(d, 57, ink_top_y(f_head, 352), HEADLINE[0], f_head, HERO_WHITE, fb_head)
    d.rectangle([(54, 447), (1272, 562)], fill=CYAN)
    draw_mixed(d, 74, ink_top_y(f_head, 475), HEADLINE[1], f_head, HERO_BLACK, fb_head)

    # sub block (left rule + lines)
    if clear:
        sub_size = max(32, int(round(h_size * 0.74)))
        pitch = int(round(sub_size * 1.38))
    else:
        sub_size, pitch = 53, 73
    f_sub, fb_sub = font(sub_size, False), fbfont(sub_size, False)
    wrap_w = W - 84 - 60
    while sub_size > 30 and max(mixed_width(d, s, f_sub, fb_sub) for s in SUBS) > wrap_w:
        sub_size -= 1
        f_sub, fb_sub = font(sub_size, False), fbfont(sub_size, False)
    wl = []
    for s in SUBS:
        wl.extend(wrap(d, s, f_sub, wrap_w))
    wl = wl[:3]
    rule_top = 618
    rule_bot = 626 + (len(wl) - 1) * pitch + int(sub_size * 0.95)
    d.rectangle([(54, rule_top), (60, rule_bot)], fill=HERO_WHITE)
    for i, ln in enumerate(wl):
        draw_mixed(d, 84, ink_top_y(f_sub, 626 + i * pitch), ln, f_sub, HERO_WHITE, fb_sub)

    out = OUT.replace(".png", "_clear.png") if clear else OUT
    img.save(out)
    print(("clear" if clear else "big"), "headline", h_size, "sub", sub_size, "->", out)


def cap_height(fnt, sample="HI"):
    h = int(fnt.size) * 2
    im = Image.new("L", (40, h), 0)
    dd = ImageDraw.Draw(im)
    dd.text((10, fnt.size), sample, font=fnt, fill=255)
    bb = im.getbbox()
    return (bb[3] - bb[1]) if bb else int(fnt.size * 0.7)


def render_portrait():
    W, H = 1122, 1402
    photo = ("/home/user/linkedin_emphire/linkedin_emphire/ARTICLES/"
             "2026-10-13_article-2_five-boring-failure-modes/cards/photos/"
             "art2_hero_portrait_cinematic.jpg")
    img = cover_photo(photo, W, H)
    d = ImageDraw.Draw(img)
    white_lines = ["Five Boring", "Failures", "Ship With Your"]
    box_lines = ["AI Feature"]
    sub_lines = ["Tested on my own support bot.", "The five failure modes, live now."]

    # banner
    d.polygon([(0, 68), (586, 68), (534, 140), (0, 140)], fill=CYAN_P)
    bt = f"{SERIES} \u00b7 ARTICLE {NUM} IS LIVE"
    _, f_b, fb_b = fit(d, bt, 30, 16, 460, bold=True, spacing=4)
    b_ink = 68 + (72 - cap_height(f_b)) // 2
    draw_mixed(d, 40, ink_top_y(f_b, b_ink), bt, f_b, HERO_BLACK, fb_b, 4)
    for x in (600, 618):
        d.line([(x, 68), (x - 52, 140)], fill=CYAN_P, width=9)

    # headline: auto-fit the longest white line
    _, f_head, fb_head = fit(d, white_lines[2], 108, 60, 980, bold=True)
    for i, line in enumerate(white_lines):
        draw_mixed(d, 57, ink_top_y(f_head, [215, 334, 445][i]), line, f_head, HERO_WHITE, fb_head)

    # cyan box
    box_top = 573
    for line in box_lines:
        tw = mixed_width(d, line, f_head, fb_head)
        d.rectangle([(46, box_top), (46 + int(tw) + 46, box_top + 126)], fill=CYAN_BOX_P)
        draw_mixed(d, 69, ink_top_y(f_head, box_top + 27), line, f_head, HERO_BLACK, fb_head)
        box_top += 127

    # sub
    f_sub, fb_sub = font(45, False), fbfont(45, False)
    y = box_top + 51
    for ln in sub_lines:
        draw_mixed(d, 65, ink_top_y(f_sub, y), ln, f_sub, HERO_WHITE, fb_sub)
        y += 60

    out = ("/home/user/linkedin_emphire/linkedin_emphire/ARTICLES/"
           "2026-10-13_article-2_five-boring-failure-modes/cards/"
           "art2_hero_portrait_baseneue_1122x1402.png")
    img.save(out)
    print("portrait headline", f_head.size, "->", out)


if __name__ == "__main__":
    render(False)
    render(True)
    render_portrait()
