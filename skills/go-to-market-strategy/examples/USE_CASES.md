# Use Cases: Go-to-Market Strategy

> Three real-world scenarios demonstrating the transformation from generic AI output to skill-powered GTM analysis. Each use case showcases different frameworks and capabilities from the Go-to-Market Strategy skill (v2.0.0).

---

## Use Case 1: "E-Commerce Pricing Analytics Tool Launching Into Mid-Market"

### Scenario

You are the CEO/co-founder of PriceScope AI, launching a pricing analytics tool for mid-market e-commerce companies ($10M-$200M GMV). These businesses are large enough that pricing mistakes cost them six figures per year, but too small to hire pricing teams or afford $100K+/yr enterprise platforms. Your product uses ML to analyze competitor pricing, model price elasticity, and recommend dynamic pricing rules. You have a $500K first-year budget, a 3-person team, and need a full GTM strategy: who to target, how to reach them, what order to launch, and when to stop.

### The Prompt

> We're launching PriceScope AI — a pricing analytics tool for mid-market e-commerce ($10M-$200M GMV). ML-powered competitor monitoring, elasticity modeling, and dynamic pricing recommendations. $500K first-year budget, 3-person team. Build the full GTM strategy.

### Without the Skill (Generic AI)

**Go-to-Market Plan for PriceScope AI**

**Target Market:** Mid-market e-commerce companies looking for better pricing tools.

**Key Segments:**
1. Shopify merchants with 500+ products
2. Amazon sellers looking for repricing automation
3. DTC brands with promotional pricing needs

**Go-to-market approach:**
- Build a freemium product to acquire users
- Create content about e-commerce pricing best practices
- Attend 2-3 e-commerce conferences (ShopTalk, IRCE)
- Partner with Shopify agencies for distribution
- Launch on Product Hunt for initial visibility

**Pricing:** $99-$499/month based on product count and features.

**Metrics to track:** MRR, customer count, churn rate, CAC, LTV

**Timeline:**
- Month 1-2: Finish product, create website
- Month 3-4: Beta with 10-20 customers
- Month 5-6: Public launch, start content marketing
- Month 7-12: Scale marketing, optimize conversion

The $500K should be allocated roughly as: 40% product development, 30% marketing, 20% sales/support, 10% buffer.

### With the Skill

**GTM Strategy: PriceScope AI — Mid-Market E-Commerce Pricing Intelligence**

> **Confidence band:** M-H (55-75%) | **Staleness window:** Reassess if Competera announces a mid-market tier or Prisync ships elasticity modeling before GA

**Executive Summary**

The window is open now because three forces are converging: ML inference costs dropped 85% in 18 months (T1: making real-time pricing viable at mid-market price points), Amazon's algorithmic pricing is forcing smaller retailers to respond (73% cite pricing as #1 threat, T2: Feedvisor Survey), and the two dominant platforms (Prisync, Competera) are focused elsewhere — Prisync hasn't shipped a major feature in 8 months (T1: changelog), Competera raised $30M for enterprise-only expansion (T2). Target: 40 paying customers and $360K ARR by month 12, with kill criteria at each phase. **Recommended action: proceed with launch into Shopify Plus beachhead; the market is ready, the product is specced, and the competitive vacuum is real.**

**Step 0: Context Gate**

| Check | Status | Evidence |
|---|---|---|
| Problem validated? | Pass | 12 interviews with Shopify Plus merchants; 9/12 cited "pricing is manual and we know we're leaving money on the table" (T2) |
| Product exists? | Pass | MVP in development; competitor monitoring module working in alpha (T1) |
| Competitive landscape known? | Pass | 5 competitors mapped: Prisync, Competera, Intelligence Node, Price2Spy, manual spreadsheets (T1) |

**Framework Selection**

| Category | Frameworks | Rationale |
|---|---|---|
| Primary | Market Entry Thesis, Segment Selection & ICP Scoring, Channel Strategy with Unit Economics, Launch Sequencing & Gating | Core GTM frameworks for new market entry with constrained budget |
| Supporting | Competitive Positioning (Dunford), Distribution & Growth Mechanics | Positioning critical for differentiation; growth mechanics for PLG design |
| Skipped | Full competitive war map (7 Powers, Aggregation Theory) | Not load-bearing — question is how to enter, not who wins long-term |

**1. Market Entry Thesis: Why This Market, Why Now**

The structural opportunity is the mid-market gap: ~14,000 merchants in the US with $10M-$200M GMV (T4: Census data) are systematically underserved. Enterprise (>$200M) has Competera at $100K+/yr. SMB (<$10M) has Prisync at $99-$399/mo for monitoring only. Mid-market is too large for spreadsheets (losing $200K-$2M/yr on pricing inefficiency) and too small for enterprise platforms.

| Timing Signal | Evidence | Confidence |
|---|---|---|
| ML inference cost collapse | 85% drop in 18 months; enables elasticity modeling at $500-$1,500/mo (T1) | H |
| Amazon algorithmic pressure | 2.5M price changes/day; 73% cite pricing as #1 threat (T2-T3) | H |
| Incumbent distraction | Competera $30M Series B enterprise-only (T2); Prisync no major updates 8 months (T1) | M |
| Shopify Plus maturation | 50,000+ merchants; app ecosystem mature; Shopify Flow enables automated rules (T2) | H |

**The Wedge:** Counter-positioning against enterprise incumbents. Competera cannot profitably serve $500-$1,500/mo without cannibalizing $100K+ deals. Their 6-month implementation cycles are structurally incompatible with mid-market economics (H). **Enterprise-grade pricing intelligence at mid-market price points, deployed through self-serve PLG, not enterprise implementation.**

| Wedge Dimension | Assessment | Evidence |
|---|---|---|
| Time to replicate | 12-18 months | ML models require 6-12 months training data; Shopify integration 3-4 months (T3) |
| Capital to replicate | $2M-$5M | Data pipeline + ML + integration + GTM (T4) |
| Structural barrier | Counter-positioning | Enterprise incumbents can't serve $750/mo with $50K+ CAC cost structure (T3) |
| Verdict | Speed-dependent, 18-month window | M |

**Decision: GO.** Market ready + product in alpha. Begin GTM execution now; build pipeline during product development.

**O->I->R->C->W:**
- **O** [T2, T3]: Mid-market merchants lose $200K-$2M/yr on pricing inefficiency, but enterprise tools cost $100K+/yr and SMB tools lack ML recommendations.
- **I**: A clear pricing gap exists: the $500-$1,500/mo band has zero solutions combining monitoring + elasticity + dynamic pricing.
- **R**: Launch PriceScope AI with Shopify Plus integration, targeting $750/mo ACV. Free tier for monitoring (acquisition engine), paid for elasticity + dynamic pricing. Begin content marketing immediately; hire 1 content marketer within 30 days. Owner: CEO. Timeline: Beta 90 days, GA 180 days.
- **C**: H — assumes ML inference costs stay flat (T1) and Competera doesn't launch mid-market tier (M).
- **W**: If Competera announces mid-market product or Prisync ships elasticity modeling before GA, accelerate timeline or pivot wedge to vertical-specific.

**2. Segment Selection: Shopify Plus Fashion/Apparel Is the Beachhead**

| Criterion | Weight | A: Shopify Plus Fashion | B: BigCommerce Electronics | C: DTC Health/Beauty |
|---|---|---|---|---|
| Acute pain (validated) | 25% | 5/5 (T2) — 9/12 interviews; seasonal markdown timing top pain | 4/5 (T3) — Amazon pressure documented | 3/5 (T3) — promotional complexity, less urgency |
| Willingness to pay | 20% | 5/5 (T2) — 7/12 would pay $500-$1,000/mo; 3 said "immediately" | 3/5 (T4) — electronics margins thin (8-15%) | 4/5 (T3) — accustomed to analytics tooling |
| Accessibility | 20% | 5/5 (T1) — Shopify Plus directory public; fashion communities active | 3/5 (T3) — less centralized ecosystem | 4/5 (T3) — DTC communities active but fragmented |
| Reference-ability | 15% | 5/5 (T3) — fashion founders highly networked; speak at ShopTalk, IRCE | 3/5 (T4) — competitive secrecy | 4/5 (T3) — vocal but may not share pricing tools |
| Expansion potential | 10% | 4/5 (T4) — fashion -> all Shopify -> BigCommerce -> enterprise | 3/5 (T4) — platform-specific | 3/5 (T4) — different buying motion |
| Competitive vacuum | 10% | 5/5 (T1) — no ML elasticity for Shopify Plus at <$2K/mo | 4/5 (T3) — Amazon tools partially serve | 3/5 (T3) — Triple Whale adding pricing |
| **Weighted Score** | | **4.85** | **3.35** | **3.55** |

**Beachhead: Segment A — Shopify Plus Fashion/Apparel.** Scores 4.85/5.0. Highest validated pain, strongest WTP, most accessible, most reference-able.

**Expansion Path:**
```
Beachhead              Adjacent 1                Adjacent 2           Mainstream
Shopify Plus Fashion   All Shopify Plus          BigCommerce+Custom   Enterprise ($200M+)
~3,200 merchants       ~50,000 merchants         ~25,000 merchants    ~5,000 accounts
$750/mo ACV            $750-$1,000/mo            $1,000-$1,500/mo     $2,000-$5,000/mo

Trigger: 50%+ share    Trigger: 80+ customers,   Trigger: Platform-   Trigger: Product
in fashion, 15+        3+ non-fashion refs,       agnostic data layer  handles >50K SKUs
case studies           supports >5K SKUs          complete             dedicated CS team
```

**3. Channel Strategy: Content-Led PLG at $500K**

| Channel | CAC (est.) | Payback | LTV/CAC | Scalability | Evidence |
|---|---|---|---|---|---|
| Content/SEO + PLG free tier | $1,800 (T3) | 2.4 mo (T4) | 8.3:1 (T4) | H | Fashion audiences consume pricing content (T3) |
| E-commerce agency partnerships | $2,400 (T4) | 3.2 mo (T4) | 6.3:1 (T4) | M | 3-6 months to establish (T3) |
| Shopify App Store | $900 (T3) | 1.2 mo (T3) | 16.7:1 (T3) | L | 20% rev share + algorithm-dependent (T1) |
| Outbound (email/LinkedIn) | $3,200 (T4) | 4.3 mo (T4) | 4.7:1 (T4) | M | Volume limited by team size |
| Paid acquisition | $4,800 (T3) | 6.4 mo (T4) | 3.1:1 (T4) | H | Too expensive at current ACV |
| Direct sales | $12,000+ (T4) | 16+ mo (T6) | 1.3:1 (T6) | M | CAC exceeds first-year ACV — structurally unviable |

[EVIDENCE-LIMITED] Unit economics are modeled (T4), not observed. If actual CAC >2x modeled ($3,600+), re-evaluate channel viability.

**Conversion Funnel (Content/PLG):**

| Stage | Volume (monthly) | Conversion | Cumulative CAC |
|---|---|---|---|
| Awareness (SEO impressions) | 50,000 (T4) | 2.5% CTR | $1.60/visitor |
| Interest (site visits) | 1,250 | 8% signup | $25/signup |
| Trial (free tier) | 100 | 60% connect store | $42/activated |
| Activation (first insight) | 60 | 25% upgrade | $187/activated |
| Paid conversion | 15 | — | **$187/customer** (CAC) |

**Channel Sequencing & Budget:**

| Phase | Channel | Budget | Gate to add next |
|---|---|---|---|
| Phase 1 (months 1-6) | Content/SEO + PLG | $180K | CAC <$2,500 on 25+ conversions |
| Phase 2 (months 4-9) | Add: agency partnerships | $120K | 5+ partners; >=10 referrals |
| Phase 3 (months 7-12) | Add: Shopify App Store | $80K | Listing approved; 4+ stars |
| Reserve | Buffer | $120K | Released only if Phase 1 economics proven |

**4. Launch Sequencing: 5 Phases, Each Gated**

| Phase | Duration | Gate Criteria (ALL must pass) | Kill Criteria (ANY = stop) |
|---|---|---|---|
| Alpha | Weeks 1-4 | Monitoring 95%+ accurate; elasticity runs on 1K+ SKUs; OAuth <30s; no P0 bugs | ML accuracy <80% backtested; API limits prevent >500 SKU monitoring |
| Closed Beta | Weeks 5-12 | 8/10 connect store in 48h; 7/10 "useful" after 2 weeks; NPS >=40; >=5 willing to pay $500+ | <5/10 connect; 0 willing to pay; "what do I do with this?" |
| Open Beta | Weeks 13-20 | Self-serve 80%+ success; free-to-paid >=15%; support <3/user/month; CAC <$2,500 on 25+ | <50 signups after 4 weeks; conversion <5% after 100 users |
| GA | Weeks 21-36 | 40+ paying; churn <5%; CAC <$2,000; 3+ case studies | **<15 paying after 6 months = KILL.** Churn >12% 3 months; CAC >$5,400 |
| Scale | Month 10+ | LTV/CAC >=3:1 sustained 6 months; non-fashion verticals; agency >=20% | LTV/CAC <2:1 after 200 customers |

**5. Competitive Positioning (Dunford)**

For **mid-market e-commerce brands ($10M-$200M GMV)** who **manage pricing through spreadsheets and gut feel**, **PriceScope AI** is a **pricing intelligence platform** that **tells you exactly what to charge and when**, unlike **enterprise tools (Competera) at $100K+/yr with 6-month implementations**, **PriceScope connects in 5 minutes and delivers recommendations in 24 hours at $750/month.**

**6. Success & Failure Criteria**

| Metric | 6-Month Target | 12-Month Target |
|---|---|---|
| Paying customers | 15 | 40 |
| ARR | $135K | $360K |
| Monthly churn | <6% | <4% |
| Blended CAC | <$2,500 | <$2,000 |
| LTV/CAC | >3:1 | >5:1 |
| NPS | >=40 | >=50 |

**HARD Stops:**
- <50 free signups after 8 weeks of content -> STOP content, pivot to outbound
- <5 merchants connect after 100 signups -> STOP, diagnose (UX or value prop)
- **<15 paying after 6 months -> KILL this GTM motion**
- CAC >3x modeled ($5,400+) after 50+ conversions -> STOP scaling

**7. Growth Flywheel**

```
More merchants connect stores
  -> More pricing data across SKUs/competitors
  -> Better ML models (more training data)
  -> Better recommendations
  -> More success stories (case studies, word-of-mouth)
  -> More merchants connect <- flywheel completes

DATA MOAT: By 100 merchants, PriceScope has data across 50,000+
SKUs and 500+ competitors — a dataset no new entrant can replicate.
```

**Assumption Registry**

| # | Assumption | Confidence | Evidence | Invalidation Signal |
|---|---|---|---|---|
| 1 | Mid-market will pay $500-$1,500/mo | H | 7/12 confirmed (T2) | <10% convert to paid at any price |
| 2 | ML inference costs stay flat or decline | H | 2 years of quarterly reductions (T1) | Provider increases >50% |
| 3 | Competera won't launch mid-market in 12 months | M | $30M Series B enterprise-only (T2); hiring 100% enterprise (T3) | "Competera Lite" announced |
| 4 | Content/SEO generates traffic in 6 months | M | SaaS benchmarks (T3); low-competition keywords (T1) | <5,000 organic visits after 6 months |
| 5 | Fashion/apparel is the right beachhead | H | Highest pain (T2); most accessible (T1); most reference-able (T3) | First 20 beta users disproportionately non-fashion |

**Cross-Framework Contradiction:** Shopify App Store has lowest CAC ($900) but Channel Strategy rejects it as primary — because App Store has low scalability, 20% rev share, and algorithm dependency. **Resolution: weight scalability over CAC.** App Store is Phase 3 supplementary, not primary.

**Adversarial Self-Critique**

**Weakness 1: WTP may be interview bias.** 7/12 said $500-$1,000/mo, but interview WTP is notoriously unreliable. The cohort may be self-selected pricing enthusiasts. If <10% convert to paid, WTP is aspirational.

**Weakness 2: ML model accuracy unproven on real data.** Backtested models always perform worse live. Fashion pricing is influenced by trends and influencer moments no model predicts. If first 3 recommendations lose money, trust is destroyed permanently.

**Weakness 3: 3-person team executing 3 channels.** 8 articles/month + 10 beta partners + agency partnerships + support = something under-resourced. If any two signals appear (content drops below 4/month, agency 0 referrals after 3 months), reduce to ONE channel.

### What Changed

- **Market Entry Thesis with 4 timing signals replaced "target mid-market e-commerce"** — structural explanation of WHY NOW with evidence tiers and confidence levels on each signal.
- **ICP Scoring Matrix with 6 weighted criteria replaced a segment list** — quantified 4.85 vs. 3.35 vs. 3.55 comparison producing a clear beachhead choice.
- **Channel unit economics (CAC/payback/LTV:CAC) replaced "build a freemium product and attend conferences"** — 6 channels evaluated, content/PLG wins at 8.3:1 LTV/CAC, with conversion funnel math.
- **5-phase launch with gate AND kill criteria replaced a vague timeline** — HARD STOP at 15 paying customers after 6 months eliminates the failure mode of spending 12 months hoping.
- **Dunford positioning with battlecards replaced generic "create content"** — specific competitive scripts for spreadsheets (70%), Prisync (20%), and Competera (10%) alternatives.
- **Data flywheel design replaced "build integrations"** — each merchant improves ML models for all other merchants, creating a compounding advantage no new entrant can replicate without first acquiring 100 merchants.

---

## Use Case 2: Enterprise SaaS Expanding Upmarket

### Scenario

A $25M ARR project management platform with 1,200 mid-market customers wants to move into enterprise (1,000+ employees). They've won 3 enterprise deals opportunistically. The VP of Sales wants 8 AEs; the CPO wants product changes first (SSO, audit logs). The CEO wants a sequenced GTM strategy.

### The Prompt

> $25M ARR project management platform, 1,200 mid-market customers, 3 organic enterprise wins. VP Sales wants 8 AEs, CPO wants product first. Build the enterprise GTM strategy.

### Without the Skill (Generic AI)

Hire 3-4 enterprise AEs. Build SSO and audit logs in parallel. Target tech companies 1,000-5,000 employees. Price at $15-25/user/month. Create case studies from 3 existing wins. Expect 6-9 month sales cycles. Target 20 enterprise logos in year one.

### With the Skill

**Market Entry Thesis:** The 3 organic wins are demand signals, not GTM validation. Each won through executive champions who bypassed procurement — this doesn't scale (T2: deal analysis). Enterprise requires: (a) product readiness (SSO, SCIM, audit logs — in 85% of RFPs, T2), (b) sales readiness (enterprise AEs with 6-12 month cycles), (c) customer proof (3 logos insufficient — need 8-10 with case studies).

**Segment Selection (ICP Scoring):**

| Criterion | Weight | Tech 1K-5K | Prof. Services 1K-5K | Healthcare 1K-5K |
|---|---|---|---|---|
| Acute pain | 25% | 5/5 (T2) — 3 organic wins, all tech | 3/5 (T3) | 2/5 (T4) |
| WTP | 20% | 5/5 (T1) — $18-25/user/mo benchmark | 4/5 (T3) | 3/5 (T4) |
| Competitive vacuum | 15% | 3/5 (T2) — Asana/Monday Enterprise | 4/5 (T3) | 2/5 (T4) |
| **Weighted Score** | | **4.4** | **3.6** | **2.5** |

**Channel Strategy:** VP Sales is right about AEs but wrong about 8. **Start with 2 AEs + 1 solutions engineer for 6 months. Gate: if pipeline >$2M by month 6, hire 4 more. If <$500K, the product gap — not sales capacity — is the bottleneck.**

**Sequencing (resolves VP Sales vs. CPO tension):** CPO is right that product comes first, but not ALL product. Ship SSO + SCIM months 1-3 (unblocks 85% of RFPs). Audit logs months 4-6. Hire AEs month 2 (3-month ramp = productive month 5, when product is ready).

**Kill criteria:** <3 enterprise deals in pipeline after 6 months -> product gap bigger than SSO/SCIM. Run Problem Framing for enterprise wedge JTBD.

### What Changed

1. **Market Entry Thesis distinguished organic wins from GTM validation** — executive champion bypasses don't scale.
2. **ICP Scoring with weighted criteria** vs. "target tech and professional services."
3. **Channel strategy gated AE hiring** — 2 first, gate to 6 based on pipeline data, vs. "hire 8."
4. **Sequencing resolved the organizational tension** — product first but AE hiring overlaps with build so ramp coincides with readiness.
5. **Kill criteria named** — <3 deals in 6 months means pivot, not "keep trying."

---

## Use Case 3: Developer Tool Community-Led Growth at $3M ARR

### Scenario

A developer observability platform ($3M ARR, 800 free users, 120 paying, 4.2% conversion, NPS 62) wants to 10x growth without hiring sales. Growth is organic word-of-mouth in DevOps communities.

### The Prompt

> $3M ARR developer observability platform. 800 free, 120 paying, 4.2% conversion, NPS 62. Organic growth via DevOps communities. How do we 10x without a sales team?

### Without the Skill (Generic AI)

Improve onboarding to increase conversion. Create more content. Build integrations. Launch a referral program. Build a Discord community. Sponsor conferences.

### With the Skill

**Context Gate flag:** 4.2% conversion with NPS 62 is a diagnostic contradiction. High NPS = users love the product; low conversion = paid tier doesn't justify the price. **This is a packaging problem, not a growth problem.** Fix free-to-paid gate before scaling acquisition.

**Conversion diagnosis (before scaling):**

| Issue | Evidence | Fix |
|---|---|---|
| Free tier too generous | Free includes 80% of features (T1) | Gate alerting rules at 5 on free (most valuable feature per usage data) |
| Activation incomplete | 55% never connect production source (T1) | Guided "connect in 5 minutes" wizard |
| Price anchoring absent | No visible usage meter (T1) | Show "you triggered 12 alerts — upgrade to customize" |

**Market Entry Thesis:** DevOps observability is $7.8B (T4: Gartner), dominated by Datadog ($2.1B ARR). The wedge is NOT "better observability" — it's developer experience at the IC level. Enterprise tools bought by platform teams; your product adopted by individual engineers. **Counter-positioning: Datadog cannot simplify without alienating enterprise buyers.**

**Growth mechanics (after conversion fix):**

| Mechanic | Fit | Investment | Expected Impact |
|---|---|---|---|
| Community-led (Discord + content) | H | $60K/yr | 2x organic signups (T3) |
| Integration marketplace (VS Code, GitHub Actions) | H | $120K (eng) | Each integration = distribution channel (T3) |
| Open-source module strategy | M | $80K (eng) | OSS awareness -> commercial capture (T3) |

**Sequencing:** Fix conversion months 1-3, scale acquisition months 4-12. **Scaling at 4.2% conversion wastes 95.8% of every dollar.** At 8% target, same spend produces 1.9x more paying customers.

### What Changed

1. **Context Gate caught the NPS/conversion contradiction** — the generic output prescribed growth; the skill diagnosed the leaky bucket first.
2. **Conversion diagnosis with 3 specific fixes** replaced "improve onboarding" — free tier gating, activation completion, price anchoring.
3. **Sequencing: conversion before growth** — quantified the waste (95.8% of every dollar at 4.2%).
4. **Counter-positioning identified the structural wedge** — IC-level adoption vs. platform team procurement.

---

*Generated using Go-to-Market Strategy skill v2.0.0 | PM Skills Arsenal*
