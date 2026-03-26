# Use Cases: Stakeholder Alignment

> Three real-world scenarios demonstrating the transformation from generic AI stakeholder advice to skill-powered alignment strategies. Each use case showcases different frameworks and capabilities from the Stakeholder Alignment skill (v2.0.0).

---

## Use Case 1: "Aligning 4 VPs on a $3M Redshift-to-Databricks Migration"

### Scenario

You are the PM driving a $3M data platform migration from Amazon Redshift to Databricks Lakehouse. Four VPs must agree within 8 weeks (the Redshift contract auto-renews for 2 years if no decision is made). Only one VP currently supports the migration: the VP of Engineering (Chen) who champions the move for technical modernization. The VP of Finance (Ramirez) is the primary blocker — she killed a similar proposal 18 months ago and was publicly blamed for a separate cloud migration that went 40% over budget. The VP of Product (Okafor) is neutral but will follow Finance's lead if not given an analytics uptime guarantee. The VP of Design (Park) hasn't been consulted because nobody explained why a data platform migration affects her team's UX research analytics pipeline.

### The Prompt

> I need to align 4 VPs on a $3M Redshift-to-Databricks migration. Engineering VP supports it. Finance VP killed a similar proposal 18 months ago. Product VP is neutral but risk-averse after a Q1 Redshift outage. Design VP hasn't been consulted. Redshift auto-renews in 8 weeks. Build the alignment strategy.

### Without the Skill (Generic AI)

**Stakeholder Alignment Plan**

Here's how to approach each VP:

1. **Engineering (champion):** Keep them engaged. Have them present the technical case.
2. **Finance (skeptic):** Build a strong ROI case. Show the TCO comparison and payback period.
3. **Product (neutral):** Address the uptime concern with an SLA guarantee.
4. **Design (unaware):** Brief them on the migration and ask for input.

**Meeting plan:** Schedule a group meeting to present the proposal. Prepare a slide deck covering technical benefits, cost analysis, and timeline. Address concerns during Q&A.

**Timeline:** Week 1-2 prep, Week 3-4 present, Week 5-6 decision.

### With the Skill

**Stakeholder Alignment Strategy: Redshift-to-Databricks Migration**

> **Confidence band:** M-H (55-80%) | **Staleness window:** Position assessments valid 30 days from analysis

**Executive Summary**

Only 1 of 4 VPs is currently supportive. The biggest risk is not Finance's skepticism — it's the Product VP interpreting silence from Design as opposition and joining a "let's delay" camp, giving Finance a blocking coalition of 2 (M, T3). **Recommended first move: brief the Design VP on the UX research pipeline dependency before any group meeting — her neutral-to-supportive shift prevents a blocking coalition and gives Engineering a second ally before engaging Finance.**

**Step 0: Context Gate**

| Question | Answer | Implication |
|---|---|---|
| Multiple stakeholders required? | Yes — 4 VPs, no single approver (T1) | Full alignment strategy warranted. Consensus model (all 4 or 3 + CEO override). |
| Positions known? | Mixed — Engineering direct (T1), Finance direct (T1), Product inferred (T2), Design unknown (T5) | Finance and Engineering are H-confidence. Product is M. Design is L. |
| Previous alignment attempt? | Yes — similar migration shelved 18 months ago after Finance flagged cost (T2) | Decision Archaeology is load-bearing. The 2024 failure shapes current positions. |
| Hard deadline? | Yes — Redshift auto-renews 2 years if no decision in 8 weeks (T1) | Sequence must compress. 1-2 weeks max per step. |

**Framework Selection**

| Question type | Primary frameworks | Supporting | Skipped |
|---|---|---|---|
| Cross-functional VP alignment, $3M, 8-week deadline | Power-Interest-Position Matrix, Decision Archaeology, Alignment Sequencing, Objection Pre-emption | Coalition Analysis, Communication Strategy | Alignment Monitoring — applied at reduced depth (8-week compressed campaign) |

**1. Power-Interest-Position Matrix**

| Stakeholder | Power | Interest | Position | Desired | Gap | Confidence |
|---|---|---|---|---|---|---|
| Chen (Engineering) | H (T1) | H (T1) | Champion (T1) | Champion | None — maintain | H |
| Ramirez (Finance) | H (T1) | H (T1) | Skeptic (T1) | Supporter | Large — skeptic to supporter requires ROI + risk mitigation | H |
| Okafor (Product) | H (T2) | M (T2) | Neutral (T2) | Supporter | Medium — needs analytics uptime guarantee | M |
| Park (Design) | M (T3) | L (T5) | Unengaged (T5) | Supporter | Unknown — hasn't been briefed; hypothesis only | L |

[EVIDENCE-LIMITED] Park's assessment is T5 (absence from Slack channel, no RFC comments). Validate with direct conversation.

**Power Source Decomposition**

| Stakeholder | Formal Authority | Informal Influence | Resource Control | Veto? | Net Power |
|---|---|---|---|---|---|
| Chen | H — owns eng capacity (T1) | H — CEO trusts her on infra (T2) | H — engineering headcount (T1) | Yes | **H** |
| Ramirez | H — budget approval >$1M (T1) | H — CFO's trusted lieutenant (T2) | H — funding allocation (T1) | Yes | **H** |
| Okafor | H — owns analytics roadmap (T1) | M — less politically active (T3) | M — analytics team, not infra budget (T2) | Soft veto (T2) | **H** |
| Park | M — owns design + UX research (T2) | M — well-liked, not politically active (T3) | L — no infra budget (T3) | No | **M** |

**2. Coalition Analysis**

| Type | Members | Basis | Durability | Defection Risk |
|---|---|---|---|---|
| Natural allies | Chen | Technical modernization; ML pipelines blocked 2 years (T1) | H | Only if scope balloons threatening Q3 commitments |
| Latent allies | Park | UX research pipeline improves with Lakehouse — but she doesn't know (T3) | M | If migration creates research data downtime during Q2 studies |
| Swing voters | Okafor | Undecided — needs uptime guarantee; knows Redshift has problems (T2) | N/A | Tips to support with uptime SLA; tips to oppose if Finance frames it as "unnecessary risk" |
| Stable opponents | Ramirez | $3M without guaranteed ROI violates her framework; burned by 2024 overrun (T2) | H | Converts only with: phased spending + kill gates, cost-of-inaction comparison, peer evidence |

**Critical mass:** Need 3 of 4 VPs. Currently have 1. Gap = 2.

**Power Broker Analysis:**
- **Ramirez influences Okafor** — Okafor defers to Finance on cost decisions (T2). His analytics investments funded through her budget process. He avoids opposing her publicly.
- **Chen influences Park** — successful Figma migration collaboration in 2024 (T2). Park said "I trust Lisa's team." Chen is the ideal messenger for Park.

**Influence Network:**
```
CHEN (Champion, H Power)            RAMIREZ (Skeptic, H Power)
     |                                      |
     | trusts technical                     | defers on cost
     | judgment                             |
     v                                      v
PARK (Unengaged, M Power) <--- if Park opposes --> OKAFOR (Neutral, H Power)
                                Okafor follows

GOAL: Build Chen -> Park -> Okafor chain BEFORE
      Ramirez -> Okafor chain activates
```

**3. Decision Archaeology**

| Past Decision | Date | Outcome | How It Shapes Today |
|---|---|---|---|
| Redshift-to-Snowflake proposal | Sep 2024 | Shelved — Finance flagged unclear ROI; Eng couldn't show <9 month timeline (T2) | **Ramirez:** "I was right." **Chen:** Learned to bring tighter plan. **Okafor:** Sat out and regretted it — suffered Q1 scaling issues. |
| Cloud cost overrun (different project) | Mar 2024 | 40% over budget — $1.2M overrun (T1) | **Ramirez:** Core of her skepticism. Publicly blamed. Her reputation is attached to preventing another overrun. Opposition is professional, not ideological. |
| Design system migration to Figma | Jun 2024 | Successful — Park and Chen collab; under budget, ahead of schedule (T2) | **Park:** Positive experience with Chen's team. Trusts Chen's scope/execute ability. Asset for briefing. |
| Redshift scaling incident | Jan 2025 | 3 dashboards down 4 hours; Okafor missed board report deadline (T1) | **Okafor:** Knows Redshift has problems. Supports migration conceptually but needs guarantee the cure isn't worse. Emotional anchor: "I can't go through that again." |

**Incentive Alignment:**

| Stakeholder | Their Goals | How Migration Affects | Hidden Agenda Risk |
|---|---|---|---|
| Chen | Tech modernization, team retention, SLA improvement (T1) | Strongly positive | Low — may overestimate speed to build support (T4) |
| Ramirez | ROI discipline, budget accuracy, no cost surprises (T1) | Mixed — $3M outlay negative; Redshift avoidance positive but speculative | M — reputation protection after 2024 overrun is stronger driver than numbers (T3) |
| Okafor | Analytics uptime, A/B test velocity, board reporting (T1) | Mixed — post-migration better; migration itself risks downtime | Low — genuine concern (Q1 incident was real, T2) |
| Park | UX research velocity, design system adoption (T2) | Slightly positive — Lakehouse enables faster analytics joins | Low — simply hasn't been consulted (T5) |

**Trust Network:**

| A | B | Trust | History | Implication |
|---|---|---|---|---|
| Chen | Ramirez | Medium (T2) | Ramirez killed Chen's 2024 proposal. Scar tissue, not animosity. | Chen approaching Ramirez directly triggers "here we go again." Need different framing. |
| Chen | Park | High (T2) | Successful Figma migration. "I trust Lisa's team." | Chen is ideal Park messenger. |
| Chen | Okafor | Medium-High (T2) | Chen's team resolved Q1 incident. Okafor is grateful. | Chen can credibly say "current platform is ticking time bomb." |
| Ramirez | Okafor | Medium-High (T3) | Ramirez funded Okafor's team expansions over 2 years. | Okafor won't publicly oppose Ramirez. |

**O->I->R->C->W:**
- **O** [T2]: Ramirez's skepticism is professional (reputation protection after overrun), not ideological (anti-technology).
- **I**: Her conversion conditions are addressable: (a) phased spending with kill gates, (b) cost-of-inaction showing Redshift renewal costs $2.1M, (c) named financial controller on team.
- **R**: Build ROI in Finance's language — not "Databricks is better" but "24-month TCO comparison with kill gates at months 3, 6, 12." Embed finance business partner. Make Ramirez a co-author of controls, not a reviewer.
- **C**: H — assumes opposition is rational (T2). Invalidated if she opposes even with Finance-grade TCO + kill gates.
- **W**: If she requests 3rd-party TCO audit -> engaging seriously (good). If she delegates to junior analyst -> distancing (bad).

**4. Alignment Sequencing**

| Seq | Stakeholder | Action | Timing | Dependency |
|---|---|---|---|---|
| 1 | Chen (maintain) | Strategy session: align on narrative, divide alignment work. She takes Park, you take Okafor. Confirm uptime guarantee she can back. | Week 1 | None |
| 2 | Park (convert) | Chen + you brief Park: Lakehouse improves research analytics, zero-downtime for Q2 study, faster queries post-migration. Framing: "research capability upgrade." | Week 1-2 | After Step 1 |
| 3 | Okafor (convert) | Present: written analytics uptime SLA (99.9%), parallel-run period, Q1 postmortem showing increasing Redshift risk. Share that Park is on board. Framing: "risk of NOT migrating now exceeds risk of migrating." | Week 2-3 | After Steps 1-2 |
| 4 | Ramirez (convert) | Finance-grade package: 24-month TCO, phased kill gates (months 3/6/12), named financial controller, 3 VPs already supportive. Ask her to co-design guardrails. Framing: "controlled investment with exits, not open-ended commitment." | Week 3-4 | After Steps 1-3 |
| 5 | Group ratification | Unified proposal. Every VP individually briefed. Meeting is ratification ceremony, not debate. Ramirez presents the guardrails she co-designed. | Week 5-6 | After Steps 1-4 |

**Anti-Patterns Avoided:**

| Anti-Pattern | Why It Fails | What We Do Instead |
|---|---|---|
| Approaching Finance first | Ramirez killed this once; gives her opportunity to set "too expensive" frame | Finance last, with coalition + TCO |
| Group meeting before 1:1s | Ramirez more oppositional in public; Okafor more cautious; Park lacks context | All 1:1s first; group for ratification only |
| Leading with "Databricks is better" | Only Chen cares about technology | Per-stakeholder framing: research for Design, uptime for Product, TCO for Finance |
| Ignoring Design | Unengaged VP = wildcard in group meeting | Proactive briefing converts wildcard to ally |

**5. Objection Pre-emption Playbook**

**Objection 1: "The ROI doesn't justify the risk" — Ramirez**

Type: Rational + Political (reputation protection). Underlying: she cannot afford another >$1M overrun.

**Steel-manned:** "We spent $3M on a migration 18 months ago that went 40% over budget. Now you want another $3M with longer payback. If we're wrong, we've spent $3M we can't recover and disrupted every analytics team."

**Response script:** "Maria, I want to acknowledge — you were right to flag the 2024 overrun. This proposal is different in three ways. First, phased: $800K in Q2 for POC on 3 non-critical pipelines, with go/no-go before committing $2.2M. If POC fails, you've spent $800K, not $3M. Second, 24-month TCO: Redshift renewal + scaling costs $2.1M — net incremental is $900K, not $3M. Third, embedded finance business partner with weekly cost tracking."

**Evidence required:** 24-month TCO model (T1), POC scope with kill criteria (T2), peer company data (T3).

**Objection 2: "What happens to my dashboards?" — Okafor**

Type: Rational (Q1 incident). Underlying: missed board report deadline, cannot absorb that risk again.

**Steel-manned:** "My 14 analysts do daily queries on production data. Board reporting in Q2 and Q3. Any plan without 100% analytics uptime during those periods is a non-starter."

**Response script:** "James, the Q1 incident is exactly why we need to migrate — Redshift caused that outage, and it'll get worse. Here's the guarantee: parallel-run Redshift and Databricks for 8 weeks. Your team queries Redshift as normal. We shift pipelines gradually, validate parity, cut over only when your team confirms. Written SLA: 99.9% analytics uptime, zero planned downtime. Named on-call engineer for your queries during transition."

**Objection 3: "Why wasn't Design consulted?" — Park**

Type: Emotional + Structural (process). Underlying: excluded from infrastructure decisions affecting her team.

**Response script (via Chen):** "Soo-Jin, you're right that Design should have been consulted earlier. Here's why this matters for your team: Lakehouse enables sub-second joins between Amplitude and user segment data. Your team currently waits 4-6 hours on Redshift. Post-migration: minutes. For Q2 usability study: we won't touch any pipeline your team depends on until after Week 8. And going forward, your research engineering lead joins the data platform planning group."

**Objection 4: "We just renewed Redshift — why switch?" — Ramirez (secondary)**

**Response:** "That's exactly the urgency — auto-renewal deadline means we decide now or lock in 2 years at $1.05M/year ($2.1M). Parallel-run adds $180K for 8 weeks. Net double-paying period is 8 weeks, not months."

**6. Communication Strategy**

| Stakeholder | Format | Framing | Messenger | Channel |
|---|---|---|---|---|
| Chen | Working session (whiteboard) | "Let's divide alignment work — you take Park, I take Okafor" | You (PM) | 1:1, in-person, Week 1 |
| Park | Conversation then 1-page brief | "Migration improves research speed 10x. We protect Q2 study. Your team joins planning group." | Chen + you | Informal (coffee), Week 1-2 |
| Okafor | Data-driven doc (SLA + architecture) | "Risk of staying > risk of migrating. Uptime guarantee. Chen and Park already on board." | You + Chen | Scheduled with pre-read, Week 2-3 |
| Ramirez | Formal TCO model + executive brief | "24-month cost comparison. Kill gates. Finance business partner. 3 VPs support. You co-design controls." | You + Chen | Scheduled, pre-read 48h before, Week 3-4 |

**Per-stakeholder framing:**
- **Chen:** Lead with technical modernization, ML pipeline enablement. Avoid cost justification.
- **Ramirez:** Lead with 24-month TCO, phased kill gates, cost-of-inaction. Avoid "modern stack" and team morale.
- **Okafor:** Lead with analytics SLA, parallel-run plan, Q1 postmortem. Avoid cost savings (not his concern).
- **Park:** Lead with research pipeline speed, Q2 protection, inclusion. Avoid budget numbers.

**7. Alignment Monitoring & Recovery**

**Drift Detection Signals:**

| Signal | Meaning | Severity | Response |
|---|---|---|---|
| Ramirez sends cost email to VPs before Week 4 | Preemptive framing — blocking move | High | Accelerate sequence. Move Ramirez 1:1 to Week 2-3. |
| Okafor starts saying "let's see what Finance thinks" | Deferring to Ramirez instead of forming own view | Medium-High | Go back with stress test offer. Make parallel-run concrete. |
| Park stops responding to briefing invitation | Busy or disengaging | Medium | Chen follows up: "20 minutes to make sure your research pipeline is protected." |
| Chen's timeline slips | Champion's credibility at risk | High | Scope down privately. Protect uptime SLA. Communicate proactively. |

**Recovery Playbook:**
- Ramirez rejects phased approach -> Ask: "What would a proposal need to look like?" If conditions, address them. If "no conditions, I oppose" -> escalate to CEO framing: "Maria and I disagree on TCO — we'd like guidance on which assumptions are correct."
- Okafor commits privately but won't go public -> Ask directly: "Can I tell Maria that Product supports this?"
- Redshift deadline moves up 2 weeks -> Compress to parallel tracks. Brief Park and Okafor simultaneously in Week 1-2.

**Success Criteria:**

| Level | What "Aligned" Looks Like | Durability |
|---|---|---|
| Verbal agreement | "I'm supportive" in 1:1 | Low — deniable |
| Written approval | Email: "Product supports given SLA" | Medium — creates record |
| Resource commitment | Ramirez allocates POC budget; Okafor assigns analyst | High — money and people hard to uncommit |
| Public advocacy | Ramirez presents guardrails at leadership meeting | Very high — reputational commitment |

**Target:** Chen = public advocacy. Park = written. Okafor = resource commitment. Ramirez = resource commitment.

**Assumption Registry**

| # | Assumption | Confidence | Evidence | Invalidation Signal |
|---|---|---|---|---|
| 1 | Ramirez's opposition is rational (addressable), not positional (protecting territory) | H | T1: 2024 objection was specific; T2: chief of staff "Maria is persuadable if numbers work" | Rejects phased approach even with Finance-grade TCO + kill gates |
| 2 | Okafor won't publicly oppose with credible uptime guarantee | M | T2: PM reports he said privately "I wish we'd migrated last year" | Demands zero-risk (impossible for any migration) |
| 3 | Park's non-engagement is disinterest, not opposition | L | T5: absence from Slack + RFC; no negative signals | Park discussed concerns with Okafor privately, forming "slow down" pact |
| 4 | CEO won't intervene unless asked | M | T2: historically delegates infrastructure decisions | CEO mentions "data platform" unprompted in leadership meeting |
| 5 | 24-month TCO favors Databricks over Redshift renewal | H | T1: Redshift $1.05M/yr; T2: Databricks vendor estimate | Databricks pricing higher than estimated OR Redshift offers 30%+ discount |

**Cross-Framework Contradictions**

| Contradiction | Framework A | Framework B | Resolution |
|---|---|---|---|
| Okafor's stated neutrality vs. revealed behavior | Power-Interest: Neutral — no stated position | Decision Archaeology: "I wish we'd migrated last year" — latent supporter | **Weight Archaeology.** Public neutrality is political caution (avoiding opposing Finance), not indifference. Treat as latent supporter needing cover. |
| Park's "low interest" vs. research dependency | Power-Interest: Low Interest — hasn't engaged | Incentive Analysis: structural dependency = should be High Interest | Park's interest is objectively high but subjectively low because nobody explained the connection. "Low interest" is an information gap, not a position. |

**Adversarial Self-Critique**

**Weakness 1: Champion dependency — entire strategy rests on Chen.** If Chen gets pulled into a P0 incident in Week 2-3, she disappears for 2+ weeks. Without Chen: Park engagement loses messenger, Okafor loses validation, Ramirez loses accountability. Mitigation: brief Chen's Sr. Director of Data Eng as backup in Week 1. P(Chen unavailable) ~20% over 6 weeks (T4).

**Weakness 2: The sequence assumes linear progression, but stakeholders talk to each other.** If Ramirez and Okafor have lunch in Week 2 and Ramirez says "do you know about another migration?" — Okafor, unbriefed, says "no, sounds expensive." Pre-framed by Finance before your presentation. Mitigation: accelerate Okafor to Week 1-2 (overlap with Park). Accept risk that Park's conversion isn't locked in first.

**Weakness 3: This strategy treats Park as easy — she may have legitimate blockers.** UX research may have data governance requirements (PII handling, GDPR compliance) that Redshift satisfies and Databricks would need to address. If Park raises governance in the group meeting, it adds weeks past the deadline. Mitigation: in Chen-Park briefing, explicitly ask: "Any data governance or compliance requirements for your research pipeline?"

**Strategic Recommendations (O->I->R->C->W)**

**Rec 1: Build Coalition Before Engaging Finance**
- **O** [T1, T2]: Ramirez is primary blocker with veto + influence over Okafor. Chen is champion. Park and Okafor are convertible.
- **I**: Approaching Ramirez first repeats 2024 failure. Approaching her last with 3-VP coalition changes dynamic from "Engineering wants expensive toys" to "the organization has decided."
- **R**: Execute 5-step sequence: Chen (Wk 1) -> Park (Wk 1-2) -> Okafor (Wk 2-3) -> Ramirez (Wk 3-4) -> Ratification (Wk 5-6).
- **C**: H — assumes Ramirez is rational and Park/Okafor convertible.
- **W**: If any step >1.5 weeks, compress to parallel. If Ramirez frames before Week 4, accelerate immediately.

**Rec 2: Make Ramirez a Co-Author, Not a Reviewer**
- **O** [T1]: Ramirez's 2024 objection was evidence-based. Reputation tied to discipline.
- **I**: A finished TCO for "review" makes her gatekeeper. Inviting her to co-design controls makes her co-owner.
- **R**: Present TCO framework (not finished model). Ask Ramirez to define kill gates, reporting cadence, variance thresholds. Embed her finance business partner. Let her present guardrails at the group meeting.
- **C**: M — assumes constructive engagement with co-authorship.
- **W**: Accepts co-design invitation -> high conversion. Says "just send me the model" -> maintaining gatekeeper.

**Rec 3: Use Redshift Deadline as Forcing Function**
- **O** [T1]: Auto-renewal = $2.1M over 2 years.
- **I**: Reframes from "should we spend $3M?" to "which $2M+ commitment is better?" Net incremental cost is $900K, not $3M.
- **R**: Lead every conversation with cost-of-inaction. Make renewal deadline visible in every document.
- **C**: H — contract terms are T1.
- **W**: If Redshift offers 30%+ discount, cost-of-inaction argument weakens.

### What Changed

- **Power-Interest-Position Matrix with evidence tiers replaced a 4-person list** — each stakeholder scored on power, interest, and position with gap analysis, confidence levels, and power source decomposition (formal authority, informal influence, resource control, veto capability).
- **Coalition Analysis identified the 2-coalition dynamic** — "this is not a 4-person problem, it's a 2-coalition problem" with influence network mapping and power broker identification (Ramirez influences Okafor; Chen influences Park).
- **Decision Archaeology excavated 4 past decisions shaping current positions** — the 2024 shelved proposal, the cloud cost overrun, the successful Figma migration, and the Q1 Redshift incident. The generic output had no historical context.
- **Alignment Sequencing with anti-patterns produced a 5-step gated plan** — specific actions, timing, dependencies, and per-stakeholder framing. The group meeting is ratification (step 5), not discovery (step 1). The generic output led with a group meeting.
- **Objection Pre-emption with steel-manned versions and scripted responses** — each objection stated stronger than the stakeholder would, with evidence-backed rebuttals and specific meeting scripts. The generic output said "build a strong ROI case."
- **Communication Strategy tailored messenger, format, and framing per stakeholder** — Chen briefs Park (trust), you + Chen brief Okafor (credibility), formal TCO for Ramirez (finance language). The generic output used a single slide deck for all.
- **Monitoring with drift signals and recovery playbook** — specific observable signals ("Okafor starts saying 'let's see what Finance thinks'") with severity ratings and response actions, vs. no monitoring mechanism.

---

## Use Case 2: Aligning CEO and CTO on Build vs. Buy for Auth System

### Scenario

A startup CEO wants to buy an auth solution (Auth0/Clerk) to ship faster. The CTO wants to build custom auth because vendor lock-in concerns and long-term flexibility. The PM needs to align them before sprint planning next Monday.

### The Prompt

> CEO wants to buy auth (Auth0/Clerk). CTO wants to build custom. I need them aligned by Monday. Build the alignment strategy.

### Without the Skill (Generic AI)

Present a comparison table of build vs. buy with costs and timelines. Schedule a meeting with both. Recommend a compromise: start with Auth0 and plan to migrate later.

### With the Skill

**Context Gate:** 2 stakeholders, 1 week deadline, binary decision. This is NOT a full alignment campaign — it's a single-decision alignment with opposing positions.

**Decision Archaeology:** Has the CTO been burned by vendor lock-in before? If yes, his position is experience-based, not theoretical — address with vendor-exit plan, not "Auth0 is great." Has the CEO shipped something late before? If yes, her urgency is experience-based — validate with timeline comparison.

**Power-Interest-Position:**

| Stakeholder | Power | Position | Core Concern |
|---|---|---|---|
| CEO | H (resource allocation authority) | Buy (Auth0/Clerk) | Speed to market — every week delayed is runway consumed |
| CTO | H (technical veto) | Build custom | Vendor lock-in, long-term flexibility, technical control |

**Coalition:** N/A — 2 person alignment. No coalition building possible. This is pure mediation.

**The Hidden Agreement:** Both want the same outcome — ship auth fast without creating future problems. They disagree on risk weighting: CEO weights speed risk (delay); CTO weights dependency risk (lock-in). Frame the discussion around shared goal, not competing options.

**Alignment Strategy:**

| Step | Action | Timing |
|---|---|---|
| 1 | 1:1 with CTO: "What specifically about vendor lock-in concerns you? What would an exit plan need to include for you to be comfortable?" Extract specific conditions. | Monday |
| 2 | 1:1 with CEO: "If we use Auth0 with a documented exit plan that CTO signs off on, would that satisfy your speed requirement?" Extract timeline constraint. | Tuesday |
| 3 | Build the "Buy with exit plan" proposal: Auth0 now, abstraction layer in sprint 3, migration capability documented. CTO co-authors exit plan. | Wednesday |
| 4 | Joint 30-min meeting: Present as "we buy for speed AND protect flexibility." CTO presents the exit plan he co-authored. | Thursday |

**Objection Pre-emption:**
- CTO: "Abstraction layers never work." Response: "You're right that generic abstraction fails. This is a specific interface contract — 3 endpoints. You define the contract."
- CEO: "Why do we need an exit plan? Just ship." Response: "The exit plan takes 2 hours to document and prevents a 3-month rewrite if Auth0 changes pricing or deprecates features."

### What Changed

1. **Decision Archaeology asked "has the CTO been burned before?"** — the opposition may be experiential, not theoretical.
2. **Hidden agreement identified** — both want "ship fast without future problems." Disagreement is on risk weighting, not outcome.
3. **CTO becomes co-author of exit plan** — converts from opponent to invested co-owner.
4. **Specific scripted responses** for both "abstraction layers never work" and "just ship."

---

## Use Case 3: Cross-Functional Alignment for Deprecating a Legacy Feature

### Scenario

A PM needs to deprecate a legacy feature used by 8% of customers (generating 15% of support tickets). Support VP wants it gone. Sales VP says 3 enterprise deals depend on it. Engineering VP needs the capacity for a new initiative. Customer Success VP is worried about churn.

### The Prompt

> I want to deprecate a legacy feature. 8% of customers use it, generates 15% of support tickets. Support VP: kill it. Sales VP: 3 enterprise deals depend on it. Eng VP: needs capacity. CS VP: worried about churn. Align them.

### Without the Skill (Generic AI)

Create a deprecation timeline. Offer migration paths. Present data showing the feature's cost. Schedule a meeting with all 4 VPs.

### With the Skill

**Power-Interest-Position:**

| Stakeholder | Position | Core Concern | Evidence Quality |
|---|---|---|---|
| Support VP | Strong champion (kill it) | 15% of tickets = team capacity drain | H (T1: ticket data) |
| Engineering VP | Champion | Capacity for new initiative | H (T1: sprint data) |
| Sales VP | Blocker | 3 enterprise deals ($X ARR) | M (T2: deal pipeline) — verify deals are actually dependent |
| CS VP | Cautious neutral | 8% customer churn risk | M (T3: churn projection) |

**Decision Archaeology:** Has this deprecation been proposed before? If yes, who blocked it and why? The Sales VP's objection may be anchored on a past commitment ("we promised this customer we'd maintain it").

**Critical question for Sales VP:** "Are the 3 enterprise deals dependent on THIS feature, or on the CAPABILITY this feature provides?" If the capability, a migration path solves it. If the specific implementation, that's a harder problem.

**Coalition:** Support + Engineering = 2 champions. Sales = 1 blocker. CS = swing voter. Convert CS first (churn data), then present to Sales with 3-VP coalition.

**Alignment Sequence:**

| Step | Action |
|---|---|
| 1 | Quantify: What is the cost of keeping the feature? (Support: 15% of tickets x avg resolution time x cost. Eng: opportunity cost of maintenance sprints.) |
| 2 | Verify Sales claim: Are the 3 deals truly dependent? Meet with AEs individually. If 1-2 deals are flexible, the blocker weakens. |
| 3 | Build migration path: What replaces the capability for the 8% of customers? If migration path is credible, CS concern addressed. |
| 4 | Convert CS: Show migration path + churn analysis (if migration is offered, expected churn drops from 8% to 2-3%). |
| 5 | Present to Sales: "2 of 3 deals are flexible on implementation. For the 1 that isn't, here's a 90-day maintenance window with migration support." |
| 6 | Group ratification with 4-VP support. |

**Objection Pre-emption — Sales VP:**

**Steel-manned:** "You want to kill a feature that 3 of my pipeline enterprise deals depend on. If any of these deals fall through because of a deprecation, that's $XM in lost ARR that MY team is held accountable for."

**Response:** "I hear you — and I verified with your AEs. [Deal A] needs the capability but is flexible on implementation — the migration path works. [Deal B] has a 90-day timeline, so the maintenance window covers it. [Deal C] — let's talk about that one specifically. What does the customer actually need?"

### What Changed

1. **Critical verification of Sales claim** — "Are deals dependent on the feature or the capability?" changes the entire negotiation.
2. **Quantified cost of keeping** — not just "it generates tickets" but specific cost in support hours + engineering opportunity cost.
3. **CS converted with churn modeling** — "if migration offered, churn drops from 8% to 2-3%" converts the cautious neutral.
4. **Sales approached with verified data** — "2 of 3 deals are flexible" defuses the blocker, leaving 1 deal to negotiate.
5. **Sequence: verify claims -> build solution -> convert neutral -> approach blocker with coalition.**

---

*Generated using Stakeholder Alignment skill v2.0.0 | PM Skills Arsenal*
