"""Build the site: posts/<slug>.md -> <slug>/index.html, plus the record at index.html

Usage: python3 build.py

Side A is the music series by date, Side B everything else. Drafts (draft: true) get a page
at their URL but stay off the record. slug-en is the English version of slug: it shares the
track, but isn't a track of its own.
"""
import glob, html, json, os, re, subprocess, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
RESERVED = {'images', 'posts', 'src'}
WORDS_PER_MIN = 175


def read_post(path):
    s = open(path).read()
    fm, body = re.match(r'---\n(.*?)\n---\n(.*)', s, re.S).groups()
    meta = {}
    for line in fm.split('\n'):
        if ': ' in line and not line.startswith(' '):
            k, v = line.split(': ', 1)
            meta[k] = v.strip().strip('"')
    meta['slug'] = os.path.basename(path)[:-3]
    meta['draft'] = meta.get('draft') == 'true'
    return meta, body


def load_posts():
    posts = {}
    for p in glob.glob(os.path.join(ROOT, 'posts', '*.md')):
        meta, body = read_post(p)
        assert meta['slug'] not in RESERVED, f'slug {meta["slug"]} clashes with a site folder'
        posts[meta['slug']] = (meta, body)
    return posts


def translations(slugs):
    pairs = {}
    for s in slugs:
        if s.endswith('-en') and s[:-3] in slugs:
            pairs[s] = s[:-3]
            pairs[s[:-3]] = s
    return pairs


def tracklist(posts, pairs):
    """The published tracks on each side, oldest first: their numbers never change."""
    metas = [m for m, _ in posts.values() if not m['draft'] and not (m['slug'].endswith('-en') and m['slug'] in pairs)]
    by_date = lambda m: m.get('date', '')
    return {'A': sorted([m for m in metas if m['series'] == 'music'], key=by_date),
            'B': sorted([m for m in metas if m['series'] == 'other'], key=by_date)}


def anchor_id(text):
    """The id pandoc's gfm reader gives a heading with this text."""
    t = urllib.parse.unquote(text).strip().lower()
    t = re.sub(r'[^\w\- ]', '', t)
    return t.replace(' ', '-')


def vimeo_block(vid):
    return (f'<div class="yt vimeo" data-vimeo="{vid}"><span>Vimeo</span>'
            f'<button type="button" aria-label="Play video"></button></div>')


def youtube_block(vid):
    return (f'<div class="yt" data-id="{vid}">'
            f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy">'
            f'<button type="button" aria-label="Play video"></button></div>')


def split_cover(md, cover):
    """The cover is shown above the text: take it out of the body, keeping its caption for the header."""
    m = re.match(r'\s*!\[[^\]]*\]\(' + re.escape(cover) + r'\)[ \t]*\n(?:\*(.+)\*[ \t]*\n)?', md)
    if not m:
        return md, ''
    return md[m.end():], m.group(1) or ''


def caption_html(cap):
    cap_html = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html'], input=cap,
                              capture_output=True, text=True, check=True).stdout.strip()
    return re.sub(r'^<p>|</p>$', '', cap_html)


def preprocess(md):
    # image + italic caption line -> figure
    def fig(m):
        alt, src, cap = m.group(1), m.group(2), m.group(3)
        out = f'<figure><img src="{src}" alt="{html.escape(alt)}" loading="lazy">'
        if cap:
            out += f'<figcaption>{caption_html(cap)}</figcaption>'
        return out + '</figure>'
    md = re.sub(r'^!\[([^\]]*)\]\(([^)]+)\)[ \t]*(?:\n\*(.+)\*[ \t]*)?$', fig, md, flags=re.M)
    # bare YouTube URL on its own line -> click-to-load embed
    md = re.sub(r'^https://www\.youtube\.com/watch\?v=([\w-]{11})\S*[ \t]*$',
                lambda m: youtube_block(m.group(1)), md, flags=re.M)
    md = re.sub(r'^https://vimeo\.com/(\d+)\S*[ \t]*$', lambda m: vimeo_block(m.group(1)), md, flags=re.M)
    return md


def fill(template, values):
    for k, v in values.items():
        template = template.replace('{{' + k + '}}', v)
    return template


def notice(meta, pairs):
    """The line under a translation's title. translated_from: en marks a Russian translation of an
    English original, and stays after review, linking to the original; translation: machine adds
    that nobody has reviewed it yet."""
    machine = meta.get('translation') == 'machine'
    if meta.get('translated_from') == 'en' and meta['slug'] in pairs:
        link = f'<a href="../{pairs[meta["slug"]]}/" lang="en" hreflang="en">читать оригинал</a>'
        text = (f'Машинный перевод с английского, автор его ещё не вычитал. Оригинал написан на английском: {link}.'
                if machine else f'Перевод с английского. Оригинал написан на английском: {link}.')
    elif machine:
        text = 'Machine-translated, not yet reviewed by the author.'
    else:
        return ''
    return f'<p class="notice">{text}</p>'


def build_post(meta, body, sides, pairs):
    slug = meta['slug']
    track_slug = pairs[slug] if slug.endswith('-en') and slug in pairs else slug
    side, idx = next(((s, i) for s in 'AB' for i, m in enumerate(sides[s]) if m['slug'] == track_slug),
                     ('A' if meta['series'] == 'music' else 'B', None))
    tracks = sides[side]

    body, cover_caption = split_cover(body, meta['cover'])
    body_html = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html', '--wrap=none'],
                               input=preprocess(body),
                               capture_output=True, text=True, check=True).stdout
    # in-page links were written for Obsidian (#Heading%20text); point them at pandoc's heading ids
    body_html = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{anchor_id(m.group(1))}"', body_html)

    def nav(j, rel):
        if idx is None or not 0 <= j < len(tracks):
            return '<span></span>'
        t = tracks[j]
        label = f'{side}{j + 1} · {html.escape(t["title"])}'
        text = f'← {label}' if rel == 'prev' else f'{label} →'
        return f'<a class="{rel}" href="../{t["slug"]}/">{text}</a>'

    # RU · EN: the current language lit, the other one a link to the translation
    alt_link = ''
    if slug in pairs:
        other = pairs[slug]
        here, there = ('en', 'ru') if slug.endswith('-en') else ('ru', 'en')
        label = {'en': 'Read in English', 'ru': 'Читать по-русски'}[there]
        parts = {here: f'<span class="on" lang="{here}" aria-current="page">{here.upper()}</span>',
                 there: (f'<a href="../{other}/" lang="{there}" hreflang="{there}" title="{label}" '
                         f'aria-label="{label}">{there.upper()}</a>')}
        alt_link = f'<span class="lang">{parts["ru"]}<span aria-hidden="true">·</span>{parts["en"]}</span>'
    is_en = slug.endswith('-en') or (re.search(r'[A-Za-z]{3,}', meta['title']) and not re.search('[А-Яа-я]', meta['title']))
    page = fill(TEMPLATES['post'], {
        'lang': 'en' if is_en else 'ru',
        'side': side,
        'body_class': 'draft' if meta['draft'] else '',
        'robots': '\n<meta name="robots" content="noindex">' if meta['draft'] else '',
        'title': html.escape(meta['title']),
        'cover': meta['cover'],
        'cover_caption': f'<figcaption>{caption_html(cover_caption)}</figcaption>' if cover_caption else '',
        'year': 'draft' if meta['draft'] else meta.get('date', '')[:4],
        'notice': notice(meta, pairs),
        'position': 'Draft · not on the record yet' if idx is None else f'Side {side} · Track {idx + 1} of {len(tracks)}',
        'alt_link': alt_link,
        'back': '../' if idx is None else f'../#{side}{idx + 1}',
        'prev': nav(idx - 1 if idx is not None else -1, 'prev'),
        'next': nav(idx + 1 if idx is not None else -1, 'next'),
        'body': body_html,
    })
    os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
    open(os.path.join(ROOT, slug, 'index.html'), 'w').write(page)


def build_index(posts, sides):
    def track(m):
        words = len(re.findall(r'\w+', re.sub(r'\(([^)]*)\)|https?://\S+', '', posts[m['slug']][1])))
        return {'slug': m['slug'], 'title': m['title'], 'year': m['date'][:4],
                'min': max(1, round(words / WORDS_PER_MIN)),
                'cover': m['cover'].replace('../images/', ''), 'page': m['slug'] + '/', 'teaser': m['teaser']}
    data = {'A': {'name': 'year in music', 'tracks': [track(m) for m in sides['A']]},
            'B': {'name': 'other writing', 'tracks': [track(m) for m in sides['B']]}}
    page = fill(TEMPLATES['index'], {'sides': json.dumps(data, ensure_ascii=False, indent=1)})
    open(os.path.join(ROOT, 'index.html'), 'w').write(page)


KNOB = open(os.path.join(SRC, 'knob.html')).read()   # the theme knob, shared by both pages
TEMPLATES = {name: open(os.path.join(SRC, name + '.html')).read().replace('{{knob}}', KNOB)
             for name in ('index', 'post')}

if __name__ == '__main__':
    posts = load_posts()
    pairs = translations(posts.keys())
    sides = tracklist(posts, pairs)
    # pages of posts that were renamed or removed linger until deleted by hand
    for d in glob.glob(os.path.join(ROOT, '*', 'index.html')):
        name = os.path.basename(os.path.dirname(d))
        if name not in posts and name not in RESERVED:
            print(f'note: {name}/ has no post in posts/ any more')
    for meta, body in posts.values():
        build_post(meta, body, sides, pairs)
    build_index(posts, sides)
    print(f'built index + {len(posts)} posts:',
          ', '.join(s + (' (draft)' if m['draft'] else '') for s, (m, _) in sorted(posts.items())))
