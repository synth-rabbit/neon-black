---
type: challenge
name: Almoner's Volunteer
slug: almoners-volunteer
status: review
source: custom
page: "294–300, 306, 307"
owner: WP4-trio2
canon_refs: ["Bible §2 werewolf", "Bible §3 power structure", "Bible §4 theme 3", "Brief §8", "Core p. 294–300", "Core p. 306", "Core p. 307", "Core p. 329"]
flags: [BUILD CHOICE]
player_safe: false
role: watcher
scale: 1
alias: "the aprons"
short_description: "Grey aprons on the counter and at the loading dock: polite, tireless, armed, and backed by two hundred people eating behind them."
limits:
  - {name: hurt-or-subdue, tier: 3}
  - {name: make-them-drop-the-manners, tier: 4}
  - {name: get-past-them, tier: 3}
default_tags: ["grey apron, clean hands", "knows everyone's name", "something short under the counter", "the district is standing right there"]
default_statuses: ["patient-2"]
specials:
  - {name: "Manners First", text: "A Volunteer's first Consequence in any scene must be social, hospitable, or administrative — never violent. They offer food, they ask after a relative, they explain the rules, they write a name down. They escalate only after make-them-drop-the-manners has taken at least one tier, and every tier on that Limit is public: the district watches it happen."}
  - {name: "The Room Is On Their Side", text: "Inside the Kitchen, on the Round's route, or anywhere in [[marlow-blocks]] with people present, a Volunteer can have a bystander take a status intended for them — a neighbor stepping in, a queue closing up, someone's grandmother in the way. If the crew hurts the bystander anyway, they take hated-in-Marlow-3, a compelling status cleared only by making the district whole."}
  - {name: "Everything Gets Written Down", text: "Whenever a Volunteer is threatened, deceived, or bribed, they later add a line to the ledger about it. As a Consequence in a later scene, the Almoners produce that line: a favor called in, a price raised, a door shut, or a name given to somebody who was asking (Escalate the Situation)."}
threats:
  - threat: "One of them steps out from behind the counter, wiping their hands, and asks whether the crew has eaten."
    consequences:
      - {text: "The offer is real, and taking it puts a line in the ledger.", statuses: ["obligated-2"], tags: []}
      - {text: "Refusing it in front of the queue reads badly, and the queue notices.", statuses: ["unwelcome-2"], tags: []}
  - threat: "Two of them drift, without hurrying, between the crew and the door to the loading dock."
    consequences:
      - {text: "The way through is closed by bodies and courtesy at the same time.", statuses: [], tags: ["politely blocked"]}
      - {text: "A third has gone to make a call. Present a New Challenge on the crew's next scene in this district: [[pack-on-the-run]] or a Syndicate Leg-Breaker (Core p. 307).", statuses: [], tags: []}
  - threat: "An apron comes off, gets folded, and gets set down on a table."
    consequences:
      - {text: "A short weapon from under the counter, used competently and without heat.", statuses: ["cracked-ribs-3"], tags: []}
      - {text: "They go for the hands and the knees, because the Kitchen has to open again tomorrow.", statuses: ["broken-fingers-3"], tags: []}
  - threat: "Somebody behind the counter says a PC's name, warmly, and mentions a relative."
    consequences:
      - {text: "The Kitchen knows exactly who the crew are and where their people eat.", statuses: ["exposed-3"], tags: ["they know where your people eat"]}
      - {text: "The tab is invoked in front of witnesses. Escalate the Situation.", statuses: [], tags: ["your tab was mentioned out loud"]}
power_sets: []
reuse_of: "Built beside Gang Member (Core p. 306) and Syndicate Leg-Breaker (Core p. 307); In The Know Power Set, Core p. 329."
---

# Almoner's Volunteer

**Role:** watcher · **Scale:** 1 · **Alias:** *the aprons* · *Polite, tireless, armed, and backed by two hundred people eating behind them.*

The Kitchen's volunteers are what the Chancery's second auditor wrote down as "an unusually committed staff" before joining the board ([[marlow-blocks]]). They serve, they clean, they carry crates, they run the Round's stops, they know everyone's name, and they are the [[syndicate|Almoners']] entire visible workforce. Most are from the Blocks. Many are working off a tab. A few are the reason the Almoners have never needed a gang.

They are a **watcher** rather than an attacker because that is what they mostly do — assess, remember, and report — and because the fight, when it comes, is the least dangerous thing about them. Everything a Volunteer sees goes in the ledger, and the ledger is the weapon.

## Limits

| Limit | Tier |
|---|---|
| hurt or subdue | 3 |
| make them drop the manners | 4 |
| get past them | 3 |

## Tags & statuses

grey apron, clean hands, knows everyone's name, something short under the counter, the district is standing right there · *patient-2*

## Specials

**Manners First:** Their first Consequence in a scene is social, hospitable, or administrative — food, a question about a relative, the rules, a name written down. They escalate only once *make them drop the manners* has a tier on it, and every tier is public.

**The Room Is On Their Side:** In the Kitchen, on the Round, or anywhere in [[marlow-blocks]] with people present, a bystander takes a status intended for a Volunteer. Hurting the bystander anyway gives the crew *hated-in-Marlow-3*, compelling, cleared only by making the district whole.

**Everything Gets Written Down:** Threaten, deceive, or bribe a Volunteer and it becomes a line. In a later scene the Almoners produce it — a favor called in, a price raised, a door shut, a name handed to somebody who was asking (Escalate the Situation).

## Threats / Consequences

› One of them steps out from behind the counter, wiping their hands, and asks whether the crew has eaten.
» The offer is real, and taking it puts a line in the ledger (*obligated-2*)
» Refusing in front of the queue reads badly (*unwelcome-2*)

› Two of them drift, without hurrying, between the crew and the loading dock.
» The way through is closed by bodies and courtesy at once (*politely blocked*)
» A third has gone to make a call (Present a New Challenge next scene: [[pack-on-the-run]] or Syndicate Leg-Breaker, Core p. 307)

› An apron comes off, gets folded, and gets set down on a table.
» A short weapon from under the counter, used competently and without heat (*cracked-ribs-3*)
» They go for the hands and the knees, because the Kitchen opens again tomorrow (*broken-fingers-3*)

› Somebody behind the counter says a PC's name, warmly, and mentions a relative.
» The Kitchen knows who the crew are and where their people eat (*exposed-3*)
» The tab is invoked in front of witnesses (Escalate the Situation; *your tab was mentioned out loud*)

## Power Sets

**In The Know** (Core p. 329) for a Volunteer who runs a Round stop — they hear everything the district says. **Connected & Protected** (Core p. 328) is *not* appropriate: the Almoners have no friends in high places, only debtors in low ones.

## Canon and flags

- Bible §2, §3 (a syndicate separate from the corps), §4 theme 3; Brief §8. Built beside Gang Member (Core p. 306) and Syndicate Leg-Breaker (Core p. 307).
- **[BUILD CHOICE]** (BC-109) manners-first escalation, the bystander Special, and the ledger as the real weapon.
