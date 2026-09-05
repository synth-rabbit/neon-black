---
type: meta
name: Image Briefs
slug: image-briefs
status: review
source: custom
page: ""
owner: WP6
canon_refs: ["Plan Part F WP-I", "Bible §4", "01-series/tone.md (BC-14)", "style-guide §4", "BC-137", "BC-179"]
flags: [BUILD CHOICE]
player_safe: false
---

# Image Briefs

One self-contained prompt block per image for WP-I (Plan Part F). **Pass 1** (this file, WP6): every district, every Key Player (emblem + territory shot), every named NPC as a full-body paper puppet, and one player-facing image per splat. **Pass 2** (WP8 appends): set-piece scenes for the three jobs' core moments, the module cover, and any NPC WP7 adds. The generated files go under `assets/` and are tracked in `assets/manifest.md`; each is linked from exactly one vault file by `![[assets/...]]` (WP-I only, [[style-guide]] §8 rule 6).

**[BUILD CHOICE]** (BC-137) The conventions below — preamble values, aspect ratios, the paper-puppet specification, the `negative` line, the manifest columns — are WP6's; the shapes are Plan WP-I's. Prompts are briefs for an image model, not canon: nothing here adds a fact to a target file, and where a prompt and its target file disagree the file wins.

## Style preamble

Paste at the top of every prompt. Values finalized from [[tone]] (BC-14) and [[style-guide]] §4.

> Cyberpunk megacity illustration. Painterly concept art, grounded and worn rather than glossy: film grain, scuffed surfaces, visible seams on chrome, wet reflections, industrial scale. Palette: neon over concrete — sodium orange, arc-lamp white, bruise violet, coolant green, blood-black, wet asphalt, rust, oxidized copper; surgical teal and warranty-card cream in the corporate tiers; bone and chrome at the top. Lighting: rain-scattered, underlit, backlit by advertising, tier-shadowed; floodlit checkpoints, flickering strip light, emergency red, clinic fluorescent. The lower the tier, the fewer the colors. No readable text, no logos of real companies, no watermarks, no photoreal faces, no mythological or religious iconography, no gods, angels, demons, dragons or creatures of any culture's legend. [ASPECT]

Three variants of the last bracket:

- **Establishing shot (districts, Key Player territory):** `Wide establishing shot, 16:9. The Wall — a kilometre-high escarpment of stacked construction — reads as enormous wherever it is in frame.`
- **Emblem (Key Players):** `Flat vector emblem on a plain neutral background, a single shape, two colors, no lettering, 1:1.`
- **Paper puppet (NPCs):** `Full-body standing figure, head to feet fully in frame, facing three-quarters toward the viewer, isolated on a transparent background (PNG with alpha) — or, if transparency is unsupported, on a flat pure green #00FF00 background. No ground shadow, no scenery, no props or clothing touching the frame edge, portrait orientation 2:3.` Not a token: the figure is placed on scene art in Foundry. Face rendered painterly, not photoreal.

**Tao, when it must be shown, is density** — heat-shimmer, iron filings aligning, a shadow that falls the wrong way — never a figure, never a glow from a hand.

**Standing negative list (every block inherits it):** readable text, real brands, watermarks, legend-Mythos iconography, halos, runes, magic circles, glowing eyes, photoreal faces, clean chrome-perfect surfaces, anime brightness.

**Secret-tell rule for NPCs.** The `negative` line of a puppet names what the target file says must not show. Bloodware: no fangs, no seams, no pallor cues beyond ordinary tiredness, no red eyes. Doppels: no seams, no sculpt scars, no mask lines, no doubled features. Howlers: no beast traits — no claws, muzzle, fur, tail, slit pupils — unless the file says the shape is showing (none in pass 1). Casters: no glowing hands, no runes, no floating objects, no aura. Baselines and unmodified people: no chrome beyond what the file lists.

**Masquerade rule.** Nothing in an in-world view (district, emblem, territory shot) depicts what the Masquerade keeps hidden (Bible §3) — a Howler in the shape, a Doppel mid-change, a Bloodware feeding — except the three permitted exceptions the public already sees (arena fighters, sculpted entertainers, bodyguards visibly more than human). The five splat images are player-facing and show what each splat's own player-safe overview says a member is; NPC puppets are MC-only assets and follow the secret-tell rule instead.

---

## Districts (18) — `assets/districts/<slug>.png`, 16:9

### assets/districts/amalgam-stack.png
target: [[amalgam-stack]]
aspect: 16:9
prompt: <preamble, establishing> A vertical factory-city bolted into the cliff face of the Wall: thirty decks of foundry, assembly and worker housing hung from the rock on girders the size of streets, corporate offices at the top deck just under the plateau's lip, loading bays at the bottom opening onto the port. Open steel lift-cages run up the outside of the structure; foundry heat vents from the cliff in orange plumes; grey primer and machine oil on every surface; a shift klaxon's floodlights sweeping the decks. Tier-shadowed, sodium orange against coolant green. Mood: owned.
negative: no clean corporate tower, no glass skyscraper, no visible company name or logo.

### assets/districts/aurelian-crest.png
target: [[aurelian-crest]]
aspect: 16:9
prompt: <preamble, establishing> The top of the Wall in daylight: a ridge of terraced estates and slim white towers along a plateau's edge, gated at every road and lift-head, with the whole rain-hazed megacity laid out a kilometre below. Wind, uncovered faces, plane trees, white and gold light; at a service lift-head a line of grey-uniformed domestic staff waiting to be sent back down. Bone and chrome, warranty-card cream. Mood: never told no.
negative: no visible chrome or seams on the residents (the work is invisible because it is perfect), no slums in the foreground.

### assets/districts/chancery-hill.png
target: [[chancery-hill]]
aspect: 16:9
prompt: <preamble, establishing> A low hill set back from the plateau's edge, crowned by a stone-and-glass administrative pile older than any tower around it, with a police annex bolted onto its side like an afterthought. Colonnades, plane trees under grow-lamps, doormen visibly more than human, a lower gate with a café where people wait holding envelopes; a respectable townhouse with a walled garden and raked gravel among the ministries. Quiet, grey-gold, evening. Mood: priced.
negative: no visible crest, seal or lettering on the building; nothing to suggest the townhouse is anything but a club.

### assets/districts/cinder-yards.png
target: [[cinder-yards]]
aspect: 16:9
prompt: <preamble, establishing> Two square kilometres of dead rendering plants and reclamation sheds on the flat inland ground below the Wall: hollow sheds, rusted gantries, kiln-halls along a rail siding, and cinder flats where grey-black ash lies a metre deep. One chimney still smoking; cages that were for carcasses; a washed white van at the siding under a single gantry light; ground marks scraped in the ash. Night, one working light, blood-black and rust. Mood: pack ground.
negative: no beast figures, no wolves, no transformed bodies — only people and their ground.

### assets/districts/coldwater-outfall.png
target: [[coldwater-outfall]]
aspect: 16:9
prompt: <preamble, establishing> Where the map ends: a delta of concrete culverts, settling lagoons and sludge-flats where a megacity's drainage discharges into the sea, kilometres of it, poisoned and officially empty. On a rise of old fill in the middle distance, behind remediation-contract fences, a work camp: prefab blocks, a wire perimeter, a single causeway, floodlight towers, a yard with speakers on poles. Fog, grey water, emergency-red beacons, the Wall a faint line on the horizon. Mood: nobody's supposed to be here.
negative: no signage, no company mark on the fences, no guard towers in the classic prison style — corporate site security, not a fortress.

### assets/districts/corbel-gallery.png
target: [[corbel-gallery]]
aspect: 16:9
prompt: <preamble, establishing> A commercial arcade six kilometres long and eight storeys deep cut into the cliff face of the Wall and roofed in glass — a continuous street in the sky. Boutiques, gene-salons, implant bars and flagship showrooms under a thick AR overlay; every window a mirror that suggests an improvement; sculpted entertainers on stage screens; below the arcade, service corridors and a staff entrance at the lift-heads. Arc-lamp white, surgical teal, warranty-card cream, backlit by advertising. Mood: judged.
negative: no readable adverts or brand names — the AR is shape and color only.

### assets/districts/ferrante-basin.png
target: [[ferrante-basin]]
aspect: 16:9
prompt: <preamble, establishing> A shallow bowl four kilometres across, ringed by a twelve-metre concrete wall with a razor crown and a watchtower every three hundred metres. Inside: a district digested — buildings eaten to lace, roads that are grey dust, a landscape the color of iron filings where nothing grows; a patrol drone with a pitted casing. Outside the wall, in the towers' shadow, a fringe of squatters' shelters. Overcast, grey on grey, one Chancery broadcast screen mounted on the wall, image only. Mood: don't touch anything.
negative: no visible nanites or swarms, no glow, no monsters — the damage is old and still.

### assets/districts/foundation-galleries.png
target: [[foundation-galleries]]
aspect: 16:9
prompt: <preamble, establishing> Inside the Wall's own foundation: construction galleries, drainage tunnels, pump chambers and sealed voids between one generation's concrete and the next, running under the port districts in the dark. Water to the ankle, a century-old flood line on the walls, cable runs, a submarine-style hatch in a concrete bulkhead, one lantern. Coolant green and wet stone; the rest is black. Mood: hollow bones.
negative: no faces visible, no inhabitants shown — the refuge is hidden.

### assets/districts/gullet-market.png
target: [[gullet-market]]
aspect: 16:9
prompt: <preamble, establishing> The port-market at the foot of the Wall where the escarpment's run-off channel meets the shore: a roofed labyrinth of stalls, pawnshops, food carts and lock-ups under the girders of a factory's bottom bays and an arena's cradle, in permanent shade and permanently wet. Locks and coasters at the quay, a squat stone customs weighhouse with a water door and a market door, frying-oil smoke, coolant, sea spray; a kilometre of Wall straight up and one hour of sun at noon. Sodium orange, rust, wet asphalt. Mood: everything falls here.
negative: no clean market, no tourists; no signage.

### assets/districts/halloran-circus.png
target: [[halloran-circus]]
aspect: 16:9
prompt: <preamble, establishing> An arena hung off the cliff face in a cradle of girders — forty thousand seats around a licensed ring — its outer wall a screen the size of a district, playing a fight to the port below. Around it, casinos, fight gyms, idol stages, clubs; a crowd of corporate-warrantied and second-hand-chrome bodies mixing on purpose; a licensed fighter on the screen with visible sculpt and chrome, mods listed on a card no one can read. Loud, garish, all night: bruise violet, arc-lamp white, blood-black. Mood: the crowd wants blood.
negative: fighter's mods may show (permitted exception) but no beast traits, no fangs; no readable card or ad text.

### assets/districts/kilbride-stretch.png
target: [[kilbride-stretch]]
aspect: 16:9
prompt: <preamble, establishing> The sprawl behind the levees: kilometres of two- and three-storey prefab housing on a grid, an automat on every corner, drone lanes overhead, distribution warehouses the size of districts, a police station every ten kilometres with its doors shut. Late afternoon; the Wall a grey line on the western horizon with a glow on top, throwing its shadow across the whole sprawl. A courtyard council under a tarpaulin. Faded colors, one working streetlamp. Mood: nobody official comes down here.
negative: no neon glamour, no towers in the foreground.

### assets/districts/lowmere-sinks.png
target: [[lowmere-sinks]]
aspect: 16:9
prompt: <preamble, establishing> A district below sea level: drowned ground floors, life moved up to second storeys and rooftops, stilt-walks between blocks, boats where cars were, rooftop shanties, and a brick pump-house — the only maintained building — with its stack lit. High tide to the knee in the streets; a drowned server farm's cooling fans turning under the water; skill-chip kiosks on a rooftop. Lit by whatever still works: coolant green, one sodium lamp, rain. Mood: the pumps are running late.
negative: no pleasure-boats, no tropical light; no monsters in the water.

### assets/districts/marlow-blocks.png
target: [[marlow-blocks]]
aspect: 16:9
prompt: <preamble, establishing> Forty identical twelve-storey tenement blocks on a grid behind the port: galleries strung with washing and pirate cabling, lifts working on three blocks out of five, a courtyard that is a market by day. On the ground floor of the central block, a relief kitchen with steam over long tables, a queue at the door, a washed white van at the back, a clinic sign board with no words. Dusk, sodium orange, wet concrete, kitchen light. Mood: everyone owes.
negative: no readable signs, no logo on the van, no visible drug handover.

### assets/districts/meliora-terraces.png
target: [[meliora-terraces]]
aspect: 16:9
prompt: <preamble, establishing> A corporate campus of stepped greenhouse towers along the inland edge of the plateau, glass stacked on glass, green under grow-light at three in the morning, so that from the port below it is a soft emerald glow at the top of the Wall. Terrace housing, tower dormitories, a ground crew tending root-mats and condensation on the glass; humid, clean, warm. Coolant green and warranty-card cream against the night. Mood: grown to specification.
negative: no leaf-and-lattice mark rendered as readable branding; no laboratory horror on show.

### assets/districts/orison-reach.png
target: [[orison-reach]]
aspect: 16:9
prompt: <preamble, establishing> The seaward end of the plateau, where the Wall runs out into the water: a weapons corporation's headquarters, proving grounds and armories walled off by a second, lower palisade of its own. Blocky family barracks inside the walls, drilled and quiet; matte grey crates on a loading apron; a dawn test detonation's flash over the ranges rattling the sea; a clean parade square empty before sunrise. Arc-lamp white, grey, the sea. Mood: the guns face outward.
negative: no visible prayer word or lettering on the crates; nothing that hints at what is under the armory.

### assets/districts/relay-fields.png
target: [[relay-fields]]
aspect: 16:9
prompt: <preamble, establishing> A field of forty dead broadcast masts, three hundred metres tall, rusting on concrete pads in a grid on the flat ground east of the port — still the tallest things on the Foot. Between them, capsule housing: coffin-blocks stacked like drawers, rented by the hour, cables leaking from the towers' old infrastructure; a kid on a stack of pallets with a secondhand jack. Night, bruise violet, blue screen-light in a thousand small windows, one mast's aviation light still blinking. Mood: every kid is a hacker.
negative: no clean data-center aesthetic; no lettering on the masts.

### assets/districts/suture-row.png
target: [[suture-row]]
aspect: 16:9
prompt: <preamble, establishing> A kilometre of clinics, surgeries, pharmacies and prosthetic fitters stacked four and five storeys against the base of the cliff, with the Wall going up forever above them: warranty-service clinics on the upper floors, chop-shops at street level with their shutters half up, and basement stairs that go down into floodwater. Clinic-fluorescent light, surgical teal, suture and seam motifs in the shop fronts, a queue of second-hand chrome. Rain. Mood: stitched up, sent back out.
negative: no readable clinic names; no gore beyond an honest surgery.

### assets/districts/the-lattice.png
target: [[the-lattice]]
aspect: 16:9
prompt: <preamble, establishing> Halfway down the cliff face, a glass-and-steel plaza hung off the Wall in front of a grid of server galleries and cooling shafts cut into the rock — a mesh crosshatching the cliff. Blue server light through the glass and a cold that gets into the teeth; a central tower with a lobby like a hospital; matte response vans parked in the plaza with side doors already open; burn-scarring on two galleries from an old fire. Arc-lamp white and cold blue. Mood: someone is always listening.
negative: no company name on the vans or the tower; no visible logo.

---

## Key Players (10 × 2) — `assets/key-players/<slug>-emblem.png` 1:1, `<slug>-scene.png` 16:9

### assets/key-players/corp-a-emblem.png
target: [[corp-a]]
aspect: 1:1
prompt: <preamble, emblem> A stylized leaf worked into a lattice — a single shape in which the veins of a leaf become a warranty-card grid; coolant green on warranty-card cream.
negative: no lettering, no caduceus or medical cross, no DNA helix.

### assets/key-players/corp-a-scene.png
target: [[corp-a]]
aspect: 16:9
prompt: <preamble, establishing> Meliora's ground: the greenhouse towers of [[meliora-terraces]] seen from a terrace walkway at three in the morning, green under grow-light, glass condensation running, a gloved technician setting down a sealed sample case with a warm wooden handle beside a row of root-mats; far below, the port in the dark. Soil and antiseptic. Mood: settled.
negative: no lettering; no laboratory horror; nothing that shows what the field kits collect.

### assets/key-players/corp-b-emblem.png
target: [[corp-b]]
aspect: 1:1
prompt: <preamble, emblem> A brass serial plate reduced to a single shape: a rounded rectangle with four stamped marks, the fourth struck deeper than the rest; matte grey on brass.
negative: no lettering or numerals that can be read, no crosshairs, no eagle.

### assets/key-players/corp-b-scene.png
target: [[corp-b]]
aspect: 16:9
prompt: <preamble, establishing> Orison's ground: the loading apron of the Reach Armory at dawn — matte grey crates with a stencilled mark, sealed cases being returned unopened with a receipt, gloved hands, a clean drilled quiet where a factory should be loud; a test detonation's flash on the ranges beyond the inner palisade rattling the windows. Grey, brass, sea-light. Mood: sealed.
negative: no readable stencil; no glimpse of the sealed shop; no Tao density effects.

### assets/key-players/corp-c-emblem.png
target: [[corp-c]]
aspect: 1:1
prompt: <preamble, emblem> An ampersand fused with a column of figures — a single shape in which the ampersand's loops read as a ledger column that balances; grey primer on foundry orange.
negative: no lettering beyond the ampersand shape itself, no gear or robot-arm cliché.

### assets/key-players/corp-c-scene.png
target: [[corp-c]]
aspect: 16:9
prompt: <preamble, establishing> AP&I's ground: a mass-fitting theater in [[amalgam-stack]] — two hundred bays under one vault running three shifts, a shift klaxon's light, grey primer and machine oil, foundry heat off the cliff behind; in the foreground a warranty tag going under the skin of a forearm, a technician's gloved hand steady. Sodium orange, surgical teal. Mood: in good standing.
negative: no lettering on the tag; no camp, no wire — the Stack shows nothing of the Outfall.

### assets/key-players/upstart-emblem.png
target: [[upstart]]
aspect: 1:1
prompt: <preamble, emblem> A single unbroken line that forms a serial-number bar and then continues as a pen stroke — one shape, matte soft-shell grey on cold server blue.
negative: no lettering, no shield, no cross, no flame.

### assets/key-players/upstart-scene.png
target: [[upstart]]
aspect: 16:9
prompt: <preamble, establishing> Continuity's ground: the plaza of [[the-lattice]] at night — blue server light through the glass, a lobby like a hospital, a response van with the side door already open and a cell in matte soft-shell armor with serial plates and no logo stepping down, clean hands and a pen on a clipboard at the cordon. Cold blue, arc-lamp white, a cold that gets into the teeth. Mood: for the duration.
negative: no company name; no faces in detail; nothing that hints who runs the firm.

### assets/key-players/syndicate-emblem.png
target: [[syndicate]]
aspect: 1:1
prompt: <preamble, emblem> A ladle whose bowl is a plain envelope — one shape, pencil grey on kitchen cream.
negative: no lettering, no skull, no dagger, no crossed anything.

### assets/key-players/syndicate-scene.png
target: [[syndicate]]
aspect: 16:9
prompt: <preamble, establishing> The Almoners' ground: the Marlow Relief Kitchen's long tables under steam, grey aprons and clean hands serving two hundred people at once, a ledger written in pencil open on the counter, a plain envelope handed across with both hands, a washed white van at the back door. Warm kitchen light against the tenement dark of [[marlow-blocks]]. Mood: settle up.
negative: no visible drugs, no dose, no violence; no readable sign.

### assets/key-players/government-emblem.png
target: [[government]]
aspect: 1:1
prompt: <preamble, emblem> Two overlapping seals in two inks on one shape — a stamped circle over a stamped circle, slightly misaligned; stone grey and registry red on paper cream.
negative: no lettering, no crest, no scales of justice, no eagle.

### assets/key-players/government-scene.png
target: [[government]]
aspect: 16:9
prompt: <preamble, establishing> The Chancery's ground: the registry basement under [[chancery-hill]] — paper shelves to the ceiling because paper cannot be Harnessed, a clerk holding a page flat under a desk lamp, a second identical shelf half-visible behind a door; above, through a light-well, the atrium queue of people holding envelopes. Stone, dust, lamp light, two inks. Mood: priced.
negative: no readable documents; no flag or crest.

### assets/key-players/tao-society-emblem.png
target: [[tao-society]]
aspect: 1:1
prompt: <preamble, emblem> Raked gravel lines around a single circle where an old tree stands — one shape: concentric strokes interrupted by one point; charcoal grey on unbleached paper.
negative: no lettering, no yin-yang, no hexagram, no mystical symbol of any tradition.

### assets/key-players/tao-society-scene.png
target: [[tao-society]]
aspect: 16:9
prompt: <preamble, establishing> The Wuji's ground: the walled garden of a respectable house on [[chancery-hill]] before dawn — forty people in grey moving slowly in unison on raked gravel around one old tree, gloves on, a reading room with no terminals lit behind the windows, a page being copied by hand at a desk. Pre-dawn grey, one warm window. Nothing supernatural in frame. Mood: containment.
negative: no glow, no aura, no runes, no floating anything — Tao is never shown as a figure or a light.

### assets/key-players/packs-emblem.png
target: [[packs]]
aspect: 1:1
prompt: <preamble, emblem> A smoking chimney drawn as one stroke, its smoke the curve of a leash — one shape, ash black on cinder grey.
negative: no lettering, no wolf head, no paw print, no moon.

### assets/key-players/packs-scene.png
target: [[packs]]
aspect: 16:9
prompt: <preamble, establishing> The Run's ground: a kiln-hall on the rail siding in [[cinder-yards]] at night — a dose counted out on a crate under gantry lights, cages that were for carcasses, ash a metre deep outside the door, a chimney still smoking, sculpt healing under a strip light in the back, a whole street beyond the fence deciding not to look. Blood-black, rust, one gantry lamp. Mood: pack ground.
negative: no beast shapes, no fur, no claws — people with old visible chrome, nothing more.

### assets/key-players/changeling-cells-emblem.png
target: [[changeling-cells]]
aspect: 1:1
prompt: <preamble, emblem> A submarine hatch wheel seen face-on, opening from the inside — one shape, wet-iron grey on black.
negative: no lettering, no mask, no two-faces motif.

### assets/key-players/changeling-cells-scene.png
target: [[changeling-cells]]
aspect: 16:9
prompt: <preamble, establishing> The Cutloose's ground: a concrete hall deep in [[foundation-galleries]] behind a submarine hatch — a wall covered in faces drawn from memory, none of them matching; bedrolls; a pump alarm's red lamp; thirty people each wearing their own face and finding it strange; water on the floor. Lantern light, coolant green, black. Mood: the queue.
negative: no seams, no sculpt scars, no half-changed faces; the drawn faces on the wall are sketches, not portraits of anyone.

### assets/key-players/fence-network-emblem.png
target: [[fence-network]]
aspect: 1:1
prompt: <preamble, emblem> A brass balance reduced to one shape — beam, two pans, and a chalk tally mark where the pointer should be; brass on slate.
negative: no lettering, no coin, no scales-of-justice styling.

### assets/key-players/fence-network-scene.png
target: [[fence-network]]
aspect: 16:9
prompt: <preamble, establishing> Tally's ground: inside the old customs weighhouse on the [[gullet-market]] quay — the brass balance under the roof still working, a chalk column on a slate by the counter door, a paper chit with a thumbprint pressed into wax on the counter, the water door open onto the locks, wet stone, frying oil, coolant, the sea. Sodium orange and brass. Mood: counted.
negative: no readable chalk figures; no guns on the counter.

---

## NPCs (23) — `assets/npcs/<slug>.png`, 2:3 paper puppets

Every block inherits the paper-puppet preamble variant and the secret-tell rule. `negative` lists what the target file says must not show.

### assets/npcs/solenne-marchetti.png
target: [[solenne-marchetti]]
aspect: 2:3
prompt: <preamble, puppet> A woman in her sixties, sculpted so competently that the only tell is how well she moves; the same soft grey coat she wears everywhere including the Crest; a warm-handled sealed sample case set down at her feet beside her like a dog; a surgeon's stillness, one hand slightly raised as if describing a good outcome. Mood: airtight.
negative: no visible seams, ports or chrome; no lab coat; no lettering on the case.

### assets/npcs/ondine-ferreira.png
target: [[ondine-ferreira]]
aspect: 2:3
prompt: <preamble, puppet> A woman of thirty-four, corporate-warrantied and unhurried, in a white outreach coat with a small leaf-and-lattice mark on the pocket, a clinic bag on a strap, chlorine tablets and dressings in the pockets, a barcode-tagged sample case in one hand; a face that is good with children and better with the elderly. Mood: gentle.
negative: no readable mark on the coat; no syringe brandished; no chrome.

### assets/npcs/adaeze-ferreira.png
target: [[adaeze-ferreira]]
aspect: 2:3
prompt: <preamble, puppet> A small woman of sixty in a grey suit, gloved indoors, flat courtesy in the set of the mouth, a thin file under one arm, standing perfectly still on a level floor as if before dawn on an empty parade square. Mood: contained.
negative: no glowing hands, no runes, no aura, no heat-shimmer; nothing that reads as a practitioner; no weapon.

### assets/npcs/reidar-solano.png
target: [[reidar-solano]]
aspect: 2:3
prompt: <preamble, puppet> A broad, blunt man of forty, ex-range crew promoted through logistics: executive shirt with the sleeves rolled, a range-crew jacket over it, a thick document folder under his arm, brand-loyal watch, the stance of a man who drinks with his shift managers. Mood: robbed.
negative: no chrome, no sidearm on show, no lettering on the folder.

### assets/npcs/priya-halstead.png
target: [[priya-halstead]]
aspect: 2:3
prompt: <preamble, puppet> A woman of forty-five, immaculate and entirely pleasant, top-deck executive tailoring in warranty-card cream, a tablet held like a ledger; the politeness of someone destroying an account. Mood: reconciled.
negative: no lettering on the tablet; no visible camp insignia; no obvious cybernetics.

### assets/npcs/rasheeda-novak.png
target: [[rasheeda-novak]]
aspect: 2:3
prompt: <preamble, puppet> A tired woman of thirty-one in grade-three office clothes with the company interface port every Stack employee wears just visible at the base of the skull above the collar, an ID lanyard with no readable text, a stack of open files held against her chest, a coffee, and the look of someone re-pricing something in her head. Mood: thorough.
negative: no readable file labels; no weapon; no glamour.

### assets/npcs/vera-solano.png
target: [[vera-solano]]
aspect: 2:3
prompt: <preamble, puppet> A narrow grey woman of sixty in a company coat pressed every day for nineteen years, a clipboard with a count on it, a hand-held speaker microphone on a cord, standing as if reading numbers to a yard and leaving a silence after them. Mood: nought.
negative: no readable numbers; no whip, no baton, no cruelty cues — she is fair.

### assets/npcs/hanne-oyelaran.png
target: [[hanne-oyelaran]]
aspect: 2:3
prompt: <preamble, puppet> A tall woman in her late thirties, close-cropped grey-blonde hair, matte soft-shell armor with a serial plate on the chest and no name anywhere, helmet held under one arm, a breaching frame slung, a replacement left eye of trauma-grade quality and nothing else modified; a paramedic's *look at me* expression. Mood: secured.
negative: no readable serial; no logo; no sculpt or bio-work; no chrome beyond the eye.

### assets/npcs/rosalind-ekwueme.png
target: [[rosalind-ekwueme]]
aspect: 2:3
prompt: <preamble, puppet> A woman who is fifties in the face in the way of somebody who chose that: grey wool, no jewellery, reading glasses held as punctuation, a paper diary in one hand, continuity-of-service papers in the other, an expression of enormous sympathy. Mood: helping.
negative: no fangs, no pallor beyond ordinary, no red eyes, no seams, nothing that hints at nanites; no chrome.

### assets/npcs/tomas-adair.png
target: [[tomas-adair]]
aspect: 2:3
prompt: <preamble, puppet> A man who looks forties and has for a while: heavy through the shoulders, hands like a man who has unloaded things for a living, a broken nose set by someone who was not a surgeon, camp coveralls with a number patch on the back and the sleeves pushed up, weight settled, saying nothing. Mood: underestimated.
negative: no fangs, no pallor cues, no seams, no red eyes, no visible chrome; the number patch is not readable; nothing that hints at what he is or why he matters.

### assets/npcs/bettina-alarcon.png
target: [[bettina-alarcon]]
aspect: 2:3
prompt: <preamble, puppet> A broad-shouldered Patched woman in her fifties, second-hand chrome showing where the sleeves are permanently rolled, a grey kitchen apron, a long-handled ladle in one hand and a pencil ledger in the other, a voice built for a room of two hundred in the set of her jaw. Mood: the Ladle.
negative: no readable ledger; no weapon; no drugs in frame.

### assets/npcs/halina-ansah.png
target: [[halina-ansah]]
aspect: 2:3
prompt: <preamble, puppet> A small, still woman in her sixties dressed like a solicitor's clerk, corporate-warrantied and neat, a plain manila form held flat, a kettle-warm cardigan under a dark coat, the underwriter's calm of someone who thinks of people as a portfolio. Mood: First Alms.
negative: no readable form; no jewellery of office; no chrome on show.

### assets/npcs/halima-boyce.png
target: [[halima-boyce]]
aspect: 2:3
prompt: <preamble, puppet> A physically unremarkable police superintendent in her late forties, twenty-two years on the force in the way she stands, plain annex-desk uniform without visible insignia, a numbered page — a concurrence — in one hand, reading glasses pushed up, precise and technically clean. Mood: noticing the shape.
negative: no readable page or badge number; no sidearm drawn; no chrome.

### assets/npcs/emeric-vann.png
target: [[emeric-vann]]
aspect: 2:3
prompt: <preamble, puppet> A tidy, tired man in his fifties, a good coat kept fifteen years, warranty-grade chrome a decade out of service showing dull at one cuff, registry dust on the cuffs, an envelope half-in a pocket, holding a page flat with both hands as if reading at a shelf. Mood: somewhere else when it comes out.
negative: no readable page; no glamour; nothing more than the one dulled, unserviced implant.

### assets/npcs/constance-marchetti.png
target: [[constance-marchetti]]
aspect: 2:3
prompt: <preamble, puppet> A small, plainly dressed woman in her seventies, gloved indoors, a club steward's cardigan and skirt, a calendar-book under one arm, a voice that does not rise in the set of her face; deliberately the least interesting person in any room. Mood: administrative.
negative: no glowing hands, no runes, no aura, no staff, no robes, nothing mystical; no chrome.

### assets/npcs/nasrin-vogel.png
target: [[nasrin-vogel]]
aspect: 2:3
prompt: <preamble, puppet> A woman of thirties or forties, hard to place, dressed like a physiotherapist — soft jacket, practical shoes — warm in a way that is not performed, a paper bag of takeaway food in one hand as if about to buy someone a meal, weight easy on both feet. Mood: good company.
negative: no glowing hands, no runes, no aura, nothing that reads as a practitioner; no chrome; no weapon.

### assets/npcs/teodora-sowande.png
target: [[teodora-sowande]]
aspect: 2:3
prompt: <preamble, puppet> A heavy woman of forty-one, grey at the temples, slow-moving in daylight, old visible chrome she has never had prettied up — anchor plates along the shoulders and hips under a work vest, a jaw line that does not quite match — cinder ash on her boots, an envelope in one hand held without looking at it. Mood: arbiter.
negative: no beast traits — no claws, muzzle, fur, tail or slit pupils; not in the shape; no readable envelope.

### assets/npcs/jarek-kovac.png
target: [[jarek-kovac]]
aspect: 2:3
prompt: <preamble, puppet> A man of thirty who looks younger, in a good cheap jacket, carrying somebody else's shopping bags up eleven flights, a friendly face already making the joke before the mothers can, sculpt visible only as a build too capable for the street he stands on. Mood: Uncle.
negative: no beast traits — no claws, muzzle, fur, tail or slit pupils; not in the shape; no dose or vial visible.

### assets/npcs/odile-ferraz.png
target: [[odile-ferraz]]
aspect: 2:3
prompt: <preamble, puppet> A short, careful woman who looks forty, quiet-voiced, in layered under-Wall clothes still damp at the hem, a folded list held closed in one hand that she does not show, the flat unhurried competence of someone deciding which of two people gets the surgery. Mood: Six.
negative: no seams, no sculpt scars, no mask lines, no doubled features; the old scars at the skull base and shoulder blade are covered; no readable list.

### assets/npcs/corin-alvarez.png
target: [[corin-alvarez]]
aspect: 2:3
prompt: <preamble, puppet> A woman who looks mid-twenties and unremarkable, which is the point: borrowed clothes, a blanket around the shoulders, a strip of surgical tape just visible at the base of the skull under the collar, sleeping badly in the set of the eyes, standing as if still waiting to be told what to do. Mood: eleven days out.
negative: no seams, no sculpt scars, no mask lines, no doubled or shifting features; nothing that reads as a mask.

### assets/npcs/marisol-okonkwo.png
target: [[marisol-okonkwo]]
aspect: 2:3
prompt: <preamble, puppet> A broad, slow-moving woman of sixty-odd in a canvas apron with brass dust on it, grey hair cut short by herself, one cheap prosthetic eye never upgraded, hands that can tell chrome grade by weight, a piece of chalk in one hand and a kitchen-table manner. Mood: counted.
negative: no gun; no glamorous cybernetics — the eye is cheap and obvious; no readable chalk.

### assets/npcs/bohdan-adeyemi.png
target: [[bohdan-adeyemi]]
aspect: 2:3
prompt: <preamble, puppet> An enormous docker of forty, chest and shoulders built by twenty-five years of unloading coasters rather than bought, a replacement left hand of plain functional make and a stiff hip, quay-wet jacket, a counterweight from a brass balance held loosely, waiting after a warning given once in a normal voice. Mood: the doorway empties.
negative: no sculpt, no bio-work, no chrome beyond the hand; no weapon.

### assets/npcs/dessa-rahimi.png
target: [[dessa-rahimi]]
aspect: 2:3
prompt: <preamble, puppet> A small, fast woman of twenty-four, permanently damp, in a cut-down docker's jacket with the pockets resewn into a dozen smaller ones, a wax-sealed paper chit between two fingers, mid-stride and grinning, eighteen months from something reckless. Mood: Chit.
negative: no chrome; no readable chit; no weapon.

---

## Splats (5) — `assets/splats/<slug>.png`, 16:9, player-facing

These are for the session-zero packet: they show what the packet's player-safe text shows and nothing MC-only.

### assets/splats/bloodware.png
target: [[bloodware]]
aspect: 16:9
prompt: <preamble, establishing> A body rebuilt from the marrow out: a figure at a scrapyard bench at night pressing a palm to a rusted beam, iron filings rising through the skin like a bruise that moves, the rust going pale where the hand rests; behind them the twelve-metre wall of a quarantine district and its watchtowers. A hundred years of getting out, one body at a time. Blood-black, rust, oxidized copper. Mood: hungry.
negative: no fangs, no cape, no coffin, no bat, no sunlight-burning, no crucifix, no garlic — none of the folklore.

### assets/splats/howlers.png
target: [[howlers]]
aspect: 16:9
prompt: <preamble, establishing> A body rebuilt to become something else and a chemical that tells it when: a sculpted figure on the cinder flats at night, mid-change, the sculpt tearing open along old anchor lines as the dose takes, chrome showing where it was never meant to be seen; an ampoule case open on a crate; the pack a few metres off, waiting. Ash, gantry light, blood-black. Mood: leashed.
negative: no wolf, no fur, no silver, no full moon iconography — this is sculpt and chrome under a drug, not a werewolf of legend.

### assets/splats/casters.png
target: [[casters]]
aspect: 16:9
prompt: <preamble, establishing> A pure practitioner in a chop-shop back room at the base of the Wall: an unremarkable person keeping a discipline over a bench of ordinary tools, and the Tao shown only as density — heat-shimmer over a soldering iron, iron filings on the bench aligning to no magnet, a shadow that falls the wrong way. Nothing glows. Clinic fluorescent, coolant green. Mood: rare.
negative: no glowing hands, no runes, no magic circles, no floating objects, no staff or robes, no aura, no god or spirit figure.

### assets/splats/doppels.png
target: [[doppels]]
aspect: 16:9
prompt: <preamble, establishing> A body rewritten to be somebody else's: a figure at a mirror in a warranty clinic fitting room, the reflection's face a stranger's and the face in the room already becoming it, seamlessly, no mask — while on a tray beside them a tracker unit and a small switch housing wait in a kidney dish. Surgical teal, mirror light. Mood: owned or free.
negative: no seams, no peeling mask, no sculpt scars, no melting face, no doubled features — the change is total and clean.

### assets/splats/baselines.png
target: [[baselines]]
aspect: 16:9
prompt: <preamble, establishing> The one who stayed human: a bounty hunter and a street medic in a Suture Row clinic doorway, one with a plain functional replacement arm and nothing else, the other with nothing at all, surrounded by a queue of bought bodies and sculpted work, holding the line by choice. Rain, clinic fluorescent, one working streetlamp. Mood: the line is worth keeping.
negative: no sculpt, no bio-work, no chrome beyond the one plain replacement; no heroics, no crusader iconography.

---

## Pass 2 (WP8) — job scenes, job NPCs, the cover

**[BUILD CHOICE]** (BC-179) Fifteen scene blocks (the core moments, climaxes and named set pieces of the three jobs; 16:9, establishing variant, the `![[...]]` embed goes in the scene file), six paper puppets for the job-only NPCs (BC-174; 2:3, puppet variant, secret-tell rule as pass 1), and the module cover (16:9 for WP9's `module.json`; no readable text anywhere in it). The Masquerade rule holds for every scene: nothing shows a shape, a feeding or a face changing; the Ledger scenes are MC-only assets and may show the camp.

### Job 0 scenes — `assets/jobs/breakout/<scene-slug>.png`, 16:9

### assets/jobs/breakout/breakout-02-hand-under-the-elbow.png
target: [[breakout-02-hand-under-the-elbow]]
aspect: 16:9
prompt: <preamble, establishing> A work-camp yard at night between a dormitory block and a row of sheds, black except for hand torches and one distant floodlit gate; a hundred people in grey camp fatigues running toward the far light; against them, at a walk, six figures in matte grey soft-shell with a serial where a name would be, and at the front of them one gloved hand placed under the elbow of a man in the same grey fatigues as everyone else. Rain, sludge underfoot, torch beams crossing. Mood: gentle, and wrong.
negative: no visible company name, no insignia, no wounds on the man being taken, no weapon raised.

### assets/jobs/breakout/breakout-03-the-wire.png
target: [[breakout-03-the-wire]]
aspect: 16:9
prompt: <preamble, establishing> A shed row and a perimeter fence at night on sludge flats: a cut gap in the wire held open by two figures in grey soft-shell, a guard post on a barge apron by black water with a skiff tied below it, a half-built fifth block with its fence unfinished, and behind the sheds a generator shed with a diesel turning over — one exhaust plume, one flicker of a floodlight that has not yet decided to come back. Sodium and torchlight. Mood: three ways out and a clock.
negative: no daylight, no floodlights fully on, no visible lettering on the sheds.

### assets/jobs/breakout/breakout-04-the-causeway.png
target: [[breakout-04-the-causeway]]
aspect: 16:9
prompt: <preamble, establishing> A raised causeway three kilometres long across drowned flats, seen from the camp end: a gate down across it, a flatbed truck held on the far side with its engine running, a crowd in grey fatigues pressed against the gate, floodlights on masts at the near end and nothing but dark beyond — and on the horizon, kilometres off, the glow along the top of the Wall. Haze over the lagoons, a drone's running light in it. Mood: the dark is where the Under begins.
negative: no city detail on the horizon beyond a glow, no readable signage on the gate.

### assets/jobs/breakout/breakout-05-a-name-and-a-place.png
target: [[breakout-05-a-name-and-a-place]]
aspect: 16:9
prompt: <preamble, establishing> A coast-road turn at the dark end of a causeway before dawn: a grey van across the road with its side door already open and figures in grey soft-shell loading into it; beside it one man in camp fatigues standing still, turned back toward a handful of people in the same fatigues twenty metres off; the sea one side, sludge flats the other, one working streetlight. Mood: a name and a place.
negative: no company markings on the van, no visible faces in detail, nothing that shows whether the man gets in.

### assets/jobs/breakout/breakout-07-the-counter-door.png
target: [[breakout-07-the-counter-door]]
aspect: 16:9
prompt: <preamble, establishing> The second hour of the morning on a port quay under the Wall: a stone customs weighhouse with a water door open on black river and a counter door open on a wet market street, a brass balance under the roof still swinging, a very large man filling the water door, a chalk slate by the counter door with figures on it, and through the back room's doorway a lit table with food on it. Mood: counted.
negative: no readable chalk, no signage, no daylight.

### Job 1 scenes — `assets/jobs/investigation/<scene-slug>.png`, 16:9

### assets/jobs/investigation/investigation-03-the-cold-room.png
target: [[investigation-03-the-cold-room]]
aspect: 16:9
prompt: <preamble, establishing> A street-level chop-shop on a flooded medical street: three surgical bays behind a hand-painted sign, four centimetres of floodwater in the corridor, a fitter's bench, a kettle, and a chest freezer standing open as a morgue with a body on the table beside it — a forearm turned up, a small subdermal tag under the skin lit by a bench reader's glow. Surgical teal over rust and wet concrete. Mood: still answering.
negative: no gore beyond a clinical incision, no readable sign text, no fangs or feeding.

### assets/jobs/investigation/investigation-04-the-mirror-rig.png
target: [[investigation-04-the-mirror-rig]]
aspect: 16:9
prompt: <preamble, establishing> A coffin-block stack at night under a dead relay mast: ten storeys of two-metre capsules stacked like drawers, every door shut, ladders and cabling up the outside, one capsule open on a rig of second-hand hardware with a screen showing a badly indexed list and a cached search string somebody else ran. Coolant green, arc-lamp white, rain on the mast. Mood: already in the file.
negative: no readable text on the screen, no holograms, no glowing Tao effects.

### assets/jobs/investigation/investigation-06-the-lower-gate.png
target: [[investigation-06-the-lower-gate]]
aspect: 16:9
prompt: <preamble, establishing> The lower gate of a government hill where the hill road meets a ring road and a lift-head: a police checkpoint, a row of permit-assistance kiosks, and a café with outdoor tables where clerks in good old coats take envelopes over coffee in the open; on one table two nearly identical registry pages side by side, each with a wax seal in a different ink, and a tired deputy registrar turning the second one round. Grey-gold evening. Mood: two seals, different inks.
negative: no readable text on the pages, no crest or lettering on the building.

### assets/jobs/investigation/investigation-07-the-counting-room.png
target: [[investigation-07-the-counting-room]]
aspect: 16:9
prompt: <preamble, establishing> A converted automat unit in a prefab sprawl behind a bonded door: a weigh-in desk with honest counter scales and a lamp, four hundred paper bundles wrapped in oilcloth on numbered steel shelves, a haulier's booking sheet pinned by the door, and a tall man in his sixties in a good brushed coat with reading glasses on a cord doing the accounts, unsurprised. Sodium light through a shutter. Mood: nothing here is his.
negative: no readable numbers on the shelves, no weapon in the man's hands, no visible company name.

### assets/jobs/investigation/investigation-08-the-cordon.png
target: [[investigation-08-the-cordon]]
aspect: 16:9
prompt: <preamble, establishing> A prefab street in the sprawl at night: a grey van with its side door already open where nothing was parked a minute ago, figures in matte grey soft-shell running tape across the street, and a second vehicle's headlights arriving from the other end with two uniformed officers stepping out holding a sheet of paper — two lawful forces, one address, and a crowd at the windows. Mood: whose room this is.
negative: no company markings, no readable paper, no shot fired.

### Job 2 scenes — `assets/jobs/acquisition/<scene-slug>.png`, 16:9

### assets/jobs/acquisition/acquisition-03-the-scan-index.png
target: [[acquisition-03-the-scan-index]]
aspect: 16:9
prompt: <preamble, establishing> A server hall cut into the rock of the Wall: half a kilometre of racks in blue light receding into cold haze, cooling shafts overhead big enough to walk in, frost on the handrails, and a small maintenance crew in insulated coats at a scanning bay where a rented flatbed scanner feeds a rack — overlaid faintly, as the Nearspace would show it, an index growing one volume at a time. Cold blue, arc white. Mood: someone is always listening.
negative: no cyberspace fantasy imagery, no avatars, no readable screen text, no glowing figures.

### assets/jobs/acquisition/acquisition-06-the-paper-barn.png
target: [[acquisition-06-the-paper-barn]]
aspect: 16:9
prompt: <preamble, establishing> A leased bay in a distribution warehouse so large the far end has its own weather: drone-lanes crossing overhead every few seconds, a loading apron under sodium light, a roller door with a painted seal stencil, and inside it four hundred metres of steel shelving with buckram spines going back sixty years, a rented arc-lamp gantry throwing hard shadow down one run, a scanning crew of six on a night shift, and a welded-mesh cage at the end of a run with certified volumes inside. Mood: never been robbed because nobody wanted anything in it.
negative: no readable seal or spine lettering, no visible company name.

### assets/jobs/acquisition/acquisition-07-the-coldwater-run.png
target: [[acquisition-07-the-coldwater-run]]
aspect: 16:9
prompt: <preamble, establishing> The bonded cage at the end of a shelving run in a records warehouse: welded mesh, a broken seal hanging from the lock, an arc-lamp gantry three runs away throwing everything into hard shadow, and one buckram volume open flat on a steel shelf with five people standing around it not moving — one hand flat on the page. Sodium and arc white, dust in the beam. Mood: the night was bought in advance.
negative: no readable text on the page, no faces in detail, no weapons drawn.

### assets/jobs/acquisition/acquisition-08-collection-night.png
target: [[acquisition-08-collection-night]]
aspect: 16:9
prompt: <preamble, establishing> A warehouse loading apron at four in the morning under sodium light: a records-contractor van reversing up to a roller door on the wrong night, a second crew's figures at the apron's edge with a handcart and bonded transit boxes, and beyond the fence four kilometres of identical prefab grid to the glow of the Wall — drone-lanes overhead, wet concrete, breath in the cold. Mood: thieves on roads.
negative: no company plate or lettering, no shot fired, no beast shapes or inhuman feats visible.

### assets/jobs/acquisition/acquisition-09-what-a-page-is-worth.png
target: [[acquisition-09-what-a-page-is-worth]]
aspect: 16:9
prompt: <preamble, establishing> A garden bench in the grounds of a government hill at dusk, plane trees under grow-lamps, raked gravel, the lit ministries behind: a woman in a career officer's plain coat sitting very straight with a single registry page in her hands, having stopped talking, and across from her a handful of people in Foot clothes who do not belong on the Hill and know it. Grey-gold, quiet. Mood: one thing, not both.
negative: no readable text on the page, no uniform insignia, no crest on the buildings.

### Job NPCs (6) — `assets/npcs/<slug>.png`, 2:3, paper puppets

### assets/npcs/wax.png
target: [[wax]]
aspect: 2:3
prompt: <preamble, puppet> A runner of twenty, fast and slight, in a docker's jacket with the pockets resewn to hold paper chits flat, a Patched replacement leg and shoulder assembly of second-hand make that show at the seams, one cheap prosthetic eye, hair tied back wet, a wax-sealed chit in one hand, caught mid-turn as if late. Mood: nine days.
negative: no wounds — she is shown alive, as the crew may have met her; no readable chit; no weapon.

### assets/npcs/anselm-boateng.png
target: [[anselm-boateng]]
aspect: 2:3
prompt: <preamble, puppet> A tall man in his sixties in a good dark coat kept brushed, reading glasses on a cord, close-cut grey hair, a leather folio of accounts under one arm, hands folded, the posture of a man who has never been in a room when it went badly and does not expect to start now. Mood: on commission.
negative: no weapon, no chrome, no readable paper.

### assets/npcs/ivo-meszaros.png
target: [[ivo-meszaros]]
aspect: 2:3
prompt: <preamble, puppet> A chop-shop surgeon in his fifties in a stained apron over a jumper, rubber boots wet to the ankle, a Patched left hand of visibly home-built make, a chipped mug of tea in the good hand, a bench reader hanging from his neck on a strap, tired and unbothered. Mood: asks nothing.
negative: no gore, no readable sign, no glamorous cybernetics — the hand is a kitchen build.

### assets/npcs/margit-nakagawa.png
target: [[margit-nakagawa]]
aspect: 2:3
prompt: <preamble, puppet> A solicitor's clerk in her thirties, brisk, expensive shoes and a cheap coat over them, hair pinned, a hard-shell document box under one arm, an index card held ready to be read from, the face of someone who has learned to look like a partner and is nervous anyway. Mood: no questions that begin with who.
negative: no chrome, no readable card, no weapon.

### assets/npcs/ileana-boakye.png
target: [[ileana-boakye]]
aspect: 2:3
prompt: <preamble, puppet> A records assistant in her late twenties in a contractor's fleece and a laminated badge on a lanyard that she is turning over in one hand, insulated gloves in a pocket, a shelf list folded in the other hand, tired, careful, looking slightly past the viewer toward a door. Mood: her name on nothing.
negative: no chrome, no readable badge or list, no weapon.

### assets/npcs/ilya-sarpong.png
target: [[ilya-sarpong]]
aspect: 2:3
prompt: <preamble, puppet> A man in his forties with a docker's build and a clerk's manners: a Fitted body with neat warranty-grade implants at the wrists, a records-contractor's hi-vis over a good shirt, driving gloves, one hand resting on the handle of an old iron-wheeled barrow he still keeps, calm, about to make a fair offer. Mood: thieves on roads.
negative: no weapon in hand (it is in the van), no company plate or readable lettering.

### Cover — `assets/cover.png`, 16:9

### assets/cover.png
target: [[README]]
aspect: 16:9
prompt: <preamble, establishing> The Wall at night from the Under looking up: a kilometre-high escarpment of stacked construction, neon over concrete, tier lights climbing to a bone-and-chrome crest against a bruise-violet sky; in the foreground on a drowned causeway five small figures in grey camp fatigues walking away from the viewer toward the glow, one of them looking back. Rain, sodium orange, coolant green, wet reflections. Mood: neon black.
negative: absolutely no readable text, title or lettering anywhere (the title is set by the module page, not the image); no logos; no faces in detail; nothing that shows any of the five's nature.

---

## What pass 3 would append

Nothing is planned. If a later package adds a district, a Key Player, an NPC or a job, it appends a block here under the same rules and a row to `assets/manifest.md`.
