#!/usr/bin/env python3
"""Neon Black -> Foundry VTT compendium source (WP9 dry run).

Reads every vault file with frontmatter and emits `_source/*.json` documents for
Taragnor's `city-of-mist` system (v4.5.3, "City of Mist / Mist Engine") running in
**Otherscape** mode, plus a `module.json`. It packages nothing and publishes nothing.

    python3 tools/foundry/convert.py --all
    python3 tools/foundry/convert.py --theme-kits --challenges
    python3 tools/foundry/convert.py --all --uuid-style world

Output (all under `build/`, which is git-ignored):

    build/module.json
    build/README.md
    build/ids.json                        slug -> {_id, pack, documentClass}
    build/report.json                     counts, skips, warnings
    build/packs/theme-kits/_source/*.json Item   themekit   (theme-kit, crew-kit)
    build/packs/challenges/_source/*.json Actor  threat     (challenge)
    build/packs/power-sets/_source/*.json Actor  threat is_template:true (power-set)
    build/packs/loadout/_source/*.json    Item   tag subtype loadout (loadout-item)
    build/packs/journals/_source/*.json   JournalEntry (everything prose)

Dependencies: Python 3 stdlib + PyYAML.

--------------------------------------------------------------------------------
ID SCHEME (deterministic, stable across rebuilds)
--------------------------------------------------------------------------------
Foundry's `DocumentIdField` wants exactly 16 characters from `[A-Za-z0-9]`.

    _id = base62( int.from_bytes( sha1( "neon-black:<kind>:<key>" ) ) )[-16:]

`base62` uses the alphabet "ABC..Zabc..z0..9" and is left-zero-padded to at least
16 characters before the last 16 are taken, so every id is exactly 16 chars.

  * top-level documents  kind = the pack name ("theme-kits", "challenges",
                         "power-sets", "loadout", "journals"), key = the vault slug.
  * embedded Items       kind = "<pack>/<parent-slug>", key = "<itemkind>:<index>"
                         (e.g. "challenges/the-cold-suite" + "spectrum:0").
  * JournalEntry pages   kind = "journals/<slug>", key = "page:0".

Because the input is a slug and the hash is stable, ids never move when the vault
grows. `build/ids.json` records the mapping for review; it is regenerated, not read.
Collisions are detected and abort the run.
"""

from __future__ import annotations

import argparse
import collections
import glob
import hashlib
import html as htmllib
import json
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("pyyaml required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BUILD = os.path.join(ROOT, "build")
SKIP_DIRS = ("ref/", "tools/", ".git/", ".claude/", "00-meta/additions/", "build/")

MODULE_ID = "neon-black"
MODULE_TITLE = "Neon Black"
MODULE_VERSION = "0.1.0"
SYSTEM_ID = "city-of-mist"
SYSTEM_VERSION = "4.5.3"        # src/city-of-mist/system.json "version"
FOUNDRY_MIN = "13"              # system.json compatibility.minimum
FOUNDRY_VERIFIED = "14"         # system.json compatibility.verified
FOUNDRY_MAX = "14"              # system.json compatibility.maximum
DM_VERSION = "1"                # item-types.ts:22 / actor-types.ts:3  const VERSION = "1"
SYSTEM_COMPAT = "otherscape"    # systemModule/otherscape.ts:37  get name() { return "otherscape" }

# ---------------------------------------------------------------------------
# Shipped Otherscape themebook ids, harvested from
# src/city-of-mist/packs/themebooks/_source/*.json where system.system_compatiblity
# == "otherscape" and type == "themebook". `subtype` is the shipped theme-type key:
# note that the four Mythos themebooks ship as "Mythos", NOT "Mythos-OS"
# (otherscape.ts:135/141/147 compares against "Mythos").
# ---------------------------------------------------------------------------
SHIPPED_THEMEBOOKS = {
    "Affiliation":       {"id": "noqoLlmqIwjirJ52", "subtype": "Self"},
    "Assets":            {"id": "m7aMSrzoz8iEjrXi", "subtype": "Self"},
    "Expertise":         {"id": "FUhv3c81M1tcVSJD", "subtype": "Self"},
    "Horizon":           {"id": "WQ1gYMo8oWoiPX2a", "subtype": "Self"},
    "Personality":       {"id": "FW5g6LLhbaf5BFFm", "subtype": "Self"},
    "Troubled Past":     {"id": "snHXQlSZdGALWPNq", "subtype": "Self"},
    "Artifact":          {"id": "NgbUT22G4qsBqSwn", "subtype": "Mythos"},
    "Companion":         {"id": "K1T0cmc315lR55ql", "subtype": "Mythos"},
    "Esoterica":         {"id": "f0Hldws5yB2ezw1Z", "subtype": "Mythos"},
    "Exposure":          {"id": "5CG8unkzHqU6xuQW", "subtype": "Mythos"},
    "Augmentation":      {"id": "K3rvh4bMi0L6S4lS", "subtype": "Noise"},
    "Cutting Edge":      {"id": "eSg1666zWlbhuoyl", "subtype": "Noise"},
    "Cyberspace":        {"id": "D88XNZrAQ5oMfsFW", "subtype": "Noise"},
    "Drones":            {"id": "3i6BJjmC1oKKQvCV", "subtype": "Noise"},
    "Crew (Otherscape)": {"id": "ayN2BXLJ2IgQyfh8", "subtype": "Crew-OS"},
    "Loadout":           {"id": "sXQ4DJvPy9GwATCn", "subtype": "Loadout"},
}
# Vault `themebook:` aliases -> shipped name.
THEMEBOOK_ALIASES = {"Crew": "Crew (Otherscape)"}

# Vault `category:` -> system.subtype. The vault writes `Mythos-OS` (Plan A.4); the
# shipped Otherscape Mythos themebooks and `determineEssenceFromThemes`
# (otherscape.ts:130-149) both use the bare key `Mythos`, so that is what we emit.
CATEGORY_TO_SUBTYPE = {
    "Self": "Self",
    "Noise": "Noise",
    "Mythos-OS": "Mythos",
    "Mythos": "Mythos",
    "Crew-OS": "Crew-OS",
    "Loadout": "Loadout",
}

MOTIVATIONS = {"identity", "mystery", "directive", "ritual", "itch", "motivation"}  # motivation-types.ts:10-17
FADE_TYPES = {"fade", "crack", "strike", "decay", "default"}                        # fade-types.ts:1-7
MOVETYPES = ("soft", "hard", "custom", "intrusion", "entrance", "downtime")         # move-types.ts:1-8
TAGTYPES = ("power", "story", "weakness", "loadout", "relationship")                # tag-types.ts:1-8
SPECTRUM_IMMUNE = 999                                                              # default-themekit.ts:57-65 SPECTRUM_VALUES[999] == "-"

# Which vault `type` goes to which pack.
PACK_OF_TYPE = {
    "theme-kit": "theme-kits",
    "crew-kit": "theme-kits",
    "challenge": "challenges",
    "power-set": "power-sets",
    "loadout-item": "loadout",
    "district": "journals",
    "key-player": "journals",
    "npc": "journals",
    "job": "journals",
    "scene": "journals",
    "character-trope": "journals",
    "pc-special": "journals",
    "crew-special": "journals",
    "membership": "journals",
    "series": "journals",
    "splat-overview": "journals",
    "index": "journals",
}
PACK_DOCCLASS = {
    "theme-kits": "Item",
    "challenges": "Actor",
    "power-sets": "Actor",
    "loadout": "Item",
    "journals": "JournalEntry",
}
# `type: meta` is never converted (foundry-mapping.md §1, BC-10).
NEVER_CONVERT = {"meta"}
# Only reviewed/approved vault files are emitted (foundry-mapping.md §2).
CONVERT_STATUS = {"review", "approved"}

IMG_ITEM = "icons/svg/item-bag.svg"
IMG_ACTOR = "icons/svg/mystery-man.svg"
ASSET_PREFIX = "modules/neon-black/"   # the module ships the vault's assets/ folder as-is (WP-I)

_NPC_ASSETS = None

def _npc_assets():
    """slug -> module image path for every `npc` file that embeds a paper puppet."""
    global _NPC_ASSETS
    if _NPC_ASSETS is None:
        _NPC_ASSETS = {}
        for path in glob.glob(os.path.join(ROOT, "0[0-9]-*", "**", "*.md"), recursive=True):
            try:
                text = open(path, encoding="utf-8").read()
            except OSError:
                continue
            if not re.search(r"^type:\s*npc\s*$", text, re.M):
                continue
            m = re.search(r"!\[\[(assets/npcs/[^\]|]+)(?:\|[^\]]*)?\]\]", text)
            if m:
                _NPC_ASSETS[os.path.basename(path)[:-3]] = ASSET_PREFIX + m.group(1)
    return _NPC_ASSETS


def doc_asset(doc):
    """First `![[assets/...]]` embed in the body -> module-relative image path.

    A named NPC's Challenge file (`<slug>-challenge`, BC-125) carries no embed of its
    own, so it borrows the NPC's paper puppet for the Actor image and token."""
    m = re.search(r"!\[\[(assets/[^\]|]+)(?:\|[^\]]*)?\]\]", doc.body or "")
    if m:
        return ASSET_PREFIX + m.group(1)
    slug = getattr(doc, "slug", "") or ""
    if slug.endswith("-challenge"):
        return _npc_assets().get(slug[:-len("-challenge")])
    return None

# Foundry ownership levels.
OWN_INHERIT, OWN_NONE, OWN_LIMITED, OWN_OBSERVER, OWN_OWNER = -1, 0, 1, 2, 3

# `unifiedSubstitution` (city-helpers.ts:309) only recognises
# /\[([ \w,]*:)?([\p{Letter}\d\- ]+)\]/ — letters, digits, hyphen and space in the
# name. Anything else (commas, apostrophes, slashes) silently fails to become a
# draggable tag/status, so we refuse to wrap it and report it instead.
MARKUP_SAFE = re.compile(r"^[^\W_][\w\- ]*$", re.UNICODE)


# ===========================================================================
# ids
# ===========================================================================
_B62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def _base62(n: int) -> str:
    if n == 0:
        return _B62[0]
    out = []
    while n:
        n, r = divmod(n, 62)
        out.append(_B62[r])
    return "".join(reversed(out))


def make_id(kind: str, key: str) -> str:
    """Deterministic 16-character [A-Za-z0-9] Foundry document id."""
    digest = hashlib.sha1(f"neon-black:{kind}:{key}".encode("utf-8")).digest()
    s = _base62(int.from_bytes(digest, "big")).rjust(16, "A")
    return s[-16:]


# ===========================================================================
# vault reading
# ===========================================================================
class Doc:
    __slots__ = ("path", "fm", "body", "slug", "type", "name")

    def __init__(self, path, fm, body):
        self.path = path
        self.fm = fm
        self.body = body
        self.slug = fm.get("slug") or os.path.basename(path)[:-3]
        self.type = fm.get("type")
        self.name = fm.get("name") or self.slug


def read_vault():
    """Every .md with a YAML frontmatter block, in stable path order."""
    docs, skipped = [], []
    paths = [p for p in sorted(glob.glob("**/*.md", recursive=True))
             if "/" in p and not p.startswith(SKIP_DIRS)]
    for p in paths:
        text = open(p, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not m:
            skipped.append({"path": p, "reason": "no frontmatter"})
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            skipped.append({"path": p, "reason": f"unparseable YAML: {e}"})
            continue
        if not isinstance(fm, dict):
            skipped.append({"path": p, "reason": "frontmatter is not a mapping"})
            continue
        docs.append(Doc(p, fm, m.group(2)))
    return docs, skipped


def convertible(doc, skipped):
    """True when this vault file becomes a Foundry document."""
    if doc.fm.get("template"):
        skipped.append({"path": doc.path, "reason": "template: true (99-templates)"})
        return False
    if doc.type in NEVER_CONVERT:
        skipped.append({"path": doc.path, "reason": f"type: {doc.type} is vault-only"})
        return False
    if doc.type not in PACK_OF_TYPE:
        skipped.append({"path": doc.path, "reason": f"unknown type: {doc.type!r}"})
        return False
    if doc.fm.get("status") not in CONVERT_STATUS:
        skipped.append({"path": doc.path,
                        "reason": f"status: {doc.fm.get('status')!r} (need review/approved)"})
        return False
    return True


# ===========================================================================
# Markdown -> HTML  (small, deterministic, stdlib only)
# ===========================================================================
WIKILINK = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]+?))?\]\]")


class Linker:
    """Resolves [[wikilinks]] against the emitted document index.

    `[[slug]]`, `[[slug|label]]` and `[[slug#Heading]]` are all handled. A
    `#Heading` on a JournalEntry target becomes the Foundry page-anchor form
    `...JournalEntry.<id>.JournalEntryPage.<pageId>#Heading`; on any other target
    the anchor is dropped. `book:<slug>` (printed book kits, BC-126) and any slug
    with no emitted document fall back to the plain label.
    """

    def __init__(self, index, style="compendium"):
        self.index = index          # slug -> {"id", "pack", "cls", "page"}
        self.style = style
        self.unresolved = collections.Counter()

    def uuid(self, slug, anchor=""):
        e = self.index.get(slug)
        if not e:
            return None
        if self.style == "world":
            u = f"{e['cls']}.{e['id']}"
        else:
            u = f"Compendium.{MODULE_ID}.{e['pack']}.{e['cls']}.{e['id']}"
        if anchor and e["cls"] == "JournalEntry" and e.get("page"):
            u += f".JournalEntryPage.{e['page']}#{anchor}"
        return u

    def sub(self, text):
        """Substitute wikilinks in *raw* (unescaped) text; labels are escaped here."""
        def rep(m):
            target = m.group(1).strip()
            label = (m.group(2) or target).strip()
            anchor = ""
            if "#" in target:
                target, anchor = target.split("#", 1)
                target, anchor = target.strip(), anchor.strip()
                if not m.group(2):
                    label = anchor or target
            if target.startswith("book:"):
                return htmllib.escape(label, quote=False)
            if target.startswith("assets/"):
                # image embed (`![[assets/...]]`, WP-I): leave for _inline's <img> rule
                return m.group(0)
            u = self.uuid(target, anchor)
            if not u:
                self.unresolved[target] += 1
                return htmllib.escape(label, quote=False)
            return f"@UUID[{u}]{{{htmllib.escape(label, quote=False)}}}"
        return WIKILINK.sub(rep, text)


def _inline(text, linker=None):
    """Inline markdown -> HTML.

    Wikilinks are resolved *before* escaping (a target may contain `&`), and the
    resulting `@UUID[...]{label}` is parked in a placeholder so the escape pass
    and the emphasis passes cannot touch it. Everything else is escaped, so raw
    HTML in the vault is inert.
    """
    parked = []

    def park(s):
        parked.append(s)
        return f"\x01{len(parked) - 1}\x01"

    # image embeds (`![[assets/...]]`, WP-I) become <img> before anything can park or escape them
    text = re.sub(r"!\[\[(assets/[^\]|]+)(?:\|[^\]]*)?\]\]",
                  lambda m: park(f'<img src="{ASSET_PREFIX}{m.group(1)}">'), text)
    if linker is not None:
        text = WIKILINK.sub(lambda m: park(linker.sub(m.group(0))), text)
    out = htmllib.escape(text, quote=False)
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"
    out = re.sub(r"`([^`]+)`", stash, out)
    out = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", r'<img src="\2" alt="\1">', out)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", out)
    out = re.sub(r"(?<![\w_])_([^_\n]+?)_(?![\w_])", r"<em>\1</em>", out)
    out = re.sub(r"~~(.+?)~~", r"<s>\1</s>", out)
    out = re.sub(r"\x00(\d+)\x00",
                 lambda m: "<code>" + htmllib.escape(codes[int(m.group(1))]) + "</code>", out)
    out = re.sub(r"\x01(\d+)\x01", lambda m: parked[int(m.group(1))], out)
    return out


def escape_with_links(text, linker=None):
    """HTML-escape a plain string, but resolve any [[wikilinks]] inside it first."""
    parked = []
    if linker is not None:
        def park(m):
            parked.append(linker.sub(m.group(0)))
            return f"\x01{len(parked) - 1}\x01"
        text = WIKILINK.sub(park, str(text))
    out = htmllib.escape(str(text), quote=False)
    return re.sub(r"\x01(\d+)\x01", lambda m: parked[int(m.group(1))], out)


def flatten_wikilinks(text):
    """[[slug|label]] / [[slug#Heading]] -> the label a reader would see."""
    def rep(m):
        if m.group(2):
            return m.group(2)
        t = m.group(1)
        return t.split("#", 1)[1].strip() if "#" in t else t
    return WIKILINK.sub(rep, str(text))


def md_to_html(md, linker=None):
    """Block-level markdown -> HTML: headings, lists, tables, quotes, rules, code."""
    lines = md.replace("\r\n", "\n").split("\n")
    out, i, n = [], 0, len(lines)
    para = []

    def flush():
        if para:
            out.append("<p>" + _inline(" ".join(para).strip(), linker) + "</p>")
            para.clear()

    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            flush(); i += 1; continue
        if stripped.startswith("```"):
            flush()
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append("<pre><code>" + htmllib.escape("\n".join(buf)) + "</code></pre>")
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush()
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{_inline(m.group(2).strip(), linker)}</h{lvl}>")
            i += 1; continue
        if re.match(r"^(\*\s*){3,}$|^(-\s*){3,}$|^(_\s*){3,}$", stripped):
            flush(); out.append("<hr>"); i += 1; continue
        # GFM table: header row then a |---|---| separator
        if stripped.startswith("|") and i + 1 < n and re.match(
                r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            flush()
            def cells(row):
                row = row.strip()
                if row.startswith("|"): row = row[1:]
                if row.endswith("|"): row = row[:-1]
                return [c.strip() for c in row.split("|")]
            head = cells(lines[i]); i += 2
            body = []
            while i < n and lines[i].strip().startswith("|"):
                body.append(cells(lines[i])); i += 1
            t = ["<table><thead><tr>"]
            t += [f"<th>{_inline(c, linker)}</th>" for c in head]
            t.append("</tr></thead><tbody>")
            for row in body:
                t.append("<tr>" + "".join(f"<td>{_inline(c, linker)}</td>" for c in row) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        if stripped.startswith(">"):
            flush()
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append("<blockquote>" + md_to_html("\n".join(buf), linker) + "</blockquote>")
            continue
        m = re.match(r"^\s*([-*+]|\d+[.)])\s+", line)
        if m:
            flush()
            ordered = not m.group(1) in ("-", "*", "+")
            items, cur = [], None
            while i < n:
                mm = re.match(r"^\s*([-*+]|\d+[.)])\s+(.*)$", lines[i])
                if mm:
                    if cur is not None:
                        items.append(cur)
                    cur = mm.group(2).strip()
                    i += 1
                elif lines[i].strip() and lines[i].startswith((" ", "\t")) and cur is not None:
                    cur += " " + lines[i].strip(); i += 1
                else:
                    break
            if cur is not None:
                items.append(cur)
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{_inline(x, linker)}</li>" for x in items) + f"</{tag}>")
            continue
        para.append(stripped)
        i += 1
    flush()
    return "".join(out)


# ===========================================================================
# helpers
# ===========================================================================
def stats_block():
    """Minimal `_stats`. Fixed timestamps keep the output byte-identical per run."""
    return {
        "systemId": SYSTEM_ID,
        "systemVersion": SYSTEM_VERSION,
        "coreVersion": f"{FOUNDRY_VERIFIED}.0",
        "createdTime": None,
        "modifiedTime": None,
        "lastModifiedBy": None,
        "compendiumSource": None,
        "duplicateSource": None,
        "exportSource": None,
    }


def flags_for(doc):
    return {MODULE_ID: {"type": doc.type, "slug": doc.slug, "path": doc.path,
                        "player_safe": bool(doc.fm.get("player_safe"))}}


def esc(x):
    return htmllib.escape(str(x), quote=False)


def parse_status(s):
    """"alert-2" -> ("alert", 2). Trailing integer after a hyphen or space."""
    s = str(s).strip()
    m = re.match(r"^(.*?)[\-\s](\d+)$", s)
    if m:
        return m.group(1).strip(), int(m.group(2))
    return s, 0


def markup_safe(name):
    return bool(MARKUP_SAFE.match(str(name).strip()))


def _bracket_in_place(text, needle, opts):
    """Wrap the first plain-text occurrence of `needle` in the system's `[...]`
    markup rather than appending a duplicate. Returns (text, did_wrap).

    Only an occurrence that is not already inside brackets is touched, and the
    vault's wording is never otherwise altered.
    """
    pat = re.compile(r"(?<!\[)\b" + re.escape(needle) + r"\b(?!\])", re.IGNORECASE)
    m = pat.search(text)
    if not m:
        return text, False
    return text[:m.start()] + f"[{opts}{m.group(0)}]" + text[m.end():], True


def humanize_limit(name):
    """"hurt-or-subdue" -> "hurt or subdue" (the name the vault prose prints)."""
    return str(name).replace("-", " ").strip()


def short_label(text, limit=64):
    """A stable short document name from a sentence of prose."""
    t = re.sub(r"\s+", " ", flatten_wikilinks(text)).strip()
    t = re.sub(r"[*_`]", "", t)
    if len(t) <= limit:
        return t.rstrip(" .,;:") or "Untitled"
    cut = t[:limit]
    if " " in cut:
        cut = cut[:cut.rfind(" ")]
    return cut.rstrip(" .,;:") + "…"


def source_book(doc):
    """`SourceBooks` has exactly one key, "OtherscapeCore" (otherscape.ts:22-26)."""
    return "OtherscapeCore" if doc.fm.get("source") in ("core", "tokyo") else ""


def canon_line(doc):
    bits = []
    if doc.fm.get("canon_refs"):
        bits.append("<p><em>Canon refs:</em> " + esc("; ".join(map(str, doc.fm["canon_refs"]))) + "</p>")
    if doc.fm.get("page"):
        bits.append("<p><em>Book pages:</em> " + esc(doc.fm["page"]) + "</p>")
    if doc.fm.get("flags"):
        bits.append("<p><em>Flags:</em> " + esc(", ".join(map(str, doc.fm["flags"]))) + "</p>")
    bits.append(f"<p><em>Source: Neon Black</em> — <code>{esc(doc.path)}</code></p>")
    return "".join(bits)


# ===========================================================================
# emitters
# ===========================================================================
class Emitter:
    def __init__(self, index, linker, report):
        self.index = index
        self.linker = linker
        self.report = report

    def warn(self, slug, msg):
        self.report["warnings"].append({"slug": slug, "message": msg})

    # -- themekit ----------------------------------------------------------
    def themekit(self, doc):
        """Item `themekit` (item-types.ts:119-137 Themekit.defineSchema)."""
        fm = doc.fm
        _id = self.index[doc.slug]["id"]

        tb_name = THEMEBOOK_ALIASES.get(str(fm.get("themebook", "")).strip(),
                                        str(fm.get("themebook", "")).strip())
        shipped = SHIPPED_THEMEBOOKS.get(tb_name)
        tb_id = shipped["id"] if shipped else ""
        if not shipped:
            self.warn(doc.slug, f"themebook {tb_name!r} is not a shipped Otherscape "
                                f"themebook; themebook_id left empty")

        category = str(fm.get("category", "")).strip()
        subtype = CATEGORY_TO_SUBTYPE.get(category)
        if subtype is None:
            subtype = "Self"
            self.warn(doc.slug, f"category {category!r} not in the Otherscape theme "
                                f"types; emitted subtype 'Self'")
        if shipped and shipped["subtype"] != subtype:
            self.warn(doc.slug, f"subtype {subtype!r} differs from shipped themebook "
                                f"{tb_name!r} subtype {shipped['subtype']!r}")

        motivation = str(fm.get("motivation_type", "")).strip()
        if motivation not in MOTIVATIONS:
            self.warn(doc.slug, f"motivation_type {motivation!r} not in MOTIVATIONLIST; "
                                f"emitted 'identity'")
            motivation = "identity"

        fade = str(fm.get("fade_type", "decay")).strip() or "decay"
        if fade not in FADE_TYPES:
            self.warn(doc.slug, f"fade_type {fade!r} not in FADETYPELIST; emitted 'decay'")
            fade = "decay"

        power = self._tk_tags(doc, fm.get("power_tags") or [], "ABCDEFGHIJ", "power_tags")
        weak = self._tk_tags(doc, fm.get("weakness_tags") or [], "ABCD", "weakness_tags")

        # improvements[]: five entries, `letter` dropped (no such key in
        # ThemekitImprovementData, default-themekit.ts:40-45).
        imps, any_named = [], False
        for entry in (fm.get("improvements") or [])[:5]:
            entry = entry or {}
            name = str(entry.get("name") or "")
            if name:
                any_named = True
            uses = entry.get("uses", 0)
            imps.append({
                "name": name,
                "uses": int(uses) if isinstance(uses, (int, float)) else 0,
                "description": str(entry.get("description") or ""),
                "effect_class": str(entry.get("effect_class") or ""),
            })
        while len(imps) < 5:
            imps.append({"name": "", "uses": 0, "description": "", "effect_class": ""})
        use_tb = bool(fm.get("use_themebook_improvements", not any_named))

        return {
            "_id": _id,
            "_key": f"!items!{_id}",
            "name": doc.name,
            "type": "themekit",
            "img": doc_asset(doc) or IMG_ITEM,
            "system": {
                # defaultItem() — item-types.ts:68-74
                "description": self._tk_description(doc, tb_name, category, power, weak),
                "locked": False,
                "version": DM_VERSION,
                # systemItem() — item-types.ts:76-83
                "free_content": False,
                "locale_name": "",
                "systemName": "",
                "sourceBook": source_book(doc),
                # Themekit — item-types.ts:125-134
                "themebook_id": tb_id,
                "themebook_name": tb_name,
                "use_tb_improvements": use_tb,
                "power_tagstk": power,
                "weakness_tagstk": weak,
                "improvements": imps,
                "motivation": motivation,
                "fade_type": fade,
                "subtype": subtype,
                "system_compatiblity": SYSTEM_COMPAT,
            },
            "effects": [],
            "folder": None,
            "sort": 0,
            "ownership": {"default": OWN_NONE},
            "flags": flags_for(doc),
            "_stats": stats_block(),
        }

    def _tk_tags(self, doc, entries, letters, field):
        """Exactly len(letters) {letter, tagname, description} entries, in letter order."""
        by_letter = {}
        for e in entries or []:
            e = e or {}
            L = str(e.get("letter") or "").strip().upper()
            if L:
                by_letter[L] = e
        out = []
        for idx, L in enumerate(letters):
            e = by_letter.get(L) or (entries[idx] if idx < len(entries) and not by_letter else {}) or {}
            out.append({
                "letter": L,
                "tagname": str(e.get("tagname") or ""),
                "description": str(e.get("description") or ""),
            })
        if len(entries) > len(letters):
            self.warn(doc.slug, f"{field} has {len(entries)} entries; truncated to {len(letters)}")
        return out

    def _tk_description(self, doc, tb_name, category, power, weak):
        """The theme-kit card as HTML. The datamodel has no motivation-statement
        field, so the statement lives here (foundry-mapping.md §3.1)."""
        fm = doc.fm
        h = [f"<p><strong>Themebook:</strong> {esc(tb_name)} · "
             f"<strong>Category:</strong> {esc(category)}"]
        if fm.get("splat"):
            h.append(f" · <strong>Splat:</strong> {esc(fm['splat'])}")
        h.append("</p>")
        mot_type = esc(str(fm.get("motivation_type", "")).title())
        if fm.get("motivation"):
            h.append(f"<p><strong>{mot_type}:</strong> <em>{esc(fm['motivation'])}</em></p>")
        h.append("<h3>Power tags</h3><table><thead><tr><th>&nbsp;</th><th>Tag</th>"
                 "<th>Answers</th></tr></thead><tbody>")
        for t in power:
            if not t["tagname"] and not t["description"]:
                continue
            h.append(f"<tr><td>{t['letter']}</td><td>{esc(t['tagname'])}</td>"
                     f"<td>{esc(t['description'])}</td></tr>")
        h.append("</tbody></table><h3>Weakness tags</h3><table><thead><tr><th>&nbsp;</th>"
                 "<th>Tag</th><th>Answers</th></tr></thead><tbody>")
        for t in weak:
            if not t["tagname"] and not t["description"]:
                continue
            h.append(f"<tr><td>{t['letter']}</td><td>{esc(t['tagname'])}</td>"
                     f"<td>{esc(t['description'])}</td></tr>")
        h.append("</tbody></table>")
        if fm.get("candidate_motivations"):
            h.append("<h3>Candidate motivations</h3><ul>")
            for c in fm["candidate_motivations"]:
                c = c or {}
                h.append(f"<li><em>{esc(c.get('type',''))}</em>: {esc(c.get('statement',''))}"
                         + (f" — against: {esc(c['against'])}" if c.get("against") else "")
                         + "</li>")
            h.append("</ul>")
        if fm.get("starting_three"):
            h.append(f"<p><strong>Suggested starting three:</strong> "
                     f"{esc(', '.join(map(str, fm['starting_three'])))}</p>")
        h.append(canon_line(doc))
        return "".join(h)

    # -- threat ------------------------------------------------------------
    def threat(self, doc, is_template=False):
        """Actor `threat` (actor-types.ts:76-91 ThreatSchema) with embedded Items."""
        fm = doc.fm
        _id = self.index[doc.slug]["id"]
        pack = self.index[doc.slug]["pack"]
        kind = f"{pack}/{doc.slug}"
        items = []

        # Limits -> `spectrum` Items (item-types.ts:240-264). Immune ("-" in the
        # vault, or tier 999) is maxTier 999: SPECTRUM_VALUES[999] == "-".
        for i, lim in enumerate(fm.get("limits") or []):
            lim = lim or {}
            tier = lim.get("tier")
            if tier in ("-", "–", "—", None, ""):
                tier = SPECTRUM_IMMUNE
            try:
                tier = int(tier)
            except (TypeError, ValueError):
                self.warn(doc.slug, f"limit {lim.get('name')!r} tier {tier!r} unparseable; "
                                    f"emitted 999 (immune)")
                tier = SPECTRUM_IMMUNE
            tier = max(1, min(999, tier))
            iid = make_id(kind, f"spectrum:{i}")
            items.append({
                "_id": iid,
                "_key": f"!actors.items!{_id}.{iid}",
                "name": humanize_limit(lim.get("name") or f"limit {i + 1}"),
                "type": "spectrum",
                "img": IMG_ITEM,
                "system": {"maxTier": tier},
                "effects": [], "folder": None, "sort": i * 100,
                "ownership": {"default": OWN_NONE}, "flags": {}, "_stats": stats_block(),
            })

        # Specials -> `gmmove` subtype custom.
        sort = 1000
        for i, sp in enumerate(fm.get("specials") or []):
            sp = sp or {}
            iid = make_id(kind, f"special:{i}")
            items.append(self._gmmove(
                _id, iid, sp.get("name") or f"Special {i + 1}",
                self._move_text(doc, sp.get("text") or ""),
                subtype="custom", hide_name=False, header="default", sort=sort))
            sort += 100

        # Threats -> `gmmove` subtype soft; each Consequence -> subtype hard with
        # superMoveId pointing at its soft parent (city-item.ts:1756-1767
        # createSubMove sets exactly superMoveId / hideName / header / subtype).
        for i, th in enumerate(fm.get("threats") or []):
            th = th or {}
            soft_id = make_id(kind, f"threat:{i}")
            items.append(self._gmmove(
                _id, soft_id, short_label(th.get("threat") or f"Threat {i + 1}"),
                self._move_text(doc, th.get("threat") or ""),
                subtype="soft", hide_name=True, header="symbols", sort=sort))
            sort += 100
            for j, cq in enumerate(th.get("consequences") or []):
                cq = cq or {}
                cid = make_id(kind, f"threat:{i}:consequence:{j}")
                text, taglist, statuslist = self._consequence_text(doc, cq)
                items.append(self._gmmove(
                    _id, cid, short_label(cq.get("text") or f"Consequence {j + 1}"),
                    text, subtype="hard", hide_name=True, header="symbols",
                    sort=sort, super_move=soft_id, taglist=taglist, statuslist=statuslist))
                sort += 100

        # defaultTags / defaultStatuses are arrays of EmbeddedTagDM /
        # EmbeddedStatusDM objects (actor-types.ts:87-88), not strings.
        default_tags = []
        for t in fm.get("default_tags") or []:
            default_tags.append({
                "type": "tag", "name": str(t),
                "description": "", "locked": False, "version": DM_VERSION,
                "subtype": "story", "crispy": False, "hidden": False,
            })
        default_statuses = []
        for s in fm.get("default_statuses") or []:
            name, tier = parse_status(s)
            if tier == 0:
                self.warn(doc.slug, f"default status {s!r} has no `-tier` suffix; tier 0")
            default_statuses.append({
                "type": "status", "name": name,
                "description": "", "locked": False, "version": DM_VERSION,
                "tier": tier, "pips": 0, "hidden": False,
            })

        alias = str(fm.get("alias") or "").strip()
        scale = fm.get("scale", 0)
        try:
            scale = int(scale)
        except (TypeError, ValueError):
            scale = 0

        template_ids = []
        for ps in fm.get("power_sets") or []:
            e = self.index.get(str(ps))
            if e and e["pack"] == "power-sets":
                template_ids.append(e["id"])
            else:
                self.warn(doc.slug, f"power_sets entry {ps!r} has no emitted power-set "
                                    f"document; dropped from template_ids")

        return {
            "_id": _id,
            "_key": f"!actors!{_id}",
            "name": doc.name,
            "type": "threat",
            "img": doc_asset(doc) or IMG_ACTOR,
            "system": {
                # default_template() — actor-types.ts:5-15
                "locked": False,
                "biography": "",
                "description": self._threat_description(doc, is_template),
                "short_description": str(fm.get("short_description") or fm.get("applies_to") or ""),
                "gmnotes": self._threat_gmnotes(doc),
                "crewThemes": [],
                "version": DM_VERSION,
                # aliasable() — actor-types.ts:32-37
                "alias": alias,
                "useAlias": bool(alias),
                # themeHolder() — actor-types.ts:17-22
                "finalized": False,
                "mythos": "",
                # person() — actor-types.ts:40-47
                "logos": "",
                "age": 0,
                "residence": "",
                "pronouns": "",
                # ThreatSchema — actor-types.ts:84-88
                "is_template": is_template,
                "template_ids": template_ids,
                "collectiveSize": scale,
                "defaultTags": default_tags,
                "defaultStatuses": default_statuses,
            },
            "items": items,
            # The book's "alias" — what PCs see before they know what this is — is
            # the *token* name in this system, not `system.alias`:
            # `getDisplayedName()` (city-actor.ts:1237-1257) resolves token name ->
            # prototypeToken.name -> name and never reads `system.alias`, and the
            # threat sheet's "Alias" input is bound to `token.name`
            # (templates/parts/threat-sheet-header.html:5,7). `system.alias` above is
            # kept for round-trip fidelity only; on a threat it is inert (scene-tags.ts
            # repurposes it to hold a scene id on the scene-container actor).
            "prototypeToken": {
                "name": alias or doc.name,
                "actorLink": False,
                "displayName": 30 if alias else 0,
                "width": 1,
                "height": 1,
                "texture": {"src": doc_asset(doc) or IMG_ACTOR},
                "disposition": -1,
                "flags": {},
            },
            "effects": [],
            "folder": None,
            "sort": 0,
            "ownership": {"default": OWN_NONE},
            "flags": flags_for(doc),
            "_stats": stats_block(),
        }

    def _gmmove(self, actor_id, iid, name, description, *, subtype, hide_name,
                header, sort, super_move="", taglist=None, statuslist=None):
        """Embedded `gmmove` Item (item-types.ts:367-389 GMMove.defineSchema)."""
        assert subtype in MOVETYPES
        return {
            "_id": iid,
            "_key": f"!actors.items!{actor_id}.{iid}",
            "name": name,
            "type": "gmmove",
            "img": IMG_ITEM,
            "system": {
                "description": description,
                "locked": False,
                "version": DM_VERSION,
                "subtype": subtype,
                "taglist": taglist or [],
                "statuslist": statuslist or [],
                "hideName": hide_name,
                "header": header,
                "superMoveId": super_move,
            },
            "effects": [], "folder": None, "sort": sort,
            "ownership": {"default": OWN_NONE}, "flags": {}, "_stats": stats_block(),
        }

    def _move_text(self, doc, text):
        """Plain move prose. Wikilinks are flattened; braces would be read as the
        system's MC-private markup (city-helpers.ts removeWithinBraces), so they go."""
        return flatten_wikilinks(text).replace("{", "(").replace("}", ")").strip()

    def _consequence_text(self, doc, cq):
        """Consequence prose plus the system's `[name-tier]` / `[s:tag]` markup.

        `formatGMMoveText` (city-item.ts:1547-1581) builds the applied tag/status
        lists *only* from the description markup; `system.taglist` / `statuslist`
        are never read for that. So the markup in `description` is what matters;
        we still fill the datamodel lists so nothing is lost on a round-trip.
        """
        text = self._move_text(doc, cq.get("text") or "")
        statuslist, taglist, bits = [], [], []
        for s in cq.get("statuses") or []:
            name, tier = parse_status(s)
            statuslist.append(str(s))
            if markup_safe(name):
                text, done = _bracket_in_place(text, f"{name}-{tier}", "")
                if not done:
                    bits.append(f"[{name}-{tier}]")
            else:
                self.warn(doc.slug, f"consequence status {s!r} has characters the system's "
                                    f"tag regex rejects; markup omitted, statuslist kept")
        for t in cq.get("tags") or []:
            taglist.append(str(t))
            if markup_safe(t):
                # `s:` = scene tag (city-helpers.ts parseOptions:355-372); Consequence
                # tags are story tags created on the scene, as in the Zeus sample.
                text, done = _bracket_in_place(text, str(t), "s:")
                if not done:
                    bits.append(f"[s:{t}]")
            else:
                self.warn(doc.slug, f"consequence tag {t!r} has characters the system's "
                                    f"tag regex rejects (commas/apostrophes); markup omitted, "
                                    f"taglist kept")
        if bits:
            text = (text + " " + " ".join(bits)).strip()
        return text, taglist, statuslist

    def _threat_description(self, doc, is_template):
        fm = doc.fm
        h = []
        if is_template:
            h.append("<p><strong>Power Set (template threat)</strong></p>")
            if fm.get("applies_to"):
                h.append(f"<p><strong>Applies to:</strong> {esc(fm['applies_to'])}</p>")
        if fm.get("role"):
            h.append(f"<p><strong>Role:</strong> {esc(fm['role'])}</p>")
        if fm.get("category"):
            h.append(f"<p><strong>Category:</strong> {esc(fm['category'])}</p>")
        if fm.get("splat"):
            h.append(f"<p><strong>Splat:</strong> {esc(fm['splat'])}</p>")
        if fm.get("scale") is not None:
            h.append(f"<p><strong>Scale:</strong> {esc(fm['scale'])}</p>")
        if fm.get("reuse_of"):
            h.append(f"<p><strong>Adapts:</strong> {esc(fm['reuse_of'])}</p>")
        h.append(md_to_html(doc.body, self.linker))
        return "".join(h)

    def _threat_gmnotes(self, doc):
        h = [canon_line(doc)]
        if not doc.fm.get("player_safe"):
            h.insert(0, "<p><strong>MC-only.</strong> This profile is not marked "
                        "<code>player_safe</code> in the vault.</p>")
        return "".join(h)

    # -- loadout tag -------------------------------------------------------
    def loadout_tag(self, doc):
        """Item `tag`, subtype loadout (item-types.ts:162-199 TagDM)."""
        fm = doc.fm
        _id = self.index[doc.slug]["id"]
        tags = [str(t) for t in (fm.get("tags") or [])]
        flaws = [str(f) for f in (fm.get("flaws") or [])]
        h = [f"<p><strong>Catalog:</strong> {esc(fm.get('catalog',''))}</p>"]
        if tags:
            h.append("<p><strong>Tags:</strong> " +
                     ", ".join(f"<em>{esc(t)}</em>" for t in tags) + "</p>")
        if flaws:
            h.append("<p><strong>Flaws</strong> (weakness tags while the item is in "
                     "your Loadout): " + ", ".join(f"<em>{esc(f)}</em>" for f in flaws) + "</p>")
        h.append(f"<p><strong>Requires setup:</strong> "
                 f"{'yes' if fm.get('requires_setup') else 'no'}</p>")
        if fm.get("availability"):
            h.append(f"<p><strong>Availability:</strong> {esc(fm['availability'])}</p>")
        h.append(md_to_html(doc.body, self.linker))
        h.append(canon_line(doc))

        # `example0..2` are the themebook-question examples; we reuse them for the
        # item's own descriptor tags so they survive and are visible on the sheet.
        ex = {f"example{i}": (tags[i] if i < len(tags) else "") for i in range(3)}
        rest = {f"restriction{i}": (flaws[i] if i < len(flaws) else "") for i in range(3)}
        return {
            "_id": _id,
            "_key": f"!items!{_id}",
            "name": doc.name,
            "type": "tag",
            "img": doc_asset(doc) or IMG_ITEM,
            "system": {
                # tagCore() — item-types.ts:140-148
                "description": "".join(h),
                "locked": False,
                "version": DM_VERSION,
                "subtype": "loadout",
                "crispy": False,
                "hidden": False,
                # TagDM — item-types.ts:167-196
                "question": "",
                "question_letter": "",
                "category": "none",          # TAG_CATEGORY_LIST, config/tag-categories.ts:1-9
                "burn_state": 0,
                "burned": False,
                "is_bonus": False,
                "theme_id": None,
                "custom_tag": False,
                "broad": False,
                "temporary": False,
                "permanent": False,
                "parentId": None,
                "subtagRequired": False,
                "showcased": False,
                "activated_loadout": False,
                **ex,
                "counterexample0": "", "counterexample1": "", "counterexample2": "",
                **rest,
                "sceneId": None,
                "createdBy": [],
            },
            "effects": [],
            "folder": None,
            "sort": 0,
            "ownership": {"default": OWN_NONE},
            "flags": flags_for(doc),
            "_stats": stats_block(),
        }

    # -- journal -----------------------------------------------------------
    #: which frontmatter keys are rendered into the header table, per type
    HEADER_FIELDS = {
        "district": ["zone_code", "central_concept", "story_tag", "pillar", "caste_band",
                     "key_players_present", "mandatory_placement"],
        "key-player": ["kp_role", "specialty", "base_concept", "twist", "twist_source",
                       "agenda", "resources", "motifs", "key_characters", "challenges",
                       "territory", "vector_face"],
        "npc": ["handle", "affiliation", "splat", "role_in_pilot", "vector", "challenge"],
        "job": ["job_type", "sessions", "series_pole", "goal", "hooks", "vectors",
                "core_moments", "scenes", "climax", "aftermath", "twist_for_pivot",
                "key_players_touched", "districts_touched", "flashback_budget",
                "employer_vector", "complications"],
        "scene": ["job", "order", "set_piece", "district", "story_tags", "challenges",
                  "book_challenges", "vectors_active", "core_moment", "flashback_hooks",
                  "outcomes_to_next"],
        "character-trope": ["splat", "essence_target", "fixed_kits", "choice_kits", "loadout"],
        "pc-special": ["splat", "prerequisite", "persists_through_theme_replacement",
                       "removal", "improvement"],
        "crew-special": ["tied_to", "prerequisite", "persists_through_theme_replacement",
                         "improvement"],
        "membership": ["key_player", "self_kit", "self_kit_status", "specials"],
        "splat-overview": ["splat", "setting_name", "mapping_primary", "mapping_secondary",
                           "required_category", "required_themebook", "optional_categories",
                           "essence_minimum", "essence_targets", "motivation_rule",
                           "persistence", "required_primary", "optional_secondary",
                           "mc_only_section"],
        "index": ["job", "companion", "splat", "key_player", "vectors",
                  "advances_public_war"],
        "series": [],
    }

    def journal(self, doc):
        """Core `JournalEntry` with one text page. No system data model applies."""
        _id = self.index[doc.slug]["id"]
        pid = make_id(f"journals/{doc.slug}", "page:0")
        player_safe = bool(doc.fm.get("player_safe"))
        content = self._journal_html(doc)
        page = {
            "_id": pid,
            "_key": f"!journal.pages!{_id}.{pid}",
            "name": doc.name,
            "type": "text",
            "title": {"show": False, "level": 1},
            "text": {"format": 1, "content": content, "markdown": ""},
            "image": {},
            "video": {"controls": True, "volume": 0.5},
            "src": None,
            "system": {},
            "sort": 0,
            "ownership": {"default": OWN_INHERIT},
            "flags": flags_for(doc),
            "_stats": stats_block(),
        }
        return {
            "_id": _id,
            "_key": f"!journal!{_id}",
            "name": doc.name,
            "pages": [page],
            "categories": [],
            "folder": None,
            "sort": 0,
            # player_safe -> OBSERVER, otherwise NONE (WP9 ownership policy).
            "ownership": {"default": OWN_OBSERVER if player_safe else OWN_NONE},
            "flags": flags_for(doc),
            "_stats": stats_block(),
        }

    def _journal_html(self, doc):
        fm = doc.fm
        rows = []
        for key in self.HEADER_FIELDS.get(doc.type, []):
            if key not in fm:
                continue
            val = fm[key]
            if val in (None, "", [], {}):
                continue
            rows.append((key, self._fmt_value(val)))
        # validate.py enforces "H1 == name", so the body opens with its own title.
        # Drop it and use one injected H1, so the header table can sit under the
        # title rather than above it.
        body = re.sub(r"^\s*#\s+.*?(\n|$)", "", doc.body, count=1)
        h = [f"<h1>{esc(doc.name)}</h1>"]
        h.append(f"<p><em>{esc(doc.type)}</em> · "
                 f"<em>{'player-safe' if fm.get('player_safe') else 'MC-only'}</em></p>")
        if rows:
            h.append("<table><tbody>")
            for k, v in rows:
                h.append(f"<tr><th>{esc(k.replace('_', ' '))}</th><td>{v}</td></tr>")
            h.append("</tbody></table>")
        h.append(md_to_html(body, self.linker))
        h.append("<hr>")
        h.append(canon_line(doc))
        return "".join(h)

    def _fmt_value(self, val):
        if isinstance(val, list):
            return ", ".join(self._fmt_scalar(v) for v in val)
        if isinstance(val, dict):
            return "; ".join(f"<em>{esc(k)}</em>: {self._fmt_scalar(v)}" for k, v in val.items())
        return self._fmt_scalar(val)

    def _fmt_scalar(self, v):
        if isinstance(v, dict):
            return "; ".join(f"<em>{esc(k)}</em>: {self._fmt_scalar(x)}" for k, x in v.items())
        if isinstance(v, list):
            return ", ".join(self._fmt_scalar(x) for x in v)
        s = str(v)
        # A bare slug that names an emitted document becomes a link.
        if re.match(r"^[a-z0-9][a-z0-9\-]*$", s) and s in self.index:
            u = self.linker.uuid(s)
            if u:
                return f"@UUID[{u}]{{{esc(s)}}}"
        return escape_with_links(s, self.linker)


# ===========================================================================
# module.json
# ===========================================================================
PACK_META = [
    ("theme-kits", "Neon Black — Theme Kits", "Item",
     {"PLAYER": "OBSERVER", "ASSISTANT": "OWNER"}),
    ("challenges", "Neon Black — Challenges", "Actor",
     {"PLAYER": "NONE", "ASSISTANT": "OWNER"}),
    ("power-sets", "Neon Black — Power Sets", "Actor",
     {"PLAYER": "NONE", "ASSISTANT": "OWNER"}),
    ("loadout", "Neon Black — Street Catalog", "Item",
     {"PLAYER": "OBSERVER", "ASSISTANT": "OWNER"}),
    ("journals", "Neon Black — Megacity, Key Players & Jobs", "JournalEntry",
     {"PLAYER": "NONE", "ASSISTANT": "OWNER"}),
]


def write_module_json(path):
    mod = {
        "id": MODULE_ID,
        "title": MODULE_TITLE,
        "description": ("Neon Black — campaign content for City of Mist / Mist Engine "
                        "in Otherscape mode: theme kits, Challenges, Power Sets, a street "
                        "catalog and the Megacity, Key Player and Job journals."),
        "version": MODULE_VERSION,
        "authors": [{"name": "Neon Black build"}],
        "compatibility": {"minimum": FOUNDRY_MIN, "verified": FOUNDRY_VERIFIED,
                          "maximum": FOUNDRY_MAX},
        "relationships": {
            "systems": [{
                "id": SYSTEM_ID,
                "type": "system",
                "manifest": "https://raw.githubusercontent.com/taragnor/city-of-mist/master/src/city-of-mist/system.json",
                "compatibility": {"minimum": SYSTEM_VERSION, "verified": SYSTEM_VERSION},
            }],
        },
        "packs": [
            {"name": name, "label": label, "path": f"packs/{name}", "type": doctype,
             "system": SYSTEM_ID, "ownership": own}
            for name, label, doctype, own in PACK_META
        ],
        "packFolders": [{
            "name": MODULE_TITLE, "sorting": "m", "color": "#1b1b23",
            "packs": [name for name, *_ in PACK_META],
        }],
        "esmodules": [],
        "styles": [],
        "languages": [],
        "manifest": f"https://<host>/{MODULE_ID}/releases/latest/download/module.json",
        "download": f"https://<host>/{MODULE_ID}/releases/latest/download/{MODULE_ID}.zip",
    }
    write_json(path, mod)


MODULE_README = """# Neon Black — Foundry module (build output)

Generated by `tools/foundry/convert.py`. This folder is **build output**: it is
git-ignored, and it is regenerated in full on every run. Do not edit by hand.

## What is here

| Path | Contents |
|---|---|
| `module.json` | Module manifest for the `city-of-mist` system, Foundry {fmin}–{fmax}. |
| `packs/theme-kits/_source/` | Item `themekit` — splat kits, Self kits, crew kits. |
| `packs/challenges/_source/` | Actor `threat` with embedded `spectrum` / `gmmove` Items. |
| `packs/power-sets/_source/` | Actor `threat` with `is_template: true` (overlays). |
| `packs/loadout/_source/` | Item `tag`, `subtype: loadout` — the street catalog. |
| `packs/journals/_source/` | `JournalEntry` — districts, Key Players, NPCs, Jobs, scenes, tropes, Specials, indexes. |
| `ids.json` | slug → document id map (deterministic; see convert.py's header). |
| `report.json` | Per-pack counts, skipped vault files, and field warnings. |

`_source/*.json` is the **unpacked** form. Nothing here is a LevelDB pack yet;
see `tools/foundry/README.md` for the packing step.

## Requirements in the world

* System **{sysid}** v{sysver} (Taragnor), switched to **Otherscape** mode.
* Client setting **autoEssence** (default on) if you want Essence auto-assigned.

Nothing in this module replaces book content; every kit and Challenge is
additional.
""".format(fmin=FOUNDRY_MIN, fmax=FOUNDRY_MAX, sysid=SYSTEM_ID, sysver=SYSTEM_VERSION)


# ===========================================================================
# driver
# ===========================================================================
def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2, ensure_ascii=False, sort_keys=False)
        fh.write("\n")


def safe_filename(slug):
    return re.sub(r"[^A-Za-z0-9._-]", "_", slug)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Neon Black -> city-of-mist compendium source")
    ap.add_argument("--all", action="store_true", help="emit every pack and module.json")
    ap.add_argument("--theme-kits", action="store_true")
    ap.add_argument("--challenges", action="store_true")
    ap.add_argument("--power-sets", action="store_true")
    ap.add_argument("--loadout", action="store_true")
    ap.add_argument("--journals", action="store_true")
    ap.add_argument("--module", action="store_true", help="emit module.json + README only")
    ap.add_argument("--uuid-style", choices=("compendium", "world"), default="compendium",
                    help="compendium (default): @UUID[Compendium.neon-black.<pack>.<Class>.<id>]; "
                         "world: @UUID[<Class>.<id>] (resolves only after import)")
    ap.add_argument("--out", default=BUILD, help="output directory (default: build/)")
    args = ap.parse_args(argv)

    wanted = set()
    for flag, pack in (("theme_kits", "theme-kits"), ("challenges", "challenges"),
                       ("power_sets", "power-sets"), ("loadout", "loadout"),
                       ("journals", "journals")):
        if getattr(args, flag):
            wanted.add(pack)
    if args.all or (not wanted and not args.module):
        wanted = set(PACK_DOCCLASS)

    os.chdir(ROOT)
    if args.all:
        # ship the vault's images with the module (WP-I): assets/ -> build/assets/, minus the
        # manifest and the unkeyed chroma originals
        import shutil
        src, dst = os.path.join(ROOT, "assets"), os.path.join(args.out, "assets")
        if os.path.isdir(src):
            if os.path.isdir(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns("manifest.md", "npcs-raw", "*.jpg"))
    docs, skipped = read_vault()

    # ---- pass 1: index every document that will be emitted (ids first, so
    # wikilinks can resolve forward references).
    index, id_owner = {}, {}
    emit_docs = []
    for d in docs:
        if not convertible(d, skipped):
            continue
        pack = PACK_OF_TYPE[d.type]
        _id = make_id(pack, d.slug)
        if _id in id_owner:
            print(f"FATAL: id collision {_id}: {id_owner[_id]} vs {d.slug}", file=sys.stderr)
            return 3
        id_owner[_id] = d.slug
        if d.slug in index:
            print(f"FATAL: duplicate slug {d.slug}", file=sys.stderr)
            return 3
        index[d.slug] = {"id": _id, "pack": pack, "cls": PACK_DOCCLASS[pack],
                         "type": d.type, "path": d.path,
                         "page": make_id(f"journals/{d.slug}", "page:0")
                                 if pack == "journals" else None}
        emit_docs.append(d)

    report = {"warnings": [], "skipped": skipped, "counts": {}, "unresolved_links": {}}
    linker = Linker(index, args.uuid_style)
    em = Emitter(index, linker, report)

    out = os.path.abspath(args.out)
    counts = collections.Counter()

    if args.module or wanted:
        write_module_json(os.path.join(out, "module.json"))
        with open(os.path.join(out, "README.md"), "w", encoding="utf-8") as fh:
            fh.write(MODULE_README)

    for d in emit_docs:
        pack = index[d.slug]["pack"]
        if pack not in wanted:
            continue
        if pack == "theme-kits":
            obj = em.themekit(d)
        elif pack == "challenges":
            obj = em.threat(d, is_template=False)
        elif pack == "power-sets":
            obj = em.threat(d, is_template=True)
        elif pack == "loadout":
            obj = em.loadout_tag(d)
        else:
            obj = em.journal(d)
        write_json(os.path.join(out, "packs", pack, "_source",
                                safe_filename(d.slug) + ".json"), obj)
        counts[pack] += 1

    report["counts"] = dict(sorted(counts.items()))
    report["unresolved_links"] = dict(sorted(linker.unresolved.items()))
    report["id_scheme"] = ("sha1('neon-black:<kind>:<key>') -> base62 -> last 16 chars; "
                           "kind = pack name for top-level docs, '<pack>/<slug>' for "
                           "embedded items and journal pages")
    report["uuid_style"] = args.uuid_style
    write_json(os.path.join(out, "report.json"), report)
    write_json(os.path.join(out, "ids.json"), dict(sorted(index.items())))

    print(f"Neon Black -> Foundry ({SYSTEM_ID} {SYSTEM_VERSION}, Otherscape)")
    print(f"  out: {out}")
    for pack in sorted(PACK_DOCCLASS):
        mark = counts.get(pack, 0) if pack in wanted else "-"
        print(f"  {pack:<12} {PACK_DOCCLASS[pack]:<12} {mark}")
    print(f"  total documents: {sum(counts.values())}")
    print(f"  skipped vault files: {len(skipped)}")
    print(f"  warnings: {len(report['warnings'])}")
    print(f"  unresolved wikilink targets: {len(linker.unresolved)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
