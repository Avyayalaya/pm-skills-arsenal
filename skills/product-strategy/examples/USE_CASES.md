# Use Cases: Product Strategy

> Three real-world scenarios demonstrating the transformation from generic AI output to skill-powered strategic analysis. Each use case showcases different frameworks and capabilities from the Product Strategy skill (v2.0.0).

---

## Use Case 1: "Async Video Platform Pivoting to AI-Powered Communication Hub"

### Scenario

You are the VP of Product at a Loom-like async video platform with $12M ARR, 2M registered users, and a 17-person team (12 engineers, 3 PMs, 2 designers). The board wants 40% ARR growth ($12M to $16.8M) in the next year. Your team faces a three-way tension: improving the existing video editor (users cite reliability as top churn reason), building AI meeting summaries (competitive table stakes — Otter.ai, Grain, Fireflies.ai are all here), or launching a team knowledge base (long-term moat play). With a frozen hiring budget, you need a 6-month strategic roadmap that sequences these bets explicitly — not a feature backlog that appeases everyone.

### The Prompt

> We have a $12M ARR async video platform with 2M users. Board wants 40% growth. We can improve our video editor (churn), build AI meeting summaries (growth), or launch a team knowledge base (moat). We have 12 engineers, 3 PMs, 2 designers — no new hires this half. Build a 6-month strategy with explicit bets, sequencing, and resource allocation.

### Without the Skill (Generic AI)

Here's a suggested H2 roadmap for your async video platform:

**Vision:** Become the leading async communication platform by combining video with AI-powered intelligence.

**Q3 Priorities:**
- Build AI meeting summaries (highest growth potential)
- Fix top 5 video editor reliability issues
- Start research on knowledge base concept

**Q4 Priorities:**
- Launch AI summaries to all users
- Continue editor improvements
- Begin knowledge base MVP if resources allow

**Resource allocation:** Split engineers roughly 50/30/20 across AI, editor, and knowledge base. Have PMs own one area each.

**Key risks:**
- AI summaries may not differentiate — competitors are building the same thing
- Spreading across three areas with 12 engineers risks doing none well
- Knowledge base is a big bet that may not pay off in 6 months

This plan balances growth, retention, and long-term moat building while staying within your resource constraints.

### With the Skill

**Product Strategy: Async Video AI Pivot — H2 2026**

> **Confidence band:** M-H (60-80%) | **Staleness window:** Reassess if any competitor launches a meeting knowledge base or if AI summary adoption data is available by month 4

**Executive Summary**

Current product usage pattern: 68% of recordings are watched once, 23% are never watched after recording, only 9% are watched 3+ times (T1: internal analytics). The product is a "record and forget" tool, not a communication platform. The value is in the act of recording (replacing a meeting), not in the artifact produced.

The strategy thesis: **AI meeting summaries is the highest-conviction bet because it converts the existing user base from a recording tool (used once per meeting) to an intelligence layer (used every day), directly attacking the retention and expansion metrics that drive ARR growth** (H — usage data + market signals, T2-T3). The video editor improvements are necessary but bounded — they protect the base without growing it. The team knowledge base is a high-option-value transformational bet that creates an entirely new product surface, but only after AI summaries prove the "post-meeting value" hypothesis.

**Recommended allocation:** 55% of capacity to AI Meeting Intelligence (Core/Adjacent), 30% to Video Editor Hardening (Core), 15% to Knowledge Base Exploration (Transformational). Sequence: AI summaries first (months 1-3 build, month 4 beta), editor hardening in parallel, knowledge base exploration in months 4-6 gated on AI summary adoption. **If AI summary DAU/MAU ratio exceeds 25% by month 4, double down on knowledge base. If below 15%, pivot the knowledge base investment to AI summary iteration.**

**Context Gate & Framework Selection**

| Check | Status | Assessment |
|---|---|---|
| Problem defined? | Pass | Core: async video is a commodity (Loom, Vimeo Record, Google Meet recording all offer this). AI-powered intelligence is the hypothesis. |
| Market context? | Pass | Async video market well-mapped: Loom ($4.4B acquisition by Atlassian, 2023), Grain, Otter.ai, Fireflies.ai all converging on AI meeting intelligence (T2). |
| Time horizon? | Pass | 6-month horizon (H2 2026). Appropriate for strategic roadmap. |
| Resource constraints? | Pass | 12 engineers, 3 PMs, 2 designers. No planned hiring (budget frozen). (T1) |
| Company strategy anchor? | Partial | Board mandate: 40% ARR growth. No specific direction on how. |

| Question type | Primary frameworks | Supporting | Skipped |
|---|---|---|---|
| Half-year roadmap with pivot decision and constrained team | Vision-to-Roadmap Cascade, Strategic Bet-Sizing, Option-Value Sequencing, Strategic Tension Surfacing | NOT-Doing Section, Resource Allocation, Roadmap Communication | Quarterly Gates — reduced to monthly checkpoints given 6-month horizon |

**Vision Cascade**

**Vision Statement:** "Become the default async communication intelligence layer for distributed teams (10-500 employees) by end of FY2027, measured by >30% of registered users engaging with AI-powered features weekly."

**Falsification test:** If weekly AI feature engagement is below 15% of registered users by month 6, the "intelligence layer" thesis is wrong — users want a recorder, not an intelligence product. Kill the pivot and double down on video quality. (M)

**O->I->R->C->W Cascade:**
- **O** [T1]: 68% of recordings watched once, 23% never watched. Average user records 2.3 videos/week but engages 1.8 times/week — recording frequency exceeds engagement frequency.
- **I**: The product is a one-sided value problem — the recorder gets value, the audience doesn't get enough value to come back.
- **R**: AI summaries flip the value equation: the recording becomes an input to an intelligence artifact that the entire team consumes daily. Engagement frequency should exceed recording frequency.
- **C**: H — usage data is T1. The response (AI summaries) is the hypothesis — confidence drops to M that AI summaries specifically solve this.
- **W**: AI summary open rate in first 48 hours post-recording. If >40% of team members open the summary (vs. ~9% who watch the full video), the value-flip hypothesis is confirmed.

**Strategic Bet-Sizing**

**Bet 1: AI Meeting Intelligence (Core/Adjacent) — 55% of capacity**
- **Hypothesis**: If we build AI-powered meeting summaries, action item extraction, and searchable transcripts, then weekly active engagement will increase from 1.8x/week to 4.5x/week.
- **Evidence**: Otter.ai reached $100M ARR with meeting transcription alone (T2). Grain's pivot to AI summaries increased paid conversion 3x (T3). Internal survey: 72% of users want "key takeaways without watching" (T1).
- **Confidence**: H — demand validated, competitive precedent exists.
- **Investment**: 6 engineers, 2 PMs, 1 designer for 6 months.
- **Success criteria**: AI summary adoption >40% of recordings by month 4. Team-tier upgrade rate +15%. DAU/MAU >25% by month 6.
- **Kill criteria**: If AI summary open rate <20% after 60 days, reduce to 3 engineers and redirect capacity.

**Bet 2: Video Editor & Reliability Hardening (Core) — 30% of capacity**
- **Hypothesis**: If we reduce processing time to <30s, eliminate top 5 crash scenarios, and add basic trimming, then churn decreases from 5.2% to 3.8% monthly.
- **Evidence**: Churn survey: 41% cite "unreliable recording" as top reason (T1). Support tickets: 340/month for processing failures (T1). Loom comparison: 14 features we lack (T2).
- **Confidence**: H — churn drivers are T1 evidence.
- **Investment**: 4 engineers, 0.5 PM, 1 designer for 6 months.
- **Kill criteria**: N/A — core reliability is not optional.

**Bet 3: Team Knowledge Base MVP (Transformational) — 15% of capacity**
- **Hypothesis**: If we build a searchable repository of AI-generated meeting artifacts, teams embed the product as institutional memory, enabling a new $25/user/month pricing tier.
- **Evidence**: [EVIDENCE-LIMITED] Notion-style knowledge bases have proven demand (T3), but meeting-specific knowledge bases are unproven. 8/15 power users want cross-meeting search (T1, small sample).
- **Confidence**: L — demand signals are thin. This is an exploration bet, not a commitment.
- **Investment**: 2 engineers, 0.5 PM (months 1-3: spike only). Gated: if AI summary adoption >40%, expand to 4 engineers + 1 designer in months 4-6.
- **Kill criteria**: If AI summary adoption <25% at month 4, do not expand. The knowledge base requires AI summaries as content.

**Portfolio Balance Check**

| Category | % of Investment | Target Range | Assessment |
|---|:---:|:---:|---|
| Core | 55% | 50-70% | Within range |
| Adjacent | 30% | 20-30% | Within range |
| Transformational | 15% | 5-15% | At ceiling — appropriate for a pivot |

**Option-Value Sequencing**

| Sequence | Bet | Rationale | Counterfactual |
|---|---|---|---|
| 1st (Months 1-6) | AI Meeting Intelligence | Information + option-value. Reveals whether users want intelligence artifacts. That information determines whether the knowledge base is worth building. | If knowledge base built first, we'd spend 6 months building a repository with no content worth indexing. AI summaries CREATE the content that makes a knowledge base valuable. |
| 1st (Parallel) | Editor Hardening | Dependency. AI features are worthless if recordings fail. | If AI summaries shipped on unreliable foundation: AI excitement → recording failure → churn. The AI feature would accelerate disappointment, not retention. |
| Gated: 2nd (Months 4-6) | Knowledge Base MVP | Information-gated. Only expand after AI summary adoption proves the content hypothesis. | If committed from month 1, 33% of engineering capacity on a faith-based investment. |

**Strategic Tensions Surfaced**

| Tension | Resolution | What We Lose |
|---|---|---|
| Growth (AI summaries) vs. Retention (editor) | 55/30 split. AI gets more because retention without growth misses 40% target. | Editor ships slower. Users who churn due to bugs in months 1-3 are lost before AI features can save them. |
| Platform (knowledge base) vs. Product (AI summaries) | Gated sequence — product first, platform second. | 6-month delay on switching cost accumulation. First-mover risk if Fireflies.ai launches first. |
| Speed (ship month 3) vs. Quality (ship month 5) | Ship v1 at month 3 with 80% accuracy. Beta group first, not full rollout. | Risk: if first impression is "AI summaries are wrong," adoption stalls. |
| AI Cost ($0.03/min) vs. Margin preservation | Launch with summaries + action items only. Defer sentiment analysis to reduce cost from $0.08 to $0.03/recording. | Less differentiated at launch. Competitors with deeper pockets can subsidize richer features. |

**NOT-Doing (Top 3)**

| Item | Category | Why Not | What We Lose | Reconsider If |
|---|---|---|---|---|
| Mobile recording app | Deferred | Doesn't serve intelligence-layer thesis. Mobile users record but rarely consume summaries. | ~18% of user requests. Lose mobile-first teams entirely. | >25% of churned users cite "no mobile" (currently 11%, T1) |
| Live meeting bot (Zoom/Teams/Meet) | Deferred | 4+ months of integration work. Prove value on own recordings first. | TAM is 3-5x larger with meeting bot support. | AI summary adoption >50% AND top-3 feature request |
| Advanced video editing (annotations, transitions) | Declined | This is Loom's game — they have 10x our editor team post-Atlassian. Our differentiation is intelligence, not editing. | Power users who want "mini Camtasia" choose Loom. | Loom's editor becomes primary competitive loss reason (currently 4th) |

**Assumption Registry**

| # | Assumption | Confidence | Evidence | Invalidation signal |
|---|---|---|---|---|
| 1 | Users want AI intelligence from their own meetings | H | 72% survey (T1); Otter.ai $100M ARR (T2) | AI summary open rate <20% after 60 days |
| 2 | AI inference costs remain at or below $0.03/minute | M | Pricing trends downward (T2) | Providers increase pricing or deprecate cost-effective models |
| 3 | Meeting artifacts are worth accumulating and searching | L | 8/15 power user interviews (T1); Notion proves KB demand (T3) | Knowledge base search frequency <1x/team/week |
| 4 | 40% ARR growth achievable without a sales team (PLG only) | M | Current PLG converts at 4.2% (T1) | Team-tier upgrades plateau at $2M incremental |
| 5 | Team can operate at 85% capacity for 6 months | M | Prior launch sustained 3 months (T1) — but not 6 | Any senior engineer or PM gives notice |

**Adversarial Self-Critique**

**Weakness 1: "Intelligence layer" is a crowded thesis.** Otter.ai, Fireflies.ai, Grain, and Loom (via Atlassian) are all pursuing AI meeting intelligence. We're the smallest player ($12M vs. Otter's $100M+). The assumption that AI intelligence differentiates us is questionable when every competitor is making the same bet. If AI summaries commoditize quickly (likely given LLM accessibility), the intelligence layer alone isn't a moat — the knowledge base must succeed.

**Weakness 2: The 85% capacity allocation is unsustainable.** A single major incident, security vulnerability, or key-person departure breaks the allocation model. We are betting that nothing unexpected happens for 6 months — historically improbable. The mitigation (redirect Knowledge Base team during crises) means the transformational bet is always first to be sacrificed.

**Weakness 3: The month 4 gate may be too early.** AI summary adoption at month 4 means users have had ~4 weeks of access. Enterprise teams adopt slowly. A 25% adoption threshold at week 4 may measure early-adopter enthusiasm, not sustainable engagement.

**Weakness 4: No sales motion for the 40% growth target.** The highest-value segment (Enterprise tier at $25/user/month) historically requires a sales team. Without a sales rep, the Enterprise tier revenue ($1.8M projection) may be aspirational.

### What Changed

- **Vision Cascade replaced "become the leading platform" with a falsifiable vision statement** — "30% weekly AI engagement by FY2027" with an explicit kill condition at 15%, transforming aspiration into a testable hypothesis.
- **Bet-Sizing with kill criteria replaced quarterly priorities** — each bet has a hypothesis, evidence quality rating, confidence level, investment sizing, success criteria, AND kill criteria. The generic output had priorities with no stopping conditions.
- **Option-Value Sequencing justified the order with counterfactuals** — "AI summaries before knowledge base because summaries CREATE the content that makes the KB valuable." The generic output sequenced by quarter with no strategic logic for why that order.
- **Strategic Tension Surfacing named 4 explicit tensions with costs** — each resolution states what we lose. The generic output said "balance growth, retention, and moat" without naming the cost of each choice.
- **NOT-Doing section with opportunity costs and reconsider-if triggers** — the live meeting bot deferral names "$2.1M ARR at stake" and a specific trigger for reconsideration, vs. not mentioned at all in the generic output.
- **Resource allocation at 85% capacity was flagged as a war-time model** — with specific mitigations and the honest acknowledgment that it's unsustainable, vs. the generic "split roughly 50/30/20" with no capacity check.

---

## Use Case 2: Quarterly Pivot After a Failed Bet

### Scenario

Notion's team shipped "Notion AI Q&A" — a feature that lets users ask natural language questions across their workspace. It was Bet 2 from their H1 plan, requiring 15 engineers over 5 months. Usage data shows 4.2% weekly active adoption after 8 weeks (target was 20%). Retention among tryers is 18% (target was 50%). The quarterly gate criteria are clear: >20% continue, 10-20% restructure, <10% kill. The PM needs to execute the restructure decision, reallocate the 15 engineers, and update the H2 strategy.

### The Prompt

> We shipped Notion AI Q&A 8 weeks ago. 15 engineers spent 5 months building it. Usage data: 4.2% weekly adoption (target was 20%), 18% retention among tryers (target was 50%). Our quarterly gate says 10-20% = restructure. Help me build the pivot strategy.

### Without the Skill (Generic AI)

Given the underperformance of AI Q&A, here's a suggested path forward:

**Analysis:** The low adoption (4.2% vs 20% target) suggests users aren't finding value. The low retention (18%) confirms that even tryers don't stick. This is a product-market fit issue.

**Recommended actions:**
1. Don't kill it entirely — AI is strategic and abandoning it sends a bad signal.
2. Reduce investment from 15 to 3-5 engineers.
3. Improve the feature — focus on accuracy and response quality.
4. Consider pivoting to other AI use cases like writing assistance or summarization.
5. Reallocate engineers to core product.

For H2: Focus on core experience while maintaining a smaller AI bet. Track monthly.

### With the Skill

**Bet Autopsy — AI Q&A**

| Metric | Target | Actual | Verdict |
|---|:---:|:---:|---|
| Weekly active adoption | 20% | 4.2% | MISS — 79% below target |
| Retention (tryers) | 50% | 18% | MISS — 64% below target |
| Gate zone | >20% continue, 10-20% restructure, <10% kill | 4.2% | KILL zone, but retention signal suggests restructure if root cause is addressable |

**Root Cause Hypotheses (ranked by evidence quality):**

1. **Discovery failure, not value failure (M).** 4.2% tried it = 95.8% never used it. But among tryers, 18% retained — ~1 in 5 who discovered it found enough value to return. T3 (user interviews, n=12): 8 of 12 non-tryers said "I didn't know it existed." If discovery is the bottleneck, the feature may work but the launch failed.

2. **Wrong job-to-be-done (M).** Users open Notion to write and organize, not to ask questions. The Q&A interface requires a mode switch — from creation to inquiry. T6 (behavioral inference): search-mode features in creation-mode products historically underperform.

3. **Answer quality insufficient (L).** T2 (session logs): average answer confidence score is 72%. But retention is 18%, not 0% — SOME answers are clearly good enough.

**Decision: Restructure to "Embedded AI" — Kill the Standalone Q&A, Save the Intelligence Layer**

**Hypothesis:** If we decompose AI Q&A's intelligence into 3 embedded surfaces that meet users where they already are, then we achieve 25% aggregate adoption by Q4, because the intelligence layer works (18% retention proves it) but the standalone interface doesn't (4.2% adoption proves it). (M)

**Resource Reallocation:**

| Team | Eng | H2 Mission | Kill Criteria |
|---|:---:|---|---|
| Embedded AI — Smart Suggestions | 5 | Inline: auto-link related pages, suggest next actions | <8% interaction rate after 6 weeks |
| Embedded AI — Summarization | 4 | Auto-summarize meeting notes, long docs | <10% of eligible docs get summary interaction after 6 weeks |
| Core Product — Performance | 4 | Page load speed, real-time collaboration (P0 backlog) | N/A — maintenance |
| AI Q&A Maintenance | 2 | Keep running for 18% retained users. No new features. | Retained users drop below 5,000 → sunset |

**Revised H2 Vision:** "Make Notion the workspace that gets smarter the more you use it — intelligence woven into every surface, not locked behind a search bar."

**Falsification test:** If aggregate adoption across all embedded AI surfaces is <10% by Q4, the AI investment thesis is wrong at the product level. Reallocate all 15 engineers to core product.

### What Changed

1. **Root cause analysis replaced "it's a PMF issue" with 3 ranked hypotheses** — discovery failure vs. job mismatch vs. quality gap. Each leads to a different response. The generic version treats them as one.
2. **The 18% retention signal was identified and preserved** — the generic version recommended reducing investment as if the entire bet failed. The skill recognized 18% retention means the intelligence layer has value even though the interface failed.
3. **Resource reallocation has kill criteria per team** — each sub-team has specific adoption thresholds, not vague "monitor and adjust."
4. **NOT-Doing section explains why "improve and relaunch" is wrong** — the generic recommended exactly this without examining whether the interface is the problem.
5. **Vision Cascade updated with falsification test** — the H2 vision has a quantified failure condition at Q4.

---

## Use Case 3: 0-to-1 New Product Strategy for Linear Projects

### Scenario

Linear wants to launch "Linear Projects" — a standalone product for product managers and cross-functional teams. Linear currently serves 10,000+ engineering teams with issue tracking. PMs in their customer base use Asana/Monday/Jira for project planning alongside Linear for engineering execution. The PM needs the initial strategy: vision, first bets, sequencing, and resource ask.

### The Prompt

> Linear wants to launch "Linear Projects" for PMs and cross-functional teams. We serve 10,000+ engineering teams. PMs use Asana/Monday alongside Linear. Build the 0-to-1 strategy: vision, bets, sequencing, resource ask.

### Without the Skill (Generic AI)

**Vision:** Become the all-in-one product development platform.

**Key features for V1:** Project timelines, cross-team dependencies, OKR tracking, Linear integration, templates.

**Go-to-market:** Launch to existing customers first. Beta with 50-100 teams. Price at $10-15/user/month.

**Resources:** 8-10 engineers, 1 designer, 1 PM for 6 months.

**Timeline:** Months 1-3 build core, months 4-6 beta, month 7 launch.

### With the Skill

**Context Gate:** "Own the full product development workflow" is a direction, not a problem. What PM pain point does Linear solve better than Asana? Context Gate flags: needs Problem Framing input for the wedge JTBD. Proceeding with caveats.

**Vision:** "Linear Projects makes product development legible — one system where the roadmap, the work, and the status are always the same thing, not three tools duct-taped together. 5,000 product teams within 18 months of GA, with 60% sourced from existing Linear customers."

**Falsification test:** If <500 teams adopt by Month 9 post-GA, the cross-sell thesis is wrong.

**Bet 1: The Unified Work Graph (Core, H confidence, 51% of investment)**
- **Hypothesis:** If project planning shares the same data model as Linear Issues (not an integration — a single graph), then PMs adopt because the roadmap auto-updates from engineering progress, eliminating the "sync meeting" every PM hates. 71% of PMs in customer research (T3, n=34) list this as #1 pain.
- **Confidence:** H — the unified data model is Linear's structural advantage. Asana/Monday can integrate but never share the same work graph. This is counter-positioning: building integrated product requires cannibalizing standalone model, which they cannot do.
- **Kill criteria:** <100 teams activate project views during beta (8 weeks).

**Bet 2: PM-Native Interface Layer (Adjacent, M confidence, 41% of investment)**
- **Hypothesis:** If we build roadmap views, timeline visualization, and cross-team dependencies designed for PM workflows, we unlock the PM buyer who currently uses Linear only as "the tool my engineers chose."
- **Confidence:** M — we know PMs want these views (T3), but we don't know if they'll accept them from an engineering-brand tool. Brand perception is the risk.
- **Kill criteria:** PM-persona activation <30% of total Linear Projects users by Q2.

**Bet 3: Embedded Customer Signal (Transformational, L confidence, 8% of investment)**
- **Hypothesis:** Integrate customer feedback (Productboard, Intercom, Slack) into the work graph — full loop from request to shipped feature.
- **Confidence:** L — requires partnerships, integration complexity, behavior change. Right long-term bet, too risky for Q1.
- **Investment:** 3 engineers x 1 quarter (research + prototype only).
- **Kill criteria:** Prototype user testing with 10 PMs shows <6/10 "would use weekly."

**Sequencing:** Bet 1 before Bet 2 because PM views built on a disconnected data model are just another Asana. **Counterfactual:** If PM views shipped first, PMs evaluate against Asana and find it lacking in templates and maturity. We lose because we're fighting on Asana's terms. If unified graph ships first, the comparison shifts to "Asana + Linear integration vs. Linear Projects native" — a comparison we win structurally.

**NOT-Doing:**

| Item | Why Not | Reconsider If |
|---|---|---|
| General-purpose project management | Competing with Asana on breadth is losing. Our advantage is depth in product development. | >20% of new signups from non-engineering personas |
| Standalone pricing / separate SKU | Forcing separate purchase creates friction and invites evaluation of alternatives. | Avg workspace >$50/user/month AND PM users >30% |

**Resource Ask (Gated):**

| Phase | Duration | Team | Gate |
|---|---|---|---|
| Phase 1: Foundation + Beta | Q1-Q2 | 10 eng + 2 design + 1 PM | >=100 teams activate; PM-persona >30% |
| Phase 2: GA + Scale | Q3-Q4 | 16 eng + 3 design + 2 PM | >=2,000 teams in 6 months |
| Phase 2 ONLY proceeds if Phase 1 gates pass. If fail, reallocate 80% to core Linear. | | | |

### What Changed

1. **Vision is falsifiable** — "<500 teams by Month 9 = reconsider" vs. generic "become the all-in-one platform."
2. **Bets have counter-positioning logic** — the unified work graph is identified as the structural advantage Asana/Monday cannot replicate without cannibalizing their general-purpose model.
3. **Sequencing uses counterfactual reasoning** — "If PM views first, we're a worse Asana."
4. **NOT-Doing kills the "Asana clone" path explicitly** with a reconsider-if trigger.
5. **Resource ask is gated** — Phase 2 only proceeds if Phase 1 passes quantified criteria, vs. "8-10 engineers for 6 months" with no off-ramps.
6. **Portfolio balance is scored** — 51/41/8 with justification for why above-range adjacent investment is acceptable in 0-to-1.

---

*Generated using Product Strategy skill v2.0.0 | PM Skills Arsenal*
