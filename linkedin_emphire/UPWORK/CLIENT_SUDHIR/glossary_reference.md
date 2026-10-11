# Key Terms Reference — paste into call chat as each phase comes up
For Sudhir to review after the session. Ordered to match session_script_live.md's phases.

## Phase 1 — Architecture & Security Controls
- **RAG (Retrieval-Augmented Generation):** generating an answer by first retrieving relevant source text, then having the LLM answer grounded in that retrieved text, instead of answering from memory alone.
- **Hybrid retrieval:** combining vector/embedding search with keyword search (BM25) to find relevant passages, catches matches either method alone would miss.
- **BM25:** a classic keyword-ranking algorithm that scores documents by term relevance, used alongside vector search in this app.
- **Reciprocal Rank Fusion (RRF):** a method for merging two separately ranked result lists (vector + BM25) into one combined ranking.
- **Reranking:** a second pass that re-scores the initially retrieved candidates with a more precise model, improving final ordering before generation.

## Phase 2 — Prompt Injection & RAG-Specific Attacks
- **Prompt injection:** an attacker's input trying to override, bypass, or manipulate a model's instructions.
- **Retrieval poisoning:** planting malicious or false content into the data a RAG system retrieves from, so the model treats it as fact.
- **Exfiltration (in this context):** getting a system to reveal internal data (raw chunks, config, instructions) it wasn't meant to expose directly.

## Phase 3 — Citation Integrity & Groundedness
- **Groundedness:** how well an answer's claims are actually supported by the retrieved source text, versus invented.
- **Hallucination:** a model stating something not actually present in or supported by its sources.
- **Citation validation:** checking that citation markers (like [1], [2]) in a generated answer actually correspond to real retrieved sources, not fabricated references.

## Phase 4 — Guardrails & Secure Integration
- **Guardrails:** controls placed around a model's input/output to prevent unsafe or unintended behavior.
- **Input/output validation:** checking and constraining what goes into and comes out of a system for safety and correctness.
- **CORS (Cross-Origin Resource Sharing):** a browser security policy controlling which websites are allowed to call an API from client-side code.
- **Rate limiting:** restricting how many requests a client can make in a given time window, to prevent abuse.

## Phase 5 — Evaluation, Logging, Monitoring
- **Trace schema:** a standard structured record of what happened during a request (inputs, retrieved sources, model used, outcome), used for debugging and auditing later.
- **Index versioning:** tracking which version of a search index/corpus answered a given query, so historical answers can be traced back to the data that produced them.
- **Observability:** the broader practice of being able to understand a system's internal state from its external outputs, logs, and metrics.

## Phase 6 — Remediation
- **Code-level control:** a safeguard enforced in software logic, true regardless of what the model decides to do.
- **Prompt-level control:** an instruction given to the model, relies on the model choosing to comply, not enforced mechanically.
- **Regression test:** an automated check that re-verifies a fix keeps working as the system changes over time.
