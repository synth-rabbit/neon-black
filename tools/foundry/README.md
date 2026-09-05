# `tools/foundry/` — Foundry VTT conversion (WP9)

![[assets/cover.png]]

Two scripts. `convert.py` reads the vault and writes Foundry compendium **source**
JSON plus a `module.json`; `check.py` validates that output against the
`city-of-mist` data models. Neither packages nor publishes anything.

Target: Taragnor's system **`city-of-mist`** ("City of Mist / Mist Engine")
**v4.5.3**, Foundry **13–14**, switched to **Otherscape** mode.
See `00-meta/foundry-mapping.md` for the field-by-field mapping and for the
verification items these scripts answer.

## Requirements

* Python 3 (stdlib) + **PyYAML**. Nothing else; no network access.
* The vault, checked out at the repository root. Both scripts locate the root
  from their own path, so they can be run from anywhere.

## Run

```bash
python3 tools/foundry/convert.py --all        # every pack + module.json
python3 tools/foundry/check.py                # validate what was emitted
```

Selective runs and options:

```bash
python3 tools/foundry/convert.py --theme-kits --challenges
python3 tools/foundry/convert.py --module                 # module.json + README only
python3 tools/foundry/convert.py --all --uuid-style world # @UUID[JournalEntry.<id>]
python3 tools/foundry/convert.py --all --out /tmp/nb      # write elsewhere
python3 tools/foundry/check.py --out /tmp/nb --verbose
```

`convert.py` is **deterministic and re-runnable**: document ids are hashes of the
vault slug, `_stats` timestamps are null, and the output directory is rewritten in
place. Two runs of the same vault produce byte-identical files, so `diff -r` is a
meaningful regression check.

## What is emitted

Everything lands under `build/`, which is git-ignored.

```
build/
  module.json                          module manifest (id: neon-black)
  README.md                            note that ships inside the module folder
  ids.json                             slug -> {_id, pack, documentClass, page}
  report.json                          counts, skipped vault files, field warnings
  packs/theme-kits/_source/*.json      Item   themekit      <- theme-kit, crew-kit
  packs/challenges/_source/*.json      Actor  threat        <- challenge
  packs/power-sets/_source/*.json      Actor  threat (is_template: true) <- power-set
  packs/loadout/_source/*.json         Item   tag (subtype loadout) <- loadout-item
  packs/journals/_source/*.json        JournalEntry <- district, key-player, npc, job,
                                       scene, character-trope, pc-special, crew-special,
                                       membership, series, splat-overview, index
```

One vault file becomes exactly one top-level document. A Challenge's Limits,
Threats, Consequences and Specials become **embedded Items** inside its Actor
document (`spectrum` / `gmmove`), not separate files.

Files that are **not** converted: anything with `template: true` (the
`99-templates/` shapes), every `type: meta` file (the registers, style guide,
README, this mapping), and anything whose `status` is not `review` or `approved`.
`report.json` lists each skip with its reason.

## Document ids

`_id` is derived from the vault slug, so it never moves between runs:

```
_id = base62( sha1("neon-black:<kind>:<key>") )[-16:]
```

* top-level documents — `kind` = pack name, `key` = the vault slug
* embedded Items — `kind` = `"<pack>/<parent-slug>"`, `key` = `"<itemkind>:<index>"`
* journal pages — `kind` = `"journals/<slug>"`, `key` = `"page:0"`

`build/ids.json` records the mapping. `convert.py` aborts on a collision.

`_key` follows the Foundry CLI `_source` layout the system's own packs use:
`!items!<id>`, `!actors!<id>`, `!actors.items!<actorId>.<itemId>`,
`!journal!<id>`, `!journal.pages!<entryId>.<pageId>`.

## Turning `_source` into LevelDB packs

`_source/*.json` is the unpacked form. Foundry loads a compendium from a LevelDB
directory, so the JSON has to be packed before a world can read it. Two routes,
both offline:

### 1. The Foundry CLI (recommended)

```bash
npm install -g @foundryvtt/foundryvtt-cli
cd build
for p in theme-kits challenges power-sets loadout journals; do
  fvtt package pack "$p" --in "packs/$p/_source" --out "packs" --nedb=false
done
```

`fvtt package pack` writes `build/packs/<name>/` as a LevelDB directory beside the
`_source` folder it read. Ship both if you like — Foundry only reads the LevelDB
files; `_source/` is harmless and useful for diffs. The CLI's `--id`/`--type`
options are only needed when it cannot infer the package from the working
directory; passing `--in`/`--out` explicitly, as above, avoids that.

To go the other way (inspect a shipped pack), `fvtt package unpack <name> --in
packs/<name> --out packs/<name>/_source`.

### 2. The system's own approach

`taragnor/city-of-mist` keeps its packs in exactly this layout —
`src/city-of-mist/packs/<name>/` holding the LevelDB files plus a `_source/`
directory of one JSON per document — and its `pack-compendium` /
`unpack-compendium` steps are the same Foundry CLI calls. The shipped
`_source` files are the reference for the JSON shape; note that some of them are
older than the current data model (the Zeus sample still carries `collective_size`
and `max_tier`, which the system migrates on load). `convert.py` emits the
**current** keys (`collectiveSize`, `maxTier`), so no migration is needed.

At the time of writing, the upstream `package.json` exposes only a `build`
script; the packing itself is the CLI call above.

## Hosting a release and installing on Sqyre

WP9 does not publish. When someone does:

1. Pack the compendia (above) so `build/` contains `module.json` and
   `packs/<name>/` LevelDB directories.
2. Fill in the two placeholder URLs in `module.json` — `manifest` and `download` —
   with the real host. They currently read `https://<host>/neon-black/releases/...`.
   `manifest` must point at the `module.json` itself and must stay reachable at a
   stable URL, because Foundry re-fetches it to check for updates.
3. Zip the module folder so the archive's top level contains `module.json`
   (`cd build && zip -r neon-black.zip module.json README.md packs`).
4. Publish both files at those URLs — e.g. a GitHub release whose assets are
   `module.json` and `neon-black.zip`, using the
   `.../releases/latest/download/<file>` form so the manifest URL never changes.
5. On Sqyre: **Add-on Modules → Install Module → Manifest URL**, paste the
   `module.json` URL, install. The `city-of-mist` system is on the official
   Foundry package list, so install it from the system picker first if the world
   does not already use it.
6. In the world: enable **Neon Black** in *Manage Modules*, then set the system to
   **Otherscape** mode in the system settings. Leave the client setting
   **autoEssence** on if you want Essence assigned automatically from theme types.

The module declares `relationships.systems: [city-of-mist]`, so Foundry will warn
if it is enabled in a world running any other system.

## `check.py`

`check.py` re-implements, by hand, the field lists that
`src/city-of-mist/module/datamodel/{item-types,actor-types,…}.ts` declare, each
with the file and line range it was transcribed from, and reports:

* **MISSING** — a `defineSchema()` field the emitted document does not carry
  (Foundry would silently substitute the field's `initial`)
* **EXTRA** — a `system.*` key no `defineSchema()` declares (Foundry drops it)
* **MISTYPED** — a value whose JSON type does not match the field class
* enum violations — `motivation`, `fade_type`, `subtype`, `system_compatiblity`,
  `sourceBook`, gmmove `subtype`/`header`, tag `subtype`/`category`
* shape rules — ten power tags lettered A–J, four weakness tags A–D, five
  improvements, `spectrum.maxTier` within 1–999, 16-character `[A-Za-z0-9]` ids,
  `_key` matching the document, `superMoveId` naming a gmmove on the same Actor,
  `template_ids` naming an emitted Power Set, `ownership.default` a real level
* `module.json` — required keys, `compatibility` tracking the system's
  `system.json`, the `city-of-mist` relationship, and the five declared packs

It exits 1 on any error. Warnings never fail the run; the one that matters is
`subtype 'Mythos-OS'`, which would break Essence auto-detection (see
`00-meta/foundry-mapping.md` §8-5).

Re-checking against a newer system release: open the cited lines in the system
source and diff them against the dictionaries at the top of `check.py`.


## Images (WP-I)

`convert.py --all` copies the vault's `assets/` folder (districts, key-players, npcs, splats, jobs, cover — minus `manifest.md` and the unkeyed `npcs-raw/` originals) to `build/assets/`, and every document whose vault file embeds an image (`![[assets/...]]`) gets it as `img` (Actors also as the prototype token texture; a named NPC's `<slug>-challenge` Actor borrows the NPC's paper puppet). Paths are module-relative (`modules/neon-black/assets/...`), so the module must be installed with `assets/` alongside `module.json`. NPC puppets are keyed PNGs with alpha (`tools/keyout.py`).
