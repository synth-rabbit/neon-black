---
type: power-set
name: Corp-Bonded Extraction Team
slug: corp-bonded-extraction-team
status: review
source: custom
page: ""
owner: WP2-hunter
canon_refs: ["Bible §2 hunter", "Bible §3 corporate security", "Brief §2.5 Hunter", "Core p. 326–333"]
flags: []
player_safe: false
splat: hunter
category: Self
applies_to: "Any Challenge representing a corp-bonded team of Baseline contractors or security operatives sent after the crew, a witness, or an extreme case — the NPC-side mirror of a Bonded Tracker or Corporate Muscle PC."
default_tags: ["corp-issued armor", "chain of command", "legal to shoot you"]
default_statuses: []
specials:
  - {name: "Contract Cover", text: "When a PC attacks or exposes this Challenge, they first take legal-liability-2 — retaliation against a bonded, legally-armed team has consequences a corp's lawyers are happy to pursue."}
  - {name: "Call It In", text: "At the end of downtime or as a Consequence, this Challenge can request reinforcements or Present a New Challenge — a second team, or the corp's cleanup crew."}
threats:
  - threat: "Move as a drilled unit, covering each other's angles."
    consequences:
      - {text: "Pin down a target with coordinated fire.", statuses: ["pinned-down-3"], tags: []}
  - threat: "Radio a position back to the corp."
    consequences:
      - {text: "The corp responds — surveillance drones, a media blackout, or a second team arrives.", statuses: [], tags: ["Escalate the Situation"]}
  - threat: "Remind everyone present who's paying for this."
    consequences:
      - {text: "Threaten with legal and contractual consequences.", statuses: ["threatened-2"], tags: []}
---

# Corp-Bonded Extraction Team

**Applies to:** Any Challenge representing a corp-bonded team of Baseline contractors or security operatives · **Category:** Self · **Splat:** hunter

They're not corp employees exactly, and they're not freelancers exactly — a bonded team, contracted, insured, and exactly as legal as a Chancery patrol on the ground they're standing on (`05-megacity/palisade.md`, "The city government and the law"). No chrome beyond what a Baseline is allowed. Just drills, discipline, and a paycheck.

## Tags & statuses

corp-issued armor, chain of command, legal to shoot you

## Specials

**Contract Cover:** When a PC attacks or exposes this Challenge, they first take *legal-liability-2* — retaliation against a bonded, legally-armed team has consequences a corp's lawyers are happy to pursue.

**Call It In:** At the end of downtime or as a Consequence, this Challenge can request reinforcements or Present a New Challenge — a second team, or the corp's cleanup crew.

## Threats / Consequences

› Move as a drilled unit, covering each other's angles.
» Pin down a target with coordinated fire (*pinned-down-3*).

› Radio a position back to the corp.
» The corp responds (Escalate the Situation: surveillance drones, a media blackout, or a second team).

› Remind everyone present who's paying for this.
» Threaten with legal and contractual consequences (*threatened-2*).

## Canon and flags

- Corporate security is exactly as legal as the Chancery's own police (Bible §3); this overlay's Contract Cover Special is that fact made mechanical.
- No Noise or Mythos content: this is an entirely Self-category overlay, consistent with hunter canon (Bible §2) and the book's own Self Power Set pattern (Heavily Armed, Corporate Sponsored, Troop-leading — Core p. 328–329).
- MC-only, per `02-splats/hunter/power-sets/` (README "Player-safe vs MC-only").
