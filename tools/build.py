"""Build dist/compendium.jsonl from entries/**/*.md.

Each output line is one H2 section of one entry, carrying the entry's frontmatter,
so the file can be used directly as a retrieval corpus. Also validates entries
against SCHEMA.md and reports problems. Exit code 1 if any entry is invalid.
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "entries"
DIST = ROOT / "dist"

REQUIRED_FIELDS = {
    "id", "title", "domain", "kind", "thinkers", "era", "sources",
    "concepts", "grounding", "extends", "disanalogies", "status",
}
REQUIRED_SECTIONS = [
    "Summary", "Original Position", "Key Passages", "Grounding",
    "Extension to Agents", "Counter-Positions", "Open Questions", "Cross-References",
]
EXTENSION_SUBSECTIONS = ["Transfers", "Strains", "Breaks", "New"]
GROUNDINGS = {"species", "capacity", "relation", "mixed"}
KINDS = {"position", "problem", "concept", "tradition"}
STATUSES = {"stub", "draft", "reviewed"}


def known_disanalogies() -> set[str]:
    text = (ROOT / "foundations" / "disanalogies.md").read_text(encoding="utf-8")
    return set(re.findall(r"^\*\*(D\d+)\.", text, flags=re.M))


def known_threads(domain: str) -> set[str] | None:
    """Thread slugs declared as "### `slug`" in domains/<domain>.md, or None if no file."""
    path = ROOT / "domains" / f"{domain}.md"
    if not path.exists():
        return None
    return set(re.findall(r"^### `([a-z0-9-]+)`", path.read_text(encoding="utf-8"), flags=re.M))


def parse(path: Path) -> tuple[dict, list[tuple[str, str]]]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\+\+\+\n(.*?)\n\+\+\+\n(.*)", text, flags=re.S)
    if not m:
        raise ValueError("missing +++ TOML frontmatter")
    meta = tomllib.loads(m.group(1))
    parts = re.split(r"^## (.+)$", m.group(2), flags=re.M)
    sections = [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts), 2)]
    return meta, sections


def validate(path: Path, meta: dict, sections: list[tuple[str, str]], dcodes: set[str]) -> list[str]:
    errs = []
    missing = REQUIRED_FIELDS - meta.keys()
    if missing:
        errs.append(f"missing fields: {sorted(missing)}")
    if meta.get("id") != path.stem:
        errs.append(f"id {meta.get('id')!r} != filename {path.stem!r}")
    if meta.get("domain") != path.parent.name:
        errs.append(f"domain {meta.get('domain')!r} != folder {path.parent.name!r}")
    for field, allowed in (("grounding", GROUNDINGS), ("kind", KINDS), ("status", STATUSES)):
        if field in meta and meta[field] not in allowed:
            errs.append(f"{field} {meta[field]!r} not in {sorted(allowed)}")
    unknown = set(meta.get("disanalogies", [])) - dcodes
    if unknown:
        errs.append(f"unknown disanalogies: {sorted(unknown)}")
    if "year" in meta and not isinstance(meta["year"], int):
        errs.append(f"year {meta['year']!r} is not an integer")
    if meta.get("threads"):
        threads = known_threads(meta.get("domain", ""))
        if threads is None:
            errs.append(f"threads given but domains/{meta.get('domain')}.md does not exist")
        elif set(meta["threads"]) - threads:
            errs.append(f"unknown threads: {sorted(set(meta['threads']) - threads)}")

    names = [name for name, _ in sections]
    for req in REQUIRED_SECTIONS:
        if req not in names:
            errs.append(f"missing section: {req}")
    for name, body in sections:
        if name.startswith("Extension to"):
            subs = re.findall(r"^### (.+)$", body, flags=re.M)
            if subs != EXTENSION_SUBSECTIONS:
                errs.append(f"{name!r} subsections {subs} != {EXTENSION_SUBSECTIONS}")
    return errs


def main() -> int:
    dcodes = known_disanalogies()
    DIST.mkdir(exist_ok=True)
    records, failures, ids = [], 0, {}

    for path in sorted(ENTRIES.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        try:
            meta, sections = parse(path)
        except (ValueError, tomllib.TOMLDecodeError) as e:
            print(f"FAIL {rel}: {e}")
            failures += 1
            continue
        errs = validate(path, meta, sections, dcodes)
        if meta.get("id") in ids:
            errs.append(f"duplicate id, also in {ids[meta['id']]}")
        ids[meta.get("id")] = rel
        if errs:
            failures += 1
            for e in errs:
                print(f"FAIL {rel}: {e}")
            continue
        for order, (name, body) in enumerate(sections):
            records.append({
                "chunk_id": f"{meta['id']}#{order:02d}",
                "entry_id": meta["id"],
                "section": name,
                "text": body,
                "path": rel,
                **{k: v for k, v in meta.items() if k != "id"},
            })

    known = set(ids)
    dangling = sorted({
        (r["entry_id"], rel_id) for r in records
        for rel_id in r.get("related", []) + r.get("responds_to", [])
        if rel_id not in known
    })
    out = DIST / "compendium.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"{len(ids) - failures} entries ok, {failures} failed, {len(records)} chunks -> {out.relative_to(ROOT).as_posix()}")
    if dangling:
        print(f"{len(dangling)} related ids not yet written (planned): "
              + ", ".join(sorted({d for _, d in dangling})))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
