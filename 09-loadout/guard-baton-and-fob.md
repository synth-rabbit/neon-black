---
type: loadout-item
name: "Lifted Guard Baton and Fob"
slug: guard-baton-and-fob
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Bible §3", "Bible §5", "Core p. 254"]
flags: ["BUILD CHOICE"]
player_safe: true
catalog: access-perks
tags: ["guard's stun baton", "gate access fob", "still logged in, for now", "gets revoked once they notice"]
flaws: ["access is revoked once noticed"]
requires_setup: true
key_player: "corp-c"
availability: "camp-issue, stolen — taken off a Ledger guard in the breakout, or bought stolen from someone who was"
---

# Lifted Guard Baton and Fob

**Catalog:** access-perks · **Tags:** *guard's stun baton*, *gate access fob*, *still logged in, for now*, *gets revoked once they notice* · **Flaws:** *access is revoked once noticed* · **Requires setup:** yes

## Description

A telescoping stun baton and its owner's gate fob, together — the piece a Ledger guard doesn't get to keep after the shift the crew took it from them. Until AP&I's security notices the fob missing and revokes it, it opens exactly the doors that guard could open. It has to be used carefully: a fob presented at the wrong reader, or too long after the guard is reported down, is worse than no fob at all.

## Availability

camp-issue, stolen — taken off a Ledger guard in the breakout, or bought stolen from someone who was

## Canon and flags

- Bible §3: corporate security is exactly as legal as the police, and exactly as capable of losing a piece of kit to a breakout; Brief §7.1 places the breakout at the Series' open.
- **[BUILD CHOICE]** (BC-27) catalog value `access-perks` — the book's Street Catalog has an Access & Perks category (Core p. 254) that Plan A.4's `loadout-item` enum omitted; this file and BC-27 to BC-30 extend the enum to include it rather than mis-catalog items the book itself treats separately.
