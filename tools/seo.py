"""SEO pass for the setup guides. Run after adding or editing any guide:  python3 tools/seo.py
- adds schema.org JSON-LD (TechArticle about the repo + breadcrumbs) to every tools/*/index.html
- points og:image at the tool's reel cover
- rewrites sitemap.xml with <lastmod> dates from git
Safe to re-run: the injected block is replaced, not duplicated."""
import glob, html, json, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://aixsam.dev'
os.chdir(ROOT)


def git_date(path, first=False):
    args = ['git', 'log', '--format=%cI', '--', path]
    out = subprocess.run(args, capture_output=True, text=True).stdout.split()
    return (out[-1] if first else out[0])[:10] if out else None


def text(rx, s):
    m = re.search(rx, s, re.S)
    return html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else ''


for f in sorted(glob.glob('tools/*/index.html')):
    slug = f.split('/')[1]
    s = open(f, encoding='utf-8').read()
    url = f'{SITE}/tools/{slug}/'
    title, desc = text(r'<title>(.*?)</title>', s), text(r'<meta name="description" content="(.*?)"', s)
    name = text(r'<h1>(.*?)</h1>', s) or title.split(':')[0]
    key = text(r'Reel keyword: ([A-Z]+)', s).lower()
    repo = re.search(r'href="(https://github\.com/[^/"#]+/[^/"#]+)', s)
    cover = f'{SITE}/img/covers/{key}.webp' if key and os.path.exists(f'img/covers/{key}.webp') else f'{SITE}/img/icon.png'
    org = {'@type': 'Organization', 'name': 'aixsam.dev', 'url': SITE + '/', 'logo': SITE + '/img/icon.png'}
    art = {'@type': 'TechArticle', '@id': url + '#guide', 'headline': title.split(' · ')[0], 'description': desc, 'url': url,
           'mainEntityOfPage': url, 'image': cover, 'inLanguage': 'en', 'author': org, 'publisher': org,
           'datePublished': git_date(f, first=True), 'dateModified': git_date(f)}
    if repo:
        art['about'] = {'@type': 'SoftwareSourceCode', 'name': name, 'codeRepository': repo.group(1)}
    faqs = re.findall(r'<details><summary>(.*?)</summary><div><p>(.*?)</p></div></details>', s.split('<section class="faq2">', 1)[1].split('</section>', 1)[0]) if '<section class="faq2">' in s else []
    faq = {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': html.unescape(re.sub(r'<[^>]+>', '', q)),
           'acceptedAnswer': {'@type': 'Answer', 'text': html.unescape(re.sub(r'<[^>]+>', '', a_))}} for q, a_ in faqs]}
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'aixsam.dev', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Setup guides', 'item': SITE + '/tools/'},
        {'@type': 'ListItem', 'position': 3, 'name': name, 'item': url}]}
    block = ('<script type="application/ld+json" id="seo">' +
             json.dumps({'@context': 'https://schema.org', '@graph': [art, crumbs] + ([faq] if faqs else [])}, ensure_ascii=False) + '</script>')
    s = re.sub(r'<script type="application/ld\+json" id="seo">.*?</script>\n?', '', s, flags=re.S)
    s = s.replace('</head>', block + '\n</head>', 1)
    s = re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="{cover}">', s)
    open(f, 'w', encoding='utf-8').write(s)
    assert s.count('id="seo"') == 1, f

pages = ['index.html', 'tools/index.html'] + sorted(glob.glob('tools/*/index.html'))
rows = []
for p in pages:
    loc = SITE + '/' + p.replace('index.html', '')
    mod = git_date(p)
    rows.append(f'  <url><loc>{loc}</loc>' + (f'<lastmod>{mod}</lastmod>' if mod else '') + '</url>')
open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                               + '\n'.join(rows) + '\n</urlset>\n')
print(f'seo: {len(pages) - 2} guides tagged, sitemap has {len(rows)} urls')
