#!/usr/bin/env python3
"""Build an Aithos Research Engineer tailored resume (PDF + DOCX).
Same verified facts as build_resume.py, plus two real new items (the open
five-test harness and Article 2). Reframed for the Research Engineer JD.
No invented content: no Inspect, no publications, no multi-agent claims."""
from fpdf import FPDF
import os

OUT = "/home/user/linkedin_emphire/RESUME"
os.makedirs(OUT, exist_ok=True)
FONT = "/usr/share/fonts/truetype/dejavu/"
NAVY = (12, 26, 52)
INK = (30, 34, 40)
GREY = (95, 104, 118)

PDF_NAME = "Timothy_Olusanya_Aithos_Research_Engineer.pdf"
DOCX_NAME = "Timothy_Olusanya_Aithos_Research_Engineer.docx"
TITLE = "Software Engineer, AI Evaluation & Safety Tooling"
CONTACT = "Lagos, Nigeria (UTC+1)  |  olusanyatimothy54@gmail.com  |  github.com/Teamthy  |  linkedin.com/in/olusanya-timothy"
OPENWORK = "Open work: github.com/Teamthy/ai-redteam-five-tests (five-test AI red-team harness)"

SUMMARY = (
    "Software engineer who builds and tests AI systems for AI safety, from the build-and-test side. "
    "I design and run reproducible evaluations that check whether an LLM does what it should under real-world "
    "and adversarial conditions, and I write the harnesses so every result traces back to a specific prompt, model, "
    "and commit. I ship clean, tested, documented Python that other engineers build on, and I work with LLMs beyond "
    "single API calls: evaluations, tool-calling and agentic scaffolding, and retrieval. Author of Breaking AI, a "
    "public series on shipping AI that survives real users, and maintainer of an open-source five-test red-team "
    "harness. Self-taught, motivated by AI safety and by work I can verify."
)

AI_BULLETS = [
    "Built an open-source five-test red-team harness (github.com/Teamthy/ai-redteam-five-tests) that runs prompt "
    "injection, retrieval poisoning, tool-description poisoning, and multilingual refusal tests against any "
    "OpenAI-compatible model, resolves tool calls, records raw responses, and reports each failure with its sample "
    "size and rate. Written as clean, tested, documented Python a small team can extend, not a one-off script; every "
    "run is reproducible and traces back to a commit.",
    "Built a customer support chatbot (LLM API, system prompts, tool wiring) and ran six structured prompt-injection "
    "tests before launch; four succeeded (system prompt leakage, an unauthorized refund commitment, a policy bypass). "
    "Fixed each and converted the findings into a repeatable pre-launch checklist.",
    "Write Breaking AI, a public 21-part series documenting reproducible AI failure modes with the exact test inputs "
    "and the controls that stop them. Articles 1 and 2 published (Oct 6 and Oct 13, 2026).",
    "Trained in NIST AI risk and safety frameworks. Background in computer vision model evaluation and image data workflows.",
]

SKILLS = (
    "Python (evaluation harnesses, testing, data pipelines)  |  LLM integration (OpenAI-compatible APIs, tool/function "
    "calling, agentic scaffolding, retrieval/RAG)  |  Security (secret and credential handling, access control, "
    "adversarial testing)  |  Reproducibility (versioned runs, traceability, sampling)  |  Go, Node.js, TypeScript  |  Git"
)

EXPERIENCE = [
    ("Software Engineer, AI Integration & Red Teaming  |  Teamart.inc", "Lagos, Nigeria  |  July 2025 - Present", [
        "Build and ship AI features for client products: LLM chatbots, retrieval pipelines, and tool-calling workflows.",
        "Write clean, tested, documented code that other engineers build on, and own features through deployment.",
        "Run pre-launch red teaming (prompt injection, unauthorized actions, policy bypass) and deliver prioritized findings with fixes.",
    ]),
    ("Senior Developer  |  YKAY ConsultingHub", "Lagos, Nigeria  |  Nov 2024 - June 2025", [
        "Led backend development in Go and Node.js; designed REST APIs and multi-role authentication (JWT, role-based access control).",
        "Raised code maintainability through modular architecture standards and Git-based review workflows.",
    ]),
]

PROJECTS = [
    "EDUos, School Management Platform  |  Node.js, TypeScript, Next.js. Multi-role platform with authentication and "
    "dashboards; fixed an authorization flaw that exposed data across roles, then hardened the access model.",
    "Nigeria LandSecure, Land Verification  |  Go, Next.js, PostgreSQL. Document verification with role-based permissions; "
    "resolved concurrency failures with transaction handling and row locking.",
]

EDUCATION = [
    "BSc Computer Science, National Open University of Nigeria  |  Expected April 2028 (studying while working)",
    "Previous academic background: Medical Laboratory Science (healthcare domain knowledge)",
]

CERTS = ("NIST AI Bootcamp (AI Risk & Safety Frameworks)  |  AI Engineering & Backend Development (Udemy)  |  "
         "Backend Engineering & Systems Design (self-directed)")


# ---------------- PDF ----------------
class CV(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


pdf = CV(orientation="P", unit="pt", format="A4")
pdf.set_auto_page_break(auto=True, margin=34)
pdf.set_margins(46, 36, 46)
pdf.add_font("DJV", "", FONT + "DejaVuSans.ttf")
pdf.add_font("DJV", "B", FONT + "DejaVuSans-Bold.ttf")
pdf.add_page()
W = pdf.w - 92


def name_block():
    pdf.set_font("DJV", "B", 19)
    pdf.set_text_color(*NAVY)
    pdf.cell(W, 22, "OLUSANYA TIMOTHY", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 10.5)
    pdf.set_text_color(*INK)
    pdf.cell(W, 14, TITLE, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 9)
    pdf.set_text_color(*GREY)
    pdf.cell(W, 13, CONTACT, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 9)
    pdf.set_text_color(*NAVY)
    pdf.cell(W, 13, OPENWORK, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)


def section(title):
    pdf.ln(0.5)
    pdf.set_font("DJV", "B", 10.0)
    pdf.set_text_color(*NAVY)
    pdf.cell(W, 13, title.upper(), new_x="LMARGIN", new_y="NEXT")
    y = pdf.get_y()
    pdf.set_draw_color(180, 195, 215)
    pdf.set_line_width(0.8)
    pdf.line(46, y + 1, pdf.w - 46, y + 1)
    pdf.ln(4.3)


def body(text, size=8.95, gap=2.0):
    pdf.set_font("DJV", "", size)
    pdf.set_text_color(*INK)
    pdf.multi_cell(W, 11.0, text)
    pdf.ln(gap)


def bullet(text, size=8.95):
    pdf.set_font("DJV", "", size)
    pdf.set_text_color(*INK)
    pdf.cell(11, 11.0, "\u2022")
    pdf.multi_cell(W - 11, 11.0, text)
    pdf.ln(0.3)


def role(title, meta):
    pdf.set_font("DJV", "B", 10)
    pdf.set_text_color(*INK)
    pdf.cell(W, 13, title, new_x="LMARGIN", new_y="NEXT")
    if meta:
        pdf.set_font("DJV", "", 8.8)
        pdf.set_text_color(*GREY)
        pdf.cell(W, 12, meta, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)


name_block()
section("Summary")
body(SUMMARY)
section("AI Safety Evaluation & Tooling")
for b in AI_BULLETS:
    bullet(b)
section("Skills")
body(SKILLS)
section("Experience")
for title, meta, bs in EXPERIENCE:
    role(title, meta)
    for b in bs:
        bullet(b)
section("Projects")
for p in PROJECTS:
    bullet(p)
section("Education")
for e in EDUCATION:
    bullet(e)
section("Certifications & Continuous Learning")
body(CERTS, gap=0)
pdf.output(f"{OUT}/{PDF_NAME}")

# ---------------- DOCX (editable twin) ----------------
from docx import Document
from docx.shared import Pt

doc = Document()
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(10)

h = doc.add_paragraph()
h.add_run("OLUSANYA TIMOTHY").bold = True
h.runs[0].font.size = Pt(18)
h.add_run("\n" + TITLE).font.size = Pt(10.5)
h.add_run("\n" + CONTACT).font.size = Pt(9)
h.add_run("\n" + OPENWORK).font.size = Pt(9)


def dsec(t):
    doc.add_paragraph(t.upper()).runs[0].bold = True


dsec("Summary")
doc.add_paragraph(SUMMARY)
dsec("AI Safety Evaluation & Tooling")
for b in AI_BULLETS:
    doc.add_paragraph(b, style="List Bullet")
dsec("Skills")
doc.add_paragraph(SKILLS)
dsec("Experience")
for title, meta, bs in EXPERIENCE:
    p = doc.add_paragraph()
    p.add_run(title + ("  |  " + meta if meta else "")).bold = True
    for b in bs:
        doc.add_paragraph(b, style="List Bullet")
dsec("Projects")
for p in PROJECTS:
    doc.add_paragraph(p, style="List Bullet")
dsec("Education")
for e in EDUCATION:
    doc.add_paragraph(e, style="List Bullet")
dsec("Certifications & Continuous Learning")
doc.add_paragraph(CERTS)
doc.save(f"{OUT}/{DOCX_NAME}")

print("pages:", pdf.pages_count)
print("PDF  ->", f"{OUT}/{PDF_NAME}")
print("DOCX ->", f"{OUT}/{DOCX_NAME}")
