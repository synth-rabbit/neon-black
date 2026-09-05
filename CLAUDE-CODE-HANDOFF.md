# Claude Code handoff — publish Neon Black to GitHub and cut the Foundry release

Open Claude Code in this folder (`neon black/`) and paste the prompt below. Claude Code runs with your own git and `gh` credentials, which the Cowork session did not have.

## Prompt to paste

> This folder is the Neon Black campaign vault (Obsidian vault + Foundry module sources). The GitHub repo `https://github.com/synth-rabbit/neon-black` exists and is empty. Do the following, checking each step before the next:
>
> 1. Run `gh auth status` and `git config user.name` / `user.email`; stop and tell me if either is missing.
> 2. Confirm `.gitignore` excludes `*.pdf`, `*.zip`, `dist/`, `build/`, `ref/`, `.claude/`. Run `git status --short | head` after `git init -b main` and make sure no PDF, zip, or `dist/`/`build/` path is staged — the two rulebook PDFs must never be committed.
> 3. `git add -A && git commit -m "Neon Black vault: campaign content, tools, assets (build through WP-I)"`, `git remote add origin https://github.com/synth-rabbit/neon-black.git`, `git push -u origin main`.
> 4. Cut the Foundry release from the already-packed module in `dist/`: `cp dist/neon-black-v0.1.0.zip dist/neon-black.zip`, then
>    `gh release create v0.1.0 dist/neon-black.zip dist/module.json --repo synth-rabbit/neon-black --title "Neon Black 0.1.0" --notes "First packaged build: 35 theme kits, 48 Challenges, 14 Power Sets, 30 loadout items, 186 journals, 88 images."`
> 5. Verify: `curl -sL https://github.com/synth-rabbit/neon-black/releases/latest/download/module.json | python3 -c "import json,sys; m=json.load(sys.stdin); print(m['id'], m['version'], m['download'])"` must print `neon-black 0.1.0` and the v0.1.0 zip URL; then `curl -sIL <that download URL> | grep -i '^content-length'` must show ~143 MB.
> 6. Report the manifest URL to paste into Sqyre's Module Manager.
>
> Do not modify any vault content. Do not commit `dist/`, `build/`, or the PDFs.

## After it's live

Sqyre → Module Manager → install by manifest URL:
`https://github.com/synth-rabbit/neon-black/releases/latest/download/module.json`
Enable in a world running `city-of-mist` (v4.5.3+) in Otherscape mode with automatic Essence on. Then run the four first-world checks in `tools/foundry/README.md` (OQ-57–60).

## Future releases

`python3 tools/foundry/convert.py --all` → pack with the Foundry CLI (steps in `tools/foundry/README.md`) → bump `version` in `module.json` → new tag `vX.Y.Z` with `neon-black.zip` + `module.json` attached. The `releases/latest/download/module.json` manifest URL never changes.
