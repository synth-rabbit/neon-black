---
type: index
name: Existing Catalog
slug: existing-catalog
status: review
source: custom
page: ""
owner: WP5
canon_refs: ["Brief §8", "Brief §9.1(g)", "Core p. 114–117", "Core p. 252–271", "Tokyo p. 76–93"]
flags: [BUILD CHOICE, TAO-REINTERPRETED]
player_safe: false
---

# Existing Catalog

A pointer table into the Core Book's Street Catalog (p. 252–271) — Plan A.1 rule 1: existing book content and custom content, always both, never substitute. Every category below is fully usable in Palisade as printed; the custom items in this folder ([[loadout-index]]) supplement, they never replace. `Loadout` itself — Loading Up, wildcard tags, theme upgrades, Loadout Theme Specials — runs exactly as written (Core p. 114–117) and is not restated here.

## The Street Catalog's categories (Core p. 252–271)

| Category | Book pages | `catalog` value | Used in Palisade |
|---|---|---|---|
| Access & Perks | 254 | `access-perks` (`[BUILD CHOICE]`, see below) | Unchanged as a category; Palisade's own perks are corp IDs, safehouses, and favors from the Key Players below (this folder adds several: a Weighhouse line of credit, a lifted Ledger guard's fob). |
| Ammo | 255 | `ammo` | Unchanged; the book's general items (armor-piercing, hollow points, tracer rounds) all exist in Palisade. This folder adds the setting's two specialty lines: EM rounds against Bloodware and null-cast rounds against Tao-worked items. |
| Apps, Chips & Databases | 256–257 | `apps` | Unchanged; every general item and named product is available as printed — chips, HUDs, medical databases, KOCMOC skill chips. No custom additions were needed; the setting's specialty gear (Kernel-scanners, hacking suites) reads more naturally as Merc Gear or Cyberspace and is filed there instead. |
| Armor | 257–258 | `armor` | Unchanged; corpwear, tactical vests, and the named products (UrbanWar Riot Armor, Lexington camouflage suits) are all Palisade street gear as printed. No custom additions in this category. |
| Body Attachments & Cybernetics | 258–259 | `attachments` | Unchanged as a category, with the setting's one hard rule laid over it: cybernetics in this catalog are temporary loadout-tag mods, same as the book (Core p. 258); *permanent* cyberware is a caste marker (Fitted/Patched, [[names]] §4) and a hunter's replacement-only line (Bible §2), which this folder's two AP&I items make explicit. |
| Cyberspace | 260–261 | `cyberspace` | Unchanged; software, VR gear, and hacking hardware run exactly as printed, consistent with [[palisade]]'s note that cyberspace runs as written (Brief §6.5). This folder adds Cutloose-specific signal tools and Continuity's own field kit. |
| Drones | 262 | `drones` | Unchanged; the book's general items and named products (Acciaio strike drones, NM3 industrial loaders) are all available. No custom additions — [[generic-reuse-map]] covers drones as Challenges instead, which is where the setting needed them. |
| Enhancers | 263 | `enhancers` | Unchanged as a category and mechanic (consumable, addictive-by-default per Core p. 263) — and this is where Leash lives mechanically: the trigger is written as an Enhancer with the book's own addiction pattern (Threat → addicted Consequence), not a new subsystem. This folder adds four grades of Leash and Meliora's signature restorative graft. |
| Garments & Fashion | 264 | `garments` | Unchanged; the book's disguises, formalwear, and privacy hoods all exist. This folder adds camp-issue fatigues and two Cutloose concealment garments. |
| Merc Gear | 265–266 | `merc-gear` | Unchanged; the general tool items and named products (medkits, grappling hooks, scanners) are all available as printed. This folder adds the setting's scanners, restraint tools, and salvage gear. |
| **Source-Touched Items → Tao-touched** | 266–267 | `tao-touched` | **[TAO-REINTERPRETED]** — reinterpreted, not unchanged. The book's category assumes legend-Mythoi (blessed water, demonic pendants, otherworldly contracts); Palisade has none of that (Bible §1; Brief §3.1–3.2). Every item under this catalog value is custom; see the *Tao-touched* section of [[loadout-index]] and [[build-choices|BC-27 to BC-30]]. |
| Vehicles | 268 | `vehicles` | Unchanged; the book's general items and named products are all Palisade street and Wall-tier vehicles as printed. No custom additions — [[generic-reuse-map]] covers vehicle Challenges (chases, gang rides). |
| Weapons | 269–270 | `weapons` | Unchanged; firearms, cold weapons, and explosives are all available as printed. This folder adds the setting's anti-Bloodware and corp-signature weapons. |

## The Tokyo Street Catalog (Tokyo p. 76–93) — format reference only

Tokyo:Otherscape's local catalog (p. 76–93, including its own "Source-Touched Items" at p. 89) is **not** a second catalog available in Palisade — it is a different Megacity's local supplement, built for a setting with kami, yōkai, and Onmyōji practice that Palisade does not have. It is cited here only as confirmation that the Street Catalog format (general items + named specific items, one weakness tag each, Core p. 252) is the book's standard pattern across sourcebooks, and every custom item in this folder follows it.

## `[BUILD CHOICE]` — the `access-perks` catalog value

Plan A.4's `loadout-item` schema lists the `catalog` enum as `weapons | armor | ammo | apps | attachments | cyberspace | drones | enhancers | garments | merc-gear | tao-touched | vehicles` — twelve values against the book's thirteen Street Catalog categories (Core p. 252–271), omitting **Access & Perks** (Core p. 254). Several of this package's items — a Ledger guard's lifted fob, Tally's line of credit — are exactly what the book's own Access & Perks category describes (temporary access, favors, and privileges, Core p. 254) and do not sit naturally under any of the twelve listed values. This file adds `access-perks` as a thirteenth `catalog` value, matching the book's own category structure. Registered as `BC-27` in [[build-choices|BC-27 to BC-30]]; `catalog` is a vault-only organizational field (not a mapped Foundry field per [[foundry-mapping]] §3.3), so the extension carries no conversion risk.

## Canon and flags

- Plan A.1 rule 1 (existing content and custom content, always both); Core p. 252–271 (Street Catalog); Brief §9.1(g) (Loadout additions in scope).
- **[TAO-REINTERPRETED]** the Source-Touched category, renamed and reinterpreted per Brief §3.1–3.2 (CR-1).
- **[BUILD CHOICE]** (BC-27) the `access-perks` catalog value, extending Plan A.4's enum to match the book's own thirteen categories.
