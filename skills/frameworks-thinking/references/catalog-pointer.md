# Catalog Pointer — the source of truth this skill routes over

> `frameworks-thinking` is a ROUTER, not a copy. All framework knowledge lives in the bundled
> **catalog_v0.1_grounded** (at `references/catalog/`). Never fork or inline it.

## Catalog root
`references/catalog/` (bundled inside this skill; paths below are relative to the skill root)

## Load order (progressive disclosure — NEVER load all at once)
| Load | File | When |
|------|------|------|
| 1 (framing) | `references/catalog/OVERVIEW.md` | ALWAYS load first for a "how should I think about this" question — it holds the 4-layer model, the 11 tensions, the combination map, the **conflict map**, the fad graveyard, the AI-era shift. This is the reasoning layer. |
| 2 (routing index) | `references/catalog/catalog.json` | To map a framework ID → its file path + facets (taxon, layer, evidence, lifecycle, combines[], conflicts[]). The router index. |
| 3 (detail, on demand) | `references/catalog/<taxon>/<slug>.md` | ONLY when the user needs a specific framework's depth (structure, SWOT, case, evidence). Pull by ID from catalog.json. One or two files, never all 43. |
| aux | `references/catalog/gap_audit.md` | To answer "is there a framework for X?" when X may be an ABSENT cluster (consulting-house IP, mental-models, lean/ops-ex, domains) — tells you what's NOT yet in the catalog. |

## The three taxa (routing targets)
- `references/catalog/operating/{strategy,alignment,execution,measurement}/` — "how do we RUN the org" (the 4-layer model). IDs `OP-*`.
- `references/catalog/thinking/` — "how do we REASON" (mental models, reasoning moves). IDs `TH-*`. (v0.1: Cynefin only; grows via gap-fill.)
- `references/catalog/domains/` — "how do we decide THIS class" (pricing, negotiation, M&A…). IDs `DM-*`. (v0.1: empty; activated by gap-fill.)

## ID convention
`{TAXON}-{slug}` (e.g. `OP-okrs`, `OP-theory-of-constraints`, `TH-cynefin`). **Layer is a FACET, not in the ID** — read it from catalog.json / the file's frontmatter.

## Grounding caveat (surface honestly)
Every framework file carries grounding markers: `[source:]` = independent, `[self-reported:]` = owner-sourced (say "self-reported" when you cite it), `[case cut]`/`[corrected]`/`[unverified]` = re-grounding outcomes. When recommending a framework whose case/stat is owner-labeled or cut, say so. The markers are inline in each framework file, and `references/catalog/catalog.json` carries the per-framework evidence facets.
