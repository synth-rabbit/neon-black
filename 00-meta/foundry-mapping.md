---
type: meta
name: Foundry Mapping
slug: foundry-mapping
status: review
source: custom
page: ""
owner: WP0
canon_refs: ["Brief §9.2", "Brief §9.3", "Brief §12", "Plan A.4", "Plan Part D", "Plan WP9"]
flags: [OPEN]
player_safe: false
---

# Foundry Mapping

The single reference for converting this vault into a Foundry VTT module. It restates Plan A.4 (frontmatter schemas) and Plan Part D (conversion notes) and **cross-checks both against the system's actual data model** in `ref/city-of-mist/` (`datamodel/item-types.ts`, `actor-types.ts`, `default-themekit.ts`, `motivation-types.ts`, `fade-types.ts`, `theme-types.ts`, `tag-types.ts`, `spectrum-values.ts`, `move-types.ts`, `otherscape.ts`, `template.json`, `system.json`, and the four sample-pack JSON files). Where the Plan and the code disagree, the **Code says** column states what the code requires and the row is marked **DIFFERS**. Rows the excerpts cannot settle are marked **UNVERIFIED** and collected in §8 for WP9.

Nothing in this file changes any vault schema: packages write the frontmatter of Plan A.4 as restated in §2–§4 (and as instantiated in `99-templates/`); WP9's scripts do the translation.

## 1. Target

| Item | Value | Source |
|---|---|---|
| System | `city-of-mist` — "City of Mist / Mist Engine", **v4.5.3**, Foundry **13–14** (`compatibility.minimum: 13`, `verified: 14`, `maximum: 14`). | `system.json` |
| Mode | Otherscape: the system's `OtherscapeSystem` module (`get name() { return "otherscape" }`); switching to it sets the settings `baseSystem`, `system`, `movesInclude`, `visualStyle` to `"otherscape"`. Enable the client setting **`autoEssence`** (default `true`). | `otherscape.ts` |
| HUD | Mist Engine HUD module (`mist-hud`) — compatible with Otherscape mode per Brief §9.3; not in the excerpts. | Brief §9.3 — **UNVERIFIED** against 4.5.3 |
| Delivery | A **module** (`module.json` + compendium packs) hosted at a stable URL, installed on Sqyre by manifest URL (§7). | Plan Part D; Brief §9.3 |
| Shipped packs the module must reference, not duplicate | `themebook` ("CoM Data", Item, `packs/themebooks`), `sampleDangers` (Actor), `macro`, `journal` (documentation). The 14 Otherscape themebooks live in the `themebook` pack as **skeletons** whose questions read "See Otherscape Core p.NNN". | `system.json`; sample `Augmentation_K3rvh4bMi0L6S4lS.json` |
| Vault-only types | `type: meta` (registers, README) and any file with `template: true` are never converted (BC-10); `series`, `splat-overview`, `index`, `membership` convert to JournalEntry pages (BC-127, §2). | [[build-choices]] |

Item types in the system (`template.json`, `ITEMMODELS`): `themebook, tag, improvement, theme, juice, status, clue, move, gmmove, spectrum, journal, themekit, essence`. Actor types: `threat, character, crew`. Note that the system's Item type **`journal`** is a question/answer Item (`{question, answer}`), **not** a Foundry JournalEntry; every "→ JournalEntry" below means the core `JournalEntry` document with text pages, which has no system fields (**DIFFERS** from the Plan's wording, not from its intent).

Theme type keys in Otherscape mode (`OtherscapeSystem.themeTypes()`): **`Loadout`, `Noise`, `Self`, `Mythos-OS`, `Mythos`, `Crew-OS`**. The code keeps both `Mythos-OS` and a legacy `Mythos` ("rewriting mythos is necessary due to a bug with older versions"). See §3.1 row `category` for the consequence.

## 2. Common frontmatter (every vault file; Plan A.4)

```yaml
type: <theme-kit | character-trope | pc-special | crew-special | crew-kit | district | key-player | npc | challenge | power-set | job | scene | loadout-item | meta | series | splat-overview | index | membership>   # closed set, BC-127
name: <display name>          # → document `name` (Item / Actor / JournalEntry)
slug: <file name without .md> # → used as the stable basis for the 16-character `_id` (see §6) and for cross-file links
status: draft | review | approved   # vault-only; WP9 converts only `review` or `approved`
source: core | tokyo | custom       # → themekit/themebook `system.sourceBook`: "OtherscapeCore" when source is core, "" otherwise (the `SourceBooks` type has only that key)
page: ""                            # vault-only; cited in the description HTML for reused content
owner: WP#                          # vault-only
canon_refs: []                      # vault-only
flags: []                           # vault-only: RULES CONFLICT | BUILD CHOICE | TAO-REINTERPRETED | OPEN
player_safe: false                  # vault-only (BC-128): drives WP8's session-zero packet; WP9 may map it to JournalEntry page ownership (true → observer-visible)
```

**Vault-only types (BC-127).** `meta` is never converted. `series`, `splat-overview`, `index`, and `membership` convert as JournalEntry pages (§5): `series` under one "Series" entry; `splat-overview` as the first page of each splat's entry; `index` files as pages of the folder they index (a `*-reuse` index under its Key Player's entry, `book-kits-index` under the theme-kits journal); `membership` as a page of its Key Player's entry. A `character-trope`'s `book:<slug>` kit reference (BC-126) is rendered as text with the page from `02-splats/book-kits-index.md`; nothing is emitted for it.

Every system Item also carries the `defaultItem()` fields `description` (HTML), `locked` (false), `version` (`"1"` — the datamodel constant; the samples show older `"2.6.7"`), and — for themekit/themebook/improvement/move/essence — the `systemItem()` fields `free_content` (false), `locale_name` (""), `systemName` (""), `sourceBook` (""). Emit them explicitly.

## 3. Item-backed types

### 3.1 `theme-kit` → Item `themekit` (also `crew-kit`, §3.2)

| Vault field | Foundry path | Code says (`item-types.ts` Themekit, `default-themekit.ts`, `otherscape.ts`) | Verdict |
|---|---|---|---|
| `themebook` | `system.themebook_name` | `txt`. Free text; sheet logic links the kit to the shipped themebook by this name and/or `themebook_id`. Use the shipped names exactly: `Affiliation, Assets, Expertise, Horizon, Personality, Troubled Past, Artifact, Companion, Esoterica, Exposure, Augmentation, Cutting Edge, Cyberspace, Drones`, and `Crew (Otherscape)` for the crew themebook (sample name). | verified name field; **UNVERIFIED** whether name alone resolves (§8-2) |
| — | `system.themebook_id` | `DocumentIdField` (16 chars). Known shipped ids from the samples: **Augmentation `K3rvh4bMi0L6S4lS`**, **Crew (Otherscape) `ayN2BXLJ2IgQyfh8`**. WP9 extracts the other 13 from `packs/themebooks`. | **UNVERIFIED** (§8-2) |
| `category` | `system.subtype` | `txt<ThemeType>`, initial `"Logos"` (must be overwritten). Valid Otherscape keys: `Self`, `Noise`, `Mythos-OS`, `Crew-OS`, `Loadout`, plus legacy `Mythos`. **`determineEssenceFromThemes()` compares theme types against the string `"Mythos"`, not `"Mythos-OS"`** (`case "Mythos": return;` and `!themeTypes.includes("Mythos")`). A PC whose Mythos kits carry `Mythos-OS` would be auto-Essenced as **Cyborg** (Self + unrecognized) instead of Spiritualist / Nexus. The shipped Otherscape Mythos themebooks' actual subtype is not in the excerpts. | **DIFFERS / UNVERIFIED** — the vault keeps writing `Mythos-OS` per Plan A.4; WP9 must match whatever the shipped Artifact/Companion/Esoterica/Exposure themebooks use and report the autoEssence behavior (§8-5) |
| `motivation_type` | `system.motivation` | `txt<Motivation>`, initial `"mystery"`; valid keys `identity, mystery, directive, ritual, itch, motivation` (`MOTIVATIONLIST`). Use `identity | ritual | itch`. | verified |
| `motivation` | `system.description` (HTML, the card text) | No dedicated field for the statement; the shipped themebooks leave `description` empty. Emit the kit card (tags, statement, questions answered) as HTML in `description`. | verified (no field) |
| `fade_type` | `system.fade_type` | `txt<FadeType>`, initial `"default"`; valid `fade, crack, strike, decay, default` (`FADETYPELIST`). Plan says always `decay`. **The shipped Augmentation themebook (`system_compatiblity: "otherscape"`) carries `fade_type: "fade"`.** The Decay label on the card comes from `themeTypes()[type].decreaseLocalization = "Otherscape.terms.decay"` regardless of this field. | **DIFFERS** — emit `decay` as the Plan says; WP9 confirms which of kit/themebook `fade_type` the sheet reads and whether it matters (§8-6) |
| `system_compatibility` | `system.system_compatiblity` (repo spelling) | `txt<System \| "any">`, initial `"any"`. The Otherscape system name is `"otherscape"` (`OtherscapeSystem.name`); the shipped Otherscape themebooks use `"otherscape"`. | **verified value: `"otherscape"`** (runtime picker check remains §8-1) |
| `power_tags[]` | `system.power_tagstk[]` | `arr(obj<ThemekitTagData>)`, default ten entries `{tagname: "", letter: "A".."J", description: ""}`. Exactly ten; letter `A` is the title tag. | verified |
| `weakness_tags[]` | `system.weakness_tagstk[]` | Same shape, default four entries `A`–`D`. | verified |
| `improvements[]` | `system.improvements[]` | `arr(obj<ThemekitImprovementData>)`, default five entries `{name: "", uses: 0, description: "", effect_class: ""}`. **No `letter` key** — the Plan's `letter: A..E` is vault-only; emit in array order. `uses` is a number (0 = unlimited by convention of the samples' `null`). | **DIFFERS** (drop `letter` on emit) |
| `use_themebook_improvements` | `system.use_tb_improvements` | `bool`, initial `false`. Set `true` when `improvements` are left blank to inherit the themebook's five Specials. | verified |
| `splat` | — | vault-only. | — |
| `source` / `page` | `system.sourceBook`; description HTML | see §2. | verified |

Essence names the code knows (`EssenceNames`): `Singularity, Conduit, Avatar, Cyborg, Nexus, Real, Transhuman, Spiritualist` — the book's eight. `autoEssence` derives only Singularity (all Noise), Real (all Self), Cyborg (Self+Noise), Spiritualist (Self+Mythos), Transhuman (Mythos+Noise), Nexus (all three); a pure-Mythos PC returns `undefined` and **Avatar vs Conduit is set by hand** — relevant to pure-Tao mages (Brief §3.3, CR-8).

### 3.2 `crew-kit` → Item `themekit`

As 3.1 with `themebook: "Crew (Otherscape)"` (shipped name), `category: Crew-OS`, and `motivation_type: identity | ritual | itch`. **Code says:** the shipped crew themebook's `system.motivation` is `"motivation"` (the Legend key) and its `subtype` is `"Crew-OS"`; the Crew-OS theme type's `identityName` is `"Otherscape.terms.crewIdentity"`, so the card label is set by the theme type, not by the kit's `motivation` key. **UNVERIFIED** how the card renders a crew kit whose `motivation` is `ritual` or `itch` (§8-10). `candidate_motivations[]` is vault-only (goes into the description HTML).

### 3.3 `loadout-item` → Item `tag` with `subtype: loadout`

| Vault field | Foundry path | Code says (`TagDM`) | Verdict |
|---|---|---|---|
| `name` | `name` | — | verified |
| `catalog` | description HTML / folder | No system field. `system.category` exists (`choices: TAG_CATEGORY_LIST`, initial `"none"`) but the list is not in the excerpts. | **UNVERIFIED** (§8-9) |
| `tags[]` | one `tag` Item per entry | `subtype: "loadout"` (`TAGTYPES`: `power, story, weakness, loadout, relationship`); `crispy`, `hidden`, `burned`, `burn_state`, `broad`, `temporary`, `permanent`, `custom_tag`, `activated_loadout` (bool, initial false), `question`, `question_letter`, `is_bonus`, `theme_id`, `parentId`, `subtagRequired`, `showcased`, `example0..2`, `counterexample0..2`, `restriction0..2`, `sceneId`, `createdBy[]`. | verified shape; **UNVERIFIED** whether loose loadout `tag` Items in a compendium can be dragged onto a PC's Loadout theme (§8-9) |
| `flaws[]` | description HTML (and optionally `tag` Items with `subtype: weakness`) | No flaw field on a tag. | verified (no field) |
| `requires_setup` | description HTML | No field. | verified (no field) |

### 3.4 `pc-special` / `crew-special` → JournalEntry page, optionally Item `improvement`

| Vault field | Foundry path | Code says (`Improvement`) | Verdict |
|---|---|---|---|
| `improvement.name/description/effect_class/uses` | `name`, `system.description`, `system.effect_class`, `system.uses {current, max, expended}` | `Improvement` has `...expendable()` → `uses: {current, max, expended}` (an object, **not** a number as Plan A.4's `uses: 0` implies), `theme_id`, `choice_item`, `chosen`, `effect_class`, `system_compatiblity`. | **DIFFERS** — emit `uses: {current: n, max: n, expended: false}` |
| `prerequisite`, `persists_through_theme_replacement` | description HTML | No fields. | verified (no field) |

## 4. Actor-backed types

### 4.1 `challenge` → Actor `threat` with embedded Items

| Vault field | Foundry path | Code says (`ThreatSchema`, embedded `Spectrum`, `GMMove`, `EmbeddedTagDM`, `EmbeddedStatusDM`) | Verdict |
|---|---|---|---|
| `name` | `name` | — | verified |
| `role` | description HTML | No field. (`system.logos` / `system.mythos` exist from `person()`; the Zeus sample uses them as descriptor lines; leave them empty.) | verified (no field) |
| `scale` | `system.collectiveSize` | `num`, initial 0. **The samples carry the legacy key `collective_size`** (string `"0"`); the current schema is `collectiveSize`. | **DIFFERS from samples, matches Plan** — emit `collectiveSize` (number) |
| `alias` | `system.alias` + `system.useAlias` | `alias` initial `"?????"`, `useAlias` initial `true`. An empty vault `alias` should emit `useAlias: false`. | verified; add `useAlias` |
| `short_description` | `system.short_description` | `txt`. | verified |
| — | `system.description`, `system.biography`, `system.gmnotes` | HTML. Emit the profile text into `description`; MC-only notes into `gmnotes`. | verified |
| `limits[]` | embedded `spectrum` Items | `Spectrum.system.maxTier` (`num`, min 1, max 999, initial 1). Item `name` = the Limit's name. **Immune ("-") is `maxTier: 999`** (`SPECTRUM_VALUES[999] = "-"`), so the Plan's "omit the item" is unnecessary — emit the spectrum with 999. The samples use the legacy `max_tier` string, which `migrateData()` converts. | **DIFFERS from Plan (immune) and from samples (key)** — emit `{maxTier: n}` |
| `default_tags[]` | `system.defaultTags[]` | `arr(EmbeddedDataField(EmbeddedTagDM))`: each entry is an object `{type: "tag", name, description: "", locked: false, version: "1", subtype: "story", crispy: false, hidden: false}` — **not a string**. | **DIFFERS** — converter expands strings to objects |
| `default_statuses[]` | `system.defaultStatuses[]` | `arr(EmbeddedDataField(EmbeddedStatusDM))`: `{type: "status", name, description: "", locked: false, version: "1", tier, pips: 0, hidden: false}`. The vault's `alert-2` splits into `name: "alert", tier: 2`. | **DIFFERS** — converter parses `name-tier` |
| `specials[]` | embedded `gmmove` Items, `subtype: "custom"` | `GMMove.system`: `subtype` (`soft, hard, custom, intrusion, entrance, downtime`, lowercase — `migrateData` fixes `"Soft"`), `taglist[]` (strings), `statuslist[]` (strings), `hideName` (bool), `header` (`default, none, symbols, text`), `superMoveId` (id), `description` (HTML). | verified |
| `threats[].threat` | embedded `gmmove`, `subtype: "soft"` | The Threat line. | verified |
| `threats[].consequences[]` | embedded `gmmove`, `subtype: "hard"`, one per Consequence | **In the samples, statuses and tags live in the description text as markup** — `[fried-5]`, `[s:thunderstorm]`, `[a: lightning-reflexes-2]` — with `taglist`/`statuslist` left empty. The Plan puts them in `statuslist`/`taglist`. Emit **both**: the markup in `description` and the lists. `superMoveId` can point a hard move at its soft parent. | **DIFFERS from samples** — dual emit; WP9 confirms what the HUD applies (§8-7) |
| `power_sets[]` | `system.template_ids[]` | `arr(id)`. The Zeus sample lists its template's `_id` (`LD0GRLAPl7sCF9eW`). Templates therefore need fixed ids (§6). | verified; inheritance scope **UNVERIFIED** (§8-4) |
| `reuse_of` | description HTML | No field. | verified (no field) |
| — | `system.is_template` | `bool`, initial false. | verified |

Status text convention throughout: `name-tier` (`alert-2`).

### 4.2 `power-set` → Actor `threat` with `is_template: true`

Same as 4.1 with `system.is_template: true`, `template_ids: []`, spectra only when the overlay's optional `limits:` block is filled (the book's *Lucky* and *Spirit-Possessed* add Limits, Core p. 330–331; BC-129 — whether a template's spectra inherit is part of §8-4), Specials as `custom` gmmoves, Threats/Consequences as `soft`/`hard` gmmoves. The `God of Olympus (Template)` sample is the shape. Whether `defaultTags`/`defaultStatuses` inherit through `template_ids` is **UNVERIFIED** (§8-4); until then, each Challenge repeats its base tags itself.

## 5. JournalEntry-backed types

`character-trope`, `pc-special`, `crew-special`, `district`, `key-player`, `npc`, `job`, `scene`, plus the vault-only prose of `power-set` and `challenge`. These become core `JournalEntry` documents (one per file, or one per folder with a page per file — WP9 chooses) with pages of `type: "text"` and `text: {content: <HTML>, format: 1}`. **No system data model applies**; all type-specific frontmatter (`zone_code`, `kp_role`, `twist_source`, `vector`, `job_type`, `order`, …) is rendered into the page HTML as a header table and also kept in `flags.neon-black.<field>` so it survives round-trips. The type-specific fields are exactly those of Plan A.4:

| Type | Fields (Plan A.4) |
|---|---|
| `character-trope` | `fixed_kits[3]`, `choice_kits[3]`, `loadout` (Core p. 178 format) |
| `pc-special` / `crew-special` | `prerequisite`, `persists_through_theme_replacement`, `improvement {name, description, effect_class, uses}` |
| `district` | `zone_code`, `central_concept`, `story_tag`, `pillar`, `developments[] {order, pillar, subtheme, summary}`, `key_players_present[]`, `caste_band` |
| `key-player` | `kp_role`, `base_concept`, `twist`, `twist_source (bible \| invented)`, `agenda`, `resources[]`, `motifs[]`, `key_characters[]`, `challenges[]`, `territory[]` |
| `npc` | `affiliation[]`, `splat`, `role_in_pilot`, `vector {want, push}`, `challenge (slug \| null)` |
| `job` | `job_type[]`, `sessions`, `series_pole (paycheck \| misfits \| pivot)`, `hooks[]`, `goal`, `vectors[]`, `core_moments[]`, `scenes[]`, `climax`, `aftermath`, `twist_for_pivot` |
| `scene` | `job`, `order`, `set_piece`, `district`, `story_tags[]`, `challenges[]`, `vectors_active[]`, `core_moment`, `flashback_hooks[]` |

Wikilinks `[[slug]]` become Foundry `@UUID[...]` links once ids are fixed (§6); until then they render as plain text.

## 6. Emission shapes (for WP9's `tools/`)

**Ids.** Every document needs a 16-character `[A-Za-z0-9]` `_id`, stable across rebuilds: derive it deterministically from the slug (e.g., first 16 base62 characters of a SHA-1 of `neon-black:<type>:<slug>`), record the mapping in `tools/ids.json`, and never regenerate it. Embedded Items derive theirs from `<parent-slug>:<kind>:<index>`.

**`_key`** (required by the repo's `pack-compendium` script and by the Foundry CLI `_source` layout, as seen in the samples): Items `!items!<id>`; Actors `!actors!<id>`; embedded Actor items `!actors.items!<actorId>.<itemId>`; JournalEntries `!journal!<id>`; pages `!journal.pages!<entryId>.<pageId>`.

Minimal `themekit`:

```json
{ "_id": "…", "_key": "!items!…", "name": "…", "type": "themekit", "img": "icons/svg/item-bag.svg",
  "system": { "description": "<p>…card HTML…</p>", "locked": false, "version": "1",
    "free_content": false, "locale_name": "", "systemName": "", "sourceBook": "",
    "themebook_id": "K3rvh4bMi0L6S4lS", "themebook_name": "Augmentation", "use_tb_improvements": true,
    "power_tagstk": [ {"letter": "A", "tagname": "…", "description": "…"}, "… ten entries …" ],
    "weakness_tagstk": [ {"letter": "A", "tagname": "…", "description": "…"}, "… four entries …" ],
    "improvements": [ {"name": "", "uses": 0, "description": "", "effect_class": ""}, "… five entries …" ],
    "motivation": "itch", "fade_type": "decay", "subtype": "Noise", "system_compatiblity": "otherscape" },
  "effects": [], "folder": null, "sort": 0, "ownership": {"default": 0}, "flags": {} }
```

Minimal `threat` (one Limit, one base status, one Threat with one Consequence):

```json
{ "_id": "…", "_key": "!actors!…", "name": "…", "type": "threat", "img": "icons/svg/mystery-man.svg",
  "system": { "locked": false, "biography": "", "description": "<p>…profile HTML…</p>", "short_description": "…",
    "gmnotes": "", "crewThemes": [], "version": "1", "alias": "?????", "useAlias": true,
    "finalized": false, "mythos": "", "logos": "", "age": 0, "residence": "", "pronouns": "",
    "is_template": false, "template_ids": [], "collectiveSize": 1,
    "defaultTags": [ {"type": "tag", "name": "…", "description": "", "locked": false, "version": "1", "subtype": "story", "crispy": false, "hidden": false} ],
    "defaultStatuses": [ {"type": "status", "name": "alert", "description": "", "locked": false, "version": "1", "tier": 2, "pips": 0, "hidden": false} ] },
  "items": [
    { "_id": "…", "_key": "!actors.items!….…", "name": "hurt or subdue", "type": "spectrum", "system": {"maxTier": 4} },
    { "_id": "…", "_key": "…", "name": "…", "type": "gmmove", "system": {"description": "…", "locked": false, "version": "1", "subtype": "soft", "taglist": [], "statuslist": [], "hideName": false, "header": "symbols", "superMoveId": ""} },
    { "_id": "…", "_key": "…", "name": "…", "type": "gmmove", "system": {"description": "… [gunshot-wound-2]", "locked": false, "version": "1", "subtype": "hard", "taglist": [], "statuslist": ["gunshot-wound-2"], "hideName": true, "header": "symbols", "superMoveId": "<soft id>"} }
  ],
  "prototypeToken": {"name": "…", "actorLink": false}, "effects": [], "folder": null, "sort": 0, "ownership": {"default": 0}, "flags": {} }
```

Minimal `JournalEntry`:

```json
{ "_id": "…", "_key": "!journal!…", "name": "…",
  "pages": [ { "_id": "…", "_key": "!journal.pages!….…", "name": "…", "type": "text", "title": {"show": true, "level": 1},
               "text": {"format": 1, "content": "<h1>…</h1>…"}, "sort": 0, "ownership": {"default": -1}, "flags": {"neon-black": {"type": "district", "slug": "…"}} } ],
  "folder": null, "sort": 0, "ownership": {"default": 0}, "flags": {"neon-black": {"type": "district", "slug": "…"}} }
```

## 7. Module skeleton and install path (Plan Part D)

```
neon-black-module/
  module.json
  packs/theme-kits/_source/*.json      (Item themekit — splat kits, Self kits, crew kits)
  packs/challenges/_source/*.json      (Actor threat, with embedded spectrum / gmmove items)
  packs/power-sets/_source/*.json      (Actor threat, is_template: true)
  packs/loadout/_source/*.json         (Item tag, subtype loadout)
  packs/journals/_source/*.json        (JournalEntry: districts, key players, jobs, scenes, tropes, specials, npcs)
  assets/                              (WP-I images, referenced by relative path)
```

`module.json` (Foundry 13/14 shape):

```json
{ "id": "neon-black", "title": "Neon Black", "description": "Neon Black campaign content for City of Mist / Mist Engine in Otherscape mode.",
  "version": "0.1.0", "authors": [{"name": "…"}],
  "compatibility": {"minimum": "13", "verified": "14"},
  "relationships": {"systems": [{"id": "city-of-mist", "type": "system", "compatibility": {"minimum": "4.5.3"}}]},
  "packs": [
    {"name": "theme-kits", "label": "Neon Black — Theme Kits", "path": "packs/theme-kits", "type": "Item", "system": "city-of-mist"},
    {"name": "challenges", "label": "Neon Black — Challenges", "path": "packs/challenges", "type": "Actor", "system": "city-of-mist"},
    {"name": "power-sets", "label": "Neon Black — Power Sets", "path": "packs/power-sets", "type": "Actor", "system": "city-of-mist"},
    {"name": "loadout", "label": "Neon Black — Street Catalog", "path": "packs/loadout", "type": "Item", "system": "city-of-mist"},
    {"name": "journals", "label": "Neon Black — Megacity, Key Players & Jobs", "path": "packs/journals", "type": "JournalEntry", "system": "city-of-mist"} ],
  "manifest": "https://<host>/neon-black/releases/latest/download/module.json",
  "download": "https://<host>/neon-black/releases/latest/download/neon-black.zip" }
```

Packing: the repo's `npm run pack-compendium` / `unpack-compendium` show the `_source/*.json` shape; the Foundry CLI (`@foundryvtt/foundryvtt-cli`) packs a `_source` folder into LevelDB. **Sqyre install path:** host the built module at a stable URL (a GitHub release carrying `module.json` and the zip), then Sqyre → Module Manager → install by manifest URL → enable the module in the world; the `city-of-mist` system and `mist-hud` are on the official package list and should appear in Sqyre's picker directly (Plan Part D). Son of Oak has recruited developers for official Foundry support for all three games with no release date; re-check before packaging (Brief §9.3). WP9 emits; it does **not** package or publish.

## 8. Verification items — WP9's findings

From Plan Part D (1–4) and from WP0's cross-check (5–15). **WP9 resolved these against the system source** (a shallow clone of `taragnor/city-of-mist` at **v4.5.3**; all `file:line` citations below are relative to `src/city-of-mist/`, and every one was read, not inferred). Each item states what the code says and what `tools/foundry/convert.py` does. Four items (3, 13-in-HUD, 15, and the runtime half of 1) need a live Foundry world or the `mist-hud` package and stay **UNRESOLVED — needs runtime**; nothing else does.

**1. `system_compatiblity` value — RESOLVED: `"otherscape"`.**
`OtherscapeSystem.name` returns the literal `"otherscape"` (`module/systemModule/otherscape.ts:37`), and every shipped Otherscape themebook, move, essence and improvement in `packs/themebooks/_source/` carries `"system_compatiblity": "otherscape"`. The comparison is `this.system.system_compatiblity.includes(system)` after an `== "any"` short-circuit (`module/city-item.ts:1674-1677`). *Also found:* for a **themekit** the effective compatibility is taken from its **themebook**, not from its own field — `get systemCompatiblity()` delegates through `getThemebookOrTK()` and only falls back to the kit's own value when the themebook cannot be resolved (`module/city-item.ts:224-228`). So a kit that resolves a shipped Otherscape themebook is Otherscape-compatible either way. **convert.py** emits `system_compatiblity: "otherscape"` on every themekit. *Runtime half unresolved:* there is **no theme-kit picker** to appear in — `CityDialogs.themeBookSelector` lists only `themebook` Items and one "theme-kit" radio that opens a *builder* (`module/city-dialogs.ts:35-99`); a prebuilt kit is added by **dragging the `themekit` Item onto a PC sheet**, which copies it to the actor and builds the theme (`module/city-actor.ts:610-618 addThemeKit`). Confirm the drag path in a world.

**2. `themebook_id` vs `themebook_name` — RESOLVED: the name alone resolves; the id is still worth emitting.**
`getThemebookOrTK()` passes both to `CityDB.getThemebook(name, id)` (`module/city-item.ts:404-431`), which calls `searchForContent(arr, id, name)` — `arr.find(x => x.id == id)` first, **then** `arr.find(x => x.name == name)` (`module/city-db.ts:188-217`, `219-224`). A name-only kit therefore resolves. But themebook **names are not unique** across systems in the shipped pack (there are two `Companion` themebooks, `K1T0cmc315lR55ql` for Otherscape and `XytWXzpkLnwgxBxA` for another game; likewise two `Personality`), so a name-only kit can bind the wrong book. **convert.py** emits both, using the ids harvested from `packs/themebooks/_source/` (filtered to `system_compatiblity == "otherscape"`), listed as `SHIPPED_THEMEBOOKS` in `tools/foundry/convert.py`:

| Themebook | `_id` | shipped `subtype` |
|---|---|---|
| Affiliation | `noqoLlmqIwjirJ52` | Self |
| Assets | `m7aMSrzoz8iEjrXi` | Self |
| Expertise | `FUhv3c81M1tcVSJD` | Self |
| Horizon | `WQ1gYMo8oWoiPX2a` | Self |
| Personality | `FW5g6LLhbaf5BFFm` | Self |
| Troubled Past | `snHXQlSZdGALWPNq` | Self |
| Artifact | `NgbUT22G4qsBqSwn` | **Mythos** |
| Companion | `K1T0cmc315lR55ql` | **Mythos** |
| Esoterica | `f0Hldws5yB2ezw1Z` | **Mythos** |
| Exposure | `5CG8unkzHqU6xuQW` | **Mythos** |
| Augmentation | `K3rvh4bMi0L6S4lS` | Noise |
| Cutting Edge | `eSg1666zWlbhuoyl` | Noise |
| Cyberspace | `D88XNZrAQ5oMfsFW` | Noise |
| Drones | `3i6BJjmC1oKKQvCV` | Noise |
| Crew (Otherscape) | `ayN2BXLJ2IgQyfh8` | Crew-OS |
| Loadout | `sXQ4DJvPy9GwATCn` | Loadout |

`check.py` warns on an empty `themebook_id`; no emitted kit has one.

**3. HUD and Limits — PARTLY RESOLVED; the HUD half needs runtime.**
In the **system's own** sheet, `999` renders as `-`: the spectrum editor's tier control is a radio row `1..6` plus one `value=999` labelled `-` (`templates/items/spectrum.html:7-13`), and the display helper is `spectrumConvert` → `SPECTRUM_VALUES[x]`, where `SPECTRUM_VALUES[999] == "-"` (`module/city-handlebars-helpers.ts:316-317`, `module/datamodel/spectrum-values.ts:57-65`). Limits are read from `getSpectrums()`, which merges the actor's own `spectrum` Items with those of its attached templates, de-duplicating **by name** (`module/city-actor.ts:291-303`). How `mist-hud` renders them is **UNRESOLVED — needs runtime** (that package is not in this repo). **convert.py** emits `{maxTier: n}` with `999` for immune.

**4. Template inheritance — RESOLVED: gmmoves, spectra *and* defaults all inherit; a compendium template resolves without import.**
`getGMMoves()` concatenates the actor's own gmmoves with each attached template's, recursing to `MAX_TEMPLATE_DEPTH` (`module/city-actor.ts:281-289`). `getSpectrums()` does the same, de-duplicating by name (`:291-303`). `allDefaultTagsAndStatuses()` merges `system.defaultTags` + `system.defaultStatuses` with the templates' own, skipping any whose `name` **and** `type` already exist (`module/city-actor.ts:1602-1633`). So **`defaultTags`/`defaultStatuses` do inherit** — WP0's §4.2 caution ("each Challenge repeats its base tags itself") is unnecessary, and duplicates are silently de-duplicated, so repeating them is harmless. Compendium resolution: `getDangerTemplate(id)` searches `CityDB._dangerTemplates`, built by `refreshDangerTemplates()` from `filterActorsByType("threat")` (`module/city-db.ts:151-158`) → `DBAccessor.allActors()` → `getAllByType("Actor")`, which is `getBaseItemsByType(...).concat(getCompendiumItemsByType(...))` (`module/tools/db-accessor.ts:55-57`, `63-65`, `96-99`), and compendium content is loaded at startup by `getCompendiumDataByType` across **all** Actor packs (`:119-120`, `:141-150`). A `power-sets` compendium template therefore resolves by id for a Challenge in the world. **convert.py** resolves each `power_sets:` slug to its emitted Power Set `_id` and writes it into `template_ids`; `check.py` errors if an entry names no emitted document.

**5. Mythos subtype — RESOLVED: the shipped books use `"Mythos"`, and `"Mythos-OS"` would break Essence.**
All four shipped Otherscape Mythos themebooks (Artifact, Companion, Esoterica, Exposure) carry `"subtype": "Mythos"` — see the table in item 2. `determineEssenceFromThemes()` reads `theme.getThemebookOrTK()!.system.subtype` and compares against the bare string in three places: `case "Mythos": return;` (`module/systemModule/otherscape.ts:135-136`), `!themeTypes.includes("Mythos")` → Cyborg (`:141`), `!themeTypes.includes("Self")` → Transhuman (`:147`). A kit whose subtype is `Mythos-OS` is an unrecognised third type, so a Self + Mythos-OS PC would be auto-Essenced **Cyborg** instead of Spiritualist, and a pure-Mythos-OS PC would fall through to `Singularity`/`Real`'s `switch` with no match instead of returning `undefined`. `themeTypes()` does define **both** keys (`:71-85`, with the comment *"rewriting mythos is necessary due to a bug with older versions"*) so `Mythos-OS` is a legal theme type for display; only the Essence logic is written against `Mythos`. **DIFFERS from Plan A.4.** **convert.py** maps the vault's `category: Mythos-OS` → `system.subtype: "Mythos"` (`CATEGORY_TO_SUBTYPE`). The vault frontmatter is unchanged; the translation happens at emit time. `check.py` raises a warning if any emitted kit ever carries `Mythos-OS`. No setting toggle exists for this — `autoEssence` is on/off only (`otherscape.ts:292-305`); turning it off just means the MC sets Essence by hand.

**6. `fade_type` — RESOLVED: the field is dead in v4.5.3; `decay` vs `fade` changes nothing.**
`fade_type` appears in exactly two places in the whole source tree — `Themebook` and `Themekit`'s `defineSchema()` (`module/datamodel/item-types.ts:113`, `:132`) — and in the shipped pack JSON. **No sheet, template or module reads it.** The Decay wording on a card comes from the theme *type*: `themeTypes()[type].decreaseLocalization = "Otherscape.terms.decay"` for every Otherscape type (`module/systemModule/otherscape.ts:53, 61, 68, 75, 83, 90`). So the shipped themebooks' `"fade"` and the Plan's `decay` are equally inert. **convert.py** emits `fade_type: "decay"` as Plan A.4 says, since it is what the vault means and nothing contradicts it.

**7. Consequences — RESOLVED: only the `description` markup is applied; `statuslist`/`taglist` are never read.**
`formatGMMoveText()` builds its returned `taglist`/`statuslist` **entirely from the description** — `CityHelpers.unifiedSubstitution(displayedText, collectiveSize)` plus `autoAddstatusClassSubstitution` — and never touches `this.system.taglist` / `this.system.statuslist` (`module/city-item.ts:1547-1581`). Those lists are what `CityActor` then applies (`module/city-actor.ts:1377-1390`). The datamodel fields exist but are vestigial. Markup grammar, from `unifiedSubstitution` (`module/city-helpers.ts:309-350`): the regex is `/\[([ \w,]*:)?([\p{Letter}\d\- ]+)\]/gmu` — an optional comma-separated option prefix ending in `:`, then a name of **letters, digits, hyphens and spaces only**. `parseOptions` (`:355-380`) maps `a`→autoApply, `i`→ignoreCollective, `s`→scene, `p`→permanent, `t`→temporary. A name is read as a **status** when its second-to-last character is a space or hyphen and its last is a digit or `X` (`isStatusParseable`, `:383-390`); otherwise it is a story tag. Statuses have the actor's `collectiveSize` **added** to their tier unless the `i` option is set. **Three consequences for us:** (a) statuses and tags must be in the description; (b) a name containing a comma, apostrophe, slash or `&` silently fails to match and stays literal text — 13 vault Consequence tags do (see §9); (c) `{braces}` are stripped from player-facing text (`removeWithinBraces`, `module/city-item.ts:1556-1560`), so prose braces must not survive. **convert.py** brackets the status/tag **in place** where the vault prose already names it, appends `[name-tier]` / `[s:tag]` markup otherwise, converts braces to parentheses, still fills `taglist`/`statuslist` for round-trip fidelity, and reports every name the regex would reject.

**8. Embedded defaults — RESOLVED as far as static checking goes.**
`defaultTags: arr(EmbeddedDataField(EmbeddedTagDM))` and `defaultStatuses: arr(EmbeddedDataField(EmbeddedStatusDM))` (`module/datamodel/actor-types.ts:87-88`); the two `DataModel`s declare `{type, name, description, locked, version, subtype, crispy, hidden}` and `{type, name, description, locked, version, tier, pips, hidden}` (`module/datamodel/item-types.ts:150-160`, `326-334` with `coreStatus()` at `:318-324` and `tiered()` at `:85-90`). An `EmbeddedDataField` takes a plain object in source JSON, so the CLI needs no special handling. **convert.py** expands each vault string into the full object and parses `alert-2` into `{name: "alert", tier: 2}`; `check.py` verifies every key and type. Confirming the CLI round-trip needs the CLI, which WP9 does not run (no packaging) — **low risk, static shape verified.**

**9. Loadout — RESOLVED for the category; the drag path is structurally supported.**
`TAG_CATEGORY_LIST` is `["none", "hindering", "weakening", "ability", "empower", "object", "being"]` (`module/config/tag-categories.ts:1-9`). It is a **mechanical** classification, not a gear catalogue, and no code reads `tag.system.category` at all in v4.5.3 (the only `system.category` reads are on `move` and `status`). **convert.py** emits `category: "none"` — the datamodel initial — and puts the vault's `catalog` in the description. Loadout mechanics: a Loadout theme's specials list is `["loadout"]` (`module/systemModule/otherscape.ts:49-56`), and a loadout tag is spendable when `subtype == "loadout" && !activated_loadout` (`module/selected-tags.ts:237-238`), toggled by `toggleLoadoutActivation()` (`module/city-item.ts:1679-1686`). Nothing requires a `theme_id` at rest, so a loose compendium `tag` Item is a valid vehicle; whether the sheet accepts the drop onto a Loadout theme is **UNRESOLVED — needs runtime**, and the fallback (a Loadout `themekit`) remains available. **Flaws** go in the description: the shipped `Loadout` themebook has empty `power_questions`/`weakness_questions` (`packs/themebooks/_source/Loadout_sXQ4DJvPy9GwATCn.json`), so there is no sample to follow, and a `tag` has no flaw field. convert.py also mirrors the first three tags into `example0..2` and the first three flaws into `restriction0..2`, which are free-text and harmless.

**10. Crew kit motivation — RESOLVED: `system.motivation` does not reach the card at all.**
`get motivationName()` fetches the themebook/themekit and then **ignores it**, returning `SystemModule.themeIdentityName(theme)` — the theme *type*'s `identityName` (`module/city-item.ts:1690-1708`; the `system.motivation` branch is commented out at `:1701-1707`). `themeIdentityName` is `allThemeTypes()[themetype].identityName` (`module/config/system-module.ts:124-132`). So in Otherscape mode the label is fixed by category: Self → Identity, Noise → Itch, Mythos / Mythos-OS → Ritual, Crew-OS and Loadout → Crew Identity (`otherscape.ts:54, 62, 69, 76, 84, 91`). A `Crew-OS` kit whose `motivation` is `ritual` or `itch` still reads "Crew Identity". **convert.py** emits the vault's `motivation_type` verbatim (it is valid data and may be read again in a later release) and puts the motivation statement in the card HTML, where it is actually visible.

**11. JournalEntry pages — RESOLVED: core rendering, no system sheet.**
The system registers sheets for Actors and Items only; the sole JournalEntry touch-points are a `renderJournalDirectory` hook that boots the status tracker (`module/city.ts:169-172`) and `CityDB.loadTutorial()`, which scans **every** JournalEntry compendium for an entry named `"System Tutorial"` (`module/city-db.ts:47-53`). Pages therefore render with core Foundry, and `text.format: 1` is core's HTML format constant. **New caution:** no Neon Black JournalEntry may be named `System Tutorial`, or it would shadow the system's own tutorial; `check.py` enforces this. **convert.py** emits one entry per vault file with a single `type: "text"` page, `title.show: false` (the page's HTML carries its own `<h1>`), and `text.format: 1`.

**12. `_key` for journals — PARTLY RESOLVED.**
The shipped `_source` files demonstrate `!items!<id>` and `!actors!<id>` / `!actors.items!<actorId>.<itemId>` (`packs/themebooks/_source/*.json`, `packs/sampledangers/_source/Zeus_*.json`), i.e. `!<collection>!` and `!<collection>.<embedded>!<parent>.<child>`. The system ships no JournalEntry pack in `_source` form (its `documentation` pack is LevelDB only), so `!journal!` / `!journal.pages!` cannot be confirmed *from this repo*; they follow the same rule and are what the Foundry CLI derives. **convert.py** emits them; if a CLI version disagrees it regenerates `_key` while packing, so the risk is cosmetic.

**13. Alias display — RESOLVED, and it is a mismatch: `system.alias` is the wrong field for a threat.**
`getDisplayedName()` resolves token name → `prototypeToken.name` → `name`, and never reads `system.alias` (`module/city-actor.ts:1237-1257`). The threat sheet's field *labelled* "Alias" is bound to `token.name` (`templates/parts/threat-sheet-header.html:5,7`). `system.alias` is read in only one place in the codebase, `scene-tags.ts:42-47`, where it stores a **scene id** on the scene-container actor, and `useAlias` is written by `toggleAlias()` (`module/city-actor.ts:1156-1159`) and read nowhere. So the book's alias — what PCs see before they know what this is — must go in **`prototypeToken.name`**. **DIFFERS from §4.1 of this document.** **convert.py** writes the vault `alias` to `prototypeToken.name` (with `displayName: 30` so the nameplate shows on hover) and falls back to the Challenge's own name when there is no alias; it still fills `system.alias`/`useAlias` for round-trip fidelity, documented as inert. `check.py` errors if the two disagree or if `prototypeToken.name` is empty. Whether `mist-hud` shows something different is **UNRESOLVED — needs runtime**.

**14. Improvement `uses` — RESOLVED: `{current, max, expended}`.**
`Improvement` composes `expendable()`, which is `uses: sch({current: num, max: num, expended: bool})` (`module/datamodel/item-types.ts:223-237`, `92-100`); the shipped improvement Items match (`packs/themebooks/_source/Interfacer_d4MptVURfH36wHCC.json` → `"uses": {"current": 0, "max": 0, "expended": false}`). This is **not** the themekit's `improvements[]` entry shape, which is a flat `{name, uses: number, description, effect_class}` (`module/datamodel/default-themekit.ts:40-45`) — the two must not be confused. `effect_class` is a free string used to hook coded effects (the shipped Otherscape improvements use values like `"VETERAN"`); an empty one simply means no coded effect, and every Neon Black Special is text-only, so empty is correct. **convert.py** emits themekit `improvements[]` in the flat shape with the Plan's vault-only `letter` key dropped. It does **not** currently emit `improvement` Items for `pc-special` / `crew-special`; those become JournalEntry pages with an `improvement` block rendered into the header table. `check.py` carries the `Improvement` field list ready for the day that pass lands.

**15. `mist-hud` — UNRESOLVED — needs runtime.** The package is not in this repo and WP9 has no network beyond the system clone. Its compatibility with `city-of-mist` 4.5.3 on Foundry 13–14, and whether it reads `collectiveSize` for Scale, must be checked in a world. Note that the *system* reads `collectiveSize` as a number and coerces `NaN` to `0` (`module/city-item.ts:1550-1555`), and adds it to every status tier parsed out of a gmmove description unless the `i` option is set — so Scale is live in the system regardless of the HUD.

## 9. WP9 run record

`tools/foundry/convert.py --all` → `build/`, checked by `tools/foundry/check.py`. See `tools/foundry/README.md` for how to run, what is emitted, and how to pack and install.

**Emitted documents, 313 in five packs:**

| Pack | Document | Count | From |
|---|---|---|---|
| `theme-kits` | Item `themekit` | **35** | 32 `theme-kit` + 3 `crew-kit` |
| `challenges` | Actor `threat` | **48** | 48 `challenge` |
| `power-sets` | Actor `threat` (`is_template: true`) | **14** | 14 `power-set` |
| `loadout` | Item `tag` (`subtype: loadout`) | **30** | 30 `loadout-item` |
| `journals` | `JournalEntry` | **186** | 42 `index`, 29 `npc`, 25 `scene`, 22 `district`, 17 `pc-special`, 10 `character-trope`, 10 `key-player`, 10 `membership`, 10 `splat-overview`, 4 `crew-special`, 4 `series`, 3 `job` |

Plus `build/module.json`, `build/README.md`, `build/ids.json`, `build/report.json`.

**Vault files skipped, 27** (all deliberate, per §1): 14 `type: meta` (registers, style guide, README, preamble, this file), 13 `99-templates/*` carrying `template: true`. Nothing else was skipped — no file failed to parse and no file was below `status: review`.

**check.py: 0 errors, 0 warnings** across all 313 documents and `module.json`.

**Residual warnings from convert.py, 13** — all one kind, and all inherent to the vault's wording rather than to the conversion: a Consequence story tag whose name contains a comma or apostrophe cannot be expressed in the system's `[...]` markup (item 7 above), so it is kept in `system.taglist` and left as plain prose in the description. The MC can still create the tag by hand. Affected: `nobody in, nobody out` and `no feed, no witnesses` (continuity-crisis-response-cell), `one operator, alone, deep` (the-cold-suite), `a haulier, a plate, and a direction` (the-consignment-window), `a date, and nothing to show` (the-counting-room), `a fair price, refused` (the-carters), `the alpha's terms` and `somebody else's count` (pack-tactics), `on Meliora's collection list` (sterile-field-unit), `on the site's entry log` (the-sterile-field), `there's work` (marisol-okonkwo-challenge), `another name in the Kitchen's ledger` (uncle), `on the Almoners' paper` (first-alms).

**Unresolved wikilink targets, 10 distinct** — every one is a `type: meta` file that is never converted (`build-choices`, `names`, `image-briefs`, `style-guide`, `open-questions`, `session-zero-packet`, `conflict-register`, `foundry-mapping`, `README`) plus the template placeholder `assets/...`. They render as plain text, which is the intended fallback. No content file is missing a document.

**New mismatches WP9 found, beyond WP0's list:**

1. **`system.alias` is not the threat's alias** (item 13) — `prototypeToken.name` is. §4.1's row is superseded.
2. **`themekit.system_compatiblity` is shadowed by the themebook's** (item 1) — `get systemCompatiblity()` delegates through `getThemebookOrTK()` (`city-item.ts:224-228`), so a kit bound to a shipped Otherscape themebook is Otherscape-compatible whatever its own field says.
3. **`themekit.motivation` never reaches the card** (item 10) — `motivationName()` returns the theme *type*'s label and the `system.motivation` branch is commented out (`city-item.ts:1690-1708`). §3.1's `motivation_type` row is correct as data, but the field is presently cosmetic.
4. **`fade_type` is unread anywhere in v4.5.3** (item 6). §3.1's DIFFERS row can be closed: neither value has an effect.
5. **`gmmove.taglist` / `statuslist` are unread** (item 7) — `formatGMMoveText` derives both from the description. §4.1's "emit both" advice is right, but only the description half does anything.
6. **`defaultTags` / `defaultStatuses` *do* inherit through `template_ids`** (item 4). §4.2's instruction that "each Challenge repeats its base tags itself" is unnecessary (harmless, since the merge de-duplicates by name + type).
7. **A JournalEntry named `System Tutorial` would shadow the system's own** (item 11) — `CityDB.loadTutorial()` scans every JournalEntry compendium by name (`city-db.ts:47-53`). `check.py` guards it.
8. **`unifiedSubstitution`'s name charset is narrower than the vault's prose** (item 7) — commas, apostrophes, `&` and slashes break the markup silently. This is the source of all 13 residual warnings, and it is worth knowing when writing future Consequence tags: keep tag names to letters, digits, hyphens and spaces.
9. **There is no theme-kit picker** (item 1) — a prebuilt `themekit` reaches a PC by drag-and-drop onto the sheet (`city-actor.ts:610-618`), not through the "Select Themebook" dialog, which lists `themebook` Items only (`city-dialogs.ts:35-58`). The Plan's phrasing "appears in the Otherscape theme-kit picker" describes something that does not exist.
10. **The repo has no `pack-compendium` / `unpack-compendium` npm script** — Plan Part D and §7 above name them, but `package.json` at v4.5.3 defines only `test` and `build`. The packing step is a direct `@foundryvtt/foundryvtt-cli` call; `tools/foundry/README.md` gives it.

**WP9's own conversion choices** (id scheme, ownership mapping, wikilink → UUID policy, and the rest) are recorded in `00-meta/additions/WP9.md`.
