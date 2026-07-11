#!/usr/bin/env python3
"""link_check.py — resolve EVERY internal reference inside the staged repo (SC/Phase 5).

Checks three reference kinds against the staged file set:
  1. Markdown links   [text](path)          — local (non-http) targets only.
  2. Wikilinks        [[name]]               — resolved against file basenames.
  3. catalog.json     every value that looks like a catalog-relative path.

A reference is UNRESOLVED if its target file does not exist in the staging tree.
External (http/https/mailto) links and pure in-page anchors (#frag) are ignored.

Exit 0 iff there are zero unresolved internal references; else exit 1 and print
each offender as `FILE:LINE  ->  TARGET  (kind)`.

Usage:
  python _tools/link_check.py <staging_root>
"""
import sys, os, re, io, json

MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
TEXT_EXT = {".md"}


def is_external(target: str) -> bool:
    t = target.strip()
    return (
        t.startswith("http://") or t.startswith("https://") or
        t.startswith("mailto:") or t.startswith("#") or t.startswith("tel:")
    )


def build_index(root):
    """Map basename (with and without extension) -> set of relpaths; plus a set of all relpaths."""
    all_paths = set()
    by_base = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root).replace("\\", "/")
            all_paths.add(rel)
            base_noext = os.path.splitext(fn)[0]
            by_base.setdefault(fn, set()).add(rel)
            by_base.setdefault(base_noext, set()).add(rel)
    return all_paths, by_base


def target_exists(target, src_rel, root, all_paths, by_base):
    """Resolve a markdown link target relative to the source file, then to root."""
    t = target.split("#")[0].strip()  # drop anchor
    if not t:
        return True  # pure anchor
    t = t.lstrip("./")
    # try relative to the source file's dir
    src_dir = os.path.dirname(src_rel)
    cand_rel = os.path.normpath(os.path.join(src_dir, t)).replace("\\", "/")
    if cand_rel in all_paths:
        return True
    # try relative to root
    cand_root = os.path.normpath(t).replace("\\", "/")
    if cand_root in all_paths:
        return True
    # try as a directory (index) — accept if the dir exists on disk
    if os.path.isdir(os.path.join(root, cand_rel)) or os.path.isdir(os.path.join(root, cand_root)):
        return True
    # try basename match
    base = os.path.basename(t)
    if base in by_base:
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print("usage: link_check.py <staging_root>", file=sys.stderr)
        return 2
    root = sys.argv[1]
    all_paths, by_base = build_index(root)
    offenders = []

    for rel in sorted(all_paths):
        if os.path.splitext(rel)[1].lower() not in TEXT_EXT:
            continue
        if rel.startswith("_tools/"):
            continue
        full = os.path.join(root, rel)
        try:
            with io.open(full, encoding="utf-8") as fh:
                lines = fh.readlines()
        except UnicodeDecodeError:
            with io.open(full, encoding="utf-8", errors="replace") as fh:
                lines = fh.readlines()
        for lineno, line in enumerate(lines, 1):
            for m in MD_LINK_RE.finditer(line):
                target = m.group(1)
                if is_external(target):
                    continue
                if not target_exists(target, rel, root, all_paths, by_base):
                    offenders.append((rel, lineno, target, "md-link"))
            for m in WIKILINK_RE.finditer(line):
                name = m.group(1).split("|")[0].strip()
                if name not in by_base and (name + ".md") not in by_base:
                    offenders.append((rel, lineno, name, "wikilink"))

    # catalog.json path values
    catjson = os.path.join(root, "skills/frameworks-thinking/references/catalog/catalog.json")
    if os.path.exists(catjson):
        with io.open(catjson, encoding="utf-8") as fh:
            try:
                data = json.load(fh)
            except Exception as e:
                offenders.append(("catalog.json", 0, f"PARSE ERROR: {e}", "json"))
                data = None
        if data is not None:
            cat_root = os.path.dirname(os.path.relpath(catjson, root)).replace("\\", "/")

            def walk(obj):
                if isinstance(obj, dict):
                    for v in obj.values():
                        yield from walk(v)
                elif isinstance(obj, list):
                    for v in obj:
                        yield from walk(v)
                elif isinstance(obj, str):
                    yield obj

            for val in walk(data):
                # a catalog path looks like operating/... or thinking/... or domains/... ending in .md
                if re.match(r"^(operating|thinking|domains)/[\w\-/]+\.md$", val):
                    cand = os.path.normpath(os.path.join(cat_root, val)).replace("\\", "/")
                    if cand not in all_paths:
                        offenders.append(("catalog.json", 0, val, "catalog-path"))

    if offenders:
        print(f"UNRESOLVED internal references: {len(offenders)}")
        for rel, lineno, target, kind in offenders:
            print(f"  {rel}:{lineno}  ->  {target}  ({kind})")
        return 1
    print("link_check: 0 unresolved internal references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
