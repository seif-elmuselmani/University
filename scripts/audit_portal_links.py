import os
import re

portal_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'portal')
menu_file = os.path.join(portal_dir, 'js', 'mega-menu.js')

print(f"Portal directory: {portal_dir}")
print(f"Mega menu file: {menu_file}")

with open(menu_file, 'r', encoding='utf-8') as f:
    menu_content = f.read()

hrefs = set(re.findall(r'url:\s*[\'"]([^\'"]+)[\'"]', menu_content))
hrefs.update(re.findall(r'href=[\'"]([^\'"]+)[\'"]', menu_content))
print(f"Total unique menu links found: {len(hrefs)}")

missing = []
for h in sorted(hrefs):
    if h.startswith('javascript:') or h.startswith('http') or h == '#':
        continue
    if '#' in h:
        page, anchor = h.split('#', 1)
        if not page:
            continue
        page_path = os.path.join(portal_dir, page)
        if not os.path.exists(page_path):
            missing.append(f"PAGE MISSING: {h} -> {page_path}")
        else:
            with open(page_path, 'r', encoding='utf-8') as pf:
                pcontent = pf.read()
            if not re.search(r'id=[\'"]' + re.escape(anchor) + r'[\'"]', pcontent, re.IGNORECASE):
                missing.append(f"ANCHOR MISSING: {h} (Anchor #{anchor} not found in {page})")
    else:
        page_path = os.path.join(portal_dir, h)
        if not os.path.exists(page_path):
            missing.append(f"PAGE MISSING: {h}")

print(f"\n--- MEGA MENU AUDIT RESULTS ---")
print(f"Missing items: {len(missing)}")
for m in missing:
    print(" [!]", m)

# Also scan all HTML files for any broken relative links
print(f"\n--- GLOBAL HTML LINK AUDIT ---")
all_html_files = [f for f in os.listdir(portal_dir) if f.endswith('.html')]
global_missing = []

for hf in all_html_files:
    hf_path = os.path.join(portal_dir, hf)
    with open(hf_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find static href="..." (not :href="...")
    file_hrefs = re.findall(r'(?<!:)href=[\'"]([^\'"]+)[\'"]', content)
    for fh in file_hrefs:
        if fh.startswith('http://') or fh.startswith('https://') or fh.startswith('mailto:') or fh.startswith('tel:') or fh.startswith('javascript:') or fh == '#' or not fh.strip():
            continue
        if fh.startswith('#'):
            anchor = fh[1:]
            if not re.search(r'id=[\'"]' + re.escape(anchor) + r'[\'"]', content, re.IGNORECASE):
                global_missing.append(f"In {hf}: Internal anchor #{anchor} missing")
        elif '#' in fh:
            target_page, anchor = fh.split('#', 1)
            target_path = os.path.join(portal_dir, target_page)
            if not os.path.exists(target_path):
                global_missing.append(f"In {hf}: Target page {target_page} missing ({fh})")
            else:
                with open(target_path, 'r', encoding='utf-8') as tpf:
                    target_content = tpf.read()
                if not re.search(r'id=[\'"]' + re.escape(anchor) + r'[\'"]', target_content, re.IGNORECASE):
                    global_missing.append(f"In {hf}: Target anchor #{anchor} missing in {target_page}")
        else:
            target_path = os.path.join(portal_dir, fh)
            if not os.path.exists(target_path) and not fh.startswith('css/') and not fh.startswith('js/') and not fh.startswith('img/') and not fh.startswith('assets/'):
                global_missing.append(f"In {hf}: Relative link to {fh} not found")

print(f"Global HTML missing/broken link targets: {len(global_missing)}")
for gm in global_missing:
    print(" [*]", gm)
