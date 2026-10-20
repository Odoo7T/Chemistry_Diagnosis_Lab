import re

with open('static/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

with open('templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ids_in_js = re.findall(r'document\.getElementById\(["\']([^"\']+)["\']\)', js)
ids_in_html = set(re.findall(r'id=["\']([^"\']+)["\']', html))

missing = [i for i in sorted(set(ids_in_js)) if i not in ids_in_html]
print('Missing IDs in HTML:', missing)
print('Total IDs in JS:', len(set(ids_in_js)))

