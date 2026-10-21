# -*- coding: utf-8 -*-
"""
Breaking AI — Study Manual. Premium PDF renderer.
Reads clean Markdown-with-directives from content/ and lays out a print-quality
A4 book via reportlab Platypus. Reuses the crisp figure PNGs from ../figures/.

Dialect (blocks):
  @cover / @frontchapter T / @chapter N T / @fh2 T / @h2 T / @h3 T
  @tier F|P|R [descriptor]   @sig TEXT   @pull TEXT
  @fig FILE CAPTION          @readywhen TEXT   @pagebreak
  @appendix T   @toc   @lof   @lot
  :::tag ... :::   where tag in {atglance,defbox,example,lab,pitfall,check,
                             objectives,terms,selftest,path1,path2,path3}
  `code fence`  | pipe tables | - bullets | 1. ordered | paragraphs
Inline: **bold**  *italic*  `code`
"""
import os, re, sys
from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Flowable, Paragraph, Spacer,
    Table, TableStyle, Image, PageBreak, NextPageTemplate, HRFlowable,
)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTDIR = os.path.join(HERE, "fonts")
FIGDIR = os.path.join(ROOT, "figures")
OUT = os.path.join(ROOT, "Breaking-AI-Study-Manual.pdf")
CONTENT = [f for f in ["front", "ch0", "ch1", "ch2", "ch3", "ch4", "ch5",
                       "ch6", "ch7", "ch8", "ch9", "ch10", "back"]]

# ---------------------------------------------------------------- colors
INK     = HexColor("#111827")
RED     = HexColor("#E63946")
GREEN   = HexColor("#059669")
AMBER   = HexColor("#D97706")
BLUE    = HexColor("#2563EB")
SLATE   = HexColor("#334155")
MUTED   = HexColor("#64748B")
FAINT   = HexColor("#94A3B8")
LINE    = HexColor("#E5E9F0")
LIGHTBG = HexColor("#F7F8FA")
CODE    = HexColor("#0B7285")

TINTS = {
    "defbox":   ("defblue",  HexColor("#EFF6FF")),
    "example":  ("slate",    HexColor("#F1F5F9")),
    "lab":      ("lab",      HexColor("#F0FDF4")),
    "pitfall":  ("pit",      HexColor("#FFFBEB")),
    "check":    ("check",    HexColor("#FDECEC")),
    "atglance": ("glance",   HexColor("#FBFBFD")),
    "objectives":("obj",     HexColor("#F8FAFC")),
    "terms":    ("terms",    HexColor("#F8FAFC")),
    "selftest": ("test",     HexColor("#F8FAFC")),
    "path1":    ("path1",    HexColor("#EFF6FF")),
    "path2":    ("path2",    HexColor("#F0FDF4")),
    "path3":    ("path3",    HexColor("#FFFBEB")),
    "readywhen":("ready",    HexColor("#F8FAFC")),
}
ACCENT = {
    "defbox": BLUE, "example": SLATE, "lab": GREEN, "pitfall": AMBER,
    "check": RED, "atglance": RED, "objectives": SLATE, "terms": SLATE,
    "selftest": BLUE, "path1": BLUE, "path2": GREEN, "path3": AMBER,
    "readywhen": RED,
}
BOXTITLE = {
    "defbox": "Definition", "example": "Worked Example", "lab": "Lab",
    "pitfall": "Pitfall — The Missing Check", "check": "The Check Is the Product",
    "objectives": "Learning Objectives", "terms": "Key Terms",
    "selftest": "Self-Test — 5 Questions", "readywhen": "Ready-When Checkpoint",
    "path1": "Path 1 — The 2-Week Sprint", "path2": "Path 2 — The Full Path",
    "path3": "Path 3 — The Research Path",
}
TIER = {"F": ("Foundation", GREEN), "P": ("Practitioner", AMBER),
        "R": ("Researcher", RED)}

# ---------------------------------------------------------------- fonts
def _reg():
    pairs = [
        ("DVSerif", "DejaVuSerif.ttf"), ("DVSerif-Bold", "DejaVuSerif-Bold.ttf"),
        ("DVSerif-Italic", "DejaVuSerif-Italic.ttf"),
        ("DVSerif-BoldItalic", "DejaVuSerif-BoldItalic.ttf"),
        ("DVSans", "DejaVuSans.ttf"), ("DVSans-Bold", "DejaVuSans-Bold.ttf"),
        ("DVSans-Oblique", "DejaVuSans-Oblique.ttf"),
        ("DVSans-BoldOblique", "DejaVuSans-BoldOblique.ttf"),
        ("DVMono", "DejaVuSansMono.ttf"), ("DVMono-Bold", "DejaVuSansMono-Bold.ttf"),
    ]
    for name, fn in pairs:
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONTDIR, fn)))
    pdfmetrics.registerFontFamily("DVSerif", normal="DVSerif", bold="DVSerif-Bold",
                                  italic="DVSerif-Italic", boldItalic="DVSerif-BoldItalic")
    pdfmetrics.registerFontFamily("DVSans", normal="DVSans", bold="DVSans-Bold",
                                  italic="DVSans-Oblique", boldItalic="DVSans-BoldOblique")
    pdfmetrics.registerFontFamily("DVMono", normal="DVMono", bold="DVMono-Bold",
                                  italic="DVMono", boldItalic="DVMono-Bold")
_reg()

# ---------------------------------------------------------------- geometry
PW, PH = A4
ML = MR = 60.0
MT, MB = 66.0, 56.0
FW = PW - ML - MR          # text width ~475
FH = PH - MT - MB

# ---------------------------------------------------------------- styles
def S(name, **kw):
    base = dict(fontName="DVSerif", fontSize=10.5, leading=15.5,
                textColor=INK, alignment=TA_JUSTIFY, spaceAfter=7)
    base.update(kw)
    return ParagraphStyle(name, **base)

ST = {
    "body":      S("body"),
    "tight":     S("tight", spaceAfter=0),
    "h2":        S("h2", fontName="DVSans-Bold", fontSize=13.5, leading=18,
                   textColor=INK, alignment=TA_LEFT, spaceBefore=13, spaceAfter=5),
    "h3":        S("h3", fontName="DVSans-Bold", fontSize=11, leading=15,
                   textColor=INK, alignment=TA_LEFT, spaceBefore=9, spaceAfter=3),
    "lead":      S("lead", fontName="DVSerif-Italic", fontSize=10.3, leading=14,
                   textColor=MUTED, alignment=TA_LEFT, spaceAfter=7),
    "bullet":    S("bullet", leftIndent=15, bulletIndent=4, spaceAfter=3.5),
    "obj":       S("obj", leftIndent=15, bulletIndent=4, spaceAfter=3.5),
    "caption":   S("caption", fontName="DVSans", fontSize=8.4, leading=11.5,
                   textColor=MUTED, alignment=TA_CENTER, spaceBefore=5, spaceAfter=12),
    "figlabel":  S("figlabel", fontName="DVSans-Bold", fontSize=8.4, leading=11.5,
                   textColor=RED, alignment=TA_CENTER, spaceBefore=6),
    "chapkick":  S("chapkick", fontName="DVSans-Bold", fontSize=10.5, leading=13,
                   textColor=RED, alignment=TA_LEFT, spaceAfter=2),
    "chapt":     S("chapt", fontName="DVSans-Bold", fontSize=23.5, leading=28,
                   textColor=INK, alignment=TA_LEFT, spaceAfter=6),
    "frontkick": S("frontkick", fontName="DVSans-Bold", fontSize=9.5, leading=12,
                   textColor=RED, alignment=TA_LEFT, spaceAfter=3),
    "frontt":    S("frontt", fontName="DVSans-Bold", fontSize=19, leading=24,
                   textColor=INK, alignment=TA_LEFT, spaceAfter=10),
    "sig":       S("sig", fontName="DVSerif-Italic", fontSize=12.5, leading=18,
                   textColor=RED, alignment=TA_LEFT),
    "pull":      S("pull", fontName="DVSerif-Italic", fontSize=11.5, leading=17,
                   textColor=SLATE, alignment=TA_LEFT),
    "boxtitle":  S("boxtitle", fontName="DVSans-Bold", fontSize=8.4, leading=11,
                   textColor=SLATE, alignment=TA_LEFT, spaceAfter=0),
    "boxbody":   S("boxbody", fontSize=9.8, leading=14.2, spaceAfter=4),
    "boxbody0":  S("boxbody0", fontSize=9.8, leading=14.2, spaceAfter=0),
    "th":        S("th", fontName="DVSans-Bold", fontSize=8.6, leading=11,
                   alignment=TA_LEFT, spaceAfter=0),
    "td":        S("td", fontSize=8.8, leading=12, alignment=TA_LEFT, spaceAfter=0),
    "toc0":      S("toc0", fontName="DVSans-Bold", fontSize=10, leading=13,
                   alignment=TA_LEFT, spaceAfter=0),
    "toc1":      S("toc1", fontName="DVSans", fontSize=8.9, leading=11.5,
                   alignment=TA_LEFT, textColor=SLATE, spaceAfter=0),
    "tocpg":     S("tocpg", fontName="DVSans", fontSize=8.6, alignment=TA_RIGHT, spaceAfter=0),
    "loflab":    S("loflab", fontName="DVSans-Bold", fontSize=8.4, leading=11,
                   textColor=RED, alignment=TA_LEFT, spaceAfter=0),
    "lofcap":    S("lofcap", fontName="DVSans", fontSize=8.4, leading=11,
                   textColor=SLATE, alignment=TA_LEFT, spaceAfter=0),
    "code":      S("code", fontName="DVMono", fontSize=8.4, leading=11.5,
                   alignment=TA_LEFT, spaceAfter=0, textColor=INK),
    "codenum":   S("codenum", fontName="DVMono", fontSize=7.4, leading=11.5,
                   alignment=TA_RIGHT, spaceAfter=0, textColor=FAINT),
}

# ---------------------------------------------------------------- globals
PAGES   = {}          # key -> page label (str)
MARKERS = []          # (level, title, key) in document order
FIGS    = []          # (label, caption, key) in document order
DOC_STATE = {"body_start": None, "chapter_open": False, "chapter_label": ""}

# ---------------------------------------------------------------- inline
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def inline(s):
    out, i, n = [], 0, len(s)
    while i < n:
        if s.startswith("**", i):
            j = s.find("**", i + 2)
            if j > i:
                out.append("<b>" + esc(s[i + 2:j]) + "</b>"); i = j + 2; continue
        if s.startswith("`", i):
            j = s.find("`", i + 1)
            if j > i:
                out.append('<font face="DVMono" size="8.4" color="#0B7285">'
                           + esc(s[i + 1:j]) + "</font>"); i = j + 1; continue
        if s.startswith("*", i):
            j = s.find("*", i + 1)
            if j > i:
                out.append("<i>" + esc(s[i + 1:j]) + "</i>"); i = j + 1; continue
        out.append(esc(s[i])); i += 1
    return "".join(out)

def para(s, style):
    return Paragraph(inline(s) or "&nbsp;", ST[style])

def numitem(k, txt, base):
    ps = ParagraphStyle("ni%d" % k, parent=ST[base], leftIndent=18,
                        firstLineIndent=-18, alignment=TA_JUSTIFY)
    return Paragraph('<font color="#E63946"><b>%d.</b></font>&nbsp;&nbsp;' % k
                     + inline(txt), ps)

# ---------------------------------------------------------------- flowable: marker
class Marker(Flowable):
    """zero-height; tagged for TOC/LOF + page-number recording."""
    def __init__(self, key, level, title, kind, label=""):
        Flowable.__init__(self)
        self.key, self.level, self.title, self.kind = key, level, title, kind
        self.label = label; self.width = 0; self.height = 0
    def wrap(self, aW, aH):
        return (0, 0)
    def draw(self):
        pass

class Flag(Flowable):
    def __init__(self, set_open=None, set_label=None):
        Flowable.__init__(self)
        self.set_open, self.set_label = set_open, set_label
        self.width = 0; self.height = 0
    def wrap(self, aW, aH):
        return (0, 0)
    def draw(self):
        pass

def cover_block():
    c = TA_CENTER
    def P(s, font, size, color, before=0, after=0, lead=None):
        return Paragraph(s, ParagraphStyle("cv", fontName=font, fontSize=size,
                   leading=lead or size * 1.35, textColor=color,
                   alignment=c, spaceBefore=before, spaceAfter=after))
    return [
        Spacer(1, 44),
        P("<b>Breaking AI</b>", "DVSans-Bold", 46, INK, after=4),
        HRFlowable(width=130, thickness=3, color=RED, hAlign="CENTER",
                   spaceBefore=10, spaceAfter=16),
        P("The Complete Guide to AI Red Teaming, AI Safety,<br/>and AI Research",
          "DVSans", 15, SLATE, after=18),
        P("<b>Study Manual — Print-Ready Edition v1.0</b>", "DVSans-Bold", 11, INK, after=4),
        P("Covers Parts 0–10 + LARA-lite Inspect Lab + Aithos Sprint",
          "DVSans", 9.5, MUTED, after=44),
        P("<i>An expert AI security &amp; safety author — direct, concrete, no-fluff.</i>",
          "DVSerif-Italic", 10, MUTED, after=16),
        P("<i>The check is the product. If you cannot rerun the failure,<br/>"
          "you have not found it, you have had an opinion.</i>",
          "DVSerif-Italic", 11, RED, after=60),
        P("A4 · 2 cm margins · 11 pt · 20 October 2026", "DVSans", 8.5, FAINT, after=2),
        P('<font name="DVMono" size="8.5">github.com/Teamthy/linkedin_emphire — manual/</font>',
          "DVSans", 8.5, FAINT),
    ]

# ---------------------------------------------------------------- boxes
def _box(title, inner, kind, title_override=None, numbered=False):
    accent = ACCENT[kind]; tint = TINTS[kind][1]
    tlabel = title_override if title_override is not None else (title or BOXTITLE.get(kind, ""))
    rows = []
    if tlabel:
        tstyle = ParagraphStyle("bt" + kind, parent=ST["boxtitle"],
                                textColor=(RED if kind == "check" else accent))
        rows.append([Paragraph(esc(tlabel).upper(), tstyle)])
    if numbered:
        body = inner  # inner already a list with numbering applied
    else:
        body = inner
    rows.append([body])
    data = rows
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), tint),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ]
    if tlabel:
        style += [("LINEBELOW", (0, 0), (0, 0), 0.6, accent),
                  ("BOTTOMPADDING", (0, 0), (0, 0), 6),
                  ("TOPPADDING", (0, 0), (0, 0), 9)]
    t = Table(data, colWidths=[FW - 0], style=TableStyle(style), repeatRows=1 if tlabel else 0)
    return t

def code_block(code):
    lines = code.rstrip("\n").split("\n")
    data = []
    for idx, ln in enumerate(lines, 1):
        data.append([Paragraph(str(idx), ST["codenum"]),
                     Paragraph(esc(ln) if ln.strip() else "&nbsp;", ST["code"])])
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), LIGHTBG),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 1.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
        ("LEFTPADDING", (0, 0), (0, -1), 8), ("RIGHTPADDING", (0, 0), (0, -1), 6),
        ("LEFTPADDING", (1, 0), (1, -1), 9), ("RIGHTPADDING", (1, 0), (1, -1), 9),
        ("LINEBEFORE", (1, 0), (1, -1), 0.5, LINE),
    ]
    t = Table(data, colWidths=[FW * 0.075, FW * 0.925], style=TableStyle(style))
    return t

def md_table(rows):
    header = rows[0]
    body = rows[2:]
    data = [[Paragraph(inline(c).strip() or "&nbsp;", ST["th"]) for c in header]]
    for r in body:
        data.append([Paragraph(inline(c).strip() or "&nbsp;", ST["td"]) for c in r])
    ncol = max(1, len(header))
    colw = [FW / ncol] * ncol
    style = [
        ("FONTNAME", (0, 0), (-1, -1), "DVSans"),
        ("LINEABOVE", (0, 0), (-1, 0), 1.1, INK),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, INK),
        ("LINEBELOW", (0, -1), (-1, -1), 1.1, INK),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, LIGHTBG]),
    ]
    return Table(data, colWidths=colw, style=TableStyle(style), repeatRows=1)

def signature(text, kind="sig"):
    """brand signature / pull line with a red left rule."""
    p = Paragraph(inline(text), ST[kind])
    t = Table([[p]], colWidths=[FW - 14], style=TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LINEBEFORE", (0, 0), (0, -1), 3, RED),
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#FDF6F6") if kind == "sig" else white),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 4)]

def tier_chip(letter, descriptor=""):
    name, col = TIER[letter]
    chip = Paragraph(
        '<font color="#FFFFFF"><b>%s</b></font>&nbsp;&nbsp;%s' % (letter, esc(name)),
        ParagraphStyle("chip", fontName="DVSans-Bold", fontSize=7.6, leading=10,
                       textColor=col, alignment=TA_LEFT, backColor=col,
                       leftIndent=0))
    # use a table so backColor spans only the chip width; simpler: colored label
    label = Paragraph(
        '<b><font color="%s">[ %s · %s ]</font></b>%s' % (
            col.hexval().replace("0x", "#"), letter, name,
            ("  <font color='#94A3B8'><i>%s</i></font>" % esc(descriptor) if descriptor else "")),
        ParagraphStyle("tier", fontName="DVSans", fontSize=8.6, leading=12,
                       textColor=INK, alignment=TA_LEFT, spaceBefore=2, spaceAfter=6))
    return label

def figure_block(fname, caption, label):
    path = os.path.join(FIGDIR, fname)
    if not os.path.exists(path):
        return [Paragraph("MISSING FIGURE: " + esc(fname), ST["body"])]
    im = PILImage.open(path)
    w, h = im.size
    width = FW
    height = width * h / w
    maxh = 430.0
    if height > maxh:
        height = maxh; width = height * w / h
    pic = Image(path, width=width, height=height, hAlign="CENTER")
    figkey = "fig::" + label + "::" + caption
    fig = _FigTag(pic, label, caption, figkey)
    FIGS.append((label, caption, figkey))
    cap = Paragraph('<font name="DVSans-Bold" color="#E63946">%s.</font>  %s'
                    % (esc(label), inline(caption)), ST["caption"])
    return [fig, cap]

class _FigTag(Flowable):
    def __init__(self, img, label, caption, key):
        Flowable.__init__(self)
        self._img = img; self.label = label; self.caption = caption; self.key = key
    def wrap(self, aW, aH):
        return self._img.wrap(aW, aH)
    def draw(self):
        self._img.drawOn(self.canv, 0, 0)

# ---------------------------------------------------------------- parse
def _is_sep(cells):
    return all(re.match(r"^:?-{2,}:?$", c.strip()) for c in cells if c.strip()) and any(cells)

def _split_cells(line):
    line = line.strip()
    if line.startswith("|"): line = line[1:]
    if line.endswith("|"): line = line[:-1]
    return [c.strip() for c in line.split("|")]

class Ctx:
    def __init__(self):
        self.chapter = None      # current chapter number (int) or 'FM'/'APP'
        self.fig_no = 0
        self.sec_no = 0
        self.sub_no = 0
        self.front = True

def parse_block_lines(lines, ctx):
    """Parse a list of lines (a box body or a chapter chunk) into flowables."""
    fl = []
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]
        if not ln.strip():
            i += 1; continue
        # code fence
        if ln.strip().startswith("```"):
            j = i + 1; buf = []
            while j < n and not lines[j].strip().startswith("```"):
                buf.append(lines[j]); j += 1
            fl.append(Spacer(1, 5)); fl.append(code_block("\n".join(buf))); fl.append(Spacer(1, 5))
            i = j + 1; continue
        # table
        if ln.strip().startswith("|"):
            j = i; buf = []
            while j < n and lines[j].strip().startswith("|"):
                buf.append(_split_cells(lines[j])); j += 1
            if len(buf) >= 2 and _is_sep(buf[1]):
                fl.append(Spacer(1, 5)); fl.append(md_table(buf)); fl.append(Spacer(1, 6))
            else:
                for r in buf:
                    fl.append(para("  ".join(r), "body"))
            i = j; continue
        # bullets
        if ln.lstrip().startswith("- "):
            items = []
            while i < n and lines[i].lstrip().startswith("- "):
                items.append(lines[i].lstrip()[2:]); i += 1
            for it in items:
                fl.append(Paragraph(inline(it), ST["bullet"], bulletText="•"))
            fl.append(Spacer(1, 4)); continue
        # ordered
        if re.match(r"^\s*\d+\.\s", ln):
            k = 1
            while i < n and re.match(r"^\s*\d+\.\s", lines[i]):
                txt = re.sub(r"^\s*\d+\.\s", "", lines[i])
                fl.append(numitem(k, txt, "body")); k += 1; i += 1
            fl.append(Spacer(1, 4)); continue
        # paragraph (merge until blank line or directive)
        buf = [ln.strip()]
        i += 1
        while i < n and lines[i].strip() and not lines[i].lstrip().startswith(
                (":::", "@")) and not lines[i].strip().startswith("|") \
                and not lines[i].lstrip().startswith("- ") \
                and not re.match(r"^\s*\d+\.\s", lines[i]):
            buf.append(lines[i].strip()); i += 1
        fl.append(para(" ".join(buf), "body"))
    return fl

def back_block(title):
    p = Paragraph(esc(title), ST["chapt"]); p.id = "ch"
    return [NextPageTemplate("body"), Flag(set_open=True, set_label="Back Matter"),
            PageBreak(), Spacer(1, 70), Paragraph("BACK MATTER", ST["chapkick"]), Spacer(1, 12),
            p, HRFlowable(width=54, thickness=2.5, color=RED, spaceBefore=6, spaceAfter=14)]


def parse_content(text, ctx):
    lines = text.split("\n")
    fl = []
    i, n = 0, len(lines)
    while i < n:
        raw = lines[i]
        ln = raw.strip()
        if not ln:
            i += 1; continue
        if ln.startswith(":::"):
            tag = ln[3:].strip()
            j = i + 1; body = []
            while j < n and lines[j].strip() != ":::":
                body.append(lines[j]); j += 1
            title_override = None
            if tag in BOXTAGS:
                inner = parse_block_lines(body, ctx)
                # atglance: render as labeled paragraphs (no bullets)
                if tag == "atglance":
                    inner = []
                    for bl in body:
                        if bl.strip():
                            inner.append(para(bl.strip(), "boxbody"))
                    title_override = (("Chapter %s at a Glance" % ctx.chapter)
                                      if isinstance(ctx.chapter, int) else "At a Glance")
                if tag == "objectives" or tag == "selftest":
                    inner = []
                    k = 1
                    for bl in body:
                        if not bl.strip():
                            continue
                        t = re.sub(r"^\s*(\d+\.|-)\s?", "", bl.strip())
                        inner.append(numitem(k, t, "boxbody")); k += 1
                if tag in ("path1", "path2", "path3"):
                    if tag not in ("path1",):
                        title_override = BOXTAG_TITLE.get(tag)
                    else:
                        title_override = "Path 1 — The 2-Week Sprint (the Aithos window)"
                if tag in ("lab",):
                    # title already in the :: line? we pass via body first bold line
                    title_override = None
                if tag == "terms":
                    inner = []
                    for bl in body:
                        if bl.strip():
                            inner.append(Paragraph(inline(bl.strip()), ST["boxbody"],
                                                  bulletText="•"))
                fl.append(_box(BOXTITLE.get(tag, ""), inner, tag,
                               title_override=title_override))
                fl.append(Spacer(1, 8))
            i = j + 1; continue
        if ln.startswith("@"):
            parts = ln[1:].split(None, 1)
            cmd = parts[0]
            arg = parts[1].strip() if len(parts) > 1 else ""
            if cmd == "cover":
                fl.extend(cover_block())
                fl.append(NextPageTemplate("front")); fl.append(PageBreak()); i += 1; continue
            if cmd == "frontchapter":
                ctx.front = True
                key = "front::" + arg
                fl.append(PageBreak())
                fl.append(Marker(key, 0, arg, "front", label="Front Matter"))
                MARKERS.append((0, arg, key))
                fl.append(Paragraph("FRONT MATTER", ST["frontkick"]))
                fl.append(Paragraph(esc(arg), ST["frontt"]))
                fl.append(HRFlowable(width=FW, thickness=2.2, color=RED, spaceAfter=12))
                i += 1; continue
            if cmd == "chapter":
                m = re.match(r"^(\d+)\s+(.*)$", arg)
                no = int(m.group(1)); title = m.group(2)
                ctx.front = False; ctx.chapter = no; ctx.fig_no = 0; ctx.sec_no = 0
                key = "ch%d" % no
                label = "Chapter %d · %s" % (no, _short(title))
                fl.append(NextPageTemplate("body"))
                fl.append(Flag(set_open=True, set_label=label))
                fl.append(PageBreak())
                fl.append(Marker(key, 0, "Chapter %d — %s" % (no, title), "chap", label=label))
                MARKERS.append((0, "Chapter %d — %s" % (no, title), key))
                fl.append(Spacer(1, 2))
                fl.append(Paragraph(("CHAPTER %d" % no).upper(), ST["chapkick"]))
                fl.append(Paragraph(esc(title), ST["chapt"]))
                fl.append(HRFlowable(width=54, thickness=2.5, color=RED, spaceBefore=6, spaceAfter=14))
                i += 1; continue
            if cmd == "appendix":
                ctx.front = False; ctx.chapter = "APP"; ctx.fig_no = 0
                key = "app::" + arg
                label = arg
                fl.append(NextPageTemplate("body"))
                fl.append(Flag(set_open=True, set_label=label))
                fl.append(PageBreak())
                fl.append(Marker(key, 0, arg, "app", label=label))
                MARKERS.append((0, arg, key))
                fl.append(Paragraph("BACK MATTER", ST["chapkick"]))
                fl.append(Paragraph(esc(arg), ST["chapt"]))
                fl.append(HRFlowable(width=54, thickness=2.5, color=RED, spaceBefore=6, spaceAfter=14))
                i += 1; continue
            if cmd == "fh2":
                fl.append(Paragraph(esc(arg), ST["h2"]))
                i += 1; continue
            if cmd == "h2":
                ctx.sec_no += 1; ctx.sub_no = 0
                num = ("%d.%d" % (ctx.chapter, ctx.sec_no)) if isinstance(ctx.chapter, int) else ""
                disp = (num + "   " if num else "") + esc(arg)
                key = "sec::%s::%s" % (ctx.chapter, arg)
                fl.append(Marker(key, 1, (num + "  " if num else "") + arg, "sec"))
                MARKERS.append((1, (num + "  " if num else "") + arg, key))
                fl.append(Paragraph(('<font color="#E63946"><b>%s</b></font>  ' % num if num else "")
                                     + esc(arg), ST["h2"]))
                i += 1; continue
            if cmd == "h3":
                ctx.sub_no += 1
                dispnum = ("%d.%d.%d" % (ctx.chapter, ctx.sec_no, ctx.sub_no)
                           if isinstance(ctx.chapter, int) else "")
                fl.append(Paragraph(('<font color="#E63946"><b>%s</b></font>  ' % dispnum if dispnum else "")
                                     + esc(arg), ST["h3"]))
                i += 1; continue
            if cmd == "tier":
                letter = arg.split()[0]
                desc = " ".join(arg.split()[1:]) if len(arg.split()) > 1 else ""
                fl.append(tier_chip(letter, desc)); i += 1; continue
            if cmd == "sig":
                fl.extend(signature(arg, "sig")); i += 1; continue
            if cmd == "small":
                fl.append(Paragraph(esc(arg), ParagraphStyle(
                    "sm", parent=ST["body"], fontName="DVSans", fontSize=8.6,
                    textColor=FAINT, alignment=TA_LEFT, spaceBefore=10, spaceAfter=2)))
                i += 1; continue
            if cmd == "pull":
                fl.extend(signature(arg, "pull")); i += 1; continue
            if cmd == "fig":
                mm = re.match(r"^(fig[\w\-]+\.png)\s+(.*)$", arg)
                if not mm:
                    i += 1; continue
                fname, cap = mm.group(1), mm.group(2)
                if ctx.front or ctx.chapter == "FM":
                    ctx.fig_no += 1; label = "FM.%d" % ctx.fig_no
                elif ctx.chapter == "APP":
                    ctx.fig_no += 1; label = "B.%d" % ctx.fig_no
                else:
                    ctx.fig_no += 1; label = "%d.%d" % (ctx.chapter, ctx.fig_no)
                fl.extend(figure_block(fname, cap, label))
                i += 1; continue
            if cmd == "readywhen":
                fl.append(_box("", [para(arg, "boxbody")], "readywhen"))
                fl.append(Spacer(1, 8)); i += 1; continue
            if cmd in ("toc", "lof", "lot"):
                fl.append(PageBreak()); fl.extend(toc_flowables(cmd)); i += 1; continue
            if cmd == "pagebreak":
                fl.append(PageBreak()); i += 1; continue
            if cmd == "back":
                fl.extend(back_block(arg)); i += 1; continue
            i += 1; continue
        if ln.strip().startswith("```"):
            j = i + 1; buf = []
            while j < n and not lines[j].strip().startswith("```"):
                buf.append(lines[j]); j += 1
            fl.append(Spacer(1, 5)); fl.append(code_block("\n".join(buf))); fl.append(Spacer(1, 5))
            i = j + 1; continue
        if ln.strip().startswith("|"):
            j = i; buf = []
            while j < n and lines[j].strip().startswith("|"):
                buf.append(_split_cells(lines[j])); j += 1
            if len(buf) >= 2 and _is_sep(buf[1]):
                fl.append(Spacer(1, 5)); fl.append(md_table(buf)); fl.append(Spacer(1, 6))
            else:
                for r in buf:
                    fl.append(para("  ".join(r), "body"))
            i = j; continue
        # default: treat as paragraph line; fall through to block parser for lists
        # gather this "paragraph region" up to next blank/directive and delegate
        j = i
        buf = [raw.rstrip()]
        while j + 1 < n and lines[j + 1].strip() and not lines[j + 1].lstrip().startswith(
                (":::", "@")) and not lines[j + 1].strip().startswith("|"):
            j += 1; buf.append(lines[j].rstrip())
        fl.extend(parse_block_lines(buf, ctx))
        i = j + 1
    return fl

BOXTAGS = {"atglance", "defbox", "example", "lab", "pitfall", "check",
           "objectives", "terms", "selftest", "path1", "path2", "path3"}
BOXTAG_TITLE = {"path2": "Path 2 — The Full Path (10–12 weeks)",
                "path3": "Path 3 — The Research Path (expert jump-in)"}

def _short(t):
    t = re.sub(r"[:].*$", "", t)
    return (t[:34] + "…") if len(t) > 34 else t

# ---------------------------------------------------------------- TOC / LOF
class TOC(Flowable):
    def __init__(self, kind="toc"):
        Flowable.__init__(self); self.kind = kind
    def _build_table(self):
        rows = []
        if self.kind == "toc":
            for lv, ti, k in MARKERS:
                pg = PAGES.get(k, "–")
                if lv == 0:
                    rows.append([Paragraph('<font color="#E63946">•</font>&nbsp;&nbsp;'
                                           + esc(ti), ST["toc0"]),
                                 Paragraph(str(pg), ST["tocpg"])])
                else:
                    rows.append([Paragraph('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                                           + esc(ti), ST["toc1"]),
                                 Paragraph(str(pg), ST["tocpg"])])
            return Table(rows, colWidths=[FW * 0.86, FW * 0.14], style=TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ]))
        elif self.kind == "lof":
            for lab, cap, k in FIGS:
                rows.append([Paragraph(esc(lab), ST["loflab"]),
                             Paragraph(esc(cap), ST["lofcap"]),
                             Paragraph(str(PAGES.get(k, "–")), ST["tocpg"])])
            return Table(rows, colWidths=[FW * 0.12, FW * 0.74, FW * 0.14],
                         style=TableStyle([
                             ("VALIGN", (0, 0), (-1, -1), "TOP"),
                             ("ALIGN", (2, 0), (2, -1), "RIGHT"),
                             ("TOPPADDING", (0, 0), (-1, -1), 3),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                             ("LEFTPADDING", (0, 0), (0, -1), 2),
                             ("RIGHTPADDING", (2, 0), (2, -1), 2)]))
        else:
            return Table([[Paragraph("No standalone tables.", ST["lofcap"])]], colWidths=[FW])
    def wrap(self, aW, aH):
        self._table = self._build_table()
        w, h = self._table.wrap(aW, aH)
        self.width, self.height = w, h
        return (w, h)
    def draw(self):
        self._table.drawOn(self.canv, 0, 0)
    def split(self, aW, aH):
        return self._table.split(aW, aH)

def toc_flowables(kind):
    heading = {"toc": "Contents", "lof": "List of Figures"}.get(kind, "List of Tables")
    head = Paragraph(esc(heading), ParagraphStyle(
        "tochead", fontName="DVSans-Bold", fontSize=23.5, leading=28,
        textColor=INK, spaceAfter=2))
    return [head, HRFlowable(width=54, thickness=2.5, color=RED,
                             spaceBefore=2, spaceAfter=14), TOC(kind=kind)]

# ---------------------------------------------------------------- doc
def to_roman(num):
    vals = [(1000,'m'),(900,'cm'),(500,'d'),(400,'cd'),(100,'c'),(90,'xc'),
            (50,'l'),(40,'xl'),(10,'x'),(9,'ix'),(5,'v'),(4,'iv'),(1,'i')]
    out = ""
    for v, s in vals:
        while num >= v:
            out += s; num -= v
    return out

class Book(BaseDocTemplate):
    def __init__(self, filename):
        BaseDocTemplate.__init__(self, filename, pagesize=A4,
                                 leftMargin=ML, rightMargin=MR,
                                 topMargin=MT, bottomMargin=MB)
        f_body = Frame(ML, MB, FW, FH, id="body")
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[f_body], onPage=self.on_cover),
            PageTemplate(id="front", frames=[f_body], onPage=self.on_front),
            PageTemplate(id="body", frames=[f_body], onPage=self.on_body),
        ])
        self._front_start = None

    def on_cover(self, c, doc):
        c.saveState()
        c.setFillColor(RED); c.rect(0, PH - 46, PW, 46, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("DVSans-Bold", 11)
        c.drawString(ML, PH - 30, "B R E A K I N G   A I")
        c.setFillColor(RED); c.rect(0, 0, PW, 10, fill=1, stroke=0)
        c.restoreState()

    def on_front(self, c, doc):
        c.saveState()
        pg = doc.page
        if self._front_start is None:
            self._front_start = pg
        roman = to_roman(pg - self._front_start + 1)
        c.setFont("DVSans", 8.4); c.setFillColor(MUTED)
        c.drawCentredString(PW / 2, 30, roman)
        c.restoreState()

    def on_body(self, c, doc):
        c.saveState()
        pg = doc.page
        # header (suppressed on chapter-open page)
        if not DOC_STATE["chapter_open"]:
            y = PH - 34
            c.setFillColor(RED); c.rect(ML, y - 1, 7, 7, fill=1, stroke=0)
            c.setFont("DVSans-Bold", 7.3); c.setFillColor(MUTED)
            c.drawString(ML + 12, y - 1, "B R E A K I N G   A I")
            c.setFont("DVSans", 7.6); c.setFillColor(MUTED)
            lab = DOC_STATE["chapter_label"]
            if lab:
                c.drawRightString(PW - MR, y - 1, lab)
            c.setStrokeColor(LINE); c.setLineWidth(0.6)
            c.line(ML, y - 9, PW - MR, y - 9)
        # footer page number (arabic, restarted)
        if DOC_STATE["body_start"] is not None:
            c.setFont("DVSans", 8.6); c.setFillColor(MUTED)
            c.drawCentredString(PW / 2, 30, str(pg - DOC_STATE["body_start"] + 1))
        c.restoreState()

    def afterFlowable(self, fl):
        if isinstance(fl, Flag):
            if fl.set_open is not None:
                DOC_STATE["chapter_open"] = fl.set_open
            if fl.set_label is not None:
                DOC_STATE["chapter_label"] = fl.set_label
            return
        if isinstance(fl, Marker):
            if fl.kind == "front":
                if self._front_start is None:
                    self._front_start = self.page
                PAGES[fl.key] = to_roman(self.page - self._front_start + 1)
            else:
                if DOC_STATE["body_start"] is None:
                    DOC_STATE["body_start"] = self.page
                if fl.kind in ("chap", "app"):
                    DOC_STATE["chapter_open"] = False
                PAGES[fl.key] = str(self.page - DOC_STATE["body_start"] + 1)
            return
        if isinstance(fl, _FigTag):
            if DOC_STATE["body_start"] is None:
                if self._front_start is None:
                    self._front_start = self.page
                PAGES[fl.key] = to_roman(self.page - self._front_start + 1)
            else:
                PAGES[fl.key] = str(self.page - DOC_STATE["body_start"] + 1)

def make_story():
    MARKERS.clear(); FIGS.clear()
    ctx = Ctx()
    story = []
    for name in CONTENT:
        p = os.path.join(HERE, "content", name + ".md")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            text = f.read()
        story.extend(parse_content(text, ctx))
    return story

def build(out, quiet=True):
    story = make_story()
    doc = Book(out)
    doc.build(story)

def main():
    # pass 1 -> collect page numbers
    tmp = os.path.join(HERE, "_pass1.pdf")
    DOC_STATE.update({"body_start": None, "chapter_open": False, "chapter_label": ""})
    build(tmp)
    # pass 2 -> render TOC/LOF with real pages
    DOC_STATE.update({"body_start": None, "chapter_open": False, "chapter_label": ""})
    build(OUT)
    d = __import__("pymupdf").open(OUT)
    print("pages:", d.page_count)
    print("wrote", OUT)

if __name__ == "__main__":
    main()
