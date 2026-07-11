# Gap Audit — Operating Frameworks Catalog

**Baseline:** the grounded `catalog_v0.1` covers **43 units** (38 operating + 1 thinking + 4 lesser buckets; 0 domains). This audit ranks what's ABSENT/THIN, scored for the gap-fill track.

**Scoring:** each cluster scored 1-5 on three axes → **Priority = reader-value × corpus-absence × effort-inverse** (higher = do first). Effort-inverse: 5 = cheap/dense primary sources, 1 = hard/sprawling.

| # | Gap cluster | Reader-value | Absence | Effort-inv | **Priority** | Taxon target |
|---|-------------|:---:|:---:|:---:|:---:|---|
| **B1** | **Consulting-house strategy IP** (Porter Five Forces, Value Chain, Generic Strategies; BCG Growth-Share; GE-McKinsey nine-box; MECE; issue trees/pyramid principle; Ansoff; PESTEL) | 5 | 5 | 5 | **125** | `operating/strategy/` + `thinking/` (MECE/issue-trees) |
| **B2** | **Investing / mental-models** (Munger latticework, inversion, second-order thinking, circle of competence; Buffett moats/owner-earnings; Taleb antifragility/barbell; Dalio principles; Marks second-level) | 5 | 5 | 4 | **100** | `thinking/` (the taxon exists for this) |
| **B3** | **Lean / operational-excellence lineage** (Kaizen, TQM, PDCA/PDSA, JIT, Jidoka, 5S, Value Stream Mapping, Kata, Andon, Poka-yoke, Heijunka) | 4 | 5 | 4 | **80** | `operating/execution/` |
| **B4** | **Under-developed canonical thinkers** (Drucker beyond MBO — knowledge-work/managing-oneself; Christensen Disruption/RPV; Collins Flywheel/Good-to-Great/Hedgehog/Level-5; Deming 14 Points/SoPK/PDSA) | 4 | 4 | 4 | **64** | mixed: `operating/*` + `thinking/` + `thinkers[]` facet |
| **B5** | **Missing domains** (pricing, negotiation/BATNA, M&A/integration, capital allocation, org design beyond 7-S) | 4 | 5 | 3 | **60** | `domains/` (activates the empty taxon) |
| **B6** | **Other named models** (OGSM, Lean Startup/Build-Measure-Learn, Design Thinking, Holacracy/Sociocracy, Netflix context-not-control, OODA as standalone) | 3 | 4 | 4 | **48** | mixed |

## Recommended batch order (for the gap-fill track)
1. **B1 — Consulting-house IP FIRST.** Highest priority on every axis: densest PRIMARY sources (Porter's HBR articles, BCG/McKinsey published matrices are canonical + independently documented), lowest grounding risk, and it's the most conspicuous hole for a "GTM operator's frameworks guide" (Five Forces + MECE are table stakes). This is also the plan's recommended dry-run batch.
2. **B2 — Investing/mental-models.** Highest reader-value and it's the taxon `thinking/` was built for; grounding is strong (Munger's *Poor Charlie's Almanack*, Buffett's shareholder letters, Taleb's books are all real, quotable primary corpus). Slightly more effort (it's a different register than operating frameworks) → second.
3. **B3 — Lean/op-excellence.** Fills the biggest *operating* hole (the master only has Lean/TPS as a partial + Six Sigma as cautionary); well-documented lineage.
4. **B4 — deepen the canonical thinkers.** Best done alongside a business-thinkers corpus, since it's thinker-corpus work.
5. **B5 — domains.** Activates `domains/`; do once ≥3 frameworks per domain are ready (the folder rule).
6. **B6 — the long tail.** Opportunistic.

## Notes
- Each batch runs through a seed-swappable deep-research prompt → dual-engine research → knowledge-synthesis reconcile → atomize into the grounded catalog → re-ground per the same evidence-marker method used across this catalog.
- B1 + B3 extend the operating layers; B2 populates `thinking/`; B5 activates `domains/` — matching the three-taxon design.
- Placeholder cross-ref IDs already seeded during atomization that B-batches will resolve: `TH-design-thinking` (B6), `OP-itil-waterfall` (a DORA conflict target — B6/B3 adjacent).

**Batch order is locked as ranked** (B1 Consulting-house IP first). Gap-fill is future work; this audit fixes the sequence, not a delivery date.
