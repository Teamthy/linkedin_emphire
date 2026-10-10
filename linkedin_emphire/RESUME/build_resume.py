#!/usr/bin/env python3
"""Build Timothy's AI/ML Engineer resume as an ATS-safe one-page PDF + DOCX.
Only verified content. Unconfirmed details are listed in the companion file, not invented here."""
from fpdf import FPDF
import os

OUT = "/home/user/linkedin_emphire/RESUME"
os.makedirs(OUT, exist_ok=True)

FONT = "/usr/share/fonts/truetype/dejavu/"
NAVY = (12, 26, 52)
INK = (30, 34, 40)
GREY = (95, 104, 118)


class CV(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


pdf = CV(orientation="P", unit="pt", format="A4")
pdf.set_auto_page_break(auto=True, margin=34)
pdf.set_margins(46, 40, 46)
pdf.add_font("DJV", "", FONT + "DejaVuSans.ttf")
pdf.add_font("DJV", "B", FONT + "DejaVuSans-Bold.ttf")
pdf.add_page()
W = pdf.w - 92  # usable width


def name_block():
    pdf.set_font("DJV", "B", 19)
    pdf.set_text_color(*NAVY)
    pdf.cell(W, 22, "OLUSANYA TIMOTHY", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 10.5)
    pdf.set_text_color(*INK)
    pdf.cell(W, 14, "Software Engineer  |  AI Integration & Red Teaming", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 9)
    pdf.set_text_color(*GREY)
    pdf.cell(W, 13, "Lagos, Nigeria  |  olusanyatimothy54@gmail.com  |  github.com/Teamthy  |  linkedin.com/in/olusanya-timothy",
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)


def section(title):
    pdf.ln(1.5)
    pdf.set_font("DJV", "B", 10.2)
    pdf.set_text_color(*NAVY)
    pdf.cell(W, 14, title.upper(), new_x="LMARGIN", new_y="NEXT")
    y = pdf.get_y()
    pdf.set_draw_color(180, 195, 215)
    pdf.set_line_width(0.8)
    pdf.line(46, y + 1, pdf.w - 46, y + 1)
    pdf.ln(5.5)


def body(text, size=9.05, gap=2.5):
    pdf.set_font("DJV", "", size)
    pdf.set_text_color(*INK)
    pdf.multi_cell(W, 11.3, text)
    pdf.ln(gap)


def bullet(text, size=9.05):
    pdf.set_font("DJV", "", size)
    pdf.set_text_color(*INK)
    x = pdf.get_x()
    pdf.cell(11, 11.3, "\u2022")
    pdf.multi_cell(W - 11, 11.3, text)
    pdf.ln(0.6)


def role(title, meta):
    pdf.set_font("DJV", "B", 10)
    pdf.set_text_color(*INK)
    pdf.cell(W, 13, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 8.8)
    pdf.set_text_color(*GREY)
    pdf.cell(W, 12, meta, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


# ---------------- content ----------------
name_block()

section("Summary")
body("Software engineer who builds LLM-powered features and then breaks them before users do. Ships backend systems "
     "in Go, Node.js, and TypeScript, with Python for tooling, automation, and test harnesses. Runs structured adversarial "
     "testing (prompt injection, tool-call abuse, unauthorized actions, policy bypass) against every AI feature before "
     "launch. Author of Breaking AI, a public 21-part field guide on shipping AI that survives real users.")

section("AI Security & Red Teaming")
bullet("Built a customer support chatbot (LLM API, system prompts, tool wiring) and ran six prompt injection tests "
       "before launch. Four succeeded: system prompt leakage, an unauthorized refund commitment, and a content policy "
       "bypass. Shipped fixes and turned every finding into a repeatable pre-launch test checklist.")
bullet("Write Breaking AI, a public 21-part technical series documenting reproducible failure modes in shipped AI "
       "features, with exact test inputs and the controls that stop them. Article 1 published October 6, 2026.")
bullet("Test the failure modes that actually reach production: hallucinated commitments, prompt leakage, unauthorized "
       "tool calls, and silent quality drift. Trained in NIST AI risk and safety frameworks.")
bullet("Computer vision research background in model evaluation and image data workflows.")

section("Experience")
role("Software Engineer - AI Integration & Red Teaming, Teamart.inc", "Lagos, Nigeria  |  July 2025 - Present")
bullet("Build and ship AI features for client products: LLM chatbots, retrieval pipelines, and tool-calling workflows.")
bullet("Run pre-launch red teaming on AI features (prompt injection, unauthorized actions, policy bypass) and deliver "
       "prioritized findings with fix recommendations.")
bullet("Develop the backend APIs behind those products in Go and Node.js, owning design through deployment.")

role("Senior Developer - YKAY ConsultingHub", "Lagos, Nigeria  |  Nov 2024 - June 2025")
bullet("Led backend development in Go and Node.js across client-facing products, owning API design through deployment.")
bullet("Designed REST APIs and multi-role authentication (JWT, role-based access control) used by client systems with "
       "distinct permission levels.")
bullet("Raised code maintainability by setting modular architecture standards and running Git-based review workflows.")

section("Projects")
role("Nigeria LandSecure - Digital Land Vault & Verification  |  Go, Next.js, PostgreSQL", "")
bullet("Built document storage and verification workflows with role-based permissions to reduce land fraud and "
       "illegal property sales.")
bullet("Resolved concurrency failures in simultaneous verification requests using controlled transaction handling "
       "and database row locking in Go.")
role("EDUos - School Management Ecosystem  |  Node.js, TypeScript, Next.js", "")
bullet("Built a multi-role platform for administrators, teachers, students, and parents with authentication, "
       "dashboards, academic tracking, and messaging.")
bullet("Fixed an authorization middleware flaw that exposed data across roles, then hardened the access model.")
role("KwikPOS - Retail POS & Inventory Management  |  Go, NestJS, Next.js", "")
bullet("Built a full-stack POS with real-time stock tracking and sales analytics on a service-based backend.")
bullet("Cut slow inventory queries under high transaction load by indexing tables and restructuring data models.")

section("Education")
bullet("BSc Computer Science - National Open University of Nigeria  |  Expected April 2028 (studying while working)")
bullet("Previous academic background: Medical Laboratory Science (healthcare domain knowledge)")

section("Certifications & Continuous Learning")
body("NIST AI Bootcamp (AI Risk & Safety Frameworks)  |  AI Engineering & Backend Development (Udemy)  |  "
     "Backend Engineering & Systems Design (self-directed)", gap=0)

pdf.output(f"{OUT}/Timothy_Olusanya_AI_ML_Engineer.pdf")

# ---------------- DOCX (editable twin) ----------------
from docx import Document
from docx.shared import Pt, RGBColor

doc = Document()
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(10)

h = doc.add_paragraph()
r = h.add_run("OLUSANYA TIMOTHY")
r.bold = True
r.font.size = Pt(18)
h.add_run("\nSoftware Engineer | AI Integration & Red Teaming").font.size = Pt(10.5)
h.add_run("\nLagos, Nigeria | olusanyatimothy54@gmail.com | github.com/Teamthy | linkedin.com/in/olusanya-timothy").font.size = Pt(9)


def dsec(t):
    p = doc.add_paragraph()
    r = p.add_run(t.upper())
    r.bold = True
    r.font.size = Pt(10.5)
    return p


def dbody(t):
    return doc.add_paragraph(t)


for para in [x.text for x in doc.paragraphs]:
    pass

dsec("Summary")
dbody("Software engineer who builds LLM-powered features and then breaks them before users do. Ships backend systems in Go, Node.js, and TypeScript with Python for tooling, automation, and test harnesses. Runs structured adversarial testing (prompt injection, tool-call abuse, unauthorized actions, policy bypass) against every AI feature before launch. Author of Breaking AI, a public 21-part field guide on shipping AI that survives real users.")

dsec("AI Security & Red Teaming")
for b in [
    "Built a customer support chatbot (LLM API, system prompts, tool wiring) and ran six prompt injection tests before launch. Four succeeded: system prompt leakage, an unauthorized refund commitment triggered by a single word, and a content policy bypass. Shipped fixes and converted every finding into a repeatable pre-launch test checklist.",
    "Write Breaking AI, a public 21-part technical series documenting reproducible failure modes in shipped AI features, with exact test inputs and the controls that stop them. Article 1 published October 6, 2026.",
    "Test the failure modes that actually reach production: hallucinated commitments, prompt leakage, unauthorized tool calls, and silent quality drift. Trained in NIST AI risk and safety frameworks.",
    "Computer vision research background: model evaluation and image data workflows.",
]:
    doc.add_paragraph(b, style="List Bullet")

dsec("Experience")
p = doc.add_paragraph(); p.add_run("Software Engineer - AI Integration & Red Teaming, Teamart.inc | Lagos, Nigeria | July 2025 - Present").bold = True
for b in [
    "Build and ship AI features for client products: LLM chatbots, retrieval pipelines, and tool-calling workflows.",
    "Run pre-launch red teaming on AI features (prompt injection, unauthorized actions, policy bypass) and deliver prioritized findings with fix recommendations.",
    "Develop the backend APIs behind those products in Go and Node.js, owning design through deployment.",
]:
    doc.add_paragraph(b, style="List Bullet")
p = doc.add_paragraph(); p.add_run("Senior Developer - YKAY ConsultingHub | Lagos, Nigeria | Nov 2024 - June 2025").bold = True
for b in [
    "Led backend development in Go and Node.js across client-facing products, owning API design through deployment.",
    "Designed REST APIs and multi-role authentication (JWT, role-based access control) used by client systems with distinct permission levels.",
    "Raised code maintainability by setting modular architecture standards and running Git-based review workflows.",
]:
    doc.add_paragraph(b, style="List Bullet")

dsec("Projects")
for t, bs in [
    ("Nigeria LandSecure - Digital Land Vault & Verification | Go, Next.js, PostgreSQL", [
        "Built document storage and verification workflows with role-based permissions to reduce land fraud and illegal property sales.",
        "Resolved concurrency failures in simultaneous verification requests using controlled transaction handling and database row locking in Go."]),
    ("EDUos - School Management Ecosystem | Node.js, TypeScript, Next.js", [
        "Built a multi-role platform for administrators, teachers, students, and parents with authentication, dashboards, academic tracking, and messaging.",
        "Fixed an authorization middleware flaw that exposed data across roles, then refactored permission logic and hardened the access model."]),
    ("KwikPOS - Retail POS & Inventory Management | Go, NestJS, Next.js", [
        "Built a full-stack POS with real-time stock tracking and sales analytics on a service-based backend.",
        "Cut slow inventory queries under high transaction load by indexing tables and restructuring data models."]),
]:
    doc.add_paragraph().add_run(t).bold = True
    for b in bs:
        doc.add_paragraph(b, style="List Bullet")

dsec("Education")
doc.add_paragraph("BSc Computer Science - National Open University of Nigeria | Expected April 2028 (studying while working)", style="List Bullet")
doc.add_paragraph("Previous academic background: Medical Laboratory Science (healthcare domain knowledge)", style="List Bullet")
dsec("Certifications & Continuous Learning")
doc.add_paragraph("NIST AI Bootcamp (AI Risk & Safety Frameworks) | AI Engineering & Backend Development (Udemy) | Backend Engineering & Systems Design (self-directed)")

doc.save(f"{OUT}/Timothy_Olusanya_AI_ML_Engineer.docx")
print("PDF + DOCX written")
