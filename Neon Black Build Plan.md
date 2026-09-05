# Neon Black — Multi-Agent Build Plan

**Purpose:** a work breakdown that several agents can execute in parallel to build the Neon Black pilot campaign as an Obsidian vault rooted directly in the `neon black/` folder, laid out so it converts into a Foundry VTT module for Taragnor's **City of Mist / Mist Engine** system (`city-of-mist`, v4.5.x) running in Otherscape mode, installable on Sqyre by manifest URL.

**Inputs every agent must read first (in this order):**
1. `Shared Lore Bible.md` — fixed canon.
2. `Otherscape Campaign Skeleton Brief.md` — design decisions, standing rules, conflict register, interviewer's choices, open questions.
3. This plan — Part A (conventions and schemas) in full, then their own work package in Part B.
4. `Metro-Otherscape Core Book.pdf` and `Tokyo-Otherscape Setting Book.pdf` — extract with `pdftotext -layout` and read the pages each package cites.
5. Format reference: `https://github.com/taragnor/city-of-mist` (clone with `--depth 1`; read `src/city-of-mist/module/datamodel/*.ts`, `template.json`, and `packs/*/_source/*.json`).

**Execution order:** WP0 → WP1 → (WP2, WP3, WP4, WP5 in parallel) → WP6 → (WP7a, WP7b, WP7c in parallel) → WP8 → WP9. Dependencies are listed per package. WP0 and WP1 are serial because every later package uses their names and map.

---

## Part A — Conventions and Schemas (binding on all packages)

### A.1 Standing rules (from the Brief, §0)

1. Existing book content **and** custom content, always both — never substitute.
2. No GM advice; the MC is experienced. Content, not coaching.
3. Rules-vs-canon conflicts get flagged `[RULES CONFLICT]`, never silently resolved. Append new ones to `00-meta/conflict-register.md`.
4. Interviewer's choices from Brief §11 stand unless the GM overrules; label any *new* judgment call `[BUILD CHOICE]` and append it to `00-meta/build-choices.md`.
5. Invent only what the Brief authorizes: names, Key Player twists, Generator-derived district content, the three corps' specialty assignment (as a flagged proposal). Everything else unknown goes to `00-meta/open-questions.md`.
6. Book vocabulary only: Series, Job, Crew theme, Challenge, Limit, Threat/Consequence, MC, Megacity, district story tag, Key Player, vector, core moment, Essence, Decay, Identity/Ritual/Itch, Quick/Tracked Outcome, Mitigate, Loadout, Scale.
7. Tao is the only mystical force; no legend-Mythoi. Reinterpret every Mythos/Source/Conjuration reference as Tao (Brief §3). Mark each reinterpretation with `[TAO-REINTERPRETED]` in the file where it occurs.

### A.2 Vault layout (rooted in `neon black/`)

Existing files stay where they are. Create these folders:

```
neon black/
  00-meta/            README.md, names.md, style-guide.md, conflict-register.md,
                      build-choices.md, open-questions.md, foundry-mapping.md, changelog.md
  01-series/          series-concept.md, pillars.md, spine-and-clock.md, tone.md
  02-splats/          <splat-slug>/overview.md
                      <splat-slug>/theme-kits/*.md
                      <splat-slug>/tropes/*.md
                      <splat-slug>/pc-specials/*.md
                      <splat-slug>/power-sets/*.md
  03-self-kits/       *.md
  04-crew/            crew-kits/*.md, motivations.md, crew-specials/*.md
  05-megacity/        overview.md, timeline.md, district-directory.md, districts/*.md
  06-key-players/     <kp-slug>/overview.md, characters/*.md, challenges/*.md
  07-jobs/            00-breakout/ | 01-investigation/ | 02-acquisition/
                        each: overview.md, vectors.md, scenes/*.md, challenges/*.md, aftermath.md
  08-challenges/      generic-reuse-map.md, custom/*.md, power-sets/*.md
  09-loadout/         *.md
  99-templates/       one template file per `type` (WP0 writes these)
```

File names: kebab-case, ASCII, no spaces (`nanite-bloodline.md`). One entity per file. Every file starts with YAML frontmatter, then a level-1 heading equal to `name`.

### A.3 Cross-references

Use Obsidian wikilinks `[[file-name]]` (no path) everywhere a named entity is mentioned for the first time in a file. Every district, Key Player, character, Challenge, kit, and job must be linkable by its file name. Never link to a file that doesn't exist yet unless the plan assigns it to a package — then link anyway and note `(pending WP#)` in the register.

### A.4 Frontmatter schema by `type`

Common fields on every file:

```yaml
type: <one of the types below>
name: <display name>
slug: <file name without .md>
status: draft            # draft | review | approved
source: custom           # core | tokyo | custom   (core/tokyo = reused book content)
page: ""                 # book page(s) when source is core/tokyo
owner: WP#               # the work package that created it
canon_refs: []           # list of Bible/Brief section refs this file relies on
flags: []                # RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
```

Type-specific fields — these mirror the `city-of-mist` data model so conversion is mechanical:

**`theme-kit`** → Foundry Item `themekit`
```yaml
themebook: Augmentation          # → system.themebook_name (one of the 14 book themebooks or Crew/Loadout)
category: Noise                  # → system.subtype: Self | Noise | Mythos-OS | Crew-OS | Loadout
motivation_type: itch            # → system.motivation: identity | ritual | itch
motivation: "Feed the nanites."  # kit-fixed statement
fade_type: decay                 # → system.fade_type (always decay for Otherscape)
system_compatibility: otherscape # → system.system_compatiblity
power_tags:                      # → system.power_tagstk, exactly 10, letters A–J; A is the title tag
  - {letter: A, tagname: "...", description: "..."}
weakness_tags:                   # → system.weakness_tagstk, exactly 4, letters A–D
  - {letter: A, tagname: "...", description: "..."}
improvements:                    # → system.improvements, up to 5 (A–E); themebook Specials this kit may use;
  - {letter: A, name: "...", description: "...", effect_class: "", uses: 0}   # leave empty to inherit the themebook's five
use_themebook_improvements: true # → system.use_tb_improvements
splat: vampire                   # vault-only
```

**`character-trope`** (vault + JournalEntry) — `fixed_kits: [slug, slug, slug]`, `choice_kits: [slug, slug, slug]`, `loadout: "..."` (p. 178 format).

**`pc-special`** / **`crew-special`** → JournalEntry (no native slot; the system stores Specials as `improvement` Items on a theme, so also give `improvement: {name, description, effect_class: "", uses: 0}` for optional Item conversion) — `prerequisite: "..."`, `persists_through_theme_replacement: true`.

**`crew-kit`** → Item `themekit` with `themebook: Crew`, `category: Crew-OS`, `motivation_type: identity|ritual|itch`; power/weakness tags as above; plus `candidate_motivations: [ ... ]` (vault-only list of prebuilt statements).

**`district`** → JournalEntry — `zone_code: "11-13"`, `central_concept: "..."`, `story_tag: "..."`, `pillar: "..."`, `developments: [{order, pillar, subtheme, summary}]`, `key_players_present: [slugs]`, `caste_band: "..."`.

**`key-player`** → JournalEntry — `kp_role: corp-a|corp-b|corp-c|upstart|syndicate|government|tao-society|packs|changeling-cells`, `base_concept`, `twist` (with `twist_source: bible|invented`), `agenda`, `resources: []`, `motifs: []`, `key_characters: [slugs]`, `challenges: [slugs]`, `territory: [district slugs]`.

**`npc`** → JournalEntry (and a `challenge` file if they fight) — `affiliation: [kp slugs]`, `splat`, `role_in_pilot`, `vector: {want, push}`, `challenge: slug|null`.

**`challenge`** → Foundry Actor `threat`
```yaml
role: attacker                   # asset|attacker|barrier|countdown|mystery|pursuer|target|temptation|watcher (p. 297)
scale: 1                         # → system.collectiveSize
alias: ""                        # → system.alias (what PCs see before they know it)
short_description: ""            # → system.short_description
limits:                          # → embedded `spectrum` Items (name = limit name, maxTier = tier); "-" = immune (omit item, note in text)
  - {name: hurt-or-subdue, tier: 4}
  - {name: convince, tier: 3}
default_tags: [ "...", "..." ]   # → system.defaultTags (story tags)
default_statuses: [ "alert-2" ]  # → system.defaultStatuses
specials:                        # → embedded `gmmove` Items, subtype custom
  - {name: "...", text: "..."}
threats:                         # → embedded `gmmove` subtype soft (the Threat line) each with its Consequences
  - threat: "..."
    consequences:                # → embedded `gmmove` subtype hard, one per Consequence; statuses go in statuslist, tags in taglist
      - {text: "...", statuses: ["gunshot-wound-2"], tags: []}
power_sets: [slugs]              # applied overlays
reuse_of: ""                     # core/tokyo Challenge this adapts, with page
```

**`power-set`** → JournalEntry + the same `specials/threats` block as `challenge` (a Power Set is an overlay; p. 326–333 format).

**`job`** → JournalEntry — `job_type: [investigation]`, `sessions: 2`, `series_pole: paycheck|misfits|pivot`, `hooks: []`, `goal`, `vectors: [slugs]`, `core_moments: [slugs]`, `scenes: [slugs]`, `climax: slug`, `aftermath: slug`, `twist_for_pivot: true|false`.

**`scene`** → JournalEntry page — `job: slug`, `order: 1`, `set_piece`, `district`, `story_tags: []`, `challenges: [slugs]`, `vectors_active: [slugs]`, `core_moment: true|false`, `flashback_hooks: []`.

**`loadout-item`** → Item `tag` (subtype `loadout`) — `catalog: weapons|armor|ammo|apps|attachments|cyberspace|drones|enhancers|garments|merc-gear|tao-touched|vehicles` (p. 252–271 categories, "Source-Touched Items" renamed), `tags: []`, `flaws: []`, `requires_setup: false`.

### A.5 Theme-kit content rules (from the book, p. 177, 196–251)

- Exactly ten power tags A–J; **A is the title tag** and defines the theme. Exactly four weakness tags A–D. Tags are short descriptors (2–5 words), lower-case except proper nouns, useful in play, no numbers.
- Each power tag answers the matching themebook question letter (e.g., Augmentation A "What does your Augmentation give you or make you into?"). Cite the question in `description`.
- One motivation statement in the kit's category voice: Itch = an impulse to indulge; Ritual = a discipline, price, or condition (never legend re-enactment — Brief §3.2); Identity = a conviction to uphold.
- Nascent-kit note: a kit must still read as a theme if only tag A plus one weakness is taken (end-of-session-one crew theme, replacement themes).
- Rarity: kits must not imply the splat is common (Bible §2 rarity).

### A.6 Challenge content rules (p. 297–300, 301–333)

- One role per Challenge; at least one Limit, tier 2–6; immune = "-".
- Base tags/statuses only for what is interesting, not inventory.
- Threats are the visible tell; Consequences are what happens if unaddressed; write Consequences as concrete statuses (`name-tier`) or story tags or "Present a New Challenge".
- Reuse map: when a core/tokyo Challenge fits a generic need, record it in `08-challenges/generic-reuse-map.md` with page and any re-flavor; write a full custom file only for setting-specific entities.
- Splat NPCs must obey the same canon as PCs (vampire EM/core weaknesses; hunter replacement-only cybernetics; changeling kill switch unless escaped).

### A.7 Names

WP0 owns `00-meta/names.md`. Every later package uses names from that file verbatim. If a package needs a name that isn't there, it adds a row to `names.md` under "Added by WP#", following the style guide, and flags `[BUILD CHOICE]`.

### A.8 Definition of done (per file)

Frontmatter validates against A.4; `name` matches the H1; every `[[wikilink]]` resolves or is registered as pending; `canon_refs` populated; no invented canon outside A.1 rule 5; `status: review`.

---

## Part B — Work Packages

Each package is written to be handed to one agent as its entire brief, together with Part A.

### WP0 — Foundation: names, style, templates, registers

**Depends on:** nothing. **Blocks:** everything.

**Read:** Bible; Brief §§0, 3, 9.4, 10–12; Core Book pp. 46–61 (Key Players) and Tokyo pp. 24–27, 148–150 for naming register.

**Produce:**
- `00-meta/README.md` — vault index, how to read the vault, folder map, links to registers.
- `00-meta/style-guide.md` — naming register (corp names like *Epis International, New Michigan Motors & Machining, KOCMOC, Cryocharm, Chimaerics, Taiyō Solartech*; gang/society names like *The Gordian, Ghost Market, Tokoyo, Returned Sōma Clan*), tag voice, tone words, forbidden terms (season, case, splat in player-facing text, Mythoi/legend language).
- `00-meta/names.md` — one primary and one or two alternates, all marked *proposal*, for: the city; the five splats (each must read instantly as vampire / werewolf / mage / changeling / hunter — include a one-line "reads as" test); Corp A (trigger maker), Corp B (Tao-controlled), Corp C (camp owner); the upstart; the syndicate; the Tao society; the escaped-changeling network (what escapees call themselves); the pack culture's name for itself; the work camp; the fence; the crew leader (vampire spy); the nanite corp that no longer exists; the trigger drug's street name; the vampire master node's street name. Also assign **weapons / bio / cybernetics** to Corps A/B/C as a flagged proposal with one sentence of reasoning each.
- `99-templates/` — one template file per `type` in A.4 with every field present and commented.
- `00-meta/conflict-register.md` (seeded from Brief §10), `build-choices.md` (seeded from Brief §11), `open-questions.md` (seeded from Brief §12), `foundry-mapping.md` (copy of A.4 plus the conversion notes in Part D), `changelog.md`.

**Acceptance:** every name has a "reads as" line; templates parse as YAML; registers list Brief items verbatim with section numbers.

---

### WP1 — Series and Megacity

**Depends on:** WP0. **Blocks:** WP2–WP9.

**Read:** Bible §§1, 3, 5; Brief §§1, 6; Core Book pp. 41–45 (district tropes), 146–153, 160–173 (Generator, Berlin example).

**Produce:**
- `01-series/series-concept.md` (crew concept, series pole = Paycheck→Misfits, the pivot mechanism), `pillars.md` (Brief §1.3 table, with *Tao Weaponized* defined), `spine-and-clock.md` (the upstart spine; the public-war Countdown Challenge — write it as a `challenge` file in `08-challenges/custom/secret-war-goes-public.md` with role countdown, progress Limit tier 6, and the specific aftermath events that advance it), `tone.md`.
- `05-megacity/overview.md` — the city, sprawl, government, corporate security legality, caste system, Masquerade-as-Noise (Brief §4.1).
- `05-megacity/district-directory.md` — run the Megacity Generator on the GM's behalf: 12-row d66 directory expanded toward 18 districts; record zone codes.
- `05-megacity/districts/<slug>.md` — one per district: central concept, **district story tag**, developments (roll or choose from the Generator tables until each district has ≥1; interpret Mythoi-pillar results as Tao and mark `[TAO-REINTERPRETED]`), caste band, which Key Players hold ground there. Mandatory placements: the work camp (Corp C, remote/secret), each Big Three HQ district, the upstart's district, the fence's turf, pack turf, a Tao-society front, a changeling-escapee refuge, the caste gradient from top to bottom.
- `05-megacity/timeline.md` — future history consistent with: Tao before mods; mods ~200 years; nanite outbreak ~100 years; the nanite corp's disappearance; the Big Three's civil agreements; caste formalization; the upstart's rise; the strike on the camp as "now."

**Acceptance:** every district has a story tag and a zone code; timeline has no dates that contradict the Bible; the map places all nine Key Players; overview cites Brief §4.1 for the Masquerade model.

---

### WP2 — Splat packages (five agents may split this by splat)

**Depends on:** WP0, WP1. **Parallel with:** WP3, WP4, WP5.

**Read:** Bible §2; Brief §§2, 3, 4.2–4.3; Core Book pp. 72–75, 133–141, 174–195 (creation, tropes, custom creation incl. Specific/Broad tags p. 192), the relevant themebooks (Self 196–219, Mythos 220–235, Noise 236–251), Tokyo pp. 42–75 (Tokyo tropes, kits, Megacity Specials as the pattern).

**Produce per splat** (`02-splats/<slug>/`):
- `overview.md` — canon summary, mapping (required/optional categories), Essence minimum, persistence rule, motivation rule, "how a PC reads on the sheet" (which themebooks, which Essence they'll likely land on).
- `theme-kits/` — (a) `existing-kits.md` listing book kits to offer with page refs and any re-flavor note; (b) **≥2 custom kits** per splat in `theme-kit` format. Required customs: vampire — the nanite bloodline (Cutting Edge) and a master-node/EM-focused kit; werewolf — the sculpted beast (Augmentation) and the trigger dependency (Augmentation or Cutting Edge); changeling — the face (Augmentation) and the Tao half (Exposure), plus an *escaped* variant weakness set; mage — a Tao discipline (Esoterica) and a tech-augmented discipline (Esoterica with Occult-Blueprints-style tags) plus a Tao Companion (Companion); hunter — a Self Expertise kit, a Cutting Edge battle-suit kit, and one replacement-cybernetics Augmentation kit framed strictly as replacement.
- `tropes/` — ≥1 custom character trope per splat (three fixed kits + three choice kits + loadout line), honoring the hunter Real/Cyborg targeting (Brief §2.3).
- `pc-specials/` — ≥2 Megacity-style PC Specials per splat carrying the *persistent condition* (Brief §2.4): e.g., vampire EM vulnerability/master node; werewolf trigger dependency; changeling kill switch (owned) / hunted (escaped); mage society oath; hunter replacement prosthetic. Each has a prerequisite and survives theme replacement.
- `power-sets/` — ≥1 custom Power Set per splat for NPC use (p. 326–333 format).

**Acceptance:** A.5 rules; every kit's A tag is a title tag; Itches indulge, Rituals are disciplines; no hunter kit contains sculpting/bio-manipulation; changeling and mage kits carry `[TAO-REINTERPRETED]` where a themebook question assumes a legend.

---

### WP3 — Self kits and crew package

**Depends on:** WP0, WP1. **Parallel with:** WP2, WP4, WP5.

**Read:** Bible §§3, 6; Brief §§4.4, 5; Core Book pp. 75, 148–149, 154–157, 196–219; Tokyo p. 75.

**Produce:**
- `03-self-kits/` — custom Self kits for: each Big Three corp citizenship (Affiliation ×3), the upstart (Affiliation), the syndicate (Affiliation), a werewolf pack (Affiliation), an escaped-changeling cell (Affiliation), Tao-society initiate (Affiliation), the work camp (Troubled Past), caste-sorted (Troubled Past), "saw something I shouldn't" (Troubled Past — questions only, content left to the player), the fence's network (Assets), climb-the-ladder (Horizon), fix-the-city (Horizon), take-the-city (Horizon). Plus `existing-self-kits.md` recommending book kits with pages.
- `04-crew/crew-kits/` — `existing-crew-kits.md` (Found Family, Rebellious Street Gang, Wanted — with the Bible's caveat on Wanted) and **≥2 custom crew kits** in `crew-kit` format (one "we scrape by together," one "we take the city"), each usable as a nascent theme after session one.
- `04-crew/motivations.md` — ≥4 prebuilt Identity/Ritual/Itch statements per kit (existing and custom), each with a one-line "what acting against it looks like" so Decay is adjudicable.
- `04-crew/crew-specials/` — existing Crew Theme Specials list (p. 155) and ≥3 custom, condition-gated (Tokyo p. 75 pattern), e.g., tied to the fence, to escapee solidarity, to a district.

**Acceptance:** each crew kit has three power tags flagged as the recommended starting three; motivations list is player-facing and free of GM advice.

---

### WP4 — Key Players (nine; may split across three agents by trio)

**Depends on:** WP0, WP1. **Parallel with:** WP2, WP3, WP5.

**Read:** Bible §§2, 3, 5; Brief §§6.4, 7.3; Core Book pp. 46–61, 280–284, 294–333; Tokyo Chapter 4 (pp. 148–238) as the *format* model for a Key Player write-up with Challenges and Membership.

**Produce per Key Player** (`06-key-players/<slug>/`):
- `overview.md` in `key-player` format: base concept, **twist** (Bible-given for the upstart; invented for the rest — Corp A's twist must answer "what the trigger is really for"), agenda, resources, motifs, territory, standing toward each other Key Player (one line each — this is the stalemate map), how the upstart's destabilization creates *opportunity* for this Key Player (Bible §5).
- `characters/` — ≥2 named NPCs per Key Player in `npc` format, at least one being the **vector face** with want/push; for Corp C include the camp's authority; for the upstart include the strike lead *and* the crew leader (vampire spy) — the crew leader's file must record everything the Bible says and nothing about their motives beyond it; for the fence's network (attach to whichever Key Player WP1 placed it under, else a tenth folder `fence-network/`) include the fence.
- `challenges/` — ≥2 custom Challenge profiles per Key Player (a signature foe and a signature hazard/system/location), plus a `reuse.md` listing core/tokyo Challenges this Key Player fields, with pages.
- A `membership.md` (Tokyo pattern) — what a PC affiliated with this Key Player looks like: which Self kit (WP3), which Specials, what the Key Player expects.

**Acceptance:** nine folders; every twist marked `twist_source`; the Corp A/B/C specialty assignment matches `names.md`; no Key Player contradicts the Big Three stalemate or the upstart's "too weak to fight one alone."

---

### WP5 — Loadout and generic Challenge reuse map

**Depends on:** WP0, WP1. **Parallel with:** WP2–WP4.

**Read:** Brief §§8, 9.1(g); Core Book pp. 114–117 (Loadout), 252–271 (Street Catalog), 301–333 (Challenge Database); Tokyo pp. 76–93.

**Produce:**
- `09-loadout/` — setting catalog additions in `loadout-item` format: trigger doses and their flaws; anti-nanite/EM gear (the hunter's and corp's answer to vampires); node-scanners; kill-switch jammers and tracker shrouds for escapees; Tao-touched items (caster-shell style, renamed from "Source-Touched"); camp-issue gear the PCs escape with; corp-branded gear per Big Three specialty. Plus `existing-catalog.md` pointing at book categories with pages.
- `08-challenges/generic-reuse-map.md` — table of every generic need in the pilot (goons, security, HURT-style units, drones, ICE, hackers, gang members, syndicate muscle, executives, civilians, locations) → core/tokyo Challenge + page + re-flavor line.
- `08-challenges/custom/` — the cross-cutting custom Challenges no Key Player owns: the camp's security system; a trigger-fueled pack in frenzy (uses WP2 werewolf Power Set); an anti-Tao countermeasure; a nanite outbreak site (Tao-free — it's tech); an EM ambush; the escapee list as a *watcher* Challenge.

**Acceptance:** every loadout item has ≥1 flaw or "requires setup" where the book pattern would; reuse map covers every generic referenced by WP4 and WP7 (coordinate via `open-questions.md` if a need appears later).

---

### WP6 — Integration pass 1

**Depends on:** WP1–WP5 complete. **Blocks:** WP7.

**Produce:** no new content. Resolve wikilinks; reconcile names against `names.md`; check every kit against A.5 and every Challenge against A.6; confirm each Key Player's territory matches WP1 districts; merge duplicate NPCs; update registers; set `status: review` on passing files, `status: draft` with a `## Fix` note on failing ones. Output `00-meta/integration-1.md` listing fixes made and fixes required from owners.

---

### WP7 — Jobs (three agents in parallel)

**Depends on:** WP6.

**Read:** Bible §§5, 6; Brief §7; Core Book pp. 76–113 (scenes, Challenges, Consequences, statuses), 118–120 (Scale), 124–125 (Downtime, Cinematic Moments incl. Flashbacks), 284–293 (jobs), 334–354 (starter job as a *format* model only).

**WP7a — `07-jobs/00-breakout/`** (session one)
- `overview.md` (`job` type): in medias res inside the camp during the upstart's strike; Flashbacks establish the crew; the upstart's real objective is the crew leader; general breakout is cover; PCs know the leader but not why; ends with the fence referral and **crew theme creation** (nascent, WP3 kits and motivations offered).
- `vectors.md`: the upstart strike lead; Corp C's camp authority; the crew leader; the camp's security system (time-pressure vector). Wants and pushes per p. 290.
- `scenes/` — ≥6 scene files: cold open under the strike; the work crew's block; the extraction moment (core moment — the PCs see *who* is being taken and how gently); the escape route (set piece using WP5 camp security Challenge); the outside (first sight of the district; escapee-list watcher Challenge); the referral; **Flashback slots** distributed across scenes with prompts tied to "why we were here" (player-authored content, never pre-written).
- `challenges/` — anything not already in WP4/WP5, plus a `roster.md` pointing at reused ones.
- `aftermath.md`: escapee-list status (no bounty), what each Key Player learns, what advances the public-war Countdown (if anything), denouement questions, Credit Roll prompts specific to this session.

**WP7b — `07-jobs/01-investigation/`** (multi-session, Paycheck)
- Job type Investigation (p. 286); hired via the fence; must touch ≥2 Key Players and ≥3 districts; ≥1 hard-choice hook per splat (Itch/Ritual/Identity vs. objective); complications from the Investigation list; a clue chain with ≥2 places the case "goes deeper"; core moments; set pieces; Challenges; aftermath advancing the spine.
- **Must plant** at least one thread that the Acquisition job can pull into the Misfits pivot.

**WP7c — `07-jobs/02-acquisition/`** (multi-session, carries the pivot)
- Job type Acquisition (p. 285), heist-structured: scout, plan (Prep Sequence and Flashbacks allowed), get in, get the loot, get out; complications from the Acquisition list; **the twist that enables the Paycheck→Misfits pivot** (`twist_for_pivot: true`) — tie it to the upstart and/or Corp C per Brief §1.2; the escape as climax; aftermath that gives the crew a reason to choose a Key Player as their opposition.

**Acceptance (all three):** every scene lists its district story tag, its Challenges by slug, and which vectors are active; no scene contains GM advice; the crew leader's motives remain unrevealed beyond canon; jobs reference only names in `names.md`.

---

### WP8 — Integration pass 2 and vault index

**Depends on:** WP7.

Repeat WP6 checks over the whole vault; build `00-meta/README.md` into a full index (Maps of Content per folder); produce `00-meta/open-questions.md` final and `00-meta/conflict-register.md` final; produce `00-meta/session-zero-packet.md` — a player-facing list of files (splat overviews, existing+custom kits, tropes, crew kits, motivations) with **no MC-only content**, and confirm no MC-only file is linked from it.

---

### WP9 — Foundry conversion dry run (see Part D)

**Depends on:** WP8.

Write `tools/` scripts that read the vault and emit `city-of-mist`-compatible compendium source JSON (`themekit`, `threat` with embedded `spectrum`/`gmmove`/tag/status items, JournalEntry pages) and a `module.json`; run them; report field mismatches to `00-meta/foundry-mapping.md`; do **not** package or publish.

---

## Part C — Verification checklist (WP6, WP8, and any reviewer)

1. Canon: grep the vault for anything asserting a fact about the setting not traceable to Bible/Brief/`names.md`/`build-choices.md`. Each hit is either registered or removed.
2. Cosmology: grep for `Mythos`, `Mythoi`, `legend`, `Conjuration`, `Avatar`, `Source` — every occurrence is either a themebook/Essence/mechanical term or is marked `[TAO-REINTERPRETED]`.
3. Splat canon: vampire files mention EM + master node and *not* sun/fire/stake; hunter files contain no sculpting/bio-manipulation; changeling files distinguish owned vs escaped; werewolf files name the syndicate as trigger supplier and Corp A as manufacturer; mage files never give Tao a will.
4. Kits: 10/4 tag counts; A is a title tag; motivation type matches category; `themebook` is one of the 14 (or Crew/Loadout).
5. Challenges: role present; ≥1 Limit tier 2–6; Threats have Consequences; Scale set.
6. Vocabulary: no "season," "case," "Danger" (City of Mist term), "Rift," "Logos," "Mist" in player- or MC-facing prose.
7. Links: zero unresolved wikilinks outside the pending register.
8. Player packet: session-zero packet links only player-safe files.

---

## Part D — Foundry conversion notes (for WP0's `foundry-mapping.md` and WP9)

**Target:** system `city-of-mist` ("City of Mist / Mist Engine", v4.5.3, Foundry 13–14) in **Otherscape** mode (system setting; enable `autoEssence`). The **Mist Engine HUD** module (`mist-hud`) is compatible with that mode. Both are on the official Foundry package list, so Sqyre's picker should offer the system directly; the Neon Black content ships as a **module** installed by manifest URL.

**Data model facts (from the repo, `src/city-of-mist/module/datamodel/`):**
- Item types: `themebook`, `themekit`, `theme`, `tag`, `status`, `improvement`, `gmmove`, `spectrum`, `essence`, `move`, `clue`, `juice`, `journal`. Actor types: `character`, `threat`, `crew`.
- `themekit.system`: `themebook_name`, `themebook_id`, `subtype` (theme type key: `Self`, `Noise`, `Mythos-OS`, `Crew-OS`, `Loadout`), `power_tagstk[10]` `{letter, tagname, description}`, `weakness_tagstk[4]`, `improvements[5]` `{name, uses, description, effect_class}`, `use_tb_improvements`, `motivation` (`identity|ritual|itch`), `fade_type` (`decay`), `system_compatiblity` (note the repo's spelling), `description` (HTML), `sourceBook`.
- `themebook.system`: `power_questions{A..J: {question, subtag}}`, `weakness_questions{A..D}`, `improvements{...}` (the five Specials), `motivation`, `subtype`. The shipped Otherscape themebooks are **skeletons** whose questions read "See Otherscape Core p.NNN" (their page numbers differ from the GM's PDF). Custom kits must therefore carry full tag text; link kits to the shipped themebook by `themebook_name` so sheet logic works.
- `threat.system`: `description`, `short_description`, `gmnotes`, `alias`/`useAlias`, `collectiveSize` (Scale), `defaultTags[]`, `defaultStatuses[]`, `is_template`/`template_ids` (a Power Set can be modeled as a **template threat** whose gmmoves are inherited). Embedded Items: `spectrum` (`maxTier`) = **Limit**; `gmmove` (`subtype: soft|hard|custom|intrusion|entrance|downtime`, `taglist[]`, `statuslist[]`) = **Threat** (soft) / **Consequence** (hard) / **Special** (custom); tag/status Items for base tags and statuses.
- `tag.system`: `subtype` (`power|story|weakness|loadout|relationship`), `question_letter`, `broad`, `burned`, `activated_loadout`, etc.
- Status text convention in this system: `name-tier` (e.g., `alert-2`); the HUD and roll dialog parse that.
- Districts, Key Players, jobs, scenes, tropes, Specials → **JournalEntry** pages (HTML); Specials may additionally be emitted as `improvement` Items for drag-onto-theme use.
- Repo scripts: `npm run pack-compendium` / `unpack-compendium` show the `_source/*.json` shape to emit; the Foundry CLI (`@foundryvtt/foundryvtt-cli`) can also pack a `_source` folder into LevelDB packs.

**Module skeleton (WP9 emits, does not publish):**
```
neon-black-module/
  module.json        (id: neon-black, relationships.systems: [{id: city-of-mist}], packs: [...])
  packs/theme-kits/_source/*.json      (Item themekit)
  packs/challenges/_source/*.json      (Actor threat, with embedded items)
  packs/power-sets/_source/*.json      (Actor threat, is_template: true)
  packs/loadout/_source/*.json         (Item tag, subtype loadout)
  packs/journals/_source/*.json        (JournalEntry: districts, key players, jobs, scenes, tropes, specials)
```
Install path on Sqyre: host the built module at a stable URL (e.g., a GitHub release with `module.json` and a zip), then Sqyre → Module Manager → install by manifest URL → enable in the world.

**Open verification items for WP9:** exact `system_compatiblity` value the Otherscape module expects; whether `themebook_id` must be resolved to the shipped compendium `_id` or `themebook_name` suffices; how the HUD reads embedded `spectrum` names for Limits; whether `is_template` inheritance covers `defaultTags`. Record findings in `foundry-mapping.md`.

---

## Part F — Model assignment

Available: Claude Fable 5.1, Claude Opus, Claude Sonnet (5 / 5.1), Gemini 3.8 Flash (image generation). Recommendations weigh three things per package: how much *judgment against canon* it needs (more → Fable/Opus), how much *volume under a fixed schema* it produces (more → Sonnet is cost-effective), and whether it needs *images* (→ Gemini). Only Gemini's image capability is assumed here; its text output has not been evaluated against the Claude models for this kind of canon-bound writing, so it is not assigned any prose package.

| Package | Model | Why |
|---|---|---|
| WP0 Foundation (names, style, templates, registers) | **Fable** | Highest-leverage, lowest-volume package; naming and the style guide propagate everywhere, and the registers require reading the Bible/Brief for subtext, not just facts. |
| WP1 Series + Megacity Generator | **Fable** or **Opus** | Running the Generator on the GM's behalf and reinterpreting Mythoi results as Tao is judgment-heavy; district story tags must be play-tested phrasing. |
| WP2 Splat packages (split per splat) | **Opus** | Creative writing under strict tag-count and canon constraints; tag voice quality matters at the table. Sonnet acceptable for the hunter package (most conventional). |
| WP3 Self kits + crew package | **Sonnet 5.1** | Large volume, fixed schema, strongly patterned on book kits; escalate the crew *motivations* file to Opus if statements come back generic. |
| WP4 Key Players (nine) | **Opus** (one agent per trio) | Twists must interlock across nine organizations and respect the stalemate; Challenges need mechanical precision. The upstart and Corp C (which touch the crew leader and the camp) should go to the strongest of the three agents. |
| WP5 Loadout + generic reuse map | **Sonnet 5.1** | Catalog work with clear book patterns; the reuse map is lookup-and-table. |
| WP6 Integration pass 1 | **Fable** | Cross-file consistency, canon audit, and deciding what to fix vs. register is the most judgment-dense step after WP0. |
| WP7a Breakout (session one) | **Fable** or **Opus** | The one job that must be table-ready and must *not* leak the crew leader's motives; Flashback slot design needs restraint. |
| WP7b Investigation | **Opus** | Clue-chain construction and hard-choice hooks per splat. |
| WP7c Acquisition (pivot) | **Opus** | Heist structure plus the series-defining twist. |
| WP8 Integration pass 2 + player packet | **Fable** | Same reasoning as WP6, plus the player-safety audit. |
| WP9 Foundry conversion dry run | **Sonnet 5.1** or **Opus** | Scripting against a known data model; Sonnet if the mapping in Part D holds, Opus if field mismatches need investigation in the repo. |
| WP-I Images (new, below) | **Gemini 3.8 Flash** | Image generation. |
| Reviewer of any package | **Fable** | Verification (Part C) benefits most from the strongest reader. |

Cost lever: if budget is tight, drop WP2 and WP4 to Sonnet 5.1 *with* a Fable review pass, rather than dropping WP0/WP6/WP8 — the integration steps are where Sonnet output gets corrected.

### WP-I — Images (Gemini 3.8 Flash)

**Depends on:** WP1 (districts, motifs), WP4 (Key Player motifs, NPCs), WP2 (splat overviews). Run after WP6 so names and motifs are stable.

**Inputs a prose agent prepares first** (`00-meta/image-briefs.md`, written by WP6 as a closing task): one prompt block per image with subject, motifs from the Key Player/district file, palette/tone words from `tone.md`, the `[[wikilink]]` target, output size, and a negative list (no readable text, no real brands, no legend-Mythos iconography).

**Produce** (`assets/` folder, referenced from the target files):
- `assets/districts/<slug>.png` — one establishing image per district (12–18); 16:9.
- `assets/key-players/<slug>-emblem.png` — logo/emblem per Key Player from its motifs; square; plus one `<slug>-scene.png` establishing shot of its territory.
- `assets/npcs/<slug>.png` — **full-body "paper puppet" per named NPC** (WP4 characters, the fence, the crew leader): standing figure, head to feet, neutral or characteristic pose, **transparent background (PNG with alpha)**, portrait orientation (2:3), no ground shadow or scenery, so the figure can be placed on any scene image in Foundry. Not tokens — the GM does not use tokens for story-centric play. If the image model cannot output true transparency, generate on a flat solid chroma color (e.g., pure green `#00FF00`) and have WP9's script key it out; record which method was used in `assets/manifest.md`.
- `assets/splats/<slug>.png` — one player-facing image per splat for the session-zero packet.
- `assets/jobs/<job>/<scene-slug>.png` — one image per set-piece scene (core moments only).
- `assets/cover.png` — module cover for `module.json`.

**Acceptance:** every image is linked from exactly one vault file via `![[...]]`; file names match slugs; no image depicts content the Masquerade would make public knowledge in-world unless the target file is MC-only; a `assets/manifest.md` lists each image, its prompt, and its target.

**When to run Gemini — two passes:**
- **Pass 1, after WP6** (names, districts, Key Player motifs, and NPCs are stable): districts, Key Player emblems and territory shots, NPC portraits, splat images.
- **Pass 2, after WP8** (jobs are final): set-piece scene art for core moments, the module cover, and any NPC added by WP7.
Running earlier than WP6 risks re-generating everything after a rename; running only once after WP8 delays the player-facing splat images you may want for session zero.

**How `image-briefs.md` is structured** (WP6 writes pass-1 blocks, WP8 appends pass-2 blocks). Image models take one prompt per image, so each block is self-contained: a shared *style preamble* pasted at the top of every prompt, then the image-specific body.

Style preamble (WP6 finalizes the bracketed values from `tone.md` and `style-guide.md`):
> Cyberpunk megacity illustration, [palette words], [lighting words], [rendering style — e.g., painterly concept art, no photoreal faces], grounded and worn rather than glossy. No readable text, no logos of real companies, no watermarks, no mythological or religious iconography. [aspect ratio].

Per-image block template:
```
### <asset path>
target: [[<vault file>]]
aspect: 16:9 | 1:1
prompt: <preamble> + <subject in one or two sentences drawn from the target file's central concept / motifs / description> + <two or three concrete details from the file> + <mood word>.
negative: <anything the target file says must not be visible — e.g., "no visible fangs" for a vampire NPC whose nature is secret>
```

Example (district): *"<preamble> A vertical shanty district stacked along a flood wall, tenement balconies wired together with pirate cabling, a corporate transit line cutting overhead; rain, sodium light, market smoke at street level; resigned."*
Example (NPC paper puppet): *"<preamble> Full-body standing figure, head to feet fully in frame, facing three-quarters toward the viewer, isolated on a transparent background (or flat pure green #00FF00 if transparency is unsupported), no ground shadow, no scenery, no props touching the frame edge. A middle-aged fence in a patched synthweave coat, one cheap prosthetic eye, weight on one hip, calm and appraising."* Aspect 2:3. For NPCs with a secret nature, the negative line lists what must not show (fangs, seams, sculpt scars).
Example (emblem): *"<preamble> Flat vector emblem on a plain background, single shape, two colors, no lettering: a stylized [motif from the Key Player file]."*

---

## Part E — Agent prompt stubs (copy, fill `<WP#>`)

> You are building part of the Neon Black campaign vault. Read, in order: `Shared Lore Bible.md`, `Otherscape Campaign Skeleton Brief.md`, `Neon Black Build Plan.md` Part A in full, then Part B section **<WP#>**. Also read `00-meta/names.md` and `00-meta/style-guide.md` and use those names verbatim. Extract the cited PDF pages with `pdftotext -layout`. Produce exactly the files your package lists, in the folders and frontmatter schemas of Part A, one entity per file, with wikilinks. Do not write GM advice. Do not invent canon beyond what Part A rule 5 allows; register anything else in `00-meta/open-questions.md`. Mark `[RULES CONFLICT]`, `[BUILD CHOICE]`, `[TAO-REINTERPRETED]` where Part A requires. When finished, append a dated entry to `00-meta/changelog.md` listing every file you created or changed, and set each file's `status: review`.
