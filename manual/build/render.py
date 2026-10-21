#!/usr/bin/env python3
# Render the Breaking AI study manual from its LaTeX source (manual/chapters/*.tex)
# into a premium A4 PDF using reportlab. No LaTeX engine required.
#
# Usage:  python3 manual/build/render.py
# Output: manual/Breaking-AI-Study-Manual.pdf  (+ a transient _pass1.pdf during the 2-pass build)
#
# The .tex stays the single source of truth. This renderer understands the bounded
# grammar used by this project: \chapter/section/subsection, tcolorbox + the custom
# def/example/lab/pitfall/check boxes, selftest, readywhen, itemize/enumerate,
# tabular/tabularx, lstlisting, figure (rendered from figures/*.png), and a small
# set of inline commands (textbf/textit/texttt/textcolor/colorbox, $math$, tiers).

import os, re, html, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Flowable,
    Paragraph, Spacer, PageBreak, Table, TableStyle, Image, HRFlowable)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # .../manual
BUILD = os.path.join(BASE, "build")
FONTS = os.path.join(BUILD, "fonts")
FIGS = os.path.join(BASE, "figures")
CH = os.path.join(BASE, "chapters")
OUT = os.path.join(BASE, "Breaking-AI-Study-Manual.pdf")
OUT1 = os.path.join(BASE, "_pass1.pdf")

PAGE_W, PAGE_H = A4
ML = MR = 60
MT = 66
MB = 56
CW = PAGE_W - ML - MR

INK   = HexColor("#111827"); RED   = HexColor("#E63946"); DBLUE = HexColor("#2563EB")
LGREEN= HexColor("#059669"); PAMB  = HexColor("#D97706"); SLATE = HexColor("#334155")
LINE  = HexColor("#E5E9F0"); FAINT = HexColor("#64748B"); LGRAY = HexColor("#F8FAFC")
LBLUE = HexColor("#EFF6FF"); LGREENBG = HexColor("#F0FDF4"); LAMBBG = HexColor("#FFFBEB")
LRED  = HexColor("#FEF2F2"); LSLATE = HexColor("#F1F5F9"); INKBG  = HexColor("#F1F5F9")
WHITE = HexColor("#FFFFFF"); ZEBRA = HexColor("#FBFCFE")

TIER_COLOR = {"F": LGREEN, "P": PAMB, "R": RED}
TIER_NAME  = {"F": "Foundation", "P": "Practitioner", "R": "Researcher"}
BOX_KIND = {
    "defbox":     ("Definition", DBLUE, LBLUE),
    "examplebox": ("Worked Example", SLATE, LSLATE),
    "labbox":     ("Lab", LGREEN, LGREENBG),
    "pitfallbox": ("Pitfall \u2014 The Missing Check", PAMB, LAMBBG),
    "checkbox":   ("The Check Is the Product", RED, LRED),
}
COLMAP = {"defblue": DBLUE, "labgreen": LGREEN, "pitamber": PAMB, "accent": RED,
          "slate": SLATE, "checkblack": INK, "white": WHITE}
BGMAP  = {"white": WHITE, "lightblue": LBLUE, "lightgreen": LGREENBG, "lightamber": LAMBBG,
          "lightred": LRED, "lightslate": LSLATE, "lightbg": LGRAY, "checkblack!5": INKBG}

def hexstr(c):
    return "#" + c.hexval()[-6:]

ST = {}
def mkstyles():
    s = ST
    s["body"]   = ParagraphStyle("body", fontName="DVSerif", fontSize=10.5, leading=15.5,
                                 textColor=INK, alignment=TA_JUSTIFY, spaceAfter=7)
    s["bodyL"]  = ParagraphStyle("bodyL", parent=s["body"], alignment=TA_LEFT)
    s["cell"]   = ParagraphStyle("cell", fontName="DVSerif", fontSize=9.2, leading=12.6, textColor=INK)
    s["cellB"]  = ParagraphStyle("cellB", parent=s["cell"], fontName="DVSans")
    s["chapkick"] = ParagraphStyle("chapkick", fontName="DVSans-Bold", fontSize=11, leading=14, textColor=RED)
    s["chapt"]  = ParagraphStyle("chapt", fontName="DVSans-Bold", fontSize=26, leading=32, textColor=INK)
    s["h1"]     = ParagraphStyle("h1", fontName="DVSans-Bold", fontSize=15.5, leading=20,
                                 textColor=INK, spaceBefore=15, spaceAfter=5)
    s["h2"]     = ParagraphStyle("h2", fontName="DVSans-Bold", fontSize=12.3, leading=16,
                                 textColor=INK, spaceBefore=10, spaceAfter=4)
    s["boxtitle"] = ParagraphStyle("boxtitle", fontName="DVSans-Bold", fontSize=10.5, leading=13, textColor=INK)
    s["boxbody"]  = ParagraphStyle("boxbody", fontName="DVSerif", fontSize=10, leading=14.5,
                                   textColor=INK, alignment=TA_LEFT, spaceAfter=4)
    s["code"]   = ParagraphStyle("code", fontName="DVMono", fontSize=8.5, leading=12,
                                 textColor=INK, alignment=TA_LEFT, wordWrap="CJK")
    s["cap"]    = ParagraphStyle("cap", fontName="DVSerif", fontSize=9, leading=12.5,
                                 textColor=FAINT, alignment=TA_CENTER, spaceBefore=4)
    s["tocH"]   = ParagraphStyle("tocH", fontName="DVSans-Bold", fontSize=17, leading=21, textColor=INK)
    s["tocC"]   = ParagraphStyle("tocC", fontName="DVSans", fontSize=10.5, leading=15, textColor=INK)
    s["tocS"]   = ParagraphStyle("tocS", fontName="DVSerif", fontSize=9.6, leading=14, textColor=SLATE, leftIndent=14)
    s["tocF"]   = ParagraphStyle("tocF", fontName="DVSerif", fontSize=9.6, leading=14, textColor=SLATE)

def load_fonts():
    reg = [("DVSerif","DejaVuSerif.ttf"),("DVSerif-Bold","DejaVuSerif-Bold.ttf"),
           ("DVSerif-Italic","DejaVuSerif-Italic.ttf"),("DVSerif-BoldItalic","DejaVuSerif-BoldItalic.ttf"),
           ("DVSans","DejaVuSans.ttf"),("DVSans-Bold","DejaVuSans-Bold.ttf"),
           ("DVSans-Oblique","DejaVuSans-Oblique.ttf"),("DVSans-BoldOblique","DejaVuSans-BoldOblique.ttf"),
           ("DVMono","DejaVuSansMono.ttf"),("DVMono-Bold","DejaVuSansMono-Bold.ttf"),
           ("DVMono-Oblique","DejaVuSansMono-Oblique.ttf"),("DVMono-BoldOblique","DejaVuSansMono-BoldOblique.ttf")]
    for name, f in reg:
        p = os.path.join(FONTS, f)
        if os.path.exists(p):
            pdfmetrics.registerFont(TTFont(name, p))
    pdfmetrics.registerFontFamily("DVSerif", normal="DVSerif", bold="DVSerif-Bold",
                                  italic="DVSerif-Italic", boldItalic="DVSerif-BoldItalic")
    pdfmetrics.registerFontFamily("DVSans", normal="DVSans", bold="DVSans-Bold",
                                  italic="DVSans-Oblique", boldItalic="DVSans-BoldOblique")
    pdfmetrics.registerFontFamily("DVMono", normal="DVMono", bold="DVMono-Bold",
                                  italic="DVMono-Oblique", boldItalic="DVMono-BoldOblique")

# ─────────────────────────  parsing  ─────────────────────────
def _read_brace(text, b):
    depth = 0
    for k in range(b, len(text)):
        if text[k] == "{": depth += 1
        elif text[k] == "}":
            depth -= 1
            if depth == 0: return text[b+1:k], k+1
    return text[b+1:], len(text)

def strip_comments(text):
    return "\n".join(ln for ln in text.split("\n") if not ln.strip().startswith("%"))

def find_env_end(text, env, i):
    j = text.find("\\end{%s}" % env, i)
    return i, (j if j >= 0 else len(text))

def split_items(content):
    m = re.match(r"\s*\[([^\]]*)\]", content)   # optional arg, e.g. [leftmargin=1.2cm]
    if m: content = content[m.end():]
    parts = re.split(r"\\item", content)
    items = [p.strip() for p in parts]
    return [p for p in items if p]

def parse_table(content):
    s = content
    for _ in range(2):                       # strip column-spec brace group(s)
        s2 = s.lstrip()
        if s2.startswith("{"):
            _, k = _read_brace(s2, 0)
            s = s2[k:]
    s = re.sub(r"\\(toprule|midrule|bottomrule|hline)\b", " ", s)
    rows = []
    for raw in s.split("\\\\"):
        r = raw.strip()
        if not r:
            continue
        cells = [c.strip() for c in r.split("&")]
        if all(c == "" for c in cells):
            continue
        rows.append(cells)
    return rows

BLOCK = re.compile(
    r"(\\chapter\*?\{)|(\\section\*?\{)|(\\subsection\*?\{)|(\\begin\{)|"
    r"(\\readywhen\{)|(\\tableofcontents)|(\\listoffigures)|(\\listoftables)|"
    r"(\\markboth\{)|(\\addcontentsline)|(\\label\{)|(\\newpage)|(\\end\{document\})")

def _parse_env(env, content, state):
    if env in BOX_KIND:
        return ("box", env, BOX_KIND[env][0], parse_blocks(content, state))
    if env == "selftest":
        return ("selftest", split_items(content))
    if env in ("itemize", "enumerate"):
        return ("list", env, split_items(content))
    if env == "figure":
        cap = ""
        mc = re.search(r"\\caption\{", content)
        if mc: cap = _read_brace(content, mc.end()-1)[0].strip()
        slug = None
        ml = re.search(r"\\label\{(fig:[^}]*)\}", content)
        if ml: slug = ml.group(1)[4:]
        path = None
        if slug:
            cand = os.path.join(FIGS, "fig" + slug + ".png")
            if os.path.exists(cand): path = cand
        if path is None:
            mg = re.search(r"\\includegraphics[^{]*\{([^}]*)\}", content)
            if mg:
                cand = os.path.join(FIGS, mg.group(1))
                if os.path.exists(cand): path = cand
        return ("figure", path, cap, slug or cap[:20])
    if env == "tikzpicture":
        state["tikz_n"] = state.get("tikz_n", 0) + 1
        k = state["tikz_n"]; prefix = state.get("fig_prefix", "X")
        path = None
        for cand in ("fig%s-%d.png" % (prefix, k), "fig%s-1.png" % (prefix)):
            p = os.path.join(FIGS, cand)
            if os.path.exists(p):
                path = p; break
        return ("figure", path, "", "tikz%s-%d" % (prefix, k))
    if env in ("tabular", "tabularx"):
        return ("table", parse_table(content))
    if env == "lstlisting":
        return ("code", content.strip("\n"))
    if env == "center":
        inner = parse_blocks(content, state)
        if len(inner) == 1 and inner[0][0] == "figure":
            return inner[0]
        return ("center", inner)
    if env == "titlepage":
        mc = re.search(r"\\begin\{center\}", content)
        inner = content[mc.end():] if mc else content
        ie = inner.find("\\end{center}")
        if ie >= 0: inner = inner[:ie]
        return ("titlepage", inner)
    if env == "tcolorbox":
        title, colframe, colback = "", "checkblack", "lightbg"
        mo = re.match(r"\s*\[([^\]]*)\]", content)
        if mo:
            o = mo.group(1)
            for key, dst in (("title", "title"), ("colframe", "colframe"), ("colback", "colback")):
                mm = re.search(key + r"=([^,]+)", o)
                if mm:
                    val = mm.group(1).strip().strip("'")
                    if dst == "title": title = val
                    elif dst == "colframe": colframe = val
                    else: colback = val
            content = content[mo.end():]
        return ("tcolorbox", title, colframe, colback, parse_blocks(content, state))
    return ("__unwrap__", parse_blocks(content, state))

def parse_blocks(text, state):
    blocks = []
    i = 0; n = len(text); free = []

    def flush():
        raw = "".join(free).strip(); free.clear()
        if not raw: return
        if re.match(r"(\\textbf\{)?\s*(Style-locked )?[Pp]rompt for [Ff]ig", raw):
            return
        blocks.append(("para", re.sub(r"\n{2,}", "\n", raw)))

    while i < n:
        m = BLOCK.search(text, i)
        if not m:
            free.append(text[i:]); break
        free.append(text[i:m.start()])
        flush()
        tok = m.group(0); i = m.end()
        if tok.startswith("\\chapter"):
            title, i = _read_brace(text, i-1); blocks.append(("chapter", title.strip()))
        elif tok.startswith("\\section"):
            title, i = _read_brace(text, i-1); blocks.append(("section", title.strip()))
        elif tok.startswith("\\subsection"):
            title, i = _read_brace(text, i-1); blocks.append(("subsection", title.strip()))
        elif tok == "\\tableofcontents": blocks.append(("toc",))
        elif tok == "\\listoffigures": blocks.append(("lof",))
        elif tok == "\\listoftables": blocks.append(("lot",))
        elif tok == "\\newpage": blocks.append(("pagebreak",))
        elif tok.startswith("\\markboth{"):
            label, i = _read_brace(text, i-1)
            if i < len(text) and text[i] == "{":
                _, i = _read_brace(text, i)
            blocks.append(("setheader", label.strip()))
        elif tok.startswith("\\addcontentsline"):
            for _ in range(3):
                if i < len(text) and text[i] == "{":
                    _, i = _read_brace(text, i)
        elif tok.startswith("\\label{"):
            _, i = _read_brace(text, i-1)
        elif tok.startswith("\\readywhen{"):
            arg, i = _read_brace(text, i-1)
            blocks.append(("box", "readywhen", "Ready-When Checkpoint", [("para", arg.strip())]))
        elif tok.startswith("\\begin{"):
            env, i = _read_brace(text, i-1)
            cs, ce = find_env_end(text, env, i)
            node = _parse_env(env, text[cs:ce], state)
            i = ce + len("\\end{%s}" % env)
            if node[0] == "__unwrap__":
                blocks.extend(node[1])
            else:
                blocks.append(node)
        elif tok.startswith("\\end{document}"):
            break
    flush()
    return blocks

# ─────────────────────────  inline markup  ─────────────────────────
MATH = {"sim":"~","approx":"\u2248","pm":"\u00b1","times":"\u00d7","pi":"\u03c0",
        "rightarrow":"\u2192","to":"\u2192","leq":"\u2264","geq":"\u2265","le":"\u2264",
        "ge":"\u2265","neq":"\u2260","infty":"\u221e","cdot":"\u00b7","dots":"\u2026",
        "alpha":"\u03b1","beta":"\u03b2","lambda":"\u03bb","sigma":"\u03c3","mu":"\u03bc",
        "Delta":"\u0394","delta":"\u03b4","emptyset":"\u2205","Rightarrow":"\u21d2"}
P_AMB, P_PCT, P_UND, P_HAS, P_TIL, P_DOL, P_DQT, P_NBSP = ("\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08")
P_BR, P_DASH3 = "\x12","\x0b"
P_LQ, P_RQ = "\x13","\x14"
TT = "\x11"

NOCMD = ("\\thispagestyle","\\pagestyle","\\LARGE","\\Large","\\large","\\normalsize",
         "\\footnotesize","\\scriptsize","\\tiny","\\small","\\bfseries","\\itshape",
         "\\mdseries","\\upshape","\\slshape","\\ttfamily","\\sffamily","\\rmfamily",
         "\\raggedright","\\raggedleft","\\centering","\\noindent","\\vfill","\\fill")
STYLE_GROUP = re.compile(
    r'^\s*(\\LARGE|\\Large|\\large|\\normalsize|\\footnotesize|\\scriptsize|\\tiny|\\small'
    r'|\\bfseries|\\itshape|\\mdseries|\\upshape|\\noindent|\\raggedright|\\centering'
    r'|\\ttfamily|\\sffamily)\s*')

def _match_brace(text, i):
    depth = 0
    for k in range(i, len(text)):
        if text[k] == "{": depth += 1
        elif text[k] == "}":
            depth -= 1
            if depth == 0: return k + 1
    return len(text)

def clean_groups(text):
    out, i, n = [], 0, len(text)
    while i < n:
        if text[i] == "{":
            j = _match_brace(text, i)
            inner = text[i+1:j-1]
            m = STYLE_GROUP.match(inner)
            if m:
                out.append(clean_groups(inner[m.end():]))
            else:
                out.append(text[i:j])
            i = j
        else:
            out.append(text[i]); i += 1
    return "".join(out)

def clean_latex(text):
    text = clean_groups(text)
    text = re.sub(r"\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}", "", text)
    text = re.sub(r"\\label\{[^}]*\}", "", text)
    text = re.sub(r"\\thispagestyle\{[^}]*\}", "", text)
    text = re.sub(r"\\pagestyle\{[^}]*\}", "", text)
    text = re.sub(r"\\setlength\{[^}]*\}\{[^}]*\}", "", text)
    text = re.sub(r"\\vspace\*?\{[^}]*\}", "", text)
    for c in NOCMD:
        text = text.replace(c, "")
    text = text.replace("\\hrulefill", "__________")
    text = text.replace("\\today", "October 2026")
    text = text.replace("\\qquad", "  ").replace("\\quad", " ")
    text = text.replace("\\par", " ")
    return text

def _rc(text, cmd, func):
    pat = "\\" + cmd; out, i = [], 0
    while True:
        j = text.find(pat, i)
        if j < 0: out.append(text[i:]); break
        if j+len(pat) < len(text) and text[j+len(pat)] == "{":
            content, k = _read_brace(text, j+len(pat)); out.append(text[i:j]); out.append(func(content)); i = k
        else:
            out.append(text[i:j+len(pat)]); i = j+len(pat)
    return "".join(out)

def _rc2(text, cmd, func):
    pat = "\\" + cmd; out, i = [], 0
    while True:
        j = text.find(pat, i)
        if j < 0: out.append(text[i:]); break
        if j+len(pat) < len(text) and text[j+len(pat)] == "{":
            a, k = _read_brace(text, j+len(pat))
            if k < len(text) and text[k] == "{":
                b, k2 = _read_brace(text, k); out.append(text[i:j]); out.append(func(a, b)); i = k2
            else:
                out.append(text[i:j+len(pat)]); i = j+len(pat)
        else:
            out.append(text[i:j+len(pat)]); i = j+len(pat)
    return "".join(out)

def _clean(c):
    c = (c.replace("\\&", P_AMB).replace("\\%", P_PCT).replace("\\_", P_UND)
          .replace("\\#", P_HAS).replace("\\$", P_DOL).replace('\\\"', P_DQT))
    c = html.escape(c, quote=False)
    c = (c.replace(P_AMB, "&amp;").replace(P_PCT, "%").replace(P_UND, "_")
          .replace(P_HAS, "#").replace(P_DOL, "$").replace(P_DQT, '"'))
    return c

def _do_math(m):
    c = m.group(1).strip()
    if c in MATH: return MATH[c]
    cm = re.match(r"\\([a-zA-Z]+)", c)
    if cm and cm.group(1) in MATH: return MATH[cm.group(1)]
    return c

def inline_markup(text):
    text = clean_latex(text)
    text = text.replace("\n", " ")
    text = re.sub(r"\\\\(\[[^\]]*\])?", P_BR, text)
    tts = []
    def grab(c):
        tts.append(c); return "%s%d%s" % (TT, len(tts)-1, TT)
    text = _rc(text, "texttt", grab)
    text = (text.replace("\\&", P_AMB).replace("\\%", P_PCT).replace("\\_", P_UND)
            .replace("\\#", P_HAS).replace("\\$", P_DOL).replace("\\~", P_TIL)
            .replace('\\\"', P_DQT).replace("~", P_NBSP).replace("``", P_LQ).replace("''", P_RQ)
            .replace("\\,", " ").replace("\\;", " "))
    text = html.escape(text, quote=False)
    text = _rc(text, "textbf", lambda c: "<b>%s</b>" % c)
    text = _rc(text, "textit", lambda c: "<i>%s</i>" % c)
    text = _rc(text, "emph",   lambda c: "<i>%s</i>" % c)
    text = _rc2(text, "textcolor", lambda a, b:
        '<font color="%s">%s</font>' % (
            {"defblue":"#2563EB","labgreen":"#059669","pitamber":"#D97706","accent":"#E63946",
             "slate":"#334155","checkblack":"#111827"}.get(re.sub(r"![0-9]+$","",a.strip()), "#111827"), b))
    text = _rc2(text, "colorbox", lambda a, b: b)
    for t in ("F", "P", "R"):
        text = text.replace("\\tier%s" % t,
            '<font color="%s"><b>[%s]</b></font>\u00a0' % (hexstr(TIER_COLOR[t]), t))
    text = re.sub(r"\$([^$]*)\$", _do_math, text)
    text = text.replace("---", P_DASH3).replace("--", "\u2013").replace(P_DASH3, "\u2014")
    text = re.sub(r"\\[ \t]", " ", text)
    text = (text.replace(P_AMB, "&amp;").replace(P_PCT, "%").replace(P_UND, "_")
            .replace(P_HAS, "#").replace(P_TIL, "~").replace(P_DOL, "$").replace(P_DQT, '"')
            .replace(P_NBSP, "&nbsp;").replace(P_LQ, "\u201c").replace(P_RQ, "\u201d").replace(P_BR, "<br/>"))
    text = re.sub(TT + r"(\d+)" + TT, lambda m: '<font name="DVMono" size="8.5" color="#111827">%s</font>' % _clean(tts[int(m.group(1))]), text)
    return text.strip()

# ─────────────────────────  flowables  ─────────────────────────
def para(text, style="body"):
    return Paragraph(inline_markup(text), ST[style])

def tier_flows(text):
    t = text.strip().strip("\\").strip()
    m = {"fbadge":"F","pbadge":"P","rbadge":"R"}.get(t)
    if not m: return None
    return [HRFlowable(width=26, thickness=2.2, color=TIER_COLOR[m], hAlign="LEFT", spaceAfter=2),
            Paragraph('<font name="DVSans-Bold" color="%s">%s \u2014 %s</font>' %
                      (hexstr(TIER_COLOR[m]), m, TIER_NAME[m]),
                      ParagraphStyle("tier", fontName="DVSans", fontSize=8, leading=11, textColor=SLATE))]

def walk(bs):
    for b in bs:
        if b[0] == "para":
            yield Paragraph(inline_markup(b[1]), ST["boxbody"])
        elif b[0] == "list":
            yield from list_flows(b[2])

def box_flowables(kind, title, inner_blocks, border=None, bg=None):
    if kind in BOX_KIND:
        _t, border, bg = BOX_KIND[kind]
    elif kind == "readywhen":
        border, bg = INK, INKBG
    if border is None:
        border, bg = INK, LGRAY
    cell = [Paragraph('<font name="DVSans-Bold" color="%s">%s</font>' % (hexstr(border), inline_markup(title)), ST["boxtitle"]),
            Spacer(1, 3)]
    cell += list(walk(inner_blocks))
    t = Table([[cell]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg), ("BOX", (0,0), (-1,-1), 1, border),
        ("LINEBEFORE", (0,0), (0,-1), 3, border),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8)]))
    t.spaceBefore = 4; t.spaceAfter = 8
    return [t]

def selftest_flowables(items):
    inner = []
    for k, it in enumerate(items, 1):
        inner.append(Paragraph('<font name="DVSans-Bold" color="#2563EB">%d.</font>\u00a0%s' % (k, inline_markup(it)),
            ParagraphStyle("st", fontName="DVSerif", fontSize=10, leading=14.5, textColor=INK,
                           leftIndent=14, firstLineIndent=-14, spaceAfter=4)))
    cell = [Paragraph('<font name="DVSans-Bold" color="#2563EB">Self-Test \u2014 %d Questions</font>' % len(items), ST["boxtitle"]),
            Spacer(1, 3)] + inner
    t = Table([[cell]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), WHITE), ("BOX", (0,0), (-1,-1), 1, DBLUE),
        ("LINEBEFORE", (0,0), (0,-1), 3, DBLUE),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8)]))
    t.spaceBefore = 4; t.spaceAfter = 8
    return [t]

def list_flows(items):
    if not items: return [Spacer(1, 2)]
    return [Paragraph('\u2022\u2002%s' % inline_markup(it),
        ParagraphStyle("li", parent=ST["body"], leftIndent=16, firstLineIndent=-16,
                       spaceAfter=3, alignment=TA_LEFT)) for it in items]

def code_flowables(code):
    body = "<br/>".join(_clean(ln) if ln.strip() else "&nbsp;" for ln in code.split("\n"))
    p = Paragraph(body, ST["code"])
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), LGRAY), ("BOX", (0,0), (-1,-1), 0.6, LINE),
        ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8)]))
    t.spaceBefore = 3; t.spaceAfter = 8
    return [t]

def table_flowables(rows):
    if not rows: return [Spacer(1, 2)]
    ncol = max(len(r) for r in rows)
    data = []
    for ri, r in enumerate(rows):
        st = ST["cellB"] if ri == 0 else ST["cell"]
        data.append([Paragraph(inline_markup(r[ci]) if (ci < len(r) and r[ci]) else "&nbsp;", st) for ci in range(ncol)])
    widths = ([CW] if ncol == 1 else [CW*0.34] + [CW*0.66/(ncol-1)]*(ncol-1))
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [("BACKGROUND",(0,0),(-1,0),LSLATE),("LINEBELOW",(0,0),(-1,0),1,SLATE),
             ("LINEABOVE",(0,0),(-1,0),1,SLATE),("LINEBELOW",(0,-1),(-1,-1),0.6,LINE),
             ("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),
             ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
             ("VALIGN",(0,0),(-1,-1),"TOP")]
    for ri in range(1, len(rows)):
        if ri % 2 == 0: style.append(("BACKGROUND",(0,ri),(-1,ri),ZEBRA))
    t.setStyle(TableStyle(style)); t.spaceBefore = 4; t.spaceAfter = 10
    return [t]

def figure_flowables(path, cap, key):
    flows = []
    if path and os.path.exists(path):
        from PIL import Image as PILImage
        try:
            with PILImage.open(path) as im: w, h = im.size
        except Exception:
            w, h = 1000, 600
        dw = CW*0.94; dh = dw*(h/w)
        if dh > CW: dh = CW; dw = dh*(w/h)
        flows.append(Image(path, width=dw, height=dh, hAlign="CENTER"))
    if cap:
        flows.append(Paragraph('<font name="DVSans-Bold">Fig %s.</font> %s' % (state_ref["fig_counter"], inline_markup(cap)), ST["cap"]))
    flows.append(Spacer(1, 8))
    return flows

def render_titlepage(content):
    flows = []
    sizemap = {"\\LARGE": (31, "DVSans-Bold"), "\\Large": (17, "DVSans-Bold"),
               "\\large": (13, "DVSans"), "\\normalsize": (11.5, "DVSerif"),
               "\\small": (9.5, "DVSerif"), "\\footnotesize": (8, "DVSerif")}
    for ln in content.split("\n"):
        ln = ln.strip()
        if not ln:
            continue
        m = re.match(r"\\vspace\*?\{([^}]+)\}", ln)
        if m:
            cm = float(re.sub(r"[^0-9.]", "", m.group(1)))
            flows.append(Spacer(1, cm * 28.35)); continue
        if ln in ("\\vfill", "\\fill"):
            flows.append(Spacer(1, 48)); continue
        m = re.match(r"\{(\\LARGE|\\Large|\\large|\\normalsize|\\small|\\footnotesize)(\\itshape)?(.*?)\\par\}\s*$", ln)
        if m:
            size, fn = sizemap[m.group(1)]
            if m.group(2): fn = "DVSerif-Italic"
            txt = inline_markup(m.group(3))
            st = ParagraphStyle("tp%d" % len(flows), fontName=fn, fontSize=size,
                                leading=size * 1.3, alignment=TA_CENTER, textColor=INK)
            flows.append(Paragraph(txt, st)); flows.append(Spacer(1, 5)); continue
    return flows

class Marker(Flowable):
    def __init__(self, kind, idx, title):
        Flowable.__init__(self); self.kind = kind; self.idx = idx; self.title = title
        self.width = 0; self.height = 0
    def wrap(self, aw, ah): return (0, 0)
    def draw(self):
        state_ref.setdefault("_entries", []).append((self.kind, self.idx, self.title, self.canv.getPageNumber()))

class HeaderSet(Flowable):
    def __init__(self, value):
        Flowable.__init__(self); self.value = value; self.width = 0; self.height = 0
    def wrap(self, aw, ah): return (0, 0)
    def draw(self):
        state_ref["running_header"] = self.value

class TOC(Flowable):
    def __init__(self, rows, kind):
        Flowable.__init__(self); self.rows = rows; self.kind = kind; self._t = None
    def wrap(self, aw, ah):
        if self._t is None: self._t = self._build()
        return self._t.wrap(aw, ah)
    def split(self, aw, ah):
        if self._t is None: self._t = self._build()
        return self._t.split(aw, ah)
    def draw(self):
        if self._t is None: self._t = self._build()
        self._t.drawOn(self.canv, 0, 0)
    def _build(self):
        data = []
        for r in self.rows:
            if self.kind == "toc":
                level, title, page = r
                if level == 0:
                    data.append([Paragraph('<font name="DVSans-Bold">%s</font>' % inline_markup(title), ST["tocC"]),
                                 Paragraph(str(page), ST["tocC"])])
                else:
                    data.append([Paragraph(inline_markup(title), ST["tocS"]), Paragraph(str(page), ST["tocS"])])
            else:
                title, page = r
                data.append([Paragraph(inline_markup(title), ST["tocF"]), Paragraph(str(page), ST["tocF"])])
        t = Table(data, colWidths=[CW-42, 42])
        t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LINEBELOW",(0,0),(-1,-1),0.4,LINE),
            ("LEFTPADDING",(0,0),(-1,-1),2),("RIGHTPADDING",(0,0),(-1,-1),2),
            ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),("ALIGN",(1,0),(1,-1),"RIGHT")]))
        return t

def toc_block(title, rows, kind):
    if not rows:
        return [Paragraph(title, ST["tocH"]), HRFlowable(width=CW, thickness=1, color=LINE, spaceAfter=8),
                Paragraph("(none)", ST["bodyL"]), PageBreak()]
    return [Paragraph(title, ST["tocH"]), HRFlowable(width=CW, thickness=1, color=LINE, spaceAfter=8),
            TOC(rows, kind), PageBreak()]

state_ref = {"running_header": "Front Matter", "fig_counter": 0}

def make_doc(path):
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
                          title="Breaking AI \u2014 Study Manual", author="Olusanya Timothy")
    frame = Frame(ML, MB, CW, PAGE_H-MT-MB, id="main")
    def on_page(canv, docobj):
        canv.saveState()
        pg = canv.getPageNumber()
        if pg > 1:
            canv.setStrokeColor(LINE); canv.setLineWidth(0.5)
            canv.line(ML, PAGE_H-50, PAGE_W-MR, PAGE_H-50)
            canv.setFont("DVSans", 8); canv.setFillColor(FAINT)
            canv.drawString(ML, PAGE_H-42, "Breaking AI \u2014 Study Manual")
            canv.drawRightString(PAGE_W-MR, PAGE_H-42, state_ref.get("running_header","")[:48])
        canv.setFont("DVSans", 8.5); canv.setFillColor(SLATE)
        if pg > 1:
            canv.drawCentredString(PAGE_W/2, 34, str(pg))
        canv.restoreState()
    doc.addPageTemplates([PageTemplate(id="body", frames=[frame], onPage=on_page)])
    return doc

FILES = [("front",None,"frontmatter.tex")] + [("chapter",n,"ch%d.tex"%n) for n in range(11)] + [("appendix",None,"backmatter.tex")]

def _prefix(fn, num):
    return "FM" if fn == "frontmatter.tex" else (str(num) if num is not None else "X")

def attach_captions(blocks):
    out, i = [], 0
    while i < len(blocks):
        b = blocks[i]
        if b[0] == "figure" and not b[2] and i + 1 < len(blocks) and blocks[i+1][0] == "center":
            cap = ""
            for bb in blocks[i+1][1]:
                if bb[0] == "para":
                    m = re.search(r"Fig\s*[A-Za-z0-9]+-[0-9]+\s*:\s*(.*)", bb[1])
                    cap = (m.group(1).strip() if m else bb[1].strip())
                    break
            if cap:
                out.append(("figure", b[1], cap, b[3])); i += 2; continue
        out.append(b); i += 1
    return out

def parse_file(fn, num, state):
    state["fig_prefix"] = _prefix(fn, num); state["tikz_n"] = 0
    path = os.path.join(CH, fn)
    if not os.path.exists(path): return []
    return attach_captions(parse_blocks(strip_comments(open(path, encoding="utf-8").read()), state))

def collect_outlines():
    state = {"x": []}
    toc, lof = [], []
    for mode, num, fn in FILES:
        for b in parse_file(fn, num, state):
            if b[0] == "chapter": toc.append((0, b[1]))
            elif b[0] == "section": toc.append((1, b[1]))
            elif b[0] == "figure": lof.append(b[2])
    return toc, lof

def render(outpath, toc_rows, lof_rows):
    state_ref["running_header"] = "Front Matter"; state_ref["fig_counter"] = 0
    state = {"x": []}
    story = []
    ti = 0; fi = 0; appx = 65
    for mode, num, fn in FILES:
        blocks = parse_file(fn, num, state)
        for b in blocks:
            kind = b[0]
            try:
                if kind == "titlepage":
                    story.extend(render_titlepage(b[1])); story.append(PageBreak())
                elif kind == "chapter":
                    title = b[1]
                    if mode == "appendix":
                        chnum = chr(appx); appx += 1; label = "Appendix %s" % chnum; kicker = "APPENDIX %s" % chnum
                    elif mode == "front":
                        chnum = None; label = title; kicker = "FRONT MATTER"
                    else:
                        chnum = num; label = "Chapter %s" % num; kicker = "CHAPTER %s" % chnum
                    story.append(PageBreak())
                    story.append(HeaderSet(label))
                    story.append(Marker("toc", ti, title)); ti += 1
                    story.append(Spacer(1, 200))
                    story.append(Paragraph(kicker, ST["chapkick"]))
                    story.append(HRFlowable(width=54, thickness=2.4, color=RED, spaceAfter=10, hAlign="LEFT"))
                    story.append(Paragraph(inline_markup(title), ST["chapt"]))
                    story.append(PageBreak())
                elif kind == "setheader":
                    story.append(HeaderSet(b[1]))
                elif kind == "section":
                    title = b[1]
                    story.append(Marker("toc", ti, title)); ti += 1
                    story.append(Paragraph(inline_markup(title), ST["h1"]))
                    story.append(HRFlowable(width=CW, thickness=0.6, color=LINE, spaceAfter=6))
                elif kind == "subsection":
                    story.append(Paragraph(inline_markup(b[1]), ST["h2"]))
                elif kind == "para":
                    tf = tier_flows(b[1])
                    story.extend(tf) if tf is not None else story.append(para(b[1]))
                elif kind == "box":
                    story.extend(box_flowables(b[1], b[2], b[3]))
                elif kind == "tcolorbox":
                    story.extend(box_flowables("tcolorbox", b[1], b[4],
                        border=COLMAP.get(re.sub(r"![0-9]+$","",b[2].strip()), INK),
                        bg=BGMAP.get(b[3].strip(), LGRAY)))
                elif kind == "selftest":
                    story.extend(selftest_flowables(b[1]))
                elif kind == "list":
                    story.extend(list_flows(b[2]))
                elif kind == "center":
                    for bb in b[1]:
                        if bb[0] == "para": story.append(Paragraph(inline_markup(bb[1]), ST["bodyL"]))
                        elif bb[0] == "table": story.extend(table_flowables(bb[1]))
                        elif bb[0] == "code": story.extend(code_flowables(bb[1]))
                        elif bb[0] == "list": story.extend(list_flows(bb[2]))
                        elif bb[0] == "figure":
                            state_ref["fig_counter"] += 1
                            story.append(Marker("fig", fi, bb[2])); fi += 1
                            story.extend(figure_flowables(bb[1], bb[2], bb[3]))
                elif kind == "code":
                    story.extend(code_flowables(b[1]))
                elif kind == "table":
                    story.extend(table_flowables(b[1]))
                elif kind == "figure":
                    state_ref["fig_counter"] += 1
                    story.append(Marker("fig", fi, b[2])); fi += 1
                    story.extend(figure_flowables(b[1], b[2], b[3]))
                elif kind == "pagebreak":
                    story.append(PageBreak())
                elif kind == "toc":
                    story.extend(toc_block("Contents", toc_rows, "toc"))
                elif kind == "lof":
                    story.extend(toc_block("List of Figures", lof_rows, "lof"))
                elif kind == "lot":
                    story.extend(toc_block("List of Tables", [], "lot"))
            except Exception as ex:
                sys.stderr.write("ERR(%s): %s :: %s\n" % (kind, ex, str(b)[:140]))
                story.append(Paragraph("<i>(render error)</i>", ST["bodyL"]))
    dedup = []
    for fl in story:
        if isinstance(fl, PageBreak) and dedup and isinstance(dedup[-1], PageBreak):
            continue
        dedup.append(fl)
    make_doc(outpath).build(dedup)

def _pages(p):
    import fitz
    return fitz.open(p).page_count

if __name__ == "__main__":
    load_fonts(); mkstyles()
    toc_list, lof_list = collect_outlines()
    toc_rows = [(lv, t, "\u00b7") for lv, t in toc_list]
    lof_rows = [(t, "\u00b7") for t in lof_list]
    passes = 0
    for passes in range(1, 6):
        state_ref["_entries"] = []
        render(OUT, toc_rows, lof_rows)
        pmap = {}
        for kind, idx, title, pg in state_ref.get("_entries", []):
            pmap[(kind, idx)] = pg
        new_toc = [(lv, t, pmap.get(("toc", i), "\u00b7")) for i, (lv, t) in enumerate(toc_list)]
        new_lof = [(t, pmap.get(("fig", i), "\u00b7")) for i, t in enumerate(lof_list)]
        if new_toc == toc_rows and new_lof == lof_rows:
            break                       # recorded pages == pages shown -> stable
        toc_rows, lof_rows = new_toc, new_lof
    print("passes:", passes, " pages:", _pages(OUT),
          " toc entries:", len(toc_list), " figures:", len(lof_list))
    print("wrote", OUT)
