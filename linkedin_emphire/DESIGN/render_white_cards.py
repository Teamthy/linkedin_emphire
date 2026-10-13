"""Render article 2 in-article cards on plain white, in Base Neue Expanded.

Re-skins the navy card system to a plain white background with Base Neue
(letters/digits in Base Neue, non-alnum symbols in DejaVu to dodge the trial
watermark). Copy and layouts are reused from the engine's ARTICLE_2 config;
the original navy cards are left untouched (outputs use a _white suffix).
All text auto-fits its box so the wider Expanded typeface never overflows.
"""
import sys
sys.path.insert(0, "/home/user/linkedin_emphire/linkedin_emphire/DESIGN")
from PIL import Image, ImageDraw
from breaking_ai_engine import ARTICLE_2, FOOTER_TEXT, HASHTAG, wrap
from render_cover_baseneue import font, fbfont, mixed_width, draw_mixed, fit

CFG = ARTICLE_2
CARDS = CFG["cards_dir"]
NUM, TOTAL = CFG["num"], CFG["total"]

# white palette
WBG = (255, 255, 255)
HEAD = (15, 25, 40)     # near-black navy (titles, primary text)
SUB = (95, 110, 126)    # gray (secondary / descriptions)
ACC = (0, 140, 165)     # teal-cyan accent (numbers, accent words, stat)
BAR = (5, 198, 224)     # bright cyan (bars / underlines / bullets)
DIV = (225, 232, 238)   # light divider
HDR = (110, 125, 141)   # header label text
FOOTB = (12, 26, 44)    # footer bar
FOOTF = (255, 255, 255) # footer text
PANEL = (241, 246, 250) # panel fill
PNLBD = (223, 231, 238) # panel border


def header(d, Wd, size=24, y=50, sp=6):
    left = f"AI RED TEAM LOG \u00b7 EP {NUM:03d}"
    right = f"BREAKING AI / {NUM:02d} OF {TOTAL:02d}"
    maxw = Wd - 128 - 60  # 60px gap between the two labels
    s = size
    while s > 14:
        f, fb = font(s), fbfont(s)
        if mixed_width(d, left, f, fb, sp) + mixed_width(d, right, f, fb, sp) <= maxw:
            break
        s -= 1
    f, fb = font(s), fbfont(s)
    draw_mixed(d, 64, y, left, f, HDR, fb, sp)
    rw = mixed_width(d, right, f, fb, sp)
    draw_mixed(d, Wd - 64 - rw, y, right, f, HDR, fb, sp)


def footer(img, Wd, Hd, size=22, bar_h=76, sp=6):
    d = ImageDraw.Draw(img)
    d.rectangle([(0, Hd - bar_h), (Wd, Hd)], fill=FOOTB)
    maxw = Wd - 128
    s = size
    while s > 12:
        f, fb = font(s), fbfont(s)
        if mixed_width(d, FOOTER_TEXT, f, fb, sp) <= maxw:
            break
        s -= 1
    f, fb = font(s), fbfont(s)
    draw_mixed(d, 64, Hd - bar_h + (bar_h - s) // 2 - 4, FOOTER_TEXT, f, FOOTF, fb, sp)


def fit_block(d, lines, start, min_size, max_w, bold=True):
    s = start
    while s > min_size:
        f, fb = font(s, bold), fbfont(s, bold)
        if max(mixed_width(d, ln, f, fb) for ln in lines) <= max_w:
            return s, f, fb
        s -= 1
    f, fb = font(min_size, bold), fbfont(min_size, bold)
    return min_size, f, fb


def save(img, name):
    img.save(f"{CARDS}/{name}")
    print("wrote", name, img.size)


def fig1():
    c = CFG["dark_fig_rows"]; Wd, Hd = 1200, 675
    img = Image.new("RGB", (Wd, Hd), WBG); d = ImageDraw.Draw(img)
    header(d, Wd, 24, 50, 6)
    _, f, fb = fit(d, c["title"], 52, 30, Wd - 128, bold=True)
    draw_mixed(d, 64, 96, c["title"], f, HEAD, fb)
    nf, tf, df = font(34), font(30), font(26, False)
    nfb, tfb, dfb = fbfont(34), fbfont(30), fbfont(26, False)
    y = 184
    for i, (num, title, desc) in enumerate(c["rows"]):
        draw_mixed(d, 64, y, num, nf, ACC, nfb)
        draw_mixed(d, 150, y + 2, title, tf, HEAD, tfb)
        draw_mixed(d, 150, y + 40, desc, df, SUB, dfb)
        if i < len(c["rows"]) - 1:
            d.line([(64, y + 78), (Wd - 64, y + 78)], fill=DIV, width=1)
        y += 82
    footer(img, Wd, Hd)
    save(img, "art2_fig1_white_1200x675.png")


def fig2():
    c = CFG["dark_fig_metric"]; Wd, Hd = 1200, 675
    img = Image.new("RGB", (Wd, Hd), WBG); d = ImageDraw.Draw(img)
    header(d, Wd, 24, 50, 6)
    _, f, fb = fit(d, c["title"], 52, 30, Wd - 128, bold=True)
    draw_mixed(d, 64, 108, c["title"], f, HEAD, fb)
    lf, lfb = font(22), fbfont(22)
    draw_mixed(d, 64, 200, c["left_label"], lf, ACC, lfb)
    body, bodyfb = font(26, False), fbfont(26, False)
    y = 250
    for item in c["left_items"]:
        d.ellipse([(68, y + 12), (80, y + 24)], fill=ACC)
        for ln in wrap(d, item, body, 452):
            draw_mixed(d, 104, y, ln, body, HEAD, bodyfb)
            y += 34
        y += 26
    px0, px1, py0, py1 = 600, Wd - 64, 196, 588
    d.rounded_rectangle([(px0, py0), (px1, py1)], radius=12, fill=PANEL, outline=PNLBD, width=2)
    d.rectangle([(px0, py0 + 12), (px0 + 6, py1 - 12)], fill=BAR)
    plf, plfb = font(22), fbfont(22)
    draw_mixed(d, px0 + 40, py0 + 30, c["panel_label"], plf, ACC, plfb)
    sf, sfb = font(80), fbfont(80)
    draw_mixed(d, px0 + 40, py0 + 60, c["panel_stat"], sf, ACC, sfb)
    tf2, tfb2 = font(23, False), fbfont(23, False)
    pt = wrap(d, c["panel_text"], tf2, 470)
    for i, ln in enumerate(pt):
        draw_mixed(d, px0 + 40, py0 + 168 + i * 31, ln, tf2, HEAD, tfb2)
    subf, subfb = font(20, False), fbfont(20, False)
    ss = py0 + 168 + len(pt) * 31 + 12
    for i, ln in enumerate(wrap(d, c["panel_sub"], subf, 470)):
        draw_mixed(d, px0 + 40, ss + i * 27, ln, subf, SUB, subfb)
    footer(img, Wd, Hd)
    save(img, "art2_fig2_white_1200x675.png")


def card1():
    Wd, Hd = 1080, 1350
    img = Image.new("RGB", (Wd, Hd), WBG); d = ImageDraw.Draw(img)
    header(d, Wd, 24, 88, 6)
    title_lines = [("The scary AI", False), ("failures are", False), ("boring.", True)]
    _, f, fb = fit_block(d, [t for t, _ in title_lines], 150, 90, Wd - 128, bold=True)
    y = 182
    for t, acc in title_lines:
        draw_mixed(d, 64, y, t, f, ACC if acc else HEAD, fb)
        if acc:
            lw = int(mixed_width(d, t, f, fb))
            uy = y + int(f.size * 0.94)
            d.rectangle([(64, uy), (64 + lw, uy + 11)], fill=BAR)
        y += int(f.size * 1.05)
    bullets = [
        "The prompt is not a wall.",
        "The retrieval is unchecked input.",
        "The tools are trusted without being read.",
    ]
    _, bf, bfb = fit_block(d, bullets, 34, 26, Wd - 112 - 64, bold=True)
    y += 40
    for b in bullets:
        d.ellipse([(68, y + 14), (84, y + 30)], fill=BAR)
        draw_mixed(d, 112, y, b, bf, HEAD, bfb)
        y += 96
    botf, botfb = font(40), fbfont(40)
    by = Hd - 300
    draw_mixed(d, 64, by, "5 modes. 5 prompts. 5 fixes.", botf, HEAD, botfb)
    draw_mixed(d, 64, by + 54, "Tomorrow, 10 AM WAT.", botf, HEAD, botfb)
    footer(img, Wd, Hd)
    save(img, "art2_card1_white_1080x1350.png")


def card2():
    c = CFG["dark_quote"]; Wd, Hd = 1080, 1350
    img = Image.new("RGB", (Wd, Hd), WBG); d = ImageDraw.Draw(img)
    header(d, Wd, 22, 64, 4)
    big, bigfb = font(56), fbfont(56)
    x0, maxw, lh = 64, Wd - 128, 72
    y = 190
    for ln in wrap(d, c["lead"], big, maxw):
        draw_mixed(d, x0, y, ln, big, HEAD, bigfb); y += lh
    y += 24
    words = []
    for t, acc in c["body_parts"]:
        for w in t.split(" "):
            if w:
                words.append((w, ACC if acc else HEAD))
    space_w = d.textlength(" ", font=big)

    def wwd(w):
        return mixed_width(d, w, big, bigfb)

    lines, cur, curw = [], [], 0.0
    for w, col in words:
        wl = wwd(w)
        need = (space_w if cur else 0) + wl
        if cur and curw + need > maxw:
            lines.append(cur); cur, curw = [(w, col)], wl
        else:
            cur.append((w, col)); curw += need
    if cur:
        lines.append(cur)
    for line in lines:
        x = x0
        for j, (w, col) in enumerate(line):
            draw_mixed(d, x, y, w, big, col, bigfb)
            x += wwd(w)
            if j < len(line) - 1:
                x += space_w
        y += lh
    labf, labfb = font(18), fbfont(18)
    draw_mixed(d, x0, Hd - 210, c["label"], labf, ACC, labfb, 3)
    footer(img, Wd, Hd, size=20, bar_h=96, sp=3)
    save(img, "art2_card2_white_1080x1350.png")


def card3():
    c = CFG["dark_checklist"]; Wd, Hd = 1080, 1350
    img = Image.new("RGB", (Wd, Hd), WBG); d = ImageDraw.Draw(img)
    header(d, Wd, 22, 64, 4)
    _, t, tfb = fit_block(d, [c["title_top"], c["title_accent"]], 80, 56, Wd - 128, bold=True)
    draw_mixed(d, 64, 150, c["title_top"], t, HEAD, tfb)
    draw_mixed(d, 64, 150 + int(t.size * 1.24), c["title_accent"], t, ACC, tfb)
    uw = int(mixed_width(d, c["title_accent"], t, tfb))
    uy = 150 + int(t.size * 1.24) + int(t.size * 1.0)
    d.rectangle([(64, uy), (64 + uw, uy + 10)], fill=BAR)
    _, nf, nfb = fit_block(d, [f"{i:02d}" for i in range(1, 6)], 40, 28, 150, bold=True)
    _, tf, tfb2 = fit_block(d, c["items"], 34, 24, Wd - 64 - 150, bold=True)
    y = 440
    for i, item in enumerate(c["items"], 1):
        draw_mixed(d, 64, y, f"{i:02d}", nf, ACC, nfb)
        for ln in wrap(d, item, tf, Wd - 64 - 150):
            draw_mixed(d, 150, y + 2, ln, tf, HEAD, tfb2)
            y += int(tf.size * 1.32)
        y += 34
    footer(img, Wd, Hd, size=20, bar_h=96, sp=3)
    save(img, "art2_card3_white_1080x1350.png")


def save_card():
    c = CFG["save_card"]; Wd, Hd = 1080, 1350
    img = Image.new("RGB", (Wd, Hd), WBG); d = ImageDraw.Draw(img)
    fnt, fntfb = font(24), fbfont(24)
    draw_mixed(d, 64, 72, f"BREAKING AI / ARTICLE {NUM} OF {TOTAL}", fnt, HDR, fntfb, 4)
    rw = mixed_width(d, "SAVE THIS CARD", fnt, fntfb, 4)
    draw_mixed(d, Wd - 64 - rw, 72, "SAVE THIS CARD", fnt, ACC, fntfb, 4)
    uppers = [L.upper() for L in c["title_lines"]]
    _, hf, hfb = fit_block(d, uppers, 92, 58, Wd - 128, bold=True)
    y = 148
    for line in uppers:
        draw_mixed(d, 64, y, line, hf, HEAD, hfb); y += int(hf.size * 1.14)
    y += 6
    sf, sfb = font(36, False), fbfont(36, False)
    for ln in wrap(d, c["subtitle"], sf, Wd - 128):
        draw_mixed(d, 64, y, ln, sf, SUB, sfb); y += 46
    d.rectangle([(64, y + 14), (204, y + 24)], fill=BAR)
    y += 68
    rows = c["rows"]
    bar_h = 100
    footer_top = Hd - bar_h
    gap = 24
    rsize = 32
    while rsize > 24:
        tfx = font(rsize)
        total = sum(len(wrap(d, r, tfx, Wd - 64 - 150)) * int(rsize * 1.36) + gap for r in rows)
        if total <= footer_top - y - 14:
            break
        rsize -= 1
    rf, rfb = font(rsize), fbfont(rsize)
    for i, row in enumerate(rows):
        draw_mixed(d, 64, y, f"{i + 1:02d}", rf, ACC, rfb)
        yy = y
        for ln in wrap(d, row, rf, Wd - 64 - 150):
            draw_mixed(d, 150, yy + 2, ln, rf, HEAD, rfb); yy += int(rsize * 1.36)
        if i < len(rows) - 1:
            d.line([(64, yy + gap // 2), (Wd - 64, yy + gap // 2)], fill=DIV, width=2)
        y = yy + gap
    d.rectangle([(0, Hd - bar_h), (Wd, Hd)], fill=FOOTB)
    cf, cfb = font(26), fbfont(26)
    cta = c["footer_cta"].upper()
    cwa = mixed_width(d, cta, cf, cfb, 3)
    htw = mixed_width(d, HASHTAG, cf, cfb, 2)
    while cwa + htw + 40 > Wd - 128:
        cf, cfb = font(24), fbfont(24)
        cwa = mixed_width(d, cta, cf, cfb, 3)
        htw = mixed_width(d, HASHTAG, cf, cfb, 2)
    draw_mixed(d, 64, Hd - bar_h + (bar_h - cf.size) // 2 - 4, cta, cf, FOOTF, cfb, 3)
    draw_mixed(d, Wd - 64 - htw, Hd - bar_h + (bar_h - cf.size) // 2 - 4, HASHTAG, cf, ACC, cfb, 2)
    save(img, "art2_save_white_1080x1350.png")


if __name__ == "__main__":
    fig1(); fig2(); card1(); card2(); card3(); save_card()
    print("white cards complete")
