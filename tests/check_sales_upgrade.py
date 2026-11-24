"""Dependency-free checks for sales links and preservation of support assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote, parse_qs
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.anchors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            assert attrs['id'] not in self.ids, 'Duplicate id'
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == 'a':
            self.anchors.append(attrs)

pages = {}
for path in ROOT.rglob('*.html'):
    page = Page()
    page.feed(path.read_text())
    pages[path.resolve()] = page

count = 0
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir():
            target /= 'index.html'
        assert target.is_file(), f'Missing target: {path}: {link}'
        if url.fragment and target in pages:
            assert url.fragment in pages[target].ids, f'Missing fragment: {link}'
        count += 1

product = ROOT / 'support/kit001/index.html'
buy = [a for a in pages[product.resolve()].anchors if a.get('href') == 'https://www.amazon.com/dp/B0HGZ3ZXWM']
assert len(buy) == 1
assert buy[0]['target'] == '_blank'
assert {'noopener', 'noreferrer'} <= set(buy[0]['rel'].split())
assert 'Complete your purchase on Amazon.' in product.read_text()
assert 'Installation &amp; Support' in product.read_text()
assert 'product-support' in pages[product.resolve()].ids

wholesale = pages[(ROOT / 'wholesale/index.html').resolve()]
emails = [a['href'] for a in wholesale.anchors if a.get('href', '').startswith('mailto:') and '?' in a['href']]
assert len(emails) == 1
mail = urlsplit(emails[0])
assert mail.path == 'support@grexvan.com'
query = parse_qs(mail.query)
assert query['subject'] == ['GREXVAN Wholesale Inquiry - GV-KIT-001']
assert 'Estimated order quantity' in query['body'][0]
ET.parse(ROOT / 'sitemap.xml')

# Only intended page additions are allowed; fitment, installation and photos stay byte-identical.
preserved = ['support/kit001/fitment/index.html', 'support/kit001/installation/index.html',
             'support/kit001/video/index.html', 'support/cf001/fitment/index.html',
             'support/ef001/fitment/index.html']
preserved += [p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.jpg')]
for name in preserved:
    old = subprocess.check_output(['git', 'show', '0f3a2c4b80f98e19f7866850394805ed6c40a27b:' + name], cwd=ROOT)
    assert old == (ROOT / name).read_bytes(), f'Protected asset changed: {name}'

print(f'PASS: {len(pages)} pages; {count} internal links, assets and fragments.')
print(f'PASS: Amazon URL/new-tab behavior, disclosure, wholesale email, sitemap and {len(preserved)} unchanged support/image files.')
