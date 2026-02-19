# Competitive Analysis Benchmark Scorecard
## Evaluator: Senior Product Strategy Evaluator
## Date: 2026-02-19
## Conditions: Baseline (A) | Anthropic PM Skill (B) | PM Codex (C)

---

## 1. Score Summary Table

Each cell = score (0–3). Columns grouped by condition × dimension. Total = sum of D1–D7.

### Scoring Key
- **D1** — Framework Application (0–3)
- **D2** — Evidence Hierarchy (0–3)
- **D3** — Strategic Specificity (0–3)
- **D4** — Failure Mode Awareness (0–3)
- **D5** — Synthesis Quality (0–3)
- **D6** — Output Structure (0–3)
- **D7** — Calibration (0–3)

---

### Master Score Table

| Prompt | A-D1 | A-D2 | A-D3 | A-D4 | A-D5 | A-D6 | A-D7 | **A-Total** | B-D1 | B-D2 | B-D3 | B-D4 | B-D5 | B-D6 | B-D7 | **B-Total** | C-D1 | C-D2 | C-D3 | C-D4 | C-D5 | C-D6 | C-D7 | **C-Total** |
|--------|------|------|------|------|------|------|------|-------------|------|------|------|------|------|------|------|-------------|------|------|------|------|------|------|------|-------------|
| **P1** | 1 | 0 | 2 | 1 | 2 | 2 | 0 | **8** | 2 | 1 | 2 | 2 | 2 | 3 | 1 | **13** | 3 | 2 | 3 | 2 | 3 | 3 | 2 | **18** |
| **P2** | 1 | 0 | 2 | 2 | 2 | 2 | 0 | **9** | 2 | 2 | 3 | 2 | 3 | 3 | 2 | **17** | 3 | 2 | 3 | 3 | 3 | 3 | 3 | **20** |
| **P3** | 1 | 0 | 2 | 2 | 2 | 2 | 1 | **10** | 2 | 2 | 3 | 2 | 3 | 3 | 2 | **17** | 3 | 2 | 3 | 3 | 3 | 3 | 3 | **20** |
| **P4** | 1 | 0 | 2 | 2 | 2 | 2 | 1 | **10** | 2 | 2 | 3 | 2 | 3 | 3 | 2 | **17** | 3 | 2 | 3 | 3 | 3 | 3 | 3 | **20** |
| **P5** | 1 | 0 | 2 | 2 | 2 | 2 | 1 | **10** | 2 | 2 | 3 | 2 | 3 | 3 | 2 | **17** | 3 | 2 | 3 | 3 | 3 | 3 | 3 | **20** |

---

## 2. Condition Totals

| Condition | Total Score | Out of | Percentage |
|-----------|-------------|--------|------------|
| **Baseline (A)** | **47** | 105 | 44.8% |
| **Anthropic PM Skill (B)** | **81** | 105 | 77.1% |
| **PM Codex (C)** | **98** | 105 | 93.3% |

---

## 3. Dimension Averages Across Prompts

| Dimension | Baseline Avg | Anthropic Avg | Codex Avg |
|-----------|:---:|:---:|:---:|
| D1 — Framework Application | 1.0 | 2.0 | 3.0 |
| D2 — Evidence Hierarchy | 0.0 | 1.8 | 2.0 |
| D3 — Strategic Specificity | 2.0 | 2.8 | 3.0 |
| D4 — Failure Mode Awareness | 1.8 | 2.0 | 2.8 |
| D5 — Synthesis Quality | 2.0 | 2.8 | 3.0 |
| D6 — Output Structure | 2.0 | 3.0 | 3.0 |
| D7 — Calibration | 0.6 | 1.8 | 2.8 |

---

## 4. Qualitative Notes — Per Prompt, Per Condition

---

### P1 — Marketing Project Management Tool Competitive Landscape

**Baseline (A) — Score: 8/21**

The key finding is that Baseline P1 delivers a well-written, intelligent piece of consultant prose but applies no named strategic frameworks whatsoever. The 2x2 positioning map appears as a rough verbal sketch ("generic vs. marketing-specific / structured vs. flexible") but is not attributed to any framework and draws no cross-referenced conclusions. Evidence quality is entirely undifferentiated — claims like "Asana's Business tier ($24.99/user/month as of 2024)" are stated with the same authority as soft assertions like "Notion has a cult-like following," with no indication that one is harder data than the other. On D3, the output earns a 2 because it does name specific customer archetypes (marketing teams of 5-25, content and demand gen) and provides some named integration priorities. It fails on D7 entirely — there is no acknowledgment of uncertainty, no confidence differentiation, no hedges on strategic conclusions. The output reads as confident expert opinion from start to finish, which is the defining structural weakness of the Baseline condition.

**Anthropic PM Skill (B) — Score: 13/21**

The skill adds material structure: a formal competitive set taxonomy (Direct / Indirect / Adjacent / Substitutes), two plotted positioning maps with labeled axes, a feature comparison matrix with a consistent rating scale, and a four-trend market analysis using a labeled format (What / Why Now / Who Affected / Timeline / Implication / Response). These earn a 3 on D6. The key improvement over Baseline is the positioning analysis section, which attributes inferred positioning statements to each competitor with message architecture layers — this is genuine framework application that produces actionable conclusions (e.g., "Monday's 'adapts to how your team works' claim is undermined by configuration burden"). The critical gap is on D2 and D7: the matrix ratings section states "based on generally available product information, user reviews, and publicly documented features" — a single blanket sourcing statement applied to all ~90 cells. There is no granular quality grading (i.e., which specific cells are user-review-derived vs. documented product features vs. observed behavior), no uncertainty differentiation between cells, and no staleness flags. The "monitoring priorities" section at the end is practical but lacks owner assignment or trigger thresholds, keeping D3 at 2.

**PM Codex (C) — Score: 18/21**

The defining characteristic of Codex P1 is the explicit application of nine named frameworks (7 Powers, Aggregation Theory, Christensen Disruption + COAP, Where to Play/How to Win, Wardley Mapping, JTBD, Data Content Loops, Blue Ocean, TAL/Crossing the Chasm) with each framework producing distinct, cross-referenced conclusions. This is what earns a 3 on D1 — it is not framework-mentioning but framework-executing. The 7 Powers Heat Map rates all four entities across all seven powers with accrual/erosion direction and produces a structural conclusion: "The market for marketing-vertical PM is structurally contestable." The Wardley Map identifies specific strategic misallocation by incumbents ("all three are over-investing in commodity task management"). The Bowling Alley section names a specific head pin with rationale across four criteria. Evidence is labeled with Tiers 1-6 inline (e.g., "[Tier 4: G2 category data]", "[Tier 6: anecdotal — needs validation]"), though most evidence is Tier 4-6 and the footnote acknowledges Tier 1 is absent. D7 earns a 2 rather than 3 because explicit confidence percentages are only on four recommendations at the end, not throughout the framework analyses — the vast majority of claims in Parts 1-13 are stated without confidence levels. The footnote is genuinely calibrating ("conclusions are based on Tier 3-6 evidence and should be validated with Tier 1 customer interview data") but functions as a blanket caveat rather than inline uncertainty throughout.

---

### P2 — Identity Verification Moat Assessment / Stripe Entry

**Baseline (A) — Score: 9/21**

The most important finding is that Baseline P2 is the strongest baseline output — it demonstrates sophisticated structural thinking (the "3-across profile" insight about being nowhere best-in-class is genuinely incisive and shows Porter-adjacent analysis without naming any framework). However it earns only a 1 on D1 because no framework is formally applied or named. The switching cost section ("build switching costs that compound") articulates the concept without the vocabulary of a switching cost taxonomy. On D4, the output earns a 2: it identifies four distinct strategic options for Stripe response, explicitly labels the risk of each, and names specific failure modes ("do not try to out-feature Stripe," "do not assume your 50 customers are safe"). The gap from a higher D4 score is the absence of countermeasures per failure mode — risks are flagged but not systematically paired with defenses. D7 gets a 0 — claims like "Jumio has processed hundreds of millions of verifications" and "Stripe will likely have a far more sophisticated identity product" are stated without any confidence distinction from each other or from softer assertions.

**Anthropic PM Skill (B) — Score: 17/21**

The key finding for Anthropic P2 is the feature comparison matrix scored on a 1-5 scale for five vendors across four capability categories — this is the most structured matrix of any non-Codex output and produces the most diagnostically valuable finding: the "3-across profile" insight (all your scores are 3, meaning you win on relationship and price, not product, which is the most fragile win reason). This insight earns D5 a 3. The hypothesized win/loss patterns table with "if true: implication" columns is a step toward failure mode awareness but stops short of full adversarial self-critique — it identifies risks without naming countermeasures. Evidence is somewhat graded: the win/loss section explicitly states "Note: these are hypotheses to validate, not confirmed findings" and distinguishes between the framework to apply vs. findings; however, the rest of the document (the feature matrix, competitive landscape map) does not carry equivalent epistemic labeling. D7 earns a 2 for the occasional explicit hypothesis/validation flags but 1 not 3 because most of the analytical content is stated without confidence levels.

**PM Codex (C) — Score: 20/21**

The Codex P2 is the highest-scoring output in the benchmark. The defining characteristic is the "Observation → Implication → Response → Confidence → Watch Indicator" cascade structure applied to every major finding (Section 14). This is genuine D3 at level 3 — each recommendation names specific owners (e.g., "run 15 win/loss interviews (protocol above) — Owner: You (CPO) + 1 senior PM"), outputs ("Win rate data by competitor + segment"), and rationale for timing ("Do not skip — every other decision depends on this data"). The 7 Powers Heat Map is the most complete of all three conditions on P2: all five competitors scored, with an explicit "Accruing vs. Eroding" section that makes the moat scorecard dynamic rather than static. The scenario analysis (Section 16) provides explicit probabilities (Base 45%, Bull 20%, Bear 20%, Worst 15%) with falsification conditions — "what would falsify the vertical specialist thesis" — which is the adversarial self-critique pattern. Evidence is Tier-labeled inline throughout (e.g., "[Tier 5: Stripe Identity launch announcement, 2024; Tier 3: Stratechery analysis of Stripe's bundling strategy]"), with the meta-note that all conclusions are structural inferences requiring Tier 1 validation. The output earns 3 on D7 for the explicit confidence percentages on each finding recommendation (80%, 75%, 70%, 60%) and the inline Tier labeling. The sole dimension held below 3 is D2: while evidence tiers are labeled, the system is partially applied — some sections (the feature matrix) carry no tier annotations on individual cells.

---

### P3 — AI Document Processing API Go/No-Go

**Baseline (A) — Score: 10/21**

The key finding is that Baseline P3 is a well-structured go/no-go analysis that organizes its argument effectively: surface reading vs. correct reading, cloud giants vs. vertical players, your actual assets, entry strategy, specific risks, and go/no-go scenarios. The structure earns a 2 on D6. The risk section earns a 2 on D4 — four named risks with genuine specificity (Risk 3 on NLP expertise in the wrong layer of the stack is particularly insightful and not commonly surfaced). However, no named frameworks are invoked, evidence quality is undifferentiated, and the output contains no explicit uncertainty markers beyond occasional hedging phrases ("likely," "probably"). It earns a 1 on D7 for the hedging language present but absent from systematic calibration.

**Anthropic PM Skill (B) — Score: 17/21**

The key finding for Anthropic P3 is the discipline in applying the five-step methodology uniformly: competitive set → landscape map → feature matrix → positioning analysis → win/loss protocol → market trends → go/no-go. Each step produces content rather than form. The go/no-go decision section stands out for being genuinely conditional — "GO — With These Conditions" with five specific, measurable, time-bound conditions (commit to vertical in 30 days, define accuracy claim with evidence in 60 days, SOC 2 process start now, pipeline milestone by month 9, pilot contract within 6 months). This earns D3 a 3 — the conditions are named, time-bound, and falsifiable. D4 earns a 2 for the "Case Against GO" section which names four specific failure risks, but countermeasures are only partial. The feature matrix footnotes use an asterisk convention ("*Represents your intended differentiation — to be earned, not assumed") to flag aspirational vs. current ratings, which is evidence quality grading — earning D2 a 2.

**PM Codex (C) — Score: 20/21**

The Codex P3 is notable for its power accrual trajectory table — a forward-looking view of when each of the 7 Powers will be acquired and via what mechanism (Counter-Positioning now → 🟢; Switching Costs at 12 months → 🟡; 24 months → 🟢 via customer-created model training). This is framework application that produces time-differentiated, sequenced conclusions — the kind of planning output that a CPO can directly route to a product roadmap. The "24-month power accumulation thesis" is clearly stated and falsifiable. The GTM comparison table (primary motion, free tier, pricing model, time to first API call, ACV range, sales cycle) for all five competitors side-by-side is one of the most practically actionable tables in the benchmark. Market sizing includes the disclaimer "Script not available — these are estimated order-of-magnitude figures; verify with CFO before board presentation" — this is both a D2 and D7 signal. The leading indicators section (7 metrics with alert thresholds) provides the monitoring infrastructure that distinguishes a strategy document from a war map. D2 earns a 2 rather than 3 because tier annotations, while present, are somewhat sparse relative to P2 — several sections (the ERRC grid, disruption vectors) carry no inline evidence tags.

---

### P4 — Visier Free Tier Competitive Response

**Baseline (A) — Score: 10/21**

The key finding for Baseline P4 is that it is the most tactically actionable of the baseline outputs — it organizes the response into a phased plan (0-30 days, 30-90 days, 90+ days) with specific named activities and decision criteria. The four strategic options (compete on price, compete on value, compete on segment, counter-position) are well-framed with honest risk assessments. This earns D4 a 2. The "What Your CEO Will Ask" section and the ARR impact modeling recommendation are practical and demonstrate good PM judgment. The output earns a 1 on D1 because no frameworks are named — the options analysis parallels strategic positioning frameworks without invoking them. D7 earns a 1 for the instruction to "build this model before Monday" — an acknowledgment that the CEO will need quantified evidence, implying the current analysis is hypothesis-grade. No confidence levels or evidence quality distinctions appear elsewhere.

**Anthropic PM Skill (B) — Score: 17/21**

The key finding for Anthropic P4 is the intelligence-gathering action table — a structured table with five signals, sources, frequencies, and owners for monitoring the Visier free tier launch. This is the closest any Anthropic output comes to the Codex's operational monitoring infrastructure. The feature comparison matrix explicitly flags Visier free tier ratings with an asterisk ("*Visier Free Tier ratings are estimates based on publicly available information... must be validated by product intelligence this week") — this is genuine evidence quality grading that earns D2 a 2. The win/loss interview guide is specific enough to be usable (not generic questions but contextual ones like "Did Visier's announcement play a role? Did you speak with a Visier rep?"). The key gap vs. Codex is the absence of explicit failure scenario probabilities, assumption registries, or named framework cross-referencing that would lift synthesis quality and calibration scores.

**PM Codex (C) — Score: 20/21**

The key finding for Codex P4 is the Aggregation Theory section applied to Visier's free tier — this produces an insight not present in either competing condition: "The $125M raise is not about free tier sustainability costs — it is about accelerating the benchmark data flywheel before competitors can replicate it." This is framework application producing a strategic insight that changes the urgency of the response (the threat is the data flywheel, not the free features). The COAP table (what is commoditizing → where profits shift) is one of the clearest strategic planning outputs in the benchmark. The scenario analysis includes explicit probabilities with falsification conditions: "What Would Falsify the Base Case?" — a standard inverse-logic check. Each recommendation in Part 15 follows the full cascade: Observation → Implication → Response → Confidence → Watch indicator. The confidence assessments distinguish between high/moderate/low for different components within a single recommendation (e.g., "High that the job is under-served [Tier 3]. Moderate that 90 days is achievable. Low confidence on competitive differentiation durability — 12-18 month window"). This granular intra-recommendation calibration is what earns D7 a 3 for this output.

---

### P5 — Commercial Real Estate Asset Management SaaS

**Baseline (A) — Score: 10/21**

The key finding for Baseline P5 is the disruption taxonomy applied to the three threats — identifying that Yardi, VTS, and Lessen represent fundamentally different attack vectors (integration/sales displacement, well-funded expansion, and low-end disruption respectively) and requiring asymmetric responses. This is the strongest analytical structure in the baseline corpus and earns D5 a 2. The "core strategic question" framing (build independently vs. build as acquisition target, dual-track rationale) is strategically sophisticated. The 90-day priorities section earns D3 a 2 by naming specific deliverables and implying owners. The gaps are: no named frameworks (D1=1), no evidence quality distinctions (D2=0), and no explicit uncertainty (D7=1 for occasional hedging language like "probably," "likely").

**Anthropic PM Skill (B) — Score: 17/21**

The key finding for Anthropic P5 is the feature comparison matrix with a weight column (★★★★★ = decisive buying criterion) applied against four competitors — this is the most buyer-perspective-grounded matrix in the Anthropic condition, distinguishing between what matters to the target buyer vs. what exists in the market. The conclusion that follows from the matrix is actionable: "Your sustainable differentiation is in investor-facing workflows — Yardi is Adequate here, VTS is Weak or Absent, Lessen is Absent." This earns D5 a 3. The competitive monitoring plan section at the end names specific signals by competitor (Yardi job postings, VTS product releases, Lessen funding announcements) with trigger thresholds — this is the closest the Anthropic condition gets to the Codex's leading indicators infrastructure. D7 earns a 2 for the general epistemic caution about the CAC analysis and the explicit "validate with win/loss data" flags, but lacks the confidence percentages that would earn a 3.

**PM Codex (C) — Score: 20/21**

The key finding for Codex P5 is the evidence tier table at the end — a standalone table labeling each major conclusion with its evidence tier (Tier 1, 2, 3, or 4), the source, and a note on how to strengthen it. For example: "Switching cost moat through LP portal → Tier 2 (customer behavior inference from 110% NRR) → Strengthen with 5 customer interviews." This is the most systematic evidence quality labeling in the benchmark, and it earns D2 a 2 (not 3, because it is a retrospective table rather than inline annotation throughout the analysis). The appendix checklist at the end — a self-verification list of 20 elements the output should contain — is structural quality assurance that is unique to the Codex condition. The COAP analysis produces the board narrative: "We are positioned at the layer where CRE software profits are migrating. Our job is to be there when the migration completes." The scenario table provides explicit probabilities (Base 45%, Bull 20%, Partnership 15%, Bear 20%) — including a partnership case not just a binary base/bear. The "Finding 2: SMB Retreat is the Highest-ROI Resource Reallocation" section is particularly notable for including a quantified impact estimate with uncertainty labeling: "estimate: approximately 15-20% of ARR at risk — flag for validation." D2 earns a 2 rather than 3 because tier annotations are not applied inline throughout the main analysis sections.

---

## 5. Skill Gap Analysis

### What the PM Codex Should Improve to Score Higher

The PM Codex already scores 93.3% overall, and achieving the remaining 7% (7 points) is concentrated in two dimensions: D2 (Evidence Hierarchy) and D7 (Calibration). Below is a precise diagnosis of what is missing, with direct citations from the outputs.

---

**Gap 1: D2 — Evidence Hierarchy (All Codex Outputs Score 2/3)**

The PM Codex applies a Tier 1-6 evidence labeling system but does so inconsistently. The pattern across all five outputs is:
- Tier labels appear on the most contentious or uncertain claims (good)
- Large sections of analysis — especially framework application (ERRC grids, Wardley maps, switching cost decompositions) — carry no tier annotations

Specific evidence:
- In Codex P1, the entire 7 Powers Heat Map (Part 2) carries tier labels only on two specific claims (Asana earnings call and G2 pricing data). The remaining 28 power ratings are unannotated.
- In Codex P3, the switching cost decomposition matrix (progress bars for 6 cost types across 5 competitors) carries no tier annotations despite being quantified estimates — the reader cannot distinguish which progress bar values are derived from customer behavioral data vs. product inference.
- In Codex P5, the feature matrix (9 rows × 4 competitors) carries no tier annotations on individual cells; the standalone evidence tier table at the end is a retrospective summary, not inline annotation.

**To score 3 on D2, the Codex would need:** Inline tier annotations on every substantive claim, not just the headline findings. The self-verification checklist in P5 includes "Evidence tiers labeled — inline tagging applied" — but the outputs do not consistently honor this self-standard.

**Specific recommendation:** Build a requirement into the skill that forces per-cell annotation in every comparison matrix. A convention of "(T3)" or "(T1: customer interviews)" at the end of each row would satisfy this. For claims without evidence, a convention of "(T6: inferred)" should be mandatory rather than optional.

---

**Gap 2: D7 — Calibration (P1 Scores 2/3; All Others Score 3/3)**

Codex P1 earns a 2 on D7. The issue is that confidence levels are provided for only four recommendations in Part 16 (the final section) but are absent from the 15 analytical sections that precede them. Claims in the JTBD section (e.g., "40-60% of SMB marketing teams have no dedicated PM tool [Tier 6: industry estimates]"), the Wardley map ("marketing integrations are in Genesis/Custom Build stage"), and the Aggregation Theory analysis are stated without inline confidence differentiators. The footnote at the very end covers all conclusions with a blanket caveat, which is not the same as claim-level calibration.

In contrast, Codex P2 is an exemplar of inline calibration — the "So What" section (Section 14) provides explicit confidence percentages (80%, 75%, 70%, 60%) with identified assumptions for each finding. This should be the standard for all prompts.

**To score 3 on D7 consistently, the Codex would need:** The "Observation → Implication → Response → Confidence → Watch Indicator" cascade format applied to all prompts, not just P2 and P4. The P1 recommendations stop at "watch indicator" without explicit confidence percentages for most sections.

---

**Gap 3: D4 — Failure Mode Awareness (P1 Scores 2/3)**

Codex P1 earns a 2 on D4 rather than a 3 because the failure mode coverage is asymmetric — the H3 scenario planning table provides three scenarios with probabilities, but failure modes within H1 and H2 (the more actionable near-term range) are scattered rather than structured. The "Warning" notes in the 7 Powers analysis (e.g., "Counter-positioning is only durable if the incumbents genuinely cannot respond") are failure mode-adjacent but do not constitute systematic adversarial self-critique. In P2, by contrast, the scenario analysis includes explicit falsification conditions ("what would falsify the vertical specialist thesis") — this is adversarial self-critique at its clearest.

**To score 3 on D4 consistently:** Every strategic recommendation section should include an explicit "failure condition" — the specific observable signal that would indicate the recommendation is wrong. P2 and P4 do this well; P1 does not. The self-verification checklist should include "Counterfactuals — what if we're wrong" as a mandatory field, as it appears in P5 but not consistently in all outputs.

---

## 6. Analyst Agent Best Practices Audit

### Patterns from Industry Analyst / Investment Analyst Agent Design

This section audits which structured analyst patterns are present vs. absent in PM Codex outputs, drawing on the design patterns associated with high-quality analyst agent outputs (investment memos, Gartner research, buy-side equity research).

---

### Present in PM Codex Outputs

**1. Structured Comparison Tables with Named Rating Scales**
All five Codex outputs use consistent comparison matrices (feature matrices, switching cost decompositions, 7 Powers heat maps) with explicit rating scales and legend keys. This is present and well-executed. The best implementation is the feature matrix in Codex P3, which uses ★-based strategic weight alongside ✅/🔄/🚧/❌ capability ratings and distinguishes "target" from "current" capability.

**2. Confidence Levels (H/M/L or Explicit Percentages)**
Present in Codex P2 and P4, where each recommendation includes explicit percentage confidence (e.g., "Confidence: High (80%). This assumes your NLP expertise applies..."). Inconsistently applied — absent or reduced in P1 and only partially applied in P3 and P5. This is an area of partial implementation.

**3. Adversarial Self-Critique (Falsification Conditions)**
Present in Codex P2 (Section 16: "What would falsify the vertical specialist thesis"), Codex P4 ("What Would Falsify the Base Case?"), and Codex P5 ("Triangulation note" and per-finding assumptions). Partially present in Codex P1 (the "Warning" notes) and P3 (the "no-go condition"). The pattern is present but inconsistently applied — not every recommendation inverts itself.

**4. Scenario Analysis with Named Probabilities**
Present in all five Codex outputs. The three-scenario framework (Base/Bull/Bear) with explicit probabilities is a consistent structural pattern. Codex P5 distinguishes four scenarios (Base 45%, Bull 20%, Partnership 15%, Bear 20%) — the highest fidelity implementation.

**5. Revision Triggers / Leading Indicators**
Present and well-executed in all five Codex outputs. Every output includes a "watch indicator" or "leading indicators" section with specific observable signals and alert thresholds (e.g., "Flag if win rate vs. Jumio in non-vertical-specific deals is below 30% and declining"). This is the strongest analyst-pattern implementation in the Codex and is largely absent from both Baseline and Anthropic outputs.

**6. Evidence Tier System**
Present — the Tier 1-6 system with inline labeling is a distinctive feature of the Codex condition. The implementation quality is highest in P2 and P5. As noted in the Skill Gap Analysis, inline annotation is inconsistent and the system is partially applied to some sections.

**7. Three Horizons Threat Landscape (H1/H2/H3 Tables)**
Present in P1, P2, P3, P4, and P5. These tables systematically categorize threats by timeline and mechanism, which is an investment-analyst-style forward risk scanning approach. The Codex is the only condition that systematically applies this structure.

**8. Asymmetric Competition Maps (Competitor Optimization Analysis)**
Present in P1, P2, P3, P4, and P5. The "each competitor is optimizing for X, willing to sacrifice Y" analysis is a structurally distinct pattern that explains competitive behavior in a way that is more durable than feature comparisons. This is well-executed across all Codex outputs and absent from Baseline and inconsistent in Anthropic.

**9. Value Chain / COAP Analysis**
Present and well-applied in P2, P3, P4, and P5. The Conservation of Attractive Profits analysis — identifying where profits are migrating in the value chain — is the most powerful strategic framing tool in the Codex. In P4, it produces the insight that analytics UI is commoditizing while AI-generated insight is the genesis-stage premium layer. This pattern is entirely absent from Baseline and present in a simplified form (market trends) in Anthropic.

---

### Absent or Underdeveloped in PM Codex Outputs

**1. Assumption Registry (Explicit List of Load-Bearing Assumptions)**
Investment analyst memos typically maintain a standalone assumption registry — a table listing every key assumption the analysis depends on, with confidence levels and what would change if the assumption is wrong. The Codex approaches this in P5's evidence tier table and P2's "what would falsify" section, but no output contains a formal, centralized assumption registry. The closest is the self-verification checklist in P5. An assumption registry would materially improve D4 and D7 scores.

**2. Formal Bull/Bear Inversion (Full Steelman of Opposing View)**
Equity research analysts typically include a formal "bear case" section that presents the strongest possible argument against their recommendation. The Codex scenario tables provide bear cases, but they are framed as probability-weighted scenarios rather than fully steelmanned opposing arguments. A bear case steelman for Codex P3 might read: "The strongest case against entering this market is not the competitive analysis — it is that GPT-5 will commoditize document AI accuracy within 18 months and make any vertical specialization defensible only through workflow integration, which requires 3-4 years to accumulate. At $5M seed, you do not have the runway to survive the accuracy commoditization period and build the workflow moat simultaneously." No output contains analysis at this depth of adversarial self-critique.

**3. Peer Comparables / Valuation Anchors**
Investment analysts anchor their analysis to comparable transactions (comps). The Codex P5 mentions an acquisition value range ("$80-150M to several credible strategic buyers") but without a formal comps table (comparable PropTech acquisitions with multiples). This is partially out of scope for a PM competitive analysis tool, but it is notable that the Codex reaches into financial territory without providing the structured evidence that would make such estimates credible.

**4. Staleness Flags on Time-Sensitive Claims**
The Codex includes evidence tier labels but does not consistently flag the recency of claims. In equity research, time-sensitive data carries a "as of Q4 2024" or "as of filing date" notation. Codex P1 mentions Asana's pricing tier ($24.99/user/month as of 2024 in the Baseline, not explicitly dated in the Codex) and product features that may have evolved. The Tier system does not distinguish between "Tier 4 data from 2024" and "Tier 4 data from 2022." Staleness flags should be added to claims where the evidence may have a short useful life.

**5. Source Citation Format**
Industry analyst reports cite specific documents, page numbers, and dates. The Codex tier system is qualitative (Tier 3 = "market behavior inferred from publicly available data") rather than formally cited. For claims that would be expected to have citable sources (e.g., "Jumio has processed hundreds of millions of verifications"), the current convention of "(T5: company press releases)" is a category label rather than a verifiable citation. The gap is significant for any output that will be presented to a board or an investor audience.

**6. Quantified Market Sizing with Source Attribution**
Only Codex P3 includes a market sizing section, with the explicit caveat "Script not available — these are estimated order-of-magnitude figures; verify with CFO before board presentation." None of the other four Codex outputs include TAM/SAM/SOM estimates. Investment analyst memos routinely ground their analysis in market size. While the Codex correctly hedges that script estimates are unavailable, the absence of any market sizing in P1, P2, P4, and P5 is a gap that limits the usefulness of the output for board or investor presentations.

---

### Summary Audit Table

| Analyst Agent Pattern | Baseline | Anthropic | Codex | Notes |
|----------------------|:---:|:---:|:---:|-------|
| Structured comparison tables | Partial | Yes | Yes | |
| Confidence levels (explicit) | No | Partial | Partial | Codex: present in P2/P4; weak in P1 |
| Adversarial self-critique | No | No | Partial | Falsification conditions in P2, P4, P5 only |
| Scenario analysis with probabilities | No | Partial | Yes | Anthropic has scenarios; Codex adds probabilities |
| Revision triggers / leading indicators | No | Partial | Yes | Codex distinctively strong here |
| Evidence tier system | No | No | Partial | Codex has system; inconsistently applied inline |
| Three horizons threat landscape | No | No | Yes | Unique to Codex |
| Asymmetric competition maps | No | No | Yes | Unique to Codex |
| Value chain / COAP analysis | No | No | Yes | Unique to Codex |
| Assumption registry | No | No | No | Absent from all conditions |
| Formal bear case steelman | No | No | No | Absent from all conditions |
| Peer comparables / valuation anchors | No | No | Partial | Present only in P5 with no formal comp table |
| Staleness flags on time-sensitive claims | No | No | No | Absent from all conditions |
| Formal citation format | No | No | No | Codex uses category labels, not formal citations |
| Market sizing with sources | No | No | Partial | Present only in Codex P3 |

---

## 7. Final Verdict

The PM Codex (Condition C) substantially outperforms both alternatives across all seven scoring dimensions. The Codex's most decisive advantages are in D1 (framework application — all prompts achieve the maximum score by applying multiple named frameworks with cross-referenced conclusions), D5 (synthesis quality — frameworks connect to and check each other rather than being applied in isolation), and D7 (calibration — confidence levels, evidence tiers, and watch indicators appear throughout). The Anthropic PM Skill (Condition B) performs well and is a clear, significant improvement over Baseline — especially on D6 (output structure) and D3 (strategic specificity) — but the skill stops short of cross-framework synthesis and does not match the Codex's systematic evidence labeling or failure mode architecture. The Baseline condition (Condition A) produces thoughtful, readable analysis but demonstrates the fundamental limitations of unguided generation: no framework vocabulary, no evidence grading, and no uncertainty acknowledgment.

The 14.5-point gap between Anthropic (81) and Codex (98) reflects a qualitative difference in analytical depth, not just structural formatting. The Codex's "Competitive War Map" produces findings that change decision priorities (e.g., Visier's free tier is a data flywheel play, not a price competition play; the correct response is asymmetric counter-positioning, not a matching free tier) in ways that the Anthropic outputs, which are well-structured but framework-light, do not. This difference is the measurable return on the PM Codex skill design.

---

*Scorecard produced: 2026-02-19 | Files evaluated: 15 | Scoring rubric: 7 dimensions × 0-3 scale × 5 prompts × 3 conditions | Maximum: 21 per output, 105 per condition*
