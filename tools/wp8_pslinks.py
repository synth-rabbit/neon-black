#!/usr/bin/env python3
"""WP8: make every [[link]] in a player_safe: true file target a player_safe: true file (Plan C.8, BC-175).
Registers, MC-only overlays and MC-only series files become code-span citations; districts and public
Key Players are re-pointed at the matching section of palisade-player-primer; secret groups become plain text."""
import re, glob, os, yaml
PRIMER = {
 'palisade':'The Wall','aurelian-crest':'Aurelian Crest','chancery-hill':'Chancery Hill','meliora-terraces':'Meliora Terraces',
 'orison-reach':'Orison Reach','amalgam-stack':'Amalgam Stack','the-lattice':'The Lattice','corbel-gallery':'Corbel Gallery',
 'halloran-circus':'Halloran Circus','suture-row':'Suture Row','gullet-market':'Gullet Market','marlow-blocks':'Marlow Blocks',
 'cinder-yards':'Cinder Yards','relay-fields':'Relay Fields','kilbride-stretch':'Kilbride Stretch','lowmere-sinks':'Lowmere Sinks',
 'foundation-galleries':'Foundation Galleries','ferrante-basin':'Ferrante Basin','coldwater-outfall':'Coldwater Outfall',
 'corp-a':'Meliora Bioworks','corp-b':'Orison Defense Systems','corp-c':'Amalgamated Prosthetic & Interface',
 'upstart':'Continuity Risk & Response','government':'The Chancery','syndicate':'The Almoners and the Kitchen','packs':'The Run',
 'tao-society':'The Quiet Hand','fence-network':'The Weighhouse','marisol-okonkwo':'The Weighhouse','tomas-adair':'Rook',
}
DISPLAY = dict(PRIMER); DISPLAY.update({'palisade':'Palisade','corp-c':'AP&I','tao-society':'the Wuji','fence-network':"Tally's network",
 'marisol-okonkwo':'Tally','syndicate':'the Almoners','packs':'the Run','government':'the Chancery','upstart':'Continuity','corp-a':'Meliora','corp-b':'Orison'})
PLAIN = {'changeling-cells':'the Cutloose'}   # secret groups: plain text, no link
files = [p for p in glob.glob('**/*.md', recursive=True) if not p.startswith(('ref/','tools/','.git/','00-meta/additions/','99-templates/'))]
fm = {}
for p in files:
    t = open(p, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    if m: fm[p] = yaml.safe_load(m.group(1)) or {}
ps = {os.path.basename(p)[:-3]: fm[p].get('player_safe') is True for p in fm}
n = 0
for p in files:
    if fm.get(p, {}).get('player_safe') is not True: continue
    t = open(p, encoding='utf-8').read()
    head, body = t.split('\n---\n', 1)
    def rep(m):
        tgt, alias = m.group(1).strip(), m.group(2)
        if tgt.startswith('assets/') or ps.get(tgt): return m.group(0)
        if tgt in PRIMER:
            disp = alias if alias else DISPLAY[tgt]
            return f'[[palisade-player-primer#{PRIMER[tgt]}|{disp}]]'
        if tgt in PLAIN: return alias if alias else PLAIN[tgt]
        return alias if alias else f'`{tgt}`'
    body2 = re.sub(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]', rep, body)
    if body2 != body:
        open(p, 'w', encoding='utf-8').write(head + '\n---\n' + body2); n += 1
print('rewrote', n, 'files')
