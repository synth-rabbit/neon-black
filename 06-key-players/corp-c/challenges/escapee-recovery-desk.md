---
type: challenge
name: "The Escapee Recovery Desk"
slug: escapee-recovery-desk
status: review
source: custom
page: "294–300, 305, 307, 320, 118–120"
owner: WP4-trio1
canon_refs: ["Bible §3 haves and have-nots", "Bible §5", "Bible §6 standing after the breakout", "Brief §8", "Core p. 294–300", "Core p. 305", "Core p. 307", "Core p. 320"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: watcher
scale: 3
alias: "a file nobody has any reason to open"
short_description: "AP&I's escapee-tracking apparatus: not a manhunt, a pricing desk. It does not look for the crew. It waits for them to become worth collecting."
limits:
  - {name: bury-the-file, tier: 5}
  - {name: mislead, tier: 3}
  - {name: buy-the-analyst, tier: 4}
  - {name: priced, tier: 4}
default_tags: ["one hundred and four open files", "warranty telemetry", "subcontracted collectors on a day rate", "a budget for buying rumors"]
default_statuses: ["patient-4"]
specials:
  - {name: "A Write-Off Is Not A Forgiveness", text: "This Challenge never initiates. It has no Threat that begins with the Desk deciding to act; every Threat below is triggered by something the crew did, spent, claimed, repaired, or told somebody. A crew that stays cheap is a crew the Desk has correctly priced at nothing (Bible §6: on the list, not worth a bounty)."}
  - {name: "Every Fitted Body Reports", text: "Whenever a PC or a named ally uses AP&I chrome in a way its warranty logs — a load beyond rating, a servicing visit, a diagnostic at a clinic, a replacement part bought through a licensed channel — this Challenge takes priced-1. The telemetry was disclosed in the fitting paperwork. Nobody read the fitting paperwork."}
  - {name: "Cheaper To Buy The Answer", text: "The Desk does not send people to look. As a Consequence, it may instead have offered somebody the crew knows a month's rent for a name, a face, or an address. That person has already been paid by the time the crew hear about it."}
  - {name: "Priced", text: "When priced maxes: the file moves from write-off to collectible. The crew gain worth-collecting-3 — a story-level status that does not expire and is removed only by making themselves expensive again — and the Desk spends the day rate. Present a New Challenge: Investigator (Core p. 305), corp-grade and firewalled-2, or Syndicate Leg-Breaker (Core p. 307) subcontracted where the price justifies muscle. Reset priced to 2."}
threats:
  - threat: "A clinic on Suture Row runs a routine warranty check on a PC's chrome without being asked, because the system prompted for it."
    consequences:
      - {text: "The tag answers a query it should not have been able to reach (priced-2).", statuses: ["priced-2"], tags: []}
      - {text: "The clinic's clerk is very apologetic about the flag on the account and asks the PC to wait a moment. Present a New Challenge: Security Guard (Core p. 305), Scale 1, as clinic security.", statuses: [], tags: []}
  - threat: "Somebody the crew grew up with has new shoes and cannot look at them."
    consequences:
      - {text: "A name was sold for a month's rent, and the file is warmer (priced-2 and the crew gain sold-out-2 in that district).", statuses: ["priced-2", "sold-out-2"], tags: []}
      - {text: "The buyer wants more and will pay for it. Escalate the Situation.", statuses: [], tags: []}
  - threat: "A Chancery permit, an insurance claim, or a residency pass is filed under a name that is on a list."
    consequences:
      - {text: "Paper crosses paper (priced-1) and the permit is held for review (Deny Them Something They Want).", statuses: ["priced-1"], tags: []}
      - {text: "A correlation is flagged in a comment field. Nothing happens yet. It stays flagged.", statuses: [], tags: ["flagged in a comment field"]}
  - threat: "A drone the crew have never noticed is in a district where they are working, and it is not looking at them."
    consequences:
      - {text: "Present a New Challenge: Surveillance Drone (Core p. 320), retained by the Desk on a standing contract; its surveillance report gives this Challenge priced-1.", statuses: [], tags: []}
  - threat: "A collector who has been paid a day rate for a different file walks past the crew and recognizes one of them."
    consequences:
      - {text: "The recognition is worth money to somebody and is sold within the hour (priced-3).", statuses: ["priced-3"], tags: []}
      - {text: "They decide to price it themselves first. Present a New Challenge: Syndicate Leg-Breaker (Core p. 307).", statuses: [], tags: []}
power_sets: []
reuse_of: ""
---

# The Escapee Recovery Desk

**Role:** watcher · **Scale:** 3 (an apparatus: a desk, a dataset, a budget and a list of contractors) · **Alias:** *a file nobody has any reason to open* · *It does not look for the crew. It waits for them to become worth collecting.*

The Bible is exact about the crew's standing: they are on the camp corporation's escapee list, and they **were not important enough to warrant a bounty or targeted recapture** (§6). This Challenge is that sentence made playable, and the reason it is true.

[[corp-c|AP&I]]'s recovery function is a **pricing function**, not a manhunt ([[corp-c|AP&I]]'s twist; [[rasheeda-novak]]). Every escaped account is costed — collection expense against expected return — and marked *pursue*, *monitor*, or *write off*. The crew are written off. Written off is not closed. The file sits open at zero value, costing nothing, and it re-prices itself every time the crew do something that makes them worth more than the day rate of the man who would come.

That is the horror of it and the play in it. Nobody is hunting them. They are being **quoted**.

Before anyone at the Desk has looked at the file, the crew are being watched only by the city's ordinary sensors — that passive layer is [[escapee-list]], whose `noticed` clock opens the file here when it maxes.

## Limits

| Limit | Tier |
|---|---|
| bury the file | 5 |
| mislead | 3 |
| buy the analyst | 4 |
| priced (progress) | 4 |

**bury the file** at 5 is the real objective and the hardest thing in the profile: get the names off the list, in the Contracts Office, on the thirtieth deck of [[amalgam-stack]]. **mislead** at 3 is cheap and temporary — feed the Desk a wrong price and it will believe it until the next data point.

**buy the analyst** at 4: [[rasheeda-novak]] cares about the arithmetic being right, which is not the same as being incorruptible, and is a harder thing to work with.

## Tags & statuses

one hundred and four open files, warranty telemetry, subcontracted collectors on a day rate, a budget for buying rumors · *patient-4*

## Specials

**A Write-Off Is Not A Forgiveness:** the Desk never initiates. Every Threat is triggered by something the crew did.

**Every Fitted Body Reports:** AP&I chrome used in a way the warranty logs gives *priced-1*.

**Cheaper To Buy The Answer:** as a Consequence, somebody the crew knows has already been paid.

**Priced:** at max — *worth-collecting-3* (does not expire), and the Desk spends the day rate: Present a New Challenge, Investigator (Core p. 305) or Syndicate Leg-Breaker (Core p. 307). Reset *priced* to 2.

## Threats / Consequences

› A Suture Row clinic runs an unrequested warranty check, because the system prompted for it.
» The tag answers a query it should not have reached (*priced-2*)
» The clerk apologizes about a flag and asks the PC to wait (Present a New Challenge: Security Guard, Core p. 305, Scale 1)

› Somebody the crew grew up with has new shoes and cannot look at them.
» A name was sold for a month's rent (*priced-2*, *sold-out-2* in that district)
» The buyer wants more (Escalate the Situation)

› A permit, a claim, or a residency pass is filed under a name on a list.
» Paper crosses paper (*priced-1*; Deny Them Something They Want)
» A correlation is flagged in a comment field and nothing happens (*flagged in a comment field*)

› A drone the crew never noticed is in their district, and is not looking at them.
» Present a New Challenge: Surveillance Drone (Core p. 320) on a standing contract; its report gives *priced-1*

› A collector on a day rate for a different file recognizes one of them.
» The recognition is sold within the hour (*priced-3*)
» Or priced privately first — Present a New Challenge: Syndicate Leg-Breaker (Core p. 307)

## Power Sets

None on the Desk itself. **Surveillance Data Fed** (Core p. 333) is the correct overlay for any collector working off its telemetry; **Connected & Protected** (Core p. 328) for anyone the crew try to lean on inside the Contracts Office.

## Canon and flags

- On the escapee list, not worth a bounty or targeted recapture: Bible §6 — this profile exists to keep that true under pressure rather than to overturn it. The camp and the strike: Bible §5.
- **[BUILD CHOICE]** (BC-101) recovery as pricing rather than pursuit, the *priced* progress Limit, and *worth-collecting* as the crew's own doing; (BC-103) tiers and Threats.
- **[OPEN]** (OQ-41) the flagged correlation is never read by this profile.
- **Scope (WP6, BC-132):** the vault has two escapee-list watchers, scoped apart. [[escapee-list]] (WP5) is the passive, Megacity-wide **detection** clock (`noticed`, tier 5) that ordinary life fills; when it maxes, it opens the file here. This profile is the **pricing and collection** apparatus once the file is open — `priced`, the collectors, the analyst, burying the file. Registered as CR-17.
