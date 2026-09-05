#!/usr/bin/env python3
"""Validate `build/packs/**/_source/*.json` against the city-of-mist data models.

    python3 tools/foundry/check.py               # check build/
    python3 tools/foundry/check.py --out build   # same
    python3 tools/foundry/check.py --verbose     # list every finding, not a summary

Exit code 1 if any ERROR is reported. This is a static check of the emitted
`_source` JSON: it re-implements, by hand, the field lists that the system's
TypeScript data models declare, and reports fields that are **missing**, **extra**
or **mistyped** relative to them, plus the enum/shape constraints those models put
on values.

The field lists below are transcribed from a shallow clone of
https://github.com/taragnor/city-of-mist at v4.5.3, under
`src/city-of-mist/module/datamodel/`. Every list cites the file and line range it
came from, so it can be re-checked against a newer system release by opening those
lines. `defineSchema()` returns exactly the keys a document's `system` object may
carry: anything else is dropped by Foundry on import (an "extra" finding here),
and anything missing falls back to the field's `initial` (a "missing" finding).
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ID_RE = re.compile(r"^[A-Za-z0-9]{16}$")

# ===========================================================================
# Field lists, transcribed from the datamodel sources.
# Value is a type token: s=str, b=bool, n=number(int), h=html(str), a=array,
# o=object, id=DocumentIdField (16-char id, null or "" allowed).
# ===========================================================================

# item-types.ts:68-74  defaultItem()
DEFAULT_ITEM = {"description": "h", "locked": "b", "version": "s"}
# item-types.ts:76-83  systemItem()
SYSTEM_ITEM = {"free_content": "b", "locale_name": "s", "systemName": "s", "sourceBook": "s"}

SCHEMAS = {
    # item-types.ts:119-137  class Themekit
    "themekit": dict(DEFAULT_ITEM, **SYSTEM_ITEM, **{
        "themebook_id": "id", "themebook_name": "s", "use_tb_improvements": "b",
        "power_tagstk": "a", "weakness_tagstk": "a", "improvements": "a",
        "motivation": "s", "fade_type": "s", "subtype": "s", "system_compatiblity": "s",
    }),
    # item-types.ts:140-148 tagCore() + 162-199 class TagDM
    "tag": dict(DEFAULT_ITEM, **{
        "subtype": "s", "crispy": "b", "hidden": "b",
        "question": "s", "question_letter": "s", "category": "s",
        "burn_state": "n", "burned": "b", "is_bonus": "b", "theme_id": "id",
        "custom_tag": "b", "broad": "b", "temporary": "b", "permanent": "b",
        "parentId": "id", "subtagRequired": "b", "showcased": "b",
        "activated_loadout": "b",
        "example0": "s", "example1": "s", "example2": "s",
        "counterexample0": "s", "counterexample1": "s", "counterexample2": "s",
        "restriction0": "s", "restriction1": "s", "restriction2": "s",
        "sceneId": "id", "createdBy": "a",
    }),
    # item-types.ts:367-389  class GMMove
    "gmmove": dict(DEFAULT_ITEM, **{
        "subtype": "s", "taglist": "a", "statuslist": "a",
        "hideName": "b", "header": "s", "superMoveId": "id",
    }),
    # item-types.ts:240-264  class Spectrum  (schema is ONLY maxTier)
    "spectrum": {"maxTier": "n"},
    # item-types.ts:223-237  class Improvement (emitted by no pack today; kept so a
    # future pc-special -> improvement pass is checked the moment it lands)
    "improvement": dict(DEFAULT_ITEM, **SYSTEM_ITEM, **{
        "uses": "o", "theme_id": "id", "choice_item": "s", "chosen": "b",
        "effect_class": "s", "system_compatiblity": "s",
    }),
    # actor-types.ts:5-15 default_template() + 17-22 themeHolder() + 32-37 aliasable()
    # + 40-47 person() + 76-91 class ThreatSchema
    "threat": {
        "locked": "b", "biography": "h", "description": "h", "short_description": "s",
        "gmnotes": "h", "crewThemes": "a", "version": "s",
        "alias": "s", "useAlias": "b",
        "finalized": "b", "mythos": "s",
        "logos": "s", "age": "n", "residence": "s", "pronouns": "s",
        "is_template": "b", "template_ids": "a", "collectiveSize": "n",
        "defaultTags": "a", "defaultStatuses": "a",
    },
}

# item-types.ts:150-160  class EmbeddedTagDM (type + name + tagCore())
EMBEDDED_TAG = {"type": "s", "name": "s", "description": "h", "locked": "b",
                "version": "s", "subtype": "s", "crispy": "b", "hidden": "b"}
# item-types.ts:326-334 class EmbeddedStatusDM (type + name + coreStatus() = defaultItem
# + tiered() [item-types.ts:85-90] + hidden)
EMBEDDED_STATUS = {"type": "s", "name": "s", "description": "h", "locked": "b",
                   "version": "s", "tier": "n", "pips": "n", "hidden": "b"}
# default-themekit.ts:21-25 ThemekitTagData
TK_TAG = {"tagname": "s", "description": "s", "letter": "s"}
# default-themekit.ts:40-45 ThemekitImprovementData
TK_IMPROVEMENT = {"name": "s", "uses": "n", "description": "s", "effect_class": "s"}

# Enumerations
MOTIVATIONS = {"identity", "mystery", "directive", "ritual", "itch", "motivation"}   # motivation-types.ts:10-17
FADE_TYPES = {"fade", "crack", "strike", "decay", "default"}                         # fade-types.ts:1-7
MOVETYPES = {"soft", "hard", "custom", "intrusion", "entrance", "downtime"}          # move-types.ts:1-8
MOVE_HEADERS = {"default", "none", "symbols", "text"}                                # item-types.ts:376
TAGTYPES = {"power", "story", "weakness", "loadout", "relationship"}                 # tag-types.ts:1-8
TAG_CATEGORIES = {"none", "hindering", "weakening", "ability", "empower",
                  "object", "being"}                                                 # config/tag-categories.ts:1-9
# otherscape.ts:47-96 themeTypes() keys, in Otherscape mode
THEME_TYPES = {"Loadout", "Noise", "Self", "Mythos-OS", "Mythos", "Crew-OS"}
SOURCE_BOOKS = {"", "OtherscapeCore"}                                                # otherscape.ts:22-26
SYSTEMS = {"otherscape", "any"}                                                      # otherscape.ts:37

# Top-level document keys the Foundry CLI `_source` layout carries (as seen in
# src/city-of-mist/packs/*/_source/*.json).
TOP_ITEM = {"_id", "_key", "name", "type", "img", "system", "effects", "folder",
            "sort", "ownership", "flags", "_stats"}
TOP_ACTOR = TOP_ITEM | {"items", "prototypeToken"}
TOP_JOURNAL = {"_id", "_key", "name", "pages", "categories", "folder", "sort",
               "ownership", "flags", "_stats"}
TOP_PAGE = {"_id", "_key", "name", "type", "title", "text", "image", "video", "src",
            "system", "sort", "ownership", "flags", "_stats"}

PACK_DOC = {"theme-kits": ("Item", "themekit"), "loadout": ("Item", "tag"),
            "challenges": ("Actor", "threat"), "power-sets": ("Actor", "threat"),
            "journals": ("JournalEntry", None)}


class Report:
    def __init__(self):
        self.errors, self.warns = [], []
        self.checked = collections.Counter()

    def err(self, where, msg):
        self.errors.append((where, msg))

    def warn(self, where, msg):
        self.warns.append((where, msg))


def type_ok(value, token):
    if token == "s":
        return isinstance(value, str)
    if token == "h":
        return isinstance(value, str)
    if token == "b":
        return isinstance(value, bool)
    if token == "n":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if token == "a":
        return isinstance(value, list)
    if token == "o":
        return isinstance(value, dict)
    if token == "id":
        return value is None or (isinstance(value, str)
                                 and (value == "" or bool(ID_RE.match(value))))
    return True


def check_system(rep, where, system, schema):
    """Missing / extra / mistyped against a defineSchema() field list."""
    if not isinstance(system, dict):
        rep.err(where, "system is not an object")
        return
    for key, token in schema.items():
        if key not in system:
            rep.err(where, f"system.{key}: MISSING (schema declares it)")
        elif not type_ok(system[key], token):
            rep.err(where, f"system.{key}: MISTYPED, want {token}, got "
                           f"{type(system[key]).__name__}")
    for key in system:
        if key not in schema:
            rep.err(where, f"system.{key}: EXTRA (not in defineSchema())")


def check_subobjects(rep, where, arr, schema, label):
    for i, entry in enumerate(arr or []):
        if not isinstance(entry, dict):
            rep.err(where, f"{label}[{i}]: not an object")
            continue
        for key, token in schema.items():
            if key not in entry:
                rep.err(where, f"{label}[{i}].{key}: MISSING")
            elif not type_ok(entry[key], token):
                rep.err(where, f"{label}[{i}].{key}: MISTYPED, want {token}")
        for key in entry:
            if key not in schema:
                rep.err(where, f"{label}[{i}].{key}: EXTRA")


def check_top(rep, where, doc, allowed, key_prefix, doc_id=None):
    for key in allowed:
        if key not in doc:
            rep.err(where, f"{key}: MISSING top-level key")
    for key in doc:
        if key not in allowed:
            rep.err(where, f"{key}: EXTRA top-level key")
    _id = doc.get("_id")
    if not (isinstance(_id, str) and ID_RE.match(_id)):
        rep.err(where, f"_id {_id!r} is not 16 chars of [A-Za-z0-9]")
    want_key = f"{key_prefix}{doc_id or _id}"
    if doc.get("_key") != want_key:
        rep.err(where, f"_key {doc.get('_key')!r} should be {want_key!r}")
    if not isinstance(doc.get("name"), str) or not doc.get("name"):
        rep.err(where, "name is empty or not a string")
    own = doc.get("ownership")
    if not isinstance(own, dict) or "default" not in own:
        rep.err(where, "ownership.default missing")
    elif own["default"] not in (-1, 0, 1, 2, 3):
        rep.err(where, f"ownership.default {own['default']!r} is not a Foundry level")


def check_themekit(rep, where, doc):
    check_top(rep, where, doc, TOP_ITEM, "!items!")
    if doc.get("type") != "themekit":
        rep.err(where, f"type {doc.get('type')!r} should be 'themekit'")
    s = doc.get("system") or {}
    check_system(rep, where, s, SCHEMAS["themekit"])
    if s.get("motivation") not in MOTIVATIONS:
        rep.err(where, f"system.motivation {s.get('motivation')!r} not in MOTIVATIONLIST")
    if s.get("fade_type") not in FADE_TYPES:
        rep.err(where, f"system.fade_type {s.get('fade_type')!r} not in FADETYPELIST")
    if s.get("subtype") not in THEME_TYPES:
        rep.err(where, f"system.subtype {s.get('subtype')!r} not an Otherscape theme type")
    if s.get("subtype") == "Mythos-OS":
        rep.warn(where, "system.subtype 'Mythos-OS' breaks autoEssence "
                        "(otherscape.ts:135/141/147 compare against 'Mythos')")
    if s.get("system_compatiblity") not in SYSTEMS:
        rep.err(where, f"system.system_compatiblity {s.get('system_compatiblity')!r} "
                       f"is not 'otherscape'/'any'")
    if s.get("sourceBook") not in SOURCE_BOOKS:
        rep.err(where, f"system.sourceBook {s.get('sourceBook')!r} not a SourceBooks key")
    for field, count, letters in (("power_tagstk", 10, "ABCDEFGHIJ"),
                                  ("weakness_tagstk", 4, "ABCD")):
        arr = s.get(field) or []
        if len(arr) != count:
            rep.err(where, f"system.{field} has {len(arr)} entries, want exactly {count}")
        check_subobjects(rep, where, arr, TK_TAG, f"system.{field}")
        got = "".join(e.get("letter", "?") for e in arr if isinstance(e, dict))
        if got != letters:
            rep.err(where, f"system.{field} letters {got!r}, want {letters!r}")
    imps = s.get("improvements") or []
    if len(imps) != 5:
        rep.err(where, f"system.improvements has {len(imps)} entries, want exactly 5")
    check_subobjects(rep, where, imps, TK_IMPROVEMENT, "system.improvements")
    if not s.get("themebook_name"):
        rep.err(where, "system.themebook_name is empty")
    if not s.get("themebook_id"):
        rep.warn(where, "system.themebook_id is empty; resolution falls back to "
                        "themebook_name (city-db.ts:199-203 searchForContent)")
    if not any(t.get("tagname") for t in (s.get("power_tagstk") or [])[:1]):
        rep.err(where, "power tag A (the title tag) is empty")


def check_loadout_tag(rep, where, doc):
    check_top(rep, where, doc, TOP_ITEM, "!items!")
    if doc.get("type") != "tag":
        rep.err(where, f"type {doc.get('type')!r} should be 'tag'")
    s = doc.get("system") or {}
    check_system(rep, where, s, SCHEMAS["tag"])
    if s.get("subtype") != "loadout":
        rep.err(where, f"system.subtype {s.get('subtype')!r} should be 'loadout'")
    if s.get("subtype") not in TAGTYPES:
        rep.err(where, f"system.subtype {s.get('subtype')!r} not in TAGTYPES")
    if s.get("category") not in TAG_CATEGORIES:
        rep.err(where, f"system.category {s.get('category')!r} not in TAG_CATEGORY_LIST")


def check_threat(rep, where, doc, expect_template):
    check_top(rep, where, doc, TOP_ACTOR, "!actors!")
    if doc.get("type") != "threat":
        rep.err(where, f"type {doc.get('type')!r} should be 'threat'")
    s = doc.get("system") or {}
    check_system(rep, where, s, SCHEMAS["threat"])
    if s.get("is_template") is not expect_template:
        rep.err(where, f"system.is_template {s.get('is_template')!r}, want {expect_template}")
    if not isinstance(s.get("collectiveSize"), int) or s.get("collectiveSize") < 0:
        rep.err(where, f"system.collectiveSize {s.get('collectiveSize')!r} is not a "
                       f"non-negative integer")
    if s.get("alias") and not s.get("useAlias"):
        rep.warn(where, "system.alias is set but useAlias is false")
    if s.get("useAlias") and not s.get("alias"):
        rep.err(where, "system.useAlias is true but alias is empty")
    # The alias a player actually sees is the token name (city-actor.ts:1237-1257
    # getDisplayedName; templates/parts/threat-sheet-header.html:5,7), not system.alias.
    tok = doc.get("prototypeToken") or {}
    if not tok.get("name"):
        rep.err(where, "prototypeToken.name is empty; the threat would display "
                       "'My Name is Error'")
    elif s.get("alias") and tok.get("name") != s.get("alias"):
        rep.err(where, f"prototypeToken.name {tok.get('name')!r} does not carry the "
                       f"alias {s.get('alias')!r}")
    for tid in s.get("template_ids") or []:
        if not (isinstance(tid, str) and ID_RE.match(tid)):
            rep.err(where, f"system.template_ids entry {tid!r} is not a 16-char id")
    check_subobjects(rep, where, s.get("defaultTags"), EMBEDDED_TAG, "system.defaultTags")
    for i, t in enumerate(s.get("defaultTags") or []):
        if isinstance(t, dict):
            if t.get("type") != "tag":
                rep.err(where, f"system.defaultTags[{i}].type should be 'tag'")
            if t.get("subtype") not in TAGTYPES:
                rep.err(where, f"system.defaultTags[{i}].subtype {t.get('subtype')!r} "
                               f"not in TAGTYPES")
    check_subobjects(rep, where, s.get("defaultStatuses"), EMBEDDED_STATUS,
                     "system.defaultStatuses")
    for i, st in enumerate(s.get("defaultStatuses") or []):
        if isinstance(st, dict):
            if st.get("type") != "status":
                rep.err(where, f"system.defaultStatuses[{i}].type should be 'status'")
            if not isinstance(st.get("tier"), int):
                rep.err(where, f"system.defaultStatuses[{i}].tier is not an integer")

    # embedded items
    parent = doc.get("_id")
    soft_ids = {it.get("_id") for it in doc.get("items") or []
                if isinstance(it, dict) and it.get("type") == "gmmove"}
    spectra = 0
    for it in doc.get("items") or []:
        if not isinstance(it, dict):
            rep.err(where, "items entry is not an object")
            continue
        iw = f"{where} > item {it.get('name')!r}"
        check_top(rep, iw, it, TOP_ITEM, f"!actors.items!{parent}.")
        itype = it.get("type")
        if itype not in ("spectrum", "gmmove", "tag", "status"):
            rep.err(iw, f"embedded item type {itype!r} unexpected on a threat")
            continue
        isys = it.get("system") or {}
        check_system(rep, iw, isys, SCHEMAS.get(itype, {}))
        if itype == "spectrum":
            spectra += 1
            mt = isys.get("maxTier")
            if not isinstance(mt, int) or not (1 <= mt <= 999):
                rep.err(iw, f"spectrum maxTier {mt!r} outside 1..999 "
                            f"(item-types.ts:244)")
        if itype == "gmmove":
            if isys.get("subtype") not in MOVETYPES:
                rep.err(iw, f"gmmove subtype {isys.get('subtype')!r} not in MOVETYPES")
            if isys.get("header") not in MOVE_HEADERS:
                rep.err(iw, f"gmmove header {isys.get('header')!r} not a valid header")
            sm = isys.get("superMoveId")
            if sm:
                if sm not in soft_ids:
                    rep.err(iw, f"superMoveId {sm!r} does not name a gmmove on this actor")
                if isys.get("subtype") != "hard":
                    rep.warn(iw, "submove is not subtype 'hard' "
                                 "(city-item.ts:1756-1767 createSubMove)")
            desc = isys.get("description") or ""
            if "{" in desc or "}" in desc:
                rep.warn(iw, "description contains braces; the system hides braced text "
                             "from players (city-helpers.ts removeWithinBraces)")
    if spectra == 0 and not expect_template:
        rep.warn(where, "no spectrum items: this Challenge has no Limits")


def check_journal(rep, where, doc):
    check_top(rep, where, doc, TOP_JOURNAL, "!journal!")
    # CityDB.loadTutorial() (city-db.ts:47-53) picks the first JournalEntry named
    # "System Tutorial" out of *every* JournalEntry compendium; ours must not shadow it.
    if doc.get("name") == "System Tutorial":
        rep.err(where, "name 'System Tutorial' shadows the system's own tutorial entry "
                       "(city-db.ts:47-53)")
    pages = doc.get("pages")
    if not isinstance(pages, list) or not pages:
        rep.err(where, "pages is empty")
        return
    for p in pages:
        pw = f"{where} > page {p.get('name')!r}"
        check_top(rep, pw, p, TOP_PAGE, f"!journal.pages!{doc.get('_id')}.")
        if p.get("type") != "text":
            rep.err(pw, f"page type {p.get('type')!r} should be 'text'")
        text = p.get("text") or {}
        if text.get("format") != 1:
            rep.err(pw, f"page text.format {text.get('format')!r} should be 1 (HTML)")
        if not isinstance(text.get("content"), str) or not text.get("content"):
            rep.err(pw, "page text.content is empty")
        for m in re.finditer(r"@UUID\[([^\]]+)\]", text.get("content") or ""):
            u = m.group(1)
            if not (u.startswith("Compendium.neon-black.")
                    or re.match(r"^(JournalEntry|Item|Actor)\.[A-Za-z0-9]{16}", u)):
                rep.err(pw, f"malformed @UUID target {u!r}")


def check_module_json(rep, path):
    if not os.path.exists(path):
        rep.err("module.json", "missing")
        return
    m = json.load(open(path, encoding="utf-8"))
    for key in ("id", "title", "version", "compatibility", "relationships", "packs",
                "esmodules"):
        if key not in m:
            rep.err("module.json", f"{key}: MISSING")
    if m.get("id") != "neon-black":
        rep.err("module.json", f"id {m.get('id')!r} should be 'neon-black'")
    comp = m.get("compatibility") or {}
    if comp.get("minimum") != "13" or comp.get("verified") != "14":
        rep.err("module.json", f"compatibility {comp!r} should track system.json (13/14)")
    sysrels = (m.get("relationships") or {}).get("systems") or []
    if not any(r.get("id") == "city-of-mist" for r in sysrels):
        rep.err("module.json", "relationships.systems does not require city-of-mist")
    names = set()
    for p in m.get("packs") or []:
        for key in ("name", "label", "path", "type", "system", "ownership"):
            if key not in p:
                rep.err("module.json", f"pack {p.get('name')!r}: {key} MISSING")
        if p.get("system") != "city-of-mist":
            rep.err("module.json", f"pack {p.get('name')!r}: system should be city-of-mist")
        if p.get("type") not in ("Item", "Actor", "JournalEntry", "Scene", "Macro",
                                 "RollTable", "Cards", "Adventure", "Playlist"):
            rep.err("module.json", f"pack {p.get('name')!r}: bad type {p.get('type')!r}")
        names.add(p.get("name"))
    for want in ("theme-kits", "challenges", "power-sets", "loadout", "journals"):
        if want not in names:
            rep.err("module.json", f"pack {want!r} not declared")


def main(argv=None):
    ap = argparse.ArgumentParser(description="check emitted _source JSON against the datamodel")
    ap.add_argument("--out", default=os.path.join(ROOT, "build"))
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)
    out = os.path.abspath(args.out)
    rep = Report()

    check_module_json(rep, os.path.join(out, "module.json"))

    ids = {}
    for pack, (cls, dtype) in sorted(PACK_DOC.items()):
        files = sorted(glob.glob(os.path.join(out, "packs", pack, "_source", "*.json")))
        if not files:
            rep.warn(pack, "no _source documents emitted")
        for path in files:
            where = f"{pack}/{os.path.basename(path)}"
            try:
                doc = json.load(open(path, encoding="utf-8"))
            except json.JSONDecodeError as e:
                rep.err(where, f"invalid JSON: {e}")
                continue
            rep.checked[pack] += 1
            if doc.get("_id") in ids:
                rep.err(where, f"_id collides with {ids[doc['_id']]}")
            ids[doc.get("_id")] = where
            if pack == "theme-kits":
                check_themekit(rep, where, doc)
            elif pack == "loadout":
                check_loadout_tag(rep, where, doc)
            elif pack == "challenges":
                check_threat(rep, where, doc, expect_template=False)
            elif pack == "power-sets":
                check_threat(rep, where, doc, expect_template=True)
            else:
                check_journal(rep, where, doc)

    # Cross-pack: every template_ids entry must name an emitted power-set actor.
    ps_ids = set()
    for path in glob.glob(os.path.join(out, "packs", "power-sets", "_source", "*.json")):
        ps_ids.add(json.load(open(path, encoding="utf-8")).get("_id"))
    for path in sorted(glob.glob(os.path.join(out, "packs", "challenges", "_source", "*.json"))):
        doc = json.load(open(path, encoding="utf-8"))
        for tid in (doc.get("system") or {}).get("template_ids") or []:
            if tid not in ps_ids:
                rep.err(f"challenges/{os.path.basename(path)}",
                        f"template_ids {tid!r} names no emitted power-set")

    print("check.py — emitted _source vs city-of-mist datamodel (v4.5.3)")
    for pack in sorted(rep.checked):
        print(f"  {pack:<12} {rep.checked[pack]} documents")
    print(f"  ERRORS: {len(rep.errors)}   WARNINGS: {len(rep.warns)}")
    limit = None if args.verbose else 25
    if rep.errors:
        print("\nERRORS")
        for where, msg in rep.errors[:limit]:
            print(f"  {where}: {msg}")
        if limit and len(rep.errors) > limit:
            print(f"  … {len(rep.errors) - limit} more (use --verbose)")
    if rep.warns:
        counts = collections.Counter(msg.split(";")[0].split("(")[0].strip()
                                     for _, msg in rep.warns)
        print("\nWARNINGS (by kind)")
        for msg, n in counts.most_common(limit):
            print(f"  {n:4d}  {msg}")
        if args.verbose:
            print("\nWARNINGS (all)")
            for where, msg in rep.warns:
                print(f"  {where}: {msg}")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
