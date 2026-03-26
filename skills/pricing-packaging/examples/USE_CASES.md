# Use Cases: Pricing & Packaging

> Three real-world scenarios demonstrating the transformation from generic AI output to skill-powered pricing analysis. Each use case showcases different frameworks and capabilities from the Pricing & Packaging skill (v2.0.0).

---

## Use Case 1: "AI Code Review Tool Transitioning From Flat-Rate to Usage-Based Pricing"

### Scenario

You are the Head of Product at CodeLens AI, an AI-powered code review tool with $4.8M ARR and 8,200 paying customers on a flat $49/month plan. The product uses LLM inference to review pull requests, catching bugs, security vulnerabilities, and code quality issues. The problem: the top 10% of users (820 accounts, 500+ reviews/month) consume 62% of AI compute but pay the same as casual users doing fewer than 20 reviews/month. At $0.03 per AI review, power users cost $15+/month in marginal inference — a 31% cost-of-revenue on a $49 price point — while casual users cost under $0.60/month. The flat rate is structurally broken. You need a full pricing redesign.

### The Prompt

> CodeLens AI has $4.8M ARR, 8,200 customers, flat $49/month pricing. AI code review costs $0.03 per review. Top 10% do 500+ reviews/month ($15+ in AI cost on a $49 plan). Bottom 50% do <20 reviews ($0.60 cost) but find $49 expensive. Redesign our pricing: model selection, tier structure, migration strategy.

### Without the Skill (Generic AI)

**Pricing Redesign for CodeLens AI**

You should move to a tiered pricing model based on usage:

**Suggested tiers:**
- **Free:** 10 AI reviews/month, 1 repo
- **Pro:** $39/month, 200 AI reviews, unlimited repos
- **Enterprise:** $99/month, unlimited reviews, priority support, SSO

**Rationale:** The free tier drives acquisition, Pro captures the majority, and Enterprise serves power users. Usage-based pricing aligns cost with value.

**Migration:** Grandfather existing users for 3 months, then move them to the tier that matches their usage. Offer an annual discount to reduce churn.

**Risks:** Some users may churn when they see limits. Communicate the value of the new tiers clearly.

### With the Skill

**Pricing Strategy: CodeLens AI — From Flat-Rate to Hybrid**

> **Confidence band:** M-H (55-80%) | **Staleness window:** Reassess if GitHub Copilot launches full AI code review or if AI inference costs change >30%

**Context Gate: Is This a Pricing Problem?**

| Gate | Assessment | Result |
|---|---|---|
| Core problem actually about pricing? | Yes — margin compression from AI costs at high usage, revenue under-realization from power users, flat model misaligned with variable cost (T1) | Proceed |
| Evidence about what customers value? | Yes — 8,200 customers, usage data segmented by review volume, 47 customer interviews (T1-T3) | Proceed |
| Cost structure known? | Yes — $0.03/review (GPU inference), $0.002/static analysis, $8.50/mo fixed infrastructure per account (T1) | Proceed |
| Pricing or positioning decision? | Pricing — competitive position established, PMF validated (92% monthly retention) | Proceed |

**Usage Distribution — The Structural Problem**

| Segment | % of Base | Accounts | Monthly Reviews | AI Cost/Account | Revenue | Margin |
|---|---|---|---|---|---|---|
| Power Users | 10% | 820 | 500-2,000+ | $15.00-$60.00 (T1) | $49/mo | $49 - $15 to **-$11 = negative at top end** |
| Regular Users | 40% | 3,280 | 50-200 | $1.50-$6.00 (T1) | $49/mo | $34.50-$39.00 |
| Casual Users | 50% | 4,100 | <20 | $0.06-$0.60 (T1) | $49/mo | $39.90-$40.44 |

**Key insight:** The top ~200 accounts (2.4% of base) doing 1,000+ reviews/month are **margin-negative** — CodeLens pays $19.50 per month to serve them. Meanwhile, 4,100 casual users cross-subsidize power users while perceiving $49 as too expensive for their light usage.

**Step 1: Pricing Model Selection**

| Criterion | Flat-Rate (Current) | Per-Seat | Pure Usage | Hybrid (Base + Usage) |
|---|---|---|---|---|
| Value alignment | None — same price for 5 and 2,000 reviews (T1) | Partial — value is per-review, not per-seat (T4) | Strong — scales with value (T4) | **Strong — base covers platform, usage covers AI** (T4) |
| Cost structure fit | Poor — variable costs, fixed revenue (T1) | Poor — AI cost is per-review (T1) | Strong — cost and revenue scale together (T1) | **Strong — base covers fixed, usage covers variable** (T1) |
| Buyer predictability | High (T1) | High (T4) | Low — variable bills cause anxiety (T3) | **Medium — predictable base + capped overage** (T4) |
| Expansion mechanic | None (T1) | Seats only (T4) | Natural — more usage = more revenue (T4) | **Both tier upgrades and usage growth** (T4) |
| Competitive norm | Common for simple tools (T2) | Common in dev tools (T2) | Emerging for AI tools (T2) | **Industry trend (Copilot, Cursor)** (T2) |
| **Overall Fit** | **Poor** | Workable | Workable | **Strong Fit** |

**Selected: Hybrid (Base Platform + Usage Overage)** (H) — because CodeLens delivers two types of value: the platform (dashboard, configuration, integration) justifying a base fee, and AI reviews with variable cost/value justifying usage pricing. Pure usage rejected for budget unpredictability; per-seat rejected because value is per-review.

**O->I->R->C->W:**
- **O** [T1]: 100x usage disparity (5 to 2,000+ reviews/month) with $0.03/review variable cost on flat pricing.
- **I**: Flat pricing creates a structural margin trap — as product improves and power users review more, margins compress. Growth in usage = growth in losses on top 10%.
- **R**: Adopt Hybrid (Base + Usage). Each tier includes review allotment; overages per-review. Base covers platform costs + margin; usage covers AI costs + margin.
- **C**: H — usage data (T1), cost structure (T1), competitive norm (T2: Copilot, Cursor adopt hybrid).
- **W**: If >15% express strong negative reaction to metering in beta rollout, raise included allotments.

**Step 2: WTP Assessment (Van Westendorp, n=47)**

| Metric | Value | Interpretation |
|---|---|---|
| Point of Marginal Cheapness (PMC) | $31/mo | Price floor — below this, buyers question AI quality (T3) |
| Optimal Price Point (OPP) | $58/mo | Least resistance — market "sweet spot" for mid-tier (T3) |
| Indifference Price Point (IDP) | $72/mo | Market normative — what customers consider "the going rate" (T3) |
| Point of Marginal Expensiveness (PME) | $119/mo | Price ceiling — above this, demand drops sharply (T3) |

**Key finding:** CodeLens is underpriced. OPP ($58) is 18% above current ($49). IDP ($72) is 47% above. **We are leaving $1.6M+ in annual revenue on the table** (H).

**Value anchor:** When asked "what would you do without CodeLens?", top response: add one more senior engineer to review rotation ($12,000/month fully loaded, T3). CodeLens at $69-$149/month is a 99% cost reduction — strong pricing power.

**Step 3: Competitive Pricing Map**

| Competitor | Model | Entry | Mid Tier | AI Reviews? |
|---|---|---|---|---|
| SonarQube Cloud | Tiered + LOC | Free | $30/mo | Static only (T1) |
| Codacy | Per-seat | Free | $15/user/mo | Basic ML (T1) |
| Snyk Code | Per-seat + usage | Free | $52/dev/mo | AI security (T1) |
| GitHub Copilot (Review) | Per-seat (bundled) | $19/mo | $39/user/mo | PR review — new (T2) |
| Cursor | Usage-based | $20/mo | $40/mo | Full AI (T1) |
| **CodeLens (Current)** | **Flat** | **$49** | **$49** | **Full AI** |
| **CodeLens (Proposed)** | **Hybrid** | **$29** | **$69** | **Full AI** |

**Reference Price Effect:** Engineering managers compare against (1) GitHub Copilot at $19-$39/mo — but this is coding assistant, not review tool, so imprecise, and (2) senior engineer time on review — $2,400-$3,600/month. CodeLens at $69 (proposed Pro) is 97-98% cheaper than the human alternative. Reference price strongly supports premium positioning (T3).

**Step 4: Good/Better/Best Package Architecture**

| Dimension | Starter ($29/mo) | Professional ($69/mo) | Enterprise ($149/mo) |
|---|---|---|---|
| Target persona | Solo devs, freelancers | Small-mid teams (2-20 devs) — **TARGET TIER** | Mid-market/enterprise (20+ devs) |
| AI reviews included | 50/month | 250/month | 1,000/month |
| Overage rate | $0.15/review | $0.12/review | $0.08/review |
| Repos | 3 | Unlimited | Unlimited |
| AI model | Standard | Advanced | Advanced + custom fine-tuned |
| Review depth | Single-file | Cross-file + dependency | Full codebase + architecture |
| Security scanning | No | OWASP Top 10 | Full SAST + compliance |
| Team features | No | Dashboard, shared rules | + SSO, SAML, audit logs, RBAC |
| Upgrade trigger | Hits 50-review limit; needs more repos | Needs SSO/compliance; hits 250; 20+ devs | N/A (expansion via usage) |

**Feature allocation rationale:**
- **50 on Starter**: Enough for solo dev at 2-3 PRs/day. 50 x $0.03 = $1.50 cost. Margin: 89% (T1).
- **250 on Professional**: Covers 80% of small-team usage (median 120-180, T1). $69 at 250 = $0.276/review — 4.6x markup on AI cost.
- **1,000 on Enterprise**: Covers all but top 2%. At $149 + overage, even 2,000-review account pays $229/mo — still margin-positive (T1).
- **Security gated to Pro+**: Highest-value feature (prevents $2K-$10K incidents). 68% cited "must-have" (T3). Strongest upgrade trigger.

**Margin Analysis:**

| Metric | Starter ($29) | Professional ($69) | Enterprise ($149) |
|---|---|---|---|
| AI cost (max included) | $1.50 | $7.50 | $30.00 |
| Infrastructure | $8.50 | $8.50 | $12.00 |
| Support | $0.50 | $2.00 | $15.00 |
| **Total COGS** | **$10.50** | **$18.00** | **$57.00** |
| **Gross margin** | **64%** | **74%** | **62%** |

All tiers maintain 62%+ margin even at max included usage. Current flat model has blended 52% margin hiding margin-negative accounts.

**Step 5: Sensitivity Analysis**

| Pro Price Scenario | Pro Customers | Total ARR | vs. Current $4.8M |
|---|---|---|---|
| $48 (-30%) | 3,600 | $5.4M | +12% |
| $55 (-20%) | 3,400 | $5.9M | +23% |
| **$69 (recommended)** | **3,100** | **$7.4M** | **+54%** |
| $76 (+10%) | 2,800 | $7.2M | +50% |
| $90 (+30%) | 2,200 | $6.5M | +35% |

**Revenue is robust across the range.** Any Pro price between $48-$90 produces meaningfully higher ARR than current. Even worst case (15% churn, heavy Starter skew, Copilot competes directly) produces $5.6M — still 17% above current.

**Step 6: Revenue Impact**

| Metric | Current (Flat $49) | Projected (Hybrid) | Delta |
|---|---|---|---|
| Customers | 8,200 | 7,544 (8% migration churn) | -656 |
| ARPU | $49/mo | $81.72/mo (blended) | +$32.72 (+67%) |
| ARR | $4.82M | $7.40M | +$2.58M (+54%) |
| Gross margin | 52% | 68% | +16 pts |
| Margin-negative accounts | ~200 | 0 | Eliminated |

**Migration Strategy (5 phases):**
1. **Day 0**: New pricing for new customers immediately. Existing grandfathered at $49 for 6 months.
2. **Months 1-6**: Usage tracking visible in dashboard ("you used X reviews — see which tier fits").
3. **Month 5**: Personalized emails: "Based on your usage, you'd be on [Tier] at [Price]. Here's your 20% loyalty discount."
4. **Month 7**: Migrate all existing to tier matching 6-month median usage. 20% loyalty discount for 12 months.
5. **Month 19**: Loyalty discount expires. Full pricing for all.

**Critical comparison:** A 2,000-review/month account on flat $49 has **-40% gross margin**. On Enterprise + overage: $229/month at 62% margin. **$180/month swing per account** across ~200 accounts = **$432,000/year in recovered margin.**

**Step 7: AI/SaaS-Specific Patterns**

| Pattern | Assessment | Recommendation |
|---|---|---|
| Value metric | Review count (customers understand "reviews" — not tokens) (T1) | Per-review metering |
| Marginal cost | $0.03/review at median; unsustainable above 400 reviews on flat (T1) | Usage component mandatory |
| GPU cost trajectory | Declining ~30%/yr (T4) | Do NOT pass savings through — capture as margin |
| Bundle vs. unbundle AI | AI IS the product — gate model quality by tier (T4) | Standard/Advanced/Custom across tiers |

**Assumption Registry**

| # | Assumption | Confidence | Evidence | Invalidation Signal |
|---|---|---|---|---|
| 1 | Power users accept $149+ because value justifies it | M | 11/15 said $100-$200/mo (T3); reference = $12K/mo engineer (T4) | >25% power users churn within 3 months |
| 2 | Casual users won't churn en masse at usage limits | M | 8/12 said $29 "more reasonable" (T3); 50 reviews covers median (T4) | Casual churn exceeds 15% months 7-9 |
| 3 | AI inference costs won't increase materially | H | GPU costs declining ~30% YoY (T4) | Supply shock doubles costs |
| 4 | GitHub Copilot won't ship full AI review at $39/user in 6 months | L | Copilot review in beta, limited (T2) | Copilot ships full review bundled in Business |
| 5 | 6-month grandfather sufficient for migration | M | Industry 3-6 months standard (T4); customers said "at least 3" (T3) | NPS drops >15 points during grandfather |

**Cross-Framework Contradictions**

| Contradiction | Framework A | Framework B | Resolution |
|---|---|---|---|
| WTP vs. Competitive Map on Pro price | WTP: OPP $58, IDP $72 — price at $58-72 | Competitive: Snyk $52, Copilot $39 — price at $39-52 | **Weight WTP.** CodeLens is differentiated; reference price already incorporates competitive awareness. Price at $69 and compete on value. |
| Package vs. AI Cost on Starter allotment | Package: deliver enough value for habit (100+ reviews) | AI Cost: $3.00 at 100 reviews on $29 — margin drops | **Weight AI Cost.** 50 reviews enough for solo dev habit. If data shows limit not triggering upgrades, raise to 75. |
| Sensitivity vs. Migration on timing | Sensitivity: every month at $49 = $214K foregone | Migration: 6-month grandfather reduces churn from 12% to 8% | **Weight Migration.** $1.3M foregone during grandfather is retention investment. Losing 4% more of base costs more over lifetime. |

**Adversarial Self-Critique**

**Weakness 1: Overage pricing may suppress usage growth.** Metered pricing creates "meter anxiety" — developers reduce reviews to avoid charges. If growth thesis depends on teams reviewing MORE code over time, overage creates counter-incentive. 14/47 cited "predictable billing" as top-3 criterion (T3). Mitigation: set allotments so 70-80% never hit overages. Monitor: if avg reviews/account drops >10% post-migration.

**Weakness 2: Revenue projections rest on tier mix assumptions with no historical precedent.** 40/38/22 split is current usage mapped to new thresholds, but behavior changes when pricing changes. If actual split is 55/30/15 (heavy Starter skew), ARR drops to $5.8M. Mitigation: 90-day A/B test with 50% of new signups before committing to migration.

**Weakness 3: The $29 Starter may cannibalize Pro.** Regular users at $49 may discover they can survive on 50 reviews by being selective. Downgrade from $49 to $29 = -$20/account. If 20% of regulars do this, $157K/year in revenue loss. Mitigation: gate security and cross-file analysis to Pro — team features drive upgrade.

### What Changed

- **Model Selection Matrix evaluated 4 pricing models on 6 criteria** with evidence tiers — producing Hybrid as the clear winner, vs. "move to tiered pricing" without structural analysis.
- **Van Westendorp WTP quantified the acceptable price range** ($31-$119) and identified CodeLens as underpriced (OPP $58 vs. $49 current) with $1.6M+ in revenue left on the table.
- **Competitive Pricing Map with price-value positioning** showed CodeLens positioned as AI-native but priced like static analysis — headroom for premium pricing.
- **Good/Better/Best with margin analysis per tier** showed all tiers at 62%+ margin with feature allocation rationale (security gated to Pro as strongest upgrade trigger).
- **Sensitivity analysis stress-tested across a 60% price range** showing $48-$90 Pro all produce higher ARR than current — robust recommendation.
- **Migration strategy with 5 phases** including personalized emails based on actual usage, grandfather period, and loyalty discount — vs. "grandfather for 3 months then move them."
- **AI/SaaS-specific patterns** addressed the unique challenges of variable AI inference costs — per-review metering, GPU cost trajectory capture, model quality gating by tier.

---

## Use Case 2: B2B SaaS Platform Adding an Enterprise Tier

### Scenario

A $15M ARR B2B analytics platform with 400 mid-market customers ($3,125 average ACV) wants to add an Enterprise tier. Several prospects have asked for SSO, dedicated support, and custom integrations, but the company has no enterprise pricing experience. Current pricing: $199/mo Standard, $399/mo Professional.

### The Prompt

> $15M ARR analytics platform, 400 customers, $199/399 tiers. Enterprise prospects asking for SSO, dedicated support, custom integrations. Design the Enterprise tier: price, packaging, what to gate, migration for existing customers who need enterprise features.

### Without the Skill (Generic AI)

Add an Enterprise tier at $999/month with SSO, dedicated CSM, custom integrations, and advanced analytics. Offer annual contracts only. Require a minimum 50-seat commitment. Create a "Contact Sales" page.

### With the Skill

**Context Gate:** This is a packaging extension, not a full pricing redesign. Current $199/$399 tiers are working (validation: 400 customers, low churn). The question is what goes in the Enterprise tier and what gets removed from Professional.

**WTP Assessment (n=18 enterprise prospects):**

| Metric | Value | Evidence |
|---|---|---|
| PMC (floor) | $599/mo | Below this, enterprise buyers question whether it's "real enterprise" (T3) |
| OPP (sweet spot) | $899/mo | Least resistance in enterprise buyer interviews (T3) |
| PME (ceiling) | $1,499/mo | Above this, procurement triggers a competitive evaluation (T3) |

**Good/Better/Best Extension:**

| Feature | Standard ($199) | Professional ($399) | Enterprise ($899) |
|---|---|---|---|
| SSO/SAML | No | No | Yes |
| Dedicated CSM | No | Email support | Named CSM + Slack channel |
| Custom integrations | No | No | 2 included |
| SLA | Best effort | 99.5% | 99.9% with credits |
| Data retention | 12 months | 24 months | Unlimited |
| **Upgrade trigger** | — | SSO requirement | Compliance + dedicated support need |

**Critical decision — what to REMOVE from Professional:** SSO must NOT be in Professional. If enterprise buyers get SSO at $399, the $899 tier loses its strongest forcing function. 78% of enterprise RFPs require SSO (T2) — it is THE gate between mid-market and enterprise pricing.

**Revenue impact:** If 40 of 400 customers (10%) upgrade to Enterprise at $899: +$240K ARR (+1.6%). If Enterprise attracts 20 net-new enterprise customers in year 1: +$215K ARR. Combined: +$455K ARR (3% lift) with pathway to $2M+ as enterprise motion matures.

**Migration:** Existing Professional customers using SSO-adjacent features (API keys, IP allowlisting) get a 60-day "Enterprise Preview" with a 25% first-year discount. Frame as "unlocking capabilities your plan doesn't include" not "removing features."

### What Changed

1. **Context Gate correctly scoped this as a tier extension, not a full redesign** — preventing unnecessary disruption to working $199/$399 tiers.
2. **WTP with enterprise-specific floor and ceiling** — $599 floor prevents the "is this real enterprise?" perception; $1,499 ceiling avoids triggering competitive evaluations.
3. **Feature gating strategy identified SSO as the critical forcing function** — 78% of enterprise RFPs require it, making it the single strongest upgrade trigger.
4. **Revenue impact modeled both upgrade and net-new paths** with conservative assumptions.
5. **Migration framed as "unlocking" not "removing"** — psychological reframing reduces churn risk.

---

## Use Case 3: Usage-Based Pricing for an AI Writing Assistant

### Scenario

An AI writing assistant ($2M ARR, 5,000 users) charges $29/month flat. AI costs are $0.08 per 1,000 tokens generated. Power users generate 500K+ tokens/month ($40 in AI cost on a $29 plan). The CEO wants to move to usage-based pricing without killing the product-led growth motion.

### The Prompt

> AI writing assistant, $2M ARR, 5,000 users, $29/mo flat. AI cost: $0.08/1K tokens. Power users do 500K+ tokens ($40 cost on $29 plan). Move to usage-based without killing PLG growth.

### Without the Skill (Generic AI)

Offer a free tier with 10,000 tokens/month, a $19 plan with 100,000 tokens, and a $49 plan with 500,000 tokens. Charge $0.10 per 1,000 tokens above the limit.

### With the Skill

**Context Gate flag:** The ask says "usage-based" but the real problem is margin protection. Pure usage-based kills PLG because variable bills create signup friction. The correct model is **hybrid with generous included allotments** — users feel flat-rate, power users pay for excess.

**Model Selection:** Hybrid wins over pure usage. The PLG motion depends on "sign up and get immediate value" — a calculator at signup kills conversion. Include enough tokens that 80% of users never see a meter.

**Recommended structure:**

| Tier | Price | Tokens Included | Overage | Target |
|---|---|---|---|---|
| Free | $0 | 5,000/mo | Hard cap | Try before buy |
| Starter | $19/mo | 50,000/mo | $0.12/1K tokens | Casual writers |
| Pro | $39/mo | 200,000/mo | $0.10/1K tokens | Daily writers — **TARGET** |
| Team | $79/mo | 500,000/mo | $0.08/1K tokens | Teams + power users |

**Key design decision:** Overages priced at DECLINING rates per tier. Power users on Team at $0.08/1K tokens pay exactly at cost for excess — margin comes from the $79 base. This prevents "penalty for using the product" perception while protecting margin.

**AI cost sensitivity:** If token costs drop 30% (from $0.08 to $0.056/1K), do NOT lower prices. Capture as margin improvement from 52% blended to 64% blended. Margin expansion funds product development.

**Migration:** Existing $29 users mapped to Starter ($19) or Pro ($39) based on 90-day usage median. Users below 50K tokens/month get a price DECREASE — frame as "we're rewarding light users." Users above get Pro with first 3 months at $29 (loyalty bridge).

### What Changed

1. **Context Gate reframed from "usage-based" to "hybrid with generous allotments"** — preserving PLG while fixing margin.
2. **Declining overage rates by tier** — prevents "penalty for using" perception; power users pay at-cost for excess with margin from base.
3. **Migration creates winners** — 60%+ of users get a price decrease, making the change a positive story.
4. **AI cost sensitivity captured as margin** — not passed through to customers.

---

*Generated using Pricing & Packaging skill v2.0.0 | PM Skills Arsenal*
