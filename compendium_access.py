"""compendium_access.py — Showing the Compendium to a model a little at a time.

A local model has roughly 8k tokens of context, and the whole corpus is far
larger than that. Retrieval was tried first and reverted: lexical scoring
over a small corpus matched on incidental word overlap, and a fixed "top k"
forced irrelevant entries into the prompt. This module uses progressive
disclosure instead. Each level is small enough to read in full, and the
model, not a word-overlap score, decides what to open next.

    Level 0  index      one line per entry: id, title, grounding, first concepts.
                        The model reads the whole index (~40 tokens/entry).
                        Once the index outgrows its budget, a domain list comes
                        first and the model opens only the domains it names.
    Level 1  brief      an entry's Summary and its strongest counter-position.
    Level 2  section    one named section of an entry, on request.

`consult()` runs the selection step: the model reads the index and the
question, and names at most a few entries (and optionally one section of
each). An empty selection is a good answer when the corpus doesn't cover
the question, and nothing is disclosed then.

What is disclosed is the corpus's own text, never a model's paraphrase of
it. Citation markers ([L:...], [P:...]) are stripped from the model-facing
text to save tokens. The entry ids stay, so every line can be traced back
to its sourced entry. Each brief carries the entry's first counter-position
as well: the Compendium requires counter-positions, and showing a position
without its rival would be a floor built out of data.

Reads dist/compendium.jsonl, so run tools/build.py after editing entries.
`stale` is True when an entry file is newer than the build. Standard
library only. Consumers find this file at $COMPENDIUM_ROOT or as a sibling
folder of their own checkout.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist" / "compendium.jsonl"

# Sections a model may ask for at level 2. Summary is already in the brief,
# and Key Passages / Original Position are the sourcing apparatus.
SECTIONS = ("Grounding", "Extension to Agents", "Extension to Digital Ecosystems",
            "Counter-Positions", "Open Questions", "Context")

_CITATION = re.compile(r"\s*\[(?:L|P):[^\]]+\]")

HEADER = (
    "FROM THE COMPENDIUM ({version}). The Compendium is a philosophy corpus. Each entry "
    "states a thinker's position in its own scope; anything it says about artificial "
    "agents or digital ecosystems is the Compendium's own extension, marked as such. "
    "These are referents, not rulings. Each comes with its strongest counter-position, "
    "and none of them settles the question for you. Citations are omitted here; the "
    "entry id names the sourced entry."
)

SELECT_SYSTEM = (
    "You choose which entries of a philosophy corpus, the Compendium, bear on a question. "
    "You are not answering the question. Read the index, then name the entries whose "
    "concepts the question actually turns on. Shared words are not enough: an entry about "
    "personal identity doesn't bear on a tax question because both mention 'persons'. "
    "An empty list is a good answer when the corpus doesn't cover the question."
)

DOMAIN_USER = """QUESTION:
{question}

The Compendium is organized in these domains:
{domains}

Name the domains whose entries could bear on the question, at most {max_domains}.
Respond with JSON only, no other text:
{{"domains": ["<domain>"]}}"""

SELECT_USER = """QUESTION:
{question}

COMPENDIUM INDEX (id | title [grounding]: concepts)
{index}

Choose at most {max_entries} entries. For each, you may also ask for one further section,
from: {sections}. Ask only if the brief summary would not be enough.

Respond with JSON only, no other text:
{{"entries": [{{"id": "<entry id>", "why": "<one sentence>", "section": "<section name or null>"}}]}}"""


def strip_citations(text: str) -> str:
    return _CITATION.sub("", text)


def final_text(raw: str) -> str:
    """The answer part of a raw completion: the final Harmony channel for gpt-oss,
    or the text after a </think> block for Qwen3-style reasoning models."""
    if "<|channel|>final<|message|>" in raw:
        raw = raw.rsplit("<|channel|>final<|message|>", 1)[1]
        return re.split(r"<\|(?:end|return|start)\|>", raw, maxsplit=1)[0].strip()
    if "</think>" in raw:
        return raw.rsplit("</think>", 1)[1].strip()
    return raw.strip()


@dataclass
class Consultation:
    """What one consult() call asked, chose and disclosed. Kept by the caller as provenance."""
    version: str
    question: str
    selected: list[dict] = field(default_factory=list)   # {"id", "why", "section"}
    rejected: list[str] = field(default_factory=list)    # ids the model named that don't exist
    domains: Optional[list[str]] = None                  # domains opened, if the index was split
    text: str = ""                                       # the disclosed block ("" if nothing)
    raw: str = ""                                        # the selection call's raw output
    error: Optional[str] = None

    @property
    def ids(self) -> list[str]:
        return [s["id"] for s in self.selected]

    def identity(self) -> str:
        """One line for a recommender identity: which Compendium, and what of it was read."""
        if self.error:
            return f"{self.version}; consultation failed: {self.error}"
        if not self.selected:
            return f"{self.version}; consulted, no entry selected"
        return f"{self.version}; consulted: {', '.join(self.ids)}"

    def to_dict(self) -> dict:
        return {"version": self.version, "question": self.question, "selected": self.selected,
                "rejected": self.rejected, "domains": self.domains, "disclosed_chars": len(self.text), "error": self.error,
                "raw": self.raw}


class Compendium:
    def __init__(self, dist: Path = DIST):
        dist = Path(dist)
        if not dist.exists():
            raise FileNotFoundError(f"{dist} not found; run tools/build.py in the Compendium")
        data = dist.read_bytes()
        self._entries: dict[str, dict] = {}
        for line in data.decode("utf-8").splitlines():
            if not line.strip():
                continue
            chunk = json.loads(line)
            e = self._entries.setdefault(chunk["entry_id"], {"meta": chunk, "sections": {}})
            e["sections"][chunk["section"]] = chunk["text"]
        self.digest = hashlib.sha256(data).hexdigest()
        self.version = f"compendium {self.digest[:12]} ({len(self._entries)} entries)"
        entries_dir = dist.parent.parent / "entries"
        built = dist.stat().st_mtime
        self.stale = any(p.stat().st_mtime > built for p in entries_dir.rglob("*.md")) \
            if entries_dir.exists() else False

    # ---------------------------------------------------------------- levels

    @property
    def ids(self) -> list[str]:
        return list(self._entries)

    def has(self, entry_id: str) -> bool:
        return entry_id in self._entries

    def title(self, entry_id: str) -> str:
        return self._entries[entry_id]["meta"]["title"]

    def domains(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for e in self._entries.values():
            out[e["meta"]["domain"]] = out.get(e["meta"]["domain"], 0) + 1
        return out

    def index_line(self, entry_id: str) -> str:
        m = self._entries[entry_id]["meta"]
        concepts = "; ".join(c if len(c) <= 48 else c[:45] + "..." for c in m["concepts"][:3])
        return f"{entry_id} | {m['title']} [{m['grounding']}]: {concepts}"

    def index_text(self, domains: Optional[list[str]] = None) -> str:
        """Level 0: one line per entry, for the whole corpus or only the named domains."""
        return "\n".join(self.index_line(eid) for eid, e in self._entries.items()
                         if domains is None or e["meta"]["domain"] in domains)

    def domain_text(self) -> str:
        """Above level 0, for when the index no longer fits: each domain and its titles."""
        lines = []
        for d, n in self.domains().items():
            titles = [e["meta"]["title"].split(":")[0] for e in self._entries.values()
                      if e["meta"]["domain"] == d]
            lines.append(f"{d} ({n} entries): {', '.join(titles[:12])}" + (", ..." if n > 12 else ""))
        return "\n".join(lines)

    def brief(self, entry_id: str, counter_limit: int = 600) -> str:
        """Level 1: Summary plus the first counter-position."""
        e = self._entries[entry_id]
        m = e["meta"]
        lines = [f"[{entry_id}] {m['title']} ({', '.join(m['thinkers'])}, {m['era']}; "
                 f"grounding: {m['grounding']})",
                 strip_citations(e["sections"].get("Summary", "")).strip()]
        counter = self._first_item(e["sections"].get("Counter-Positions", ""))
        if counter:
            if len(counter) > counter_limit:
                counter = counter[:counter_limit - 3].rstrip() + "..."
            lines.append("Strongest counter-position: " + counter)
        return "\n".join(lines)

    def section(self, entry_id: str, name: str) -> str:
        """Level 2: one section of an entry, citations stripped ("" if it has none)."""
        return strip_citations(self._entries[entry_id]["sections"].get(name, "")).strip()

    @staticmethod
    def _first_item(text: str) -> str:
        text = strip_citations(text).strip()
        m = re.search(r"^- (.+?)(?=^- |\Z)", text, flags=re.S | re.M)
        return re.sub(r"\s+", " ", (m.group(1) if m else text)).strip()

    def disclose(self, selected: list[dict], budget_chars: int = 6000) -> str:
        """Briefs for every selected entry first, then requested sections while they fit."""
        if not selected:
            return ""
        parts = [HEADER.format(version=self.version)]
        parts += [self.brief(s["id"]) for s in selected]
        used = sum(len(p) for p in parts)
        for s in selected:
            name = s.get("section")
            if not name:
                continue
            body = self.section(s["id"], name)
            if not body:
                continue
            block = f"[{s['id']}] {name}:\n{body}"
            if used + len(block) > budget_chars:
                parts.append(f"[{s['id']}] {name}: omitted, it would not fit the context budget.")
                continue
            parts.append(block)
            used += len(block)
        return "\n\n".join(parts)

    # ------------------------------------------------------------- selection

    def selection_prompts(self, question: str, max_entries: int = 3,
                          domains: Optional[list[str]] = None) -> tuple[str, str]:
        return SELECT_SYSTEM, SELECT_USER.format(
            question=question.strip(), index=self.index_text(domains), max_entries=max_entries,
            sections=", ".join(SECTIONS))

    @staticmethod
    def _json_answer(raw: str, key: str) -> dict:
        text = final_text(raw)
        for m in reversed(list(re.finditer(r"\{", text))):
            try:
                cand = json.JSONDecoder().raw_decode(text[m.start():])[0]
            except ValueError:
                continue
            if isinstance(cand, dict) and isinstance(cand.get(key), list):
                return cand
        raise ValueError(f"no {{\"{key}\": [...]}} object in the answer")

    def parse_selection(self, raw: str, max_entries: int = 3) -> tuple[list[dict], list[str]]:
        """(valid selections, unknown ids). Raises ValueError if no JSON answer is found."""
        obj = self._json_answer(raw, "entries")
        selected, rejected, seen = [], [], set()
        for item in obj["entries"]:
            if isinstance(item, str):
                item = {"id": item}
            if not isinstance(item, dict):
                continue
            eid = str(item.get("id", "")).strip()
            if not self.has(eid):
                if eid:
                    rejected.append(eid)
                continue
            if eid in seen:
                continue
            seen.add(eid)
            section = item.get("section")
            selected.append({"id": eid, "why": str(item.get("why") or "").strip(),
                             "section": section if section in SECTIONS else None})
        return selected[:max_entries], rejected

    def consult(self, question: str, complete: Callable[[str, str], str], max_entries: int = 3,
                budget_chars: int = 6000, index_budget_chars: int = 8000) -> Consultation:
        """Let the model choose from the index, then disclose what it chose. Never raises.

        If the whole index is longer than index_budget_chars, the model first picks
        domains from domain_text(), and only those domains' index lines are shown."""
        c = Consultation(version=self.version, question=question)
        try:
            domains = None
            if len(self.index_text()) > index_budget_chars:
                raw = complete(SELECT_SYSTEM, DOMAIN_USER.format(
                    question=question.strip(), domains=self.domain_text(), max_domains=3))
                named = [d for d in self._json_answer(raw, "domains")["domains"] if d in self.domains()]
                c.domains = named
                if not named:
                    c.raw = raw
                    return c
                domains = named
            system, user = self.selection_prompts(question, max_entries, domains)
            c.raw = complete(system, user)
            c.selected, c.rejected = self.parse_selection(c.raw, max_entries)
        except Exception as e:  # the caller's analysis goes on without the Compendium
            c.error = f"{type(e).__name__}: {e}"
            return c
        c.text = self.disclose(c.selected, budget_chars)
        return c


def locate(start: Path, env_var: str = "COMPENDIUM_ROOT") -> Path:
    """Find a Compendium checkout: $COMPENDIUM_ROOT, else a sibling folder named Compendium
    of `start` or any of its parents."""
    import os
    env = os.environ.get(env_var)
    candidates = [Path(env)] if env else [p / "Compendium" for p in [start, *start.parents]]
    for c in candidates:
        if (c / "compendium_access.py").exists():
            return c
    raise FileNotFoundError(f"Compendium not found: set {env_var} to the Compendium folder")


if __name__ == "__main__":
    import sys
    comp = Compendium()
    if len(sys.argv) > 1 and sys.argv[1] in comp.ids:
        print(comp.brief(sys.argv[1]))
    else:
        idx = comp.index_text()
        print(idx)
        print(f"\n{comp.version}; index {len(idx)} chars (~{len(idx) // 4} tokens)"
              + ("; STALE: rebuild with tools/build.py" if comp.stale else ""))
