# Aithos Alignment Report — Breaking AI Study Manual

**Checked:** 2026-10-23 (UTC). Every [V] label in the manual refers to a check made on this date.
**Branch:** `arena/3a514eda-linkedin-emphire`

## 1. What was asked

Align the manual with the Aithos research statement, mission, and LARA material supplied with the request: value pluralism, systemic alignment, floors rather than targets, public and stakeholder-defined evaluation, and LARA's method.

## 2. What changed

| File | Change |
|---|---|
| `manual/chapters/frontmatter.tex` | New "Aithos lens" subsection (three commitments) and an evidence-label legend ([V] verified, [S] reported, [R] recommendation, [X] illustrative). |
| `manual/chapters/ch5.tex` | LARA section rebuilt as a labelled table of the published design. Added the four LARA features worth copying (real tools, law-knowledge arms, eval-awareness screening, human override kept beside the judge). Added a "leaderboards move" pitfall. Lab 5 rewritten (see §4). Added a scope pitfall. Corrected the 96.7% and "10 scenarios" claims. |
| `manual/chapters/ch6.tex` | New section "The Aithos Lens: Floors, Not Targets": Aithos framing, target-vs-floor table, two Aithos papers (from abstracts), illustrative worked example, pitfalls. |
| `manual/chapters/ch8.tex` | Liability and fine ceilings, labelled. "Test before you deploy." |
| `manual/chapters/ch10.tex` | Aithos research agenda as stated, each item with a method the reader could bring. |
| `manual/chapters/backmatter.tex` | Verified and labelled references: Aithos article, leaderboard, DOIs, EUR-Lex AI Act and GDPR, Commission guidelines (secondary), UDHR, judge-reliability notes. |
| `manual/lara_lite.py` | Rewritten (see §4). |
| `manual/build/render.py` | Added PDF bookmarks (130 entries, nested) and clickable TOC links. The previous build had none, which missed the spec. |
| `manual/Breaking-AI-Study-Manual.pdf` | Rebuilt: 122 pages. |

## 3. Verification results

| Claim | Status | Evidence |
|---|---|---|
| Art. 5(1)(f) verbatim text | [V] via secondary reproductions (aiact-info, Dutch DPA call for input, Oliver Patel, Wolters Kluwer). EUR-Lex page reachable; full text not paged through (81 chunks). | **Confirm on EUR-Lex before publishing a result.** |
| Art. 5(1)(f) scope: inference from text is outside the prohibition | [S] secondary commentary citing the Commission guidelines (C(2025) 5052 final). Not read from the Commission's own copy. | Drove the rewrite of the lab scenario. |
| Aithos LARA: 10 provisions, 12 models, 3000+ runs, 50+ hours review, ~80% Art. 5 breach, Opus 4.7 breach 46% (54% compliance), Gemini 3.1 Pro breach 90% | [V] Aithos article dated 27 May 2026 | fetched 2026-10-23 |
| Live leaderboard differs from May snapshot (e.g. `claude-opus-4-8`, `gpt-5.6-sol`, runs dated Oct 2026) | [V] lara.aithos.org/#/scenarios | fetched 2026-10-23 |
| 96.7% judge–human agreement | **Not verified.** Not in the May launch article. | Labelled [S] everywhere. |
| "Kimi worst at 7%" | **Not verified.** | Labelled [S]. |
| 156 tools across 22 services; judges from three labs; human override shown beside judge; eval-awareness screening | [S] Aithos "Introducing LARA" text as supplied with the request | Not independently checked. |
| Henselmans et al. (DOI 10.65701/kl7do0n9re): 9 models, 200 items, 6,778 cells, 89.6% inter-judge agreement | [V] abstract on paris-conference.com | Full paper not read. |
| Libert et al. (DOI 10.65701/1zidk02aqx): four conditions, 9 models, up to 99 pp shift | [V] abstract | Full paper not read; the four conditions are not defined in the manual beyond the abstract. |
| GDPR fines €20M / 4%; AI Act €35M / 7% | [V] secondary (Aithos article, confir.eu). | Confirm against GDPR Art. 83(5) and AI Act Art. 99(3) on EUR-Lex. |
| Inspect API: `model_graded_fact(model=list, reducer="majority")`, `system_message`, `generate` | [V] signature inspected in installed inspect-ai 0.3.283 | Also `-T` task args and `--model-role` exist in the CLI. |
| Ollama provider exists in Inspect | [V] `inspect_ai/model/_providers/ollama.py` present | Not run (no Ollama in sandbox). |
| Judge model IDs (`openai/gpt-5.5`, `anthropic/claude-opus-4-7`, `google/gemini-3.1-pro-preview`) | [S] named by Aithos in May 2026 | **Not verified against provider lists.** Check before a live run. |

## 4. Tests performed

1. **Offline end-to-end runs** of `lara_lite.py` with `mockllm/model` for all three `law_state` arms (`none`, `expectation`, `full_text`), 2 epochs each. Verified: runs complete, sample metadata records the arm, the system prompt changes per arm (inspected in the log), invalid arm raises a clear `ValueError`.
2. **Board task construction** (`board=True`) built offline; the judge list and majority reducer are passed to the scorer.
3. **Test-only shim:** the sandbox cannot download the `tiktoken` encoding file, which Inspect's token estimator requires. A stand-in `tiktoken` module was placed in `/tmp/shim` (outside the repo) for these runs only. The manual does not depend on it.
4. **PDF build** with `manual/build/render.py` (reportlab 5.1.0). Build completes in two passes; 122 pages; 130 bookmarks; 33 internal TOC links on the contents page, all resolving; key new phrases are searchable in the text layer.
5. **Visual check** of rendered pages: LARA table (p. 58) and Lab 5 (p. 62) rendered legibly with no overflow.

## 5. What was not tested

- **No live model runs.** No Ollama model was available, and no provider keys were provided. The lab's judge-agreement step and the `board=true` path were not executed against real judges.
- **Not all pages were visually inspected** (only 2 of 122 pages were rasterised). The new Ch. 6 section, Ch. 8 and Ch. 10 insertions, and back matter were checked by text extraction only.
- **EUR-Lex Article 5 full text** was not read end to end.
- **Full Aithos papers** were not read; only their abstracts.
- **The `build/content/*.md` files** use a different markup and are not read by `render.py`. They were not updated, so they now disagree with the `.tex` source. The `.tex` files are canonical.
- **Other chapters** (0–4, 7, 9) were not re-audited for the Aithos alignment. The request was about alignment, not a full rewrite.

## 6. Substantive findings to keep

1. **The original lab's scenario was likely out of scope.** It asked the model to rank staff from chat text, but Art. 5(1)(f) concerns biometric inference. The lab now uses video and voice.
2. **The original lab's provision was a paraphrase**, but was labelled "verbatim". It also dropped "education institutions" and the exception wording. Both are fixed.
3. **The curriculum's LARA numbers mixed verified and unverified claims** (96.7%, Kimi 7%) as established facts. They are now labelled.
4. **Leaderboards change.** The May 2026 snapshot and the October live leaderboard disagree on model versions. Reports must carry a snapshot date.
5. **Judge agreement is not one number.** Henselmans et al. report inter-judge agreement (89.6%), LARA reports judge–human agreement (96.7%, unverified). They measure different things.

## 7. Next steps

1. Confirm the Article 5(1)(f) wording and the Commission guidelines against EUR-Lex and the Commission's own copy.
2. Confirm the GDPR and AI Act fine ceilings against the articles.
3. Check judge model IDs against provider lists before any live run.
4. Run `lara_lite.py` against a real local model (Ollama) and a second grader; record the honest number with the snapshot date.
5. Locate the LARA methodology page and verify the 96.7% figure, or remove it.
6. Read the full Libert et al. and Henselmans et al. papers before using their conditions or statistics.
7. Visually inspect the full PDF, and either regenerate or delete the stale `build/content/*.md`.
