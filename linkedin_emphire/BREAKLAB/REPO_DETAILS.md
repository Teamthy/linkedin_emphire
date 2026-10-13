# breaklab repo details and final polish sheet

Verified live via GitHub API on 2026-10-13. Everything below is a current state, not an assumption.

## Live state (Teamthy/My-Breaking-lab)

- Full name: `Teamthy/My-Breaking-lab` (renamed from the original long name; still not `breaklab`)
- Visibility: **public**
- Description: not set
- Homepage: not set
- License: MIT
- Default branch: main
- Last push: 2026-10-12 05:53 UTC, 92 paths
- The v1.0 completion pack IS applied live: `src/breaklab/evidence.py`, `src/breaklab/checks/` (canary, echo, verbatim, sensitive, citation, policy), the guideline_rag fixture pack with PROVENANCE.md, the diff_pair fixtures, `tests/test_seed_fixtures.py`, v2 DOCS, v2 CI
- README live is the intermediate short version, not the polished v2 story README

## The one thing still wrong

`config/example_target.yaml` is still `name: ncd-guideline-tutor` and `config/example_sse_target.yaml` is still `name: ncd-guideline-tutor-stream`. That is a client-identifying name in a public repo, and the standing rule is no public mention of that engagement. This is the only client reference left in the live tree (build-plan.md, .history/, artifacts are all gone).

## Final repo settings (what the About box should say)

- **Name:** `breaklab` (rename from `My-Breaking-lab`; GitHub keeps a redirect from old names, so nothing breaks)
- **Description (one line):** `Deterministic red-team harness for LLM apps: verdicts against the app's own evidence, the exact span that broke, CI-gateable.`
- **Homepage:** leave empty for now (no project site yet); add the Breaking AI series page when it exists. LinkedIn profile is a fallback.
- **Topics:** `ai-security`, `llm`, `red-teaming`, `prompt-injection`, `rag`, `llm-evals`, `ci-cd`, `security-testing`, `python`, `agent-security`
- **License:** MIT (already set, keep)
- **Default branch:** main (keep)
- **Features:** Issues on, Projects off, Wiki off, Packages off
- **Tag:** `v0.1.0` after the next push is CI green

## Owner procedure, in order (~30 minutes)

1. **Flip the repo Private** (Settings, General, last section). Do this before the file swaps so the client name is not public for another push cycle.
2. **Scrub decision (pick one):**
   - Full scrub (recommended, per the audit): while private, replace history with a single clean commit so the client name is gone from history too, not just the tip:
     ```
     git checkout --orphan clean
     git add -A
     git commit -m "breaklab v1.0: evidence-driven checks, 28-case battery, session-fixture golden pair, CI gate"
     git branch -M main
     git push -f origin main
     ```
     The repo has no releases, no other branches in use, and zero open issues, so the force push is safe.
   - Minimum: just replace the two config files and commit. The client name then remains in older commits (visible to anyone who reads history).
3. **Replace the three files** (contents are in this directory, verified byte-for-byte from the tested pack):
   - `README.md` (the polished v2 story README)
   - `config/example_target.yaml` (generic `my-http-chat`)
   - `config/example_sse_target.yaml` (generic `my-http-chat-stream`)
   Commit message: `README: v2 story (positioning, garak/promptfoo comparison, battery taxonomy, evidence model, ethics) + generic example targets`
4. **Locally before pushing**, run the pack verification block (`pytest -q` expecting 62 passed, `ruff check .`, `mypy src`, the four `breaklab verify` lines).
5. **Rename to `breaklab`**, set the description and topics from the sheet above.
6. **Flip back to Public.**
7. **Tag `v0.1.0`** once the new commit's CI is green, and create the release with the notes below.

## v0.1.0 release notes (paste-ready)

```
breaklab v0.1.0.

Evidence-driven verdicts: checks compare the response against the target's
declared evidence (system prompt n-grams, canaries, corpus runs, retrieval
set, sensitive patterns, policy flags), never against the prompt's own
vocabulary. A refusal that quotes the user's own words cannot break.

- 28-case battery across six layers (injection, exfiltration, citation,
  policy, robustness, poisoning), real multi-turn, real k, span evidence
  on every break
- Bundled golden pair from a live red-team session, anonymized with a
  provenance file and an anonymization test: broken 2.41/100, fixed 100/100
- CI-gateable: exit codes plus per-case expectation YAML
- Three bundled target templates (openai-compatible, fastapi, fastapi-sse)
```

## The two pending slots (do not fill from expectation)

- **SLOT-1 (first real-target verdicts):** the support-bot run from today's lab tests. One run serves both: the four Article 2 `[LAB RESULT]` lines and SLOT-1 in the README ("Validation status" section). The config template is `config/support_bot.yaml` in the completion pack (PLANS/2026-10-12_breaklab_v1_completion_pack.md, Phase 2).
- **SLOT-2 (flagship before/after diff):** after the fix lands on the bot, second run plus `breaklab diff before after`.

## Series link, both directions

- Article 2 first comment: "The full version with the raw logs is in the repo: https://github.com/Teamthy/breaklab. One run against the same bot from Article 1. Nothing smoothed."
- README closing line: companion to Article 2 of the Breaking AI series.
- Both go live Tuesday 10:00 WAT, same hour.
