---
type: challenge
name: "The Counterpart Stacks"
slug: counterpart-stacks
status: review
source: custom
page: "294–300, 310, 319"
owner: WP7c
canon_refs: ["Bible §3 power structure", "Brief §8", "Plan A.6", "Core p. 294–300", "Core p. 310", "Core p. 319"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: barrier
scale: 2
alias: "a warehouse full of paper"
short_description: "Four hundred metres of shelving holding the second half of Palisade's official memory: numbered runs, a scanning crew's arc-lamp, a duty clipboard, and a bonded cage. It cannot be hacked and it does not fight; it costs time, and time is the thing the crew do not have."
limits:
  - {name: find-the-volume, tier: 3}
  - {name: open-the-cage, tier: 4}
  - {name: leave-no-trace, tier: 5}
  - {name: take-over-or-shut-down, tier: 999}
default_tags: ["four hundred metres of steel shelving", "runs numbered, contents not", "an arc-lamp gantry moving one run a night", "a duty clipboard that is the only real index", "a bonded cage with a certificate on it"]
default_statuses: ["quiet-3"]
specials:
  - {name: "Paper Cannot Be Harnessed", text: "The counterpart set exists on shelves for the same reason the registry does ([[chancery-process]] *Not On The Net*): paper cannot be Harnessed. take-over-or-shut-down is immune, and no cyberspace action produces a page that has not been scanned yet. The scan index in a Domain in [[the-lattice]] can tell the crew which run a volume is in; it cannot tell them what is on a page still in the building."}
  - {name: "The Clipboard Is The Index", text: "The runs are numbered and their contents are not. The only working index of what is where is the duty clerk's clipboard in the office, updated by hand by whoever is on shift. Taking, copying or altering it drops find-the-volume by two tiers — and a missing clipboard is noticed at the shift change, which advances [[collection-run]] and sets leave-no-trace back to full."}
  - {name: "An Hour You Did Not Budget For", text: "Reading is not free. Any scene in which a PC reads more than a page or two of a volume inside the bay advances [[collection-run]] by one tier per exchange, and each advance is also a tier off leave-no-trace, because the gantry keeps moving and the crew are standing under it. A crew that carries the volume out and reads it elsewhere pays neither cost, and learns everything later than the MC would like."}
  - {name: "Certified Means Sealed", text: "A volume marked certified — awaiting collection is inside the bonded cage under a numbered certificate. The certificate must be physically broken to open the cage, and breaking it converts the theft from something discovered at the next collection into something discovered at the next inspection. Once the certificate is broken, leave-no-trace can no longer be maxed; the best available outcome is that nobody can say who."}
  - {name: "It Burns", text: "Five hundred bound pages in a room of five hundred more. Any fire, incendiary, energy discharge, or fire-suppression event in the bay destroys the contents of the run it happens in, on a scale the MC chooses, starting with whatever the crew are holding. This is a Consequence, not a Threat: it is what happens when a fight starts in here."}
threats:
  - threat: "The arc-lamp gantry finishes a run and starts down the next one, and the next one is theirs."
    consequences:
      - {text: "The crew are lit and the scanning crew are eleven metres away (exposed-2), and leave-no-trace loses a tier.", statuses: ["exposed-2"], tags: []}
      - {text: "Advance [[collection-run]] one tier: the scanners have made better progress than the schedule assumed.", statuses: [], tags: []}
  - threat: "The duty clerk fills the kettle and walks the length of the bay with it, out of habit, on no schedule at all."
    consequences:
      - {text: "Somebody has to be somewhere else, now (split-up-2).", statuses: ["split-up-2"], tags: []}
      - {text: "The clipboard leaves the office in his hand, and find-the-volume resets to full until it comes back.", statuses: [], tags: []}
  - threat: "The run is not in run order. Sixty years of a records office means three renumberings and two floods."
    consequences:
      - {text: "find-the-volume resets by two tiers and the crew are now working from the spines (frustrated-2).", statuses: ["frustrated-2"], tags: []}
      - {text: "Deny Them Something They Want: whatever they planned to do next needed the volume in hand ten minutes ago.", statuses: [], tags: []}
  - threat: "The certificate on the cage is numbered, and the number is on tonight's manifest."
    consequences:
      - {text: "Breaking it is loud, permanent, and dated (a broken certificate). The theft will be discovered at the next inspection rather than the next collection.", statuses: [], tags: ["a broken certificate"]}
      - {text: "Escalate the Situation: the manifest is checked at collection, and the contractor's driver is the one who has to explain a broken seal.", statuses: [], tags: []}
  - threat: "A ladder, four metres of shelving, and a volume that weighs five kilos."
    consequences:
      - {text: "A run goes over, or a body does (wear-and-tear-2, or worse if a PC is on the ladder).", statuses: ["wear-and-tear-2"], tags: []}
      - {text: "Present a New Challenge: the scanning crew and the duty clerk arrive — Security Guard (Core p. 305) at Scale 1, unarmed, and appalled.", statuses: [], tags: []}
  - threat: "leave-no-trace maxes out."
    consequences:
      - {text: "The bay is as they found it: cage closed, certificate replaced, clipboard correct, the volume's absence explicable as a renumbering. Gain nobody knows it is gone and this Challenge is overcome for this job.", statuses: [], tags: ["nobody knows it is gone"]}
power_sets: []
reuse_of: "Structurally a Location/Barrier in the Crumbling Building and Hazard Zone pattern (Core p. 310) with navigate replaced by find-the-volume; the cage borrows the Security System's sealed-container logic (Core p. 319)."
---

# The Counterpart Stacks

**Role:** barrier · **Scale:** 2 (a leased bay and the shift working it) · **Alias:** *a warehouse full of paper* · *It does not fight. It costs time.*

The eleventh bay of a distribution warehouse in [[kilbride-stretch]], leased by the Chancery under a records-retention contract: four hundred metres of steel shelving in numbered runs, sixty years of buckram spines, a duty office with a kettle and a clipboard, a rented arc-lamp gantry, six scanners on a night shift, and a bonded cage at the end of run C. The street calls it the paper barn.

It is the physical half of the Chancery's double-sold registry ([[government]], BC-122): the **counterpart set**, separated from the Hill's copies years ago as a clerical convenience and reconciled never. [[chancery-process]] is the Hill's version of this obstacle — a barrier made of desks. This is the same institution with the desks removed: no clerks to bribe, no fee schedule, no referral, and nothing to argue with. Just a room built so that nobody ever has to find anything in it, and a clock ([[collection-run]]) that will resolve the whole problem in six days by destroying it.

Written for [[acquisition-06-the-paper-barn]] and [[acquisition-07-the-coldwater-run]]; reusable for any job that needs a records site under the Wall.

## Limits

| Limit | Tier |
|---|---|
| find the volume | 3 |
| open the cage | 4 |
| leave no trace | 5 |
| take over or shut down | – (immune; see *Paper Cannot Be Harnessed*) |

`hurt or subdue` is not listed because there is nothing here to hurt. The scanning crew, the duty clerk and the posted [[envelope-detail]] are separate profiles and separate decisions.

## Tags & statuses

four hundred metres of steel shelving · runs numbered, contents not · an arc-lamp gantry moving one run a night · a duty clipboard that is the only real index · a bonded cage with a certificate on it · *quiet-3*

## Specials

**Paper Cannot Be Harnessed:** immune to `take over or shut down`; no cyberspace action produces an unscanned page.

**The Clipboard Is The Index:** taking, copying or altering it drops `find the volume` by two tiers; a missing clipboard is noticed at shift change.

**An Hour You Did Not Budget For:** reading inside the bay advances [[collection-run]] and costs `leave no trace`.

**Certified Means Sealed:** the certificate must be physically broken; once broken, `leave no trace` cannot be maxed.

**It Burns:** fire, energy discharge or suppression destroys the run, starting with what the crew are holding.

## Threats / Consequences

› The gantry finishes a run and starts down theirs.
» Lit, eleven metres from the crew (*exposed-2*); a tier off `leave no trace`
» Advance [[collection-run]]

› The duty clerk walks the bay with the kettle, on no schedule at all.
» Somebody has to be elsewhere (*split-up-2*)
» The clipboard leaves the office; `find the volume` resets

› The run is not in run order — three renumberings and two floods.
» `find the volume` resets by two tiers (*frustrated-2*)
» Deny Them Something They Want

› The certificate is numbered and the number is on tonight's manifest.
» Breaking it is loud, permanent and dated (*a broken certificate*)
» Escalate the Situation at collection

› A ladder, four metres of shelving, five kilos of book.
» A run goes over, or a body does (*wear-and-tear-2*)
» Present a New Challenge: the scanning crew (Security Guard, Core p. 305, Scale 1, unarmed)

› `leave no trace` maxes out.
» *nobody knows it is gone* — overcome

## Power Sets

None.

## Canon and flags

- The registry is paper because paper cannot be Harnessed, and most pages exist twice: Bible §3; [[chancery-hill]]; [[government]] (BC-122); [[chancery-process]].
- **[BUILD CHOICE]** the Repository, the bay's layout, the certified cage, the clipboard-as-index, and the reading cost. Registered in [[build-choices]] "Added by WP7c".
- **[OPEN]** (OQ-21) the bay is a lease-holder's site, not a tier control; nothing here makes any of the paper caste papers (OQ-8).
