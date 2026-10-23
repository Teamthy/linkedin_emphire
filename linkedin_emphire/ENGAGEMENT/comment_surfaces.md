# COMMENT SURFACES — TRACKED LIST

Source of picks for the daily comment round (empire_pipeline Stage 2,
Step 2.1). Built from the owner's network read 2026-10-23 (684
followers, 468 following). This is a menu, not a quota: pick 5-8 fresh
posts across tiers per day.

## Protocol (per 2026-10-23 analytics + feed data)
1. 5-8 comment actions per day, spaced across the day, never a burst.
   The 10-23 burst (14-16 actions in about an hour) is the throttling
   risk this cap exists to remove.
2. A comment action = a comment OR a follow-up reply. Follow-up replies
   are first-class: threads compound (Paolo Perrone thread: main + 2
   replies; the reply alone hit 3,722 impressions).
3. Fresh posts only (same day or yesterday). Stale posts do not push.
4. Tier 1 first (reach), tier 2 for home-turf authority, tier 3 as
   spice.
5. One thesis (the check frame) across all tiers, different surface
   each time. No two comments in the same 24h may reuse the same
   closing line.
6. If an author replies (supportive or hostile), the reply is a
   scheduled action the same day. Hostile reply protocol: do not
   defend, serve the verifiable claim, invite the re-run (reference:
   the 10-23 Filip R. exchange on the Endrit banks thread).

## Tier 1 — big reach (your comment rides into the author's audience)
Chip Huyen, Ethan Mollick, Sebastian Raschka, Eugene Yan, Hamel Husain,
Simon Willison, Jerry Liu (LlamaIndex), Amjad Masad (Replit),
Paolo Perrone (60,500-imp thread origin; keep watching)

## Tier 2 — home turf (LLM security / red teaming; this audience hires)
Kai Greshake, Leon Derczynski (garak, NVIDIA), Battista Biggio
(Cagliari), Dustin Farley (Lakera), Pete Bryan (Microsoft AI Red
Team), Clint Gibler (OpenAI), Ian W. (Promptfoo / OpenAI), Joseph
Thacker, Rebecca Huteson, Alex Combessie (Giskard), Keren Katz
(Zenity, OWASP Agentic Top 10), Hyrum Anderson (Abundant Security),
Rock Lambros (Zenity), Tarique Smith (Zero Day Agent)

## Tier 3 — builder / adjacent layer + active thread partners
Ado Kukic (Claude Code community), Jason Liu (OpenAI DevEx),
Ife Abimbola-Olulesi (Proof), Shehbaz Pathan (RAG / agent memory),
Alex Banks, Sam Illingworth (Slow AI), al neitsch, Endrit Restelica,
Helen Oakley (Zenity), Robinson Miranda, Tanay Kothari, Salman
Lakhani, Chris H., Madhan Vadlamudi, Ned Lowe, Sudarshan Thorat

## Groups (free distribution; separate from the comment round)
- Group 6773411: the 90-day top performer is a post in this group
  (1,053 imp, VERIFIED_POSTS row 15). Sunday planning decision:
  cross-post the week's strongest standalone, or publish a
  group-native post with a group-specific question close (the
  "Question for this group" pattern worked).

## Refresh rules
- On any network or feed paste: add new qualifying surfaces (reach,
  home turf, or active thread partner) with their tier.
- Demote a surface after 3 consecutive comments under ~20 impressions
  or zero replies; log the demotion and why in
  LINKEDIN/performance_tracker.md.
- Follow-back audit each refresh: any thread partner or tier 1-2
  author not followed back gets a follow (10-23 finding: Robinson
  Miranda was a thread partner and not followed back).
- Rebuild the whole list from the network read every 90 days,
  aligned with the 90-day tracker snapshot.

Last refreshed: 2026-10-23
