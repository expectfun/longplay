"""Build the site: posts/<slug>.md -> <slug>/index.html, plus the record at index.html

Usage: python3 build.py

Side A is the music series by date, Side B everything else. Drafts (draft: true) get a page
at their URL but stay off the record. slug-en is the English version of slug: it shares the
track, but isn't a track of its own. The record is built twice: in Russian at index.html and in
English at en/index.html, each linking to the posts in its own language.
"""
import glob, html, json, os, re, subprocess, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
RESERVED = {'images', 'posts', 'src', 'en'}
WORDS_PER_MIN = 175
SITE = 'https://expectfun.github.io/longplay/'

# interface text; the printing on the turntable itself (SIDE A, 7 TRACKS, STOP) stays English in both
UI = {
    'ru': {
        'back': 'Назад к пластинке', 'tracks_nav': 'Другие треки',
        'position': 'Сторона {side} · трек {n} из {total}', 'draft_position': 'Черновик · пока не на пластинке',
        'draft': 'черновик', 'play': 'Включить видео', 'other_lang': 'Read in English',
        'side': 'Сторона', 'sides': {'A': 'год в музыке', 'B': 'другие тексты'}, 'record_side': 'Сторона пластинки',
        'read': 'Читать →', 'close': 'Закрыть', 'min': 'мин', 'sound': 'Звук', 'stop': 'Остановить и поднять иглу',
        'note': 'Выберите название или опустите иглу на пластинку, чтобы послушать превью трека. '
                'Ширина дорожки зависит от времени чтения поста.',
        'knob': {'auto': 'авто', 'light': 'светлая', 'dark': 'тёмная', 'cyber': 'кибер', 'autoLong': 'авто, как в системе',
                 'aria': 'Тема: {mode}. Нажмите, чтобы переключить.'},
    },
    'en': {
        'back': 'Back to the record', 'tracks_nav': 'Other tracks',
        'position': 'Side {side} · Track {n} of {total}', 'draft_position': 'Draft · not on the record yet',
        'draft': 'draft', 'play': 'Play video', 'other_lang': 'Читать по-русски',
        'side': 'Side', 'sides': {'A': 'year in music', 'B': 'other writing'}, 'record_side': 'Record side',
        'read': 'Read →', 'close': 'Close', 'min': 'min', 'sound': 'Sound', 'stop': 'Stop and lift the needle',
        'note': "Pick a title or place the needle on the record to preview a track. "
                "Band width follows each post's reading time.",
        'knob': {'auto': 'auto', 'light': 'light', 'dark': 'dark', 'cyber': 'cyber', 'autoLong': 'auto, follows the system',
                 'aria': 'Theme: {mode}. Click to change.'},
    },
}


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


def vimeo_block(vid, lang):
    return (f'<div class="yt vimeo" data-vimeo="{vid}"><span>Vimeo</span>'
            f'<button type="button" aria-label="{UI[lang]["play"]}"></button></div>')


def youtube_block(vid, lang):
    return (f'<div class="yt" data-id="{vid}">'
            f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy">'
            f'<button type="button" aria-label="{UI[lang]["play"]}"></button></div>')


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


def preprocess(md, lang):
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
                lambda m: youtube_block(m.group(1), lang), md, flags=re.M)
    md = re.sub(r'^https://vimeo\.com/(\d+)\S*[ \t]*$', lambda m: vimeo_block(m.group(1), lang), md, flags=re.M)
    return md


def page_lang(meta, pairs):
    """A paired post's language comes from its name alone: slug-en is English, slug Russian (a Russian
    title can be all Latin, like «Alyona Alyona»). Only an unpaired post falls back to its title."""
    slug, t = meta['slug'], meta['title']
    if slug.endswith('-en') or slug in pairs:
        return 'en' if slug.endswith('-en') else 'ru'
    return 'en' if re.search(r'[A-Za-z]{3,}', t) and not re.search('[А-Яа-я]', t) else 'ru'


def in_lang(slug, lang, pairs):
    """The version of a track's post in the given language, if it has one."""
    return pairs[slug] if lang == 'en' and slug in pairs else slug


def lang_switch(here, links):
    """The language toggle: RU and EN on either side of a lever pointing at the current language.
    The whole thing is one link to the same place in the other language (styles in src/flip.html)."""
    there = 'en' if here == 'ru' else 'ru'
    label = UI[here]['other_lang']
    return (f'<a class="flip" data-lang="{here}" href="{links[there]}" hreflang="{there}" '
            f'title="{label}" aria-label="{label}">'
            '<span class="flip-l" lang="ru">RU</span>'
            '<svg viewBox="0 0 24 26" aria-hidden="true">'
            '<rect x="2.5" y="14" width="19" height="10" rx="2.5" fill="#141210" stroke="currentColor" stroke-opacity=".6"/>'
            '<g class="lever"><path d="M 12,18 V 5.5" stroke="currentColor" stroke-opacity=".85" stroke-width="2.4" stroke-linecap="round"/>'
            '<circle cx="12" cy="4.6" r="1.1" fill="var(--accent)"/></g>'
            '<circle cx="12" cy="18" r="3.3" fill="#24201c" stroke="#fff" stroke-opacity=".18" stroke-width=".6"/>'
            '</svg><span class="flip-l" lang="en">EN</span></a>')


def alternates(urls):
    """hreflang links, so search engines can offer each reader their language."""
    return ''.join(f'\n<link rel="alternate" hreflang="{code}" href="{SITE}{path}">' for code, path in urls.items())


def knob_text(lang):
    return html.escape(json.dumps(UI[lang]['knob'], ensure_ascii=False))


def fill(template, values):
    for k, v in values.items():
        template = template.replace('{{' + k + '}}', v)
    return template


def notice(meta, pairs):
    """The line under a translation's title. translated_from: en marks a Russian translation of an
    English original, and stays after review, linking to the original; translation: machine adds
    that nobody has reviewed it yet, and sensitive: true makes that a fuller warning."""
    machine = meta.get('translation') == 'machine'
    if meta.get('translated_from') == 'en' and meta['slug'] in pairs:
        link = f'<a href="../{pairs[meta["slug"]]}/" lang="en" hreflang="en">читать оригинал</a>'
        text = (f'Машинный перевод с английского, автор его ещё не вычитал. Оригинал написан на английском: {link}.'
                if machine else f'Перевод с английского. Оригинал написан на английском: {link}.')
    elif machine and meta.get('sensitive') == 'true':
        text = ('Machine-translated, not yet reviewed by the author. The subject is painful and sensitive, '
                'and in translation some wording may have come out harsher or less precise than in the '
                'Russian original. Please read with that in mind.')
    elif machine:
        text = 'Machine-translated, not yet reviewed by the author.'
    else:
        return ''
    return f'<p class="notice">{text}</p>'


def build_post(meta, body, sides, pairs, posts):
    slug = meta['slug']
    lang = page_lang(meta, pairs)
    ui = UI[lang]
    record = '../en/' if lang == 'en' else '../'
    track_slug = pairs[slug] if slug.endswith('-en') and slug in pairs else slug
    side, idx = next(((s, i) for s in 'AB' for i, m in enumerate(sides[s]) if m['slug'] == track_slug),
                     ('A' if meta['series'] == 'music' else 'B', None))
    tracks = sides[side]

    body, cover_caption = split_cover(body, meta['cover'])
    body_html = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html', '--wrap=none'],
                               input=preprocess(body, lang),
                               capture_output=True, text=True, check=True).stdout
    # in-page links were written for Obsidian (#Heading%20text); point them at pandoc's heading ids
    body_html = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{anchor_id(m.group(1))}"', body_html)

    # previous and next stay in this page's language
    def nav(j, rel):
        if idx is None or not 0 <= j < len(tracks):
            return '<span></span>'
        t = posts[in_lang(tracks[j]['slug'], lang, pairs)][0]
        label = f'{side}{j + 1} · {html.escape(t["title"])}'
        text = f'← {label}' if rel == 'prev' else f'{label} →'
        return f'<a class="{rel}" href="../{t["slug"]}/">{text}</a>'

    alt_link, alt_urls = '', {lang: f'{slug}/'}
    if slug in pairs:
        other = pairs[slug]
        alt_link = lang_switch(lang, {'ru': f'../{other}/', 'en': f'../{other}/'})
        alt_urls['en' if lang == 'ru' else 'ru'] = f'{other}/'
    page = fill(TEMPLATES['post'], {
        'lang': lang,
        'alternates': alternates(alt_urls) if len(alt_urls) > 1 else '',
        't_back': ui['back'],
        't_tracks': ui['tracks_nav'],
        'knob_text': knob_text(lang),
        # theme: cyber in the front matter adds a fourth position to the knob (styles in src/post.html)
        'knob_modes': 'auto light dark cyber' if meta.get('theme') == 'cyber' else 'auto light dark',
        'cyber_fonts': CYBER_FONTS if meta.get('theme') == 'cyber' else '',
        'side': side,
        'body_class': 'draft' if meta['draft'] else '',
        'robots': '\n<meta name="robots" content="noindex">' if meta['draft'] else '',
        'title': html.escape(meta['title']),
        'cover': meta['cover'],
        'cover_caption': f'<figcaption>{caption_html(cover_caption)}</figcaption>' if cover_caption else '',
        'year': ui['draft'] if meta['draft'] else meta.get('date', '')[:4],
        'notice': notice(meta, pairs),
        'position': (ui['draft_position'] if idx is None
                     else ui['position'].format(side=side, n=idx + 1, total=len(tracks))),
        'alt_link': alt_link,
        'back': record if idx is None else f'{record}#{side}{idx + 1}',
        'prev': nav(idx - 1 if idx is not None else -1, 'prev'),
        'next': nav(idx + 1 if idx is not None else -1, 'next'),
        'body': body_html,
    })
    os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
    open(os.path.join(ROOT, slug, 'index.html'), 'w').write(page)


def build_index(posts, sides, pairs, lang):
    """The record in one language: Russian at the root, English at en/, one level down."""
    ui, root = UI[lang], '../' if lang == 'en' else ''
    def track(m):
        meta, body = posts[in_lang(m['slug'], lang, pairs)]
        words = len(re.findall(r'\w+', re.sub(r'\(([^)]*)\)|https?://\S+', '', body)))
        return {'slug': meta['slug'], 'title': meta['title'], 'year': m['date'][:4],
                'min': max(1, round(words / WORDS_PER_MIN)),
                'cover': meta['cover'].replace('../images/', ''), 'page': f'{root}{meta["slug"]}/',
                'teaser': meta.get('teaser', m['teaser'])}
    data = {s: {'name': ui['sides'][s], 'tracks': [track(m) for m in sides[s]]} for s in 'AB'}
    page = fill(TEMPLATES['index'], {
        'sides': json.dumps(data, ensure_ascii=False, indent=1),
        'lang': lang, 'root': root,
        'alternates': alternates({'ru': '', 'en': 'en/'}),
        'lang_switch': lang_switch(lang, {'ru': '../', 'en': 'en/'}),
        'knob_text': knob_text(lang), 'knob_modes': 'auto light dark',
        **{f't_{k}': ui[k] for k in ('side', 'record_side', 'read', 'close', 'min', 'sound', 'stop', 'note')},
        't_side_a': ui['sides']['A'], 't_side_b': ui['sides']['B'],
    })
    out = os.path.join(ROOT, 'en') if lang == 'en' else ROOT
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w').write(page)


# the cyber theme's type, all with Cyrillic; the browser fetches the font files only once the theme is on
CYBER_FONTS = ('\n<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,600;1,400'
               '&family=JetBrains+Mono:wght@400;600&family=Unbounded:wght@500;700&display=swap" rel="stylesheet">')

# the theme knob and the language toggle's styles and script, shared by both pages
PARTS = {name: open(os.path.join(SRC, name + '.html')).read() for name in ('knob', 'flip')}
TEMPLATES = {name: open(os.path.join(SRC, name + '.html')).read()
             .replace('{{knob}}', PARTS['knob']).replace('{{flip}}', PARTS['flip'])
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
        build_post(meta, body, sides, pairs, posts)
    build_index(posts, sides, pairs, 'ru')
    build_index(posts, sides, pairs, 'en')
    print(f'built the record (ru, en) + {len(posts)} posts:',
          ', '.join(s + (' (draft)' if m['draft'] else '') for s, (m, _) in sorted(posts.items())))
