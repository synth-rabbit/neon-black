---
type: challenge
name: Pack on the Run
slug: pack-on-the-run
status: review
source: custom
page: "294–300, 306"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §2 rarity", "Bible §3 the Masquerade", "Bible §4 theme 3", "Brief §2.5 werewolf", "Brief §8", "Core p. 294–300", "Core p. 297", "Core p. 306", "Core p. 329"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: pursuer
scale: 1
alias: "a gang, apparently"
short_description: "Four to six of the Run, dosed, across open ground at night: a pursuer that does not tire, does not spread out, and stops when the dose does."
limits:
  - {name: hurt-or-subdue, tier: 4}
  - {name: outrun-them, tier: 5}
  - {name: convince-them-youre-not-worth-it, tier: 3}
default_tags: ["knows every yard of this ground", "hunts as a unit, not a mob", "the district looked away an hour ago"]
default_statuses: ["settled-3", "on-the-scent-2"]
specials:
  - {name: "They Are Counting", text: "The pack's settled status (from [[running-shape]]) is a clock they can read and the crew cannot. They will not follow a target past the point where the shape would come apart somewhere they cannot get home from. When settled reaches 1, the pack breaks off, whatever it was chasing — and everyone in the Yards knows this, which is why the flats are safe at dawn and only at dawn."}
  - {name: "One Voice", text: "A pack hunts as a unit: they cut angles, drive a target toward the ground they want, and do not chase individually. As a Consequence they may reduce outrun-them by two tiers by anticipating rather than running faster. If the pack's leader is removed from the scene, the unit loses this Special and takes disorganized-3."}
  - {name: "Not Worth It", text: "Convince-them-you're-not-worth-it is tier 3 and is the intended way out of most scenes: the Run does not kill for sport, and a target who is clearly more trouble than the errand is a target a pack leaves. Maxing it ends the pursuit for the scene, not for the Series — the pack remembers, and so does the person who sent them."}
  - {name: "It Was A Gang Fight", text: "Whatever happens here, the account that reaches Palisade by morning is a Patched gang and a stimulant (Bible §3). Cleanup handles the rest ([[running-shape]], Cleanup Comes At First Light). A crew that documents the truth well enough to break that account is doing something to [[secret-war-goes-public]], not to the Run."}
threats:
  - threat: "Something crosses the cinder two hundred metres out, and then does not appear where it should have appeared."
    consequences:
      - {text: "The crew's line of retreat is already occupied.", statuses: [], tags: ["they are between you and the way out"]}
      - {text: "The pack gains ground without being seen to move.", statuses: ["on-the-scent-2"], tags: []}
  - threat: "One of them puts a hand flat on a shutter, a fence, or a vehicle door and leans."
    consequences:
      - {text: "Cover the crew was relying on stops being cover (burn a tag representing cover or a barrier).", statuses: [], tags: []}
      - {text: "Whoever was behind it takes the shutter with them.", statuses: ["slammed-3"], tags: []}
  - threat: "They stop pushing and start herding — spreading a little, moving a lot, driving the crew somewhere."
    consequences:
      - {text: "The crew is driven onto the flats, into the levee road, or up against the Kiln Row. Present a New Challenge: [[kiln-row]].", statuses: [], tags: ["driven onto their ground"]}
      - {text: "The route out costs something. Deny Them Something They Want.", statuses: [], tags: []}
  - threat: "One of them speaks — a name, a number, a message from somebody else."
    consequences:
      - {text: "The errand is stated out loud: a tab, a price, a person, a warning from [[first-alms]] or from an alpha.", statuses: [], tags: ["you know who sent them"]}
      - {text: "The pack takes what it came for and goes.", statuses: [], tags: ["they got what they came for"]}
power_sets: [running-shape]
reuse_of: "Built beside Gang Member (Core p. 306) at Scale 1, with the Run's overlay; In The Know (Core p. 329) for a pack on its own ground."
---

# Pack on the Run

**Role:** pursuer · **Scale:** 1 · **Alias:** *a gang, apparently* · *Four to six of the Run, dosed, across open ground at night.*

The signature Challenge of [[packs|the Run]]: a pack that has taken the delivery and is out. Use it on the cinder flats of [[cinder-yards]], in the courtyards of [[marlow-blocks]], across the levees into [[lowmere-sinks]], and anywhere a debt has gone unpaid long enough for [[syndicate|the Almoners]] to stop writing letters.

It is a **pursuer** (Core p. 297) rather than an attacker because that is what a pack is for. They come after you, they are better at the ground than you are, they do not tire on the dose, and the way out of the scene is almost never *win the fight*. The mechanically important fact — and the one the crew has to learn the expensive way — is that the pack is running a clock and knows exactly how much of it is left.

To the rest of Palisade, this Challenge is a street gang. Nobody who survives it is believed.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 4 |
| outrun them | 5 |
| convince them you're not worth it | 3 |

## Tags & statuses

knows every yard of this ground, hunts as a unit not a mob, the district looked away an hour ago · *settled-3*, *on-the-scent-2*

## Specials

**They Are Counting:** *Settled* (from [[running-shape]]) is a clock the pack reads and the crew cannot. At *settled-1* they break off, whatever they were chasing. This is why the flats are safe at dawn and only at dawn.

**One Voice:** They cut angles and drive rather than chase. As a Consequence they may reduce *outrun them* by two tiers by anticipating. Remove the pack's leader and they lose this Special and take *disorganized-3*.

**Not Worth It:** Tier 3, and the intended exit. The Run does not kill for sport. Maxing it ends the pursuit for the scene, not the Series.

**It Was A Gang Fight:** By morning the account is a Patched gang and a stimulant (Bible §3). Breaking that account is an action against [[secret-war-goes-public]], not against the Run.

## Threats / Consequences

› Something crosses the cinder two hundred metres out, and then does not appear where it should have appeared.
» The crew's line of retreat is already occupied (*they are between you and the way out*)
» The pack gains ground without being seen to move (*on-the-scent-2*)

› One of them puts a hand flat on a shutter, a fence, or a vehicle door and leans.
» Cover stops being cover (burn a cover or barrier tag)
» Whoever was behind it takes the shutter with them (*slammed-3*)

› They stop pushing and start herding.
» The crew is driven onto their ground (Present a New Challenge: [[kiln-row]]; *driven onto their ground*)
» The route out costs something (Deny Them Something They Want)

› One of them speaks — a name, a number, a message from somebody else.
» The errand is stated out loud (*you know who sent them*; see [[first-alms]])
» The pack takes what it came for and goes (*they got what they came for*)

## Power Sets

[[running-shape]] — always, when the pack is dosed. A pack that is *not* dosed is a Gang Member collective (Core p. 306) with worse tempers and better anchors, and should be run as exactly that.

## Canon and flags

- Bible §2 (packs function like gangs; the dose; rarity), §3 (the Masquerade; incidents blamed on Baselines), §4 theme 3; Brief §2.5, §8. Built beside Gang Member (Core p. 306).
- **[BUILD CHOICE]** (BC-114) the clock the pack can read, *One Voice*, and *Not Worth It* at tier 3 as the designed exit.
- Splat canon (Plan A.6): dependency on the syndicate's supply is in the profile, not in the fiction around it; no Tao (**[OPEN]** OQ-5).
