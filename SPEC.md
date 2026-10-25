# Posts website — spec

A single website that republishes Eugene Trifonov's posts, which are currently scattered across telegra.ph, Habr and expectfun.github.io. It should read well and have a visual identity of its own.

Status: **draft**. Sections are split into *Settled* (decided, build on it) and *Open* (still exploring, don't lock in).

---

## Settled

### Name (working title)
- **Longplay**: "long play" is what LP stands for, and the posts are long reads. It's a working title; the final name is still open. Other candidates: Trifonograph, Jukebox, Liner Notes, Grooves, Needle Drop.
- It appears in the page header, the browser tab titles ("<post> — Longplay") and the text around the record label ("LONGPLAY • SIDE A").

### Goal
- One site that hosts all posts, instead of them being spread across other platforms.
- The posts are **republished**: the site holds full copies, not links out.

### Hosting
- GitHub Pages.

### Priorities
1. **Readability.** Posts are long reads (up to about 130 KB of text for `dugri`). Typography, line length, contrast and image handling for long-form reading come first.
2. **Uniqueness.** The site shouldn't look like a generic blog template. It needs a recognisable visual idea. *Which* idea is open (see below).

### Source content
- Posts live in `posts/<slug>.md`, and their images in `images/<slug>/`. This folder is the source of truth.
- Front matter fields:

  | Field | Meaning |
  |---|---|
  | `title` | Post title |
  | `date` | Publication date (`YYYY-MM-DD`) |
  | `author` | Author name as originally published |
  | `cover` | Cover image path |
  | `original` | URL where the post was first published |
  | `series` | `music` or `other`: internal id only; display names are open (Open §2) |
  | `parts` | Optional: original URLs of a multi-part post (`dugri`) |
  | `draft` | Optional: `true` for unpublished posts (`cybermus`) |

- Markdown conventions the site must render:
  - **YouTube embeds:** a YouTube URL alone on a line. There are many; music posts depend on them.
  - **Captions:** an image followed by an `*italic*` line holding its caption.
  - **Quotes:** `>` blockquotes, often song lyrics with hard line breaks.
  - **Section links:** in-page anchors. `dugri` uses the Obsidian style `#Мой%20взгляд`, so web anchor slugs need to match or be converted.
  - **Section breaks:** `---` lines.
- Languages: mostly Russian, plus some English posts (`sudan-en`, `jagged-intelligence`).

### Content types
- The site hosts **more than one type of content**:
  - **The music series.** Yearly birthday posts about music, each a special project with a shared theme. This is the core of the site.
  - **Other posts.** Older posts worth keeping, and reference material.
- `cyberpunk2020` is **in**. The new cyberpunk music post (`cybermus`) links to it, so it must live on the same site as reference material. The link in `cybermus` currently points to `expectfun.github.io/jukebox/cyberpunk.html` and must be updated to the final URL.
- How the types are split and presented is open (see Open §2).

### Current posts (12)

| Date | Slug | Title | Originally on |
|---|---|---|---|
| 2019-12-24 | alyona | Alyona Alyona | telegra.ph |
| 2020-03-20 | software2020 | В софте всё восхитительно, но все недовольны | Habr |
| 2020-12-11 | cyberpunk2020 | Киберпанк 2020: как развивался жанр с появления до наших дней | Habr |
| 2020-12-13 | nf | NF | telegra.ph |
| 2021-12-31 | lmm | Лин-Мануэль Миранда | telegra.ph |
| 2022-12-18 | eminem | Эминем: 8 роль | telegra.ph |
| 2023-12-13 | dugri | Палестина/Израиль: музыка и боль | telegra.ph (4 pages merged) |
| 2024-12-14 | sudan | Судан: песни незамеченных событий | telegra.ph |
| 2025-01-25 | sudan-en | Sudan: Songs of Unnoticed Events | telegra.ph |
| 2025-12-17 | adhd | Хип-хоп и СДВГ | telegra.ph |
| 2026-01-07 | jagged-intelligence | Jagged intelligence | expectfun.github.io |
| — (draft) | cybermus | Как звучит киберпанк? | not yet published |

---

## Open

### 1. Visual concept (the main open question)

**Constraint for any option:** the uniqueness should live mainly in the *shell*: the index, navigation, post headers and transitions. The reading view itself should stay calm. *(Proposed principle, not yet agreed.)*

**Leading direction: the site as a music player** *(Eugene's idea, being explored)*
- The site is an album. **Posts are tracks**, and the index is a tracklist with a main album plus extra material.
- The main page shows the physical medium. Opening a post is like playing a specific song: on vinyl, the needle drops on the right track; on a CD player, you press a track button. That transition is the signature moment of the site.

Which physical format (open):

| Format | How the content split maps | Choosing a post | Notes |
|---|---|---|---|
| **Vinyl** | Side A / Side B. The B side is flipped to view. | Needle drop on a track's band | Random access is literal: tracks are visible bands at different radii, and you aim at one. Band width could reflect reading length. The flip is a strong animation for reaching Side B. Bonus tracks also exist on vinyl, e.g. a bonus 7" or a reissue's extra side. |
| **CD** | Main album plus bonus tracks on a single side. The hidden track is a native CD idea. | Track-number buttons, an LCD showing "TRACK 05" | Fits the "main + bonus" split best. Less tactile: the disc is uniform, so the interface is buttons and the display rather than the disc itself. |
| **Cassette** | Side A / Side B, with the tape turned over. | Fast-forward or rewind to a position | Sequential access works against jumping straight to a post. Strong "mixtape" character, weakest for navigation. |

Initial assessment: **vinyl** maps best to "pick a post", because aiming the needle at a band *is* choosing a track. CD fits the bonus-track split best. Cassette is the weakest for navigation.

Interaction sketch (any format):
- **Index:** the record or player sits next to a real HTML tracklist, like the back of a sleeve. Hovering a track in the list highlights its band on the record, and vice versa. The cover of the hovered post can show on the centre label or in the CD display.
- **Opening a post:** the tonearm swings, the needle drops, there's an optional short crackle, then a transition into the post. Sound only plays after a click, is subtle, and can be turned off.
- **Post page:** calm reading, with a link back to the record and "previous / next track" navigation (see "From index to post" below).
- **Index:** no "now playing" panel. Playing a track leads into its post anyway, and a panel appearing would push the tracklist around.
- **Track numbers and order (settled):**
  - Numbers are **permanent and chronological**: A1 is the first post of a side, and a new post always gets the next number (A9, A10 …). Nothing is ever renumbered, so `#A6` links and "Side A · Track 6" on post pages stay valid.
  - The tracklist shows the **newest first** (A8 … A1), with no "new" tag. The cued tonearm (below) points at the newest published track, and drafts are skipped.
  - The record keeps the physical order: A1 on the outer edge, new tracks cut towards the label.
  - When idle, the raised tonearm hovers over the newest track's band, as if cued up and waiting. It re-cues after a side flip.
  - Later: once a side grows to about 12–15 tracks, the bands get thin. The archive could then continue on "Vol. 2" (a second record) rather than squeezing more onto one side.
- **Index controls:** the side switch is a pair of tabs ("Side A · year in music", "Side B · other writing") heading the tracklist; switching flips the record. Sound on/off is a speaker key on the turntable base, next to STOP. Both are part of the existing layout, so nothing shifts.
- **Mobile:** the disc fills the width, with the tracklist below it as a normal list.
- `prefers-reduced-motion` turns the animations off.

Rendering (open):
- **2D (SVG + CSS):** a turntable seen from above is naturally 2D: concentric grooves, a label, and a tonearm rotating around a pivot.
  - Pros: text stays crisp, tracks are real links (accessible, indexable), light, fast on phones, easy dark/light theming. A conic-gradient sheen adds a sense of material. CSS 3D transforms can still handle the side flip or a tilt.
- **3D (three.js):** a real 3D turntable or CD player with lighting, reflections and a camera move.
  - Pros: the most impressive look.
  - Cons: heavy (three.js plus models), mobile performance and battery, the canvas isn't accessible or indexable (a parallel HTML tracklist is needed anyway), much more work to polish, and a slower first load for a reading site.
- **Hybrid:** 2D/SVG first, with CSS 3D only for specific moments like the flip or a zoom into the label.

Initial assessment: start with 2D SVG and CSS 3D for the flip. Move to three.js only if a prototype feels too flat.

From index to post (current prototype behaviour):
- **Tracklist title and record do the same thing:** browse and listen. (Earlier, a title went straight to the post; it felt too abrupt next to the record.) Cmd/Ctrl-click on a title still opens the post in a new tab.
  - The needle drops with a thump, the crackle starts and keeps going, and a **preview card** fades in over the lower part of the turntable. It shows the cover, "A6 · 2024", the title, the opening lines (the "Привет, Саша" greeting is skipped) and a **Read →** button. There's no automatic navigation and no timer. From there:
    - Stay and listen.
    - Drop the needle elsewhere to preview another track.
    - Press STOP to hide the card and park the arm.
    - Press Read to fade through dark (0.65 s) into the post.
  - On phones, the card is a sheet at the bottom of the screen.
- **Transition: fade through dark.** The page fades to black, and the next page fades up from black (only when arriving from inside the site, not from external links). This replaced the cover morph (View Transitions), which looked odd: a rotated circle turning into a wide image, with mismatched shapes. The post page's back, previous and next links use the same fade.
- **Never in the way:**
  - Cmd/Ctrl/middle-click opens a new tab with no fade.
  - Reduced motion means instant navigation.
- **Post page:**
  - The header is the title with the year quietly under it. Many posts lean on time ("в этом году", "в прошлом году"), so readers need the year before they start reading. There's no author byline (every post is Eugene's), and the album position isn't shown up top.
  - **Track bar** at the end of the post: "← A5 · previous title | SIDE A · TRACK 6 OF 8 | next title A7 →". The album position sits between the neighbouring tracks, like a record label. On phones, the position goes on top and the links stack under it.
  - **Column width:** about 70 characters per line on desktop: 790 px at 19 px Literata (the comfortable range is 45–75). It was 680 px, about 60 characters. Phones get about 44 characters. Title, cover, images, videos and track navigation all share this width.
  - Below the title, the static, uncropped cover at the same width as the text and the other images. The round, spinning cover was dropped because it cropped details the posts discuss.
  - Calm reading.
  - "Back to the record" at the top left, with a small turntable icon whose record spins on hover. Its label uses the side's colour.
  - A link to the other language where one exists.
  - **No "originally published" links:** the original sites may disappear, and the texts are Eugene's own.
- **Sound:** only on the record page. A normal page load stops all audio, so it can't continue into the post.

Visible rotation: the grooves are concentric, so spinning them shows no motion. Real records show rotation through the label and small surface imperfections, while the light reflection stays still. The record needs elements that aren't symmetric and that rotate (dust, faint radial marks, an off-centre printed label), with the sheen kept static.

Prototype: `prototypes/vinyl.html` (2D SVG, no libraries). It has:
- a needle drop, and the Side A/B flip
- linked hover between the tracklist and the bands
- band width taken from reading time
- the hovered cover on the label
- generated crackle sound
- a whole-record spin with dust and scuffs, plus a slow idle spin
- reduced-motion support

All 12 posts are built as pages (`prototypes/<slug>.html`) from the Markdown by `prototypes/build_post.py all`, with `post-template.html`. Clicking any track runs a fast needle drop (≈1.5 s), then a View Transition morphs the label's cover into the post's round header cover. Each post page has:
- the side's accent colour (orange A, teal B)
- previous/next track links that go straight to the neighbouring posts
- "Back to the record" (`vinyl.html#A6`), which returns with the needle on the track
- a link to the other language for `sudan` / `sudan-en`
- YouTube and Vimeo that load only on click

`dugri`'s section links are converted to the web anchor format at build time. Serve over HTTP to try it (`python3 -m http.server` from the repo root), because cross-document View Transitions don't work on `file://`.

**Candidate: Jukebox** (the earlier idea, not settled; it's another kind of music player)
- Each post is a record or track in a jukebox. The index is the machine you pick from.
- It fits because most posts are a yearly music series (birthday posts to Саша about an artist or a music scene), and every post is full of songs.
- Already in place:
  - `~/life/code/jukebox/` exists with conversion tools (`html2md.py`, `pdf2md.py`) and two converted posts, but no site yet.
  - The `cybermus` draft already links to `expectfun.github.io/jukebox/cyberpunk.html`, which implies a `/jukebox/` URL.
- To be described by Eugene: what exactly makes it a jukebox visually and in how it works.
- Concerns to check:
  - Non-music posts (`software2020`, `jagged-intelligence`, the AI series) don't fit a jukebox metaphor naturally.
  - A heavily skeuomorphic machine can hurt readability and mobile use.

**Other candidates to explore**
- **Mixtapes and liner notes.** Each post is a cassette or CD. The index is a shelf of spines with years on them. The post page reads like liner notes, and the songs from its YouTube embeds form a "tracklist" sidebar.
- **Radio dial.** The index is a frequency band, and you tune between "stations" (posts or years). Static and noise between stations could be a signature visual.
- **Annual letters.** Lean into the series format: one post per year, each a "letter to Саша". The index is a timeline of envelopes or cards. It's honest about the format, but the music angle is weaker.
- **Part of City.** Posts live in the existing cyberpunk City (`expectfun/city`), for example as books in the Library. This reuses an existing world, but ties the blog to City's aesthetic and complexity.
- **Typographic identity only.** No metaphor. Uniqueness comes from a strong type and colour system: per-post accent colours taken from each cover, and expressive headings. This is the lowest risk to readability.

How to decide: build a quick prototype of the index and of one post page for 2–3 candidates, then compare them on desktop and mobile.

### 2. Splitting the content types

The music series is the core: 8 posts, one per year, all on a shared theme. The rest is a mix: work articles from Habr, reference material like `cyberpunk2020`, and the English AI series, which is likely to grow. How should one site present both?

Facts that affect the choice:
- The groups are uneven: 9 music posts (8 years plus the English Sudan translation) against 3 others today. The "others" may grow faster, through the AI series.
- The groups differ partly by language (the AI series is in English).
- Some "other" posts are reached mainly through links from music posts (`cybermus` → `cyberpunk2020`), not from the index. A direct URL has to work whatever the index looks like.

Options:
- **A. Side A / Side B** *(Eugene's idea)*. The two types are the two sides of a vinyl record or cassette, and the design plays on it: flipping the record, turning the tape over. The split is explicit and part of the concept.
  Risk: "sides" suggest two roughly equal halves, while the real content is unequal, and Side B may end up the bigger one.
- **B. Music first, the rest behind a link** *(Eugene's idea)*. The music posts are the site. Other posts sit behind a modest link ("Archive", "Other writing").
  Risk: a growing AI series ends up hidden.
  - **Variant: hidden track.** Like the unlisted track at the end of a CD after a stretch of silence, a deliberately half-hidden entry to the other posts at the very end of the index. This is option B made into part of the concept.
- **C. B-sides and rarities.** The music posts are the "album". The others are "B-sides & rarities" or "bonus tracks": secondary, but named and reachable in the same metaphor. It sits between A and B.
- **D. Liner notes.** Reference posts like `cyberpunk2020` aren't listed as equals at all. They show up as "liner notes" or further reading inside the music posts that cite them, plus a small index of their own. This fits material whose role is to be referenced.
- **E. Split by series, not by type.** Each post belongs to a named series: the birthday series (could be numbered like volumes: Vol. 1 = 2019 … Vol. 8 = 2026), the "Bear with me" AI series, and an archive. The index groups by series. This scales when a new series appears, and the visual metaphor can be applied to it later (series = albums, posts = tracks).
- **F. One timeline, different weight.** A single chronological list where music posts get large covers and the rest are compact one-line entries. The split shows through visual weight, not separate sections.

These can be combined. For example, E as the data model with A or C as the presentation, or D for reference posts on top of any of them.

**Decided:** two series, stored as `series: music` / `series: other` in front matter. The ids are internal and stable; what the site *calls* them is a display choice made later.
- `music` (9): alyona, nf, lmm, eminem, dugri, sudan, sudan-en, adhd, cybermus
- `other` (3): software2020, cyberpunk2020, jagged-intelligence

The `other` series is treated as **bonus material**: everything that isn't the main content. Its posts don't share a topic. Most are about tech, but `cyberpunk2020` is about culture, so the name shouldn't claim a topic.

**Display names (open, decided together with the visual concept).** The right name depends on the medium the site imitates: "Side B" only works for vinyl or cassette, "Bonus tracks" and "Hidden track" fit a CD best, and "Off the record" works with any of them. Don't pick one before §1 is settled. Candidates for `other` that describe its *role*, not its topic, and work with a music concept:
- **Bonus tracks**: plain and immediately understood.
- **B-sides**: pairs naturally with Side A / Side B.
- **Deep cuts**: lesser-known tracks for those who dig further.
- **Off the record**: a music pun that also means "unofficial, aside from the main thing".
- **Hidden track**: only if the section is deliberately half-hidden (option B).
- **Outtakes** / **Rarities**: suit old material kept for the archive.

`music` may need a display name too, e.g. "Birthday series", "Year in music", "Vol. 1–8", or simply "Side A" / "Album".

### 3. Site structure and URL
- Where it lives:
  - `expectfun.github.io/jukebox/` (a separate repo, matching the link in `cybermus`)
  - `expectfun.github.io/posts/` (inside the existing home repo)
  - a custom domain
- The name of the site, which depends on the concept.
- The URL scheme for posts, e.g. `/<slug>.html` or `/<slug>/`.
- The relation to the existing home page `expectfun.github.io`, which already lists projects and posts.

### 4. Tech stack
- Options:
  - Plain HTML with no build step, as in `home` and `city`. Markdown would then need converting by a script.
  - A static site generator: Jekyll is native to Pages; Eleventy or Astro would run through GitHub Actions.
- Markdown → HTML handling for the conventions above: YouTube embeds, captions, anchors.

### 5. Content scope
- Which posts go in:
  - **Birthday music series (8):** `alyona`, `nf`, `lmm`, `eminem`, `dugri`, `sudan`, `adhd`, plus `cybermus` once it's done. These are clearly in.
  - **Habr articles written for work:** `software2020`, and `cyberpunk2020`, which is settled as in (see Content types).
  - **English AI series:** `jagged-intelligence`, which is planned to grow.
  - **Not collected yet:** `~/life/code/city/posts/good-spec.html`.
- Translations: `sudan` / `sudan-en` are the same post in two languages. Should they be linked as translations, or listed separately?
- Language of the site UI: Russian, English, or switchable like the home page.

### 6. Embeds and media
- YouTube:
  - Options: full iframes, a lightweight click-to-load facade, or plain links.
  - Things to weigh: page speed with 10–15 videos per post, privacy, and YouTube not working well for some readers (the `sudan` post itself mentions this).
- Images: about 21 MB in total, kept in the repo. Possibly generate responsive sizes.

### 7. Extras (nice to have, not decided)
- RSS feed, tags or series, search, reading time, table of contents for long posts, comments, a dark/light theme.

### 8. Content fixes pending
- `lmm`: the year 2021 is inferred, not confirmed.
- `sudan`: the date is 12-14, but the telegra.ph URL says 12-13. Other posts use the URL date.
- `cybermus`: needs a date and the FSOL "Dead Cities" and Deltron 3030 cover images, which are marked "ЗАГРУЗИТЬ ОБЛОЖКУ".
- `dugri`: the anchor format may need changing for the web renderer (see Source content).
