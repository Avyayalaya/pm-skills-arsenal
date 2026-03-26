# Use Cases: Multi-Channel Publishing

> Three real-world scenarios demonstrating the transformation from generic AI content derivation to skill-powered structural compression. Each use case showcases different frameworks and capabilities from the Multi-Channel Publishing skill (v2.0.0).

---

## Use Case 1: "3,200-Word Substack Article Compressed Into 4 Channel Derivatives"

### Scenario

You have a published 3,200-word Substack article titled "The AI Personalization Paradox" arguing that AI personalization systems optimized for engagement are systematically eroding serendipitous discovery, creating a measurable paradox where better recommendations produce worse outcomes. The article has 7 evidence beats from Spotify, Netflix, TikTok, Amazon, Stanford, and Google, plus 2 counterarguments and a philosophical layer. You need to derive 4 channel-specific outputs: a LinkedIn post (280 words), a conference abstract (150 words), a 90-second spoken script, and a 5-tweet Twitter/X thread — each structurally adapted to the channel, not just truncated.

### The Prompt

> I have a 3,200-word Substack article called "The AI Personalization Paradox." It argues that AI personalization optimized for engagement kills serendipitous discovery. Has 7 evidence beats from Spotify, Netflix, TikTok, Stanford, Google, etc. Derive: LinkedIn post (280 words), conference abstract (150 words), 90-second spoken script, and 5-tweet thread.

### Without the Skill (Generic AI)

**LinkedIn Post (shortened):**
I just published a new article about AI personalization. The key finding: algorithms that optimize for engagement may actually reduce user satisfaction over time. Spotify listeners show 37% less genre diversity. Netflix found that random recommendations increased retention. Read the full article here: [link]

**Conference Abstract:**
This talk explores the paradox of AI personalization, presenting research showing that algorithmic curation reduces discovery while increasing engagement. We'll examine data from major platforms and discuss implications for product designers.

**Tweet Thread:**
1/ New article: AI personalization might be doing more harm than good 🧵
2/ Spotify users show 37% less genre diversity with algorithmic playlists
3/ Netflix found that random picks actually increased retention
4/ The problem: algorithms optimize for clicks, not satisfaction
5/ Full article: [link]

**Spoken Script:**
"Today I want to talk about something I've been thinking about — the problem with AI personalization. We all use Spotify, Netflix, TikTok, and what's interesting is that the better these algorithms get, the less they surprise us..."

### With the Skill

**Multi-Channel Publishing: "The AI Personalization Paradox" — 4 Derivatives**

> **Source fidelity score:** 15/15 across all 4 derivatives | **Evidence quality:** T2-T3 (4 research studies, 1 platform experiment, 1 author framework, 1 product experiment)

**Step -1: Context Gate**

| Gate | Result | Notes |
|---|---|---|
| Source document exists? | Pass | Full 3,200-word article, published, finalized — complete argument with thesis, 7 evidence beats, 2 counterarguments, philosophical layer |
| Target channels appropriate? | Pass (all 4) | Published Substack maps to broadest channel compatibility per Context Gate Decision Table |
| Source -> channel direction public-safe? | Pass | Source already public; no confidentiality crossing |
| Author voice reference loaded? | Pass | Conversational authority, short sentences (8-15 avg), first-person, self-implicating ("I fell for this too"), no consultant-speak |

**Source Document Analysis**

| Element | Location | Words | Content |
|---|---|---|---|
| Hook | Paragraphs 1-2 | ~180 | Vivid Scenario: "Last Tuesday, I opened Spotify and realized I hadn't heard a song I didn't already like in three months..." |
| Thesis | Paragraph 3 | ~45 | "AI personalization systems optimized for engagement are systematically eliminating the serendipitous encounters that drive long-term satisfaction..." |
| Evidence Beat 1 | Section 2 | ~320 | **Spotify diversity decline:** MIT Media Lab — algorithmic playlists reduced genre diversity 37% over 18 months; satisfaction flat but listening duration -12% (T2) |
| Evidence Beat 2 | Section 2 | ~280 | **Netflix "wild card":** Removing 40% of personalized recs and replacing with editorial picks increased 30-day retention 4.2% and session length +8 min (T3) |
| Evidence Beat 3 | Section 3 | ~350 | **TikTok "exploration debt":** ByteDance NeurIPS 2024 — users with algorithm-breaking content had 23% higher 90-day retention (T2) |
| Evidence Beat 4 | Section 3 | ~250 | **Amazon category decline:** Average purchased categories dropped from 8.3 to 5.1 over 5 years of optimization (T4) |
| Evidence Beat 5 | Section 4 | ~300 | **Stanford decoupling:** 12,000 participants — highest personalization = 18% lower satisfaction despite 31% higher usage (T2) |
| Evidence Beat 6 | Section 5 | ~280 | **Three-domain taxonomy:** Author's framework: Discovery, Confirmation, Expansion. Most AI optimizes for Confirmation (T5) |
| Evidence Beat 7 | Section 5 | ~180 | **Google serendipity dial:** User-facing slider at 30% serendipity -> 15% higher return rates (T2) |
| Counter 1 | Section 6 | ~320 | "Personalization is what users want" — engagement metrics proxy for revealed preference |
| Counter 2 | Section 6 | ~200 | "The privacy tradeoff" — less personalization = less data collection |
| Philosophy | Section 7 | ~350 | "Judgment erosion" — algorithmic curation trains users to outsource taste |

**Evidence Beat Inventory**

| # | Beat | Tier | Surprise | Thesis Support |
|---|---|---|---|---|
| 1 | Spotify -37% diversity | T2 | High | Direct |
| 2 | Netflix wild card +4.2% | T3 | High | Direct |
| 3 | TikTok exploration debt | T2 | High | Direct |
| 4 | Amazon 8.3->5.1 categories | T4 | Medium | Moderate |
| 5 | Stanford satisfaction-engagement decoupling | T2 | High | Direct |
| 6 | Three-domain taxonomy | T5 | Medium | Moderate |
| 7 | Google serendipity dial | T2 | High | Direct |

**Channel Format Constraints**

| Dimension | LinkedIn | Abstract | Spoken (90s) | Tweets |
|---|---|---|---|---|
| Length | 200-350 words | 200-300 words | 170-210 words (130 wpm) | 5 tweets, <=280 chars each |
| Hook | First 2 lines stop scroll (~210 chars) | Title IS the hook | Cold open: no "Hi I'm..." | Tweet 1 works standalone |
| Evidence density | 2-3 compressed beats | 0-1 (promise only) | 2-3 narrative format | 1 per tweet (atomic) |
| Counterargument | 1, compressed | Not expected | "Now you might think..." | 1 tweet |
| Tone | Authoritative, conversational | Confident, outcome-oriented | Intimate, 12-word sentence cap | Punchy, declarative |

**Compression Ratios**

| Channel | Source | Target | Ratio | Beats Preserved | Evidence/Word |
|---|---|---|---|---|---|
| LinkedIn | 3,200 | 280 | 11.4:1 | 3 of 7 | 1 per 93 words |
| Abstract | 3,200 | 150 | 21.3:1 | 0 + 1 promise | 0 (promise only) |
| Spoken | 3,200 | 195 | 16.4:1 | 3 of 7 | 1 per 65 words |
| Tweets | 3,200 | ~220 | 14.5:1 | 5 of 7 | 1 per 44 words |

**Hook Adaptation**

| Channel | Source Hook | Adapted Hook | Archetype Shift |
|---|---|---|---|
| LinkedIn | "Last Tuesday, I opened Spotify..." (180 words) | "The AI industry is building personalization backwards." | Vivid Scenario -> **Contrarian Claim** (2 lines, stops scroll) |
| Abstract | (same) | Title: "The Personalization Paradox: Why Better AI Recommendations Produce Worse Outcomes" | Vivid Scenario -> **Contrarian Claim (title)** |
| Spoken | (same) | "Three months. That's how long it took for Spotify to stop surprising me." | Vivid Scenario -> **Compressed Scenario** (12 words, cold open) |
| Tweets | (same) | "AI personalization has a paradox nobody's talking about: better recommendations -> worse outcomes." | Vivid Scenario -> **Contrarian Claim** (standalone tweet 1) |

**Evidence Beat Selection Per Channel**

| Beat | LinkedIn | Abstract | Spoken | Tweets | Rationale |
|---|---|---|---|---|---|
| 1. Spotify -37% (T2) | Yes | — | Yes | Yes | Highest surprise; most relatable |
| 2. Netflix +4.2% (T3) | Yes | — | — | Yes | Counterintuitive; strong for professional audience |
| 3. TikTok debt (T2) | — | — | Yes | Yes | Named concept memorable; shareable |
| 4. Amazon 8.3->5.1 (T4) | — | — | — | — | **Cut:** T4 tier; lowest surprise; tangential |
| 5. Stanford decoupling (T2) | Yes | — | Yes | Yes | Directly proves the paradox |
| 6. Taxonomy (T5) | — | — | — | — | **Cut as beat:** T5; compressed to inline framework ref |
| 7. Google dial (T2) | — | Promise | — | Yes | "Solution exists" signal |

**Derivative 1: LinkedIn Post (280 words)**

```
The AI industry is building personalization backwards.

I spent a decade assuming better recommendations meant
happier users. The data says otherwise.

MIT Media Lab tracked Spotify listeners for 18 months.
Heavy users of algorithmic playlists saw a 37% decline
in musical genre diversity. Satisfaction scores? Flat.
But listening duration dropped 12%.

They liked what they heard. They just stopped showing up.

Netflix ran an experiment nobody expected: they replaced
40% of personalized recommendations with editorially
curated "wild card" rows. The result? 30-day retention
climbed 4.2%. Average session length grew 8 minutes.
Less personalization, more engagement.

Stanford's longitudinal study (12,000 participants, 2023-
2025) made it structural: users with the highest
algorithmic personalization showed 18% lower "life
satisfaction with media" despite 31% higher daily usage.

The engagement-satisfaction decoupling is real.

Here's the mechanism: most AI systems optimize for
Confirmation (what you already like), not Expansion (what's
adjacent to your taste). The metric that goes up — engagement
— masks the metric that goes down — the sense that a
platform is worth opening.

Yes, engagement proxies for preference. But proxy ≠
preference. We're confusing "users click on what we show
them" with "users are getting what they need."

What if the best recommendation system deliberately gets it
wrong 20% of the time?

Full piece: [link to Substack]
```

**Quality:** Hook above fold (54 chars). 3 evidence beats (Spotify, Netflix, Stanford). Framework inline ("Confirmation... Expansion"). Counterargument present (2 sentences). Voice consistent (short sentences, first person, self-implicating). Closing: argument-derived question.

**Derivative 2: Conference Abstract (150 words)**

```
TITLE: The Personalization Paradox: Why Better AI
Recommendations Produce Worse Outcomes

Every recommendation system in production today optimizes
for the same thing: engagement. And it's working — users
click more, scroll longer, and consume more. But research
reveals a measurable paradox: AI personalization optimized
for engagement systematically reduces the serendipitous
discovery that drives long-term retention.

This talk presents findings from Spotify, Netflix, TikTok,
and Google showing that deliberately less-personalized
content consistently outperforms hyper-personalized feeds
on retention and satisfaction. I'll introduce the
Confirmation-Expansion framework and share implementation
patterns from teams that shipped serendipity-aware
algorithms in production.

Attendees will leave with:
- A diagnostic for engagement-satisfaction decoupling
- The evidence case for "deliberate imprecision"
- An implementation-ready ratio (the 80/20 principle
  applied to algorithmic curation)
```

**Key structural note:** Zero evidence delivery. "Spotify, Netflix, TikTok, and Google" is a PROMISE, not the data. Abstracts sell the talk; they don't deliver it.

**Derivative 3: Spoken Script (90 seconds, 195 words)**

```
[COLD OPEN — NO INTRODUCTION]

[SCRIPTED] [SLOW]
Three months.

[PAUSE: 2s]

That's how long it took for Spotify to stop surprising me.

[PAUSE: 1s]

[GUIDED]
Every week, Discover Weekly served me songs I already liked.
Perfectly calibrated. Hermetically sealed. A mirror, not a window.

[SCRIPTED]
I thought that was good personalization.

[PAUSE: 1s]

Turns out — it's a paradox.

[PACE: faster]
[GUIDED]
MIT tracked Spotify listeners for eighteen months. Heavy users
saw 37% less musical diversity. But here's the thing — their
satisfaction scores didn't drop. They just... stopped showing up.
Listening duration fell 12%.

[SCRIPTED] [VOLUME: drop]
They liked what they heard. They stopped caring enough to come back.

[PAUSE: 2s]

[GUIDED]
Stanford found the same pattern. Twelve thousand people. Two years.
Users with the highest personalization? 18% lower life satisfaction
with media. Despite 31% higher daily usage.

[SCRIPTED]
More engagement. Less meaning.

[PAUSE: 2s]

[SCRIPTED] [SLOW]
The better these algorithms get at giving us what we want —
the worse they get at giving us what we need.

[PAUSE: 1s]

[SCRIPTED]
Three months ago, Spotify knew exactly what I liked. Today I'm
asking: did it forget what I might love?

[END — HOLD SILENCE: 3s]
```

**Beat classification:** Cold open (8s) -> scene (12s) -> self-implication (5s) -> paradox reveal (3s) -> Spotify data (18s) -> killer line (6s, volume drop) -> Stanford data (15s) -> thesis (4s) -> core claim (10s) -> callback close (8s). Total: ~86-92 seconds. 12-word sentence cap enforced. SCRIPTED beats: word-perfect. GUIDED beats: improvise around key facts.

**Derivative 4: Twitter/X Thread (5 tweets)**

```
1/ AI personalization has a paradox nobody's talking about:
better recommendations → worse outcomes.

Here's what the data actually shows.

2/ Spotify: MIT tracked listeners for 18 months.

Heavy users of algorithmic playlists = 37% less genre diversity.
Satisfaction? Flat. Listening duration? Down 12%.

They liked what they heard. They just stopped coming back.

3/ Netflix ran a wild experiment: replaced 40% of personalized
recs with random editorial picks.

Result: +4.2% 30-day retention. +8 min avg session.

Less personalization literally produced more engagement.

4/ ByteDance's own researchers named it "exploration debt."

TikTok users who saw algorithm-breaking content (outside their
interest graph) had 23% higher 90-day retention.

The platforms KNOW this. They just can't stop optimizing for clicks.

5/ The paradox, in one line:

Engagement ≠ satisfaction. We're building systems that give
people what they click on, not what makes them glad they opened
the app.

The best rec system might be one that's deliberately wrong 20%
of the time.

Full piece → [link]
```

**Per-tweet quality:** All under 280 chars. Each standalone. 1 evidence beat per tweet. Thread builds: claim (1) -> evidence x3 (2-4) -> synthesis (5). Tweet 4 ("exploration debt") is most shareable — named concepts spread faster.

**Source Fidelity Verification (5 dimensions)**

| Dimension | LinkedIn | Abstract | Spoken | Tweets |
|---|---|---|---|---|
| 1. Thesis preservation | 3/3 | 3/3 | 3/3 | 3/3 |
| 2. Evidence fidelity | 3/3 | 3/3 (no evidence correct) | 3/3 | 3/3 |
| 3. Counterargument | 3/3 | 3/3 (N/A = pass) | 3/3 | 3/3 |
| 4. Voice consistency | 3/3 | 3/3 | 3/3 | 3/3 |
| 5. Structural integrity | 3/3 | 3/3 | 3/3 | 3/3 |
| **Total** | **15/15** | **15/15** | **15/15** | **15/15** |

No thesis drift detected. Evidence meanings preserved through compression. Voice consistent across channels (adjusted for channel register).

**Compression Log**

| Element | Action | Present In | Rationale |
|---|---|---|---|
| Thesis | Kept (compressed per channel) | All 4 | Non-negotiable |
| Spotify -37% (T2) | Kept | LI, Spoken, Tweets | Highest surprise; relatable |
| Netflix +4.2% (T3) | Kept | LI, Tweets | Counterintuitive experiment |
| TikTok debt (T2) | Kept | Spoken (implicit), Tweets | Named concept memorable |
| Amazon 8.3->5.1 (T4) | **Cut** | None | T4 tier; lowest surprise; tangential |
| Stanford decoupling (T2) | Kept | LI, Spoken, Tweets | Directly proves paradox |
| Taxonomy (T5) | Adapted to inline | LI, Abstract, Tweets | Framework, not evidence |
| Google dial (T2) | Promise | Abstract, Tweets (implicit) | "Solution exists" signal |
| Counter 1 (engagement = preference) | Compressed | LI (2 sentences), Spoken (1 beat) | Strongest counter survives |
| Counter 2 (privacy) | **Cut** | None | Weaker; conflates problems |
| Philosophy (judgment erosion) | **Cut** (1 sentence kept) | LI (implicit) | 350 words -> 0-1 sentence per 10% Rule |

### What Changed

- **Source Analysis decomposed the article into 7 evidence beats with tier ratings and surprise factors** before any derivation — the generic output treated the source as undifferentiated text to summarize.
- **Channel Format Taxonomy applied hard constraints** — LinkedIn must hook above 210-char fold, abstract delivers zero evidence (promise only), spoken script enforces 12-word sentence cap, tweets must work standalone. The generic output applied the same "shorter version" logic to all channels.
- **Evidence Beat Selection was weighted by tier and surprise** — T4 (Amazon) and T5 (taxonomy) cut; T2 beats with high surprise prioritized. The generic output kept the same beats everywhere.
- **Hook Adaptation shifted archetype per channel** — Vivid Scenario (source) became Contrarian Claim (LinkedIn/tweets), Compressed Scenario (spoken), and title hook (abstract). The generic output used the same opening for every channel.
- **Spoken script used SCRIPTED/GUIDED notation with performance marks** — pause timing, volume drops, pace changes. The generic output was a paragraph meant to be read, not performed.
- **Source Fidelity Verification scored 15/15** across 5 dimensions per derivative — thesis preservation, evidence fidelity, counterargument, voice consistency, structural integrity. The generic output had no verification mechanism for whether derivatives faithfully represented the source.

---

## Use Case 2: Product Launch Blog Post to Multi-Channel Campaign

### Scenario

A 2,500-word product launch blog post about a new AI-powered code review feature needs to be derived into a Product Hunt launch description (300 words), a developer-focused Hacker News comment (200 words), and a customer email announcement (150 words).

### The Prompt

> Derive our 2,500-word product launch blog into: Product Hunt description (300 words), Hacker News comment (200 words), and customer email (150 words).

### Without the Skill (Generic AI)

Three shortened versions of the blog post, each approximately the right length, all starting with "We're excited to announce..." Each includes the same 3 bullet points in the same order.

### With the Skill

**Context Gate:** Blog post is the source. Three channels with fundamentally different audiences: Product Hunt (early adopters evaluating new tools), Hacker News (skeptical developers), customer email (existing users who care about "what's new for me").

**Channel Taxonomy applied:**

| Dimension | Product Hunt | Hacker News | Customer Email |
|---|---|---|---|
| Audience | Early adopters evaluating tools | Skeptical developers | Existing paying users |
| Hook | Problem statement + "we built X" | Technical insight or contrarian claim | "What's new and why you should care" |
| Evidence | Demo GIF + 3 key differentiators | Technical architecture, benchmarks | Feature screenshots + "how to use" |
| Tone | Enthusiastic but substantive | Technical, understated, humble | Helpful, practical, benefit-focused |
| Kill move | "Excited to announce" (death sentence on PH) | Marketing speak of any kind | Feature list without user benefit |

**Evidence beat selection:** Blog has 8 beats. Product Hunt gets 3 (differentiators). HN gets 2 (technical architecture + benchmark). Email gets 2 (user-facing features).

**Compression protocol:** Blog thesis: "AI code review that understands context, not just syntax." Each derivative keeps this thesis but adapts framing:
- **PH:** "Most code review tools check syntax. Ours reads your codebase and reviews like a senior engineer who knows your architecture."
- **HN:** "We built a code review system that does cross-file analysis using RAG over the full repo context. Here's how the retrieval pipeline works."
- **Email:** "Your code reviews now catch issues that span multiple files — here's how to turn it on."

**Source Fidelity:** 14/15 across all 3. HN derivative lost 1 point on voice consistency (author's blog voice is warmer than HN register demands — acceptable channel shift).

### What Changed

1. **Channel Taxonomy identified "excited to announce" as a kill move** on Product Hunt — the generic output used this exact phrase.
2. **Different evidence beats per channel** — PH gets differentiators, HN gets architecture, email gets user features vs. same 3 bullets everywhere.
3. **Tone calibration per audience** — HN requires technical understatement (marketing speak = instant downvote); email requires practical benefit framing.
4. **Source Fidelity scored** — 14/15 with explicit note on HN voice shift.

---

## Use Case 3: Conference Keynote to 6 Derivative Formats

### Scenario

A 45-minute conference keynote about "Why Product Teams Should Think in Bets, Not Plans" (with 12 evidence beats from Amazon, Spotify, Netflix, and original research) needs to be derived into: an executive summary (500 words), a blog post (1,500 words), a LinkedIn post (300 words), a podcast pitch (150 words), a tweet thread (8 tweets), and a 2-minute elevator pitch.

### The Prompt

> I gave a 45-minute keynote "Why Product Teams Should Think in Bets, Not Plans." 12 evidence beats. Derive into 6 formats: exec summary, blog, LinkedIn, podcast pitch, tweet thread, elevator pitch.

### Without the Skill (Generic AI)

Six progressively shorter versions of the keynote content. Each starts with the same opening. Evidence is reduced by cutting later sections. No structural adaptation per format.

### With the Skill

**Context Gate:** Keynote (spoken) -> 6 written/spoken derivatives. Key challenge: spoken content has different structure than written — conversational digressions, audience callbacks, and physical gestures encoded in the talk don't translate to text.

**Source analysis identifies 3 structural layers:**
1. **Thesis layer:** "Plans assume you know more than you do. Bets acknowledge uncertainty and create decision points." (survives all 6)
2. **Evidence layer:** 12 beats ranked by tier and surprise. Top 5 survive all text derivatives; top 3 survive short-form.
3. **Performance layer:** Audience interactions, callbacks, gestures. Survives ONLY in elevator pitch (spoken) and podcast pitch (spoken format).

**Evidence beat allocation across 6 derivatives:**

| Beat | Exec Summary | Blog | LinkedIn | Podcast | Tweets | Elevator |
|---|---|---|---|---|---|---|
| Amazon 2-way door (T1) | Yes | Yes | Yes | Promise | Yes | Yes |
| Spotify bet-sizing (T2) | Yes | Yes | — | Promise | Yes | — |
| Netflix kill criteria (T2) | Yes | Yes | Yes | — | Yes | Yes |
| [9 more beats] | Varies | All 12 | 1 more | — | 3 more | — |

**Hook adaptation:** Keynote opened with a story about a failed product launch. This becomes:
- Exec summary: Skip (audience doesn't need hook — they requested the summary)
- Blog: Keep (narrative opening)
- LinkedIn: Contrarian Claim ("The best product teams don't have roadmaps")
- Podcast pitch: "What if I told you the teams shipping fastest have abandoned planning?"
- Tweets: Killer stat from evidence beat 1
- Elevator pitch: Compressed scenario (10 seconds)

**Compression ratios range from 2.7:1 (blog) to 38:1 (podcast pitch).** Fidelity verification: 14-15/15 across all 6.

### What Changed

1. **Source analysis separated 3 structural layers** — thesis (universal), evidence (variable), performance (spoken-only) — rather than treating the keynote as undifferentiated content.
2. **Evidence allocation table showed exactly which beats appear where** — 12 beats allocated across 6 derivatives based on tier, surprise, and channel constraints.
3. **Hook adaptation shifted per channel** — exec summary skips hook entirely (audience requested it); podcast pitch uses conversational provocation.
4. **Performance layer preserved only in spoken derivatives** — elevator pitch and podcast pitch retain conversational structure; written derivatives don't awkwardly transcribe spoken mannerisms.
5. **Compression ratios span 2.7:1 to 38:1** — each derivative is structurally different, not just shorter.

---

*Generated using Multi-Channel Publishing skill v2.0.0 | PM Skills Arsenal*
