---
type: challenge
name: "Tier-Lift Checkpoint"
slug: chancery-checkpoint
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §3", "Core p. 294–300", "Core p. 305"]
flags: [BUILD CHOICE]
player_safe: false
role: barrier
scale: 1
alias: "Papers, Please"
short_description: "A joint Chancery-and-corporate checkpoint at a tier lift or enclave gate — corporate security is exactly as legal as the police, and the Chancery's own corruption makes bribery the reliable way through."
limits:
  - {name: bluff-or-present-papers, tier: 3}
  - {name: bribe, tier: 2}
  - {name: force-through, tier: 4}
default_tags: ["papers checked twice", "corporate-and-government joint post", "the price list is unwritten but everyone knows it"]
default_statuses: ["alert-1"]
specials:
  - {name: "Exactly as Legal as the Police", text: "This checkpoint may be staffed by Chancery officers, a corporation's own security, or both — mechanically identical either way (Bible §3). If the crew is on ground a corporation owns, a maxed force-through or a failed bribe alerts that corporation's Security Guard (generic reuse, [[generic-reuse-map]]) instead of, or alongside, the Chancery."}
  - {name: "The Price List", text: "The bribe Limit is always available, reflecting the Chancery's own kleptocracy (Core p. 168; [[chancery-hill]]) — 'everything has a price list.' A high enough bribe, in cash, gear, or a Weighhouse-brokered favor, works even where bluffing or forcing through would not."}
threats:
  - threat: "A guard steps out and raises a hand, palm out."
    consequences:
      - {text: "The crew is stopped and asked for papers.", statuses: ["stopped-2"], tags: []}
  - threat: "A scanner beeps on a bag, a body, or a piece of gear."
    consequences:
      - {text: "The item or person is flagged for a closer look.", statuses: ["flagged-2"], tags: []}
  - threat: "Radios crackle; the post calls it in."
    consequences:
      - {text: "alert advances a tier.", statuses: ["alert-1"], tags: []}
      - {text: "If bluff-or-present-papers and bribe both fail, Present a New Challenge: Security Guard or Heavy Urban Response Tactics Officer (generic reuse, [[generic-reuse-map]]).", statuses: [], tags: []}
  - threat: "force-through maxes out."
    consequences:
      - {text: "The checkpoint is broken through bodily. The crew gains wanted-2 in this district, and a story tag broke a checkpoint follows them.", statuses: ["wanted-2"], tags: ["broke a checkpoint"]}
      - {text: "If it happened where people were watching, this may be a Threat toward public-war ([[secret-war-goes-public]]) at the MC's discretion.", statuses: [], tags: []}
  - threat: "bribe maxes out."
    consequences:
      - {text: "Waved through, no questions logged. Remove alert entirely and gain the price was paid as a story tag.", statuses: [], tags: ["the price was paid"]}
power_sets: []
reuse_of: ""
---

# Tier-Lift Checkpoint

**Role:** barrier · **Scale:** 1 (a single post) · **Alias:** Papers, Please · *A joint Chancery-and-corporate checkpoint — corporate security is exactly as legal as the police.*

The cross-cutting checkpoint Challenge for the tier lifts, enclave gates, and district borders [[palisade|Palisade]]'s geography is built from (BC-15) — no single Key Player owns it, because it is staffed by whichever authority owns the ground: the Chancery on public streets, a corporation inside its own enclave, and either or both at a tier lift between them (Bible §3). It reuses the Investigator's bribe/threaten pattern (Core p. 305) rather than inventing a new one.

## Limits

| Limit | Tier |
|---|---|
| bluff or present papers | 3 |
| bribe | 2 |
| force through | 4 |

## Tags & statuses

papers checked twice, corporate-and-government joint post, the price list is unwritten but everyone knows it · *alert-1*

## Specials

**Exactly as Legal as the Police:** Corp security and Chancery officers are mechanically identical here (Bible §3); a failure on corp-owned ground alerts that corporation's Security Guard.

**The Price List:** `bribe` is always available — the Chancery's kleptocracy (Core p. 168; [[chancery-hill]]) means a large enough bribe works even where bluffing or force would not.

## Threats / Consequences

› A guard steps out and raises a hand, palm out.
» Stopped and asked for papers (*stopped-2*)

› A scanner beeps on a bag, a body, or a piece of gear.
» Flagged for a closer look (*flagged-2*)

› Radios crackle; the post calls it in.
» `alert` advances
» If both `bluff` and `bribe` fail, Present a New Challenge ([[generic-reuse-map]])

› `force-through` maxes out.
» Broken through bodily (*wanted-2*, *broke a checkpoint*); may be a Threat toward [[secret-war-goes-public]] if witnessed

› `bribe` maxes out.
» Waved through (*the price was paid*), `alert` removed

## Power Sets

None.

## Canon and flags

- Bible §3: corporate security is exactly as legal as the city police; the Chancery is deeply corrupt. [[chancery-hill]]: "everything has a price list."
- **[BUILD CHOICE]** the specific Limit split (bluff / bribe / force) and its link to [[secret-war-goes-public]] are this package's invention; the GM may re-tier per district.
