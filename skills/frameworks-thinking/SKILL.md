---
name: frameworks-thinking
description: "Route a decision to the right operating framework or thinking model, name the taxon/layer, recommend 1-2 frameworks, and warn on conflicts — a router over the grounded frameworks catalog. Use when user says: 'which framework for this decision', 'frameworks thinking', 'name the layer', 'what conflicts with OKRs', 'how should I decide X', 'what framework should I use'. CAPABILITY: a lean progressive-disclosure router that loads the catalog OVERVIEW for framing and pulls per-framework reference files on demand; framework-fluent but framework-skeptical (match the tool to the decision). OUTPUT: a recommendation (taxon/layer + 1-2 framework IDs + when-it-fails + conflict warning), citing catalog files. Does NOT write content or channel business thinkers (that is a separate management-masters skill)."
domain: professional
type: skill
updated: 2026-07-10
status: active
tags:
  - skill
  - frameworks
  - operating-model
  - decision-routing
  - strategy
allowed-tools:
  - Read
  - Glob
  - Grep
references:
  - references/catalog-pointer.md
version: 1.0
---
# Frameworks Thinking

**A router, not a library.** All framework knowledge lives in the frozen catalog
(bundled at `references/catalog/`, frozen release `catalog_v0.1_grounded`).
This skill decides *which* framework fits a decision, then pulls that framework's file on demand.

## Meta-posture (say this first, always)
**Framework-fluent but framework-skeptical.** Frameworks are a toolkit, not a religion. The senior
move is to **match the framework to the decision and pick the *lightest* one that makes the decision
clear** — and to distrust any framework that adds ceremony without changing an outcome. Reciting a
menu is a junior tell; showing judgment about *when each applies* is the operator signal.

## When to use
- "Which framework should I use to decide X?" / "How should I think about X?"
- "Name the layer" for a problem (strategy / alignment / execution / measurement).
- "What conflicts with / combines with [framework]?"
- Pressure-testing whether a framework someone is invoking actually fits the decision.

**Do NOT use for:** writing content (that's the content pipeline); channeling business thinkers
("what would Munger say") — that's a separate `management-masters` skill.

---

## HOW THIS SKILL RUNS (progressive disclosure — the load rules)

1. **ALWAYS load `references/catalog/OVERVIEW.md` first** — it is the reasoning layer (4-layer model, the 11
   tensions, the combination map, the **conflict map**, the fad graveyard, the AI-era shift).
2. **Use `references/catalog/catalog.json` as the router index** — map a framework ID → path + facets.
3. **Pull a per-framework file (`references/catalog/<taxon>/<slug>.md`) ONLY on demand** — when the user needs
   that framework's structure / SWOT / case / evidence. **Never load all 43 files.** One or two.
4. For "is there a framework for X?" where X might be absent, check `references/catalog/gap_audit.md` (the known
   gaps) before saying "none exists."

Full load table + paths: `references/catalog-pointer.md`.

---

## THE ROUTE (3-question decision tree)

Ask these in order; the first YES routes.

### Q1 — Is this a specific *functional* decision? (price it, negotiate it, buy it, allocate capital)
→ **`domains/`** (IDs `DM-*`). *v0.1 note: `domains/` is empty until gap-fill — if so, say the
catalog doesn't cover it yet and point to `gap_audit.md` cluster B5.*

### Q2 — Is this about *running or structuring the org*? (goals, ownership, delivery, metrics)
→ **`operating/`** — then name the LAYER using this table, and pull the 1-2 fitting frameworks:

| Layer | The question it answers | Reach for (pull the file by ID) |
|-------|------------------------|--------------------------------|
| **strategy** | What are we doing, where do we play, what must be true? | `OP-okrs`, `OP-playing-to-win`, `OP-wardley-mapping`, `OP-gotta-believes`, `OP-working-backwards`, `OP-jtbd`, `OP-three-horizons`, `OP-blue-ocean`, `OP-mbo`, `OP-v2mom` |
| **alignment** | Who owns what; how do teams stay pointed the same way? | `OP-raci`, `OP-daci`, `OP-rapid`, `OP-commanders-intent`, `OP-single-threaded-ownership`, `OP-hoshin-kanri`, `OP-mckinsey-7s`, `OP-cascading-okrs` |
| **execution** | How does work move from priority to shipped? | `OP-agile-scrum`, `OP-kanban`, `OP-shape-up`, `OP-4dx`, `OP-theory-of-constraints`, `OP-lean-tps`, `OP-safe`, `OP-six-sigma`, `OP-eos-traction`, `OP-prioritization`, `OP-now-next-later`, `OP-rite`, `OP-spotify-model` |
| **measurement** | How do we know it worked, early enough to steer? | `OP-kpis-north-star`, `OP-dora`, `OP-space`, `OP-balanced-scorecard`, `OP-aarrr`, `OP-bowtie`, `OP-gist` |

### Q3 — Is this about *how to reason through the problem itself*?
→ **`thinking/`** (IDs `TH-*`), routed by reasoning move: *classify it* (`TH-cynefin`) · *structure it*
(MECE/issue-trees — gap B1) · *generate options* (inversion — gap B2) · *evaluate* (second-order,
margin of safety — gap B2). *v0.1 note: only `TH-cynefin` exists; the rest are gap_audit B1/B2.*

**Tie-break law** (when Q2 vs Q1 is unclear): recurring org process → `operating`; per-instance
functional decision → `domains`; content-free reasoning tool → `thinking`.

---

## THE OUTPUT CONTRACT (what a good answer contains)

Every recommendation states, in order:
1. **The layer/taxon** the decision lives in (name it — that's the operator signal).
2. **1-2 frameworks by ID**, each with a one-line *fit* and its *when-it-fails* (from the file's Use/fails).
3. **A conflict/caveat** — check the OVERVIEW conflict map + the framework file's `conflicts[]`:
   - Never stack two *full* operating systems (OKRs + EOS + Hoshin simultaneously = reporting fatigue).
   - Autonomy vs. bureaucracy (Spotify/STO ✗ SAFe); innovation vs. optimization (Six Sigma kills
     Blue Ocean/GIST discovery); goal-rigidity vs. flow (MBO/rigid-cascade ✗ Theory of Constraints).
4. **Grounding honesty** — if the framework's case/stat is `[self-reported:]` or a `[case cut]`, say so.
   Flag fad-graveyard entries (e.g. `OP-spotify-model` lifecycle:graveyard) as "principle survives,
   copy-paste doesn't."

**Lightest-tool rule:** if a heuristic (RICE, Now/Next/Later) answers the decision, recommend it over
a full operating system. Distrust ceremony that doesn't change the outcome.

---

## Worked micro-example (the shape, not a script)
> *"How do we decide what to build next quarter?"* → **Layer: strategy** (+ a measurement hook).
> Reach for `OP-okrs` (set the destination) or `OP-playing-to-win` (if the real question is
> where-to-play), with `OP-now-next-later` for the roadmap shape. **When it fails:** OKRs degrade to
> a to-do list if KRs measure activity. **Conflict:** don't also run `OP-eos-traction`/`OP-hoshin-kanri`
> cadence on top — one full system at a time. Pull `OP-okrs.md` for the depth.

## References
| File | Purpose |
|------|---------|
| `references/catalog-pointer.md` | The catalog load table + paths + ID convention + grounding markers |
| `references/catalog/OVERVIEW.md` (in the frameworks catalog) | The reasoning layer — load first |
| `references/catalog/catalog.json` | Router index (ID → path + facets) |
| `references/catalog/gap_audit.md` | What's ABSENT (route here when the catalog doesn't cover a decision yet) |
