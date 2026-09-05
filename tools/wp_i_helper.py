#!/usr/bin/env python3
"""WP-I helper script for Neon Black image generation, asset ingestion, and vault linking."""

import os
import re
import sys
import glob
import json
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAIN_DIR = "/Users/pandorz/.gemini/antigravity-ide/brain/b1ea50dd-e7aa-46fd-ad02-ca31e15b7a3a"

PREAMBLE_BASE = (
    "Cyberpunk megacity illustration. Painterly concept art, grounded and worn rather than glossy: "
    "film grain, scuffed surfaces, visible seams on chrome, wet reflections, industrial scale. "
    "Palette: neon over concrete — sodium orange, arc-lamp white, bruise violet, coolant green, "
    "blood-black, wet asphalt, rust, oxidized copper; surgical teal and warranty-card cream in the corporate tiers; "
    "bone and chrome at the top. Lighting: rain-scattered, underlit, backlit by advertising, tier-shadowed; "
    "floodlit checkpoints, flickering strip light, emergency red, clinic fluorescent. The lower the tier, the fewer the colors. "
    "No readable text, no logos of real companies, no watermarks, no photoreal faces, no mythological or religious iconography, "
    "no gods, angels, demons, dragons or creatures of any culture's legend."
)

PREAMBLE_VARIANTS = {
    "<preamble, establishing>": (
        PREAMBLE_BASE + " Wide establishing shot, 16:9. The Wall — a kilometre-high escarpment of stacked construction — reads as enormous wherever it is in frame."
    ),
    "<preamble, emblem>": (
        PREAMBLE_BASE + " Flat vector emblem on a plain neutral background, a single shape, two colors, no lettering, 1:1."
    ),
    "<preamble, puppet>": (
        PREAMBLE_BASE + " Full-body standing figure, head to feet fully in frame, facing three-quarters toward the viewer, isolated on a flat pure green #00FF00 background. No ground shadow, no scenery, no props or clothing touching the frame edge, portrait orientation 2:3. Not a token. Face rendered painterly, not photoreal."
    )
}

STANDING_NEGATIVE = (
    "Standing negative list: readable text, real brands, watermarks, legend-Mythos iconography, "
    "halos, runes, magic circles, glowing eyes, photoreal faces, clean chrome-perfect surfaces, anime brightness."
)


def get_tasks():
    content = open(os.path.join(ROOT, "00-meta/image-briefs.md"), encoding="utf-8").read()
    blocks = re.findall(
        r"^### (assets/[^\n]+)\ntarget: \[\[(.*?)\]\]\naspect: ([^\n]+)\nprompt: ([^\n]+)\nnegative: ([^\n]+)",
        content,
        re.M
    )

    files = {
        os.path.basename(p)[:-3]: p
        for p in glob.glob(os.path.join(ROOT, "**/*.md"), recursive=True)
        if not p.startswith((
            os.path.join(ROOT, "ref/"),
            os.path.join(ROOT, "tools/"),
            os.path.join(ROOT, ".git/"),
            os.path.join(ROOT, ".claude/"),
            os.path.join(ROOT, "00-meta/additions/"),
            os.path.join(ROOT, "build/")
        ))
    }

    tasks = []
    for idx, (path, tgt, asp, pr, neg) in enumerate(blocks):
        m = re.match(r"(<[^>]+>)\s*(.*)", pr)
        tag, body = m.group(1), m.group(2)
        full_prompt = f"{PREAMBLE_VARIANTS[tag]} {body} {STANDING_NEGATIVE} Negative: {neg}"

        # generate a short identifier (max 3 words)
        slug = os.path.splitext(os.path.basename(path))[0].replace("-", "_")
        parts = slug.split("_")
        if len(parts) > 3:
            img_name = "_".join(parts[-2:] if "scene" in parts or "emblem" in parts else parts[:2])
            if len(img_name.split("_")) > 3:
                img_name = "_".join(img_name.split("_")[:3])
        else:
            img_name = slug

        is_puppet = "<preamble, puppet>" in tag
        method = "chroma" if is_puppet else "—"

        tasks.append({
            "idx": idx,
            "asset_path": path,
            "target_slug": tgt,
            "target_file": files.get(tgt),
            "aspect": asp,
            "full_prompt": full_prompt,
            "img_name": img_name,
            "is_puppet": is_puppet,
            "method": method
        })
    return tasks


def save_image_as_png(src_jpg_path, dest_png_path, is_puppet=False):
    os.makedirs(os.path.dirname(dest_png_path), exist_ok=True)
    with Image.open(src_jpg_path) as img:
        img = img.convert("RGBA")
        img.save(dest_png_path, "PNG")
    print(f"Saved: {dest_png_path}")


def embed_assets_in_vault():
    tasks = get_tasks()
    # Group assets by target file
    by_target = {}
    for t in tasks:
        tgt_file = t["target_file"]
        if not tgt_file:
            print(f"Warning: target file not found for {t['target_slug']}")
            continue
        by_target.setdefault(tgt_file, []).append(t["asset_path"])

    embedded_count = 0
    for tgt_file, asset_paths in by_target.items():
        with open(tgt_file, "r", encoding="utf-8") as f:
            content = f.read()

        missing_embeds = [p for p in asset_paths if f"![[{p}]]" not in content]
        if not missing_embeds:
            continue

        embed_block = "\n\n".join(f"![[{p}]]" for p in missing_embeds)
        lines = content.split("\n")

        # Find first H2 heading
        h2_idx = -1
        for i, line in enumerate(lines):
            if line.startswith("## "):
                h2_idx = i
                break

        if h2_idx != -1:
            new_lines = lines[:h2_idx]
            if new_lines and new_lines[-1].strip() != "":
                new_lines.append("")
            new_lines.append(embed_block)
            new_lines.append("")
            new_lines.extend(lines[h2_idx:])
            new_content = "\n".join(new_lines)
            new_content = re.sub(r"\n{3,}", "\n\n", new_content)
            with open(tgt_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            embedded_count += len(missing_embeds)
            print(f"Embedded in {tgt_file}: {missing_embeds}")
        else:
            print(f"Warning: No H2 found in {tgt_file}")

    print(f"Total embeds placed: {embedded_count}")


def update_manifest():
    manifest_path = os.path.join(ROOT, "assets/manifest.md")
    with open(manifest_path, "r", encoding="utf-8") as f:
        content = f.read()

    tasks = get_tasks()
    for t in tasks:
        path = t["asset_path"]
        # Check if file exists in assets
        full_dest = os.path.join(ROOT, path)
        if os.path.exists(full_dest):
            status = "generated"
            method = t["method"]
            # Find and replace line in manifest
            # Pattern: | `assets/...` | ... | [[tgt]] | asp | method | status |
            pattern = rf"(\| `{re.escape(path)}` \| [^|]+ \| [^|]+ \| [^|]+ \|) [^|]+ (\|) [^|]+ (\|)"
            replacement = rf"\1 {method} \2 {status} \3"
            content = re.sub(pattern, replacement, content)

    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated assets/manifest.md")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "embed":
        embed_assets_in_vault()
    elif len(sys.argv) > 1 and sys.argv[1] == "manifest":
        update_manifest()
    elif len(sys.argv) > 1 and sys.argv[1] == "tasks":
        tasks = get_tasks()
        print(json.dumps(tasks, indent=2))

def ingest_latest(image_name, dest_path, is_puppet=False):
    pattern = os.path.join(BRAIN_DIR, f"{image_name}_*.jpg")
    matches = glob.glob(pattern)
    if not matches:
        # also check exact image_name
        pattern = os.path.join(BRAIN_DIR, f"*{image_name}*.jpg")
        matches = glob.glob(pattern)
    if not matches:
        print(f"Error: no match for {image_name} in {BRAIN_DIR}")
        return False
    # pick newest
    matches.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    newest = matches[0]
    save_image_as_png(newest, os.path.join(ROOT, dest_path), is_puppet)
    return True
