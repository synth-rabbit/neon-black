#!/usr/bin/env python3
"""WP8: draft one-line descriptions for every file, per top-level folder, from frontmatter (for the MOCs, BC-178).
Prints markdown lines; the MOC files were assembled from this output and hand-finished."""
import glob, re, yaml, os, sys, collections
def first_para(body):
    body = re.sub(r'^# .*\n', '', body, count=1)
    for para in re.split(r'\n\s*\n', body):
        s = para.strip()
        if not s or s.startswith(('#', '|', '>', '-', '*', '```', '!')): continue
        s = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', s); s = re.sub(r'\[\[([^\]]+)\]\]', r'\1', s)
        s = re.sub(r'\*\*|\*|`', '', s)
        return re.split(r'(?<=[.!?])\s+(?=[A-Z])', s)[0][:220]
    return ''
def one_line(fm, body):
    ty = fm['type']
    if ty == 'theme-kit': return f"{fm.get('themebook')} kit ({fm.get('category')}); {fm.get('motivation_type')}: *{fm.get('motivation','').rstrip('.')}*"
    if ty == 'crew-kit': return f"Crew kit; {fm.get('motivation_type')}: *{fm.get('motivation','').rstrip('.')}*"
    if ty == 'character-trope': return f"Trope — fixed {', '.join(fm.get('fixed_kits',[]))}; choice {', '.join(fm.get('choice_kits',[]))}"
    if ty in ('pc-special','crew-special'): return f"Special — prerequisite: {str(fm.get('prerequisite','')).rstrip('.')}"
    if ty == 'power-set': return f"Power Set — applies to {fm.get('applies_to') or first_para(body)}"
    if ty == 'challenge': return f"{fm.get('role')}, Scale {fm.get('scale')} — {fm.get('short_description') or first_para(body)}"
    if ty == 'npc':
        h = ('"%s" — ' % fm['handle']) if fm.get('handle') else ''
        return h + str(fm.get('role_in_pilot',''))
    if ty == 'key-player': return f"{fm.get('base_concept','')}"
    if ty == 'district': return f"{fm.get('zone_code')} — {fm.get('central_concept','')} Story tag: *{fm.get('story_tag')}*"
    if ty == 'loadout-item': return f"{fm.get('catalog')} — {', '.join('*'+t+'*' for t in fm.get('tags',[])[:3])}; flaws {', '.join(fm.get('flaws',[])) or '—'}"
    if ty == 'scene': return f"{fm.get('order')} · {fm.get('district')} · {'core moment · ' if fm.get('core_moment') else ''}{fm.get('set_piece','')}"
    if ty == 'job': return f"{', '.join(fm.get('job_type',[]))}; {fm.get('sessions')} session(s); pole {fm.get('series_pole')}; pivot twist {fm.get('twist_for_pivot')} — {fm.get('goal','')}"
    return first_para(body)
folder = sys.argv[1]
for p in sorted(glob.glob(f'{folder}/**/*.md', recursive=True)):
    t = open(p, encoding='utf-8').read(); m = re.match(r'^---\n(.*?)\n---\n(.*)$', t, re.S)
    fm = yaml.safe_load(m.group(1)); body = m.group(2)
    print(f"| [[{fm['slug']}]] | {fm['type']} | {'✓' if fm.get('player_safe') else '—'} | {one_line(fm, body)} |   <!-- {os.path.dirname(p)} -->")
