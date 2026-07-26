═══════════════════════════════════════
🔗 CHAIN: DAILY POST CREATION
═══════════════════════════════════════

PURPOSE: Create a complete LinkedIn post from 
scratch, ready to publish
TIME: 15-20 minutes manually
AUTOMATED TIME: 3-5 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: TOPIC IDEATION
Agent: Strategist
Input: Today's date, day of week, pillar rotation, 
       recent post performance

Prompt:
"Based on my content pillar rotation and last week's 
performance, suggest today's post topic. Consider:
- Which pillar am I due to post from?
- What's my audience most engaged with lately?
- What's timely or trending in my space?
- What haven't I covered recently?

Return:
1. Recommended topic (specific)
2. Content pillar it serves
3. Suggested content style
4. Why this topic today
5. Angle recommendation"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: HOOK GENERATION
Agent: Content Creator
Input: Topic + angle from Step 1

Prompt:
"Using this topic and angle: [PASTE STEP 1 OUTPUT]

Generate 5 hook options using different styles:
1. Story-based hook
2. Question hook
3. Bold statement hook
4. Statistic/data hook
5. Contrarian opinion hook

For each hook:
- Full text
- Style used
- Predicted engagement type
- Emotion it triggers

Then recommend the strongest hook with reasoning."

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: FULL POST WRITING
Agent: Content Creator
Input: Selected hook from Step 2

Prompt:
"Using this hook: [PASTE SELECTED HOOK]

Write the complete LinkedIn post:

Requirements:
- 800-1500 characters
- Line breaks between paragraphs (max 2 lines each)
- Bold key phrases with asterisks
- Uses '→' for lists
- Natural CTA at end
- My authentic voice (reference voice_dna.txt)
- Zero banned words
- Include personal experience/perspective

Structure:
- Hook (2-3 lines)
- Context/problem
- Insight/story/framework
- Practical takeaway
- Natural CTA
- Optional: 3 relevant hashtags

Return the complete post ready to publish."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: VOICE VERIFICATION
Agent: Content Creator (or dedicated voice checker)
Input: Complete post from Step 3

Prompt:
"Review this post: [PASTE POST]

Voice check:
□ Does it sound like Timothy?
□ Are contractions used naturally?
□ Includes personal perspective?
□ Zero banned words used?
□ Has em dashes, fragments, or rhetorical questions?
□ Nigerian/African context if relevant?
□ Ends with natural CTA?

If any check fails, rewrite that section.
Return either:
- APPROVED: [post as-is]
- REVISED: [improved version]

Explain any changes made."

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: VISUAL BRIEF (Optional)
Agent: Visual Designer
Input: Approved post from Step 4

Prompt:
"For this post: [PASTE APPROVED POST]

Determine if it needs a visual:
- Text-only post (no visual): Justify why
- Simple graphic: Provide design brief
- Carousel: Provide multi-slide outline

If visual recommended, provide:
1. Type (poster/carousel/quote card)
2. Layout recommendation (A-F from templates)
3. Photo pose suggestion
4. Text overlay (max 6 words)
5. Color scheme
6. Canva execution steps"

Output → Feed to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 6: METADATA & PUBLISHING PREP
Agent: Strategist
Input: Post + visual from Steps 4-5

Prompt:
"Prepare publishing metadata:

1. Best posting time (based on my audience)
2. Three relevant hashtags
3. Suggested tags (people to tag if relevant)
4. Predicted performance (LOW/MED/HIGH)
5. Follow-up plan (comments to engage with)
6. Cross-platform adaptation notes

Also provide:
- 2 alternative CTAs to test
- Reply templates for likely comments
- Follow-up post ideas from this post"

Output → FINAL: Complete content package

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ Approved post ready to publish
✓ Visual design brief (if needed)
✓ Hashtags and metadata
✓ Best posting time
✓ Predicted performance
✓ Alternative CTAs
✓ Reply templates
✓ Follow-up content ideas

═══════════════════════════════════════
HOW TO RUN THIS CHAIN:
═══════════════════════════════════════

MANUAL METHOD (Using ChatGPT Projects):

1. Open Strategist project → Run Step 1
2. Copy output
3. Open Content Creator project → Paste output → Run Step 2
4. Copy output
5. Same project → Paste output → Run Step 3
6. Continue through all steps

Time: 15-20 minutes total

AUTOMATED METHOD (Using CrewAI or similar):

Build workflow that:
- Calls each agent sequentially
- Passes outputs automatically
- Returns final package

Time: 3-5 minutes total (mostly waiting for API)