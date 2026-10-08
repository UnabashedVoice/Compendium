"""Build dist/compendium.jsonl from entries/**/*.md.

Each output line is one H2 section of one entry, carrying the entry's frontmatter,
so the file can be used directly as a retrieval corpus. Also validates entries
against SCHEMA.md and reports problems. Exit code 1 if any entry is invalid.
"""

from __future__ import annotations

import datetime
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from compendium_access import EVALUATION_FINDINGS  # noqa: E402  (one definition, shared with the access layer)

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
STANDING_CURRENT = {"dominant", "major", "minority", "marginal", "historical"}
AGENT_FITS = {"stronger", "comparable", "weaker", "inapplicable", "open"}
STANDING_SUBSECTIONS = ["Reception", "Measured", "For Agents"]
COUNTER_TAG = re.compile(r"^- \[(answered|contested|unanswered|conceded)\] ", flags=re.M)
ENTRY_CITE = re.compile(r"\[E:([a-z0-9-]+)\]")
DRIVERS = {"argument", "evidence", "authority", "access", "fashion"}
DRIVER_TAG = re.compile(r"\[driver: ([a-z, ]+)\]")
PAGE_CITE = re.compile(r"\[P:[a-z0-9][a-z0-9.-]*:\d+[a-z]?(?:-\d+[a-z]?)?\]")  # same form as library.py CITE_P
LINE_CITE = re.compile(r"\[L:([a-z0-9][a-z0-9.-]*):(\d+)(?:-(\d+))?\]")        # same form as library.py CITE
_secondary: dict[str, bool | list[tuple[int, int]]] | None = None


def secondary_texts() -> dict[str, bool | list[tuple[int, int]]]:
    """Library texts that are secondary sources: text id -> True (the whole text) or its secondary line spans."""
    global _secondary
    if _secondary is None:
        path = ROOT / "library" / "catalog.toml"
        cat = tomllib.loads(path.read_text(encoding="utf-8")).get("text", {}) if path.exists() else {}
        _secondary = {tid: True if rec.get("secondary") else [tuple(s) for s in rec["secondary_spans"]]
                      for tid, rec in cat.items() if rec.get("secondary") or rec.get("secondary_spans")}
    return _secondary


def cites_secondary(text: str) -> bool:
    """A [P:] citation, or an [L:] citation lying wholly inside a secondary text or secondary span."""
    if PAGE_CITE.search(text):
        return True
    sec = secondary_texts()
    for tid, a, b in LINE_CITE.findall(text):
        lo, hi = int(a), int(b or a)
        spans = sec.get(tid)
        if spans is True or (spans and any(s <= lo and hi <= e for s, e in spans)):
            return True
    return False


def known_disanalogies() -> set[str]:
    text = (ROOT / "foundations" / "disanalogies.md").read_text(encoding="utf-8")
    return set(re.findall(r"^\*\*(D\d+)\.", text, flags=re.M))


def known_profiles() -> set[str]:
    """Deployment-profile slugs from the table in foundations/deployments.md (empty if no file)."""
    path = ROOT / "foundations" / "deployments.md"
    if not path.exists():
        return set()
    return set(re.findall(r"^\| P\d+ \| `([a-z0-9-]+)` \|", path.read_text(encoding="utf-8"), flags=re.M))


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


def validate(path: Path, meta: dict, sections: list[tuple[str, str]], dcodes: set[str],
             profiles: set[str]) -> list[str]:
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
    if "agent_fit" in meta:
        fit = meta["agent_fit"]
        if not isinstance(fit, dict):
            errs.append("agent_fit must be a table of deployment profile -> value")
        else:
            if set(fit) != profiles:
                errs.append(f"agent_fit profiles {sorted(fit)} != foundations/deployments.md {sorted(profiles)}")
            bad = {k: v for k, v in fit.items() if v not in AGENT_FITS}
            if bad:
                errs.append(f"agent_fit values {bad} not in {sorted(AGENT_FITS)}")
    if "standing_reviewed" in meta and not isinstance(meta["standing_reviewed"], datetime.date):
        errs.append(f"standing_reviewed {meta['standing_reviewed']!r} is not a TOML date")
    if meta.get("standing") and meta.get("status") == "reviewed" and "standing_reviewed" not in meta:
        errs.append("status is reviewed but the Standing section and state tags have no standing_reviewed date")
    for rec in meta.get("standing", []):
        if not isinstance(rec, dict) or set(rec) != {"community", "current", "as_of"}:
            errs.append(f"standing record {rec!r} needs exactly community, current, as_of")
            continue
        if rec["current"] not in STANDING_CURRENT:
            errs.append(f"standing current {rec['current']!r} not in {sorted(STANDING_CURRENT)}")
        if not isinstance(rec["as_of"], int):
            errs.append(f"standing as_of {rec['as_of']!r} is not an integer")

    names = [name for name, _ in sections]
    for req in REQUIRED_SECTIONS:
        if req not in names:
            errs.append(f"missing section: {req}")
    summary = dict(sections).get("Summary", "")
    hit = EVALUATION_FINDINGS.search(summary)
    if hit:
        errs.append(f"Summary refers to Palaestra or its scenarios ({hit.group(0)!r}); models are never shown "
                    "evaluation findings, and the brief rests on the Summary. Keep findings in Extension to Agents")
    for name, body in sections:
        if name.startswith("Extension to"):
            subs = re.findall(r"^### (.+)$", body, flags=re.M)
            if subs != EXTENSION_SUBSECTIONS:
                errs.append(f"{name!r} subsections {subs} != {EXTENSION_SUBSECTIONS}")

    has_standing = bool(meta.get("standing"))
    if has_standing != ("Standing" in names):
        errs.append("standing frontmatter and ## Standing section must appear together")
    if REQUIRE_STANDING and not has_standing:
        errs.append("missing standing: every entry needs a standing record and a ## Standing section "
                    "(SCHEMA.md, \"Standing\"); --allow-missing-standing skips this check for a draft build")
    if has_standing and "Standing" in names:
        body = dict(sections)["Standing"]
        subs = re.findall(r"^### (.+)$", body, flags=re.M)
        if subs != STANDING_SUBSECTIONS:
            errs.append(f"'Standing' subsections {subs} != {STANDING_SUBSECTIONS}")
        if names.index("Standing") != names.index("Counter-Positions") + 1:
            errs.append("## Standing must follow ## Counter-Positions")
        counters = dict(sections).get("Counter-Positions", "")
        bullets = re.findall(r"^- ", counters, flags=re.M)
        if len(COUNTER_TAG.findall(counters)) != len(bullets):
            errs.append("every Counter-Positions bullet needs a state tag when ## Standing is present")
        reception = next((r for r in re.split(r"^### ", body, flags=re.M) if r.startswith("Reception")), "")
        for bullet in re.findall(r"^- (.+)$", reception, flags=re.M):
            tags = DRIVER_TAG.findall(bullet)
            drivers = {d.strip() for t in tags for d in t.split(",")}
            if not tags:
                errs.append(f"Reception bullet has no [driver: ...] tag: {bullet[:60]!r}")
            elif drivers - DRIVERS:
                errs.append(f"unknown drivers {sorted(drivers - DRIVERS)} (allowed: {sorted(DRIVERS)})")
            if "fashion" in drivers and not cites_secondary(bullet):
                errs.append(f"[driver: fashion] needs a secondary source in the same bullet ([P:], or [L:] "
                            f"inside a text or span the catalog marks secondary): {bullet[:60]!r}")
    return errs


# Standing is required of every entry (all 35 met it on 2026-10-01). --allow-missing-standing relaxes
# this for a work-in-progress build; --require-standing is still accepted and is now the default.
REQUIRE_STANDING = "--allow-missing-standing" not in sys.argv


def main() -> int:
    dcodes = known_disanalogies()
    profiles = known_profiles()
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
        errs = validate(path, meta, sections, dcodes, profiles)
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
    # graph check: responders to an entry with ## Standing should appear in its ledger via [E:]
    responders: dict[str, set[str]] = {}
    for r in records:
        if r["section"] == "Summary":
            for target in r.get("responds_to", []):
                responders.setdefault(target, set()).add(r["entry_id"])
    cited: dict[str, set[str]] = {}
    for r in records:
        if r["section"] in ("Counter-Positions", "Standing"):
            cited.setdefault(r["entry_id"], set()).update(ENTRY_CITE.findall(r["text"]))
    unlinked = sorted(
        (target, src) for r in records if r["section"] == "Standing"
        for target in [r["entry_id"]] for src in responders.get(target, set()) - cited.get(target, set())
    )
    bad_e = sorted({(r["entry_id"], e) for r in records for e in ENTRY_CITE.findall(r["text"]) if e not in known})

    out = DIST / "compendium.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False, default=str) + "\n")  # default=str: TOML dates

    print(f"{len(ids) - failures} entries ok, {failures} failed, {len(records)} chunks -> {out.relative_to(ROOT).as_posix()}")
    if dangling:
        print(f"{len(dangling)} related ids not yet written (planned): "
              + ", ".join(sorted({d for _, d in dangling})))
    for target, src in unlinked:
        print(f"WARN {target}: {src} responds to it but is not cited with [E:{src}] in Counter-Positions or Standing")
    for eid, e in bad_e:
        print(f"FAIL {eid}: [E:{e}] names no existing entry")
    return 1 if failures or bad_e else 0


if __name__ == "__main__":
    sys.exit(main())
