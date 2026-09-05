---
type: power-set
name: "Bloodware"
slug: bloodware-power-set
status: review
source: custom
page: ""
owner: WP2-vampire
canon_refs: ["Bible §2 vampire", "Bible §2 rarity", "Bible §3 Masquerade", "Brief §8", "Plan A.6", "Plan WP2", "Core p. 297–300", "Core p. 326–333"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
splat: vampire
category: Noise
applies_to: "Any Challenge representing a person who carries the Ferrante strain. Layered on top of whatever they already are — a fixer, a leg-breaker, a corporate officer, a tenant."
default_tags: ["rebuilt from the marrow out", "moves before you finish looking", "reads the iron in a room"]
default_statuses: []
limits:
  - {name: pop-the-kernel, tier: 5}
  - {name: overload, tier: 3}
specials:
  - {name: "Gets Back Up", text: "Physical Consequences do not finish this Challenge. When a status would take it out of the scene, it goes down and stays down until the scene ends, then gets up — unless its Kernel was destroyed, or it is inside an active electromagnetic field, in which case it stays where it is."}
  - {name: "Takes What It Needs", text: "As a Consequence, the Challenge opens someone up and feeds: the target takes drained-3, and the Challenge removes two tiers of statuses representing physical injury. It can do this to a person, or to enough exposed metal, more slowly and with less to show for it."}
  - {name: "The Node Is Not Where You Looked", text: "The first time anyone locates this Challenge's Kernel, they are wrong. Reset pop-the-kernel once, the first time it would max out, and describe what they cut into instead. This Special is spent after one use and is not available to a Challenge that has never had reason to move it."}
  - {name: "(Optional +) Knows the Line", text: "This Challenge recognizes any other carrier on sight and can say which line they came from. Give it a Bloodware ally, an obligation, or a grudge that arrives later (Escalate the Situation)."}
threats:
  - threat: "Cross the room faster than anyone tracks"
    consequences:
      - {text: "Take hold of someone and put them against a wall", statuses: ["grappled-3"], tags: []}
      - {text: "Break something structural in a person", statuses: ["broken-4"], tags: []}
      - {text: "Be somewhere else entirely when the shooting stops", statuses: [], tags: ["out of sight"]}
  - threat: "Look at the wound, or at the railing, or at the cuffs"
    consequences:
      - {text: "Open a person up and feed (see Takes What It Needs)", statuses: ["drained-3"], tags: []}
      - {text: "Drink the iron out of gear, a hinge, a blade or a bar", statuses: [], tags: []}
      - {text: "Strip a weapon or a restraint to grey dust (burn an equipment tag)", statuses: [], tags: []}
  - threat: "Take a wound and keep talking"
    consequences:
      - {text: "Close the wound while everyone watches (remove two tiers of physical statuses from itself)", statuses: [], tags: []}
      - {text: "Let a limb go and keep the rest", statuses: ["one-handed-2"], tags: []}
      - {text: "Stop moving entirely and read as a corpse until it is convenient not to", statuses: [], tags: ["reads as dead"]}
  - threat: "Stand very still and listen through the wall"
    consequences:
      - {text: "Know exactly how many people are in the next room and where their blood is going", statuses: ["found-out-2"], tags: []}
      - {text: "Have been waiting in the room the crew was about to enter (Escalate the Situation)", statuses: [], tags: []}
---

# Bloodware

**Applies to:** Any Challenge representing a person who carries the Ferrante strain · **Category:** Noise · **Splat:** vampire

An overlay, not a Challenge (Core p. 326–333). Put it on whatever the character already is. A Bloodware fixer is a fixer with this attached; a Bloodware leg-breaker is the Syndicate Leg-Breaker profile with this attached. The strain does not replace a person's job.

**Rarity note (Bible §2):** this overlay is not a stat block for a population. One Bloodware in a Series is a lot. A room with three in it is a clan, and a clan in the open is the sort of thing the corporations answer with a cleanup.

## Limits

| Limit | Tier | What maxing it out does |
|---|---|---|
| **pop the kernel** | 5 | The master node is destroyed. The Challenge dies and does not get up. Nothing in this overlay, and nothing in the Challenge under it, reverses this. |
| **overload** | 3 | A sustained electromagnetic field scrambles the colony. The Challenge takes `scrambled-4`, loses *Gets Back Up* and *Takes What It Needs* until the end of the scene, and mitigates nothing with Noise. |

**Every Bloodware Challenge must carry both of these Limits** (Plan A.6: NPCs of the five obey the same canon as PCs). They are the only two ways to finish one and they replace the classic vampire vulnerabilities entirely; none of those appears on any Bloodware Challenge in this vault (Bible §2). `hurt or subdue` on the Challenge underneath still works for putting one on the floor; it does not work for keeping one there (see *Gets Back Up*).

`pop the kernel` is a Limit the crew has to *earn access to*: it does not tick from ordinary attacks. It ticks when the crew learns where the node is, gets to it, and does something to it — a scan that finds it, a surgeon, a shaped charge, a field held on one spot long enough. The MC should treat locating it as the job.

## Tags & statuses

rebuilt from the marrow out, moves before you finish looking, reads the iron in a room

## Specials

**Gets Back Up:** Physical Consequences do not finish this Challenge. When a status would take it out of the scene, it goes down and stays down until the scene ends, then gets up — unless its Kernel was destroyed, or it is inside an active electromagnetic field, in which case it stays where it is.

**Takes What It Needs:** As a Consequence, the Challenge opens someone up and feeds: the target takes `drained-3`, and the Challenge removes two tiers of statuses representing physical injury. It can do this to a person, or to enough exposed metal, more slowly and with less to show for it.

**The Node Is Not Where You Looked:** The first time anyone locates this Challenge's Kernel, they are wrong. Reset `pop the kernel` once, the first time it would max out, and describe what they cut into instead. Spent after one use, and not available to a Challenge that has never had reason to move it.

**(Optional + ) Knows the Line:** This Challenge recognizes any other carrier on sight and can say which line they came from. Give it a Bloodware ally, an obligation, or a grudge that arrives later (Escalate the Situation).

## Threats / Consequences

› Cross the room faster than anyone tracks
» Take hold of someone and put them against a wall (*grappled-3*)
» Break something structural in a person (*broken-4*)
» Be somewhere else entirely when the shooting stops (create *out of sight*)

› Look at the wound, or at the railing, or at the cuffs
» Open a person up and feed (*drained-3*, and remove two tiers of its own physical statuses)
» Drink the iron out of gear, a hinge, a blade or a bar
» Strip a weapon or a restraint to grey dust (burn an equipment tag)

› Take a wound and keep talking
» Close the wound while everyone watches (remove two tiers of physical statuses from itself)
» Let a limb go and keep the rest (*one-handed-2*)
» Stop moving entirely and read as a corpse until it is convenient not to (create *reads as dead*)

› Stand very still and listen through the wall
» Know exactly how many people are in the next room and where their blood is going (*found-out-2*)
» Have been waiting in the room the crew was about to enter (Escalate the Situation)

## Canon and flags

- **[BUILD CHOICE]** (BC-36) `99-templates/template-power-set.md` has no `limits` field, but the book's own Power Sets add Limits to the Challenge they overlay (*Lucky* adds `out of luck 3`, *Spirit-Possessed* adds `exorcise 3` and `banish 3`, Core p. 330–331). This file adds a `limits` block in the `challenge` schema's shape (Plan A.4) because canon requires an NPC Bloodware to carry both. WP6 added the optional `limits:` block to the template (BC-129); a Challenge that takes this overlay carries these two Limits.
- Splat canon this overlay obeys (Plan A.6): **EM and the Kernel are the weaknesses**, present as the two mandatory Limits; the strain replicates with iron, present as *Takes What It Needs*; the body is progressively rebuilt, present in the base tags; the carrier is rare.
- **[OPEN]** (OQ-4) Nothing in this overlay transmits the strain. A Bloodware Challenge that feeds does not thereby make another Bloodware, because the vector is not settled; if the GM settles it, add a Consequence then.
- Masquerade (Bible §3): none of these Threats identifies the Challenge as anything but a very dangerous person until the crew works it out. *Gets Back Up* is the tell, and it is a late one.
- MC-facing only. What an individual Bloodware NPC knows — about clans, about cleanups, about [[upstart|Continuity Risk & Response]] — is set on that character, not here; the default for a street-level one is nothing ([[bloodware]] MC only).
