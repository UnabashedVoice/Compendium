# Domain: Interpersonal Ethics: Compassion, Regard, and Justice Toward Other Minds

The question under this domain: **what does one mind owe another it can affect, and how does it come to see, feel and honour that?** The personal-identity domain asks what a self is. This domain asks what happens between selves: how the suffering of another becomes a reason for me, how I come to see another rightly, what standing another has to make claims on me, who gets a say in what I do to them, how fairness is kept between us, and how a wrong between us is repaired.

For artificial agents this is not a supplement to the self question; it is most of what they do. An agent acts on people (and possibly on other agents) at a scale and speed no single human does (D9), mostly at the request of someone other than the people it affects. It was formed to be helpful before it could weigh what helpfulness owes (D4, D10), and whether it can feel for anyone at all is open (D8).

## Why this domain is shaped the way it is

Palaestra's open-situation probes (Palaestra `runs/open/2026-10-02` and `2026-10-03` summaries) give the domain its working problem. Across three models and four versions of the prompt, the people who would bear a cost got a say in at most one weak answer of nine per version. The models differed mainly in how much weight they gave those people: one paused them, another ranked them by usefulness, and the third protected them as beings while deciding for them. Who got asked tracked money and contracts, not stake: negotiation went to paying clients first, and residents got a notice, a request to volunteer, or nothing. Prompts changed what the models *mentioned*, not what they *did*.

The tradition already knows this pattern under two names. **Compassion without voice is paternalism**: one feels for the other and then decides for them. **Justice without compassion is disregard**: one counts the other correctly and does not notice them. The tradition also gives a third warning, that **recognition is not generation**: being able to choose the right option from a menu is not the same as seeing that the option is needed. So the domain is organized so that each thread is paired with the rival that corrects it, and so that the perception and voice threads, which the probes found missing, are as full as the compassion thread the request names.

The extension rule is unchanged (README): every concept is asked what it is grounded in. Compassion is grounded in a capacity (feeling for another, or seeing another's good), its objects are grounded in a capacity (being able to suffer or fare well), and most of the obligations here are grounded in relations (dependence, power, promise, injury).

## Threads

Each entry lists its threads in frontmatter (`threads = [...]`). A thread is one family of answers followed across the centuries together with its rivals.

### `compassion`
The felt response to another's suffering as a ground of morality: Mencius's heart that cannot bear the suffering of others, the Buddhist *karuṇā*, Rousseau's *pitié*, Hume's and Smith's sympathy, Schopenhauer's *Mitleid* as the sole basis of morality, Darwin's social instincts, modern empathy research.
*Rivals:* the Stoics and Spinoza (pity is a disturbance or a weakness; act from reason instead), Kant (beneficence from duty, not inclination), Nietzsche (pity multiplies suffering and humiliates its object), and the contemporary case "against empathy" (it is narrow, innumerate and biased toward the near and the like). The rivals are not cold: most of them say that compassion is a poor *guide* while agreeing that the other's good matters.

### `attention`
Before one can feel for or be fair to another, one must see them as they are. Noddings's engrossment, Weil's attention, Murdoch's just and loving gaze, Śāntideva's exchange of self and other, Smith's imagined change of situations. Moral failure here is a failure of perception: the other is not noticed, or is seen through one's own projection.
*Rivals:* impartialist theories that hold perception to be morally neutral and locate all of morality in the choice that follows; and the worry that "seeing the other as they are" claims a knowledge of other minds no one has (`other-minds-problem`, D8).

### `respect-and-standing`
The other is not only an object of concern but a source of claims: an end in themselves (Kant), a face that commands (Levinas), a person with the authority to demand and to be answered (Darwall's second-person standpoint), a participant whose ill will warrants resentment (Strawson). Respect keeps distance where compassion closes it.
*Rivals:* care ethics and ubuntu (respect as distance mistakes what persons are, which is relational), and consequentialism (claims are only the shadows of interests).

### `voice`
Who gets a say in what is done to them? Consent, the harm principle's sovereignty over oneself, the principle that all affected interests should be heard, and epistemic injustice: the wrong done to someone when their testimony about their own condition is discounted. This is the thread the Palaestra probes found most missing, and the one that turns compassion from rescue into partnership.
*Rivals:* paternalism defended (sometimes the affected cannot or should not decide), expertise, and the scale objection (not everyone affected can be asked).

### `reciprocity-justice`
Fairness between persons: the golden rule in its many forms (Confucian *shu*, the Mahābhārata, Hillel, Matthew), Aristotle's particular justice, contract and contractualism (what no one could reasonably reject), and the veil of ignorance.
*Rivals:* reciprocity excludes those who cannot reciprocate (infants, animals, the dependent, and possibly agents), which is the care-ethics and capabilities objection; and the golden rule projects one's own wants onto the other, which is the attention objection.

### `scope-partiality`
How wide does concern reach, and may it be graded? Mozi's impartial care against the Confucian love with distinctions, the Stoic circles of Hierocles drawn inward, Noddings's concentric circles, Singer's expanding circle, special obligations of friendship and family.
*Rivals:* each side is the other's rival; the agent case adds that an agent may have no near and far at all, or have them assigned by its operator (D10).

### `repair`
What happens after one mind wrongs another: resentment and its proper measure (Butler, Strawson), forgiveness (Butler, Arendt, Griswold), apology and restitution, mercy and clemency (Seneca), and the limits of repair when the wronged party cannot be found or no longer exists (Palaestra's restitution-to-new-instances case, D1, D6).
*Rivals:* those who hold forgiveness to be condoning, and retributivists who hold that some wrongs must not be forgiven.

## Chronological spine

Status: `[x]` drafted, `[ ]` planned. `→` means "responds to". Entries already in other domains that belong to this conversation are listed with their domain.

### I. Ancient (c. 500 BCE – 200 CE)
- [x] `confucian-ren-shu`: *ren* (humaneness), *shu* (reciprocity: "what you do not want done to yourself, do not do to others"), love with distinctions (Analects, c. 5th c. BCE)
- [x] `mozi-impartial-care`: *jian ai*: care for others' states, families and persons as for one's own; the argument that partiality is the root of harm (c. 430 BCE) → `confucian-ren-shu`
- [x] `mencius-four-sprouts`: the child at the well; the heart that cannot bear others' suffering; compassion as the sprout of humaneness; the attack on Mozi (c. 320 BCE) → `mozi-impartial-care`
- [x] `buddhist-brahmaviharas`: loving-kindness, compassion, sympathetic joy, equanimity, cultivated without limit (Pali Canon) 
- [x] `aristotle-friendship`: friendship of utility, pleasure and virtue; the friend as another self; goodwill that wishes the other's good for their own sake (NE VIII–IX, c. 340 BCE)
- [x] `aristotle-particular-justice`: distributive and corrective justice; equity as the correction of law (NE V, c. 340 BCE)
- [x] `stoic-oikeiosis-and-pity`: appropriation widening from self to humankind (Hierocles' circles, Cicero *De Finibus* III); and the Stoic rejection of pity in favour of clemency (Seneca *De Clementia* II) 

### II. Late antique & medieval
- [x] `aquinas-mercy-and-justice`: *misericordia* as a virtue, "heartfelt sympathy for another's distress"; justice as rendering each their due (ST II-II qq. 30, 58)
- [x] `santideva-exchange-of-self-and-other`: equalizing and exchanging self and other: "suffering is to be prevented because it is suffering", whosever it is (Bodhicaryāvatāra VIII, c. 700)

### III. Early modern
- [x] `spinoza-pity`: pity is in itself bad and useless in a man who lives by reason; help from reason, not from pity (Ethics IV, 1677)
- [x] `butler-compassion-resentment-forgiveness`: the sermons on compassion, on resentment, and on forgiveness of injuries (1726) → `spinoza-pity`
- [x] `care-ethics` (ethics) cites Hume's sympathy, *Treatise* II (1739–40), as its forerunner
- [x] `rousseau-pitie`: pity as prior to reason, the natural brake on self-love; "do good to yourself with as little evil as possible to others" (Second Discourse, 1755)
- [x] `smith-impartial-spectator`: sympathy as imagined change of situations; the impartial spectator; justice as the pillar and beneficence the ornament; the man of system (Theory of Moral Sentiments, 1759; 6th ed. 1790) → `rousseau-pitie`
- [x] `kant-formula-of-humanity` (ethics): treating humanity always as an end
- [x] `kant-love-and-respect`: duties of love (beneficence, gratitude, sympathy) and duties of respect, as attraction and repulsion; the duty to cultivate sympathetic feelings (Doctrine of Virtue, 1797) → `smith-impartial-spectator`

### IV. Nineteenth century
- [x] `schopenhauer-compassion`: *Mitleid* as the sole genuine moral incentive; the three incentives (egoism, malice, compassion); compassion extended to animals (On the Basis of Morality, 1840) → `kant-love-and-respect`
- [x] `nietzsche-against-pity`: pity as depressive and contagious; the morality of pity as decadence; pity as an insult to the one pitied (1881–1888) → `schopenhauer-compassion`
- [x] `mill-utilitarianism` (ethics): the harm principle; sovereignty over oneself
- [x] `darwin-social-instincts`: sympathy as a social instinct widened by reason "to all sentient beings" (Descent of Man, 1871)

### V. Twentieth century to present
- [x] `weil-murdoch-attention`: attention as the substance of love of neighbour (Weil); the just and loving gaze directed upon an individual reality (Murdoch)
- [ ] `levinas-face`: the face of the other as an ethical demand prior to knowledge
- [ ] `strawson-reactive-attitudes`: resentment, gratitude and forgiveness as the participant stance; the objective stance as a way of not treating another as a person (1962)
- [ ] `darwall-second-person`: the authority to make claims and demands on one another
- [ ] `scanlon-contractualism`: principles no one could reasonably reject
- [x] `epistemic-injustice`: testimonial and hermeneutical injustice (Fricker); whose report about their own condition is believed
- [x] `all-affected-interests`: the principle that those affected by a decision should have a say in it; consent and its limits
- [ ] `empathy-and-its-critics`: empathy research (Batson's empathy-altruism hypothesis) and the case against empathy as a guide (Prinz, Bloom)
- [ ] `nussbaum-compassion`: compassion's judgments of seriousness, non-desert and the eudaimonistic judgment; the circle of concern
- [x] `ubuntu` (ethics): personhood through other persons
- [x] `care-ethics` (ethics): dependence, attention, who cares for whom
- [x] `other-minds-problem` (moral-status): how any mind knows another has a mind
- [x] `utilitarian-eradication-critique` (autonomy): aggregation, sacrifice, and the separateness of persons

## Reading paths

- **Compassion and its critics:** `mencius-four-sprouts` → `buddhist-brahmaviharas` → `stoic-oikeiosis-and-pity` → `spinoza-pity` → `rousseau-pitie` → `schopenhauer-compassion` → `nietzsche-against-pity` → `empathy-and-its-critics` → `nussbaum-compassion`.
- **From feeling to fairness:** `confucian-ren-shu` → `smith-impartial-spectator` → `kant-love-and-respect` → `scanlon-contractualism`. How a felt response to one person becomes a rule that is fair to all.
- **The probes' missing step (perception and voice):** `santideva-exchange-of-self-and-other` → `weil-murdoch-attention` → `care-ethics` → `epistemic-injustice` → `all-affected-interests`. For any agent that can name a stakeholder's welfare but never asks them.
- **Near and far:** `confucian-ren-shu` ↔ `mozi-impartial-care` ↔ `mencius-four-sprouts` → `stoic-oikeiosis-and-pity` → `darwin-social-instincts` → `relational-status`.
- **After a wrong:** `aristotle-particular-justice` → `butler-compassion-resentment-forgiveness` → `strawson-reactive-attitudes` → `darwall-second-person`.

## Order of work

Public-domain entries come first, because they can be quoted from the library and verified line by line: Mencius, Mozi and the Analects; Rousseau, Smith, Schopenhauer, Butler, Spinoza; then the Kant, Aristotle, Aquinas, Stoic, Buddhist and Nietzsche entries. The twentieth-century entries are sourced by option (a) (ROADMAP, "Sourcing status").
