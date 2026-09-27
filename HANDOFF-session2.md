# Compendium work session: handoff

Paste the prompt below into the new thread.

---

This thread continues work on the Compendium, a philosophy and ethics corpus for ML use at `B:\HouseLLaMas\Claude\Compendium`. It extends "man" and "person" to artificial agents, and "society" to digital ecosystems. The core discipline is **extend by grounding, never by substitution**.

Before doing anything, read these in order:
1. `README.md` (includes "Source library" and "Works in copyright")
2. `SCHEMA.md` (especially "Sourcing standard" — two citation forms, `[L:]` and `[P:]`)
3. `ROADMAP.md` (especially "Sourcing status and open items")
4. `domains/personal-identity.md` (threads, chronological spine, reading paths)
5. Two finished entries as models: `entries/personal-identity/hume-bundle.md` (public-domain, `[L:]`) and `entries/personal-identity/parfit-reductionism.md` (in-copyright, `[P:]`)

Then check that everything is still green:

```
python tools/library.py check      # expect: 72 files, 72 catalog entries, 6 in-copyright sources, 0 problems
python tools/library.py verify     # expect: 0 failed
python tools/library.py lint       # expect: 0 / 0 / 0 totals
python tools/build.py              # expect: 35 entries ok, 0 failed
```

## Where things stand (2026-09-26)

- **Personal-identity domain:** ancient through twentieth-century eras are underway. Ancient, medieval, early-modern, and nineteenth-century (4/4) are done. Twentieth-century is 6/12: Williams, Parfit, Lewis, Dennett, Korsgaard, and `llm-identity-contemporary` (the corpus's own contemporary entry, drawing on Shanahan et al.'s simulator/simulacra framing) are written; Shoemaker, Nozick, the narrative-identity trio (MacIntyre/Ricoeur/Schechtman), Olson, Baker, and Metzinger are blocked (see below). 35 entries total in the corpus (32 personal-identity, 1 ethics, 1 political).
- **Sourcing standard:** every entry passes `lint` (0 paraphrase marks, 0 unsourced Original Position paragraphs, 0 uncited quotations). `verify`: 634 citations (82 page-cited/in-copyright, the rest `[L:]` against stored full texts), 700 quotations, 0 failed. 77 quotes are OCR-fuzzy (`~ok`), awaiting spot-checks against page images (unchanged from earlier sessions — not yet done).
- **Library:** `library/texts/` holds 72 full texts (public-domain originals, plus two compendium transcriptions: Avicenna's Latin and Kierkegaard's Danish). `library/catalog.toml` records each one's edition, source, rights, format (`gutenberg` | `ocr` | `transcription`), sha256. `library/sources.toml` is the newer registry for in-copyright, page-cited sources (`[P:key:page]`), one record per source, no full text stored — six entries so far (Williams, Parfit, Lewis, Dennett, Korsgaard, Shanahan et al.). `library/index.sqlite` is a full-text index (FTS5) over `library/texts/` only. `library/ocr-cache/` holds page images, per-page OCR, and `tessdata/` (lat, ara, dan, Fraktur, eng, osd models).
- **Tools:**
  - `tools/library.py`: `check [--pin]`, `index`, `search`, `show ID:LINE`, `verify`, `lint [-v]`. `verify`/`lint` handle both `[L:]` and `[P:]` citations; see the module docstring for exactly how.
  - `tools/ocr_archive.py <archive-id> <out-id> [--lang lat] [--start N --end M]`: Tesseract OCR from archive.org page images, for texts whose own OCR is unusable.
  - Tesseract 5.5.3 is at `C:\Program Files\Tesseract-OCR\`.
- **Copyright decision:** works in copyright are sourced by option (a) or (b), chosen per work (see README, "Works in copyright", and ROADMAP, "Sourcing status and open items" — there is no single blanket "option", despite what an earlier draft of ROADMAP.md said).
  - (a) Short, page-cited quotation (`[P:key:page]` against `library/sources.toml`), checked against a copy the user owns, a legitimate library loan, or a legitimately open-access copy (author's own posting, institutional repository, arXiv) — never a pirated upload. Used for the twentieth-century entries so far.
  - (b) For a pre-modern work whose original-language text is public domain but whose only English translations are in copyright: store the original (or a hand transcription from page images, when OCR fails) and give the compendium's own translation in italics, marked as such. Used for Avicenna (Latin) and Kierkegaard (Danish).

## Conventions (enforced by the tools)

- `[L:<text-id>:<line>]` or `[L:<text-id>:<start>-<end>]` for a stored public-domain text. `<text-id>` is a file stem in `library/texts/`.
- `[P:<key>:<page>]` or `[P:<key>:<start>-<end>]` for an in-copyright, page-cited source. `<key>` is a record in `library/sources.toml`. `verify` checks the key is registered; it cannot check the quotation's wording, since no full text is held — accuracy there is on the citer.
- Double quotes of 4+ words = a source's exact words. They must sit in the same paragraph or bullet as a citation, or repeat a cited quote from elsewhere in the entry. This includes titles and the compendium's own English renderings of a quote — those go in *italics*, never in double quotes, or `verify`/`lint` will try (and fail) to match them against the source.
- Shorter quoted phrases are mentions; titles, hypotheticals and the compendium's own translations go in *italics*.
- Editorial marks: `[sic]`, `o[f]`, `...`. Quote exactly as the library file reads, typos included.
- Every Original Position paragraph carries a citation. Every Key Passages item is a cited verbatim quote. "(paraphrase)" means unfinished — except it does not apply to option-(a) sourcing, where a short `[P:]`-cited quote is the accepted, finished state.
- **Don't touch TOML frontmatter** when doing quote-to-italics replacements (this broke `nyaya-self` once). Run `build.py` after bulk edits.
- After adding or editing a library text: add a catalog record, then `check --pin`, then `index`. An edited text needs its sha256 line removed before re-pinning.
- Every entry's frontmatter `disanalogies` array should match the D-codes actually discussed in its body (both directions) — checked in the 2026-09-26 audit; keep it that way.
- Keep `domains/personal-identity.md`'s chronological-spine checkboxes and `ROADMAP.md`'s per-era counts in sync with reality as entries are added.

## Workflow that worked

For each entry:
1. `search` the index (for `[L:]` sources) and `show` or `sed -n` the lines; for `[P:]` sources, find a legitimately open copy, convert to text (`pdftotext -layout`, or PyMuPDF/Tesseract when the text layer is garbled or absent — see below), and locate real page numbers.
2. Write the Original Position and Key Passages with citations. Replace the sections from "## Original Position" to "## Grounding" wholesale.
3. `verify <entry>`, then `lint -v <entry>`, and fix what they report.
4. Update `domains/personal-identity.md`'s checkbox and `ROADMAP.md`'s era count.

When archive.org's own OCR is garbage (Devanagari-engine scans, black-letter/Fraktur type), use `ocr_archive.py`, or PyMuPDF (`fitz`) + Tesseract directly, or transcribe by hand from the page images. When a PDF's text layer is corrupted (a custom font encoding poppler can't resolve — check for "Unknown character collection" warnings from `pdftotext`), try PyMuPDF's `get_text()` instead; it handles some encodings poppler doesn't.

For in-copyright PDFs behind a bot-check wall (CAPTCHA): never solve it yourself. If the user is willing, open it in a foreground Chrome tab (`mcp__claude-in-chrome__navigate`), tell them where it stopped, and wait for them to clear it in their own browser before continuing.

Windows notes: use `PYTHONIOENCODING=utf-8` when printing non-Latin text. Heredocs containing apostrophes can break Bash; write scripts to the scratchpad instead. `pdftotext`/PyMuPDF page numbers frequently don't match a journal article's own printed pagination — check both a manuscript's own printed page numbers (if it has them, as Korsgaard's DASH deposit did) and the journal's front-matter citation before assuming they're the same.

## Next steps (in order)

1. **Finish the twentieth century** (6/12 done): the six blocked sources (Shoemaker 1970, Nozick 1981, MacIntyre/Ricoeur/Schechtman, Olson 1997, Baker 2000, Metzinger 2003) need the user's own copy, a library loan, or a purchase — no legitimate free copy was found for any of them as of this session.
2. **Open items** (ROADMAP): Avicenna *Nafs* V.3 (the persistence-after-death part) and V.7, from the same 1508 volume, `bub_gb_JJThV3vtDJIC`; Aquinas *Super I Cor.* 15; Avicenna *Ishārāt* (Forget 1892); Richard of St Victor, *De Trinitate* IV.22; spot-check the 77 `~ok` OCR-fuzzy matches against page images.
3. **After personal-identity is closer to done:** the other domains in ROADMAP.md are still at 1 entry each (ethics: `kant-formula-of-humanity`; political: `aristotle-political-animal`) with no `domains/<domain>.md` or `sources/<domain>.md` files yet — those get created once each domain has enough entries to need threads/reading paths.

## Questions still pending for the user

- Where are their copies of the six still-blocked twentieth-century works (or would a library loan or purchase make more sense), and in what format?
- Should `library/ocr-cache/` (~209 MB, regenerable) and `library/index.sqlite` (~128 MB, regenerable) be `.gitignore`d if the Compendium goes to GitHub? (There is no git repo here yet at all, and no `.gitignore`.)

Standing preferences (in memory): give real pushback, not agreeableness; on design questions, extend the user's idea structurally, don't just mirror it; the Compendium stays separate from Actualizer and Palaestra, with no wiring yet.
