# Use Cases: Specification Writing

These three use cases demonstrate the transformation from generic AI output to skill-powered output. Each scenario is a realistic, complex specification challenge that product managers face. The "Without" sections represent what competent AI produces without structured methodology. The "With" sections demonstrate the Specification Writing skill's six frameworks in action.

---

## Use Case 1: AI-Powered Semantic Search for a Customer Support Knowledge Base

### Scenario

Your B2B SaaS product has a knowledge base with 12,000 articles. Support agents currently rely on keyword search, which fails when customers describe problems in natural language ("my dashboard is stuck" does not match the article titled "Resolving Dashboard Rendering Timeouts"). You are specifying an AI-powered semantic search feature that uses embeddings to return relevant results even when queries do not share keywords with articles. The engineering team has never built an ML-powered feature before.

### The Prompt

> Write a spec for adding AI-powered semantic search to our customer support knowledge base. It should understand natural language queries and return relevant articles even when the query doesn't share exact keywords with the article. Our support agents are the primary users.

### Without the Skill (Generic AI)

**Feature: AI-Powered Semantic Search**

**Overview:** Add semantic search capability to the existing knowledge base to help support agents find relevant articles using natural language queries.

**Requirements:**

1. **Search Input:** Support agents can type natural language queries into the existing search bar.
2. **Semantic Understanding:** The system uses AI embeddings to understand the intent behind queries, not just keywords.
3. **Result Ranking:** Results are ranked by semantic relevance, with the most relevant articles appearing first.
4. **Fallback:** If semantic search produces no results, fall back to keyword search.
5. **Performance:** Search results should appear quickly to maintain agent productivity.
6. **Result Display:** Each result shows the article title, a relevance snippet, and a confidence indicator.

**Technical Approach:**
- Use OpenAI's text-embedding-ada-002 model to generate embeddings for all articles.
- Store embeddings in a vector database (e.g., Pinecone or Weaviate).
- At query time, embed the query and perform cosine similarity search.
- Implement a hybrid approach combining semantic and keyword results.

**Success Criteria:**
- Support agents report improved search experience.
- Reduction in average time to find relevant articles.
- Search relevance is better than keyword-only search in A/B testing.

**Edge Cases:**
- Very short queries (1-2 words)
- Queries in languages other than English
- Newly added articles that haven't been indexed yet

**Timeline:** 4-6 weeks for initial implementation.

*This output is structured and reasonable. A competent engineer would still need to ask: What "quickly" means in ms. What happens when the LLM hallucinates relevance for an unrelated article. Whether the fallback is automatic or user-triggered. What "confidence indicator" looks like and how it is calculated. How newly added articles get indexed and on what delay. Whether this replaces keyword search or supplements it. What "improved search experience" means quantitatively.*

### With the Skill

**Specification: Semantic Search for Support Knowledge Base -- Agents Find Relevant Articles Without Keyword Matching**

> **Spec type:** Product/feature | **Load-bearing frameworks:** F1, F2, F3, F5 | **Supporting:** F4, F6
> **Date:** 2026-02-20 | **Author:** PM | **Decision owner:** VP Support Engineering
> **Zero-Question Score:** 0

**Notation Key:** `[Validated]` = confirmed by stakeholder/data. `[Assumed: verify]` = reasonable assumption, needs sign-off. `[Unknown: TBD]` = explicitly unknown. Confidence: H (>70%), M (40-70%), L (<40%). AC quality: 0 (not testable) through 3 (binary-testable with threshold).

---

**1. Outcome Statement**

**After this spec is executed:** Any support agent can enter a natural-language description of a customer problem into the knowledge base search bar and receive at least one relevant article in the top 3 results for queries where a relevant article exists, without needing to guess the article's keywords or title. **Outcome score: 3** -- binary-testable via relevance evaluation on a test set.

**Verification method:** Run a benchmark set of 200 natural-language queries (compiled from actual support tickets) against the search. An article in the top-3 results is "relevant" if a support lead confirms it addresses the query. Target: relevant-in-top-3 rate >= 80%. `[Assumed: verify -- 80% threshold based on industry benchmarks for semantic search; validate with Head of Support before execution]`

---

**2. Scope: Search Query-to-Result Only -- No Article Authoring, No Analytics, No Agent Feedback Loop**

**IN Scope:**

| # | Capability | Description | AC Reference |
|---|---|---|---|
| S-1 | Semantic query processing | Agent enters natural-language query; system returns ranked results using embedding similarity | AC-1, AC-2 |
| S-2 | Hybrid ranking | Results combine semantic similarity score and keyword match score with configurable weighting | AC-3 |
| S-3 | Fallback to keyword | When semantic search returns zero results above the relevance threshold, system automatically executes keyword search and displays those results with a "Showing keyword results" label | AC-4 |
| S-4 | Result display | Each result shows: article title, 2-sentence contextual snippet (extracted from the most relevant section, not the article intro), and a relevance badge (High / Medium / Low) | AC-5 |
| S-5 | Article indexing pipeline | New/updated articles are embedded and indexed within 15 minutes of publication | AC-6 |

**OUT of Scope:**

| # | Excluded Capability | Rationale | Where/When Addressed |
|---|---|---|---|
| X-1 | Agent feedback mechanism ("Was this result helpful?") | Requires separate data pipeline and model fine-tuning loop; Phase 2 -- backlog item SUPP-892 | Q3 2026 roadmap |
| X-2 | Search analytics dashboard (query volume, zero-result rate, CTR) | Valuable but separate outcome; tracked in SUPP-910 | Q3 2026 roadmap |
| X-3 | Multi-language query support | Current knowledge base is English-only; multi-language is blocked on content translation initiative | After CONTENT-340 completes |
| X-4 | Article quality scoring or gap identification | Different outcome (content improvement vs. search improvement) | Discovery phase in Q3 |
| X-5 | Customer-facing search (only agent-facing in this spec) | Different security model, different UI, different relevance tuning | Separate spec required |

---

**3. Acceptance Criteria**

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-1 | Behavioral | When an agent enters a natural-language query (>3 words) describing a customer problem, the system returns results ranked by semantic relevance within 800ms (measured from query submission to first result rendered). | 3 | `[Assumed: verify -- 800ms target from Support Eng, needs load-test validation]` |
| AC-2 | Behavioral | When a relevant article exists in the knowledge base, it appears in the top 3 results for >=80% of test queries in the 200-query benchmark set. | 3 | `[Assumed: verify -- benchmark set must be compiled and approved by Support Lead before testing]` |
| AC-3 | Behavioral | When hybrid ranking is active, the system combines semantic score (0-1) and keyword score (0-1) using the formula: `final_score = (semantic_weight * semantic_score) + ((1 - semantic_weight) * keyword_score)` where `semantic_weight` defaults to 0.7 and is configurable via admin settings without code deployment. | 3 | `[Assumed: verify -- 0.7 default weight based on industry practice; tune after benchmark testing]` |
| AC-4 | Edge case | When semantic search returns zero results with similarity score above 0.3 (the relevance threshold), the system automatically executes keyword-only search and displays results with the label "Showing keyword results -- try rephrasing for better matches." | 3 | `[Validated -- fallback behavior confirmed with VP Support Eng on 2026-02-18]` |
| AC-5 | Behavioral | Each search result displays: (a) article title, (b) a 2-sentence snippet extracted from the paragraph with highest semantic similarity to the query (not the article introduction), (c) a relevance badge: "High" (similarity >= 0.7), "Medium" (0.5-0.7), "Low" (0.3-0.5). | 3 | `[Assumed: verify -- badge thresholds are initial; adjust after benchmark testing]` |
| AC-6 | Behavioral | When a knowledge base article is created or updated, its embedding is recomputed and the vector index is updated within 15 minutes. The agent does not need to trigger reindexing manually. | 3 | `[Assumed: verify -- 15-min SLA based on current article publication rate of ~20/day; verify infra can sustain]` |
| AC-7 | Non-behavioral | Embedding generation for the full 12,000-article corpus completes initial backfill in <4 hours using batch processing. Cost per full reindex is <$50 at current OpenAI pricing. | 2 | `[Assumed: verify -- cost estimate based on ada-002 pricing as of Feb 2026; verify before execution]` |
| AC-8 | Negative | The system does NOT rerank or filter results based on article view count, article age, or agent history. Ranking is purely relevance-based (semantic + keyword scores). | 3 | `[Validated -- confirmed with VP Support Eng; personalization is Phase 2]` |
| AC-9 | Negative | The system does NOT generate, summarize, or paraphrase article content. It returns existing articles only. No generative AI in the search results. | 3 | `[Validated -- legal review prohibits generated answers in support context until policy update]` |
| AC-10 | Edge case | When an agent enters a query of 1-3 words, the system executes keyword search only (skips semantic search) and does not display the "Showing keyword results" label. Short queries are treated as keyword queries by default. | 3 | `[Assumed: verify -- 3-word threshold is heuristic; validate with benchmark data]` |
| AC-11 | Edge case | When the vector database is unavailable (outage, timeout >2s), the system falls back to keyword search silently and logs the incident. The agent sees results (keyword-only) without an error message. | 3 | `[Assumed: verify -- silent fallback approved by Support Eng; verify with SRE team]` |
| AC-12 | Dependency | OpenAI Embeddings API (text-embedding-ada-002) must be accessible from the production environment with <200ms p95 latency for single-query embedding generation. | 3 | `[Unknown: TBD by 2026-03-01 / Infra team -- production firewall rules not yet verified]` |

**Definition of done:** All AC pass on staging with the 200-query benchmark. AC-2 threshold (>=80% relevant-in-top-3) is the gate for production rollout.

---

**5. Failure Conditions**

| # | Type | Assumption at Risk | Deviation Signal | Escalation Action | Severity |
|---|---|---|---|---|---|
| FC-1 | Integration | OpenAI API returns embeddings with stable dimensionality and consistent semantic quality | Embedding dimensions change, or semantically similar queries produce dissimilar vectors across API calls | STOP. Do not ship. Escalate to Tech Lead -- may require pinning model version or switching to self-hosted model. | Critical |
| FC-2 | Data Model | Knowledge base articles have sufficient textual content for meaningful embeddings | >20% of articles produce embeddings with <0.15 average pairwise similarity to related articles (i.e., embeddings are not differentiating) | STOP. Investigate article quality. Escalate to Content Lead -- may require article enrichment before search improvement is viable. | Critical |
| FC-3 | Integration | OpenAI API latency stays within budget (200ms p95 for single embedding) | p95 latency exceeds 200ms in load testing with 50 concurrent queries | ADJUST: evaluate caching strategy for frequent queries, or switch to self-hosted embedding model. Do not degrade search latency below 800ms AC. | Major |
| FC-4 | Process | The 200-query benchmark set is representative of real agent queries | Benchmark achieves >80% but production usage shows <60% satisfaction (measured by agents abandoning search and browsing manually) | ESCALATE to PM. Benchmark set may be biased. Rebuild benchmark from 30 days of production query logs post-launch. | Major |

**Worst Misinterpretation Test:**
- AC-5 ("2-sentence snippet from most relevant paragraph"): Worst interpretation -- the system returns the first two sentences of the article regardless of relevance. Defense: AC-5 explicitly states "extracted from the paragraph with highest semantic similarity to the query."
- AC-9 ("no generative AI"): Worst interpretation -- the system returns raw article text with no formatting. Defense: AC-5 specifies snippet extraction (extractive, not generative) as the display method.

---

**Assumption Registry**

| # | Assumption | Section | Confidence | Evidence | What Would Invalidate |
|---|---|---|:---:|---|---|
| A-1 | OpenAI ada-002 embedding quality is sufficient for support domain terminology | AC-2 | M | General benchmarks show strong performance on technical text; no domain-specific evaluation yet | Benchmark relevance rate <60% on first test run |
| A-2 | 12,000 articles is within vector DB performance limits for <800ms search | AC-1 | H | Pinecone benchmarks show <100ms for 1M vectors; 12K is well within range | Latency exceeds 400ms at the vector DB layer in load testing |
| A-3 | Support agents will adopt natural-language queries rather than continuing keyword habits | Outcome | M | Anecdotal feedback from 5 agents in discovery interviews | Agent query logs post-launch show >70% of queries are still 1-3 keyword phrases |

---

**Adversarial Self-Critique**

**Weakness 1: Embedding model lock-in**
- **Assumption being made:** OpenAI ada-002 will remain available, affordable, and performant for the product's lifetime.
- **What happens if wrong:** A pricing increase or deprecation forces emergency migration to a different embedding model, which produces different vectors -- requiring full reindex and re-benchmarking.
- **Watch indicator:** OpenAI deprecation announcements; cost-per-query exceeding $0.01 for embeddings.

**Weakness 2: Benchmark-production gap**
- **Assumption being made:** The 200-query benchmark set accurately represents the distribution of real agent queries.
- **What happens if wrong:** The feature passes all benchmarks but fails in production because real queries are shorter, more ambiguous, or domain-specific in ways the benchmark does not capture.
- **Watch indicator:** Post-launch zero-result rate >15% or agent search abandonment rate >25%.

**Weakness 3: The 0.3 relevance threshold is a guess**
- **Assumption being made:** A cosine similarity score of 0.3 meaningfully separates "relevant" from "irrelevant" results for this domain.
- **What happens if wrong:** Too low: agents see irrelevant results ranked as "Low" relevance. Too high: the system falls back to keyword search too often, negating the value of semantic search.
- **Watch indicator:** Fallback-to-keyword rate >40% of queries (threshold too high) or agent complaints about irrelevant results (threshold too low).

### What Changed

- **Outcome anchoring with verification method:** Generic output said "improved search experience"; skill output defines a binary-testable outcome (>=80% relevant-in-top-3 on a 200-query benchmark) with a specific verification protocol.
- **Acceptance criteria by type with quality scores:** Generic output listed 6 vague requirements; skill output produces 12 scored criteria spanning behavioral, non-behavioral, negative, edge case, and dependency types -- including the critical negative criteria (no generative AI, no personalization) that prevent the most likely scope creep.
- **Explicit scope boundaries with named exclusions:** Generic output had no OUT section; skill output names 5 specific adjacent capabilities (feedback loop, analytics dashboard, multi-language, content quality scoring, customer-facing search) with rationale and tracking references.
- **Failure conditions tied to specific assumptions:** Generic output assumed everything works; skill output identifies 4 typed failure conditions (embedding quality degradation, article content insufficiency, API latency budget, benchmark representativeness) with observable signals and escalation paths.
- **Adversarial self-critique exposing real weaknesses:** Generic output had no self-awareness of its own gaps; skill output names 3 genuine weaknesses (model lock-in, benchmark-production gap, arbitrary threshold) with watch indicators that convert uncertainty into monitorable signals.

---

## Use Case 2: Payment Gateway API Contract for Multi-Currency Checkout

### Scenario

Your e-commerce platform is integrating with a new payment gateway (StripeConnect) to support multi-currency checkout for international expansion. The API contract must be implemented by your backend team while the payment gateway's SDK is still in beta. Three downstream services (order management, invoicing, and fraud detection) depend on the payment events this integration emits. A failed payment that is not handled correctly results in either lost revenue (charge not captured) or customer trust violation (double-charge).

### The Prompt

> Write an API contract spec for our StripeConnect payment gateway integration. We need to support multi-currency checkout, handle the full payment lifecycle (authorize, capture, refund), and emit events that our order management, invoicing, and fraud detection services consume. The SDK is still in beta.

### Without the Skill (Generic AI)

**API Contract: StripeConnect Payment Gateway Integration**

**Overview:** Integrate with StripeConnect to process multi-currency payments, supporting the full payment lifecycle including authorization, capture, and refund operations.

**Endpoints:**

1. **POST /payments/authorize** -- Create a payment authorization
   - Request: `{ amount, currency, customer_id, payment_method_id, metadata }`
   - Response: `{ authorization_id, status, amount, currency, created_at }`

2. **POST /payments/{auth_id}/capture** -- Capture an authorized payment
   - Request: `{ amount }` (optional partial capture)
   - Response: `{ capture_id, status, amount, currency }`

3. **POST /payments/{auth_id}/refund** -- Refund a captured payment
   - Request: `{ amount, reason }`
   - Response: `{ refund_id, status, amount, currency }`

4. **GET /payments/{id}** -- Get payment status
   - Response: `{ payment_id, status, amount, currency, timeline[] }`

**Events Emitted:**
- `payment.authorized` -- When authorization succeeds
- `payment.captured` -- When capture completes
- `payment.refunded` -- When refund processes
- `payment.failed` -- When any operation fails

**Error Handling:**
- Use standard HTTP status codes (400, 401, 403, 404, 500)
- Return error objects with code, message, and details fields
- Implement retry logic for 5xx errors with exponential backoff

**Security:**
- All endpoints require API key authentication
- PCI compliance: no raw card data touches our servers
- HTTPS only

**Multi-Currency:**
- Support ISO 4217 currency codes
- Amount specified in smallest currency unit (cents, pence, etc.)
- Currency conversion handled by StripeConnect, not by us

**Idempotency:**
- Support idempotency keys on all write operations to prevent duplicate charges

**Monitoring:**
- Log all payment operations
- Alert on failure rates exceeding thresholds

*This output provides a solid starting point. An engineer would still need to ask: What happens when an authorization expires. What the exact retry policy is (how many retries, what backoff intervals, which errors are retryable). Whether partial captures are supported and if so, what the rules are. What event schema downstream services should expect. What "exceeding thresholds" means specifically. How idempotency keys are generated and what the collision behavior is. What happens during a StripeConnect SDK outage. What the authorization hold duration is. How currency conversion rounding is handled.*

### With the Skill

**Specification: StripeConnect Payment API Contract -- Authorize, Capture, and Refund with Multi-Currency Support and Downstream Event Emission**

> **Spec type:** API contract | **Load-bearing frameworks:** F2, F3, F5 | **Supporting:** F4, F6
> **Date:** 2026-02-20 | **Author:** PM | **Decision owner:** Head of Payments Engineering
> **Zero-Question Score:** 0

**Notation Key:** `[Validated]` = confirmed by stakeholder/data. `[Assumed: verify]` = reasonable assumption, needs sign-off. `[Unknown: TBD]` = explicitly unknown. Confidence: H (>70%), M (40-70%), L (<40%). AC quality: 0-3.

---

**1. Outcome Statement**

**After this spec is executed:** Our checkout service can authorize, capture, and refund payments in any of the 15 launch currencies via StripeConnect, and every payment state transition emits a versioned event that order management, invoicing, and fraud detection consume without requiring those services to call back into the payments service. **Outcome score: 3** -- testable via end-to-end payment lifecycle test in each currency + event consumer verification.

**Verification method:** Execute a full authorize-capture-refund cycle in each of the 15 launch currencies in staging. For each cycle, verify that 3 downstream services receive and acknowledge all emitted events within 5 seconds.

---

**2. Scope: Payment Lifecycle API Only -- No Subscription Billing, No Dispute Handling, No Customer Vault**

**IN Scope:**

| # | Capability | Description | AC Reference |
|---|---|---|---|
| S-1 | Authorization | Create a hold on customer funds in the specified currency; hold valid for 7 days `[Assumed: verify -- StripeConnect beta docs say 7 days; confirm with their team]` | AC-1, AC-2 |
| S-2 | Capture (full and partial) | Capture authorized funds, full or partial. Partial capture releases remaining hold. Only one capture per authorization. | AC-3, AC-4 |
| S-3 | Refund (full and partial) | Refund captured funds, full or partial. Multiple partial refunds allowed up to captured amount. | AC-5, AC-6 |
| S-4 | Idempotency | All write endpoints accept an `Idempotency-Key` header. Duplicate requests with the same key return the original response without re-executing. Keys expire after 24 hours. | AC-7 |
| S-5 | Event emission | Every state transition emits a versioned event to the internal event bus (Kafka). Schema is fixed per event version. | AC-8, AC-9 |
| S-6 | Multi-currency amounts | All amounts in smallest currency unit per ISO 4217. Zero-decimal currencies (JPY, KRW) use whole units. | AC-10 |

**OUT of Scope:**

| # | Excluded Capability | Rationale | Where/When Addressed |
|---|---|---|---|
| X-1 | Subscription / recurring billing | Different authorization model (stored credentials, merchant-initiated transactions); separate spec required | PAY-445, Q3 2026 |
| X-2 | Dispute / chargeback handling | Requires webhook ingestion from StripeConnect + internal dispute workflow; separate spec | PAY-446, Q3 2026 |
| X-3 | Customer payment method vault (save card for later) | PCI scope expansion requires security review; blocked on InfoSec assessment | After SECURITY-201 completes |
| X-4 | Currency conversion display (showing converted amounts to the customer) | Frontend concern; this spec covers the API contract only | Checkout UI spec FRONT-312 |
| X-5 | Payment retry orchestration (automatic retry on soft decline) | Business logic that sits above this API layer; separate spec | PAY-450 |

---

**3. Acceptance Criteria**

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-1 | Behavioral | When `POST /payments/authorize` is called with a valid `amount` (>0), `currency` (one of 15 launch currencies), `customer_id`, and `payment_method_id`, the endpoint returns HTTP 201 with `{ authorization_id, status: "authorized", amount, currency, expires_at }` within 2000ms p95. | 3 | `[Assumed: verify -- 2000ms p95 includes StripeConnect round-trip; validate in beta]` |
| AC-2 | Edge case | When `POST /payments/authorize` is called with a currency not in the 15 launch currencies, the endpoint returns HTTP 422 with `{ error: { code: "UNSUPPORTED_CURRENCY", message: "Currency {X} is not supported. Supported currencies: [list]" } }`. The authorization is NOT created. | 3 | `[Validated -- 15 currencies confirmed by Head of International on 2026-02-15]` |
| AC-3 | Behavioral | When `POST /payments/{auth_id}/capture` is called with no `amount` field, the full authorized amount is captured. When called with an `amount` field where `0 < amount <= authorized_amount`, that partial amount is captured and the remaining hold is released. | 3 | `[Assumed: verify -- partial capture support confirmed in StripeConnect beta docs v0.9; re-verify at v1.0]` |
| AC-4 | Negative | The system does NOT allow more than one capture per authorization. A second `POST /payments/{auth_id}/capture` on an already-captured authorization returns HTTP 409 with `{ error: { code: "ALREADY_CAPTURED" } }`. | 3 | `[Validated -- single-capture model confirmed with Head of Payments Eng]` |
| AC-5 | Behavioral | When `POST /payments/{auth_id}/refund` is called with `amount <= captured_amount - previously_refunded_amount`, the refund is processed. Multiple partial refunds are allowed. | 3 | `[Assumed: verify -- StripeConnect beta supports multiple partial refunds; re-verify at v1.0]` |
| AC-6 | Edge case | When `POST /payments/{auth_id}/refund` is called with `amount > captured_amount - previously_refunded_amount`, the endpoint returns HTTP 422 with `{ error: { code: "REFUND_EXCEEDS_CAPTURABLE", remaining_refundable: N } }`. The refund is NOT processed. | 3 | `[Validated]` |
| AC-7 | Behavioral | When any write endpoint receives a request with an `Idempotency-Key` header that matches a request processed within the last 24 hours, the endpoint returns the original response (same status code, same body) without re-executing the operation. If the in-flight request with the same key is still processing, the endpoint returns HTTP 409 with `{ error: { code: "IDEMPOTENCY_KEY_IN_USE" } }`. | 3 | `[Assumed: verify -- in-flight collision behavior needs Payments Eng sign-off]` |
| AC-8 | Behavioral | Every state transition (authorized, captured, capture_failed, refunded, refund_failed, authorization_expired) emits an event to Kafka topic `payments.events.v1` with schema: `{ event_id, event_type, version: 1, timestamp, payment_id, authorization_id, data: {amount, currency, status, metadata}, idempotency_key }`. | 3 | `[Assumed: verify -- schema must be reviewed by order-mgmt, invoicing, and fraud teams before execution]` |
| AC-9 | Dependency | Order management, invoicing, and fraud detection services each have a consumer deployed to staging that can deserialize `payments.events.v1` schema and acknowledge receipt within 5 seconds. | 3 | `[Unknown: TBD by 2026-03-05 / respective service owners -- consumer readiness not yet confirmed]` |
| AC-10 | Behavioral | All monetary amounts are represented as integers in the smallest currency unit. For zero-decimal currencies (JPY, KRW, VND), the amount represents whole units (e.g., 1000 = 1000 yen). For two-decimal currencies (USD, EUR, GBP), the amount represents cents (e.g., 1000 = $10.00). | 3 | `[Validated -- follows ISO 4217 and StripeConnect's own convention]` |
| AC-11 | Edge case | When an authorization has not been captured within 7 days of creation, the system emits an `authorization_expired` event and marks the authorization as `expired`. A capture attempt on an expired authorization returns HTTP 410 with `{ error: { code: "AUTHORIZATION_EXPIRED" } }`. | 3 | `[Assumed: verify -- 7-day window from StripeConnect beta docs; confirm at v1.0]` |
| AC-12 | Non-behavioral | All endpoints return error responses in the format `{ error: { code: string, message: string, details?: object, request_id: string } }`. The `request_id` is included in every response (success and error) for traceability. | 3 | `[Validated -- error format agreed with frontend team on 2026-02-10]` |
| AC-13 | Negative | The system does NOT store, log, or transmit raw card numbers (PAN), CVV, or full magnetic stripe data. All card data is tokenized by StripeConnect's client-side SDK before reaching our servers. Our API never receives raw card data. | 3 | `[Validated -- PCI DSS SAQ-A compliance requirement]` |
| AC-14 | Negative | The system does NOT perform currency conversion. The `currency` in the authorization request is the currency charged to the customer. If the merchant settlement currency differs, conversion is handled entirely by StripeConnect. | 3 | `[Validated -- confirmed with Head of International]` |

**Definition of done:** Full authorize-capture-refund cycle succeeds in all 15 currencies in staging. All events received by all 3 downstream consumers. Idempotency verified by replaying each write request with same key.

---

**5. Failure Conditions**

| # | Type | Assumption at Risk | Deviation Signal | Escalation Action | Severity |
|---|---|---|---|---|---|
| FC-1 | Integration | StripeConnect beta SDK behaves consistently with their v0.9 documentation | Any endpoint returns an undocumented error code, an unexpected field, or a different status transition than documented | STOP. Do not implement workarounds against undocumented behavior. Escalate to StripeConnect technical contact (Alex R.) and Head of Payments Eng. File beta feedback. | Critical |
| FC-2 | Integration | StripeConnect authorization hold duration is 7 days | Holds are released earlier than 7 days in testing, or StripeConnect changes the hold window in a beta update | STOP capture implementation. Verify new window. If <3 days, escalate to PM -- may require architectural change (immediate capture instead of delayed). | Critical |
| FC-3 | Data Model | All 15 launch currencies are supported by StripeConnect in their current beta | Authorization in any of the 15 currencies returns `UNSUPPORTED_CURRENCY` from StripeConnect | ADJUST: Remove unsupported currency from launch list. Escalate to Head of International for business impact. Do NOT silently convert to a supported currency. | Major |
| FC-4 | Process | Downstream consumers (order-mgmt, invoicing, fraud) can process events within 5 seconds | Any consumer takes >5 seconds or fails to acknowledge events during integration testing | ESCALATE to respective service owner. Do not degrade event emission. The payments API ships even if consumers are delayed -- but flag the consumer gap for tracked resolution. | Major |
| FC-5 | Integration | Idempotency keys are honored by StripeConnect (same key = same response, not re-executed) | Duplicate requests with the same idempotency key produce different authorization_ids or trigger double charges | STOP immediately. This is a double-charge risk. Escalate to StripeConnect and Head of Payments Eng. Do not ship until idempotency is verified. | Critical |

**Worst Misinterpretation Test:**
- AC-3 (partial capture): Worst interpretation -- executor allows multiple partial captures that sum to more than the authorized amount. Defense: AC-4 explicitly limits to one capture per authorization, and AC-3 specifies `amount <= authorized_amount`.
- AC-7 (idempotency): Worst interpretation -- executor implements key matching by request body hash instead of explicit header. Defense: AC-7 specifies `Idempotency-Key` header explicitly.
- AC-13 (no raw card data): Worst interpretation -- executor logs tokenized card data, which is technically "not raw." Defense: AC-13 specifies tokenization happens client-side and our API "never receives raw card data" -- logging is irrelevant because the data never arrives.

---

**Assumption Registry**

| # | Assumption | Section | Confidence | Evidence | What Would Invalidate |
|---|---|---|:---:|---|---|
| A-1 | StripeConnect beta SDK (v0.9) API surface will not change materially before v1.0 GA | All ACs | L | Beta docs disclaimer says "subject to change"; no contractual API stability guarantee | Any breaking change in authorization, capture, or refund endpoints between now and v1.0 |
| A-2 | Single-capture-per-authorization model meets business needs | AC-3, AC-4 | H | Confirmed with Head of Payments Eng; multi-capture is a subscription billing pattern, not checkout | Business request for split shipment capture (partial capture per shipment) |
| A-3 | All 3 downstream consumers can adapt to the v1 event schema before payments API ships | AC-9 | M | Verbal commitment from service owners; no written confirmation or timeline | Any downstream team reports >2 week delay in consumer deployment |

---

**Adversarial Self-Critique**

**Weakness 1: Beta SDK dependency**
- **Assumption being made:** StripeConnect's beta API surface is stable enough to spec against.
- **What happens if wrong:** Breaking changes in the SDK invalidate acceptance criteria, requiring spec revision and rework.
- **Watch indicator:** StripeConnect beta changelog showing breaking changes; any AC that passes in one SDK version and fails in the next.

**Weakness 2: Downstream consumer readiness is unverified**
- **Assumption being made:** Three separate teams will ship event consumers on time, against a schema they have not yet reviewed.
- **What happens if wrong:** Payments API ships but events are not consumed, creating a silent data gap that affects order tracking, invoicing accuracy, and fraud detection.
- **Watch indicator:** AC-9 dependency status still `Unknown` as of 2026-03-01; any downstream team requesting schema changes after spec is finalized.

**Weakness 3: Idempotency collision handling is underspecified for race conditions**
- **Assumption being made:** The "in-flight request returns 409" behavior in AC-7 is sufficient for all concurrency scenarios.
- **What happens if wrong:** Under high load, two requests with the same idempotency key arrive simultaneously before either completes. If both proceed, double-charge occurs.
- **Watch indicator:** Load testing with concurrent duplicate requests; StripeConnect's own idempotency documentation for race condition guidance.

### What Changed

- **Zero-question API contract:** Generic output left engineers guessing about authorization expiry, partial capture rules, idempotency collision behavior, and error response format. Skill output specifies exact status codes, exact error payloads, exact timing windows, and exact edge case behaviors -- engineers can implement without a single Slack message.
- **Failure conditions calibrated to payment risk:** Generic output mentioned "alert on failure rates." Skill output identifies 5 typed failure conditions specific to payment safety (double-charge from idempotency failure, hold window change from beta SDK, unsupported currency) with explicit STOP/ADJUST/ESCALATE actions that prevent the two catastrophic outcomes: lost revenue and double-charges.
- **Scope boundaries preventing API sprawl:** Generic output had no OUT section. Skill output names 5 adjacent capabilities (subscriptions, disputes, card vault, currency conversion display, retry orchestration) that would naturally creep into a "payments integration" if not excluded.
- **Downstream dependency surfaced as explicit blocker:** Generic output assumed downstream services would "just consume events." Skill output makes AC-9 a dependency criterion with `[Unknown: TBD]` annotation and a named deadline, forcing the consumer readiness conversation before execution begins.
- **Beta SDK risk made visible throughout:** Generic output ignored the beta status. Skill output marks every StripeConnect-dependent criterion with `[Assumed: verify]` and dates it to the beta version, and FC-1 is an explicit STOP trigger for undocumented SDK behavior.

---

## Use Case 3: Multi-Role B2B Onboarding Flow with Conditional Paths

### Scenario

Your B2B project management platform is launching a new onboarding flow. The product supports three distinct user roles: Admin (sets up the workspace, manages billing, invites team), Project Manager (creates projects, assigns tasks, configures workflows), and Contributor (views tasks, updates status, adds comments). Each role has a different onboarding path because they need different capabilities on day one. The Admin must complete workspace setup before PMs can create projects, and PMs must create at least one project before Contributors see useful content. A poorly specified onboarding creates a cascade: if the Admin gets stuck, every downstream user is blocked.

### The Prompt

> Write a spec for our new multi-role onboarding flow. We have three roles: Admin, Project Manager, and Contributor. Each needs a different onboarding path. The Admin sets up the workspace first, then PMs create projects, then Contributors are onboarded into existing projects. We need to handle the dependencies between these flows and make sure no role gets stuck.

### Without the Skill (Generic AI)

**Feature Spec: Multi-Role Onboarding Flow**

**Overview:** Design and implement a role-based onboarding experience that guides each user type through the setup steps relevant to their role, ensuring a smooth first-time experience.

**User Roles:**

1. **Admin** -- First user; responsible for workspace configuration, billing, and team invitations.
2. **Project Manager (PM)** -- Creates and manages projects; depends on workspace being set up.
3. **Contributor** -- Task-level user; depends on projects existing.

**Onboarding Flows:**

**Admin Flow (5 steps):**
1. Welcome screen with workspace name input
2. Company profile setup (logo, industry, team size)
3. Billing plan selection
4. Invite team members (with role assignment)
5. Completion screen with "Create First Project" CTA

**PM Flow (4 steps):**
1. Welcome screen personalized to PM role
2. Create first project (name, template selection)
3. Quick tour of project management features
4. Invite team members to project

**Contributor Flow (3 steps):**
1. Welcome screen showing assigned projects
2. Quick tour of task management features
3. Complete a sample task to learn the interface

**Dependencies:**
- PM onboarding requires workspace setup to be complete
- Contributor onboarding requires at least one project to exist
- Admin can skip non-essential steps (logo, industry) but must complete billing

**Progress Tracking:**
- Show a progress bar for each flow
- Allow users to skip non-essential steps
- Save progress so users can return later

**Success Metrics:**
- Onboarding completion rate per role
- Time to first meaningful action per role
- Drop-off rate per step

*This output describes the happy path well. An engineer would still need to ask: What happens when a PM is invited but the Admin has not completed workspace setup. What "skip non-essential steps" means exactly -- which steps are skippable and which are blocking. What happens to a Contributor invited before any project exists. Whether "save progress" means the user sees a partially completed flow or starts over. How role assignment works during invitation -- can an Admin invite someone as Admin. What happens if the Admin abandons onboarding mid-flow -- is the workspace in a broken state. What the "sample task" for Contributors actually is. Whether these flows are web-only or also mobile.*

### With the Skill

**Specification: Role-Based Onboarding Flow -- Admin, PM, and Contributor Paths with Dependency Gating**

> **Spec type:** Product/feature | **Load-bearing frameworks:** F1, F2, F3, F4, F5 | **Supporting:** F6
> **Date:** 2026-02-20 | **Author:** PM | **Decision owner:** VP Product
> **Zero-Question Score:** 0

**Notation Key:** `[Validated]` = confirmed by stakeholder/data. `[Assumed: verify]` = reasonable assumption, needs sign-off. `[Unknown: TBD]` = explicitly unknown. Confidence: H (>70%), M (40-70%), L (<40%). AC quality: 0-3.

---

**1. Outcome Statement**

**After this spec is executed:** Every new user who signs up or accepts an invitation reaches their role-specific "first meaningful action" (Admin: sends first team invite; PM: creates first project; Contributor: updates first task status) within a single session, without encountering a dead-end screen caused by unmet dependencies from another role's incomplete onboarding. **Outcome score: 3** -- binary-testable by running each role through onboarding and verifying no dead-end states exist in every dependency permutation.

**Verification method:** Test matrix covering 6 dependency states (Admin complete/incomplete x PM complete/incomplete x project exists/not-exists). In every state, each role either (a) completes onboarding to first meaningful action or (b) sees an actionable waiting state that tells them exactly what must happen and who needs to do it. Zero dead-end screens in all 6 states.

---

**2. Scope: First-Session Onboarding Only -- No Re-Engagement, No Admin Console, No Mobile**

**IN Scope:**

| # | Capability | Description | AC Reference |
|---|---|---|---|
| S-1 | Admin onboarding path | 4-step guided flow: workspace name (required) -> billing plan selection (required) -> invite team with role assignment (required, minimum 1 invite) -> completion screen | AC-1, AC-2 |
| S-2 | PM onboarding path | 3-step guided flow: welcome with workspace context -> create first project (name + template) -> completion with "invite to project" CTA | AC-3, AC-4 |
| S-3 | Contributor onboarding path | 2-step guided flow: welcome showing assigned project(s) -> guided first task update (pre-created sample task in their assigned project) | AC-5, AC-6 |
| S-4 | Dependency gating | When a user's onboarding depends on another role's action that has not been completed, they see an actionable waiting state (not an error, not a blank screen) | AC-7, AC-8 |
| S-5 | Progress persistence | Onboarding progress is saved per-user. If a user closes the browser and returns, they resume at the last incomplete step, not the beginning. | AC-9 |
| S-6 | Step skippability rules | Only explicitly designated optional steps can be skipped. Required steps block progression. | AC-10 |

**OUT of Scope:**

| # | Excluded Capability | Rationale | Where/When Addressed |
|---|---|---|---|
| X-1 | Re-engagement nudges (email/push for users who abandon onboarding) | Requires notification infrastructure and copy; separate spec | ONBOARD-215, Q3 2026 |
| X-2 | Admin workspace settings beyond onboarding (SSO, security policies, integrations) | Admin console is a separate surface; onboarding covers minimum viable workspace setup only | ADMIN-330 |
| X-3 | Mobile onboarding (iOS/Android) | Web-first decision; mobile onboarding deferred until mobile app redesign | MOBILE-112, H2 2026 |
| X-4 | Onboarding analytics dashboard | Tracking events will be emitted (see AC-14) but the dashboard to visualize them is a separate deliverable | ANALYTICS-445 |
| X-5 | Role change during onboarding (e.g., PM promoted to Admin mid-flow) | Edge case with <1% expected frequency; handle manually via support for now | Evaluate after launch data |
| X-6 | Custom onboarding paths per customer (enterprise customization) | Requires configuration layer; all customers get the same paths in v1 | ENTERPRISE-220 |

**Open Scope Tension:**

```
OPEN TENSION: S-1 (Admin onboarding) requires billing plan selection as a required step,
but some enterprise customers have pre-negotiated contracts and should not see a self-serve
billing screen.
PROPOSED RESOLUTION: For v1, enterprise customers flagged in the CRM skip the billing step
automatically (step is marked complete). The Admin still sees the other 3 steps.
DECISION OWNER: VP Product
DEADLINE: 2026-03-01 -- must resolve before engineering begins step-skippability logic.
```

---

**3. Acceptance Criteria**

**Admin Path:**

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-1 | Behavioral | When the first user signs up for a new workspace, they enter the Admin onboarding flow. Step 1 (workspace name) is required: the "Next" button is disabled until a workspace name of 1-50 characters is entered. Workspace name is persisted immediately on "Next" -- if the Admin closes the tab after Step 1, the workspace exists with that name when they return. | 3 | `[Validated -- workspace persistence requirement from Eng Lead]` |
| AC-2 | Behavioral | Step 3 (invite team) requires the Admin to enter at least 1 email address and assign a role (PM or Contributor) before the "Complete Setup" button is enabled. The Admin can invite up to 50 users in this step. Role options are PM and Contributor only -- the Admin cannot invite another Admin from this flow. | 3 | `[Assumed: verify -- 50-user limit and no Admin invitation from onboarding need VP Product sign-off]` |

**PM Path:**

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-3 | Behavioral | When a user with PM role accepts an invitation and workspace setup is complete (Admin finished onboarding), they enter the PM onboarding flow. Step 1 shows "Welcome to {workspace_name}" with a brief role description. Step 2 requires creating a project: project name (1-100 chars, required) and template selection (from 5 predefined templates + "Blank project", required). | 3 | `[Assumed: verify -- 5 templates need confirmation from Design; currently 3 exist, 2 are in design review]` |
| AC-4 | Behavioral | Upon project creation in Step 2, the system automatically creates a sample task titled "Your first task -- try updating the status" in the new project, assigned to the PM. This sample task is used in Contributor onboarding (AC-6) if a Contributor is later assigned to this project. | 3 | `[Validated -- sample task approach confirmed by VP Product on 2026-02-14]` |

**Contributor Path:**

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-5 | Behavioral | When a user with Contributor role accepts an invitation and is assigned to at least one project that has been created, they enter the Contributor onboarding flow. Step 1 shows "Welcome to {workspace_name}" and lists their assigned project(s) by name. | 3 | `[Validated]` |
| AC-6 | Behavioral | Step 2 presents the sample task (created by AC-4) in their assigned project. The Contributor is guided to change the task status from "To Do" to "In Progress." Upon status change, a success animation plays and the onboarding is complete. The Contributor lands on the project board. | 3 | `[Assumed: verify -- success animation needs Design spec; placeholder OK for engineering but must be replaced before launch]` |

**Dependency Gating:**

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-7 | Edge case | When a PM accepts an invitation but the Admin has NOT completed workspace setup (billing step incomplete), the PM sees a waiting state screen: "Almost ready! {Admin first name} is finishing workspace setup. We'll notify you by email when your workspace is ready. Expected wait: a few minutes." The PM does NOT see an error. The PM does NOT see a partially configured workspace. | 3 | `[Validated -- waiting state design confirmed by Design Lead on 2026-02-16]` |
| AC-8 | Edge case | When a Contributor accepts an invitation but no project has been created yet (PM has not completed onboarding Step 2), the Contributor sees a waiting state screen: "Your workspace is set up! A project manager will create your first project soon. We'll notify you by email when there's a project to explore." | 3 | `[Validated -- waiting state design confirmed by Design Lead on 2026-02-16]` |

**Progress and Navigation:**

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-9 | Behavioral | Onboarding progress is saved per-user in real time (each step completion is persisted within 1 second). If the user closes the browser and returns (same day or later), they resume at the last incomplete step. Completed steps show a checkmark and are reviewable but not re-editable (workspace name cannot be changed from onboarding after Step 1 is complete). | 3 | `[Assumed: verify -- "not re-editable" constraint needs VP Product sign-off; some customers may want to fix typos]` |
| AC-10 | Behavioral | The only skippable step across all flows is Admin Step 2 (company profile: logo and industry). All other steps are required and block progression. The skip button text is "Skip for now" (not "Skip"), and skipped steps appear as "incomplete" in the progress bar with a visual indicator distinct from "not yet reached." | 3 | `[Validated -- skippability rules confirmed by VP Product on 2026-02-14]` |

**Negative and Guard Rail Criteria:**

| # | Type | Criterion | Score | Annotation |
|---|---|---|:---:|---|
| AC-11 | Negative | The onboarding flow does NOT allow a user to change their own role. An Admin who wants to also be a PM must complete Admin onboarding first, then have another Admin (or support) assign them the PM role. Role changes are out of scope for onboarding. | 3 | `[Validated]` |
| AC-12 | Negative | The onboarding flow does NOT allow the Admin to delete the workspace or remove billing information. Destructive actions are only available in the Admin Console (out of scope). | 3 | `[Validated]` |
| AC-13 | Edge case | When an Admin abandons onboarding after Step 1 (workspace created) but before Step 2 (billing), the workspace exists in a "setup_incomplete" state. Users invited to this workspace see the dependency waiting state (AC-7/AC-8). The workspace is NOT automatically deleted. After 14 days of inactivity, the system sends a re-engagement email to the Admin (email content out of scope -- just the trigger). | 3 | `[Assumed: verify -- 14-day threshold and no-auto-delete policy need VP Product sign-off]` |
| AC-14 | Dependency | Each onboarding step emits a tracking event to Segment: `{ event: "onboarding_step_completed", properties: { role, step_number, step_name, workspace_id, time_in_step_seconds } }`. Step skip emits `onboarding_step_skipped` with the same properties. | 3 | `[Validated -- Segment schema approved by Data team on 2026-02-12]` |

**Definition of done:** All 6 dependency state permutations tested (Admin complete/incomplete x PM complete/incomplete x project exists/not-exists). Zero dead-end screens. All roles reach first meaningful action in a single session when dependencies are met.

---

**4. Context and Decisions**

**Executor Profile:**

| Field | Value |
|---|---|
| Executor type | Cross-functional team (2 frontend engineers, 1 backend engineer, 1 designer, 1 QA) |
| Domain familiarity | High (existing team, knows codebase) |
| Available for questions? | Yes -- async via Slack #onboarding-v2 |

**Glossary:**

| Term | Definition | Why Non-Obvious |
|---|---|---|
| Workspace | A single tenant instance containing all projects, users, and settings for one customer. One workspace per paying customer. | Could be confused with "project" or "organization." A workspace contains many projects. |
| First meaningful action | The specific action that confirms the user has successfully started using the product in their role: Admin = sends invite, PM = creates project, Contributor = updates task status. | "Meaningful" is subjective without this definition. It is NOT "logs in" or "views dashboard." |
| Waiting state | A non-error screen shown when a user's onboarding is blocked by another role's incomplete action. Provides context about what is happening and who needs to act. | Could be confused with a loading state or error state. A waiting state has explanatory copy and is an expected, designed experience. |
| Setup_incomplete | Workspace state where the Admin has started onboarding but has not completed the billing step. Functionally, the workspace exists but is not ready for other roles. | Engineers might assume "incomplete" means the workspace should be rolled back. It should not be. |

**Decisions Already Made:**

| # | Decision | Rationale | Date | Decided by |
|---|---|---|---|---|
| D-1 | Web-only for v1, no mobile onboarding | 78% of new signups come from desktop; mobile can reuse the same flow in a future responsive pass | 2026-02-10 | VP Product |
| D-2 | Single Admin per workspace at creation | Multi-admin adds complexity to the invitation step; Admin can promote others post-onboarding via Admin Console | 2026-02-14 | VP Product |
| D-3 | Sample task created automatically, not by the PM | Eliminates the dependency on PM remembering to create a task for Contributor onboarding; sample task is system-generated | 2026-02-14 | VP Product + Eng Lead |
| D-4 | 5 predefined templates + Blank project | Templates reduce time-to-first-project; "Blank" ensures power users are not forced into a template | 2026-02-14 | VP Product + Design Lead |

---

**5. Failure Conditions**

| # | Type | Assumption at Risk | Deviation Signal | Escalation Action | Severity |
|---|---|---|---|---|---|
| FC-1 | Process | Admin completes onboarding within the same day they sign up | >30% of Admins do not complete Step 2 (billing) within 24 hours of starting onboarding | ESCALATE to PM. The dependency gating model assumes Admins complete quickly. If they do not, PMs and Contributors are stuck in waiting states for days, which may cause invitation abandonment. Consider adding an Admin reminder flow or allowing limited PM access to the workspace without billing. | Critical |
| FC-2 | Process | PMs create at least one project during onboarding | >40% of PMs complete onboarding without creating a project (skip or abandon at Step 2) | ADJUST: Evaluate whether Contributor onboarding should have a fallback path that does not depend on a project existing (e.g., a system-generated demo project). Escalate to VP Product for decision. | Major |
| FC-3 | Data Model | The invitation-to-role mapping is 1:1 (each invited user has exactly one role) | Users are invited with multiple roles, or role is not specified at invitation time | STOP. The onboarding routing logic assumes each user maps to exactly one flow. Multi-role users need a role-selection screen that is not in this spec. Escalate to PM. | Critical |
| FC-4 | Authorization | Invited PMs and Contributors can access the workspace immediately upon accepting the invitation | SSO or domain verification requirements block invited users from accessing the workspace until IT approves | ESCALATE to PM and customer success. If enterprise SSO is enabled, the onboarding flow may need to defer to the SSO approval process. This is not handled in the current spec. | Major |

**Worst Misinterpretation Test:**
- AC-7 (PM waiting state): Worst interpretation -- the PM sees the waiting state permanently, even after the Admin completes setup, because the page does not refresh. Defense: AC-7 specifies "We'll notify you by email when your workspace is ready," implying the PM returns via the email link. Add clarification: the waiting state page also auto-refreshes every 60 seconds and transitions to PM onboarding when workspace setup completes.
- AC-10 (skippable steps): Worst interpretation -- an engineer makes ALL Admin steps skippable because the UI pattern exists. Defense: AC-10 explicitly lists "Admin Step 2 (company profile)" as the ONLY skippable step. All others "are required and block progression."
- AC-13 (abandoned workspace): Worst interpretation -- the engineer implements auto-deletion after 14 days. Defense: AC-13 explicitly states "the workspace is NOT automatically deleted" and only an email trigger fires.

---

**Assumption Registry**

| # | Assumption | Section | Confidence | Evidence | What Would Invalidate |
|---|---|---|:---:|---|---|
| A-1 | Admins complete workspace setup quickly enough that PMs and Contributors do not churn from waiting | AC-7, AC-8, FC-1 | M | Industry benchmark: 60% of B2B admins complete setup within 1 hour. No internal data yet. | >30% of PMs/Contributors never return after seeing the waiting state (measured by invitation acceptance -> 7-day retention) |
| A-2 | Each user has exactly one role at onboarding time | All routing logic | H | Current data model enforces 1:1 user-role mapping; multi-role is a future feature | Product decision to support multi-role users, or enterprise request for Admin+PM combo role |
| A-3 | 5 predefined templates are sufficient for first-project creation | AC-3 | M | Based on analysis of 200 existing customer projects; 5 templates cover 85% of structures. But new customers may have novel workflows. | >20% of PMs select "Blank project" in onboarding (suggests templates do not match their mental model) |
| A-4 | The "sample task" approach for Contributor onboarding is more effective than a product tour or video walkthrough | AC-4, AC-6 | M | UX research from 8 user interviews showed preference for "learning by doing." No quantitative A/B test yet. | Contributor onboarding completion rate <60% (suggesting the sample task is confusing or insufficient) |

---

**Adversarial Self-Critique**

**Weakness 1: The dependency chain is fragile**
- **Assumption being made:** A sequential dependency model (Admin -> PM -> Contributor) works because each role completes quickly. In reality, days or weeks can pass between Admin signup and Contributor onboarding.
- **What happens if wrong:** Contributors invited on day 1 see a waiting state for days, never return, and the workspace appears "dead" to the Admin who invited them. The onboarding funnel leaks at the dependency boundaries.
- **Watch indicator:** Median time from Admin signup to first Contributor task update exceeds 7 days; waiting-state page has >50% bounce rate.

**Weakness 2: No recovery path for the stuck Admin**
- **Assumption being made:** If an Admin gets stuck on billing (credit card declined, needs procurement approval, budget not yet allocated), there is no path forward for any user in the workspace.
- **What happens if wrong:** The entire workspace of invited users is blocked by a single billing issue. PMs and Contributors churn before the Admin resolves it.
- **Watch indicator:** >10% of workspaces remain in `setup_incomplete` state for >72 hours; support tickets mentioning "cannot access workspace" from non-Admin users.

**Weakness 3: Sample task may not exist when the Contributor arrives**
- **Assumption being made:** The sample task created in AC-4 persists until the Contributor reaches Step 2. The PM does not delete it, the system does not archive it, and it remains assigned to the Contributor's project.
- **What happens if wrong:** The Contributor reaches Step 2 and the sample task is missing. The onboarding flow breaks -- there is nothing to update.
- **Watch indicator:** Contributor onboarding Step 2 error rate >2%; any "task not found" errors in the onboarding flow logs.

### What Changed

- **Dependency states as first-class specification concern:** Generic output mentioned dependencies in one line. Skill output defines a 6-state test matrix, specifies actionable waiting screens for every blocked state, and makes the dependency chain an explicit acceptance criterion category with dedicated edge case criteria (AC-7, AC-8, AC-13).
- **Executor context model for a cross-functional team:** Generic output assumed the reader was an engineer. Skill output provides a glossary defining "workspace," "first meaningful action," "waiting state," and "setup_incomplete" with explicit notes on what each term does NOT mean -- preventing the most common misinterpretations across engineering, design, and QA.
- **Step-level skippability rules eliminating ambiguity:** Generic output said "allow users to skip non-essential steps" without defining which steps. Skill output names exactly one skippable step (Admin Step 2: company profile), explicitly requires all others, and specifies the visual distinction between "skipped" and "not yet reached" in the progress bar.
- **Failure conditions exposing the dependency chain's fragility:** Generic output did not consider what happens when Admins are slow, PMs skip project creation, or the sample task gets deleted. Skill output identifies 4 failure conditions including the cascade failure (Admin delay blocking all downstream users) with specific thresholds that trigger escalation.
- **Open tension surfaced for enterprise billing exception:** Generic output silently assumed all customers go through self-serve billing. Skill output surfaces the enterprise pre-negotiated contract tension explicitly, proposes a resolution, names the decision owner, and sets a deadline -- preventing a mid-sprint discovery that derails the billing step implementation.

---

## Summary: The Pattern Across All Three Use Cases

The transformation from generic AI output to skill-powered output follows the same structural pattern in every use case:

1. **Outcome anchoring (F1):** Generic output describes features to build. Skill output defines a binary-testable change in the world with a verification method.

2. **Acceptance criteria taxonomy (F2):** Generic output lists requirements. Skill output classifies criteria by type (behavioral, non-behavioral, negative, edge case, dependency), scores each for testability, and includes the negative criteria that prevent scope creep.

3. **Scope boundary protocol (F3):** Generic output has no OUT section. Skill output names specific adjacent capabilities that are excluded, with rationale and future tracking references.

4. **Executor context model (F4):** Generic output assumes a mind-reader executor. Skill output identifies the executor type, fills context gaps (glossary, decisions already made, dependencies with status), and annotates every decision as validated, assumed, or unknown.

5. **Failure condition design (F5):** Generic output assumes perfect execution. Skill output identifies typed failure conditions with observable signals and escalation actions, plus a worst-misinterpretation test on critical acceptance criteria.

6. **Ambiguity resolution (F6):** Generic output leaves ambiguities for the executor to discover. Skill output resolves ambiguities proactively and marks any remaining unknowns with explicit TBD owners and deadlines, driving the Zero-Question Score to 0.
