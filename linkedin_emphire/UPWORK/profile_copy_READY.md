# UPWORK PROFILE — READY TO PASTE (SEO-OPTIMIZED, v2)
Source plan: `../PLANS/2026-10-10_upwork-rebrand-empire.md`
Live profile checked 2026-10-10: still "Shopify & TikTok Shop Strategist VA," $20/hr, 33% complete, 0 completed jobs. Nothing below has been pasted in yet.

Profile: https://www.upwork.com/freelancers/~01a65712b8b0954fd2
Sibling: https://www.linkedin.com/in/olusanya-timothy

---

## SEO & RANKING NOTES (read before pasting — this is why v2 differs from v1)
Checked against Upwork's own help docs and 2026 ranking data before rewriting:
- **Skills limit is 20, not 15.** Confirmed directly on `support.upwork.com`: "You can add up to 20 skills to your profile." v1 only used 13 — that's wasted search-match surface. Fixed below.
- **Title cap is 70 characters, confirmed on upwork.com itself** (`upwork.com/resources/freelancer-headlines`). Best headlines combine role + specialty/tool + a result or credential, using 60-70 of the 70 characters. v1 was fine at 62 chars but didn't include "agent," a fast-growing search term for your exact service (tool-call/agent abuse testing). Fixed below.
- **The algorithm and clients both weight the first ~150-200 characters of the overview most heavily** (this appears in preview cards and is what search indexes hardest). v1 opened with a hook ("AI products don't fail quietly") before any keyword appeared. v2 front-loads the keywords in sentence one, then lands the hook in sentence two — same voice, reordered for search.
- **Job Success Score (25-30% estimated weight) is the single biggest ranking factor** — but it doesn't exist until you complete contracts. You cannot optimize it today. What you CAN control today: title, overview, skills, completeness, response rate, and the "Available Now" toggle. This file focuses only on what's controllable before job #1.
- **Specialized Profiles — confirmed removed.** Upwork discontinued Specialized Profiles on May 28, 2026. There is no option to run a second, separate profile for the AI security positioning while keeping Shopify/TikTok untouched — this account has exactly one profile, and the full rebrand below is the only path. (If you ever had specialized-profile content pre-removal, Upwork states it did not auto-transfer and isn't recoverable — not relevant here since this account never had one, but worth knowing.)
- **Generic or AI-generated-sounding copy correlates with lower ranking and lower click-through in 2026** — clients and the algorithm both increasingly filter for it. Everything below was written against `voice_dna.txt` / `banned_words.txt` for this reason, not just brand consistency.

---

## 1. TITLE (70-char field — this is a search field, not a tagline)
**Primary — recommended (63 chars, adds "agent" keyword):**
```
AI Red Teaming | Prompt Injection, RAG & Agent Security Testing
```
**Alternate A — v1, still solid (62 chars):**
```
AI Red Teaming | LLM & RAG Security Testing | Prompt Injection
```
**Alternate B — if you want "pentest" in there for broader search match (60 chars):**
```
AI Red Teaming | LLM, RAG & Agent Security Testing | Pentest
```
Upwork lets you change the title any time at no cost — if you're unsure, start with the Primary, check profile impressions/views after ~2 weeks (Upwork stats tab), and switch to an alternate if impressions are flat.

## 2. RATE
```
$65/hr
```
Raise to $95-150/hr after your 5th review. Not before. See `analytics_tracker.txt`.

## 3. OVERVIEW (paste as-is — keywords front-loaded in sentence one per the SEO note above)
```
AI red teaming for teams shipping LLM features. I test chatbots, RAG pipelines, and tool-calling agents for prompt injection, RAG poisoning, and agent abuse, then hand you a findings report your engineers can act on the same day.

AI products don't fail quietly. They fail publicly. I ran six injection attempts against my own production chatbot. Four worked. Every fix became a permanent regression test. That's the whole service: find the holes before the screenshots do.

What you get:
- Prompt injection and jailbreak testing on your AI feature, manual plus garak and promptfoo coverage
- RAG poisoning: does your system obey instructions planted inside documents it retrieves
- Agent checks: forged tool calls, tampered arguments, confirmation bypass, runaway loops and cost blowouts
- A findings report in four-part format: exact repro, which layer failed, the practical fix, how to verify it holds
- Regression suite: your new tests run on every future model or prompt change, so the hole cannot come back

Who this is for: startups shipping AI without a security loop. Agencies that need an independent pre-launch check. Anyone building chatbots, RAG systems, or AI agents for health, finance, or other regulated workflows.

Proof: I write Breaking AI, a 21-part public field guide on shipping AI that survives real users. My lab repos and findings samples are in the portfolio below.

Start with the $150 Quick Scan for a low-risk first look, or send a proposal with your stack and I'll scope the full Red Team Review. Either way: test it before they do.
```
**Voice + SEO check:** "AI red teaming," "LLM," "RAG" (x2), "prompt injection," "agent abuse" all land in the first 230 characters. No banned words from `banned_words.txt`. Ends on an action, not a question (matches `voice_dna.txt` rule 3 — Upwork CTA is transactional, not relational).

## 4. SKILLS — up to 20 (confirmed via support.upwork.com, not 15)
Paste in this order (Upwork ranks by the order you set, and each tag is a separate search-match surface):
```
1. AI Security
2. Prompt Injection
3. LLM
4. AI Red Teaming
5. RAG (Retrieval Augmented Generation)
6. AI Agents
7. Penetration Testing
8. Cybersecurity
9. Security Testing
10. Vulnerability Assessment
11. API Security
12. Machine Learning
13. Python
14. OWASP
15. Chatbot Development
16. Artificial Intelligence
17. FastAPI
18. Risk Assessment
19. AI Consulting
20. Go (Golang)
```
Note: Upwork only accepts tags from its own autocomplete list — when typing each term, pick the closest official match it suggests (e.g. it may offer "Large Language Model (LLM)" or "Retrieval-Augmented Generation (RAG)" as the exact tag name rather than the short form). If a term from this list isn't offered at all, skip it rather than forcing a near-miss tag.

Current live skills to remove entirely: Shopify, WordPress, Website Redesign, Web Development, Sales Funnel, Graphic Design, Shopify Templates, Shopify SEO, Shopify Theme, Payment Gateway Integration, TikTok, TikTok Marketing, Virtual Assistance.

## 5. CATEGORIES
- **Primary:** AI Services
- **Secondary:** Development & IT
- **Subcategories:** Data Science & Machine Learning, Cybersecurity & Data Protection, AI Application Development

## 6. EMPLOYMENT HISTORY (new in v2 — profile-completeness + recency signal)
2026 ranking data flags "work history gaps or old-jobs-only" as a top mistake; top-ranked profiles show recent, relevant history. Add these two entries under Upwork's Employment History section (separate from on-platform Work History, which is currently empty — that's fine, everyone starts at zero there):
```
Software Engineer – AI Integration & Red Teaming
Teamart.inc · Lagos, Nigeria · July 2025 – Present
Build and ship AI features for client products: LLM chatbots, retrieval pipelines, and tool-calling workflows. Run pre-launch red teaming on AI features (prompt injection, unauthorized actions, policy bypass) and deliver prioritized findings with fix recommendations.

Senior Developer
YKAY ConsultingHub · Lagos, Nigeria · Nov 2024 – June 2025
Led backend development in Go and Node.js across client-facing products, owning API design through deployment. Designed REST APIs and multi-role authentication used by client systems with distinct permission levels.
```

## 7. EDUCATION (new in v2 — completeness)
```
BSc Computer Science — National Open University of Nigeria — Expected April 2028
```

## 8. PROFILE PHOTO
Match the LinkedIn headshot exactly (same brand test: a buyer who finds both profiles should recognize the same person instantly). If LinkedIn still has the illustrated avatar per `STRATEGY/2026-10-02_90-day-10k-client-positioning.md` item 6, fix that one first — both profiles need the real photo, not just this one. A clear, professional headshot is one of the highest-cited "common mistake" fixes in every 2026 Upwork guide reviewed.

## 9. PORTFOLIO — add 4, reorder above the old ones (keep 2 e-comm items as platform-history proof)
1. **Breaking AI, Article 1** — paste the LinkedIn Pulse link. Title: "Why Every Team Shipping AI Needs Someone Whose Job Is to Break It"
2. **redteam-lab repo** — findings-folder screenshot: "6 attempts, 4 breaks"
3. **Sample findings report** — sanitized example using the four-part template, built from your own bot's test
4. **The 30-minute starter test checklist card** — reuse `../ARTICLES/2026-10-06_article-1_why-engineers-need-red-teaming/cards/art1_card2_checklist_1080x1350.png`

Keep the 2 strongest existing Shopify/TikTok items below the new 4. Drop the rest. Guides consistently recommend 6+ portfolio items with role + outcome stated per item — the 4 new + 2 kept hits that target.

## 10. PROFESSIONAL POLISH CHECKLIST (new in v2 — controllable ranking factors beyond copy text)
Do all of these in the same sitting as the text paste — a half-updated profile (new title, old photo, empty employment history) reads worse than the current honest mismatch:
- [ ] ID verification badge showing (if not already — check Settings > My Info)
- [ ] "Available Now" toggle turned on (official Upwork feature; low-effort signal, amplifies a strong profile)
- [ ] Record a 30-60 second video intro if your account has that field — state the one-line thesis ("I break AI before your users do") on camera, not just text
- [ ] Take any relevant Upwork skill tests you can pass comfortably (Python, if offered) for a "Top 10%/20%" badge — a quality signal 2026 guides cite directly
- [ ] Set a realistic response-time habit: reply to invites/messages within a few hours, ideally same day — response rate is an explicit ranking input, not just courtesy

## 11. COMPLETION TARGET
Title + rate + overview + skills (20) + categories + employment history + education + 6 portfolio items + 3 catalog listings (see `project_catalog.md`) + the polish checklist above should take the profile from 33% to 100% and address every documented 2026 ranking factor that's controllable pre-JSS. Finish it in one sitting.
