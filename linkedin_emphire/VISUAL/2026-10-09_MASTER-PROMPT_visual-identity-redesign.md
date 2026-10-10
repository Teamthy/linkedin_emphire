# MASTER PROMPT: Visual Identity Redesign, "Breaking AI"
For: Max (or any designer / AI design tool). One prompt, everything included. Do not ask follow-up questions; every answer is here.

---

## WHO THIS IS FOR

Olusanya Timothy. Software engineer in Lagos. Positioning: **AI red teaming — he breaks AI products before users do.** Audience: founders, CTOs, engineering leaders at 50-500 person companies, plus the African tech ecosystem. He is mid-launch of "Breaking AI," a 21-part builder's field guide on LinkedIn.

## THE ONE SENTENCE THAT GOVERNS EVERYTHING

**Field guide, not threat poster.**

Everything should look like the cover system of a serious engineering handbook that a builder would leave on their desk. It must NOT look like cybersecurity marketing. Calm authority beats alarm. Navy calm beats red fear.

## PALETTE (exact hex, fixed ratios)

| Role | Hex | Usage |
|---|---|---|
| Base navy | #0A1428 | ~55% of every canvas |
| Deep panel | #12203C (gradient endpoint) | background depth |
| Grid thread | #14243F | texture only, never text |
| White | #FFFFFF | ~30%: primary type |
| Soft cyan | #8BB8E8 | ~10%: highlight blocks, rules, signature |
| Dim text | #CBD7E8 | sublines |

**Ratios are not suggestions.** Cyan is a scalpel. If cyan exceeds ~12% of a canvas, the design is sick. NEVER use: red, green, orange, yellow, neon, rainbow, or gradients behind/on text.

## TYPOGRAPHY (download-free, Google Fonts)

- **Display:** Montserrat ExtraBold (800). Headline lines. Sentence case ONLY ("I broke it in an hour." not "I Broke It In An Hour."). Sentences end with periods. Periods are part of the voice.
- **Body/labels:** Inter Regular + SemiBold. Sublines, kickers, signatures.
- Sizes at 1080px width: display 92-116pt, sublines 36-40, kicker 26-30 (tracking +2.5), signature 27.
- Auto-fit rule: no line ever comes within 40px of the right edge at margin 72. Shrink the font before you wrap a sentence awkwardly.

## THE LAYOUT SYSTEM (the signature device)

1. **Margins:** 72px left and right on a 1080 canvas. Every element left-aligned to this line. Nothing centered except whole-card compositions for quote squares.
2. **The twist block (the ONE signature):** the headline's pivot line is set in NAVY text (#0A1428) inside a solid CYAN rectangle (#8BB8E8), padding 34h × 22v, no rounded corners, no shadow. This is what yellow highlighting is to generic LinkedIn cards; it is our brand.
3. **Kicker chip:** top-left, white rectangle, navy text, 26-30pt Inter SemiBold, letter-spaced: e.g. "BREAKING AI · ARTICLE 1 IS LIVE". Never top-center, never full-width.
4. **Divider:** short cyan rule 164×8 between headline and subline. A period for the eye.
5. **Subline:** 2-3 Inter lines, dim white. Plain sentences, no adjectives.
6. **Signature footer:** one cyan Inter line, bottom area: "Olusanya Timothy · Lagos · Breaking AI #01/21".
7. **Vertical rhythm:** generous negative space is on-brand. Do not fill it with graphics.

## BACKGROUND RECIPE (the fix — every dark asset uses this, no flat fills)

1. Base: vertical linear gradient #0A1428 (top) → #12203C (bottom).
2. Grid: 1px lines every 56px, color #14243F, opacity ~100% over base (it IS a subtle step).
3. Vignette: radial darkening at corners, edges -15% brightness, center untouched.
4. Optional depth cue for covers ≥1920px: one 40%-opacity cyan horizontal glow 20px tall directly under the twist block. Never anywhere else.
5. Result must read as "navy with texture," never "black." If a screenshot of the card looks like #000 on a phone, the background failed.

Light-variant canvases (checklist/save cards): paper #F7F9FC, panel navy #0A1428, same cyan devices, no gradient, no grid.

## COPY GRAMMAR ON CANVASES

- Three beats max per card: setup line → twist (in the block) → promise/label line.
- Every headline is a sentence a builder would say out loud. Banned register: marketing verbs, exclamation marks, emoji, "unlock/elevate/leverage/revolutionary", question-marclickbait.
- Numbers are sacred: "6 attempts. 4 hits." beats any adjective.
- Em dash: never. Periods, commas, colons only.

## DO NOT (absolute list)

Hooded hackers, locks, shields, padlocks, binary rain, glowing brains, robot imagery, AI-glow gradients, lens flares, drop shadows on the block, rounded-corner highlight blocks, watermark quote glyphs, fake UI (profile photos, repost buttons, browser chrome) baked into images, Title Case headlines, more than 3 colors on one canvas, text within 40px of any edge, red anywhere, yellow anywhere.

## PHOTO RULES (profile + any face usage)

Real photo only, no illustrated avatars anywhere. Dark navy or plain wall background, plain shirt (charcoal or white), direct eye line to camera, one soft light source, natural expression (small smile or neutral, never pointing/gesturing). Crop square 1:1 at 400×400+. Face occupies ~60-70% of frame height, chin near bottom third. For cards with photos: photo occupies right ~35-40% of canvas, hard edge, NO rounded frames, NO circle masks except the profile itself, text left column untouched.

## ASSET SPECS (all @1x px, export PNG ≤8MB, sRGB)

| Asset | Size | Notes |
|---|---|---|
| Profile photo | 400×400 min, 1:1 | square crop safe |
| Profile banner | 1584×396 | headline left in 60% width; right 40% can carry a faint grid + cyan rule; name never in art (LinkedIn overlays) |
| Article cover | 1920×1200 (1.6:1) | safe zone: center 1600×950 |
| Feed card portrait | 1080×1350 | the standard for all micro-post cards |
| Feed card square | 1080×1080 | quote cards only |
| Feed wide | 1200×627 | only when a link preview must match a crop |
| Inline article image | 1600 wide, any height ≤900 | diagrams: single-weight 2-3px cyan lines on navy, one accent per diagram, labels 32px min |

## FILE + NAMING DISCIPLINE

One card = one message = one filename: `breakingai_{topic}_{size}.png`. Everything in `VISUAL/` or the article's `cards/` folder. Never export to Desktop. Never "final_v2.png".

## PER-ASSET CHECKLIST (run before shipping anything)

1. Base gradient + grid + vignette present?
2. Kicker chip top-left, cyan twist block, divider rule, signature line?
3. Sentence case, periods, zero em dashes, zero banned words?
4. Nothing within 40px of edges? Cyan under 12% coverage?
5. Thumbnail test: shrink card to 350px wide — is the twist block still the first thing you read?
6. Phone test: screenshot on a phone in daylight — does it read navy, not black?
7. Red/yellow/glow check: zero.

## THE FINAL FILTER (if a design passes everything but this, it fails)

Does this look like something a calm, expensive engineer made — or like something designed to be loud? **We are the person in the room who tests the thing. The brand is the quiet in that sentence.**
