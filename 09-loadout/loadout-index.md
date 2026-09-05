---
type: index
name: Loadout README
slug: loadout-index
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Brief §8", "Brief §9.1(g)", "Core p. 114–117", "Core p. 252–271"]
flags: [BUILD CHOICE, TAO-REINTERPRETED]
player_safe: false
---

# Loadout README

Palisade's Street Catalog additions: 30 custom `loadout-item` files plus [[existing-catalog]], a pointer table into the book's own thirteen categories. Every item here supplements the book's Street Catalog (Core p. 252–271) — it is never used instead of it (Plan A.1 rule 1). This folder is **MC-only**: a catalog item may be shown to a player one at a time during Loading Up, but the folder as a whole carries supply-chain facts (who sells the trigger, what the Ledger issues) that are not player-safe on their own ([[README|vault README]] §"Player-safe vs MC-only").

## Index by catalog

### `enhancers` — the trigger and Meliora's own line
- [[leash-clinical-dose]] — Leash, Clinical Grade
- [[leash-almoners-cut]] — Leash, Almoners' Cut
- [[leash-black-ice]] — Black Ice
- [[leash-works-brew]] — Kennel Brew
- [[meliora-restorative-graft]] — Meliora Restorative Graft

### `ammo` — anti-Bloodware and anti-Tao rounds
- [[em-pulse-cartridges]] — Deadband EM Rounds
- [[tao-null-round]] — Null-Cast Rounds

### `weapons` — anti-Bloodware tools and one corp signature
- [[degaussing-baton]] — Degaussing Baton
- [[em-riot-canister]] — Starburst EM Canister
- [[orison-directed-energy-sidearm]] — Orison "Devotional" Sidearm

### `merc-gear` — scanners, restraints, kits, and Weighhouse stock
- [[kernel-scanner-rig]] — Deadband Kernel-Scanner Rig
- [[degaussing-collar]] — Degaussing Collar
- [[null-field-emitter]] — Null-Field Emitter
- [[switch-removal-kit]] — Sump Switch-Removal Kit
- [[reclamation-worksheds-toolkit]] — Reclamation Shed Toolkit
- [[weighhouse-salvage-crate]] — Weighhouse Salvage Crate
- [[weighhouse-pawned-piece]] — Hocked Piece

### `cyberspace` — Cutloose signal tools and Continuity's kit
- [[kill-switch-jammer]] — Sump-Cut Signal Jammer
- [[kill-switch-decoy-transponder]] — Ghost Ping Transponder
- [[continuity-response-kit]] — Continuity Crisis-Response Kit

### `garments` — concealment and camp issue
- [[tracker-shroud-cloak]] — Tracker Shroud
- [[ledger-issue-fatigues]] — Reconciliation Facility Fatigues

### `attachments` — AP&I's two grades
- [[api-replacement-limb]] — AP&I Replacement-Grade Limb (a Baseline may take this)
- [[api-enhancement-splice]] — AP&I Enhancement-Grade Splice (a Baseline may **not**)

### `tao-touched` — `[TAO-REINTERPRETED]`
- [[caster-shell-rounds]] — Caster-Shell Rounds
- [[focus-lattice]] — Focus Lattice
- [[sinks-scrap-shard]] — Sinks Scrap Shard

### `access-perks` — `[BUILD CHOICE]` BC-27, see [[existing-catalog]]
- [[guard-baton-and-fob]] — Lifted Guard Baton and Fob
- [[weighhouse-line-of-credit]] — Weighhouse Line of Credit
- [[weighhouse-runner-favor]] — Runner's Favor

## Index by theme (Plan WP5's seven lines)

| Line | Items |
|---|---|
| **Leash** (the trigger, multiple grades) | [[leash-clinical-dose]], [[leash-almoners-cut]], [[leash-black-ice]], [[leash-works-brew]] |
| **Anti-Bloodware gear** (EM + Kernel-scanners) | [[em-pulse-cartridges]], [[degaussing-baton]], [[kernel-scanner-rig]], [[degaussing-collar]], [[em-riot-canister]] |
| **Cutloose gear** (kill-switch jammers, tracker shrouds, removal kits) | [[kill-switch-jammer]], [[tracker-shroud-cloak]], [[switch-removal-kit]], [[kill-switch-decoy-transponder]] |
| **Tao-touched items** (caster-shell ammo/foci, Sinks scrap, anti-Tao countermeasures) | [[caster-shell-rounds]], [[focus-lattice]], [[sinks-scrap-shard]], [[tao-null-round]], [[null-field-emitter]] |
| **Ledger-issue gear** (what escapees walk out wearing) | [[ledger-issue-fatigues]], [[reclamation-worksheds-toolkit]], [[guard-baton-and-fob]] |
| **Corp-branded gear** (one signature item per Key Player) | [[meliora-restorative-graft]] (Meliora), [[orison-directed-energy-sidearm]] (Orison), [[api-replacement-limb]] + [[api-enhancement-splice]] (AP&I), [[continuity-response-kit]] (Continuity) |
| **Weighhouse stock** (what Tally fronts on credit) | [[weighhouse-line-of-credit]], [[weighhouse-salvage-crate]], [[weighhouse-runner-favor]], [[weighhouse-pawned-piece]] |

30 items total. Every item carries at least one flaw or `requires_setup: true` (Plan WP5 acceptance) — several carry both.

## Every file in this folder

One row per file (this index excepted); *P* marks a `player_safe: true` file that may be handed to a player whole. Descriptions are drawn from each file's frontmatter.

### `09-loadout/`

| File | Type | P | One line |
|---|---|---|---|
| [[api-enhancement-splice]] | loadout-item | — | attachments — *AP&I enhancement splice*, *grants capability beyond baseline human*, *visibly Fitted*; flaws draws attention |
| [[api-replacement-limb]] | loadout-item | — | attachments — *AP&I replacement limb*, *restores a lost function*, *warranty-monitored*; flaws monitored by the company |
| [[caster-shell-rounds]] | loadout-item | — | tao-touched — *caster-shell rounds*, *Tao worked into the casing*, *fires once, warm for a week*; flaws single use |
| [[continuity-response-kit]] | loadout-item | — | cyberspace — *Continuity response kit*, *field hacking suite*, *priority comms uplink*; flaws monitored by the company |
| [[degaussing-baton]] | loadout-item | — | weapons — *degaussing baton*, *close-range EM discharge*, *corp cleanup issue*; flaws short range |
| [[degaussing-collar]] | loadout-item | — | merc-gear — *degaussing collar*, *restrains via EM field*, *locks around the throat*; flaws battery drains quickly |
| [[em-pulse-cartridges]] | loadout-item | — | ammo — *EM pulse rounds*, *disrupt nanite lattice*, *localized pulse*; flaws weak against Baselines |
| [[em-riot-canister]] | loadout-item | — | weapons — *EM starburst canister*, *area pulse*, *thrown, not fired*; flaws indiscriminate |
| [[existing-catalog]] | index | — | A pointer table into the Core Book's Street Catalog (p. 252–271) — Plan A.1 rule 1: existing book content and custom content, always both, never substitute. |
| [[focus-lattice]] | loadout-item | — | tao-touched — *focus lattice*, *channels a Caster's Tao*, *must be attuned to one user*; flaws requires setup |
| [[guard-baton-and-fob]] | loadout-item | ✓ | access-perks — *guard's stun baton*, *gate access fob*, *still logged in, for now*; flaws access is revoked once noticed |
| [[kernel-scanner-rig]] | loadout-item | — | merc-gear — *Kernel-scanner rig*, *locate the master node*, *cross-references nanite density*; flaws requires setup |
| [[kill-switch-decoy-transponder]] | loadout-item | — | cyberspace — *decoy transponder*, *spoofs the tracker's last position*, *buys a false trail*; flaws single use |
| [[kill-switch-jammer]] | loadout-item | — | cyberspace — *kill-switch jammer*, *blocks the activation signal*, *narrow band*; flaws battery drains quickly |
| [[leash-almoners-cut]] | loadout-item | — | enhancers — *Leash, Almoners' cut*, *cut with fillers*, *pack-standard supply*; flaws withdrawal symptoms |
| [[leash-black-ice]] | loadout-item | — | enhancers — *Black Ice, uncut Leash*, *no filler*, *hits like a wall*; flaws incriminating |
| [[leash-clinical-dose]] | loadout-item | — | enhancers — *Leash, clinical grade*, *measured dose*, *Meliora batch stamp*; flaws source-traceable |
| [[leash-works-brew]] | loadout-item | — | enhancers — *Kennel brew*, *home-cooked*, *you don't know the dose*; flaws unpredictable dose |
| [[ledger-issue-fatigues]] | loadout-item | ✓ | garments — *camp fatigues*, *RFID-chipped*, *marks you as Ledger property*; flaws incriminating |
| [[meliora-restorative-graft]] | loadout-item | — | enhancers — *Meliora restorative graft*, *closes wounds fast*, *grown-tissue injector*; flaws addictive |
| [[null-field-emitter]] | loadout-item | — | merc-gear — *null-field emitter*, *suppresses Tao in a radius*, *corp anti-Tao issue*; flaws heavy |
| [[orison-directed-energy-sidearm]] | loadout-item | — | weapons — *Orison directed-energy sidearm*, *silent discharge*, *corporate-Latin nameplate*; flaws requires recharging |
| [[reclamation-worksheds-toolkit]] | loadout-item | ✓ | merc-gear — *work-shed toolkit*, *pry bar, cutters, torch*, *doubles as improvised weapons*; flaws cumbersome |
| [[sinks-scrap-shard]] | loadout-item | — | tao-touched — *Tao-dense scrap*, *salvaged from the Sinks*, *hums faintly*; flaws unstable |
| [[switch-removal-kit]] | loadout-item | — | merc-gear — *switch-removal kit*, *surgical*, *cuts the kill switch out clean*; flaws dangerous to use |
| [[tao-null-round]] | loadout-item | — | ammo — *null-cast rounds*, *disrupts Tao-worked items*, *corp anti-Tao issue*; flaws weak against mundane targets |
| [[tracker-shroud-cloak]] | loadout-item | — | garments — *tracker shroud*, *woven signal cage*, *blocks passive tracking*; flaws conspicuous |
| [[weighhouse-line-of-credit]] | loadout-item | ✓ | access-perks — *Weighhouse line of credit*, *Tally will front it*, *she takes a cut until it's clear*; flaws recurring fees |
| [[weighhouse-pawned-piece]] | loadout-item | ✓ | merc-gear — *a hocked piece*, *bought back cheap*, *someone else's story attached*; flaws can be reclaimed |
| [[weighhouse-runner-favor]] | loadout-item | ✓ | access-perks — *a runner's favor*, *one of Tally's people owes you*, *opens a door once*; flaws recurring fees |
| [[weighhouse-salvage-crate]] | loadout-item | ✓ | merc-gear — *salvage crate*, *grab-bag of Gullet finds*, *one of everything, none of it new*; flaws poor quality |

## Canon and flags

- Splat canon obeyed throughout: Bloodware weaknesses are EM and the master node, never sun/fire/stake (Bible §2, [[em-pulse-cartridges]] etc.); Baselines take cybernetics only as replacements, never enhancement (Bible §2, [[api-replacement-limb]] vs. [[api-enhancement-splice]]); changelings are owned unless Cutloose (Bible §2, the Cutloose-gear line); Howlers depend on Leash made by Meliora and sold by the Almoners (Bible §2, the Leash line); Tao is never given a will ([[style-guide]] §6, the Tao-touched line).
- **[TAO-REINTERPRETED]** every `tao-touched` item, per [[existing-catalog]].
- **[BUILD CHOICE]** (BC-27) the `access-perks` catalog value.
