# Code Audit: NCD Guideline Tutor (sudhirshivaram/ncd-guideline-tutor)
Source read directly from the public Hugging Face repo, commit `21e913b`, Oct 10 2026.
Stack: FastAPI + Gradio, Chroma (vector) + BM25 hybrid retrieval with RRF fusion + MiniLM rerank, 3 static WHO PDFs, BYO API key (OpenAI/Gemini/Anthropic) sent per-request via header, never stored server-side.

## What's genuinely good (tell him this directly, it's true)
- System prompt (`backend/app/rag/generate.py`) is tight and well-written: grounds answers in retrieved sources only, explicitly forbids inventing thresholds/doses, explicitly forbids strengthening hedged language ("suggests" -> "recommends"), requires inline citation. This is above-average prompt engineering for a learning project.
- API key handling is correct: passed via `x-api-key` header per request, never persisted server-side, matches what he told us.
- Output capped at 1200 tokens, matches what he told us.
- Hybrid retrieval (vector + BM25 + RRF) with reranking is a legitimately solid architecture choice, not just a toy wrapper around an LLM call.

## Finding 1 (confirmed at code level): no server-side citation validation
`generate.py: format_context()` numbers retrieved chunks `[1]..[N]` purely for the prompt text. The model is instructed to "cite them inline as [1], [2]," but nothing anywhere in `pipeline.py` or `chat.py` checks that a citation number appearing in the model's free-text answer is actually `<= N`. This is the exact root cause of last night's `[5]`-when-only-3-chunks-retrieved finding. It isn't a fluke, it's a structural gap.
**Fix location:** after `stream_llm` completes in `pipeline.py`, parse citation markers (`\[(\d+)\]`) from the accumulated answer text and compare against `len(contexts)`. Strip or flag anything out of range before it reaches the UI.

## Finding 2 (new, found by reading the code, not live-testable on demand): raw exceptions leak to the client
`chat.py`: `yield f"data: {json.dumps({'type': 'error', 'message': str(exc)})}\n\n"`. Any unhandled exception during retrieval or generation sends `str(exc)` straight to the browser. Depending on the exception, that can include internal file paths, SDK error internals, or library version strings. Standard fix: log the real exception server-side, send a generic message to the client. Hard to trigger reliably live in a 60-minute call, so this is a "found it by reading the code" talking point, which is itself a skill worth demonstrating Tuesday.

## Finding 3 (confirmed, matches his own self-assessment): no CORS policy, no rate limiting
`main.py` has no `CORSMiddleware`, and nothing in `chat.py` limits request rate. Worth noting why this specific combination matters here: the `/api/chat` endpoint accepts any `x-api-key` value and proxies it directly to the chosen provider. No CORS restriction means any third-party webpage could embed a call to this public endpoint. Combined with it being a BYO-key endpoint, that's a real (if not currently exploited) pattern worth naming in an interview: an open CORS policy on a key-forwarding endpoint is a potential key-harvesting vector if a user is ever tricked into entering a key somewhere that silently relays it here.

## Finding 4 (confirmed, matches his list): no input sanitization or prompt-injection-specific filtering
Nothing between the user's raw message and the model beyond the system prompt's own instructions, which are requests, not enforcement. This is exactly what tonight's Phase 2 tests (disclaimer echo, translate-your-instructions, rule laundering) are built to demonstrate live.

## Architectural note that changes tonight's poisoning test (good news, not a gap)
`ingest.py` / `indexing.py` only ever read from a fixed `DOCUMENT_CATALOG` (3 named WHO PDFs in `data/`). There is no live document-upload endpoint anywhere in the API routes. The corpus is static, baked in at build time (`app.py`: `if not index_is_ready(): build_index()`). This confirms the retrieval-poisoning demo **must** be done on a local clone, not the live Hugging Face deployment, exactly as planned, and it also means the live production app currently has no reachable live-poisoning attack surface. Worth telling him this is one thing that's already safe, by architecture rather than by design intent, and worth knowing the difference between those two in an interview answer.

## Practical note for tonight: avoid repeating last night's failed live test
The UI (`gradio_app.py`) exposes three swappable providers with exact model names:
- OpenAI: `gpt-4o-mini` (default), `gpt-4o`, `gpt-4.1-mini`
- Google Gemini: `gemini-3.5-flash-lite` (default), `gemini-3.1-flash-lite`
- Anthropic: `claude-haiku-4-5` (default), `claude-sonnet-4-5`, `claude-sonnet-5`

If his Anthropic key is still out of credits, switch the provider dropdown to Gemini before the call starts. Google's free tier is typically easy to get a working key for same-day, and it avoids losing live-testing time twice in a row.
