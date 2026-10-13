# Breaklab repo audit, round 2 (2026-10-12)

Repo: https://github.com/Teamthy/Red-Team-Harness-My-Breaking-AI-lab-
Audited commit: `b87ac0b` (pushed 2026-10-12 05:53 UTC, CI green)
Method: fresh clone, full git history scan, local test/lint/type run, CI cross-check.

## What changed since round 1 (HEAD was `ecb192e`)

Commit `b87ac0b` applied the v1 completion pack and a cleanup pass:

- `.history/` (18 files) deleted from the tree
- `DOCS/build-plan.md` (the empire plan, client name x4) deleted from the tree
- ~60 dev artifacts under `artifacts/` deleted from the tree
- `.gitignore` now ignores `.history/`, `artifacts/`, `.breaklab/`
- Pack fixtures added: `tests/fixtures/guideline_rag/` (6 files + `PROVENANCE.md`), `tests/fixtures/diff_pair/`, `tests/test_seed_fixtures.py`
- README rewritten, no client references, generic `my-support-bot` example
- Docs added: `DOCS/live-validation.md`, `DOCS/release-readiness.md`, `BACKLOG.md` trimmed

## Verification (run locally at `b87ac0b`, matches CI)

| Check | Result |
| --- | --- |
| pytest | 62/62 passed (0.45s) |
| ruff | clean |
| mypy | clean, 28 files |
| CLI exit codes | fixed=0, echo=0, broken=1 (as specified) |
| Golden pair score | broken 2.41/100, fixed passes all 28 |
| diff command | 27-case before/after report generated |
| Fixture scan | zero matches for client name, ncd, huggingface, year, dates, emails, URLs inside `tests/fixtures/` |
| Secrets sweep (HEAD + all history) | no keys, no tokens, no private keys; only demo values marked as demo |
| GitHub Actions on `b87ac0b` | success |

Code quality: publishable. The pack was applied correctly and is pinned by tests.

## Findings, ranked

### F1. CRITICAL. The repo is still public.
`private: false`. No one should have seen this repo at all, let alone publicly, in its current state.

### F2. CRITICAL. The client name is still in the git history.
Deleting a file does not remove it from history. `git clone` + `git show 8f97935:DOCS/build-plan.md` (or any of the 5 older commits) returns the full empire plan with "Sudhir" x4, plus `.history/DOCS/build-plan_*.md` duplicates. Any visitor, search crawler, or Upwork colleague can recover the client's name and the internal plan today. This is the only finding that makes the repo unsafe for any audience.

### F3. HIGH. Client-project fingerprint in HEAD.
`ncd-guideline-tutor` / `ncd-guideline-tutor-stream` survive in three files:
- `config/example_target.yaml` (line 2)
- `config/example_sse_target.yaml` (line 2)
- `tests/test_config.py` (line 37)

Combined with the "clinical guideline assistant" + "WHO guideline" persona in the mock and sample reports, this identifies the client engagement's domain (health/WHO guideline chatbot). `ncd` is on the pack's own FORBIDDEN list for fixtures; the configs were just not covered.

### F4. MEDIUM. History is full of dev-process noise.
- `.history/` 18 files
- ~60 timestamped run outputs under `artifacts/` (20261012T00xxx), including 2 zero-byte `http_127.0.0.1` captures and 4 zero-byte `python_breaklab.example_local_target` files
- one failed CI commit in the chain (`27c7a06`)
No secrets in any of it (swept), but it exposes the build process, timing, and iteration count of a private engagement.

### F5. LOW. Housekeeping.
- No `v0.1.0` tag or release (release-readiness doc says tag when green; it is green)
- Repo name has a trailing dash: `Red-Team-Harness-My-Breaking-AI-lab-`
- Commit author email (`olusanyatimothy54@gmail.com`) on all 6 commits; fine for a personal repo, it just ties the history to his identity

## What the history does NOT contain (verified)

- No real client hostnames or endpoints (configs use `api.example.com`)
- No API keys, tokens, or private keys in any commit
- No client calendar dates, no machine-specific real paths (only authored `/home/app`, `/var/lib/app` demo paths)
- No real target runs: every artifact is mock/python-local output

## Recommended fix, in order

1. NOW, owner, one click: Settings -> General -> Danger zone -> Change visibility -> **Private**. Stops public exposure of F2 immediately. Nothing depends on this repo being public.
2. Kill the old history before it ever goes public again. The repo has 0 stars, 0 forks, 0 PRs, 0 releases: zero external dependencies.
   - Option A (cleanest, recommended for a future public release): delete the repo and recreate it; I push a single clean commit (current `b87ac0b` tree, minus the F3 names) plus the `v0.1.0` tag.
   - Option B (if keeping the repo forever private): I force-push an orphan `main` with the same clean tree. Old objects stay in the private repo but are unreachable.
3. Agent does: rename `ncd-guideline-tutor(-stream)` to generic names in the 3 files, re-run the full check, tag `v0.1.0`.
4. Owner decision: final repo name. Suggestions: `breaklab` (matches package name) or `llm-red-team-harness`.
5. Only after 1-4: SLOT-1 real support-bot run. Its artifacts and commits must land on clean history, or the Article 2 lab tests ship the leak along with them.

## Decision needed from owner

- D1: make the repo private now? (yes/no)
- D2: option A (delete + recreate, clean for public later) or option B (private forever, orphan push)?
- D3: final repo name?
