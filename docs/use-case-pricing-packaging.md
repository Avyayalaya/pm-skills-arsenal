---
layout: default
title: "Pricing & Packaging: CodeLens AI Usage-Based Redesign"
parent: Use Cases
nav_order: 12
---

<script>window.location.href = "{{ site.baseurl }}/showcase/articles/use-case-pricing-packaging.html";</script>

Redirecting to [interactive showcase]({{ site.baseurl }}/showcase/articles/use-case-pricing-packaging.html)...

# Use Case: Pricing & Packaging | CodeLens AI Usage-Based Redesign

**A Complete Pricing Strategy with Unit Economics and Migration Planning**

*Last Updated: March 2026*

---

## Executive Summary

CodeLens AI is a code review tool with 8,200 paying customers at a flat $49/month ($4.8M ARR). The flat-rate model is structurally broken: the top 10% of users (500+ AI reviews/month) consume 62% of AI compute at $0.03/review, creating margin-negative accounts, while the bottom 50% (<20 reviews/month) find $49 too expensive for their usage.

This document applies the **pricing-packaging** skill from the PM Skills Arsenal to design a complete pricing strategy including:

- **Pricing Model Selection** — Hybrid (base + usage) chosen over flat-rate, per-seat, and pure usage-based
- **WTP Assessment** — Van Westendorp (n=47): OPP $58, IDP $72, PME $119
- **Competitive Pricing Map** — 6 competitors mapped; CodeLens positioned as premium AI-native
- **Good/Better/Best Packages** — Starter $29/mo (50 reviews), Pro $69/mo (250 reviews), Enterprise $149/mo (1,000 reviews)
- **Sensitivity Analysis** — Revenue robust across +/-30% price variations
- **Revenue Impact** — Projected $7.4M ARR (+54% uplift) with 8% migration churn
- **AI Cost Patterns** — Per-review metering, cost trajectory analysis, model quality gating
- **Migration Strategy** — 5-phase plan: 6-month grandfather, personalized tier assignment, 20% loyalty discount

**Key Numbers:**

| Metric | Current | Projected |
|--------|---------|-----------|
| ARR | $4.8M | $7.4M |
| ARPU | $49/mo | $81.72/mo |
| Gross Margin | 52% | 68% |
| Margin-Negative Accounts | ~200 | 0 |

---

## Frameworks Applied

1. **Pricing Model Selection** — Decision matrix evaluating per-seat, flat-rate, usage-based, and hybrid models against cost structure, value delivery, buyer predictability, and competitive norms
2. **Van Westendorp Price Sensitivity Meter** — Four-question method for finding the acceptable price range, applied to 47 customer interviews
3. **Competitive Pricing Map** — Price-value positioning against SonarQube, Codacy, DeepSource, Snyk Code, GitHub Copilot, and Cursor
4. **Good/Better/Best Package Architecture** — Tier design with feature allocation rationale, upgrade triggers, and margin analysis
5. **AI/SaaS-Specific Pricing Patterns** — Value metric alignment, marginal cost structure, metering approach, GPU cost trajectory
6. **Sensitivity Analysis** — Revenue impact at 7 price variations plus key variable sensitivity
7. **Revenue Impact Modeling** — Churn risk, grandfathering cost, expansion uplift, net 12-month impact

---

## Evidence Quality

- **54 total evidence points** (T1-T4: 48; T5: 6; T6: 0)
- All pricing recommendations cite minimum 2 evidence tiers
- Core model decision supported by T1 (usage data), T2 (competitive norms), T3 (customer interviews)
- Revenue projections are T4-T5 (directional) — recommend A/B pricing test for T1 validation

---

## Skill Used

**[pricing-packaging](https://github.com/Avyayalaya/pm-skills-arsenal/blob/main/skills/pricing-packaging/SKILL.md)** — Produces pricing and packaging strategy documents with model selection routing, willingness-to-pay assessment, competitive pricing maps, Good/Better/Best package architecture, sensitivity analysis, AI/SaaS-specific pricing patterns, and migration planning.
