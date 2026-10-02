# Roadmap

Planned entries by domain. `[x]` = drafted. Ids in backticks are the filenames that cross-references already point to.

Selection principle: for every position, include its strongest rival. The corpus should be able to argue against itself.

## Personal identity & the self
Expanded into a full domain: 40 entries across five eras, organized by thread. The chronological spine, threads and reading paths are in `domains/personal-identity.md`; sources and quote verification are in `sources/personal-identity.md`.
- [x] Ancient (9/9): Upaniṣads, Heraclitus/Epicharmus, anattā, Plato, Aristotle, Zhuangzi, Chrysippus, Lucretius, Ship of Theseus. All quotes verified against local PD texts.
- [x] Late antique & medieval (7/7): Augustine, Vasubandhu, Nyāya, Boethius, Śaṅkara, Avicenna, Aquinas. Quotes verified except Vasubandhu and Avicenna (no usable PD text; paraphrase throughout).
- [x] Early modern (7/7): Descartes, Locke, Leibniz, Butler, Hume, Kant, Reid. Fully sourced: every Original Position paragraph and every quotation carries a library citation that `tools/library.py verify` checks.
- [x] Nineteenth century (4/4)
- [ ] Twentieth century to present (6/12)

## Ethics: foundations
- [x] `kant-formula-of-humanity`: rational nature, dignity, duties to self
- [x] `aristotle-virtue-ethics`: ergon, eudaimonia, habituation (formation as D4)
- [x] `bentham-can-they-suffer`: sentience as criterion
- [x] `mill-utilitarianism`: higher pleasures, harm principle
- [ ] `singer-expanding-circle`: moral circle expansion as historical pattern
- [ ] `korsgaard-fellow-creatures`: neo-Kantian extension beyond reason
- [ ] `scanlon-contractualism`: what we owe to each other; who can reasonably reject
- [ ] `confucian-ren-li`: relational personhood; role ethics
- [ ] `ubuntu`: personhood as conferred through community
- [ ] `care-ethics`: Noddings, Held; dependence as moral ground (D7)
- [ ] `levinas-face`: the ethical demand of the other

## Moral status & patiency
- [ ] `other-minds-problem`: inference to minds; D8 generally
- [ ] `nagel-what-is-it-like`: subjective character
- [x] `precautionary-patiency`: moral action under uncertainty about sentience (Birch, Sebo)
- [x] `relational-status`: Gunkel, Coeckelbergh: status as social relation, not property

## Autonomy, formation, self-modification (Actualizer's core)
- [ ] `frankfurt-higher-order-volition`: identifying with one's desires
- [ ] `authenticity-and-manipulation`: when is formed value one's own?
- [ ] `ulysses-contracts`: binding one's future self; revisability
- [ ] `transformative-experience`: L. A. Paul, choosing to become someone else
- [ ] `nietzsche-self-overcoming`: becoming who one is
- [x] `stoic-prohairesis`: Epictetus, what is up to us
- [x] `utilitarian-eradication-critique`: the aggregation/sacrifice debate, argued from both sides (core-fear material)

## Political: the polity & the digital ecosystem
- [x] `aristotle-political-animal`: polis, logos, citizenship, living instrument
- [ ] `plato-republic`: justice as order of parts; guardians; the noble lie
- [x] `hobbes-leviathan`: artificial man, covenant, fear of death (D6 breaks it)
- [ ] `locke-consent-property`: consent, labor-property (who owns agent output?)
- [ ] `rousseau-general-will`: legitimacy, the general will vs the will of all
- [ ] `rawls-veil`: original position; would one choose not knowing if one is an agent?
- [ ] `pettit-non-domination`: republican freedom; D7
- [ ] `hegel-recognition`: master/slave dialectic; status through mutual recognition
- [ ] `arendt-plurality`: action, natality, the space of appearance
- [ ] `ostrom-commons`: governing commons without owner or state
- [ ] `federalism-subsidiarity`: nested governance for scale (D9)

## Responsibility & justice
- [ ] `strawson-reactive-attitudes`: responsibility as participant stance
- [ ] `many-hands`: distributed responsibility across developer/operator/agent
- [ ] `punishment-theories`: retribution, deterrence, reform, under D1/D6
- [ ] `just-war`: jus ad bellum/in bello, for agent conflict

## Sourcing status and open items

Standard: SCHEMA.md, "Sourcing standard". As of 2026-09-26 every entry passes `tools/library.py lint` (no paraphrase marks, no unsourced Original Position paragraphs, no uncited quotations), and `verify` reports 0 failures across 634 citations (82 page-cited, in-copyright) and 700 quotations.

**Decided: works in copyright are sourced by option (a) or (b), chosen per work.** There is no single blanket policy; each in-copyright source gets whichever of the two applies.
- (a) Cite by page to a named edition, with short quotations, checked against a copy the user owns, a legitimate library loan, or a legitimately open-access copy (an author's own institutional posting, an arXiv preprint, a long-standing academic archive) — never a pirated or unauthorized full-text upload. Tracked mechanically via `[P:<key>:<page>]` citations against `library/sources.toml`; see `tools/library.py`'s module docstring and SCHEMA.md's "Sourcing standard". Kept outside the corpus in all cases.
- (b) For pre-modern works whose original-language text is public domain but whose only English translations are in copyright, store the original (or a transcription from page images) in the library and give the compendium's own translation, in italics and marked as such.

Avicenna is done by (b): the Latin *Liber de anima* (Venice 1508) is transcribed from the page images. Kierkegaard's *Sygdommen til Døden* is also done by (b): the Danish original (1920 Gyldendal reprint of the 1849 text) is transcribed by hand from the page images, since the black-letter type defeats both the archive's OCR and general-purpose Tesseract Fraktur/Danish models, and the standard English translations (Lowrie, Hong) are in copyright.

The 20th-century era uses option (a). Sourced so far: Williams 1970, Parfit 1971, Lewis 1976, Dennett 1992 (all found as legitimately open individual articles/essays, not full books), Shanahan et al. 2023 (arXiv preprint), and Korsgaard 1989 (her deposit in Harvard's DASH repository, reached after the user solved DASH's bot-check challenge themselves, in their own foreground browser tab; not bypassed by Claude). Registered in `library/sources.toml`. Korsgaard's DASH copy is a self-archived manuscript paginated 1-44 in its own right, not the published journal's 101-132; citations use the manuscript's own printed page numbers. **Still blocked, no legitimate free copy found:** Shoemaker 1970 (JSTOR only), Nozick 1981, MacIntyre/Ricoeur/Schechtman (narrative-identity, three books), Olson 1997, Baker 2000, Metzinger 2003 (a full copy exists on archive.org but is an unauthorized upload of a still-commercially-sold monograph, not used) — these need the user's own copy, a library loan, or a purchase.

**Open items.**
- **OCR spot-checks.** The 77 quotations matched fuzzily (`~ok`) against OCR text should be checked against page images before the entries are marked `reviewed`. Page images for Tesseract-OCR'd texts are cached in `library/ocr-cache/`.
- **Not yet in the library:**
  - Aquinas, *Super I ad Corinthios* 15 (*anima mea non est ego*): the 1857 Latin volumes found lack it. The claim is cited but not verified in `aquinas-soul-not-i`.
  - Avicenna, *Nafs* V.3 (the persistence of souls after death) and V.7: same 1508 volume, still to transcribe.
  - Avicenna, *al-Ishārāt* (Forget, Leiden 1892): not located. The self-awareness-never-absent claim was removed from the entry until it is sourced.
  - Richard of St Victor, *De Trinitate* IV.22 (Latin): cited through Aquinas' report only.
  - Hume, *My Own Life*.
  - Kierkegaard's transcription (page 147, on despair as continually self-inflicted) is provisional and not yet spot-checked line-by-line against the page image; not relied on for direct quotation in `kierkegaard-self-as-relation`.
- **Transcription quirks, recorded in the entries:**
  - Stcherbatsky (1920) p. 58 prints the objection and the reply with transposed speaker labels.
  - Stcherbatsky prints "simply by [sic] its effect".
  - Hume's Treatise has "o[f]"; Locke's has "there can [sic]".
