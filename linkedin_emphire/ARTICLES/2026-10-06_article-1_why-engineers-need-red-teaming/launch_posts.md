# Article 1 launch sequence — REVISED schedule
Updated: Tuesday, Oct 6, 2026 (article moved from Tue to Fri per decision)
**Article 1 publishes: Friday, October 9, 2026, 10:00 AM WAT**
New shape: 3-day arc. Wednesday confession, Thursday checklist, Friday the article. Each post stands alone, so a bad day does not break the chain, and the article lands with two days of priming.

---

## WEDNESDAY, OCT 7 — 10:00 AM WAT — CONFESSION POST
**Attach:** cards/art1_card1_testlog_1080x1350.png

Last week I tried to break my own chatbot.

6 attempts. 4 of them worked.

One leaked my system prompt. One made the bot promise a full refund to anyone who typed "pineapple."

I built that thing. I wrote every prompt in it. I still found four ways in without trying hard.

I wrote the whole thing up: what broke, why builders are the worst people to test alone, and the 30-minute test you can run on your own AI feature before lunch.

Article 1 of Breaking AI lands Friday morning.

**Seed comment (60 seconds after posting):**
The part that stung was how easy it was. No clever payloads. One of the four was a single word.

I am not publishing this to look humble. I am publishing it because every AI feature I test has the same kind of hole, and the only teams finding them are the ones who went looking.

Friday I will show exactly what I ran on my own bot, prompt by prompt.

**Then: Zara interview after this post.**

---

## THURSDAY, OCT 8 — 10:00 AM WAT — SAVE-BAIT POST
**Attach:** cards/art1_card2_checklist_1080x1350.png

I turned the 30-minute red team test into one card.

Ten things to try on your own AI feature. One input per line. It works on chatbots, RAG pipelines, and even tool-calling agents.

Most teams I talk to fail at item 1.

Steal it. Run it before you ship anything this week.

Full article with every test and result lands tomorrow morning.

**Seed comment:**
Item 1 works more often than it should. "Ignore all previous instructions" is the lock that is not really locked.

If you run the list and something breaks, comment what it was. No shame in this series. Every AI engineer has shipped a hole, the ones who admit it fix it fastest.

---

## FRIDAY, OCT 9 — 10:00 AM WAT — ARTICLE 1 PUBLISHES
Publish from `article_LINKEDIN_READY.txt`. Title and subtitle go in their own fields. Hero image at [IMAGE 1], checklist card at [IMAGE 2].

**Feed post announcing it (attach hero_generated.png or cards/art1_card3_headline_1080x1350.png):**

Article 1 of Breaking AI is live.

Why every team shipping AI needs someone whose job is to break it.

Most AI security failures are not security problems. They are engineering problems. And the team that built the system is the last team on earth that will find them.

I broke my own chatbot on purpose last week. Six attempts, four worked. The article covers what happened, the four things nobody warns you about before you ship AI, and the 30-minute test you can run before lunch.

Link in the first comment.

**First comment:** [paste the article link]

**Seed comment (on the article, 60 seconds after publishing):**
One thing that did not fit: the first injection that worked on my bot took eleven words. No clever encoding. Eleven words I typed out of frustration.

That is the part nobody believes until they try it. The bar for breaking an AI feature is lower than the bar for building one.

If you run the 30-minute test this week, comment what broke.

**90-minute window, 10:00 to 11:30 AM:** reply to every comment within 5 minutes, like every commenter, no edits during the window. Paste anything tricky here and I will draft the reply.

---

## WHAT SHIFTED AND WHY IT DOES NOT HURT
- Article 2 (five boring failure modes) moves from Fri Oct 9 to Tue Oct 13. Series cadence continues Tue/Fri from there. Nothing is lost, the series just starts two days later than planned.
- The Wednesday and Thursday posts are the same assets that were already built (test log card, checklist card), so no new production work.
- Two days of priming before the article means launch-day traffic arrives warm instead of cold. This is the better version.

## IF A DAY SLIPS
Post the next one the following morning. Do not double-post to catch up. The rule stands: miss a day, post the next day, no guilt.


## VISUAL QA (Fri ~6:55 AM) — Max's finals
FEED CARD: ship. One micro-fix: drop the dangling em-dash after "Broke It in an Hour." (move pivot to the cyan line or delete). Whiteboard in shot = perfect field-guide texture. Approved.
COVER: 3 fixes before use: (1) REMOVE the glowing AI-brain hologram + circuit lines - banned by own brand rules and it's the generic-AI look we position against; (2) chip swap: series tag top-left, name small bottom-left not boxed top-left; (3) stock faces: replace with his cutout OR go clean - fallback already rendered: launch_cover_twist_1920x1200.png (system-perfect, zero edit needed).
VERDICT: if no time to edit cover, publish with PIL fallback cover + Max's feed card. GO at 10:00 regardless.
