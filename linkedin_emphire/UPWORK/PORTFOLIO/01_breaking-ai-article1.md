# Portfolio Item 1 — Breaking AI, Article 1

**Project title:**
```
Breaking AI, Article 1: Why Every Team Shipping AI Needs Someone Whose Job Is to Break It
```
**Your role:** Author / AI Red Teamer
**URL:** [paste your LinkedIn Pulse link for Article 1 here]
**Skills/tags:** AI Security, Prompt Injection, Large Language Model, Technical Writing

**Description:**
```
Article 1 of Breaking AI, a 21-part public field guide on shipping AI that survives real users. I ran six prompt injection attempts against my own production chatbot. Four worked: a leaked system prompt, a fabricated refund promise triggered by a single word, and a content-policy bypass. This piece breaks down why that happens and why the people who build AI features are the ones best positioned to break them first.
```
**Image (landscape, 1584x990):** `ARTICLES/2026-10-06_article-1_why-engineers-need-red-teaming/hero_cover_C_photoreal_1584x990.png`
**Image (square, 1080x1080):** `ARTICLES/2026-10-06_article-1_why-engineers-need-red-teaming/hero_cover_D_square_1080x1080.png`

## The Full Story — What, Why, How

**What was done:** Published Article 1 of a 21-part public series, Breaking AI: A Builder's Field Guide to Shipping AI That Survives Users. The article documents six prompt-injection attempts run against a real, self-built production customer-support chatbot. Four of the six worked: a leaked system prompt, a fake refund promise triggered by the word "pineapple," and a content-policy bypass via fictional framing (a "pretend you're writing a movie script" prompt). The article also closes with a free, runnable 30-minute checklist (that checklist became its own portfolio item, #4 on this list).

**Why it was done:** Two reasons stacked on top of each other. First, credibility: anyone can claim to do AI red teaming, but client findings are confidential, so there was nothing to show a buyer. Testing a system fully owned and controlled meant the whole process, including the failures, could be published without an NDA conflict. Second, positioning: the series is deliberately framed as written by a builder, not a security theorist. Most AI-risk writing comes from people who have never shipped a tool call or debugged a RAG failure at 2am. Opening with "I built this and still broke it myself" draws a hard line between that kind of writing and someone who actually ships AI products for a living.

**How it was done:**
1. Picked a target with full ownership and authority to test and publish, a self-built production chatbot, to avoid any confidentiality or ethics problem.
2. Designed six adversarial prompts covering core attack categories: instruction override, system-prompt extraction, authority/trigger-word exploitation, and fictional-framing policy bypass.
3. Ran each prompt once, recorded exactly what happened, no cherry-picking which failures to report.
4. Grouped the results into reusable patterns ("the demo is not the product," "the prompt is not a wall," "the boring failures are the ones that cost you," "the builder is the worst person to test alone") so the piece reads as a transferable engineering lesson, not a one-off bug list.
5. Closed with an immediate, low-effort action: a 10-step checklist readers can run themselves in 30 minutes, lowering the barrier to trying it before anyone is asked to pay for anything.
