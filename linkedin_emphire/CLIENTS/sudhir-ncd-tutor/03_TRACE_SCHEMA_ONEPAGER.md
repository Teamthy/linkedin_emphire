# Trace Schema - one page (Sudhir)
Per request, ONE jsonl line:
{"request_id","ts","query_hash","retrieved":[{"chunk_id","corpus_hash"}],"prompt_version","gate_verdicts":{"citation_gate":"pass|strip|reject","echo_check":"pass|hit","dosage_filter":"pass|hit","ingest_flags":[]},"model","tokens_in","tokens_out","cost_usd"}
## Why each field exists
- corpus_hash: proves WHICH index version answered - re-runs and audits depend on it
- prompt_version: "who changed the prompt and when" stops being a Slack archaeology project
- gate_verdicts: the security story; the judge can score an answer, only these flags say what code enforced
- tokens/cost: the denial-of-wallet tripwire
## Interview line
"Requests carry the permission state at the moment of action. I designed the schema that makes my system auditable three months later, and I built the gates that write to it."
## Test yourself
Pick five answers from yesterday. Can you rebuild what they saw? If no, the trace is decorative.
