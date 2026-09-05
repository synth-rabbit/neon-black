---
type: challenge
name: "Reconciliation Facility 4 — Security System"
slug: ledger-security-system
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §3", "Bible §5", "Brief §7.1", "Core p. 294–300", "Core p. 319"]
flags: [BUILD CHOICE]
player_safe: false
role: barrier
scale: 2
alias: "The Fence Line"
short_description: "The Ledger's cameras, RFID-gated blocks, and floodlit perimeter — the obstacle between the crew and the causeway. Progress Limit toward lockdown."
limits:
  - {name: alarm, tier: 3}
  - {name: override-or-shutdown, tier: 4}
  - {name: lockdown, tier: 6}
default_tags: ["RFID-gated blocks", "camera coverage overlapping by design", "floodlit perimeter", "truck gate on the causeway"]
default_statuses: ["alert-1"]
specials:
  - {name: "RFID Fatigues", text: "Every inmate's issued fatigues carry a chip that logs the wearer at every gate reader in range (see [[ledger-issue-fatigues]]). Anyone wearing uncut camp fatigues who passes a reader is automatically detected — no roll required — unless the chip has been removed, jammed, or shrouded first."}
  - {name: "Overlapping Coverage", text: "This Challenge's camera and sensor coverage overlaps by design (Core p. 319): defeating or blinding one node does not blind the system. Reducing alarm or lockdown by a meaningful amount requires addressing more than one node, narratively or mechanically."}
threats:
  - threat: "A reader chimes on a signature it doesn't recognize, or recognizes too well."
    consequences:
      - {text: "The system logs it and starts counting.", statuses: ["alarm-1"], tags: []}
      - {text: "A patrol is dispatched to the reader's location.", statuses: [], tags: []}
  - threat: "Floodlights snap on over a work block, catching everyone in the open."
    consequences:
      - {text: "Anyone in the light is exposed to the towers.", statuses: ["exposed-2"], tags: []}
      - {text: "alarm ticks up.", statuses: ["alarm-1"], tags: []}
  - threat: "alarm maxes out and the gate klaxon sounds."
    consequences:
      - {text: "Present a New Challenge: Security Guard or Heavy Urban Response Tactics Officer (generic reuse, [[generic-reuse-map]]) as AP&I's on-site response arrives at the alarm's source.", statuses: [], tags: []}
      - {text: "alarm resets to 0 once the responding Challenge is dealt with or the source is no longer flagged.", statuses: [], tags: []}
  - threat: "The gate line goes hot and every reader starts logging every signature it sees."
    consequences:
      - {text: "lockdown advances one tier.", statuses: ["lockdown-1"], tags: ["gates sealed"]}
      - {text: "The truck gate and landing stage close; the causeway becomes the only way out, and it is watched.", statuses: [], tags: []}
  - threat: "lockdown reaches 6."
    consequences:
      - {text: "Full lockdown: every gate sealed, every tower manned, guard Challenges reused from the generic map arrive at Scale +1, and the causeway is lit end to end. This is the breakout's worst outcome, not its only one — the crew's exit route becomes whatever gap the job's scenes have opened (WP7a).", statuses: ["lockdown-6"], tags: ["the Ledger is sealed"]}
power_sets: []
reuse_of: ""
---

# Reconciliation Facility 4 — Security System

**Role:** barrier · **Scale:** 2 (the fenced compound, several blocks) · **Alias:** The Fence Line · *The camp's cameras, RFID-gated work blocks, and floodlit perimeter — the obstacle between the crew and the causeway.*

The custom Challenge behind [[coldwater-outfall|the Ledger]]'s security, as promised by [[district-directory]] and the mandatory placement in [[coldwater-outfall]]. It is written to serve as the breakout job's time-pressure vector (Plan Part B, WP7a: "the camp's security system (time-pressure vector)") without pre-writing any scene — the progress Limit `lockdown` is the clock; WP7a decides how fast the scenes move it. Before the breakout, the same profile covers the Ledger's ordinary electronic security (readers, cameras, gate control).

**Scope (WP6, BC-131).** This is the camp's *system*: cameras, RFID readers, gate control, floodlight automation. The camp's *routine* — the count, the quota, the arrears column, the guards on the wire and the causeway — is [[ledger-line-security]] (WP4-trio1, AP&I's signature barrier). Run both in the breakout: the routine hands out *arrears* and pulls bodies off the line; the system logs and locks. The `lockdown` progress Limit below is the **single** lockdown clock for the camp — [[ledger-line-security]]'s *The Count* and its Threats add their *lockdown-1* here rather than to a second track. Registered as CR-17.

## Limits

| Limit | Tier |
|---|---|
| alarm (progress) | 3 |
| override or shutdown | 4 |
| lockdown (progress) | 6 |

`alarm` is the local, per-incident Limit — a patrol responding to one reader. `lockdown` is the whole-camp progress Limit: the watcher function the task brief calls for, expressed as a Limit rather than a second role (Plan A.6: one role per Challenge). Maxing `alarm` repeatedly, or scoring a Consequence that says so directly, is what advances `lockdown`.

## Tags & statuses

RFID-gated blocks, camera coverage overlapping by design, floodlit perimeter, truck gate on the causeway · *alert-1*

## Specials

**RFID Fatigues:** Every inmate's issued fatigues carry a chip that logs the wearer at every gate reader in range ([[ledger-issue-fatigues]]). Wearing uncut fatigues past a reader is automatic detection — no roll — unless the chip is removed, jammed, or shrouded first.

**Overlapping Coverage:** Coverage overlaps by design (Core p. 319); blinding one node does not blind the system. Meaningfully reducing `alarm` or `lockdown` needs more than one node addressed.

## Threats / Consequences

› A reader chimes on a signature it doesn't recognize, or recognizes too well.
» The system logs it and starts counting (*alarm-1*)
» A patrol is dispatched to the reader's location

› Floodlights snap on over a work block, catching everyone in the open.
» Anyone in the light is exposed to the towers (*exposed-2*)
» `alarm` ticks up (*alarm-1*)

› `alarm` maxes out and the gate klaxon sounds.
» Present a New Challenge: Security Guard or Heavy Urban Response Tactics Officer ([[generic-reuse-map]]) responds to the source
» `alarm` resets to 0 once dealt with

› The gate line goes hot and every reader starts logging every signature it sees.
» `lockdown` advances (*lockdown-1*, *gates sealed*)
» The truck gate and landing stage close; the causeway becomes the only way out, and it is watched

› `lockdown` reaches 6.
» Full lockdown (*lockdown-6*, *the Ledger is sealed*): every gate sealed, every tower manned, guard Challenges reused at Scale +1, the causeway lit end to end — the breakout's worst outcome, not its only one.

## Power Sets

None.

## Canon and flags

- Bible §3, §5: AP&I owns the camp; corporate security is exactly as legal as the police. Brief §7.1: the breakout is the Series' opening job and the camp's security is its named time-pressure vector.
- **[BUILD CHOICE]** the specific Limits, tags, and notch structure are this package's specification of the security system Plan WP1/WP7a require; WP7a may re-tier `lockdown`'s pacing to fit its scene count.
- No GM advice: every Consequence here is a concrete status, story tag, or "Present a New Challenge" (Plan A.6), never a pacing instruction.
