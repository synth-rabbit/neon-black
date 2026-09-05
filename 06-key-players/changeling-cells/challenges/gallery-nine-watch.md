---
type: challenge
name: "The Gallery Nine Watch"
slug: gallery-nine-watch
status: review
source: custom
page: "294–300, 310"
owner: WP4-trio3
canon_refs: ["Bible §2 changeling", "Bible §3 Masquerade", "Brief §2.1", "Brief §8", "Plan A.6", "Core p. 42", "Core p. 294–300", "Core p. 310"]
flags: [BUILD CHOICE, OPEN, RULES CONFLICT]
player_safe: false
role: watcher
scale: 1
alias: "nobody, and the sound of the pumps"
short_description: "The cell's counter-surveillance on the route into Gallery Nine: a changing path, a pump schedule, and people who kill trackers on sight."
limits:
  - {name: pass-unnoticed, tier: 5}
  - {name: earn-the-hatch, tier: 4}
  - {name: hurt-or-subdue, tier: 3}
  - {name: bribe, tier: 999}
default_tags: ["a route that changes every week", "the pump schedule", "watchers who are never in the same place twice", "a submarine hatch that opens only from the inside", "nothing on the outside to knock on"]
default_statuses: ["already-watching-you-3", "ready-to-move-2"]
specials:
  - {name: "Anything That Transmits", text: "The watch's first and only test is whether the visitor is emitting: a tracker, a live lens, an open link, a corporate tag, a drone overhead. Anything transmitting is not challenged and not warned — the route simply becomes a different route, the hatch is not there, and the crew has walked two hours to a wall. A crew that has been swept clean by the Sump's people, or that arrives dark, may roll against pass-unnoticed at all."}
  - {name: "The Pumps Are The Clock", text: "Movement through the Galleries happens between pump cycles. Every scene on the route carries a countdown of the MC's choosing; when the water comes, everyone moves up, and whoever does not, drowns ([[foundation-galleries]]). The watch knows the schedule perfectly. A crew that does not is fighting the district, not the cell."}
  - {name: "Never The Same Face", text: "The watchers are Doppels. Whoever met the crew at the last junction is not the person at this one, and may be wearing the face of somebody the crew met an hour ago in the Drainage Vault. Statuses the crew inflicted on a watcher do not carry to the next watcher, and a crew that thinks it is tracking one person is tracking three."}
  - {name: "Cannot Be Bought", text: "Bribe is immune. Money is not what the route protects against — the route protects against being found, and there is no sum that makes being found survivable. An attempt to buy passage adds a tier to already-watching-you and ends the conversation."}
  - {name: "Vouched", text: "A visitor brought by a Cutloose the cell knows starts with earn-the-hatch at two tiers and is not tested for transmission until the last junction. Vouching is personal: if the visitor is wrong, the voucher is off the list, and everyone at the hatch knows what that costs."}
threats:
  - threat: "The junction the crew was told to use is dry, empty, and has a fresh chalk mark on the wall that means nothing to them."
    consequences:
      - {text: "The route has changed since the directions were given, and the directions are now worse than nothing (lost-in-the-Galleries-3).", statuses: ["lost-in-the-Galleries-3"], tags: []}
      - {text: "Somebody has already gone ahead to say who is coming (add a tier to already-watching-you).", statuses: ["already-watching-you-4"], tags: []}
  - threat: "A pump alarm sounds two levels up and the water in the tunnel starts to move against the crew's boots."
    consequences:
      - {text: "The cycle has started early because somebody started it early; the crew is in the wrong tunnel (rising-water-3).", statuses: ["rising-water-3"], tags: []}
      - {text: "The route out is now up, into a gallery the crew has never seen, which is exactly where the watch wanted them (herded)", statuses: [], tags: ["herded"]}
  - threat: "A stranger with a lamp helps them past a bad section, chats the whole way, and asks two questions too many."
    consequences:
      - {text: "The watch now knows who hired the crew, what they want, and which of them will talk (Escalate the Situation).", statuses: [], tags: []}
      - {text: "The stranger is gone at the next junction and the crew's guide from an hour ago is standing there wearing the stranger's face (unnerved-2).", statuses: ["unnerved-2"], tags: []}
  - threat: "Somebody says, from the dark, without heat: \"You are carrying something that is talking.\""
    consequences:
      - {text: "The crew is given one chance to find it themselves. If they cannot, the route ends here and the hatch was never on it (Deny Them Something They Want).", statuses: [], tags: []}
      - {text: "If it is a corporate tag and the crew knew, the watch does not warn again — it moves, and the crew is alone in a flooding tunnel with people who have nothing left to lose (Present a New Challenge: Six at the Hatch, and two watchers, Scale 1).", statuses: [], tags: []}
  - threat: "The hatch is there, closed, with no handle and no panel and no way to be heard through it."
    consequences:
      - {text: "It opens from the inside or it does not open (earn-the-hatch must be maxed; nothing else works).", statuses: [], tags: []}
      - {text: "It opens, and what is on the other side is thirty people wearing their own faces, all of them looking at the crew (Escalate the Situation).", statuses: [], tags: ["you have been inside Gallery Nine"]}
power_sets: []
reuse_of: "The Undercity as a barrier is built on Crumbling Building / Hazard Zone's navigate structure (Core p. 310); watchers use Gang Member (Core p. 306) as bodies, with Shape-Changing (Tokyo p. 137) for the faces — see reuse.md and CR-19."
---

# The Gallery Nine Watch

**Role:** watcher · **Scale:** 1 (a handful of escapees, never all in one place) · **Alias:** *nobody, and the sound of the pumps* · *The cell's counter-surveillance on the route in.*

Gallery Nine is reached "by a route that changes, through the water, past people who will kill a tracker on sight" ([[foundation-galleries]], BC-22). This is that route as a Challenge. It is not a guard post and there is nothing to breach; it is a two-hour walk through the Wall's foundation during which the crew is continuously assessed by people they mostly do not see, on one criterion — *is anything about you transmitting* — and, secondarily, on whether anyone inside is willing to be responsible for them.

The watch is not brave and does not fight if it can move instead. Every escapee on it has removed a tracker and a kill switch from their own body and knows exactly what arrives if the route is ever followed to the end. They will drown a tunnel, lose a crew in the dark, and abandon a friend at a junction before they will let that happen.

## Limits

| Limit | Tier |
|---|---|
| pass unnoticed | 5 |
| earn the hatch | 4 (progress — the crew's) |
| hurt or subdue | 3 |
| bribe | – (immune) |

## Tags & statuses

a route that changes every week · the pump schedule · watchers who are never in the same place twice · a submarine hatch that opens only from the inside · nothing on the outside to knock on · *already-watching-you-3* · *ready-to-move-2*

## Specials

**Anything That Transmits:** The one test is emission — a tracker, a live lens, an open link, a corporate tag, a drone overhead. Anything transmitting is not challenged and not warned: the route becomes a different route and the crew has walked two hours to a wall. Only a crew that arrives dark may roll against *pass unnoticed* at all.

**The Pumps Are The Clock:** Movement happens between pump cycles; every scene on the route carries a countdown. When the water comes, everyone moves up. The watch knows the schedule perfectly.

**Never The Same Face:** The watchers are Doppels. Whoever met the crew at the last junction is not the person at this one, and may be wearing a face the crew saw an hour ago. Statuses do not carry from watcher to watcher.

**Cannot Be Bought:** *Bribe* is immune. An attempt adds a tier to *already watching you* and ends the conversation.

**Vouched:** A visitor brought by a Cutloose the cell knows starts *earn the hatch* at two tiers and is not tested for transmission until the last junction. If the visitor is wrong, the voucher comes off the list.

## Threats / Consequences

› The junction they were told to use is dry, empty, and marked in chalk in a way that means nothing to them.
» The route changed after the directions were given (*lost-in-the-Galleries-3*)
» Somebody has gone ahead to say who is coming (*already-watching-you-4*)

› A pump alarm sounds two levels up and the water starts to move against their boots.
» The cycle started early because somebody started it (*rising-water-3*)
» The only way out is up, into a gallery they have never seen (*herded*)

› A stranger with a lamp helps them past a bad section and asks two questions too many.
» The watch learns who hired them and which of them talks (Escalate the Situation)
» At the next junction the stranger is gone and their earlier guide is wearing that face (*unnerved-2*)

› From the dark, without heat: "You are carrying something that is talking."
» One chance to find it themselves; otherwise the route ends and the hatch was never on it (Deny Them Something They Want)
» If it was a corporate tag and they knew — no second warning (Present a New Challenge: [[six-at-the-hatch]] and two watchers, Scale 1)

› The hatch is there, closed, with no handle, no panel, and no way to be heard through it.
» It opens from the inside or not at all (*earn the hatch* must be maxed)
» It opens, and thirty people wearing their own faces are looking at them (*you have been inside Gallery Nine*)

## Power Sets

**Shape-Changing** (Tokyo p. 137) on any watcher, for *Never The Same Face* — **[RULES CONFLICT]** (CR-19) the book files that Power Set under Mythos; in this setting a Doppel's face is Noise, body mods at the tech end of "Tao and tech at the body level" (Bible §2; Brief §2.1). See `reuse.md`. **Local to Ward** (Tokyo p. 132) re-flavoured as *knows this tunnel and the schedule*.

## Canon and flags

- Escapees removed their kill switches and trackers, live in constant danger, group with other escapees, and are purely underground (Bible §2, §3). The Galleries are ungoverned and the pump schedule is their law ([[foundation-galleries]], BC-17, BC-22).
- **[BUILD CHOICE]** (BC-123) the watch, the transmission test, and *Vouched*.
- **[RULES CONFLICT]** (CR-19) Shape-Changing as a Mythos Power Set versus the Doppel's face as Noise — options presented in `reuse.md`, not resolved.
- **[OPEN]** (OQ-15) the Galleries' cut-off Domain and its omens ([[foundation-galleries]]) are not used by this Challenge and nothing here says Tao is in them.
