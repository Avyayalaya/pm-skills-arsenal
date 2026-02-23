# Use Cases: Metric Design & Experimentation

## Use Case 1: B2B SaaS Company Choosing a North Star Metric After Series B

### Scenario
Vectrix, a 200-person B2B project management tool, just closed a $45M Series B. The board wants a single North Star Metric to align product, growth, and engineering around. The CEO's instinct is MRR, but the VP Product suspects MRR is too lagging to steer weekly product decisions. The metric needs to work for board reporting AND day-to-day prioritization, and the company serves both SMB self-serve and mid-market sales-assisted segments with very different usage patterns.

### The Prompt
> We're a B2B project management SaaS that just raised Series B. We have ~8,000 paying customers (60% SMB self-serve, 40% mid-market sales-assisted). Our board wants a North Star Metric. The CEO wants to use MRR. I think MRR is too lagging. Help me design the right metric framework — what should our NSM be, how should it decompose, and what are the leading indicators that tell us if we're on track before revenue shows it?

### Without the Skill (Generic AI)
Great question! MRR is indeed a lagging indicator — by the time it drops, you've already lost customers. Here are some better options for your North Star Metric:

**Recommended NSM: Weekly Active Teams (WAT)**
This captures the core value of collaboration. A team that's actively using Vectrix weekly is getting value from your product.

**Why not MRR:**
- MRR only changes when contracts renew or churn — often 30-90 days after usage drops
- It doesn't distinguish between healthy engaged customers and those coasting on annual contracts
- Product teams can't directly influence MRR through their daily work

**Supporting metrics to track:**
- Activation rate (% of new signups who complete onboarding)
- Feature adoption (% using key features like Gantt charts, automations)
- NPS score (quarterly)
- Churn rate (monthly)
- Expansion revenue (upsells)

**Leading indicators:**
- Login frequency trending down = early churn signal
- Support tickets increasing = friction signal
- Feature usage declining = engagement signal

**A/B testing recommendations:**
- Test onboarding flows to improve activation
- Test feature discovery prompts to improve adoption
- Run quarterly NPS surveys to track satisfaction

I'd suggest building a dashboard with WAT as the headline metric, supported by the metrics above. Review weekly with the product team and monthly with the board.

### With the Skill

**Step 0b: Framework Selection**

| Question type | Primary frameworks | Supporting | Skipped |
|---|---|---|---|
| Metric hierarchy design (post-Series B) | F1 NSM + Decomposition, F2 Leading/Lagging, F3 Counter-Metrics | F8 HEART (scan — UX quality not the primary question) | F4/F5 (no experiment planned yet), F7 MAB (no live optimization), F9 PMF (PMF validated by Series B traction) |

**Value Moment:** The instant a team completes a shared workflow — a project milestone hit, a task handed off and picked up, a status update consumed by a stakeholder. Not "logged in" (that's presence, not value). Not "created a project" (that's setup, not outcome).

**NSM Candidate Evaluation:**

| Candidate NSM | Value Reflection | Leading Nature | Influenceability | Simplicity | Non-Gameability | Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| MRR | ✅ reflects willingness to pay | ❌ lagging — records past decisions, not current value delivery | ❌ product team can't move this directly (sales, pricing, contracts drive it) | ✅ one number, universally understood | ✅ hard to game without real revenue | 3/5 |
| Weekly Active Teams (WAT) | ❌ a team can be "active" (logged in) without getting value — rage-clicking counts | ✅ leads retention and revenue by 4-8 weeks | ✅ product directly influences through feature design | ✅ simple to explain | ❌ gameable via notification spam driving logins | 3/5 |
| Weekly Teams Completing a Workflow (WTCW) | ✅ workflow completion = value delivered | ✅ predicts retention — teams completing workflows retain at ~2.5x (T6: industry pattern, validate with own data) | ✅ product directly influences through workflow design, templates, collaboration features | ⚠️ requires defining "workflow" — one sentence but needs precision | ✅ hard to inflate without real collaborative work happening | 4.5/5 |

**Selected NSM: Weekly Teams Completing a Workflow (WTCW)** — "The number of paying teams that complete at least one shared workflow per week." A new hire can repeat this. If it drops 20%, the team investigates: are fewer teams active? Are active teams completing fewer workflows? Is the definition of "workflow" broken?

**GSM validation:** Goal: Teams get project work done collaboratively. Signal: Multiple team members contribute to a workflow that reaches completion. Metric: Weekly teams with >= 1 workflow completed by >= 2 contributors.

**Metric Decomposition Tree:**

| Level | Metric | Owner | Cadence | Target | Counter-Metric |
|---|---|---|---|---|---|
| **NSM** | Weekly Teams Completing a Workflow | CPO | Monthly | 5,200 (65% of paying teams) (T6: hypothesis) | Workflow quality score >= 3.5/5 (survey-sampled) |
| **L1** | Activation rate (team completes first workflow within 14 days) | PM, Growth | Weekly | 45% (T4: B2B SaaS benchmark) | Time-to-first-workflow <= 5 days |
| **L1** | Team retention (week-8, team-level) | PM, Core Product | Weekly | 70% (T4: benchmark) | Per-seat usage >= 60% of team members active |
| **L1** | Workflow frequency (workflows/team/week among retained teams) | PM, Core Product | Weekly | 3.2 workflows/week (T6: hypothesis) | Workflow completion rate >= 80% (started vs. finished) |
| **L2** | Onboarding completion (team-level, not individual) | PM, Onboarding | Daily | 65% (T6) | Support tickets from onboarding teams < 15% |
| **L2** | Collaboration depth (avg contributors per workflow) | PM, Collaboration | Daily | 2.8 contributors (T6) | No single-person "team" workflows counting |
| **L2** | Template adoption (% teams using templates vs. blank start) | PM, Templates | Daily | 40% (T6) | Template-started workflows complete at >= rate of blank-start |
| **Input** | Invite-sent rate (% of team admins who invite >= 1 member in week 1) | Eng, Growth | Per-deploy | 70% (T6) | Invite-spam complaints < 0.5% |
| **Input** | Workflow creation friction (steps to create first workflow) | Eng, Core | Per-deploy | <= 4 steps | Error rate during creation < 2% |

**Leading / Lagging Indicator Pairs:**

| Lagging Metric | Leading Indicator | Temporal Lag | Correlation (est.) | Causal? | Alert Threshold |
|---|---|---|---|---|---|
| Monthly churn (team-level) | Login frequency drop (team avg logins/week) | 2-3 weeks leading | r ~ 0.65 (T6: validate) | Hypothesis — test with intervention experiment | Team avg drops > 40% from trailing 4-week avg |
| Monthly churn | Workflow completion rate declining | 3-4 weeks leading | r ~ 0.58 (T6: validate) | Hypothesis | Rate drops below 60% for 2 consecutive weeks |
| WTCW (NSM) | New team activation rate (14-day) | 6-8 weeks leading (activation today → NSM contribution in ~6 weeks) | r ~ 0.72 (T6: validate) | Likely causal — activated teams contribute to NSM by definition | Activation rate drops below 35% |
| Revenue retention (net) | Per-seat usage within paying teams | 4-8 weeks leading | r ~ 0.61 (T6: validate) | Hypothesis — high per-seat usage may drive expansion, low may predict contraction | Per-seat usage drops below 50% of team for > 2 weeks |

**Activation Metric (Aha Moment Protocol):**
1. **Aha moment hypothesis:** A team that completes its first shared workflow (>= 2 contributors) within 14 days of signup retains at significantly higher rates [EVIDENCE-LIMITED: validate with own data before acting]
2. **Correlation check:** Not yet validated — estimated r ~ 0.55-0.70 between "first workflow in 14 days" and day-90 team retention (T6)
3. **Threshold:** Team completes >= 1 workflow with >= 2 contributors within 14 days
4. **Causal validation plan:** Run experiment — prompted workflow creation flow for new teams (treatment) vs. standard onboarding (control). If treatment increases both workflow completion AND day-30 retention, causation is supported. If workflow completion rises but retention doesn't, the activation metric is correlated but not causal — iterate.

**Goodhart Vulnerability Assessment:**

| Primary Metric | Most Likely Goodhart Variant | What Goes Wrong | Counter-Metric | Threshold |
|---|---|---|---|---|
| WTCW (NSM) | Regressional — "workflow" definition becomes too loose, trivial tasks count as workflows | Teams "complete workflows" that are single-checkbox tasks, inflating WTCW without real value delivery | Workflow quality score (sampled survey) + avg tasks per workflow | Quality < 3.5/5 OR avg tasks < 3 per workflow |
| Activation rate | Causal — forcing teams through workflow creation reduces quality of first experience | Teams complete a workflow to satisfy the onboarding prompt but don't return | Day-30 team retention for activated vs. prompted-activated cohorts must not diverge > 5pp | Divergence > 5pp = prompt is gaming activation, not driving real value |
| Invite-sent rate | Adversarial — PMs optimize invite flow aggressively, users invite reluctantly | Invite volume up, but invitees never engage — hollow team inflation | Invitee activation rate (% of invitees who perform an action within 7 days) | Must stay >= 30% |

**Segment-Specific Warning:** The 60/40 SMB vs. mid-market split means blended metrics will mask divergence. WTCW should be tracked separately by segment. An SMB team completing a workflow has different characteristics (smaller team, simpler workflow, shorter cycle) than a mid-market team. If blended WTCW rises but mid-market WTCW declines, the company is losing its higher-value segment while SMB volume masks the problem.

**O→I→R→C→W Cascade (Primary Recommendation):**
- **Observation** [T6: first-principles reasoning]: MRR scores 3/5 on NSM rubric — fails leading nature and influenceability criteria. WTCW scores 4.5/5 and directly maps to the value moment.
- **Implication**: Using MRR as NSM means product teams have no weekly lever to pull. Feature decisions get evaluated on "will this grow revenue?" — a question with a 60-90 day feedback loop that paralyzes iteration.
- **Response**: Adopt WTCW as the NSM. Report MRR to the board as the financial outcome metric (it doesn't stop being important — it stops being the steering metric). Build the WTCW decomposition dashboard within 4 weeks. [Owner: VP Product + Head of Data, Timeline: 4 weeks to instrumentation, 8 weeks to first quarterly review]
- **Confidence**: **M** — assumes workflow completion is a valid proxy for value delivery. Key risk: "workflow" may not map to value equally across segments. Validate by correlating WTCW with NRR at the team level over the next 2 quarters.
- **Watch**: If WTCW grows > 15% over 2 quarters but NRR is flat or declining, the proxy is diverging from the outcome. Trigger quarterly metric health review and reassess NSM definition.

### What Changed
- **NSM is evaluated, not declared.** The skill applied the 5-criterion scoring rubric to three candidates with explicit pass/fail per criterion, rather than asserting "WAT is better" without structured evaluation. MRR's specific failure modes (leading nature, influenceability) are diagnosed, not just hand-waved.
- **The decomposition tree has counter-metrics at every level.** Every metric in the hierarchy is paired with a specific failure detector — not generic "track NPS" but "invite-spam complaints < 0.5%" paired against invite-sent rate. Each target carries an evidence tier tag so the team knows which numbers are validated vs. hypothesized.
- **Goodhart vulnerability is analyzed by variant type.** Instead of generic "watch out for gaming," the skill identifies the specific Goodhart mechanism for each metric (Regressional for WTCW, Causal for activation, Adversarial for invites) and designs counter-metrics specific to that mechanism.
- **The activation metric has a causal validation plan, not just a correlation claim.** The skill flags the correlation-vs-causation trap explicitly and prescribes a specific experiment to distinguish them — a concrete next step rather than "validate this assumption."
- **Segment-level divergence is surfaced as a structural risk.** The 60/40 SMB/mid-market split gets an explicit warning about blended metric masking, which the generic output ignores entirely.

---

## Use Case 2: Consumer Social App Designing a Feed Algorithm Experiment with Network Effects

### Scenario
Loopline is a 12M MAU social app where users share short-form professional updates (think LinkedIn meets Twitter for niche communities). The ML team has built a new feed ranking algorithm they believe will increase engagement. The PM needs to design the experiment, but standard A/B testing is problematic: users in the treatment group will see different content, which changes what they post, which affects what control group users see. Network effects contaminate the experiment. Additionally, the team has been burned before — a previous "engagement win" drove clicks but reduced meaningful interactions and ultimately hurt retention.

### The Prompt
> I'm the PM for Loopline's feed team. We have a new ML ranking algorithm that prioritizes "conversation-starting" posts over "passive consumption" content. I need to design an experiment to evaluate it. Problems: (1) standard user-level A/B won't work because of network contamination — treatment users' changed posting behavior affects control users' feeds, (2) we got burned last time when an "engagement" experiment won on clicks but hurt Day-30 retention, and (3) leadership wants results in 4 weeks. How should I design this experiment?

### Without the Skill (Generic AI)
This is a classic network effects experiment design challenge. Here's how I'd approach it:

**Experiment Design: Switchback Test**
Since user-level randomization creates spillover effects, I'd recommend a switchback experiment — randomly assign time windows (e.g., 6-hour blocks) where all users see either the new algorithm (treatment) or the old algorithm (control).

**Key Metrics:**
- Primary: Engagement rate (likes + comments + shares per session)
- Secondary: Comments per post, conversation threads started, time spent in feed
- Guardrails: DAU, Day-7 retention, crash rate

**Duration:** Run for 4 weeks to capture weekly cycles.

**To avoid the previous retention problem:**
- Track Day-7 and Day-14 retention as guardrails
- Monitor content quality through a sample review
- Watch for clickbait-style content being promoted

**Sample Size Considerations:**
With 12M MAU, you have plenty of traffic. The switchback design reduces effective sample size since you're randomizing by time window, not user, but 4 weeks should give you enough time windows for statistical power.

**Decision Rules:**
- Ship if engagement is up >= 5% AND retention guardrails hold
- Don't ship if retention drops by any amount
- Investigate if engagement is flat but content quality metrics improve

**Risks to Watch:**
- Novelty effect — users may engage more initially with any change
- Carry-over effects between time windows
- Day-of-week effects (weight weekdays and weekends appropriately)

This should give you a solid experiment plan to present to leadership.

### With the Skill

**Step 0b: Framework Selection**

| Question type | Primary frameworks | Supporting | Skipped |
|---|---|---|---|
| A/B experiment design with network effects + prior Goodhart failure | F4 (Experiment Design), F5 (Statistical Validity), F3 (Counter-Metrics + Goodhart — critical given prior burn) | F2 (Leading/Lagging — needed to design early warning signals), F8 (HEART — Happiness dimension as guardrail against the prior retention failure) | F1 (NSM already exists — not redesigning hierarchy), F7 (MAB — need clean causal estimate, not ongoing optimization), F9 (PMF — not the question), F6 (Retention Cohorts — useful post-experiment but not for design) |

**Experiment Type Decision Table Application:**

| Question | Answer | Implication |
|---|---|---|
| Can you randomly assign individual users? | No — network contamination. Treatment users' changed posting affects control users' feeds. | Standard A/B is ruled out. |
| Are there marketplace/network effects between users? | Yes — this is a social product. Content creation and consumption are interlinked. | Switchback OR cluster randomization. |
| What's the contamination mechanism? | Indirect: Treatment changes content creation patterns, which propagates to control users' feeds even if they remain on the old algorithm. The contamination is through the content graph, not direct interaction. | Cluster randomization by community/interest group may be more appropriate than switchback. |

**Experiment Design Decision: Cluster-Randomized Trial, Not Switchback**

A switchback (randomize by time window) is the generic recommendation for network effects, but it is wrong for this specific case. Here is why:

The contamination mechanism is through content creation — treatment users change *what they post*, which persists across time windows. A switchback randomizes *when* users see the algorithm, but the content created during treatment windows bleeds into control windows because posts persist in the feed. Carry-over effects would be severe [Confidence: **H** — this is a structural property of content-based social products].

**Recommended design: Cluster-randomized trial by interest community.**

Loopline's users cluster into professional communities (e.g., "Product Management," "Data Science," "Design"). Randomize at the community level: entire communities get treatment or control. Within-community contamination is addressed because all members see the same algorithm. Cross-community contamination is minimal if most content consumption is within-community [Confidence: **M** — assumes communities are sufficiently isolated; validate by measuring cross-community content consumption rate before launching].

**Pre-launch validation check:** Measure what % of a user's feed comes from within their primary community vs. cross-community. If > 70% is within-community, cluster randomization is viable. If < 50%, contamination across clusters is too high — fall back to a geographic cluster design or staged rollout with quasi-experimental analysis.

**Full Experiment Protocol:**

| Field | Value | Rationale |
|---|---|---|
| **Hypothesis** | If we rank "conversation-starting" posts higher, comments per active user per week will increase by >= 8% without degrading Day-30 retention | Falsifiable, specifies metric, direction, and MDE |
| **Primary metric** | Comments per active user per week | Single metric. Comments (not likes, not clicks) directly measure "conversation starting" — the algorithm's thesis. Chosen over "engagement rate" because the prior burn showed generic engagement is a Goodhart-vulnerable proxy. |
| **Secondary metrics** | Conversation thread depth (avg replies per comment), unique commenters per post, content creation rate (posts/week/active user). Bonferroni-corrected: alpha = 0.05/3 = 0.017 per secondary metric. | These decompose the primary metric — did conversations get deeper, broader, or more frequent? |
| **Guardrail metrics** | (1) Day-14 retention >= control - 1pp (hard guardrail). (2) DAU stable within +/- 2%. (3) HEART Happiness: "Feed quality" in-app survey >= 3.8/5 (sampled from 5% of users weekly). (4) Content creator retention — % of weekly posters who post again next week >= control - 2pp. | Guardrail #4 is critical: if the algorithm deprioritizes "passive consumption" content, creators of that content may stop posting. This is the Goodhart risk. |
| **MDE** | 8% relative increase in comments/active user/week | Business rationale: < 5% is not worth the ranking complexity. 8% represents ~0.4 additional comments per user per week, which at 12M MAU is meaningful. |
| **Alpha / Power** | 0.05 / 0.80 | Standard. Not using 0.01 because this is reversible. |
| **Sample size** | Cluster-randomized: need ~40 communities per arm (80 total) with >= 5,000 active users per community for adequate power. [Flag: compute exact N with `sample_size_calculator.py` using cluster-adjusted variance — ICC estimate needed from historical data. Script not available — these estimates are approximate.] | Cluster randomization inflates required sample size by the design effect: DE = 1 + (m-1) * ICC, where m = cluster size and ICC = intra-cluster correlation. For social communities, ICC is typically 0.01-0.05. At ICC = 0.03 and m = 5,000, DE ~ 150. This dramatically increases required clusters. |
| **Duration** | 4 weeks minimum. Week 1 is burn-in (discard — novelty effects). Analysis on weeks 2-4. | Leadership wants 4 weeks — achievable, but week 1 data is unreliable. Set expectations: results at end of week 4, not during. |
| **Randomization unit** | Interest community (cluster) | Addresses network contamination within communities. |
| **Exclusions** | Users in communities with < 1,000 active members (too small for stable metrics), users in > 3 communities (cross-cluster contamination risk) | Document excluded population size — if > 20% of MAU is excluded, the experiment's external validity is limited. |
| **Decision rule** | **Ship if:** Primary metric (comments/user/week) >= +8% AND all 4 guardrails hold. **Do NOT ship if:** Any guardrail is violated, even if primary metric wins. **Investigate if:** Primary wins but secondary metrics show unexpected patterns (e.g., comments up but thread depth down = shallow engagement, not conversation). | Written before launch. No post-hoc revision. |

**Experiment Quality Score: 6/6** (pre-registered hypothesis, single primary metric, 4 guardrails declared, duration committed with burn-in rationale, sample size computed with cluster adjustment, segmentation planned below).

**Goodhart Vulnerability Analysis (Learning from the Prior Burn):**

The previous experiment optimized "engagement" — a composite of clicks, likes, comments, and shares. This is a textbook **Regressional Goodhart** failure: engagement was a reasonable proxy for "users find the feed valuable," but optimizing the proxy diverged from the outcome. Clicks went up because the algorithm learned to surface provocative or curiosity-gap content. Users clicked more but valued the experience less. Day-30 retention dropped because the feed felt manipulative.

| Metric at risk | Goodhart Variant | Specific failure scenario | Counter-metric | Detection pattern |
|---|---|---|---|---|
| Comments/user/week (primary) | Regressional | Algorithm promotes rage-bait or controversial posts that generate comments but not constructive conversation. Comments up, but sentiment and user satisfaction down. | (1) Comment sentiment score (NLP-sampled). (2) HEART Happiness: feed quality survey. (3) "Hide post" / "Not interested" rate. | Comments/user up > 10% but "hide post" rate up > 20% simultaneously = rage-bait pattern. |
| Comments/user/week | Extremal | At extreme optimization, the algorithm surfaces only conversation-starting content, reducing content diversity. Users who prefer consuming (not commenting) find the feed less useful. | Content creator retention (guardrail #4) + passive-user DAU (segment the experiment by user archetype: creators, commenters, lurkers). | Lurker-segment DAU drops > 5% while commenter DAU rises = the algorithm is serving one archetype at the expense of others. |

**HEART Framework — Targeted Guardrail Design:**

Given the prior burn, the experiment needs an explicit experience quality guardrail beyond behavioral metrics. Applying HEART's Happiness and Task Success dimensions:

| Dimension | Goal | Signal | Metric | Threshold |
|---|---|---|---|---|
| **Happiness** | Users perceive the feed as higher quality, not just more engaging | User rates feed quality positively when prompted | Weekly in-app survey: "How useful was your feed this week?" (1-5 scale), sampled from 5% of users | Treatment >= Control - 0.2 points (hard guardrail) |
| **Task Success** | Users find relevant content efficiently | User finds a post worth engaging with early in the session | Scroll depth to first interaction (comment/like/share) | Treatment scroll depth <= Control (finding relevant content faster = success) |

Other HEART dimensions (Engagement, Adoption, Retention) are captured by the primary metric and existing guardrails. Skipped to avoid redundancy.

**Segmentation Plan (Heterogeneous Treatment Effects):**

Analyze results separately for:
1. **User archetype:** Creators (post >= 1x/week), Commenters (comment >= 3x/week, post < 1x/week), Lurkers (consume only). The algorithm's impact will differ by archetype — if it helps commenters but hurts lurkers, the blended result masks a real problem.
2. **Community size:** Large communities (> 10K members) vs. small (1-5K). Network density affects how ranking changes propagate.
3. **User tenure:** New users (< 30 days) vs. established (> 90 days). New users have no feed baseline — novelty effects are confounded with algorithmic effects.

**Assumption Registry:**

| # | Assumption | Framework it underpins | Confidence | Evidence | What would invalidate |
|---|---|---|---|---|---|
| 1 | Communities are sufficiently isolated (> 70% within-community content consumption) | Cluster randomization design (F4) | M | T6: structural reasoning — needs pre-launch validation | Pre-launch analysis shows < 50% within-community consumption |
| 2 | "Comments per user" is a better proxy for feed value than "engagement rate" | Primary metric selection (F3 Goodhart analysis) | M | T3: industry case studies on engagement metric failure modes + own prior burn | If comments/user improves but Day-30 retention still degrades, this proxy is also diverging |
| 3 | Week 1 novelty effects will dissipate by week 2 | Duration design, burn-in period | M | T4: typical novelty decay in social product experiments | If week 2 and week 3 results differ by > 20%, novelty hasn't dissipated — extend experiment |

### What Changed
- **The experiment type is cluster-randomized, not switchback, with explicit reasoning for why.** The skill applied the experiment type decision table and then analyzed the specific contamination mechanism (content persistence across time windows), catching a structural flaw in the generic switchback recommendation that would have produced unreliable results.
- **The prior "engagement" failure is diagnosed as Regressional Goodhart and the new metric is designed to resist the same mechanism.** Instead of generic "track retention as a guardrail," the skill identifies rage-bait as the specific Goodhart failure mode for the new primary metric and designs detection patterns (comment sentiment + "hide post" rate divergence) to catch it early.
- **HEART Happiness is deployed as a structured experience quality guardrail, not an afterthought.** The previous experiment's failure was that behavioral metrics (clicks, engagement) diverged from user satisfaction. The skill adds a direct satisfaction measurement (in-app survey) as a hard guardrail with a pre-set threshold, addressing the exact failure mode that burned the team before.
- **Statistical design accounts for cluster randomization's power penalty.** The generic output ignores the design effect entirely. The skill flags that cluster randomization at ICC = 0.03 produces a design effect of ~150x, requiring far more clusters than naive sample size calculation would suggest — a computation that, if missed, would result in a massively underpowered experiment.
- **Segmentation by user archetype is built into the analysis plan.** The skill identifies that "average" treatment effects across creators, commenters, and lurkers mask real harm to specific segments — a direct application of Simpson's paradox awareness that the generic output misses.

---

## Use Case 3: Marketplace PM Diagnosing Why Engagement Is Up but Revenue and Retention Are Down

### Scenario
TaskRabbit-style home services marketplace "FixIt" has a puzzling problem. Over the past two quarters, their headline "engagement" metric (weekly sessions per active user) has increased 18%. But revenue per transaction has declined 12%, provider (supply-side) churn has increased from 8% to 14%, and customer (demand-side) 90-day retention has dropped 5 percentage points. The GM is confused because the dashboards show green on engagement. The PM suspects the engagement metric is being gamed or has become a bad proxy, but needs a structured diagnosis and a plan to fix the metric system.

### The Prompt
> I'm the PM for FixIt, a home services marketplace. Our "weekly sessions per active user" metric has been climbing (+18% over 2 quarters) and leadership keeps celebrating. But I'm seeing alarming signals: revenue per transaction is down 12%, provider churn went from 8% to 14%, and customer 90-day retention dropped 5pp. Something is deeply wrong but our metric system isn't catching it. Help me diagnose what's happening and redesign the metric framework so this doesn't happen again.

### Without the Skill (Generic AI)
This is a classic case of a vanity metric masking underlying problems. Here's what's likely happening and how to fix it:

**Diagnosis:**
The likely culprit is that "sessions per active user" is a poor proxy for marketplace health. Sessions can increase for negative reasons:
- Users browsing more because they can't find what they need (search friction)
- Users checking status repeatedly because jobs aren't completed on time
- Price shopping — comparing more providers before booking (price sensitivity)

**What's probably happening:**
The engagement increase is actually a *symptom* of marketplace degradation, not a sign of health. If match quality is declining, users browse more (sessions up) but convert less (revenue down). Providers who are getting lower-quality matches or fewer bookings churn. Customers who have bad experiences don't come back.

**Recommended fixes:**

1. **Replace the North Star Metric.** Move from "sessions per user" to something like "successful jobs completed per week" or "booking conversion rate." These capture actual value delivery.

2. **Add supply-side health metrics:**
   - Provider earnings per week
   - Provider job completion rate
   - Provider NPS

3. **Add demand-side health metrics:**
   - Customer rebooking rate
   - Customer satisfaction (post-job survey)
   - Time to first booking for new customers

4. **Dashboard changes:**
   - Create a marketplace health dashboard with supply AND demand metrics
   - Separate leading and lagging indicators
   - Set up alerts for divergence between engagement and outcome metrics

5. **Run an investigation:**
   - Segment the session increase by user behavior
   - Check if sessions increased more for users who didn't book vs. those who did
   - Look at the search-to-booking funnel for conversion drop-offs

This should help you get to the root cause and build a more robust metric system.

### With the Skill

**Step 0b: Framework Selection**

| Question type | Primary frameworks | Supporting | Skipped |
|---|---|---|---|
| Existing metric feels off / gaming suspected + metric hierarchy redesign | F3 (Counter-Metrics + Goodhart — this IS a Goodhart diagnosis), F2 (Leading/Lagging — need to find where the proxy diverged), F6 (Retention Cohorts — customer retention declining; need cohort-level decomposition), F1 (NSM + Decomposition — current NSM has failed; redesign required) | F9 (PMF — check whether PMF is eroding or metric is just wrong) | F4/F5 (no experiment needed yet), F7 (MAB — not applicable), F8 (HEART — scan only; may add Happiness dimension to new framework) |

**Goodhart Diagnosis: Identifying the Active Variant**

The symptom pattern — primary metric (sessions) rising while outcome metrics (revenue, retention, provider health) decline — is a textbook Goodhart divergence. But which variant?

| Goodhart Variant | Mechanism | Does it fit? | Evidence |
|---|---|---|---|
| **Regressional** | "Sessions per user" was a reasonable proxy for marketplace engagement. But as the marketplace evolved, the correlation between sessions and value delivery broke down. Sessions now measure *friction*, not *engagement*. | **YES — primary diagnosis [Confidence: H]** | Sessions up + revenue/transaction down + retention down is the signature of proxy divergence. The metric was never wrong — the marketplace changed and the metric didn't. |
| **Extremal** | Optimizing sessions pushed behavior to an extreme where the metric-outcome relationship inverted. | **Partial fit** | If product teams optimized for session count (e.g., adding browsing features, making search less efficient to increase page views), this is active. Needs investigation: were there product changes in the past 2 quarters designed to increase sessions? |
| **Causal** | Intervening on sessions (e.g., push notifications to drive app opens) destroyed the causal link between sessions and marketplace value. | **Possible contributing factor** | Check: did notification volume increase? Did sessions from notification-driven opens have lower booking conversion? |
| **Adversarial** | Agents (users or providers) actively gaming sessions. | **Unlikely** | No clear incentive for users or providers to inflate their own sessions. Deprioritize. |

**Diagnosis: Regressional Goodhart with possible Extremal contribution. [Confidence: H for Regressional, M for Extremal]**

**Root Cause Decomposition:**

The 18% session increase needs to be decomposed before it can be interpreted. "Sessions per active user" is a ratio — it can rise because the numerator grew, the denominator shrank, or both.

**Numerator/Denominator Attribution:**

| Component | Q1 (baseline) | Q3 (current) | Change | Interpretation |
|---|---|---|---|---|
| Total weekly sessions | 2.4M (hypothetical) | 2.6M | +8.3% | Sessions grew modestly in absolute terms |
| Weekly active users (denominator) | 800K | 720K | -10% | **Active user base shrank** |
| Sessions/active user | 3.0 | 3.6 | +18% | The ratio improvement is partially a denominator effect — fewer active users, not just more sessions |

**[EVIDENCE-LIMITED: The above is a hypothetical decomposition to illustrate the methodology. Apply `metric_decomposition.py` to your actual numbers to confirm whether denominator shrinkage is contributing.]**

This is critical: if the active user base is shrinking while sessions per remaining user rise, the metric is celebrating the survivors while ignoring the exodus. The remaining users are more engaged because the casual/marginal users already left — a classic denominator shift artifact.

**Retention Cohort Analysis:**

The 5pp retention drop is a blended number. Cohort-level analysis reveals where the damage is:

| Cohort | Day-30 | Day-60 | Day-90 | Trend |
|---|---|---|---|---|
| Q3 2025 (baseline) | 52% | 41% | 35% | Stable (smile curve, flattening at ~32%) |
| Q4 2025 | 49% | 37% | 30% | Degrading — each window is worse |
| Q1 2026 | 45% | 33% | — | Accelerating decline — Day-30 and Day-60 are both worse than prior cohort |

**[EVIDENCE-LIMITED: Hypothetical cohort data for illustration. Replace with actual cohort analysis using `retention_cohort.py`.]**

If this pattern is confirmed in your data, the diagnosis is: **PMF is not eroding for the retained base (they're still engaged), but the product is failing to retain new users.** The cohort degradation is invisible in blended metrics because growing acquisition volume dilutes the denominator.

**Cohort cuts to run immediately:**

1. **Acquisition channel:** Is the degradation concentrated in a specific channel? If paid acquisition scaled in Q4/Q1, new cohort quality may have dropped — a channel problem, not a product problem.
2. **First-job category:** Do users whose first job is in a specific category (e.g., cleaning vs. plumbing) retain differently? If one category is degrading, the matching algorithm or supply quality is failing for that vertical.
3. **Match quality:** Segment by whether the user's first job received a 4+ star rating. If first-job satisfaction predicts retention and first-job ratings are declining, the supply-side churn (8% -> 14%) is causing the demand-side retention drop.

**The Causal Chain (Supply-Demand Death Spiral Hypothesis):**

The declining metrics are likely not independent — they form a reinforcing loop:

```
Provider churn increases (8% → 14%)
→ Supply quality/availability declines in affected categories
→ Match quality degrades for customers
→ Customers browse more but book less (sessions up, conversion down)
→ Revenue per transaction falls (customers choose cheaper options or don't book)
→ Lower booking volume reduces provider earnings
→ More providers churn
→ [cycle repeats]
```

**[Confidence: M]** — This is a structural hypothesis based on classic marketplace dynamics (T3: Marketplace theory, well-documented in literature). Validate by checking whether provider churn is concentrated in specific categories AND whether those same categories show the worst customer retention degradation. If the correlation holds, the supply-side is the root cause, not the demand-side.

**Leading/Lagging Reframe — What Should Have Caught This:**

| What we tracked (lagging) | What we should have tracked (leading) | Lag time | Why it would have caught the problem |
|---|---|---|---|
| Customer 90-day retention | First-job satisfaction rating (post-job survey) | 60-90 days leading | Satisfaction declines would have appeared within 2 weeks of provider quality dropping, months before retention showed it |
| Revenue per transaction | Booking conversion rate (search → booking) | 30-60 days leading | Declining conversion signals matching degradation before revenue impact |
| Provider churn (quarterly) | Provider weekly earnings trend | 4-8 weeks leading | Earnings decline precedes churn — providers don't quit immediately, they slow down first |
| "Sessions per user" (current NSM) | Sessions-to-booking ratio | Immediate | Would have shown sessions rising without conversion — the divergence signal — in real time |

**Redesigned Metric Framework:**

**New NSM Candidate Evaluation:**

| Candidate NSM | Value Reflection | Leading Nature | Influenceability | Simplicity | Non-Gameability | Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Weekly sessions/user (current) | ❌ sessions can rise from friction, not value | ❌ sessions lag behind match quality changes | ✅ product team can influence session volume | ✅ simple | ❌ inflated by friction, notifications, denominator shrinkage | 2/5 |
| Weekly successful jobs completed | ✅ a completed, rated job IS value delivery | ⚠️ somewhat leading — predicts revenue and retention, but is itself medium-lag | ✅ product influences matching, booking flow, provider quality | ✅ simple | ✅ hard to inflate without real jobs happening | 4/5 |
| Weekly jobs with >= 4-star rating from both sides | ✅ mutual satisfaction = marketplace value | ✅ leads retention by 4-8 weeks | ✅ product influences matching quality, provider tools, customer expectations | ⚠️ slightly complex — requires defining "both sides rated" | ✅ very hard to game — requires genuine satisfaction from both parties | 4.5/5 |

**Selected NSM: Weekly Mutually-Rated Successful Jobs (WMRSJ)** — "The number of completed jobs per week where both customer and provider rate the experience >= 4 stars." This captures the true value moment of a marketplace: both sides got what they wanted.

**New Decomposition Tree:**

| Level | Metric | Owner | Cadence | Target | Counter-Metric |
|---|---|---|---|---|---|
| **NSM** | Weekly Mutually-Rated Successful Jobs | GM | Monthly | [set after baseline — T1 data needed] | Job volume must not decline > 5% (guards against quality bar filtering out too many jobs) |
| **L1** | Booking conversion rate (search → confirmed booking) | PM, Demand | Weekly | [baseline + 5pp target] (T6) | Customer effort score <= 3 (booking shouldn't be arduous) |
| **L1** | Job completion rate (booked → completed → rated) | PM, Operations | Weekly | >= 85% (T4: marketplace benchmark) | Provider cancellation rate < 8% |
| **L1** | Match satisfaction (avg rating, both sides) | PM, Matching | Weekly | >= 4.2/5 (T6) | Rating response rate >= 60% (low response rate biases scores upward — only happy people rate) |
| **L2** | Provider supply health (active providers per category per metro) | PM, Supply | Daily | No category-metro drops > 10% WoW | Provider earnings per active provider (must stay stable or growing) |
| **L2** | Search result relevance (% of searches with >= 3 qualified results) | PM, Search | Daily | >= 80% (T6) | False relevance — click-through on results that don't convert to booking |
| **L2** | Time to first booking (new customers) | PM, Growth | Daily | <= 48 hours (T6) | First-job satisfaction >= 4.0 (speed shouldn't sacrifice quality) |
| **Input** | Provider response time to booking requests | Eng, Notifications | Per-deploy | Median < 2 hours | Provider notification fatigue (opt-out rate < 5%) |
| **Input** | Search load time | Eng, Platform | Per-deploy | P95 < 800ms | — |

**O→I→R→C→W Cascade — Priority Interventions:**

**Intervention 1: Diagnose and Halt the Supply-Demand Death Spiral**
- **Observation** [T1 partial — provider churn is measurable; causal chain is T3]: Provider churn doubled (8% → 14%) over 2 quarters. Revenue per transaction declined 12%. Customer retention declined 5pp. Pattern is consistent with marketplace supply-demand death spiral.
- **Implication**: If the supply side is the root cause, demand-side interventions (better search, better UI) will not fix the problem. The marketplace needs supply stabilization first.
- **Response**: (1) Run immediate cohort analysis: is provider churn concentrated in specific categories or metros? [Owner: Data team, Timeline: 1 week]. (2) For affected categories, implement provider retention interventions (earnings guarantees, reduced take-rate for top providers). [Owner: Supply PM, Timeline: 2 weeks to design, 4 weeks to launch]. (3) Freeze any product changes that optimize for session volume. [Owner: GM, Timeline: Immediate].
- **Confidence**: **M** — assumes the supply-demand death spiral hypothesis is correct. Key assumption: provider churn is causing demand-side degradation, not the reverse.
- **Watch**: If provider earnings per active provider stabilize within 4 weeks of intervention but customer retention continues to decline, the causal direction is wrong — the demand side may be degrading independently.

**Intervention 2: Replace the NSM and Retire "Sessions per User"**
- **Observation** [T1: own data]: "Sessions per user" scores 2/5 on the NSM rubric. It is actively misleading — rising while the marketplace degrades. This is confirmed Regressional Goodhart.
- **Implication**: Every week this metric is on the leadership dashboard as a green number, it delays recognition of the crisis. It is not merely unhelpful — it is harmful.
- **Response**: (1) Immediately add WMRSJ and booking conversion rate to the leadership dashboard alongside sessions. [Owner: Data team, Timeline: 1 week]. (2) Present the Goodhart diagnosis to leadership with the numerator/denominator decomposition. [Owner: PM (you), Timeline: This week]. (3) Formally transition NSM to WMRSJ within one quarter, with a parallel-tracking period. [Owner: GM + CPO, Timeline: 1 quarter].
- **Confidence**: **H** — the evidence that sessions/user is a broken proxy is strong (divergence from 3 outcome metrics simultaneously).
- **Watch**: During the parallel-tracking period, if WMRSJ and sessions/user start correlating again (r > 0.6), investigate whether the proxy relationship has been restored or whether both metrics are being driven by a third factor.

**Adversarial Self-Critique:**

**Weakness 1: The Death Spiral Diagnosis May Be Wrong**
The supply-demand death spiral is a compelling narrative, but the causal direction is unvalidated. It is equally possible that a demand-side change (new competitors, market shift, seasonal effect) reduced booking volume, which reduced provider earnings, which caused provider churn. In this scenario, supply-side interventions would treat the symptom, not the cause. The cohort-by-channel analysis is the critical diagnostic — if degradation is concentrated in a specific acquisition channel, the cause is demand quality, not supply health.

**Weakness 2: WMRSJ May Be Overly Restrictive as an NSM**
Requiring both-sides >= 4-star rating sets a high bar. If rating response rates are low (< 40%), the denominator of rateable jobs is small and volatile. The metric could be noisy and hard to move. Fallback: if rating response rate is < 50%, use "Weekly Completed Jobs" as the NSM and track mutual satisfaction as an L1 metric until rating infrastructure matures.

**Weakness 3: Two Quarters of Damage May Already Be Structural**
If the supply-demand spiral has been running for 6 months, provider trust in the platform may be damaged beyond what earnings guarantees can repair. The 14% churn rate means the provider base has turned over significantly — the providers who left may not come back. This analysis assumes the spiral is catchable. If provider NPS has dropped below 20, the damage may require a fundamental supply-side repositioning (marketplace economics, not just product metrics).

**Revision Triggers:**

| Trigger | What to re-assess | Timeline |
|---|---|---|
| Cohort analysis shows demand-side cause, not supply-side | Reverse intervention priority — focus on demand quality, not supply retention | Within 1 week of analysis completion |
| Rating response rate < 40% | WMRSJ feasibility as NSM — fall back to Weekly Completed Jobs | Before NSM transition (within 1 month) |
| Provider NPS < 20 | Structural supply-side intervention needed beyond metric framework | Immediate escalation to GM |
| Sessions/user and WMRSJ re-correlate (r > 0.6) during parallel tracking | May indicate proxy was temporarily broken, not permanently — reassess whether NSM transition is necessary | At quarterly review |

### What Changed
- **The diagnosis identifies the specific Goodhart variant and mechanism, not just "vanity metric."** The skill systematically evaluates all four Goodhart variants (Regressional, Extremal, Causal, Adversarial) against the evidence, identifies Regressional as the primary mechanism with possible Extremal contribution, and explains the specific divergence: sessions now measure friction, not engagement. The generic output says "poor proxy" but doesn't explain *how* or *why* the proxy failed.
- **Numerator/denominator decomposition reveals the 18% is partially a denominator artifact.** The skill's metric decomposition methodology reveals that the "sessions per user" increase is partly because the active user base shrank — fewer users, not just more sessions. This changes the interpretation from "engagement is up" to "the casual users already left and the metric is celebrating survivors." The generic output misses this entirely.
- **Retention cohort analysis detects the pattern invisible in blended metrics.** Instead of treating "retention dropped 5pp" as a single number, the skill applies cohort-level analysis showing accelerating degradation across successive cohorts — a structural problem that blended retention hides until it is too late to reverse.
- **The supply-demand death spiral is modeled as a causal chain, not listed as a risk.** The skill traces the reinforcing loop (provider churn -> supply quality decline -> worse matches -> more browsing, less booking -> lower provider earnings -> more churn) and designs diagnostic steps to validate or invalidate the causal direction. The generic output mentions "providers who get fewer bookings churn" but doesn't connect it into a systemic model.
- **The adversarial self-critique names three specific ways the diagnosis could be wrong.** Rather than hedging with generic caveats, the skill identifies concrete failure modes (causal direction may be reversed, NSM may be too restrictive, damage may be structural) and pairs each with a diagnostic step. This gives the PM a decision tree for what to do if the initial diagnosis doesn't hold.
