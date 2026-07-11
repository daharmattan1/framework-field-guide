# License Ledger — Framework Field Guide

This ledger shows the repo ships **no in-copyright full text**. Every source class in the catalog
is enumerated below, and a mechanical quote sweep (`_tools/quote_inventory.py`, threshold ≥ 40
consecutive words) confirms the only long runs are our own summaries — not verbatim third-party
passages.

## Source classes in the catalog

| Class | What it is | Redistribution basis |
|-------|-----------|----------------------|
| **Our own summaries** | Every per-framework description, SWOT, fit envelope, combination/conflict note, the OVERVIEW reasoning layer, gap_audit — written by us, describing each framework in our own words. | Original work → CC BY 4.0 (content) / MIT (skill logic). |
| **Quotes-with-attribution** | Short, attributed phrasings of a framework's own definitions (e.g. a one-line gloss of a principle), always ≤ a sentence and cited. | Fair use — short, transformative, attributed, non-substitutive. |
| **Resolvable links** | 57 citation URLs to HBR, MIT Sloan, McKinsey, academic, gov, and standards-body pages (`bibliography.md`). Links only — no copied article text. | Linking is not redistribution. |
| **Public-domain / permissive** | Framework *names* and *structures* (RACI, OKRs, PDCA, etc.) are ideas/methods, not copyrightable expression. | Not copyrightable as ideas. |

## Mechanical quote sweep

`python _tools/quote_inventory.py <root> --threshold 40` flags every quoted or
blockquoted run ≥ 40 consecutive words. Result: **5 flagged runs, all our own work.**

| File | Words | What it is | In-copyright? |
|------|-------|-----------|---------------|
| `catalog/OVERVIEW.md` (intro) | 159 | The catalog's own "What this is" description block | No — our summary |
| `SKILL.md` (frontmatter) | 115 | The skill's own `description` string | No — our text |
| `catalog/OVERVIEW.md` (index note) | 82 | The catalog's own structural/index note | No — our summary |
| `SKILL.md` (micro-example) | 69 | The skill's own worked micro-example | No — our example |
| `catalog/thinking/cynefin.md` | 60 | Our own "reassignment note" for Cynefin's taxon | No — our note |

**Deep-check verdict:** none of the flagged runs reproduces a copyrighted book,
article, or document. Every long run is original catalog prose. **0 verbatim
in-copyright passages ship.**

## Evidence-marker integrity (informational)

The catalog's honest grading ships intact (this is the differentiator, and it is our own work).
Inline evidence tags on the per-framework claims: `[source:]` × 37, `[self-reported:]` × 23,
`[case cut]` × 10, `[unverified]` × 2, `[corrected]` × 1. (The OVERVIEW legend and summary mention
these markers a few more times when explaining them.) See the README legend.

## How to re-verify

```bash
python _tools/quote_inventory.py skills/frameworks-thinking --threshold 40
```

Re-run after any content change and deep-check any newly flagged run.
