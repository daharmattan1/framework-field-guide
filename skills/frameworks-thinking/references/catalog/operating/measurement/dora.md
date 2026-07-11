---
id: OP-dora
taxon: operating
layer: measurement
layers_secondary: []
domain: null
title: DORA Metrics
slug: dora
thinkers: [forsgren, humble, kim]
school: null
evidence:
  provenance: FACT
  efficacy: DIRECT
  coi: null
lifecycle: canonical
combines: [OP-space, OP-theory-of-constraints, OP-kanban]
conflicts: [OP-itil-waterfall]
grounding_status: grounded
claim_ids: []
source_section: "master L365-370"
---

# DORA Metrics

- **Layer / Taxon:** operating · measurement
- **Origin** `[FACT]`: Nicole Forsgren, Jez Humble, Gene Kim (DevOps Research and Assessment); *Accelerate* + State of DevOps; 2014. [source: https://itrevolution.com/product/accelerate/]
- **Structure:** *Velocity:* Deployment Frequency + Lead Time for Changes · *Stability:* Change Failure Rate + Mean Time to Restore.
- **SWOT:** **S** unifies Dev speed + Ops stability, correlates with profitability · **W** tracks systems, misses human context (burnout) · **O** drives automation/CI-CD/trunk-based dev · **T** weaponizing to rate individual developers → gaming (empty commits).
- **Case study:** **HP LaserJet Firmware** (Gary Gruver) — automated testing shifted the team **5% → 40% of time on new features.** [source: https://itrevolution.com/articles/the-amazing-devops-transformation-of-the-hp-laserjet-firmware-team-gary-gruver/]
- **Combine:** SPACE (human context), Theory of Constraints, Kanban. **Conflict:** legacy ITIL/Waterfall change-approval boards. Evidence `[DIRECT]` — multi-year statistical research. **The measurement-layer cautionary case** for misuse.
