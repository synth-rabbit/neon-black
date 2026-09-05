---
type: challenge
name: "The Escapee List"
slug: escapee-list
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §3", "Bible §5", "Bible §6", "Brief §7.1", "Core p. 294–300"]
flags: [BUILD CHOICE]
player_safe: false
role: watcher
scale: 3
alias: "A Line in a Database"
short_description: "AP&I's standing, low-priority watch for the Ledger's escapees — no bounty, per canon. Progress Limit noticed tracks exposure, not pursuit; at max it hands the file to the Escapee Recovery Desk."
limits:
  - {name: noticed, tier: 5}
default_tags: ["cross-referenced intake photos", "RFID logs going back years", "quiet, not urgent"]
default_statuses: []
specials:
  - {name: "Not Worth the Bounty", text: "AP&I places no bounty on Ledger escapees (Bible §5–6; [[coldwater-outfall]]). This Challenge never Presents an active hunting party as a default Consequence — its Threats only add tiers to noticed. Only when noticed maxes out does AP&I's interest become active, and even then it is a file opened on a desk, not a manhunt — see [[escapee-recovery-desk]]."}
  - {name: "The List Doesn't Forget", text: "noticed never decreases on its own between jobs. Reducing it requires a specific downtime action — new identity papers, leaving the district that flagged the crew, a favor called in with someone who can edit a record — resolved the same way any other tag or status removal is (Effects: Weaken, Restore, or Set Back)."}
threats:
  - threat: "A face in a crowd-scan flags a partial match to Ledger intake photos."
    consequences:
      - {text: "noticed advances a tier, quietly — a flag in a database, nothing more.", statuses: [], tags: []}
  - threat: "An RFID reader somewhere logs a signature that shouldn't exist anymore."
    consequences:
      - {text: "noticed advances a tier.", statuses: [], tags: ["a name goes on the list"]}
  - threat: "An AP&I data analyst cross-references two sightings that shouldn't connect."
    consequences:
      - {text: "noticed advances two tiers.", statuses: [], tags: ["your face is in a file"]}
  - threat: "The Ledger's administration confirms an identity against its own debt records."
    consequences:
      - {text: "noticed advances two tiers.", statuses: [], tags: ["confirmed escapee"]}
  - threat: "noticed maxes out at 5."
    consequences:
      - {text: "The file is opened and priced. Present a New Challenge: [[escapee-recovery-desk]] — AP&I's pricing apparatus takes over from here (its priced Limit starts at 2); noticed resets to 3 and this Challenge keeps watching.", statuses: [], tags: ["the file is open"]}
power_sets: []
reuse_of: ""
---

# The Escapee List

**Role:** watcher · **Scale:** 3 (Megacity-wide reach; abstract, not a physical entity — the MC may treat its Scale as beyond a single encounter, as with [[secret-war-goes-public]]) · **Alias:** A Line in a Database · *AP&I's standing, low-priority watch for the Ledger's escapees.*

The setting-specific watcher Challenge Plan WP5 calls for, and the mechanical form of what [[coldwater-outfall]] and the Build Plan's WP7a aftermath both point at: the escapee list carries **no bounty** (Bible §5–6 read together with the district file's own line, "where the escapee list's 'not worth the bounty' is first tested"). This is deliberately not a pursuit Challenge — it is a slow, bureaucratic accumulation of attention that the crew can outrun, out-wait, or out-maneuver, and only becomes dangerous once it maxes out.

**Scope (WP6, BC-132).** Two watchers share the escapee list and are scoped so they do not duplicate: this profile is the **detection** layer — Megacity-wide, passive, a single `noticed` clock that the crew's ordinary life fills. [[escapee-recovery-desk]] (WP4-trio1, AP&I's signature apparatus) is the **pricing** layer: what the Contracts Office does once a file is open — the `priced` clock, the day-rate collectors, the analyst who can be bought, the file that can be buried. Play this one until `noticed` maxes; then Present the Desk. The Desk can also be opened directly by a Consequence elsewhere. Registered as CR-17.

## Limits

| Limit | Tier |
|---|---|
| noticed (progress) | 5 |

## Tags & statuses

cross-referenced intake photos, RFID logs going back years, quiet, not urgent

## Specials

**Not Worth the Bounty:** No bounty exists (Bible §5–6). This Challenge's Threats only add tiers to `noticed`; it never Presents an active hunting party by default — at max it opens the file on [[escapee-recovery-desk]].

**The List Doesn't Forget:** `noticed` never decreases on its own. Reducing it needs a specific downtime action, resolved as any tag/status removal (Weaken, Restore, or Set Back).

## Threats / Consequences

› A face in a crowd-scan flags a partial match to Ledger intake photos.
» `noticed` advances, quietly

› An RFID reader somewhere logs a signature that shouldn't exist anymore.
» `noticed` advances (*a name goes on the list*)

› An AP&I data analyst cross-references two sightings that shouldn't connect.
» `noticed` advances two tiers (*your face is in a file*)

› The Ledger's administration confirms an identity against its own debt records.
» `noticed` advances two tiers (*confirmed escapee*)

› `noticed` maxes out at 5.
» The file is opened and priced (*the file is open*) — Present a New Challenge: [[escapee-recovery-desk]]; `noticed` resets to 3

## Power Sets

None.

## Canon and flags

- Bible §5–6: the crew are Ledger escapees; [[coldwater-outfall]]: "not worth the bounty" is canon-adjacent district content this profile makes mechanical. Brief §7.1: the breakout's aftermath states the escapee-list status (WP7a).
- **[BUILD CHOICE]** the specific tier values and the "no default pursuit" Special are this package's invention of a mechanic the Bible only gestures at (no bounty); the GM may re-tier or decide what a maxed `noticed` looks like in a specific job.
