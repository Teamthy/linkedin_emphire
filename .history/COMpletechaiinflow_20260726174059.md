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



═══════════════════════════════════════
🔗 CHAIN: WEEKLY 5-POST BATCH
═══════════════════════════════════════

PURPOSE: Create all 5 posts for the week in one 
session (Sunday batching)
TIME: 90 minutes manually
AUTOMATED: 15-20 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: WEEKLY REVIEW
Agent: Strategist
Input: Last week's performance data

Prompt:
"Analyze last week's LinkedIn performance:

[PASTE YOUR METRICS - impressions, engagement, 
best/worst posts, follower growth]

Provide:
1. Performance summary (3 sentences)
2. What worked (with why)
3. What didn't work (with why)
4. Pillar balance analysis
5. Emerging patterns
6. Recommendations for next week"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: WEEKLY THEME & CALENDAR
Agent: Strategist
Input: Review from Step 1

Prompt:
"Based on last week's analysis and my pillar rotation, 
plan next week's 5 posts (Monday-Friday):

For each day, provide:
- Day and best posting time
- Content pillar (across the week: balance!)
- Content style (variety across the week)
- Specific topic
- Hook angle
- Predicted performance

Rules:
- No same pillar two days in row
- Mix of technical + leadership + personal
- Include at least 1 story post
- Include at least 1 opinion/hot take
- Include at least 1 educational/framework

Return as calendar table with all 5 posts outlined."

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: BATCH POST WRITING
Agent: Content Creator
Input: Calendar from Step 2

Prompt:
"Write complete LinkedIn posts for all 5 days.

Here's the week plan: [PASTE CALENDAR]

For each post:
1. Generate 3 hook options
2. Select strongest
3. Write full 800-1500 char post
4. Format with proper line breaks
5. Include natural CTA
6. Suggest 3 hashtags

Ensure:
- Voice consistency across all 5
- Zero banned words in any post
- Variety in structure/style
- Each stands alone and provides value

Return all 5 complete posts, clearly separated 
by day."

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: VOICE & QUALITY REVIEW
Agent: Content Creator
Input: All 5 posts from Step 3

Prompt:
"Review all 5 posts:

[PASTE ALL 5 POSTS]

Quality check for each:
- Voice matches Timothy
- No banned words
- Has hook that stops scrolling
- Contains real insight/value
- Ends with natural CTA
- Mobile-friendly formatting

Flag any that need revision.
Provide improved versions where needed.

Return:
- Approved posts (as-is)
- Revised posts (with changes explained)"

Output → Feed to Step 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 5: VISUAL BRIEFS FOR CAROUSEL DAYS
Agent: Visual Designer
Input: Approved posts

Prompt:
"Review these 5 posts: [PASTE APPROVED POSTS]

Identify 2-3 posts that would benefit from carousels 
or posters.

For each visual-worthy post:
1. Determine visual type (poster/carousel/quote)
2. Provide complete design brief
3. Slide-by-slide script if carousel
4. Photo pose recommendation
5. Canva execution steps

Return visual briefs for chosen posts."

Output → Feed to Step 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 6: SCHEDULING & PUBLICATION PACKAGE
Agent: Strategist
Input: All posts and visuals

Prompt:
"Create the complete publication package for this week:

For each of the 5 posts:
- Day and time to publish
- Hashtag recommendations
- Predicted performance
- Optional engagement strategy
- Follow-up post ideas from each

Also provide:
- Weekly engagement targets (comments, DMs, etc.)
- Creators to prioritize engaging with this week
- Any collaboration opportunities to pursue
- One optional Friday/Saturday casual post idea

Format as a week-at-a-glance publishing plan."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ 5 complete posts (Mon-Fri) ready to schedule
✓ 2-3 visual design briefs
✓ Publishing calendar with times
✓ Hashtags for each post
✓ Engagement strategy for the week
✓ Performance predictions
✓ Bonus content ideas for weekend







═══════════════════════════════════════
🔗 CHAIN: DAILY ENGAGEMENT ROUTINE
═══════════════════════════════════════

PURPOSE: Prepare all daily comments and engagement
TIME: 15 minutes manually
AUTOMATED: 3-5 minutes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: TARGET IDENTIFICATION
Agent: Strategist
Input: List of target creators + today's date

Prompt:
"For today's engagement session, identify which 
creators to prioritize.

From my target creator list: [PASTE OR REFERENCE]

Consider:
- Who posts frequently and I haven't engaged with recently?
- Who has posted in last 24 hours (high visibility)?
- Who aligns with today's content focus?
- Who's in my target industries (AI, engineering, career)?

Return:
- Top 10 creators to engage with today
- 1-line reason for each
- Suggested comment type (agreement/challenge/story/question)"

Output → Feed to Step 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 2: COMMENT GENERATION (Batch)
Agent: Engagement Specialist
Input: Target list + their recent posts

Prompt:
"For each of these 10 creator posts, generate a 
substantive comment:

[PASTE 10 POSTS OR SUMMARIES]

For each post, provide:
1. Brief post summary (so I remember what it's about)
2. THREE comment options:
   A) Add expertise angle
   B) Personal story angle  
   C) Respectful challenge angle
3. Recommended option with reasoning
4. Tone notes

Requirements:
- Never generic ('great post!')
- Reference specific point from their post
- Add value or perspective
- Include personal experience where relevant
- 3-5 sentences ideal
- Natural voice (contractions, phrases)
- Zero banned words

Return all 10 comment sets."

Output → Feed to Step 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 3: DM DRAFTING (If any warm leads)
Agent: Engagement Specialist
Input: Warm connection list

Prompt:
"Draft DMs for these warm connections today:

[LIST OF PEOPLE TO DM]

For each person, provide:
1. Context reminder (why we're connecting/who they are)
2. Initial DM (if new connection)
3. Follow-up DM (if continuing conversation)
4. Value-add message (if warming a relationship)

Rules:
- Under 100 words each
- Personalized to them specifically
- Value-first, no pitching
- Ends with easy-to-answer question
- Warm but professional"

Output → Feed to Step 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 4: COMMENT REPLIES (On my posts)
Agent: Engagement Specialist
Input: Comments received on my recent posts

Prompt:
"Draft replies to these comments on my posts:

[PASTE COMMENTS]

For each comment:
1. Reply draft (2-3 sentences)
2. Alternative version if they were:
   - Disagreeing
   - Asking a question
   - Just being nice
3. Whether to continue conversation further

Requirements:
- Acknowledge their specific point
- Add value or continue conversation
- Include question when appropriate
- Warm but not overly formal
- Reference their comment specifically"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINAL OUTPUT PACKAGE:

✓ 10 comments ready to post on target creators' posts
✓ 3-5 DMs ready to send
✓ Replies to comments on my posts
✓ Estimated 15 minutes to execute all