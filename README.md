# Framework Field Guide

A grounded, agent-callable catalog of **~43 corporate operating frameworks** — RACI, OKRs,
Theory of Constraints, DORA, Wardley Mapping, JTBD, Kanban, and the rest — plus a Claude Code
skill that routes a decision to the *right* framework and warns you when two of them conflict.

It is a **router, not a lecture.** The catalog holds the knowledge (origin, structure, SWOT,
a real company case, and how each framework combines or conflicts with the others). The
`frameworks-thinking` skill decides *which* framework fits the decision in front of you, names
the layer it lives in, and pulls just that framework's file on demand.

The differentiator is **grounding honesty**: every factual claim is labeled with where the
evidence actually comes from. Owner-reported numbers say so. Claims that couldn't be grounded
independently were cut or flagged — not dressed up.

## What's inside

```
skills/frameworks-thinking/
├── SKILL.md                    # the router (progressive-disclosure logic)
└── references/
    ├── catalog-pointer.md      # the catalog load table + ID convention
    └── catalog/                # the grounded catalog (the knowledge)
        ├── OVERVIEW.md         # the reasoning layer — 4-layer model, tensions, combine/conflict maps, fad graveyard
        ├── catalog.json        # machine index: framework ID → path + facets
        ├── bibliography.md     # 57 resolvable citation URLs, tiered by authority
        ├── gap_audit.md        # what's deliberately NOT in v0.1 yet (route here for "is there a framework for X?")
        ├── operating/          # "how do we RUN the org" — strategy / alignment / execution / measurement (42 files)
        ├── thinking/           # "how do we REASON" — mental models (Cynefin)
        └── domains/            # "how do we decide THIS class" — pricing, negotiation, M&A (reserved taxon)
```

The catalog covers the operating layer in depth (42 frameworks across strategy, alignment,
execution, and measurement). The `thinking/` and `domains/` taxa are part of the taxonomy and
carry what's grounded today; `gap_audit.md` is the honest map of which clusters are thin, so you
always know what the catalog does and doesn't cover.

## Install (as a Claude Code skill)

The catalog is bundled **inside** the skill folder, so installing is one copy:

1. Copy the `skills/frameworks-thinking/` directory into your project's `.claude/skills/`
   directory (so you end up with `.claude/skills/frameworks-thinking/SKILL.md`).
2. That's it. The skill's `references/` — including the whole `catalog/` — travels with it, and
   every path inside the skill is relative to the skill root, so nothing points outside the folder.

Claude Code discovers skills in `.claude/skills/`, so the agent can now invoke `frameworks-thinking`
for decisions like *"which framework should I use to decide what to build next quarter?"* or
*"two teams keep stepping on each other — how do we fix ownership?"* (Depending on your Claude Code
version, it's available as the `/frameworks-thinking` skill and/or auto-selected by the agent when a
routing question comes up.)

You can also just **read the catalog directly** — `skills/frameworks-thinking/references/catalog/OVERVIEW.md`
is a standalone reference guide with no tooling required.

## How to read the evidence

There are **two** grading systems, and they mean different things.

**1. Inline evidence markers** — attached to individual claims inside each framework file:

| Marker | Means |
|--------|-------|
| `[source: URL]` | Independently verifiable, with a resolvable citation. |
| `[self-reported: URL]` | The number or case comes from the framework's own owner/vendor. Use it, but say "self-reported." |
| `[case cut]` | A claim that couldn't be independently grounded was removed. |
| `[corrected]` | A source-level factual error was found and fixed. |
| `[unverified]` | Flagged as not independently confirmed. |

Re-grounding outcome: of the 83 publish-critical claims audited, **33 grounded independently, 32
were labeled self-reported, and 18 were cut, corrected, or downgraded.** (That's the audit tally.
Separately, the shipped files carry the surviving inline markers: `[source:]` and `[self-reported:]`
on individual lines, plus `[case cut]` / `[corrected]` / `[unverified]` where re-grounding changed a
claim — a different count, because one audited claim can map to more or fewer inline marks.)

**2. `catalog.json` evidence facets** — structured metadata on each framework as a whole (not the same as the inline markers):

| Facet | Values |
|-------|--------|
| `evidence.provenance` | `FACT` (origin established) / `SIGNAL` (plausible, single-source) |
| `evidence.efficacy` | `DIRECT` / `INDIRECT` / `ABSENT` (how strong the proof it *works* is) |
| `evidence.coi` | `FRAMEWORK OWNER` / `AUTHOR EQUITY` / `PRACTITIONER ORG` / `VENDOR` / `null` |
| `lifecycle` | `canonical` / `contested` / `graveyard` (e.g. copy-paste Spotify-model is `graveyard`) |

## License

- **Code** (the skill and any scripts) — MIT.
- **Content** (the framework catalog) — Creative Commons Attribution 4.0 (CC BY 4.0).

Third-party framework names and the ideas of their originators remain the property of their
respective owners; this catalog describes and cites them and reproduces no copyrighted work in
full. See [`LICENSE`](LICENSE) and [`LICENSE_LEDGER.md`](LICENSE_LEDGER.md).

---

Built by Victor Sowers ([STEEPWORKS](https://steepworks.io)). Catalog and skill released under the licenses in LICENSE.
