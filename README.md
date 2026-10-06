# Durus Advisory website

Static site, deployed on Vercel from this repo (Root Directory: `site`, clean URLs via `site/vercel.json`).

```
src/pages/*.html     homepage, services overview, how we work, about, blog index, contact, privacy, 404
src/services/*.md    the four service pages
src/posts/*.md       blog posts
src/css/*.css        styles, combined into site/assets/site.css
src/build.py         builds everything into site/
src/covers.py        generates the blog cover artwork
site/                what gets published (don't edit generated .html by hand)
```

## Change something
1. Edit the file in `src/`.
2. `pip install markdown` (once), then run `python3 src/build.py`.
3. Commit and push. `main` goes live; other branches get a Vercel preview link.

## Add a blog post
Copy a file in `src/posts/`, edit the front matter (`title`, `slug`, `date`, `cover`, `excerpt`) and the text, build, push.
Covers available: question, chaos, calendar, orgchart, launch, documents, brands, busy, roadmap, fracture, gap.
New cover art: add a function to `src/covers.py`, then `python3 src/covers.py site/assets/covers`.

## Share images for posts
Each post gets its own LinkedIn/social preview image. After adding or renaming a post:
`python3 src/og.py && python3 src/build.py` (needs `pip install playwright` and `playwright install chromium`).
