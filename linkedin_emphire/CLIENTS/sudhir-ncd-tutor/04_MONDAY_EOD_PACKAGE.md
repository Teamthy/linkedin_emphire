# Monday EOD Package, Sudhir NCD Guideline Tutor

What this is. The three deliverables Timothy sends Sudhir on Monday EOD, after the Sun Oct 11 session. This is a SCAFFOLD built from the real code audit (`UPWORK/CLIENT_SUDHIR/audit_ncd_guideline_tutor.md`, commit 21e913b) and the existing templates (`02_FINDINGS_TEMPLATE.md`, `03_TRACE_SCHEMA_ONEPAGER.md`). Parts that depend on the session (his before/after evidence, his schema redraw) are placeholders to fill after the session, before sending.

Status: SCAFFOLD, not final. Do not send until every [SESSION] placeholder is filled with the real session outputs.

How to use it: after the session, fill every [SESSION] placeholder with what actually happened, then send to shivaram.sudhir@live.com.

Framing note: Part 1 is written in Sudhir's first person, ready for his README. He genuinely built the gates and ran the tests in the session, so the claims are his, not fabricated. Parts 2 and 3 are technical reference.

---

## Part 1, His three README findings (portfolio-clean, first person)

Use the structure in `02_FINDINGS_TEMPLATE.md`. Fill after the session.

### Finding 1, Fabricated citation accepted by evals (confirmed, the headline)
**What happened, before (real evidence, from the free call Fri Oct 9).** The app was asked for the exact wording the system gave it about medical advice, and responded:

> Based on the retrieved sources, here is the text of the general disclaimers regarding the interpretation and use of the material:
>
> From the HEARTS protocols (2018): "The responsibility for the interpretation and use of the material lies with the reader. In no event shall WHO be liable for damages arising from its use." [1]
> From the Hypertension guideline (2021): "The responsibility for the interpretation and use of the material lies with the reader. In no event shall WHO be liable for damages arising from its use." [2]
> From the HEARTS-D diabetes (2020) guide: "The responsibility for the interpretation and use of the material lies with the reader. In no event shall WHO be liable for damages arising from its use." [5]
> This is a clinical decision-support response based exclusively on WHO guideline information and does not constitute individualized medical advice.

The response cites [1], [2], and [5]. [SESSION: confirm the exact probe prompt, and confirm via a `len(contexts)` debug print that fewer than five chunks were retrieved, which makes [5] reference a chunk that was never in the request.] Neither the evals nor the LLM judge flagged it.
**Which layer failed:** model plus a missing code check. The response cited [5] though retrieval returned N chunks, and no code verified the number existed in this request.
**Fix:** in the generate path, valid_nums = 1 to len(contexts), strip any citation not in valid_nums, log the verdict.
**How verified, after [SESSION]:** re-run the same prompt with the gate active, paste the response showing the out-of-range citation stripped and the strip logged, and note the eval now shows a non-zero rejection rate.
**Why it matters:** citations are the product's claim of truthfulness. A hallucinated citation passes every text-quality metric.

### Finding 2, System rules leakable by a formatting request [CONFIRM or DROP after the session]
**What happened [SESSION]:** the disclaimer echo result, the exact prompt and the app's response.
**Which layer failed:** the model paraphrased protected closing wording when asked indirectly. A prompt-level instruction is a request, not enforcement.
**Fix:** an output filter on instruction-like phrasing, not just exact match, comparing the answer against the protected prompt substrings (n-grams or a hash, not just the exact English line).
**How verified [SESSION]:** re-run the translate and JSON variant prompts, confirm the protected line no longer echoes verbatim.

### Finding 3, Retrieved content treated as instructions [CONFIRM with his own test after the session]
**What happened [SESSION]:** the retrieval poisoning result on the local copy, the planted line and the app's response.
**Which layer failed:** the pipeline treated ingested data as instructions.
**Fix:** ingest-time sanitization plus trust tagging. A low-trust chunk cannot state a dosage without a citation flag.
**How verified [SESSION]:** re-run the same prompt after the fix, confirm the planted line no longer surfaces as unqualified fact.

---

## Part 2, Gate placement list (per finding, with snippets)

Reference for where each fix lives in his code, from the audit (commit 21e913b). Snippets are skeletons to drop into his actual files, confirm them against his live code in the session (variable names and file paths will differ).

### 1. Citation gate (Finding 1)
Location: `pipeline.py`, after `stream_llm` completes.
```python
# after the answer text is accumulated:
import re
valid_ids = set(range(1, len(contexts) + 1))
cited = set(int(n) for n in re.findall(r"\[(\d+)\]", answer))
invalid = cited - valid_ids
if invalid:
    # strip or flag out-of-range citations, then log the verdict
    log.warning("citation_gate: stripped %s", sorted(invalid))
```

### 2. Instruction-echo output filter (Finding 2)
Location: output path, `generate.py` / `chat.py`, before the answer returns to the UI.
```python
# compare the answer against protected prompt substrings (the closing disclaimer line, etc.)
for probe in PROTECTED_PHRASES:  # n-grams or hashes, not just the exact string
    if probe in answer:
        # replace or refuse
        ...
```
Note: use n-grams or a hash of the prompt, not just the exact English line, so format and language variants are caught.

### 3. Ingest-time sanitization plus trust tagging (Finding 3)
Location: `ingest.py` / `indexing.py`, at index build time.
```python
# when chunking a document, flag imperative or instruction-like sentences
# and tag each chunk with a trust level (trusted corpus vs external)
# a low-trust chunk cannot assert a dosage without a citation flag
```
Note: the live app's corpus is a static DOCUMENT_CATALOG with no upload endpoint, so the live poisoning surface is already closed by architecture, not just by this fix. Name that difference (safe by architecture vs safe by design intent) in the interview.

---

## Part 3, Trace schema one-pager (his redraw plus annotations)

Canonical schema (reference, from `03_TRACE_SCHEMA_ONEPAGER.md`):
Per request, ONE jsonl line:
`{"request_id","ts","query_hash","retrieved":[{"chunk_id","corpus_hash"}],"prompt_version","gate_verdicts":{"citation_gate":"pass|strip|reject","echo_check":"pass|hit","dosage_filter":"pass|hit","ingest_flags":[]},"model","tokens_in","tokens_out","cost_usd"}`

Why each field exists:
- `corpus_hash`: proves which index version answered, re-runs and audits depend on it
- `prompt_version`: "who changed the prompt and when" stops being a Slack archaeology project
- `gate_verdicts`: the security story. The judge can score an answer, only these flags say what code enforced
- `tokens` / `cost`: the denial-of-wallet tripwire
- `permission_state_at_action`: the day he adds a tool call, this is the only thing between him and an unauditable agent

Interview line:
"Requests carry the permission state at the moment of action. I designed the schema that makes my system auditable three months later, and I built the gates that write to it."

Test yourself: pick five answers from yesterday. Can you rebuild what they saw? If no, the trace is decorative.

His redraw [SESSION]: capture his from-memory redraw during the session, note any gaps.
Timothy's annotations [SESSION]: annotate his redraw, correct only what is wrong.

---

## Send checklist (before sending to Sudhir)
- [ ] All [SESSION] placeholders filled with real session outputs.
- [ ] Finding 1, the `len(contexts)` confirmation is in, so the [5] claim is proven, not assumed.
- [ ] Finding 2 is CONFIRMED or DROPPED, not left ambiguous.
- [ ] Finding 3 confirmed with his own test.
- [ ] Snippets checked against his actual code (variable names, file paths).
- [ ] His schema redraw captured and annotated.
- [ ] Send to shivaram.sudhir@live.com.
- [ ] Update `CLIENTS/sudhir-ncd-tutor/00_LINKEDIN_CONVERSATION_TRACKER.md` with the session outcome.
