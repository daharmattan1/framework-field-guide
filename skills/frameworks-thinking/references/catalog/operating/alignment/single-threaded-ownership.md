---
id: OP-single-threaded-ownership
taxon: operating
layer: alignment
layers_secondary: [execution]
domain: null
title: Single-Threaded Ownership / DRI
slug: single-threaded-ownership
thinkers: []
school: null
evidence:
  provenance: FACT
  efficacy: DIRECT
  coi: null
lifecycle: canonical
combines: [OP-working-backwards, OP-commanders-intent]
conflicts: [OP-safe]
grounding_status: grounded
claim_ids: []
source_section: "master L203-209"
---

# Single-Threaded Ownership / DRI

- **Layer / Taxon:** operating · alignment
- **Layer:** ⚠️ Gemini dual-tags Alignment + Execution.
- **Origin** `[SIGNAL]`: Amazon early 2000s — unverified 2004 date. Apple "Directly Responsible Individual" is the analogue.
- **Structure:** `Single-Threaded Leader (owns P&L + delivery) → Two-Pizza Team (<10, cross-functional, autonomous, API-communicating).`
- **SWOT:** **S** eradicates coordination drag + dependency bottlenecks · **W** resource-intensive; multidisciplinary STLs are rare · **O** microservices matching autonomous teams (Conway's Law) · **T** siloed/duplicated effort without governance.
- **Case study:** API-separable autonomous teams enable independent scale and throughput. **Caveat — Prime Video reduced costs 90% by moving FROM microservices TO monoliths**, challenging the pure STO microservice thesis. [corrected 2026-07: Prime Video achieved cost reduction via monolith consolidation, not microservice separation]
- **Combine:** `OP-working-backwards` (PR-FAQ), microservices, `OP-commanders-intent`. **Conflict:** matrix management, `OP-safe` (SAFe).
- **Evidence:** Gemini `[DIRECT]`, ChatGPT `[INDIRECT]`.
