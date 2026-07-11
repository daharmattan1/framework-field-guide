---
id: OP-space
taxon: operating
layer: measurement
layers_secondary: []
domain: null
title: SPACE / DevEx Metrics
slug: space
thinkers: [forsgren]
school: null
evidence:
  provenance: FACT
  efficacy: DIRECT
  coi: null
lifecycle: canonical
combines: [OP-dora]
conflicts: []
grounding_status: grounded
claim_ids: []
source_section: "master L372-377"
---

# SPACE / DevEx Metrics

- **Layer / Taxon:** operating · measurement
- **Origin** `[FACT]`: Nicole Forsgren, GitHub, Microsoft Research, 2021. [source: https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/]
- **Structure:** `Satisfaction & Well-being + Performance + Activity + Communication & Collaboration + Efficiency & Flow.`
- **SWOT:** **S** productivity is multi-dimensional, prevents toxic single-metric optimization · **W** needs qualitative surveys + telemetry (harder than DORA) · **O** essential for measuring AI-coding-assistant ROI (Flow without degrading Collaboration) · **T** survey fatigue if Satisfaction is over-polled without action.
- **Case study:** Distributing code review load across experience levels improves velocity and satisfaction. [case cut 2026-07: specific examples unverifiable]
- **Combine:** DORA (SPACE is the qualitative wrapper for DORA's system metrics). Evidence: Gemini `[DIRECT]` (peer-reviewed); ChatGPT `[INDIRECT]→[DIRECT]` (implementation evidence still evolving).
