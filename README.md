# Longplay

Posts as Markdown in `posts/`, images in `images/<slug>/`. The site is plain static HTML
served by GitHub Pages from the repository root; the built pages are committed.

To publish a post: add `posts/<slug>.md` (front matter: `title`, `date`, `series: music|other`,
`cover`, `teaser`), run `python3 build.py` (needs pandoc), commit everything, push.
It appears at `/<slug>/`. With `draft: true` the page is built but left off the record.

Templates: `src/index.html` (the record) and `src/post.html`.
