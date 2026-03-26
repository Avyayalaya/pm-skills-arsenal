# Use Cases: Executive Writing

> Three real-world scenarios demonstrating the transformation from generic AI output to skill-powered executive documents. Each use case showcases different frameworks and capabilities from the Executive Writing skill (v2.0.0).

---

## Use Case 1: "Strategy One-Pager: Invest $2M to Build DataVault's AI API Platform"

### Scenario

You are a Senior PM at DataVault, a $18M ARR SaaS analytics platform with 340 mid-market customers and 87% gross retention. Your VP of Product (James Park) has $3M signing authority for product investments. Three competitors — Amplitude, Mixpanel, and Streamline — launched developer API products in the last 9 months. Amplitude's API now accounts for 22% of new bookings. Your sales team reports 6 of the last 14 lost deals cited "no API access" as a deciding factor. You need to write a strategy one-pager recommending a $2M investment in an AI-powered API platform — and it needs to be structured for the VP's decision-making style, not a generic strategy document.

### The Prompt

> Write a strategy one-pager for my VP of Product recommending that DataVault invest $2M to build an AI-powered API platform. DataVault has $18M ARR, 340 customers, 87% gross retention. Three competitors launched APIs in 9 months. 6 of 14 lost deals cited "no API access." The VP has $3M signing authority. He reads documents asynchronously and annotates in Google Docs.

### Without the Skill (Generic AI)

**DataVault API Platform Strategy**

**Executive Summary:**
DataVault should consider building an API platform to remain competitive in the evolving analytics market. Several competitors have recently launched API products, and we're seeing increasing demand from customers who want to embed analytics into their own products.

**Market Context:**
The embedded analytics market is growing rapidly. Amplitude, Mixpanel, and a new competitor called Streamline have all launched API products. This trend suggests that the market is moving toward embedded analytics as a standard offering.

**Recommendation:**
We recommend investing in building an API platform. The exact investment amount should be determined after a technical assessment, but we estimate it would require significant engineering resources over 6-8 months.

**Benefits:**
- Unlock new revenue stream from developer-focused customers
- Reduce churn from customers wanting embedded analytics
- Position DataVault as a platform, not just a dashboard tool
- Leverage our AI capabilities as a differentiator

**Risks:**
- Engineering resources diverted from core product
- API maintenance creates long-term obligation
- Competitors have a head start

**Next Steps:**
Schedule a meeting to discuss the technical requirements and timeline. We should also talk to sales about the pipeline opportunity.

### With the Skill

**The Finished Executive Document (as the VP would receive it)**

---

**DataVault Should Invest $2M to Launch an AI API Platform in H2 2026**

*Date: 2026-03-12 | Author: Sarah Chen, Sr. PM | For: James Park, VP of Product | Ask type: Decision*

---

**Situation.** DataVault's SaaS analytics platform generates **$18M ARR** with 340 mid-market customers and 87% gross retention (T1). Our core product — real-time data dashboards and SQL-based reporting — has achieved product-market fit. Engineering has built proprietary data processing infrastructure that handles **2.3 billion events per day** (T1).

**Complication.** Three competitors launched developer API products in the last 9 months (T2). Amplitude's API platform now accounts for **22% of their new bookings** (T2). Our sales team reports that **6 of our last 14 lost deals cited "no API access"** as a deciding factor (T1). Without an API platform, we are locked into the dashboard-only segment while the market shifts to embedded analytics (H).

**Recommendation.** **Invest $2M ($1.4M engineering + $600K go-to-market) to build and launch an AI-powered API platform by Q4 2026** (H). This unlocks an estimated **$6.2M incremental ARR within 18 months** by: (1) converting lost API deals, (2) expanding existing accounts from dashboard to dashboard + embedded, and (3) entering the developer-tools segment. DataVault's AI differentiation — predictive anomaly detection and natural-language query — gives our API a structural advantage over competitors offering raw data endpoints. Key assumption: mid-market companies want **intelligent APIs** (AI-enriched responses), not just data pipes (M).

**Strategic Options**

| Dimension | Option A: Full AI API | Option B: Basic REST API | Option C: Do Nothing |
|---|---|---|---|
| Cost | $2M (6 eng, 8 months + GTM) | $800K (3 eng, 5 months) | $0 direct |
| Expected ARR impact | +$6.2M in 18 months (T3) | +$2.8M in 18 months (T3) | -$2.1M (lost deals) (T1) |
| Risk | M — engineering capacity strain | L — commoditized offering | H — market share erosion |
| Reversibility | Hard — API contracts are commitments | Easy to extend later | Reversible but window narrows |
| Key tradeoff | Delays v4.2 dashboard by one quarter | No AI differentiation; competes on price | Cedes embedded analytics to Amplitude |

**Recommendation: Option A.** A basic REST API puts us 12 months behind Amplitude with no differentiation. Our competitive advantage is AI-enriched analytics, which cannot be replicated by bolting AI onto a data pipe after launch. Option A builds AI-native from day one. Key assumption: customers will pay a **30-40% premium** for AI-enriched API responses (M).

**Key Risks**

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| v4.2 dashboard delayed | H | 3 accounts expecting v4.2; $420K at risk | Pre-brief accounts. Deliver high-priority items Q3, remainder Q1 2027. |
| API adoption slower than modeled | M | $6.2M target missed 30-50%; ROI extends 24+ months | Gate: if <15 API beta signups by Q3, pause GTM and reassess. |
| Amplitude launches AI API first | M | First-mover advantage narrows | Ship beta Q3 (not Q4). Accept tech debt for speed. Our 2.3B events/day vs. ~800M gives scale advantage. |

**The Ask.** **Approve the $2M investment (Option A).** Engineering begins sprint planning April 1. If not approved by March 28, we miss the Q3 beta window and Amplitude's lead grows from 6 to 9 months. Next step: engineering kickoff April 1, beta partner recruitment April 15 (Chen + Williams own).

*Appendix available on request: competitive analysis, financial model, technical architecture, beta pipeline.*

---

**How the Skill Built This Document (Framework Dissection)**

**Step -1: Context Gate**

| Check | Assessment | Result |
|---|---|---|
| Artifact fit | VP reads docs asynchronously, annotates in Google Docs. Written document correct. (T1: observed behavior) | Pass |
| Analysis readiness | Clear recommendation + evidence: lost deal data (T1), competitive timeline (T2), financial model (T3) | Pass |
| Decision authority | VP has $3M signing authority. $2M within his authority. (T1: budget policy) | Pass |
| Timing | Amplitude launched 9 months ago; Q2 planning starts April 1; 6 lost deals provide fresh evidence | Pass |

**Step 0: Format Routing**

| Signal | Points To | Match? |
|---|---|---|
| "Strategy one-pager" | Strategy One-Pager | Direct match |
| VP as audience (single decision-maker) | Strategy One-Pager (not group) | Yes |
| $2M within VP authority | Not complex enough for Board Memo | Yes |

**Selected: Strategy One-Pager.** 400-600 words, answer-first, async consumption optimized. Board Memo rejected (over-engineering for VP decision). Decision Brief rejected (optimized for meetings, not async).

**Minto Pyramid / SCR**

| Element | Purpose | Application |
|---|---|---|
| Situation | Shared context (2-3 sentences) | "$18M ARR, 340 customers, 87% retention, 2.3B events/day" |
| Complication | What changed (2-3 sentences) | "3 competitors launched APIs. 6/14 lost deals. Market shifting." |
| Resolution | The answer (paragraph 1) | "Invest $2M. Launch by Q4 2026. Unlocks $6.2M ARR." |

**10-Second Test: Pass.** Reader scanning only the recommendation gets: what to do ($2M AI API), when (Q4 2026), what it achieves ($6.2M ARR), and confidence (H).

**Audience Calibration**

| Dimension | VP of Product (selected) | CFO | CTO | CEO |
|---|---|---|---|---|
| Primary lens | Strategic fit + competitive positioning | Unit economics + ROI | Technical feasibility + capacity | Market position + growth |
| Opens with | "Competitors launched APIs; we're losing deals" | "$2M yields 4x ROI at month 11" | "6 engineers for 8 months; reallocate from v4.2" | "$4.2B embedded analytics market, 28% CAGR" |
| Risk framing | Competitive risk — what if we don't | Financial risk — downside scenarios | Execution risk — team dependencies | Strategic risk — market window |
| Ask framing | "Close the competitive gap" | "Approve $2M from product budget" | "Commit 6 engineers for 8 months" | "Align on embedded analytics as priority" |

**Decision Architecture**

| Criterion | Assessment |
|---|---|
| Type 1 or 2? | Type 1 (One-Way Door) — API contracts are commitments. Deprecating endpoints breaks customer products. |
| Evidence bar | High — need strong data. Have T1 (lost deals, metrics) and T2 (competitive launches). Met. (H) |
| Options | 3 structurally different (technology, cost, positioning). Each has genuine advantage. |
| "Do nothing" quantified | Option C: -$2.1M from continued lost deals. ~$350K/month opportunity cost. |

**Evidence Cascade**

| Level | Content | Where It Appears |
|---|---|---|
| L1 (Headline) | "6 of 14 lost deals cited no API" (T1) | Document body |
| L2 (Summary) | "$2.1M in lost ARR: Acme $380K, Nexus $290K, four others" | Selected body + appendix |
| L3 (Appendix) | Full CRM export, AE transcripts, financial sensitivity model | "Available on request" |

**Zero-Jargon Compression:**

| PM Draft | After Compression |
|---|---|
| "DataVault has achieved PMF in the mid-market analytics vertical with strong NRR metrics" | "DataVault's analytics platform generates $18M ARR with 87% gross retention" |
| "Competitors are leveraging API-first strategies to capture the embedded analytics TAM" | "Three competitors launched API products in the last 9 months" |

**Quality Gate: 12/12**

| # | Check | Result |
|---|---|---|
| 1 | 10-second test (recommendation extractable) | Pass |
| 2 | Ask present (explicit, time-bound, actionable) | Pass — "Approve by March 28" |
| 3 | Audience calibrated (VP = competitive lens) | Pass |
| 4 | SCR structure (answer first) | Pass |
| 5 | Options genuine (structurally different) | Pass — technology, cost, positioning differ |
| 6 | Jargon clean | Pass — 2 acronyms (ARR, API) |
| 7 | Risks honest (probability + impact + mitigation) | Pass — 3 risks, each with P/I/M |
| 8 | Evidence leveled (L1 body, L2 appendix) | Pass |
| 9 | Word count (400-600 for One-Pager) | Pass — 487 words |
| 10 | Reversibility stated per option | Pass |
| 11 | Assumptions surfaced | Pass — "intelligent APIs vs. data pipes" (M) |
| 12 | "So what" complete (every paragraph connects to decision) | Pass |

**Assumption Registry**

| # | Assumption | Confidence | Evidence | Invalidation Signal |
|---|---|---|---|---|
| 1 | Customers want intelligent APIs (AI-enriched), not raw endpoints | M | T1: lost deals mentioned "API access" not AI. T3: dev survey 67% prefer AI-enriched. | <15% AI tier adoption in beta |
| 2 | 2.3B events/day scale = structural API advantage | H | T1: internal metrics. T2: Amplitude ~800M. 3x scale advantage. | Amplitude closes to within 2x via investment |
| 3 | $6.2M ARR achievable in 18 months | M | T3: financial model (60% lost deal recovery + 15% upsell + new segment) | Deal cycles >6 months or upsell <10% |
| 4 | 6 engineers reallocatable without material churn risk | M | T1: 3 accounts expecting v4.2, $420K ARR, health scores >80/100 | Any of 3 accounts escalates or churn signals |
| 5 | Amplitude won't launch AI API before our Q3 beta | L | T2: Q4 earnings mentioned "AI in 2026 roadmap." T3: ML job postings. | Amplitude April developer conference announcement |

**Adversarial Self-Critique**

**Weakness 1: "No API access" may be a proxy for price sensitivity.** 6 lost deals cited API, but it may be the socially acceptable reason when the real issue is price, features, or sales execution. If 3 of 6 were actually lost on price, the demand signal drops 50%. Test: re-interview lost accounts with non-sales interviewer.

**Weakness 2: AI premium pricing is untested.** Assuming 30-40% premium for AI-enriched responses. The dev-tools market is brutally price-competitive — Stripe succeeded with simple APIs, not AI magic. If devs want reliable data pipes, our premium puts us at cost disadvantage. Test: offer both tiers in beta; if <30% choose AI tier, premium isn't valued.

**Weakness 3: We may be solving a sales problem with a product investment.** Some "lost to API competitor" deals may have been recoverable with better sales execution or integration partnerships. Building a $2M product when the real issue is enablement is expensive misdiagnosis. Test: review 6 deals for sales process quality — were alternatives proposed? Were pilots offered?

### What Changed

- **Minto Pyramid / SCR structure replaced background-first with answer-first** — recommendation in paragraph 1 with the "ask" explicitly time-bound ("approve by March 28 or we miss Q3 beta"), vs. recommendation buried after 4 paragraphs of context.
- **Audience Calibration for VP of Product shaped every element** — led with competitive threat (not ROI), framed risk as "what happens if we don't move" (not financial downside), structured ask as "close the competitive gap" (not "approve the budget"). The generic output was audience-agnostic.
- **Decision Architecture produced 3 structurally different options including "do nothing"** — Type 1 classification (irreversible), genuine advantages per option, cost of inaction quantified at $2.1M. The generic output said "we recommend" with no alternatives.
- **Evidence Cascade with L1/L2/L3 levels replaced a flat list of bullet points** — body uses headlines ("6/14 lost deals"), appendix holds methodology. Zero jargon — 2 acronyms vs. the generic output's PMF, NRR, TAM.
- **Quality Gate (12/12) validated every structural element** — 10-second test, audience calibration, MECE options, reversibility per option, assumptions surfaced. The generic output had no quality assurance mechanism.
- **Format Routing prevented over-engineering** — Strategy One-Pager (400-600 words) selected over Board Memo (3-5 pages) because the VP has $3M authority and reads 15-20 docs/week. The generic output produced a full-length document with no format awareness.

---

## Use Case 2: Board Memo for Series B Fundraise Narrative

### Scenario

A Series A startup ($8M ARR) needs a board memo explaining why they're raising Series B now instead of in 6 months. The board has 5 members who read in advance of the quarterly meeting. One board member (lead investor) is skeptical about the timing.

### The Prompt

> Write a board memo explaining why we should raise Series B ($30M) now at $8M ARR instead of waiting 6 months for $12M ARR. One board member thinks we should wait.

### Without the Skill (Generic AI)

**Board Update: Series B Fundraising Timeline**

Dear Board Members,

We'd like to discuss accelerating our Series B timeline. While our current plan targets $12M ARR before raising, several factors suggest we should move now...

[Continues for 1,500 words with market conditions, competitive landscape, and a vague recommendation]

### With the Skill

**Context Gate:** Board Memo is the correct format — 5 readers, group decision, read before meeting. NOT a Strategy One-Pager (group, not individual). NOT a Decision Brief (read before, not during meeting).

**Format Routing:** Board Memo, 3-5 pages, L1+L2 evidence in body, meeting discussion guide at end.

**SCR:**
- **S**: $8M ARR, 40% growth, $2M cash remaining. Board approved $12M ARR as Series B trigger.
- **C**: Two shifts since the trigger was set: (1) two competitors raised Series B in last 90 days totaling $85M (T2), and (2) our enterprise pipeline has $4.2M in Stage 3+ deals that close in 60-90 days but require dedicated CS team we can't hire without funding (T1).
- **R**: Raise Series B now at $8M ARR. Waiting costs us $4.2M in pipeline and 6 months of competitive ground. The $12M trigger was correct when set; the competitive landscape changed.

**Audience Calibration — The Skeptic:**

| Board Member | Position | Frame |
|---|---|---|
| Lead investor (skeptic) | "Wait for $12M — better valuation" | Address directly: "Waiting costs $4.2M in pipeline AND lets competitors lock in enterprise customers. The valuation uplift at $12M (~20% higher) doesn't compensate for $4.2M in lost deals and competitive disadvantage." |
| Other 4 members | Likely supportive | Standard risk/reward framing |

**Decision Architecture:** Type 2 (reversible — we can stop fundraise at any point). But the window is Type 1 (competitive ground lost is irreversible). Present as: "The fundraise is reversible. The pipeline loss is not."

**Adversarial self-critique:** The $4.2M pipeline may not close even with CS. If only 60% closes, the urgency argument weakens but still holds — $2.5M in wins plus competitive positioning justifies raising 6 months early.

### What Changed

1. **Format Routing selected Board Memo over One-Pager** — 5 readers, group decision, read-ahead format.
2. **Skeptic board member explicitly addressed** with a dedicated rebuttal frame: "valuation uplift doesn't compensate for pipeline loss."
3. **Decision Type classification** — fundraise is Type 2 (reversible) but competitive window is Type 1 (irreversible), creating an asymmetric urgency argument.
4. **The trigger context was preserved** — "The $12M trigger was correct when set; the competitive landscape changed" acknowledges the board's prior decision rather than overriding it.

---

## Use Case 3: Decision Brief for Engineering Reorg

### Scenario

A VP of Engineering needs to propose restructuring 4 teams into 3 during a leadership offsite. She has 15 minutes for discussion. One director whose team would be dissolved is present.

### The Prompt

> Write a decision brief for a 15-minute leadership discussion: restructuring from 4 eng teams to 3. One director's team is being dissolved (she'll be reassigned). The director is in the room.

### Without the Skill (Generic AI)

**Engineering Team Restructuring Proposal**

We propose consolidating from 4 to 3 teams to improve velocity and reduce coordination overhead. Team D would be distributed across Teams A, B, and C. Director Chen would take a new role as Principal Engineer...

[Continues with org chart and vague rationale]

### With the Skill

**Context Gate:** Decision Brief — group decision, synchronous (15-minute discussion), multiple stakeholders with conflicting interests.

**Format Routing:** Decision Brief (NOT Board Memo — too long for 15 minutes; NOT One-Pager — needs meeting discussion flow).

**Audience Calibration — The Affected Director:**

| Dimension | Other leaders | Director Chen |
|---|---|---|
| What they hear | "Fewer teams, faster velocity" | "My team is being dissolved" |
| What to address | Efficiency gains, customer impact | Career path, team member placement, her value |
| Risk if not calibrated | Low — they'll support if data is clear | High — public humiliation triggers opposition; she becomes a detractor |

**Pre-meeting action (CRITICAL):** Brief Director Chen 1:1 BEFORE the offsite. She must not learn about this in a room of peers. Frame: "I want to discuss your role in the new structure — your expertise in X makes you the right person to lead Y." If she enters the meeting already briefed and with a clear path forward, she becomes a supporter rather than a victim.

**Decision Architecture:** 2 options (not 3 — adding a "keep 4 teams" option wastes the 15 minutes on status quo defense). Option A: 4→3 with Chen as principal. Option B: 4→3 with Chen leading the merged team.

**Meeting structure (15 minutes):**
1. **Problem (2 min):** "4 teams create 6 handoff points. We shipped 3 features last quarter that should have been 1. Here's the dependency data." (T1)
2. **Proposal (3 min):** The reorg. Chen's new role. Every team member placed.
3. **Options (3 min):** A vs. B. Tradeoffs named.
4. **Discussion (5 min):** Guided by 2 pre-seeded questions.
5. **Decision (2 min):** Vote or consensus.

### What Changed

1. **Pre-meeting action identified as CRITICAL** — briefing the affected director before the offsite prevents public humiliation and converts a potential detractor to supporter.
2. **Audience calibration distinguished what each person HEARS** — "fewer teams" vs. "my team is dissolved" are structurally different messages requiring different frames.
3. **Format Routing selected Decision Brief over Board Memo** — 15 minutes requires a compressed, meeting-optimized format.
4. **Meeting structure with minute-by-minute timing** — 15 minutes doesn't allow wandering. Every minute allocated.
5. **2 options, not 3** — "keep 4 teams" wastes time defending status quo. Both options accept the restructure and differ on Chen's role.

---

*Generated using Executive Writing skill v2.0.0 | PM Skills Arsenal*
