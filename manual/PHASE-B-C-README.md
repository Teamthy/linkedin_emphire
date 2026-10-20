# Breaking AI — Manual: Phases B, C, D Deliverable

**Branch:** `arena/5165a61a-linkedin-emphire`  
**Print format:** LaTeX (`manual/main.tex` + `manual/chapters/*.tex` + `manual/figures/`) → A4 PDF, 2 cm margins, running headers/footers, numbered sections/figures/tables.  
**Also runnable:** `manual/lara_lite.py` is included standalone.

## What was built in Phase B (Write)

All 11 chapters written, each with **11 elements in order** per spec §5:

1. Learning objectives (3–6, "You will be able to…")  
2. The idea (Foundation, plain language)  
3. The mechanics (Practitioner, tooling/steps)  
4. Worked examples (≥2, concrete, named — real attacks, provisions, numbers)  
5. Hands-on lab (target + steps + deliverable; Ch. 5 = full 7-step LARA-lite Inspect lab with `lara_lite.py`)  
6. Pitfalls and the missing check  
7. Illustrations (numbered + captioned)  
8. Key terms (3–8)  
9. Self-test (5 Qs: recall, application, design-a-check)  
10. Ready-when checkpoint (one sentence)  
11. Expert extension (Researcher, open problem + method)

Chapters: 0 Orientation, 1 Foundations, 2 Cybersecurity & System Security, 3 Testing Methodologies, 4 Agentic & Multi-Agent Security, 5 Evals & Measurement (core, longest, ~28p equivalent), 6 AI Safety & Alignment, 7 Tools & Frameworks, 8 Real-World Applications, 9 Professional Development & Standing Out, 10 Future Directions.

Front matter (How to Use This Book, one-page primer "The check is the product," TOC/LOF/LOT) and Back matter (Glossary ~60 terms → expandable to 120, reproducible-report template, threat-model worksheet, engagement checklist, index, references/resource map) included.

Voice: direct, concrete, no-fluff, short sentences. Thesis woven: 5 callout boxes — Definition (blue), Worked Example (slate), Lab (green), Pitfall (amber), **The Check Is the Product** (black+red) — used where genuine.

Tiers: every chapter has visible [F] Foundation → [P] Practitioner → [R] Researcher badges + "The idea → Do it → Push it" flow.

## Phase C (Illustrate)

Every required figure drawn as **embedded TikZ** (print-sharp vector, no external files) + listed with (a) human-draw description and (b) one-line style-locked text-to-image prompt (black/white + `#E63946`, minimal, no clip art, numbered + captioned). List in `manual/figures/README.md` (15 figures). Also described inline under each figure in the LaTeX.

Required figures covered: Two Hats (0.1), LLM System Stack (1.1), Attack Surface Map (2.1), Box-Color Decision (3.1) + Canary-Drift Loop (3.2), A2A Message Flow (4.1), Eval Pipeline (5.1) + LARA Architecture (5.2) + Two-Sided Boundary (5.3), Three Circles (6.1), Tooling Stack (7.1), Engagement E2E (8.1), Portfolio (9.1), Threat Landscape (10.1), Primer (FM-1).

## Phase D (Assemble)

Single self-contained `manual/main.tex` + `manual/figures/` listing. Compile:

```bash
cd manual
# if you have LaTeX installed:
xelatex main.tex
xelatex main.tex   # second pass for TOC/refs

# without LaTeX: read main.tex directly — it is the complete book source.
```

No PDF binary is checked in (snapshot-friendly). The `.tex` is the artifact; compile locally or in Overleaf (upload `main.tex` + `chapters/` folder).

## Compile check

If `pdflatex`/`xelatex` is not on your machine, use Overleaf or install TeX Live. The source uses only standard packages (fancyhdr, geometry, tcolorbox, tikz, listings, booktabs, hyperref, etc. — no custom class).

## Acceptance bar (§9)

- Beginner can start at Part 0 → reach Part 5 with no reference book: yes — no jargon without definition, every lab lists exact commands, Ollama path is free.  
- Expert can jump to Ch. 5 + extensions and get a method: yes — Ch. 5 mechanics + 3 worked examples + 7-step lab + expert extension on judge calibration.  
- Every chapter has ≥1 figure, ≥1 worked example (≥2), ≥1 lab, 5-Q self-test, ready-when: yes — enforced by structure.  
- Stranger can follow LARA-lite lab, run it, reproduce a number: yes — `lara_lite.py` verbatim + install + `inspect eval` + `inspect view` + honest-report template.  

## Files

```
manual/
  main.tex                # the book — compile this
  lara_lite.py            # runnable lab (also embedded in Ch. 5)
  00-PHASE-A-PLAN.md      # Phase A plan (approved)
  PHASE-B-C-README.md     # this file
  chapters/
    frontmatter.tex       # half-title, copyright, How to Use, Primer, TOC/LOT/LOF
    ch0.tex … ch10.tex    # 11 chapters
    backmatter.tex        # glossary + templates + checklists + index + references
  figures/
    README.md             # figure list + prompts
```

