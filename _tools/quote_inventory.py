#!/usr/bin/env python3
"""quote_inventory.py — mechanical license gate (SC3).

Scans every staged markdown/json/txt file for long quoted runs that could be
verbatim in-copyright text. Two extractors:
  1. Blockquote runs  — consecutive `> ` lines joined.
  2. Inline quoted runs — text inside straight/curly double quotes.

Any run of >= THRESHOLD consecutive words is flagged for human deep-check.
Writes a quote-inventory table to stdout (and optionally a file) so the
LICENSE_LEDGER can enumerate every long run with source + length + status.

This does NOT prove license by itself — it surfaces every candidate so a human
(or the ledger) classifies each. Exit code is 0 always; the count of flagged
runs is what Phase 4 acts on.

Usage:
  python _tools/quote_inventory.py <staging_root> [--threshold N] [--out FILE]
"""
import sys, os, re, io, argparse, json

# Force UTF-8 stdout/stderr so catalog excerpts with arrows/em-dashes don't crash on Windows cp1252.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

DEFAULT_THRESHOLD = 40  # consecutive words
TEXT_EXT = {".md", ".json", ".txt", ".jsonl"}


def word_count(s: str) -> int:
    return len(re.findall(r"\S+", s))


def iter_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        # never scan the git dir or the tools dir itself
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() in TEXT_EXT:
                yield os.path.join(dirpath, fn)


def extract_blockquote_runs(lines):
    """Yield (start_line, text) for each consecutive run of `> ` lines."""
    run, start = [], None
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith(">"):
            if start is None:
                start = i
            run.append(re.sub(r"^\s*>\s?", "", line).rstrip("\n"))
        else:
            if run:
                yield start, " ".join(run).strip()
            run, start = [], None
    if run:
        yield start, " ".join(run).strip()


# straight and curly double quotes
INLINE_RE = re.compile(r'["“]([^"“”]{1,2000})["”]')


def extract_inline_runs(text):
    for m in INLINE_RE.finditer(text):
        yield m.group(1).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    flagged = []
    for path in iter_files(args.root):
        rel = os.path.relpath(path, args.root)
        # skip the tools dir and the ledger/inventory outputs themselves
        if rel.startswith("_tools" + os.sep) or rel.endswith("QUOTE_INVENTORY.md"):
            continue
        try:
            with io.open(path, encoding="utf-8") as fh:
                text = fh.read()
        except UnicodeDecodeError:
            with io.open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        lines = text.splitlines()

        for start, run in extract_blockquote_runs(lines):
            wc = word_count(run)
            if wc >= args.threshold:
                flagged.append((rel, start, "blockquote", wc, run[:160]))
        for run in extract_inline_runs(text):
            wc = word_count(run)
            if wc >= args.threshold:
                flagged.append((rel, "-", "inline-quote", wc, run[:160]))

    # report
    out_lines = []
    out_lines.append(f"# Quote Inventory (threshold >= {args.threshold} consecutive words)\n")
    out_lines.append(f"Flagged runs: **{len(flagged)}**\n")
    if flagged:
        out_lines.append("| File | Line | Kind | Words | Excerpt |")
        out_lines.append("|------|------|------|-------|---------|")
        for rel, start, kind, wc, excerpt in sorted(flagged, key=lambda x: -x[3]):
            safe = excerpt.replace("|", "\\|").replace("\n", " ")
            out_lines.append(f"| `{rel}` | {start} | {kind} | {wc} | {safe} |")
    else:
        out_lines.append("_No quoted run >= threshold. No verbatim in-copyright passage candidates._")
    report = "\n".join(out_lines) + "\n"

    print(report)
    if args.out:
        with io.open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(report)

    # machine-readable count to stderr for scripting
    sys.stderr.write(f"FLAGGED={len(flagged)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
