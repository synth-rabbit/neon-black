---
type: challenge
name: "The Ledger's Line Security"
slug: ledger-line-security
status: review
source: custom
page: "294–300, 305, 310, 319, 118–120"
owner: WP4-trio1
canon_refs: ["Bible §3 corporate security legality", "Bible §5 the camp", "Bible §6", "Brief §7.1", "Brief §8", "Core p. 294–300", "Core p. 305", "Core p. 310", "Core p. 319"]
flags: [BUILD CHOICE, OPEN]
player_safe: false
role: barrier
scale: 2
alias: "the shift"
short_description: "Not a wall — a routine. The count, the quota, the wire, the floodlights and the arrears column, working together to make leaving cost more than staying."
limits:
  - {name: breach, tier: 4}
  - {name: slip-the-count, tier: 3}
  - {name: bribe, tier: 5}
default_tags: ["wire, floodlight, and no cover for three kilometers", "the count is read twice a shift", "guards exactly as legal as the police", "lagoons on three sides"]
default_statuses: ["watched-2"]
specials:
  - {name: "The Count", text: "Any scene that begins or ends inside the fence begins or ends with the count read over the yard speakers. If any PC is somewhere they are not rostered when a count is read, this Challenge takes lockdown-1 and that PC takes accounted-for-2 — a compelling status that goes away when they are back where the roster says they are."}
  - {name: "Debt Is The Lock", text: "In place of a physical status, any Consequence from this Challenge may instead be delivered as arrears-2 against a PC's Standing Account: months added to what they owe. arrears cannot be mitigated by anything physical and does not heal; it is removed only by paying, by a forged reconciliation, or by leaving Palisade's accounting behind entirely."}
  - {name: "The Ledger Is Never Wrong", text: "Arguing a number with a guard, a clerk, or the officer adds arrears-1 to the arguer whether or not the argument is correct. The count is not a record of the camp; the camp is an enforcement of the count."}
  - {name: "No Bounty Beyond The Wire", text: "This Challenge cannot pursue past the far end of the causeway. Once anyone is off the fill-rise and into the sludge-flats, line security hands off — Present a New Challenge: the Escapee Recovery Desk, or nothing at all, because a body in the Outfall at night is cheaper written off than followed (Bible §6)."}
  - {name: "Lockdown", text: "The lockdown progress Limit is a single clock kept on the camp's electronic profile, [[ledger-security-system]] (tier 6); every lockdown-1 this routine adds is added there. When it maxes: floodlights to full, blocks sealed, the causeway gate down, and every guard on the fence line. Present a New Challenge: Security Guard (Core p. 305) at Scale 2 and Gun Turret (Core p. 319) on the gate; reset lockdown to 2 and it can max again."}
threats:
  - threat: "A tower light stops sweeping and stays where it is."
    consequences:
      - {text: "Whoever is in it is lit, and everyone on the fence line knows exactly where (exposed-3).", statuses: ["exposed-3"], tags: []}
      - {text: "The light stays on that spot for the rest of the scene, and nothing crosses it (Deny Them Something They Want).", statuses: [], tags: ["that ground is lit"]}
  - threat: "A guard walks a shed row counting heads, gets a number he does not like, and starts again from the beginning."
    consequences:
      - {text: "A second count is called out of sequence (this Challenge takes lockdown-1).", statuses: [], tags: []}
      - {text: "The nearest body is pulled off the line to explain the discrepancy (separated-3, and Present a New Challenge: Security Guard, Core p. 305).", statuses: ["separated-3"], tags: []}
  - threat: "The shed klaxon sounds early and the quota board is still short."
    consequences:
      - {text: "The shift is extended and the shortfall is priced against everyone on the line (arrears-2 to the whole crew).", statuses: ["arrears-2"], tags: []}
      - {text: "Machinery is run past its safe rate to make the number (Present a New Challenge: Hazard Zone, Core p. 310, confined to the shed floor).", statuses: [], tags: []}
  - threat: "The causeway gate comes down and a truck is held on the far side of it with its engine running."
    consequences:
      - {text: "The only dry route off the fill-rise is closed (Deny Them Something They Want; add lockdown-1).", statuses: ["lockdown-1"], tags: []}
      - {text: "Whoever was on the causeway when it dropped is in the open, on three kilometers of raised road with no cover (pinned-in-the-open-3).", statuses: ["pinned-in-the-open-3"], tags: []}
  - threat: "An officer's voice comes over the yard speakers and reads a name that is not a block number."
    consequences:
      - {text: "That person's account is read aloud to the entire camp (shamed-2 and arrears-2).", statuses: ["shamed-2", "arrears-2"], tags: []}
      - {text: "They are wanted in the administration block before the next count. Present a New Challenge: Věra Solano.", statuses: [], tags: []}
power_sets: []
reuse_of: ""
---

# The Ledger's Line Security

**Role:** barrier · **Scale:** 2 (a shift: the guards on the fence and the sheds, plus the routine they enforce) · **Alias:** *the shift* · *Not a wall — a routine.*

The Ledger's security is unimpressive to look at, and that is the design. Reconciliation Facility 4 sits on a fill-rise at the center of the [[coldwater-outfall|Coldwater Outfall]], with settling lagoons on three sides and three kilometers of floodlit causeway on the fourth (BC-24). It does not need a wall. It needs a **count**, a **quota**, and an **arrears column**, and it has all three: the count twice a shift, the quota on the board, and the arithmetic that makes every act of resistance a longer sentence ([[corp-c|AP&I]]'s twist).

The guards are AP&I corporate security, exactly as legal as the police (Bible §3), and out here they are the only law there is. They are bored, adequately paid, and entirely unafraid of the population, because the population has been taught that the way out is the column, and the column is never wrong.

This is the Challenge the breakout runs through (WP7a). The strike does not defeat it — [[continuity-crisis-response-cell]] cuts the power and opens the doors, and *then* this profile is what stands between a hundred people and the causeway.

## Limits

| Limit | Tier |
|---|---|
| breach | 4 |
| slip the count | 3 |
| bribe | 5 |
| lockdown (progress) | — tracked on [[ledger-security-system]] (tier 6); see *Lockdown* below |

**bribe** at 5: a guard who takes money is a guard whose own account gets a note in it. It is possible and it is expensive.

## Tags & statuses

wire, floodlight, and no cover for three kilometers, the count is read twice a shift, guards exactly as legal as the police, lagoons on three sides · *watched-2*

## Specials

**The Count:** scenes inside the fence open or close on the count; anyone off-roster when it is read gives this Challenge *lockdown-1* and takes *accounted-for-2* (compelling).

**Debt Is The Lock:** any Consequence may be delivered as *arrears-2* instead of a physical status. *arrears* does not heal and cannot be physically mitigated.

**The Ledger Is Never Wrong:** arguing a number adds *arrears-1*, correct or not.

**No Bounty Beyond The Wire:** cannot pursue past the causeway; hands off to [[escapee-recovery-desk]] or to nothing (Bible §6).

**Lockdown:** one clock, kept on [[ledger-security-system]] (tier 6) — every *lockdown-1* here is added there. At max — floodlights full, blocks sealed, causeway gate down; Present a New Challenge: Security Guard (Core p. 305) Scale 2 and Gun Turret (Core p. 319) on the gate; reset *lockdown* to 2.

## Threats / Consequences

› A tower light stops sweeping and stays where it is.
» Lit, and every guard knows where (*exposed-3*)
» That ground is closed for the scene (Deny Them Something They Want; *that ground is lit*)

› A guard counting a shed row gets a number he does not like and starts again.
» A second count out of sequence (*lockdown-1*)
» The nearest body pulled off the line to explain it (*separated-3*; Present a New Challenge: Security Guard, Core p. 305)

› The klaxon sounds early and the quota board is still short.
» Shift extended, shortfall priced against everyone (*arrears-2* to the crew)
» Machinery run past its safe rate (Present a New Challenge: Hazard Zone, Core p. 310, on the shed floor)

› The causeway gate drops with a truck held on the far side, engine running.
» The dry route is closed (Deny Them Something They Want; *lockdown-1*)
» Whoever was on the causeway is in the open (*pinned-in-the-open-3*)

› An officer's voice reads a name over the yard speakers instead of a block number.
» The account is read aloud to the camp (*shamed-2*, *arrears-2*)
» Wanted in the administration block before the next count — Present a New Challenge: [[vera-solano-challenge]]

## Power Sets

None. Guards escalate with **Heavily Armed** (Core p. 328) only after *lockdown* has maxed once.

## Canon and flags

- The camp is debt labor and penal, secret, remote, AP&I's, produces something generic and is not the mystery: Bible §5. Escapee list without bounty: Bible §6. Corporate security's legality: Bible §3. The camp's cover, layout, and causeway: BC-24, [[coldwater-outfall]].
- **[BUILD CHOICE]** (BC-101) *Debt Is The Lock* and *The Ledger Is Never Wrong* express AP&I's twist mechanically; (BC-103) tiers, Specials and Threats.
- **[OPEN]** (OQ-38) nothing here names what the sheds produce; the quota board has a number on it and no product on it.
- **Scope (WP6, BC-131):** this profile is the *routine* — count, quota, arrears, wire, causeway, guards. The camp's *electronic* system — cameras, RFID readers, gate control — is [[ledger-security-system]] (WP5). The two run side by side in the breakout; the `lockdown` progress Limit is kept once, on the system profile (tier 6), and both feed it. Registered as CR-17.
