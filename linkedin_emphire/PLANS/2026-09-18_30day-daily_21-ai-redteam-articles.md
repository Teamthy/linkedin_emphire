# 30 Days Daily Posting + 21 AI Red Teaming Articles Plan
Start: Fri Sep 18, 2026
Daily posting (every day, 30 days straight) + 3 AI Red Teaming articles/week for 7 weeks (21 total)
Built for zero burnout, zero essay fatigue, and maximum payoff by Day 40 (job hunt launch)

═══════════════════════════════════════════════════════
FIRST, THE REAL TALK
═══════════════════════════════════════════════════════
I'm not going to tell you "that's too much, don't do it." You want to post daily for 30 days and write 21 articles on AI red teaming — that's ambitious, but it's exactly the kind of focused sprint that turns a random LinkedIn account into a known person in a niche.

But here's the rule that keeps you from burning out on day 8 (which is what happens to 95% of people who declare daily posting):

NOT EVERY POST HAS TO BE A BANGER.

If you try to write a 1000-word perfect Bolaji-post every day, you will quit in a week. Instead:

## POST CATEGORIES (so you don't grind essays daily)
Daily posts fall into two buckets. Mix them across the week.

### A. ANCHOR POSTS (2/week, ~900-1200 chars, high effort)
These are the pillar posts we've been writing — Bolaji-short structure, screenshot line, PS question, the format you already know performs.
- Wednesdays 12pm WAT: SE / technical craft
- Fridays 12pm WAT: AI / AI Red Teaming (these tie into your articles)

### B. MICRO POSTS (5/week, ~200-500 chars, LOW effort)
These are short, casual, and can be written in 5 minutes. They exist to keep momentum, show personality, and stay in the algorithm without burning you out. Formats:
1. Quick question posts ("What's one bug you found this week that made you laugh out loud?")
2. One-line hot takes ("Prompt injection isn't an AI problem. It's an input validation problem that nobody took seriously.")
3. "Something I learned today" (1 thing from going through Tarique's guide, 1 thing from a build, 1 quote you liked)
4. Code snippet posts (screenshot of a bug, 1 line explaining it, question)
5. Reply roundups ("Here are 3 things people said in my comments yesterday that changed how I think about X")
6. Personal check-ins ("Day 4 of posting daily. Here's what surprised me so far.")
7. Faith short reflections (Sunday micro post, ~200 chars)

Micro posts are NOT throwaway content — they build authenticity. People follow humans, not essays. But they take 5 minutes, not 90.

### CADENCE PER WEEK (7 posts)
- Wed 12pm: Anchor SE post (1000 chars)
- Fri 12pm: Anchor AI / Red Teaming post (1000 chars, ties to that week's article)
- Sat 10am: Micro (question / hot take)
- Sun 10am: Micro (personal / faith / weekly recap)
- Mon 10am: Micro ("something I learned today" from reading the red teaming guide)
- Tue 10am: Micro (code snippet / bug / reply roundup)
- Thu 10am: Micro (takeaway from that week's article)

That's 2 high-effort posts + 5 low-effort posts per week = sustainable daily posting without essay fatigue.

If you miss a day, YOU MISSED A DAY. Post the next day. Don't let one missed day turn into a 3-week silence (that's what happened Aug 21 → this week). That is the only rule.

═══════════════════════════════════════════════════════
21 AI RED TEAMING ARTICLES (3/week for 7 weeks)
═══════════════════════════════════════════════════════
## WHY THIS IS YOUR MOAT
By Day 40, you won't be "a software engineer in Lagos posting about AI." You'll be the software engineer in Lagos who wrote a 21-part field guide to AI red teaming for builders, grounded in Tarique's guide and real testing on his own AI integrations. That is not a resume bullet. That is a body of work recruiters cold-message you about.

## STRUCTURE (SO YOU DON'T INVENT TOPICS OUT OF THIN AIR)
Each article maps DIRECTLY to Tarique's AI-Red-Teaming-Guide (which you've forked) and builds up your CV appendix contribution over 7 weeks. You don't have to invent a topic — you work through the guide section by section, test each thing against your own AI integrations (or a simple lab app you build as you go), and write up what you learned.

3 articles per week = ~800-1200 words each. Publish on LinkedIn as articles AND as shorter LinkedIn posts (the Friday anchor post is the teaser for that week's article). By article 21, you have:
- A complete beginner-friendly AI red teaming field guide for working engineers
- Material you can PR to Tarique's repo (remember the fork strategy)
- A portfolio piece recruiters can't ignore
- Real, hands-on red teaming skill — not just course knowledge

### WEEK 1 (Sep 18–24) — Foundations
1. **Why every AI integration engineer needs to know red teaming (even if you're not a "security person")** → published as a LinkedIn article; Friday anchor post teases it
2. **The 5 boring failure modes nobody warns you about before you ship AI** (PII leaks, hallucinated actions, prompt injection, silent bias, over-trust)
3. **Red teaming your first AI feature: a 30-minute starter test anyone can run** (starter checklist, no fancy tools required)

### WEEK 2 (Sep 25–Oct 1) — Prompt Injection
4. **Prompt injection isn't a "prompt" problem — it's an input validation problem**
5. **I tried prompt-injecting my own AI customer support bot. Here are 6 ways I got in in 10 minutes.**
6. **Defending against prompt injection: 4 cheap controls that actually work before you buy fancy tooling**

### WEEK 3 (Oct 2–8) — Agent & MCP Security
7. **Why AI agents are a bigger attack surface than chatbots**
8. **MCP servers are coming. Nobody is talking about securing them.** (ties back to MCP pinning from Tarique's PR checklist)
9. **Tool-call injection: when your AI agent does something it shouldn't because a prompt told it to**

### WEEK 4 (Oct 9–15) — Bias & Fairness
10. **I ran my hiring-assist AI against non-Western names. Here's what happened.** (ties back to the hiring-bias point from your Endrit post — runs a real test on a real or dummy model)
11. **Bias testing isn't an ethics exercise. It's a production liability.**
12. **3 cheap bias tests you can run on your AI model in an afternoon**

### WEEK 5 (Oct 16–22) — Multimodal / CV Red Teaming (YOUR specialization)
13. **Red teaming computer vision models: what text-model security guides miss**
14. **Adversarial patches in the real world: why a sticker on a stop sign is still a problem**
15. **Deepfake detection evasion: 3 things I tested that worked (and 2 that didn't)**

### WEEK 6 (Oct 23–29) — Operationalizing Red Teaming
16. **The calibrated trust problem: why users either over-trust or ignore your AI** (ties back to Gustavo's Tesla point)
17. **Logging, monitoring, and why "we'll catch it in testing" never works**
18. **Building a red teaming checklist for your team before you ship any AI feature** (this is the saveable/framework post that gets reposted)

### WEEK 7 (Oct 30–Nov 5) — Builder Mindset + Wrap-up
19. **AI red teaming isn't just for security teams. It's software engineering.** (core thesis, ties to SE primary identity)
20. **What 21 days of red-teaming my own AI code taught me about shipping real things**
21. **The builder's AI security starter pack: tools, checklists, and resources I actually use** (publish this as a free resource; this is the post that gets shared widely and gets inbound)

## ARTICLE PRODUCTION CADENCE (doable, not a dissertation):
- Mon: Pick the week's topics from the list above
- Tue: Outline + run any test/lab for article 1 (30 min)
- Wed: Write article 1 (60-90 min); tease on Friday anchor post
- Thu: Run test/lab for article 2
- Fri: Write article 2; publish anchor post
- Sat: Write article 3 (lighter, listicle-style)
- Sun: Edit + publish all 3, schedule teaser posts for the next week

Articles don't need to be perfect. They need to be honest, specific, and grounded in things you actually tried. Real tests with real results beat theoretical essays.

═══════════════════════════════════════════════════════
30-DAY CONTENT CALENDAR (FIRST 10 DAYS, TO GET YOU STARTED)
═══════════════════════════════════════════════════════

### Day 1 — Fri Sep 18 (today)
- 12pm: ANCHOR friday-cutoff ("No code merges after 4pm Friday") — already verified
- Engagement 90 min
- No article yet — use today to set up

### Day 2 — Sat Sep 19
- 10am MICRO: Question post — "What's one thing you wish someone had told you before you shipped your first AI feature? I'm compiling notes for the engineers I teach." (doubles as research for article 1)

### Day 3 — Sun Sep 20
- 10am MICRO: Personal — short reflection on "Day 3 of posting daily. I thought I'd be tired. I'm actually having fun." Or a short faith reflection (your call).

### Day 4 — Mon Sep 21
- 10am MICRO: Hot take — "Prompt injection isn't an AI problem. It's an input validation problem that developers forgot how to do."

### Day 5 — Tue Sep 22
- 10am MICRO: Something I learned — first takeaway from going through Tarique's guide (e.g., "The first thing I learned reading through the AI Red Teaming Guide: I've been shipping AI features without an eval harness. Oops.")

### Day 6 — Wed Sep 23
- 12pm ANCHOR (SE): Proof-of-work post about a real bug you shipped or fixed while building an AI integration. ~1000 chars.
- Begin writing Article 1 (why AI integrators need red teaming)

### Day 7 — Thu Sep 24
- 10am MICRO: Code snippet — screenshot of a prompt injection you ran on your own code, 1 line explaining what happened.

### Day 8 — Fri Sep 25
- 12pm ANCHOR (AI/Red Team): Teaser for article 1 — "I spent this week red-teaming my own AI customer support bot. Here's what I learned about how broken 'ship fast' culture is for AI."
- Publish Article 1.

### Day 9 — Sat Sep 26
- 10am MICRO: Question post — "What's the dumbest way you've seen an AI feature fail in production? I'll start: ..."
- Publish Article 2.

### Day 10 — Sun Sep 27
- 10am MICRO: Weekly recap / faith post + publish Article 3.

Days 11–30 follow the same pattern — anchors on Wed/Fri, micros the rest of the week, 3 articles per week.

═══════════════════════════════════════════════════════
JOB HUNT ALIGNMENT (why this works for your Oct 28 goal)
═══════════════════════════════════════════════════════
By Day 40 (Oct 28), you will have:
- 40 public posts showing your voice, judgment, and expertise
- 9 published AI Red Teaming articles (with 12 more rolling out)
- A public fork of Tarique's guide with real contributions started (the PR work)
- A proven, demonstrable specialization in AI red teaming + AI integration + CV — the exact mix that AI security teams are hiring for right now
- 100+ new warm connections from people engaging with your series

That is not "someone applying for a job." That is "someone who is visibly building expertise in a hot niche, publicly, every day." Recruiters reach out to that person before they even turn on "open to work."

Activate job hunt moves (recruiter-only open-to-work, warm outbound DMs) starting Day 35 (Oct 23) — by then your profile will speak for itself.

═══════════════════════════════════════════════════════
NON-NEGOTIABLES TO AVOID BURNOUT
═══════════════════════════════════════════════════════
1. Micro posts are allowed to be SHORT. 200 chars is fine. You don't have to be profound every day.
2. If you miss a day, don't quit. One missed day = one missed day. Post the next day like nothing happened. The only real failure is letting a missed day turn into a 3-week gap.
3. Don't write after 9pm. Prep posts in the morning or during lunch.
4. One post per day max. Don't flood the feed.
5. If an article isn't good enough, ship it anyway. You're not writing a PhD thesis — you're writing for working engineers who need practical stuff. Imperfect and shipped > perfect and in drafts forever.
6. Keep writing like you talk. The second your posts start sounding like an AI essay, people will unfollow. Your voice is the moat.
