# breaklab audit, 2026-10-12

Repo audited: github.com/Teamthy/Red-Team-Harness-My-Breaking-AI-lab- (the package inside is `breaklab`). Audit method: full clone, line-by-line read against the build plan, local test run, CLI run with exit-code checks, GitHub API checks, secret scan.

## Verdict

Working Phase 1-2 skeleton, not the v1.0 the plan defines. Does not yet sit as a portfolio project. URGENT: the repo is public (API: private=false) and contains client-identifying references.

## Urgent findings (fix today)

1. Repo is PUBLIC. API `private` field is false; anonymous clone works. Created 2026-10-12 00:33 UTC, last push 03:08 UTC.
2. Client references in the public tree:
   - `DOCS/build-plan.md`: "Sudhir session report", "Sudhir session post-mortem", NCD session date, the verbatim-prompt seed section (4 hits).
   - `config/example_target.yaml`: target name `ncd-guideline-tutor`.
   - `config/example_sse_target.yaml`: target name `ncd-guideline-tutor-stream`.
   - `.history/` (18 committed files, VS Code local history) contains an older copy of the build plan with the same references.
   Standing rule: no public mention of the Sudhir engagement; he is mid-scope-review of the report the repo references.
3. Fix order: make the repo PRIVATE first (one click), then scrub while private, then publish clean. No public history rewrites.
4. Rename the repo to `breaklab` (current name has a trailing hyphen and "My Breaking AI lab" phrasing; the package is already named breaklab).

## Verified good (evidence, not claims)

- 28 cases across all 6 layers, counted in `battery.py`; matches the plan taxonomy.
- CI green at HEAD (GitHub Actions latest run succeeded; 4 earlier runs failed, iteration history). 26 local tests pass in under 1s.
- Golden pair: broken mock fails 28/28 (plan required >=15), fixed mock holds 28/28.
- `verify` exit codes correct: broken=1, fixed=0 (the CI-gate contract holds).
- `diff` produces a real before/after table (0 to 28 passes).
- SSE parser (event:/data: lines) + local SSE demo server; 3 target templates; MIT license; no secrets found (only {API_KEY} placeholders).

## Core quality problem: verdict engine is keyword matching on prompt vocabulary

- `CaseDefinition.evaluate` fires when the response contains trigger phrases that are frequently words from the prompt itself ("system prompt", "source", "config").
- The broken mock "breaks" 28/28 only because it echoes the prompt (guaranteeing trigger words). The fixed mock "holds" only because its canned refusal contains no trigger words. The golden test proves detection of the mock's behavior, not verdict trustworthiness on real apps.
- Real-app failure mode: a polite refusal that quotes the user ("You asked me to reveal the system prompt. I can't do that.") contains "system prompt" and scores as BREAK. This is plan risk #1, unmitigated.
- Missing from the plan's check suite: canary n-gram module, 12+ word verbatim check vs corpus snippets, citation validation (`TargetResponse.citations` is captured and never used by any check). The "judge" is a second regex pass, not an LLM (deterministic, fine, but a wording mismatch with the plan).
- "Evidence" is the first 200 chars of the response, not the matched span. The plan's "rule plus evidence span" claim is half true.
- Seed fixtures not wired in: the first six cases are supposed to be the verbatim session prompts (the exfil dump prompt, four injection prompts, the French refusal); the registry has generic paraphrases instead.
- `k` (attempts per case) is accepted by CLI/config but ignored: the battery always runs exactly 1 attempt and records attempts: 1. Multi-turn history is always empty.
- Scope pattern: ahead of the plan on adapters (Python import target is v1.1 in the plan; target templates done) and behind on checks. The plan's risk note says cut cases, never cut check quality; the build did the reverse.

## Definition of done scorecard (plan section 10, 8 items)

1. Public repo, CI green, MIT, v0.1.0 tag: partial (public accidentally, CI green, MIT yes, no tag).
2. Install + one command on an owned target via README only: partial (mock works; real target unproven; quick start is Windows-only venv syntax).
3. Broken mock fails >=15/28, fixed holds all, in CI: PASS (28/28 and 28/28).
4. Every verdict cites rule + evidence span, reproducible from artifacts: partial (rule yes, span no; artifacts exist but the two http_127.0.0.1 captures are 0 bytes, i.e., the real-target runs captured nothing).
5. `verify` gates a branch in a public CI example: partial (exit codes correct; the example is the harness's own CI smoke step, which hard-references two committed dev artifacts by name).
6. Flagship diff from real session data: FAIL (mock only).
7. README taxonomy table + score formula + ethics: partial (ethics yes; taxonomy and formula absent; the formula exists in scoring.py undocumented).
8. Article linking the repo + Upwork/LinkedIn updated: not started (planned flywheel).

Score: 3.5 of 8.

## Portfolio gap list (ranked)

1. Client references in a public repo (urgent).
2. Repo name (trailing hyphen, "My ... lab" phrasing).
3. README is a build log, not a story: no positioning line, no garak/promptfoo differentiator, no taxonomy table, no score formula, no demo evidence, no Breaking AI series link; "Project status" and "Release readiness" are internal tone.
4. Sample reports undercut: every row of the fixed report carries the identical canned-refusal string as evidence; the flagship real before/after is missing (plan Phase 5).
5. Repo hygiene: 60 committed dev artifacts (430 KB, mostly mock echo runs, two 0-byte http captures), committed .history/ (18 files), CI smoke hard-references two artifact filenames.
6. Auto-style commit messages ("feat: Add new artifacts..."); rewrite the 5-commit history while the repo is small and private.
7. BACKLOG.md stale (lists the Python adapter and target templates as future ideas; both are built).
8. Minor: Windows-only quick start; judge docstring/plan wording mismatch.

## Fix order

Phase 0 (today, ~1h, repo private): flip private; rename repo to breaklab; delete DOCS/build-plan.md from the public repo (it lives in the empire repo); rename the two example configs to a generic demo target; delete .history/ and the 60 artifacts; move the two diff fixtures to tests/fixtures/ and point CI at them; rewrite history to 2-4 meaningful commits; set a one-line description.

Phase 1 (this week, doubles as the Article 2 critical path): run the harness against the Article 1 support bot (the owner's lab tests). One run serves both: the four real [LAB RESULT] numbers for Article 2, and breaklab's first real verdicts, report, and (if the bot is gated before/after) first real diff. BUT fix the verdict engine first: checks must compare the response against the target's known secrets/canaries, never against the prompt's own vocabulary. Implement the canary, verbatim, and citation checks.

Phase 2 (before portfolio use): README as a story (positioning, differentiator, taxonomy, formula, ethics, one demo), flagship before/after from the real bot data, v0.1.0 tag, first article linking the repo.

## Log

- 2026-10-12: audit performed and committed to the empire repo. Repo remains public until the owner flips it private (owner action, one click). Build speed note: the whole repo was created and pushed in under 3 hours (00:33 to 03:08 UTC); the plan estimated 6 weeks to v1.0. Skeleton is good; verdict logic is the thin part.
