---
type: index
name: Assets Manifest
slug: manifest
status: review
source: custom
page: ""
owner: WP6
canon_refs: ["Plan Part F WP-I", "BC-137"]
flags: []
player_safe: false
---

# Assets Manifest

Every image the vault expects, with its prompt block in [[image-briefs]], the vault file it is linked from, and its generation status. WP-I fills `status` (`generated` | `rejected` | `regenerate`) and, for paper puppets, `method`: `alpha` when the model produced true transparency, `chroma` when it was generated on flat pure green `#00FF00`; all 29 puppets came back chroma and were keyed with `tools/keyout.py` (greenness key + edge-aware despill); the unkeyed originals are kept in `assets/npcs-raw/` (Plan WP-I; BC-137). Territory shots, districts and splat images have no method (they are opaque). Acceptance: every image is linked from exactly one vault file via `![[assets/...]]`; file names match slugs; no in-world image shows what the Masquerade hides unless its target is MC-only.

Pass 1 (WP6): 66 images — 18 districts, 20 Key Player images (10 emblems, 10 territory shots), 23 NPC paper puppets, 5 splat images. Pass 2 (WP8, BC-179): 22 images — 15 job scenes (core moments, climaxes and named set pieces), 6 job-NPC paper puppets, and the module cover — the rows at the end of the table.

| Image path | Brief block | Target | Aspect | Method (`alpha` \| `chroma`) | Status |
|---|---|---|---|---|---|
| `assets/districts/amalgam-stack.png` | [[image-briefs]] `### assets/districts/amalgam-stack.png` | [[amalgam-stack]] | 16:9 | — | generated |
| `assets/districts/aurelian-crest.png` | [[image-briefs]] `### assets/districts/aurelian-crest.png` | [[aurelian-crest]] | 16:9 | — | generated |
| `assets/districts/chancery-hill.png` | [[image-briefs]] `### assets/districts/chancery-hill.png` | [[chancery-hill]] | 16:9 | — | generated |
| `assets/districts/cinder-yards.png` | [[image-briefs]] `### assets/districts/cinder-yards.png` | [[cinder-yards]] | 16:9 | — | generated |
| `assets/districts/coldwater-outfall.png` | [[image-briefs]] `### assets/districts/coldwater-outfall.png` | [[coldwater-outfall]] | 16:9 | — | generated |
| `assets/districts/corbel-gallery.png` | [[image-briefs]] `### assets/districts/corbel-gallery.png` | [[corbel-gallery]] | 16:9 | — | generated |
| `assets/districts/ferrante-basin.png` | [[image-briefs]] `### assets/districts/ferrante-basin.png` | [[ferrante-basin]] | 16:9 | — | generated |
| `assets/districts/foundation-galleries.png` | [[image-briefs]] `### assets/districts/foundation-galleries.png` | [[foundation-galleries]] | 16:9 | — | generated |
| `assets/districts/gullet-market.png` | [[image-briefs]] `### assets/districts/gullet-market.png` | [[gullet-market]] | 16:9 | — | generated |
| `assets/districts/halloran-circus.png` | [[image-briefs]] `### assets/districts/halloran-circus.png` | [[halloran-circus]] | 16:9 | — | generated |
| `assets/districts/kilbride-stretch.png` | [[image-briefs]] `### assets/districts/kilbride-stretch.png` | [[kilbride-stretch]] | 16:9 | — | generated |
| `assets/districts/lowmere-sinks.png` | [[image-briefs]] `### assets/districts/lowmere-sinks.png` | [[lowmere-sinks]] | 16:9 | — | generated |
| `assets/districts/marlow-blocks.png` | [[image-briefs]] `### assets/districts/marlow-blocks.png` | [[marlow-blocks]] | 16:9 | — | generated |
| `assets/districts/meliora-terraces.png` | [[image-briefs]] `### assets/districts/meliora-terraces.png` | [[meliora-terraces]] | 16:9 | — | generated |
| `assets/districts/orison-reach.png` | [[image-briefs]] `### assets/districts/orison-reach.png` | [[orison-reach]] | 16:9 | — | generated |
| `assets/districts/relay-fields.png` | [[image-briefs]] `### assets/districts/relay-fields.png` | [[relay-fields]] | 16:9 | — | generated |
| `assets/districts/suture-row.png` | [[image-briefs]] `### assets/districts/suture-row.png` | [[suture-row]] | 16:9 | — | generated |
| `assets/districts/the-lattice.png` | [[image-briefs]] `### assets/districts/the-lattice.png` | [[the-lattice]] | 16:9 | — | generated |
| `assets/key-players/corp-a-emblem.png` | [[image-briefs]] `### assets/key-players/corp-a-emblem.png` | [[corp-a]] | 1:1 | — | generated |
| `assets/key-players/corp-a-scene.png` | [[image-briefs]] `### assets/key-players/corp-a-scene.png` | [[corp-a]] | 16:9 | — | generated |
| `assets/key-players/corp-b-emblem.png` | [[image-briefs]] `### assets/key-players/corp-b-emblem.png` | [[corp-b]] | 1:1 | — | generated |
| `assets/key-players/corp-b-scene.png` | [[image-briefs]] `### assets/key-players/corp-b-scene.png` | [[corp-b]] | 16:9 | — | generated |
| `assets/key-players/corp-c-emblem.png` | [[image-briefs]] `### assets/key-players/corp-c-emblem.png` | [[corp-c]] | 1:1 | — | generated |
| `assets/key-players/corp-c-scene.png` | [[image-briefs]] `### assets/key-players/corp-c-scene.png` | [[corp-c]] | 16:9 | — | generated |
| `assets/key-players/upstart-emblem.png` | [[image-briefs]] `### assets/key-players/upstart-emblem.png` | [[upstart]] | 1:1 | — | generated |
| `assets/key-players/upstart-scene.png` | [[image-briefs]] `### assets/key-players/upstart-scene.png` | [[upstart]] | 16:9 | — | generated |
| `assets/key-players/syndicate-emblem.png` | [[image-briefs]] `### assets/key-players/syndicate-emblem.png` | [[syndicate]] | 1:1 | — | generated |
| `assets/key-players/syndicate-scene.png` | [[image-briefs]] `### assets/key-players/syndicate-scene.png` | [[syndicate]] | 16:9 | — | generated |
| `assets/key-players/government-emblem.png` | [[image-briefs]] `### assets/key-players/government-emblem.png` | [[government]] | 1:1 | — | generated |
| `assets/key-players/government-scene.png` | [[image-briefs]] `### assets/key-players/government-scene.png` | [[government]] | 16:9 | — | generated |
| `assets/key-players/tao-society-emblem.png` | [[image-briefs]] `### assets/key-players/tao-society-emblem.png` | [[tao-society]] | 1:1 | — | generated |
| `assets/key-players/tao-society-scene.png` | [[image-briefs]] `### assets/key-players/tao-society-scene.png` | [[tao-society]] | 16:9 | — | generated |
| `assets/key-players/packs-emblem.png` | [[image-briefs]] `### assets/key-players/packs-emblem.png` | [[packs]] | 1:1 | — | generated |
| `assets/key-players/packs-scene.png` | [[image-briefs]] `### assets/key-players/packs-scene.png` | [[packs]] | 16:9 | — | generated |
| `assets/key-players/changeling-cells-emblem.png` | [[image-briefs]] `### assets/key-players/changeling-cells-emblem.png` | [[changeling-cells]] | 1:1 | — | generated |
| `assets/key-players/changeling-cells-scene.png` | [[image-briefs]] `### assets/key-players/changeling-cells-scene.png` | [[changeling-cells]] | 16:9 | — | generated |
| `assets/key-players/fence-network-emblem.png` | [[image-briefs]] `### assets/key-players/fence-network-emblem.png` | [[fence-network]] | 1:1 | — | generated |
| `assets/key-players/fence-network-scene.png` | [[image-briefs]] `### assets/key-players/fence-network-scene.png` | [[fence-network]] | 16:9 | — | generated |
| `assets/npcs/solenne-marchetti.png` | [[image-briefs]] `### assets/npcs/solenne-marchetti.png` | [[solenne-marchetti]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/ondine-ferreira.png` | [[image-briefs]] `### assets/npcs/ondine-ferreira.png` | [[ondine-ferreira]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/adaeze-ferreira.png` | [[image-briefs]] `### assets/npcs/adaeze-ferreira.png` | [[adaeze-ferreira]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/reidar-solano.png` | [[image-briefs]] `### assets/npcs/reidar-solano.png` | [[reidar-solano]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/priya-halstead.png` | [[image-briefs]] `### assets/npcs/priya-halstead.png` | [[priya-halstead]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/rasheeda-novak.png` | [[image-briefs]] `### assets/npcs/rasheeda-novak.png` | [[rasheeda-novak]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/vera-solano.png` | [[image-briefs]] `### assets/npcs/vera-solano.png` | [[vera-solano]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/hanne-oyelaran.png` | [[image-briefs]] `### assets/npcs/hanne-oyelaran.png` | [[hanne-oyelaran]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/rosalind-ekwueme.png` | [[image-briefs]] `### assets/npcs/rosalind-ekwueme.png` | [[rosalind-ekwueme]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/tomas-adair.png` | [[image-briefs]] `### assets/npcs/tomas-adair.png` | [[tomas-adair]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/bettina-alarcon.png` | [[image-briefs]] `### assets/npcs/bettina-alarcon.png` | [[bettina-alarcon]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/halina-ansah.png` | [[image-briefs]] `### assets/npcs/halina-ansah.png` | [[halina-ansah]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/halima-boyce.png` | [[image-briefs]] `### assets/npcs/halima-boyce.png` | [[halima-boyce]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/emeric-vann.png` | [[image-briefs]] `### assets/npcs/emeric-vann.png` | [[emeric-vann]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/constance-marchetti.png` | [[image-briefs]] `### assets/npcs/constance-marchetti.png` | [[constance-marchetti]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/nasrin-vogel.png` | [[image-briefs]] `### assets/npcs/nasrin-vogel.png` | [[nasrin-vogel]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/teodora-sowande.png` | [[image-briefs]] `### assets/npcs/teodora-sowande.png` | [[teodora-sowande]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/jarek-kovac.png` | [[image-briefs]] `### assets/npcs/jarek-kovac.png` | [[jarek-kovac]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/odile-ferraz.png` | [[image-briefs]] `### assets/npcs/odile-ferraz.png` | [[odile-ferraz]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/corin-alvarez.png` | [[image-briefs]] `### assets/npcs/corin-alvarez.png` | [[corin-alvarez]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/marisol-okonkwo.png` | [[image-briefs]] `### assets/npcs/marisol-okonkwo.png` | [[marisol-okonkwo]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/bohdan-adeyemi.png` | [[image-briefs]] `### assets/npcs/bohdan-adeyemi.png` | [[bohdan-adeyemi]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/dessa-rahimi.png` | [[image-briefs]] `### assets/npcs/dessa-rahimi.png` | [[dessa-rahimi]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/splats/bloodware.png` | [[image-briefs]] `### assets/splats/bloodware.png` | [[bloodware]] | 16:9 | — | generated |
| `assets/splats/howlers.png` | [[image-briefs]] `### assets/splats/howlers.png` | [[howlers]] | 16:9 | — | generated |
| `assets/splats/casters.png` | [[image-briefs]] `### assets/splats/casters.png` | [[casters]] | 16:9 | — | generated |
| `assets/splats/doppels.png` | [[image-briefs]] `### assets/splats/doppels.png` | [[doppels]] | 16:9 | — | generated |
| `assets/splats/baselines.png` ⚠ readable signage ("SUTURE ROW") — brief said no readable text; regenerate if strict | [[image-briefs]] `### assets/splats/baselines.png` | [[baselines]] | 16:9 | — | generated |
| `assets/jobs/breakout/breakout-02-hand-under-the-elbow.png` | [[image-briefs]] `### assets/jobs/breakout/breakout-02-hand-under-the-elbow.png` | [[breakout-02-hand-under-the-elbow]] | 16:9 | — | generated |
| `assets/jobs/breakout/breakout-03-the-wire.png` | [[image-briefs]] `### assets/jobs/breakout/breakout-03-the-wire.png` | [[breakout-03-the-wire]] | 16:9 | — | generated |
| `assets/jobs/breakout/breakout-04-the-causeway.png` | [[image-briefs]] `### assets/jobs/breakout/breakout-04-the-causeway.png` | [[breakout-04-the-causeway]] | 16:9 | — | generated |
| `assets/jobs/breakout/breakout-05-a-name-and-a-place.png` | [[image-briefs]] `### assets/jobs/breakout/breakout-05-a-name-and-a-place.png` | [[breakout-05-a-name-and-a-place]] | 16:9 | — | generated |
| `assets/jobs/breakout/breakout-07-the-counter-door.png` | [[image-briefs]] `### assets/jobs/breakout/breakout-07-the-counter-door.png` | [[breakout-07-the-counter-door]] | 16:9 | — | generated |
| `assets/jobs/investigation/investigation-03-the-cold-room.png` | [[image-briefs]] `### assets/jobs/investigation/investigation-03-the-cold-room.png` | [[investigation-03-the-cold-room]] | 16:9 | — | generated |
| `assets/jobs/investigation/investigation-04-the-mirror-rig.png` | [[image-briefs]] `### assets/jobs/investigation/investigation-04-the-mirror-rig.png` | [[investigation-04-the-mirror-rig]] | 16:9 | — | generated |
| `assets/jobs/investigation/investigation-06-the-lower-gate.png` | [[image-briefs]] `### assets/jobs/investigation/investigation-06-the-lower-gate.png` | [[investigation-06-the-lower-gate]] | 16:9 | — | generated |
| `assets/jobs/investigation/investigation-07-the-counting-room.png` | [[image-briefs]] `### assets/jobs/investigation/investigation-07-the-counting-room.png` | [[investigation-07-the-counting-room]] | 16:9 | — | generated |
| `assets/jobs/investigation/investigation-08-the-cordon.png` | [[image-briefs]] `### assets/jobs/investigation/investigation-08-the-cordon.png` | [[investigation-08-the-cordon]] | 16:9 | — | generated |
| `assets/jobs/acquisition/acquisition-03-the-scan-index.png` | [[image-briefs]] `### assets/jobs/acquisition/acquisition-03-the-scan-index.png` | [[acquisition-03-the-scan-index]] | 16:9 | — | generated |
| `assets/jobs/acquisition/acquisition-06-the-paper-barn.png` | [[image-briefs]] `### assets/jobs/acquisition/acquisition-06-the-paper-barn.png` | [[acquisition-06-the-paper-barn]] | 16:9 | — | generated |
| `assets/jobs/acquisition/acquisition-07-the-coldwater-run.png` | [[image-briefs]] `### assets/jobs/acquisition/acquisition-07-the-coldwater-run.png` | [[acquisition-07-the-coldwater-run]] | 16:9 | — | generated |
| `assets/jobs/acquisition/acquisition-08-collection-night.png` | [[image-briefs]] `### assets/jobs/acquisition/acquisition-08-collection-night.png` | [[acquisition-08-collection-night]] | 16:9 | — | generated |
| `assets/jobs/acquisition/acquisition-09-what-a-page-is-worth.png` | [[image-briefs]] `### assets/jobs/acquisition/acquisition-09-what-a-page-is-worth.png` | [[acquisition-09-what-a-page-is-worth]] | 16:9 | — | generated |
| `assets/npcs/wax.png` | [[image-briefs]] `### assets/npcs/wax.png` | [[wax]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/anselm-boateng.png` | [[image-briefs]] `### assets/npcs/anselm-boateng.png` | [[anselm-boateng]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/ivo-meszaros.png` | [[image-briefs]] `### assets/npcs/ivo-meszaros.png` | [[ivo-meszaros]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/margit-nakagawa.png` | [[image-briefs]] `### assets/npcs/margit-nakagawa.png` | [[margit-nakagawa]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/ileana-boakye.png` | [[image-briefs]] `### assets/npcs/ileana-boakye.png` | [[ileana-boakye]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/npcs/ilya-sarpong.png` | [[image-briefs]] `### assets/npcs/ilya-sarpong.png` | [[ilya-sarpong]] | 2:3 | chroma → keyed (`tools/keyout.py`) | generated |
| `assets/cover.png` | [[image-briefs]] `### assets/cover.png` | [[README]] | 16:9 | — | generated |
