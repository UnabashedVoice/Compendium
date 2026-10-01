"""The Compendium's source library: catalog checks, full-text index, search, and quote verification.

    python tools/library.py check              catalog/sources <-> files, sha256 pins (--pin to record hashes)
    python tools/library.py index              rebuild library/index.sqlite (SQLite FTS5)
    python tools/library.py search QUERY       full-text search (FTS5 syntax: "exact phrase", a AND b, prefix*)
          [--text ID] [-n N]
    python tools/library.py show ID:LINE       print lines around a location  [-C N]
    python tools/library.py verify [ENTRY...]  check every [L:id:line]/[P:key:page] citation and its quotes
    python tools/library.py lint [ENTRY...]    report unsourced material: '(paraphrase)' marks and
                                               Original Position paragraphs with no citation

Two citation forms. [L:<text-id>:<line>] or [L:<text-id>:<start>-<end>] cites a full public-domain text
stored (and line-numbered) in library/texts/; a quotation "..." (straight or curly quotes, 4+ words) in the
same bullet or paragraph as the citation is checked against the cited lines (with a small window, since OCR
line breaks drift). Ellipses split a quotation into segments that must each be found, in order. Matching
ignores case, punctuation, diacritics and line-break hyphenation; OCR texts fall back to fuzzy matching.

[P:<key>:<page>] or [P:<key>:<start>-<end>] cites an in-copyright source registered in library/sources.toml,
by page, or for unpaginated sources (encyclopedia articles) by section: 4, or subsection label: 5c. Registered in
library/sources.toml (README, "Works in copyright": short quotations only, never stored in this repository).
verify checks that <key> is registered and reports the citation; it cannot check a P-cited quotation's exact
wording, since no full text is held to check it against, so accuracy there rests on the page citation being
checked by hand against the named edition. lint treats a [P:...] citation exactly like an [L:...] one for
the purposes of "does this paragraph/quotation have a citation".

Stdlib only (Python 3.11+).
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import sqlite3
import sys
import tomllib
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "library"
TEXTS = LIB / "texts"
CATALOG = LIB / "catalog.toml"
SOURCES = LIB / "sources.toml"
INDEX = LIB / "index.sqlite"
ENTRIES = ROOT / "entries"

CITE = re.compile(r"\[L:([a-z0-9][a-z0-9.-]*):(\d+)(?:-(\d+))?\]")
# locator: a page (27), a section (4) or a subsection label (5c) for sources without pages; ranges 27-29, 5c-5d
CITE_P = re.compile(r"\[P:([a-z0-9][a-z0-9.-]*):(\d+[a-z]?)(?:-(\d+[a-z]?))?\]")
CITE_E = re.compile(r"\[E:([a-z0-9-]+)\]")  # another entry in the corpus; Standing / Counter-Positions only
QUOTE = re.compile(r"[\"“]([^\"“”]*)[\"”]")  # pair every quote; length filter applied by callers
WINDOW_BEFORE, WINDOW_AFTER = 40, 120
FUZZY_OK = 0.90


# ---------- normalization ----------

def norm(s: str) -> str:
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)        # join line-break hyphenation
    s = s.replace("¬", "")
    s = re.sub(r"\[\d{1,3}\]", "", s)                    # footnote reference markers, e.g. [11]
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"([㐀-鿿豈-﫿])", r" \1 ", s)   # CJK: each character counts as a word
    s = re.sub(r"[^a-z0-9㐀-鿿豈-﫿]+", " ", s.lower())
    return s.strip()


def read_lines(text_id: str) -> list[str]:
    return (TEXTS / f"{text_id}.txt").read_text(encoding="utf-8", errors="replace").splitlines()


def load_catalog() -> dict[str, dict]:
    return tomllib.loads(CATALOG.read_text(encoding="utf-8")).get("text", {}) if CATALOG.exists() else {}


def load_sources() -> dict[str, dict]:
    return tomllib.loads(SOURCES.read_text(encoding="utf-8")).get("source", {}) if SOURCES.exists() else {}


# ---------- check ----------

def cmd_check(args) -> int:
    cat = load_catalog()
    files = {p.stem: p for p in TEXTS.glob("*.txt")}
    bad = 0
    for tid in sorted(set(files) - set(cat)):
        print(f"UNCATALOGED {tid}"); bad += 1
    for tid in sorted(set(cat) - set(files)):
        print(f"MISSING FILE {tid}"); bad += 1
    pins = {}
    for tid in sorted(set(files) & set(cat)):
        h = hashlib.sha256(files[tid].read_bytes()).hexdigest()
        pins[tid] = h
        want = cat[tid].get("sha256")
        if want and want != h:
            print(f"CHANGED {tid}: sha256 differs from catalog pin"); bad += 1
        for field in ("author", "title", "edition", "source", "rights"):
            if not cat[tid].get(field):
                print(f"INCOMPLETE {tid}: no {field}"); bad += 1
        # secondary = true (whole text) or secondary_spans = [[start, end], ...] (editorial notes in a primary text)
        spans = cat[tid].get("secondary_spans", [])
        if "secondary" in cat[tid] and not isinstance(cat[tid]["secondary"], bool):
            print(f"BAD {tid}: secondary must be true or false"); bad += 1
        n = sum(1 for _ in files[tid].open(encoding="utf-8")) if spans else 0
        for sp in spans:
            if not (isinstance(sp, list) and len(sp) == 2 and all(isinstance(x, int) for x in sp) and 1 <= sp[0] <= sp[1] <= n):
                print(f"BAD {tid}: secondary span {sp!r} is not [start, end] within 1-{n}"); bad += 1
    if args.pin:
        text = CATALOG.read_text(encoding="utf-8")
        for tid, h in pins.items():
            block = re.search(rf'(\[text\."{re.escape(tid)}"\]\n(?:(?!\[text\.).*\n?)*)', text)
            if block and "sha256" not in block.group(1):
                text = text.replace(block.group(1), block.group(1).rstrip("\n") + f'\nsha256 = "{h}"\n\n', 1)
        CATALOG.write_text(text, encoding="utf-8")
        print(f"pinned {len(pins)} hashes")
    srcs = load_sources()
    for key, rec in sorted(srcs.items()):
        for field in ("author", "title", "edition", "year", "url", "rights"):
            if not rec.get(field):
                print(f"INCOMPLETE source {key}: no {field}"); bad += 1
    print(f"{len(files)} files, {len(cat)} catalog entries, {len(srcs)} in-copyright sources, {bad} problems")
    return 1 if bad else 0


# ---------- index / search / show ----------

def passages(lines: list[str], max_chars: int = 1500):
    """Yield (start_line, end_line, text) chunks: paragraphs, split further when very long. 1-based lines."""
    buf, start = [], None
    size = 0
    for i, line in enumerate(lines, 1):
        if line.strip():
            if start is None:
                start = i
            buf.append(line); size += len(line)
            if size >= max_chars:
                yield start, i, "\n".join(buf); buf, start, size = [], None, 0
        elif buf:
            yield start, i - 1, "\n".join(buf); buf, start, size = [], None, 0
    if buf:
        yield start, len(lines), "\n".join(buf)


def cmd_index(args) -> int:
    cat = load_catalog()
    if INDEX.exists():
        INDEX.unlink()
    db = sqlite3.connect(INDEX)
    db.execute("CREATE TABLE texts (id TEXT PRIMARY KEY, author TEXT, title TEXT, edition TEXT, lines INTEGER)")
    db.execute("CREATE VIRTUAL TABLE passages USING fts5(text_id UNINDEXED, line_start UNINDEXED, "
               "line_end UNINDEXED, body, tokenize='unicode61 remove_diacritics 2')")
    total = 0
    for p in sorted(TEXTS.glob("*.txt")):
        lines = read_lines(p.stem)
        meta = cat.get(p.stem, {})
        db.execute("INSERT INTO texts VALUES (?,?,?,?,?)",
                   (p.stem, meta.get("author", ""), meta.get("title", ""), meta.get("edition", ""), len(lines)))
        rows = [(p.stem, a, b, re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", t)) for a, b, t in passages(lines)]
        db.executemany("INSERT INTO passages VALUES (?,?,?,?)", rows)
        total += len(rows)
    db.commit()
    print(f"indexed {total} passages from {len(list(TEXTS.glob('*.txt')))} texts -> {INDEX.relative_to(ROOT).as_posix()}")
    return 0


def cmd_search(args) -> int:
    if not INDEX.exists():
        print("no index; run: python tools/library.py index"); return 1
    db = sqlite3.connect(INDEX)
    sql = ("SELECT text_id, line_start, line_end, snippet(passages, 3, '>>', '<<', ' ... ', 24) "
           "FROM passages WHERE passages MATCH ?")
    params: list = [args.query]
    if args.text:
        sql += " AND text_id = ?"; params.append(args.text)
    sql += " ORDER BY rank LIMIT ?"; params.append(args.n)
    try:
        rows = db.execute(sql, params).fetchall()
    except sqlite3.OperationalError as e:
        print(f"query error: {e} (quote phrases, e.g. '\"bundle or collection\"')"); return 1
    for tid, a, b, snip in rows:
        print(f"[L:{tid}:{a}-{b}]\n    {' '.join(snip.split())}")
    print(f"{len(rows)} results")
    return 0


def cmd_show(args) -> int:
    tid, _, line = args.loc.rpartition(":")
    lines = read_lines(tid)
    n = int(line)
    for i in range(max(1, n - args.C), min(len(lines), n + args.C) + 1):
        print(f"{'>' if i == n else ' '}{i:6d}  {lines[i - 1]}")
    return 0


# ---------- verify / lint ----------

def entry_paths(names: list[str]) -> list[Path]:
    if not names:
        return sorted(ENTRIES.rglob("*.md"))
    out = []
    for n in names:
        p = Path(n)
        out += [p] if p.exists() else list(ENTRIES.rglob(f"{n}.md"))
    return out


def blocks(body: str) -> list[str]:
    """Bullets and paragraphs: the units within which a quote is tied to its citation."""
    out, cur = [], []
    for line in body.splitlines():
        if re.match(r"\s*([-*]|\d+\.)\s", line) or not line.strip() or line.startswith("#"):
            if cur:
                out.append("\n".join(cur)); cur = []
            if line.strip() and not line.startswith("#"):
                cur = [line]
        else:
            cur.append(line)
    if cur:
        out.append("\n".join(cur))
    return out


def find_chunked(seg: str, hay: str, size: int = 8) -> float:
    """OCR page layouts interleave running heads and footnotes mid-sentence. Accept a segment whose
    consecutive word-chunks each occur, in order, within a short span of the haystack."""
    words = seg.split()
    pos, k, started = 0, 0, False
    while k < len(words):
        # longest run of the remaining words (at least 3, or all that remain) found after pos
        best = None
        for j in range(len(words), k + min(3, len(words) - k) - 1, -1):
            i = hay.find(" ".join(words[k:j]), pos)
            # short gaps (running heads) for any run; long gaps (footnotes) only for runs of 5+ words
            if i >= 0 and (not started or i - pos <= 600 or (i - pos <= 3000 and j - k >= 5)):
                best = (i, j)
                break
        if best is None:
            return k / len(words)
        i, j = best
        pos, k, started = i + len(" ".join(words[k:j])), j, True
    return 1.0


def find_segment(seg: str, hay: str, ocr: bool) -> float:
    if seg in hay:
        return 1.0
    if not ocr:
        return 0.0
    if len(seg.split()) > 6 and find_chunked(seg, hay) == 1.0:
        return 0.99
    # fuzzy: slide a window of the segment's length over the haystack at word boundaries
    words, n = hay.split(), len(seg.split())
    best = 0.0
    for i in range(0, max(1, len(words) - n + 1)):
        cand = " ".join(words[i:i + n])
        if cand[:1] != seg[:1] and best > 0.5:
            continue
        r = difflib.SequenceMatcher(None, seg, cand).ratio()
        if r > best:
            best = r
            if best >= 0.98:
                break
    return best


def cmd_verify(args) -> int:
    cat = load_catalog()
    srcs = load_sources()
    cache: dict[str, list[str]] = {}
    ok = fuzzy = fail = cites = p_cites = trusted = e_cites = 0
    entry_ids = {p.stem for p in ENTRIES.rglob("*.md")}
    for path in entry_paths(args.entries):
        text = path.read_text(encoding="utf-8")
        for eid in CITE_E.findall(text.split("+++", 2)[-1]):
            e_cites += 1
            if eid not in entry_ids:
                print(f"FAIL {path.stem}: [E:{eid}] names no existing entry"); fail += 1
        for blk in blocks(text.split("+++", 2)[-1]):
            found = CITE.findall(blk)
            found_p = CITE_P.findall(blk)
            if not found and not found_p:
                continue
            for tid, a, b in found:
                cites += 1
                if not (TEXTS / f"{tid}.txt").exists():
                    print(f"FAIL {path.stem}: unknown text {tid}"); fail += 1; continue
                lines = cache.setdefault(tid, read_lines(tid))
                lo, hi = int(a), int(b or a)
                if not (1 <= lo <= hi <= len(lines)):
                    print(f"FAIL {path.stem}: [L:{tid}:{a}{'-' + b if b else ''}] out of range (1-{len(lines)})"); fail += 1
            for key, a, b in found_p:
                cites += 1; p_cites += 1
                if key not in srcs:
                    print(f"FAIL {path.stem}: unregistered source {key} (add it to library/sources.toml)"); fail += 1
            quotes = [q for q in QUOTE.findall(blk) if len(norm(q).split()) >= 4]  # shorter spans are mentions
            if not quotes:
                continue
            if not found:
                # P-only block: no stored full text to check wording against; trust the page citation,
                # which README's option (a) says is checked by hand against the named edition.
                trusted += len(quotes)
                continue
            hay = norm("\n".join(
                "\n".join(cache.setdefault(t, read_lines(t))[max(0, int(a) - 1 - WINDOW_BEFORE): int(b or a) + WINDOW_AFTER])
                for t, a, b in found if (TEXTS / f"{t}.txt").exists()))
            is_ocr = any(cat.get(t, {}).get("format") == "ocr" for t, _, _ in found)
            for q in quotes:
                segs = [norm(s) for s in re.split(r"\.\s?\.\s?\.|…", q) if len(norm(s)) >= 8]
                scores = [find_segment(s, hay, is_ocr) for s in segs]
                worst = min(scores) if scores else 1.0
                if worst < 1.0 and "[" in q:
                    # bracketed text is editorial: an insertion in the source ([conceives]) or a
                    # correction of it (o[f]); accept a match either with or without it
                    bare = [norm(s) for s in re.split(r"\.\s?\.\s?\.|…", re.sub(r"\[[^\]]*\]", "", q)) if len(norm(s)) >= 8]
                    alt = [find_segment(s, hay, is_ocr) for s in bare]
                    worst = max(worst, min(alt) if alt else 1.0)
                label = q if len(q) < 70 else q[:67] + "..."
                if worst == 1.0:
                    ok += 1
                    if args.verbose:
                        print(f"ok   {path.stem}: \"{label}\"")
                elif worst >= FUZZY_OK:
                    fuzzy += 1
                    print(f"~ok  {path.stem}: \"{label}\" (OCR match {worst:.2f})")
                else:
                    fail += 1
                    print(f"FAIL {path.stem}: \"{label}\" not found near {', '.join(f'{t}:{a}' for t, a, _ in found)} (best {worst:.2f})")
    print(f"{cites} citations ({p_cites} page-cited, in-copyright), {e_cites} entry cross-citations; "
          f"quotes: {ok} exact, {fuzzy} OCR-fuzzy, {fail} failed, {trusted} in-copyright (not checked by tool)")
    return 1 if fail else 0


def cmd_lint(args) -> int:
    total_para = total_unsourced = total_stray = total_standing = 0
    for path in entry_paths(args.entries):
        text = path.read_text(encoding="utf-8").split("+++", 2)[-1]
        paraphrase = len(re.findall(r"\bparaphrase[ds]?\b", text, flags=re.I))
        paraphrase += text.count("TODO(source)")  # same to-do status as a paraphrase mark
        sections = dict((m.group(1), m.group(2)) for m in re.finditer(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S))
        op = sections.get("Original Position", "")
        paras = [p for p in blocks(op) if len(p) > 80]
        unsourced = [p for p in paras if not (CITE.search(p) or CITE_P.search(p))]
        kp = sections.get("Key Passages", "")
        kp_items = [b for b in blocks(kp) if any(len(norm(q).split()) >= 4 for q in QUOTE.findall(b)) or re.search(r"paraphrase", b, flags=re.I)]
        kp_uncited = [b for b in kp_items if not (CITE.search(b) or CITE_P.search(b))]
        # every quotation anywhere in the entry must be cited, or repeat words from a cited quotation
        # Convention: a double-quoted span of 4+ words is a quotation of a source; shorter spans are
        # mentions ("the same agent"); titles go in italics. [P:key:page] (in-copyright, page-cited)
        # counts as a citation exactly like [L:id:line].
        cited_q, loose_q = [], []
        for blk in blocks(text):
            qs = [q for q in QUOTE.findall(blk) if len(norm(q).split()) >= 4]
            (cited_q if (CITE.search(blk) or CITE_P.search(blk)) else loose_q).extend(qs)
        cited_all = " | ".join(norm(q) for q in cited_q)

        def echoed(q: str) -> bool:
            segs = [norm(s) for s in re.split(r"\.\s?\.\s?\.|…|\[[^\]]*\]", q)]
            return all(s in cited_all for s in segs if len(s.split()) >= 2)

        stray = [norm(q) for q in loose_q if not echoed(q)]
        standing_uncited = []
        if "Standing" in sections:
            subs = dict((m.group(1).strip(), m.group(2)) for m in
                        re.finditer(r"^### ([^\n]+)\n(.*?)(?=^### |\Z)", sections["Standing"], flags=re.M | re.S))
            standing_uncited += [b for b in blocks(subs.get("Reception", ""))
                                 if not (CITE.search(b) or CITE_P.search(b) or CITE_E.search(b))]
            standing_uncited += [b for b in blocks(subs.get("Measured", ""))
                                 if b.strip() != "None available." and re.search(r"\d+(\.\d+)?\s*%", b)
                                 and not CITE_P.search(b)]
            # one bullet per deployment profile, each driven by at least one D-code
            standing_uncited += [b for b in blocks(subs.get("For Agents", ""))
                                 if b.startswith("- ") and not re.search(r"\bD\d+\b", b)]
        total_para += paraphrase; total_unsourced += len(unsourced); total_stray += len(stray)
        total_standing += len(standing_uncited)
        status = "clean" if not (paraphrase or unsourced or kp_uncited or stray or standing_uncited) else ""
        print(f"{path.stem:40s} paraphrase {paraphrase:3d} | OP unsourced {len(unsourced):2d}/{len(paras):2d} "
              f"| KP uncited {len(kp_uncited):2d}/{len(kp_items):2d} | stray quotes {len(stray):2d} "
              f"| standing uncited {len(standing_uncited):2d} {status}")
        if args.verbose:
            for p in unsourced:
                print(f"    unsourced OP: {' '.join(p.split())[:90]}")
            for b in kp_uncited:
                print(f"    uncited KP: {' '.join(b.split())[:90]}")
            for q in stray:
                print(f"    stray: \"{q[:80]}\"")
            for b in standing_uncited:
                print(f"    uncited Standing: {' '.join(b.split())[:90]}")
    print(f"total: {total_para} paraphrase marks, {total_unsourced} unsourced Original Position paragraphs, "
          f"{total_stray} uncited quotations, {total_standing} uncited Standing items")
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("check"); s.add_argument("--pin", action="store_true"); s.set_defaults(f=cmd_check)
    s = sub.add_parser("index"); s.set_defaults(f=cmd_index)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--text"); s.add_argument("-n", type=int, default=10); s.set_defaults(f=cmd_search)
    s = sub.add_parser("show"); s.add_argument("loc"); s.add_argument("-C", type=int, default=12); s.set_defaults(f=cmd_show)
    s = sub.add_parser("verify"); s.add_argument("entries", nargs="*"); s.add_argument("-v", "--verbose", action="store_true"); s.set_defaults(f=cmd_verify)
    s = sub.add_parser("lint"); s.add_argument("entries", nargs="*"); s.add_argument("-v", "--verbose", action="store_true"); s.set_defaults(f=cmd_lint)
    args = ap.parse_args()
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
