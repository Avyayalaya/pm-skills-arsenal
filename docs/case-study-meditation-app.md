---
layout: "default"
title: "Case Study: Meditation App Engagement"
parent: "Case Studies"
nav_order: 2
---

<script>window.location.href = "{{ site.baseurl }}/showcase/articles/case-study-meditation-app.html";</script>

Redirecting to [interactive showcase]({{ site.baseurl }}/showcase/articles/case-study-meditation-app.html)...
# Case Study: Meditation App Engagement Recovery

**Scenario:** Growth PM at Mindful (B2C meditation app, 280K DAU, 920K MAU). DAU/MAU ratio declining from 0.31 to 0.27 over Q1 2026 (Jan–Mar). Absolute DAU down 8% despite MAU holding steady — users installing but not sticking. CEO escalates in weekly all-hands: "We need better engagement. What's the plan?"

**Time:** 110 minutes (spread across 1 week)
**Output:** 5 artifacts — from problem decomposition to exec-approved experiment spec
**Outcome:** 2-sprint onboarding redesign experiment launched, tracked to 14% lift in D7 retention

---

## The Chain

### 1. Problem Framing (15 min)
**Input:** CEO directive "We need better engagement" + DAU/MAU trend (0.31 → 0.27) + no hypothesis on root cause

**Skill invoked:** `/problem-framing`

**Output:** Problem Definition Document (abbreviated)

```markdown
## Problem Statement
DAU/MAU declining 13% (0.31→0.27) over 90 days. Absolute DAU -8% while MAU flat suggests
acquisition is working but retention is broken. "Better engagement" is multi-causal — need
to decompose into testable hypotheses.

## Root Cause Hypotheses (ICE Prioritization)

| Hypothesis | Impact (1-10) | Confidence (1-10) | Ease (1-10) | ICE Score | Evidence Tier |
|------------|---------------|-------------------|-------------|-----------|---------------|
| **(A) Onboarding drop-off** — Users not reaching habit formation milestone (D7) | 9 | 7 | 6 | 42 | **Tier 2** (cohort retention curves show 60% churn by D7) |
| **(B) Day 7 retention cliff** — Specific failure point where habit loop breaks | 8 | 8 | 5 | 40 | **Tier 1** (SQL query shows 68% of D7+ survivors become D30+ users) |
| **(C) Notification fatigue** — Daily reminders perceived as spam, users muting | 6 | 5 | 8 | 39 | **Tier 3** (anecdotal from support tickets, not quantified) |
| **(D) Content staleness** — Library unchanged for 4 months, power users exhausting catalog | 7 | 4 | 3 | 21 | **Tier 4** (assumption, not validated) |

## Prioritized Root Cause
**(A) + (B) are the same problem:** Getting users TO day 7 is the leverage point.
- Current D7 retention: 41%
- D7→D30 retention (for survivors): 68%
- Math: Fixing onboarding to achieve 55% D7 retention would yield +39K DAU (14% lift)

## Confidence Level
**HIGH** on problem frame (evidence tier 1-2 from internal data)
**MEDIUM** on solution direction (have not yet validated WHY users churn before D7)
```

**Key insight:** The problem isn't "engagement" broadly — it's a **day 7 habit formation cliff**. Users who survive to D7 love the product (68% become long-term). The bottleneck is getting them there.

**Handoff to Discovery:** "Validate: (1) What causes D0-D7 churn? (2) Do churned users have common behavioral patterns? (3) Is there a stated vs. revealed preference gap (what users SAY vs. what data shows)? Synthesize: 12 recent churned user interviews, cohort retention data, session recordings from D0-D7 users, most recent NPS survey."

---

### 2. Discovery & Research (25 min)
**Input:** Problem Framing's prioritized hypothesis (D7 retention cliff) + research backlog (12 churned user interviews, cohort data, session recordings, NPS survey results)

**Skill invoked:** `/discovery-research`

**Output:** Research Synthesis Brief (abbreviated)

```markdown
## Research Question
Why do 59% of new users churn before day 7, despite high NPS (72) from retained users?

## Evidence Synthesis (4 sources)

### Source 1: Cohort Retention Analysis (Tier 1 — SQL, 90-day lookback)
- D1 retention: 68% (industry benchmark: 65–70%, ✓ healthy)
- D3 retention: 52% (benchmark: 50–60%, ✓ on par)
- **D7 retention: 41%** (benchmark: 45–55%, ⚠️ below par)
- D7→D30 retention: 68% (for survivors, ✓✓ excellent)
- **Insight:** We don't have an "engagement" problem with retained users. We have an onboarding problem.

### Source 2: Churned User Interviews (Tier 2 — 12 interviews, conducted week of Feb 10)
Top churn reasons (coded):
1. **"I forgot to come back"** (8/12) — no habit formation, app disappeared from routine
2. **"I didn't know what to do after the intro"** (6/12) — unclear next steps after D0 onboarding flow
3. **"I wanted a coach, got a library"** (4/12) — expected guided program, got content catalog
4. "Too many notifications" (2/12)
5. "Not enough content variety" (1/12)

**Pattern:** Onboarding sets wrong expectations OR fails to create habit scaffolding.

### Source 3: Session Recordings (Tier 2 — Fullstory, 50 random D0-D6 churners)
- 78% completed D0 intro (3-min "Welcome to Mindful" guided meditation)
- **Only 34% clicked into content library after intro**
- Of those who clicked library, 62% browsed <30 seconds without playing anything
- **Key UX gap:** After intro ends, user lands on library homepage with 200+ sessions, no guidance

### Source 4: NPS Survey (Tier 2 — quarterly, n=4,200, Feb)
- NPS: 72 (promoters 81%, passives 10%, detractors 9%)
- Top promoter verbatim: "Love the variety, great for wind-down routine"
- **Top detractor verbatim: "Needed more structure, felt overwhelming"**
- **⚠️ STATED VS. REVEALED GAP:** NPS detractors cite "not enough content" (31%), but behavioral
  data shows they churned before exploring >3 sessions. Users blame content when the real issue
  is NAVIGATION/DISCOVERY.

## Synthesis: The Onboarding Problem
**Observation:** Current onboarding is a single 3-min intro, then dumps users into a 200+ session
library with no scaffolding. 68% complete intro, only 34% engage with library. Users who survive
D7 have figured out the library; churners never got oriented.

**Implication:** Habit formation requires (1) clarity on what to do next and (2) early wins to
reinforce return. Current flow provides neither.

**Response Recommendation:** Redesign D0-D7 onboarding as a **7-day guided program** ("Your First
Week") with daily unlock structure, progress tracking, and milestone celebrations at D3/D7.

**Confidence:** HIGH (triangulated across 4 sources, stated/revealed gap identified)

**Watch Indicator:** If D7 retention moves but D7→D30 retention DROPS, we've created a "fake win"
(users completing onboarding but not forming real habit). Counter-metric required.

## Open Questions for Experimentation
1. What is the minimum effective onboarding length? (7 days vs. 3 days vs. 14 days?)
2. Should onboarding be mandatory or optional? (Force flow vs. "Skip to library" escape hatch?)
3. How much does progress visualization matter? (Streak counter vs. milestone badges vs. no gamification?)
```

**Key insight:** This is NOT a content problem or a notification problem. It's an **orientation problem** — users complete the intro, then feel lost in a 200+ session library with no map. The stated preference ("not enough content") is a rationalization; the revealed preference is "I didn't know where to start."

**Handoff to Metric Design:** "Design experiment for 7-day guided onboarding program ('Your First Week'). Primary metric: D7 retention rate (current 41%, target ≥55%). Counter-metric: Session quality (prevent gaming via fast-completion). Power analysis for 2-week test window. Identify trade-offs: Does mandatory onboarding increase D7 at the cost of D1 drop-off?"

---

### 3. Metric Design & Experimentation (25 min)
**Input:** Discovery's recommended intervention (7-day guided onboarding program) + target metric (D7 retention: 41% → ≥55%)

**Skill invoked:** `/metric-design-experimentation`

**Output:** Experiment Design + Metric Framework (abbreviated)

```markdown
## North Star Metric Evaluation

### Candidate: D7 Retention Rate
**Definition:** % of D0 users who return on or after D7 (7-day lookback window)

**NSM Criteria Assessment:**
1. ✓ **Leading indicator:** Predicts D30/D90 retention (68% of D7 survivors → D30+)
2. ✓ **Captures value exchange:** User has formed early habit (proxy for perceived value)
3. ✓ **Actionable by team:** Onboarding changes directly impact D0-D7 experience
4. ✓ **Cross-functional alignment:** Eng (build flow), Design (UX), Content (session selection), Growth (messaging)
5. ⚠️ **Not gaming-resistant alone:** Could be gamed via push spam to hit D7, need counter-metric

**Goodhart Risk:** If we optimize D7 retention without quality gates, we risk inflating the metric
via low-quality engagement (e.g., users opening app to dismiss notification but not meditating).

**Counter-Metric Required:** Session Quality Score = (Total meditation minutes D0-D7) / (Total sessions started D0-D7). Target: ≥6 min/session average (current baseline: 7.2 min/session). If this drops below 6, we're creating hollow engagement.

**Decision:** D7 Retention Rate is the PRIMARY metric. Session Quality Score is COUNTER-METRIC (must not degrade).

---

## Experiment Design

### Hypothesis
Replacing the single 3-min intro with a 7-day guided program ("Your First Week") will increase D7
retention from 41% to ≥55% by providing structure, progress feedback, and habit scaffolding during
the critical formation window.

### Variants

| Variant | Experience | Hypothesis |
|---------|------------|------------|
| **Control** | Current: 3-min intro → library homepage | Baseline: 41% D7 retention |
| **Treatment A** | 7-day guided program (mandatory, no skip) | +14pp lift (55% D7 retention). Risk: D1 drop-off if users reject mandatory flow. |
| **Treatment B** | 7-day guided program (optional, "Skip to Library" CTA) | +8pp lift (49% D7 retention). Lower ceiling but safer (no D1 cannibalization). |

**Recommendation:** Run 3-way test (Control vs. A vs. B) to measure mandatory vs. optional trade-off.

---

## Sample Size & Power Analysis

**Baseline:** 41% D7 retention (control)
**MDE (Minimum Detectable Effect):** +8pp (49% D7 retention)
**Significance level (α):** 0.05
**Power (1-β):** 0.80

**Calculation (per variant):**
- n = 2 × [(Z_α/2 + Z_β)² × p(1-p)] / (MDE)²
- n = 2 × [(1.96 + 0.84)² × 0.41(0.59)] / (0.08)²
- n ≈ 14,200 users per variant

**Total sample required:** 42,600 users (3 variants)
**Current daily new users:** ~3,000/day
**Test duration:** 14 days to reach sample size + 7 days for D7 observation = **21-day test**

**Traffic allocation:** 100% of new users (no holdout) — onboarding is pre-monetization, low risk

---

## Counter-Metrics & Guardrails

| Metric | Baseline | Threshold | Alert Condition |
|--------|----------|-----------|-----------------|
| **Session Quality Score** (min/session, D0-D7) | 7.2 min | ≥6.0 min | If <6.0, experiment is creating hollow engagement — STOP |
| **D1 Retention** | 68% | ≥65% | If <65%, mandatory onboarding is causing D1 churn — fail Treatment A, evaluate B |
| **D30 Retention** (post-test) | 28% | ≥26% | If <26%, D7 lift didn't translate to long-term habit — re-evaluate program design |
| **Session Start Rate** (D0-D7) | 4.1 sessions | ≥3.5 sessions | If <3.5, users completing program but not exploring library — onboarding too rigid |

---

## Statistical Validity Checks

1. **A/A Test (Pre-Flight):** Run 3-day A/A test on control variants to confirm randomization integrity (expect 0pp difference, p>0.05)
2. **Sequential Testing:** Use sequential testing framework (e.g., mSPRT) to enable early stopping if Treatment A hits +14pp at Day 10
3. **Multiple Testing Correction:** 3 variants = 3 comparisons. Use Bonferroni correction: α = 0.05/3 = 0.017 per test
4. **Novelty Effect Control:** Measure D7→D14 retention post-experiment to ensure lift persists beyond initial exposure

---

## Experiment Readiness Checklist

- [ ] Instrumentation: D7 retention event logging (D0 cohort tag + D7 return event)
- [ ] Instrumentation: Session Quality Score (meditation_minutes / sessions_started, D0-D7 window)
- [ ] Randomization: User-level assignment (not session-level), consistent hash on user_id
- [ ] QA: All 3 variants render correctly on iOS/Android (no A/B crosstalk)
- [ ] Rollback plan: Feature flag ready, can revert to Control within 10 min if D1 retention crashes
- [ ] Stakeholder alignment: Eng (2 sprints), Design (assets ready), Content (7-day program finalized), Exec (approved 21-day test window)

---

## Success Criteria

**Primary:** Treatment A or B achieves ≥55% D7 retention (p<0.017) with no counter-metric violations
**Secondary:** Session Quality Score ≥6.0 min/session (no hollow engagement)
**Tertiary:** D1 retention ≥65% (no early churn from mandatory flow)

**Decision Framework:**
- If Treatment A wins: Ship mandatory 7-day program
- If Treatment B wins: Ship optional 7-day program (preserve user agency)
- If both fail: Re-evaluate program design (may be content issue, not structure)
- If A wins but violates D1 threshold: Ship B (optional variant)

**Post-Launch:** Monitor D30 retention 30 days post-ship to confirm long-term habit formation (not just D7 inflation)
```

**Key insight:** This isn't just "run an A/B test" — it's a **statistical decision framework** with counter-metrics, power analysis, multiple testing correction, and guardrails. The D7 metric could be gamed (push spam), so Session Quality Score acts as a fraud detector. Treatment B (optional onboarding) is the safety valve if mandatory flow backfires.

**Handoff to Specification Writing:** "Write spec for Treatment A (mandatory 7-day guided program). Outcome: ≥55% D7 retention, ≥6.0 min/session quality. Acceptance criteria by type: Functional (7 daily unlocks, progress UI, D7 milestone celebration), Performance (page load <2s), Edge cases (user skips a day, what happens?). Failure conditions: If Session Quality Score drops >15% (below 6.1), auto-rollback."

---

### 4. Specification Writing (20 min)
**Input:** Metric Design's experiment structure (Treatment A: mandatory 7-day guided program) + success criteria (55% D7 retention, 6.0 min/session quality)

**Skill invoked:** `/specification-writing`

**Output:** Feature Specification — "Your First Week" Guided Onboarding (abbreviated)

```markdown
# Feature Spec: "Your First Week" Guided Onboarding Program

**Owner:** Growth PM (Parth)
**Sprint:** 2-sprint build (Feb 24–Mar 7)
**Launch:** Mar 10 (21-day experiment window)
**Status:** Approved by Exec 2/23, Eng scoped 2/22

---

## Outcome (North Star)
**Primary:** Increase D7 retention from 41% to ≥55% (+14pp lift)
**Secondary:** Maintain session quality score ≥6.0 min/session (prevent hollow engagement)
**Tertiary:** D1 retention ≥65% (no churn from mandatory flow)

**Success Metric:** 55% of users who start "Your First Week" on D0 return to app on/after D7

---

## User Story
**As a** new Mindful user
**I want** clear guidance on how to build a meditation habit in my first week
**So that** I don't feel lost in the content library and can experience early wins that motivate me to return

---

## Acceptance Criteria

### Functional Requirements

**F1. Program Structure**
- [ ] 7-day guided program ("Your First Week") replaces current 3-min intro
- [ ] Each day unlocks 1 guided meditation session (5–12 min duration)
- [ ] Day 1: "Welcome" (3 min, breathing basics) — matches current intro
- [ ] Day 2: "Body Scan" (8 min)
- [ ] Day 3: "Mindful Moment" (5 min, milestone celebration UI at completion)
- [ ] Day 4: "Stress Release" (10 min)
- [ ] Day 5: "Gratitude Practice" (7 min)
- [ ] Day 6: "Walking Meditation" (12 min)
- [ ] Day 7: "Your Foundation" (8 min, milestone celebration + library unlock)
- [ ] Sessions are MANDATORY in sequence (cannot skip to Day 4 without completing D1-D3)

**F2. Progress Visualization**
- [ ] Home screen shows "Your First Week" card with progress tracker (e.g., "Day 3 of 7 complete ✓")
- [ ] Visual: 7-day calendar with checkmarks for completed days, lock icons for future days
- [ ] Celebration UI at Day 3 ("Halfway there! 🎉") and Day 7 ("You've built your foundation! Library now unlocked 🔓")

**F3. Daily Unlock Logic**
- [ ] Day N unlocks at 12:01 AM local time AFTER Day N-1 is completed
- [ ] Edge case: If user completes Day 1 at 11:00 PM, Day 2 unlocks at 12:01 AM (1 hour later, acceptable)
- [ ] Edge case: If user skips a day (e.g., completes D1 on Mon, returns Wed), Day 2 is STILL available (no penalty for gaps)
- [ ] Edge case: If user completes multiple days in one session (e.g., D1 + D2 back-to-back same day), block this — force 1 day per calendar day to reinforce habit formation

**F4. Notifications**
- [ ] Daily reminder push at user-selected time (default: 7 PM local)
- [ ] Message: "Day [N] is ready: [Session Title]" (e.g., "Day 3 is ready: Mindful Moment")
- [ ] If user has not set reminder time, prompt during D1 completion: "When should we remind you tomorrow?"

**F5. Library Access**
- [ ] Full content library is LOCKED until Day 7 completion
- [ ] "Library" tab shows lock icon + message: "Unlock after completing Your First Week"
- [ ] After D7 completion, library fully accessible + "First Week" program remains in "Programs" section for replay

### Performance Requirements

**P1. Page Load**
- [ ] "Your First Week" home card loads in <2s on 4G connection (p95)
- [ ] Session video/audio starts playing within 3s of tap (p95)

**P2. Instrumentation**
- [ ] Log event: `onboarding_day_N_started` (timestamp, user_id, day_number)
- [ ] Log event: `onboarding_day_N_completed` (timestamp, user_id, day_number, session_duration_sec)
- [ ] Log event: `onboarding_program_completed` (timestamp, user_id) — fires on D7 completion
- [ ] Log event: `d7_return` (timestamp, user_id, days_since_d0) — fires on first return D7+

### Edge Cases & Error Handling

**E1. User Force-Closes Mid-Session**
- [ ] Resume from last playback position (not restart from beginning)
- [ ] Day is marked "complete" only if ≥80% of session is played (prevent gaming via 10-sec opens)

**E2. User Reinstalls App Mid-Program**
- [ ] Progress persists via backend sync (not just local storage)
- [ ] If user completed D1-D3, reinstalls, they resume at D4 (not reset to D1)

**E3. User Changes Time Zone Mid-Program**
- [ ] Day unlock logic uses UTC offset at time of D0 start (consistent clock)
- [ ] If user travels from PST → EST mid-program, unlock times shift with device clock

**E4. User Completes Program, Then Churns, Then Returns**
- [ ] If user returns after D30, offer "Start a New Week" CTA (replay program)
- [ ] Do NOT force re-onboarding (they already graduated)

### Failure Conditions (Auto-Rollback)

**Rollback triggers (monitored in real-time during experiment):**
1. **D1 retention drops below 65%** (from 68% baseline) → indicates mandatory flow causing early churn
2. **Session Quality Score drops below 6.1 min/session** (from 7.2 baseline, >15% decline) → indicates hollow engagement
3. **Crash rate >2%** on "Your First Week" flows (iOS or Android)
4. **Page load time p95 >5s** (UX unacceptable)

**Rollback process:**
- Feature flag: `onboarding_first_week_enabled` (default: false)
- If rollback triggered: Flip flag to false, all new users revert to Control (3-min intro)
- Users mid-program: Allow completion (do not disrupt active cohort), but stop new enrollments

---

## Out of Scope (v1)

- [ ] Personalized session recommendations (Day 1-7 are fixed for all users)
- [ ] Social features (e.g., "Invite a friend to join Your First Week")
- [ ] Localization (v1 is English-only, Spanish/French in v2)
- [ ] "Skip to Library" escape hatch (Treatment B variant, tested separately if A fails)

---

## Open Questions for Engineering

1. **Backend:** How do we handle day unlock logic for users who cross time zones? (Proposal: store D0 timezone offset, use consistent clock)
2. **iOS/Android:** Can we block "complete D1+D2 same day" logic client-side, or need server-side validation? (Prefer server-side to prevent client manipulation)
3. **Analytics:** Session Quality Score (min/session) — calculate real-time or batch post-day? (Need real-time for rollback trigger)

---

## QA Scenarios

| Scenario | Expected Behavior | Test Status |
|----------|-------------------|-------------|
| User completes D1 at 11 PM, returns 1 hour later (12:01 AM) | D2 unlocks, available immediately | ⏳ Pending |
| User completes D1 on Mon, skips Tue, returns Wed | D2 is available Wed (no penalty) | ⏳ Pending |
| User completes D3, tries to tap D4 same day | D4 locked, toast message: "Come back tomorrow for Day 4!" | ⏳ Pending |
| User force-closes app at 50% of D2 session, reopens | Resumes at 50% mark, progress saved | ⏳ Pending |
| User plays 90% of D2 session, closes | Day 2 marked complete (≥80% threshold met) | ⏳ Pending |
| User plays 70% of D2 session, closes | Day 2 NOT marked complete (toast: "Finish today's session to unlock tomorrow") | ⏳ Pending |
| Session Quality Score drops to 5.8 min/session during test | Auto-rollback triggered, feature flag flipped to false | ⏳ Pending |
| User completes D7, taps Library tab | Full library accessible, lock icon removed | ⏳ Pending |

---

## Dependencies
- **Content Team:** 7 guided meditation sessions finalized (script + audio recorded) by Feb 28
- **Design:** Progress tracker UI mockups approved by Feb 25
- **Engineering:** Feature flag infrastructure (rollback-ready) by Feb 26
- **Analytics:** Real-time dashboard for D1 retention + Session Quality Score by Mar 9 (1 day before launch)

---

## Launch Plan
1. **Mar 10:** Enable feature flag for 100% of new users (no gradual rollout — need 14K/variant ASAP)
2. **Mar 10-13 (Days 1-3):** Monitor D1 retention hourly (rollback if <65%)
3. **Mar 17-24 (Days 7-14):** Monitor D7 retention daily (goal: ≥55%)
4. **Mar 24:** Analyze results, decide ship/kill/iterate
5. **Mar 31:** If shipped, measure D30 retention (goal: no drop from 28% baseline)
```

**Key insight:** The spec is NOT just "build a 7-day program" — it's a **decision-ready artifact** with auto-rollback conditions, edge case handling, QA scenarios, and statistical guardrails. If Session Quality Score drops >15%, the spec gives Eng authority to kill the experiment without PM approval (speed over bureaucracy).

**Handoff to Narrative Building:** "Need exec narrative to justify 2-sprint build (opportunity cost: delays other roadmap items). Narrative must answer: (1) Why onboarding, not content or notifications? (2) Why mandatory flow (Treatment A) vs. optional (Treatment B)? (3) What's the ROI if we hit 55% D7 retention? (4) What's the risk if we DON'T fix this? Use all prior outputs (Problem Framing's DAU/MAU decline, Discovery's stated vs. revealed gap, Metric Design's 14% DAU lift projection, Spec's rollback safety net)."

---

### 5. Narrative Building (25 min)
**Input:** Full chain context (Problem Framing → Discovery → Metric Design → Spec) + audience (exec team: CEO, CFO, Head of Product, Head of Eng) + goal (get buy-in for 2-sprint experiment, resource commitment)

**Skill invoked:** `/narrative-building`

**Output:** Executive Narrative — "Why Onboarding is the Leverage Point" (abbreviated, 3-min read)

```markdown
# Executive Brief: The Onboarding Leverage Point

**To:** Exec Team (CEO, CFO, Head of Product, Head of Eng)
**From:** Parth, Growth PM
**Date:** Feb 23, 2026
**Ask:** Approve 2-sprint build for "Your First Week" guided onboarding experiment (Mar 10 launch)

---

## The Problem: Users Love Us. They Just Never Discover It.

Our DAU/MAU ratio dropped 13% this quarter (0.31 → 0.27). The CEO asked for "better engagement."

Here's the insight: **We don't have an engagement problem. We have a discovery problem.**

The data tells a clear story:
- **Users who survive to Day 7: 68% become long-term users (D30+).** They love the product.
- **Users who churn before Day 7: 59% of all new installs.** They never discover what we are.

**The users who stay, stay.** The problem is we're losing them before they get oriented.

This isn't a content problem (our library has 200+ sessions). This isn't a notification problem (D1 retention is healthy at 68%). **This is an onboarding problem.**

---

## What We Learned: The Stated vs. Revealed Preference Gap

We ran 12 churned user interviews. The stated reason for churn: "Not enough content variety."

But the behavioral data revealed the truth:
- 78% of churners completed our 3-min intro
- **Only 34% clicked into the content library after the intro**
- Of those who clicked, 62% browsed <30 seconds without playing anything
- They churned before exploring more than 3 sessions

**They blamed content. But they never engaged with content.** The real issue: After the intro, we dump users into a 200+ session library with no map. They feel overwhelmed, not empowered.

**Our NPS is 72 among retained users.** The users who figure out the library love us. The users who don't, leave.

---

## The Solution: "Your First Week" — Structure the Habit Formation Window

Habit formation research (and our own data) shows Day 7 is the inflection point. Users who cross D7 have formed a routine. Users who don't, forget we exist.

**Proposal:** Replace the single 3-min intro with a 7-day guided program:
- 1 session per day (5-12 min, sequenced for skill-building)
- Progress visualization (daily checkmarks, milestone celebrations at D3/D7)
- Library unlocks after D7 (users earn access by building foundation)

**This isn't gamification. This is scaffolding.** We're not tricking users into engagement. We're giving them structure to discover value before decision fatigue sets in.

---

## The Math: 14% DAU Lift if We Hit Target

**Current state:**
- D7 retention: 41%
- D7→D30 retention (for survivors): 68%
- Projected annual DAU if we do nothing: continue 8% decline (from 280K to 258K)

**Target state (if "Your First Week" succeeds):**
- D7 retention: 55% (+14pp)
- D7→D30 retention: 68% (hold steady, or improve if onboarding creates better habit loops)
- Projected annual DAU: +39K (14% lift from improved retention alone)

**ROI:**
- 2-sprint build cost: ~$80K (Eng + Design + Content)
- Value of +39K DAU: ~$1.2M annual revenue (assuming $30 LTV per DAU)
- **Payback period: <1 month**

**Risk if we DON'T fix this:** DAU continues declining at 2.5%/month. By Q4, we're below 250K DAU. Acquisition cost stays flat, but retention leak means every dollar spent on ads is 15% less effective.

---

## Why Mandatory Flow (Treatment A) Over Optional (Treatment B)?

We're testing both, but here's the logic for Treatment A (mandatory 7-day program, no "Skip to Library" escape):

**Pro:**
- Forces habit formation (users can't opt out of structure)
- Higher ceiling (+14pp D7 lift vs. +8pp for optional variant)
- Aligns with behavioral science: defaulting to the "right path" increases adoption

**Con:**
- Risk: Some users reject mandatory flow, churn at D1 (power users who already know what they want)

**Mitigation:**
- We monitor D1 retention in real-time. If it drops below 65% (from 68% baseline), we auto-rollback within 10 minutes.
- Treatment B (optional flow) is the safety valve if A backfires.

**Why we believe A will win:** Only 9% of churned users cited "too much structure" in interviews. 67% cited "didn't know what to do." The demand signal is for MORE guidance, not less.

---

## The Safety Net: Auto-Rollback Conditions

This isn't a "build and pray" experiment. We've instrumented real-time rollback triggers:

1. **D1 retention drops below 65%** → mandatory flow is causing early churn, revert to Control
2. **Session Quality Score drops below 6.1 min/session** → we're creating hollow engagement (users opening app to dismiss notifications, not meditating), kill experiment
3. **Crash rate >2%** → UX broken, revert

**Engineering has authority to rollback without PM approval.** Speed over bureaucracy.

---

## The Ask: 2 Sprints, 21-Day Test, 1 Decision Point

**Timeline:**
- **Feb 24–Mar 7:** Build (2 sprints)
- **Mar 10:** Launch to 100% of new users
- **Mar 10-24:** 14-day test window (need 14K users/variant for 80% power)
- **Mar 24:** Analyze results, decide ship/kill/iterate
- **Mar 31:** Post-ship D30 retention measurement (confirm long-term habit formation)

**Opportunity cost:** Delays 2 other roadmap items (social sharing feature, content personalization v2).

**Why this is the right trade-off:** Social sharing and personalization improve engagement for **retained users**. Onboarding fixes the retention leak for **churning users**. If we don't fix the leak, every other feature has 14% less reach.

---

## What Success Looks Like

**March 24 outcome scenarios:**

| Scenario | Result | Decision |
|----------|--------|----------|
| **A: Treatment A wins (≥55% D7 retention, no counter-metric violations)** | Ship mandatory 7-day program to 100% | Winner |
| **B: Treatment B wins (≥49% D7 retention, Treatment A violated D1 threshold)** | Ship optional 7-day program (preserve user agency) | Acceptable |
| **C: Both fail (<49% D7 retention)** | Re-evaluate program design (may need content changes, not just structure) | Learn & iterate |
| **D: Treatment A wins BUT Session Quality Score drops >15%** | Kill experiment (hollow engagement = fake win) | Protect long-term health |

**Post-launch (Mar 31):** If we ship, measure D30 retention. Goal: ≥28% (hold baseline). If D30 retention DROPS, we've created a "fake win" (users completing onboarding but not forming real habit). That triggers a deeper product review.

---

## The Bottom Line

**The users who stay, stay.** Our D7→D30 retention (68%) proves the product has enduring value.

**The problem is getting users TO Day 7.** Right now, 59% never make it. They leave before discovering what we are.

"Your First Week" is the bridge. It's structure for the critical habit formation window. It's a map when users feel lost.

**This is the leverage point.** Fix onboarding, and every downstream metric improves: D30 retention, LTV, CAC efficiency, NPS.

**Ask:** Approve 2-sprint build, Mar 10 launch, 21-day test window. Rollback-ready if metrics degrade. Decision point Mar 24.

Let's ship the map.

---

**Approval signatures:**
- [ ] CEO (strategic priority)
- [ ] CFO (budget approved: $80K build cost)
- [ ] Head of Product (roadmap slot allocated)
- [ ] Head of Engineering (2-sprint commitment)

**Status:** ✅ Approved 2/23/2026
```

**Key insight:** The narrative doesn't lead with "we need better engagement" (vague CEO directive). It reframes the problem: **"The users who stay, stay. The problem is getting them TO Day 7."** This shift — from "engagement problem" to "discovery problem" — changes the conversation from "do more features" to "fix the map." The exec team approves because the narrative shows this is the HIGHEST LEVERAGE intervention (not just one of many options).

**Outcome:** Exec team approved 2-sprint build on Feb 23. Experiment launched Mar 10. Results (Mar 24): Treatment A achieved 56% D7 retention (+15pp lift, p=0.003), no counter-metric violations. Shipped to 100% of users Mar 25. Post-launch D30 retention (measured Apr 24): 31% (+3pp from baseline, confirms long-term habit formation). Estimated annual impact: +42K DAU, $1.3M incremental revenue.

---

## What This Demonstrates

### 1. Complete Growth Initiative (Problem → Ship)
This isn't "use a skill in isolation." It's a **5-skill chain** that takes a vague exec directive ("better engagement") and produces a shipped experiment in 3 weeks. Each skill hands off explicit inputs to the next:
- Problem Framing → "Validate D7 cliff"
- Discovery → "Design experiment for D7 retention"
- Metric Design → "Spec the onboarding flow"
- Specification → "Build exec narrative for 2-sprint commitment"
- Narrative → Exec approval → Ship

### 2. Stated vs. Revealed Preference Analysis (Discovery Skill)
Users SAID "not enough content." Data SHOWED they never explored content. The Discovery skill surfaces this gap (NPS blames content, session recordings show 62% browsed <30 sec). **A Growth PM who takes user feedback at face value will build the wrong thing.** This skill forces triangulation across behavioral + attitudinal data.

### 3. Statistical Rigor (Metric Design Skill)
This isn't "let's A/B test it and see what happens." It's:
- **Power analysis** (14K users/variant for 80% power at +8pp MDE)
- **Counter-metrics** (Session Quality Score prevents gaming)
- **Multiple testing correction** (Bonferroni adjustment for 3 variants)
- **Sequential testing** (early stopping if Treatment A hits +14pp at Day 10)
- **Novelty effect control** (measure D7→D14 retention post-experiment)

**A Growth PM without this rigor ships experiments that are underpowered (false negatives) or gamed (Goodhart's Law).** This skill embeds statistical thinking into the PM workflow.

### 4. Auto-Rollback Safety Net (Specification Skill)
The spec gives **Engineering authority to kill the experiment without PM approval** if:
- D1 retention drops below 65%
- Session Quality Score drops below 6.1 min/session
- Crash rate >2%

This is CRITICAL for growth experiments where metrics can degrade fast. The spec isn't just "what to build" — it's "when to stop building."

### 5. Narrative Reframes the Problem (Narrative Skill)
The CEO said "better engagement." The narrative reframes to **"The users who stay, stay. The problem is getting them TO Day 7."** This shift is strategic: it moves the conversation from "do more features" (unbounded) to "fix the onboarding map" (scoped). The exec team approves because the narrative shows THIS IS THE LEVERAGE POINT (not just one option among many).

### 6. Realistic Growth PM Challenges
A Growth PM reading this should recognize:
- **Vague exec directives** ("better engagement" is not a strategy)
- **Stated vs. revealed preference gaps** (users blame content when the real issue is navigation)
- **D7 habit formation cliff** (meditation apps live or die on week-1 retention)
- **Counter-metric design** (prevent gaming via Session Quality Score)
- **Opportunity cost trade-offs** (this experiment delays 2 other roadmap items)
- **Real-time rollback decisions** (if D1 drops, you have 10 minutes to revert)

**This is the daily work of a Growth PM.** The skills chain automates the rigor (so you don't forget the power analysis or counter-metric), but the judgment calls (mandatory vs. optional flow, 7 days vs. 3 days, auto-rollback thresholds) remain human.

---

## Time Breakdown

| Skill | Time | Output |
|-------|------|--------|
| **Problem Framing** | 15 min | Problem Definition Doc (4 root causes, ICE prioritization, D7 cliff identified) |
| **Discovery & Research** | 25 min | Research Synthesis Brief (12 interviews, cohort data, session recordings, NPS — stated vs. revealed gap) |
| **Metric Design & Experimentation** | 25 min | Experiment Design (3 variants, power analysis, counter-metrics, rollback triggers) |
| **Specification Writing** | 20 min | Feature Spec (acceptance criteria by type, edge cases, QA scenarios, auto-rollback conditions) |
| **Narrative Building** | 25 min | Executive Brief (reframes problem, shows ROI, gets approval for 2-sprint build) |
| **TOTAL** | **110 min** | **5 artifacts** → problem decomposed, validated, designed, spec'd, approved, shipped |

**Reality check:** This is condensed. In the wild, these steps take 1 week (not 110 min). But the TIME SAVINGS vs. doing this manually:
- No forgotten counter-metrics (Metric Design skill enforces this)
- No underpowered experiments (power analysis auto-generated)
- No vague specs (Specification skill forces edge case enumeration)
- No rambling exec narratives (Narrative skill enforces arc: problem → insight → solution → ROI → ask)

**The skills don't replace PM judgment. They AUTOMATE the rigor so you can focus on strategy.**

---

## Files Referenced (For Transparency)

This case study is synthesized from realistic Growth PM patterns, not a real company. Numbers are plausible:
- **DAU/MAU 0.27-0.31:** Industry benchmark for meditation apps (Calm ~0.33, Headspace ~0.29)
- **D7 retention 41%:** Typical for meditation/habit apps (retention cliff at week 1 is well-documented)
- **D7→D30 retention 68%:** High but realistic (users who cross habit formation threshold have strong retention)
- **NPS 72:** Healthy for consumer subscription apps
- **Session duration 7.2 min:** Matches Calm's reported average session length

**If you're a Growth PM and these numbers feel wrong for YOUR app, adjust them.** The skill chain structure (Problem → Discovery → Metric → Spec → Narrative) is universal. The specific metrics are context-dependent.

---

**Next steps for PM Skills Arsenal users:**
1. Clone this case study structure for YOUR product
2. Replace meditation app context with your domain (e.g., fintech onboarding, SaaS trial conversion, marketplace liquidity)
3. Run the 5-skill chain on a real problem
4. Compare your output to this benchmark (are you hitting the same level of rigor?)

**Feedback loop:** If your real-world run surfaces gaps in the skills (e.g., "I needed to model CAC payback but Metric Design didn't guide me"), file an issue. The skills evolve based on PM needs.
