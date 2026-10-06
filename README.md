# Durus Advisory website

Static site deployed on Vercel from this repo (Root Directory: `site`).

```
site/   what gets published: index.html, blog/, assets/, sitemap.xml
src/    working files: posts/*.md, build.py (pages + homepage cards + sitemap), covers.py (cover art)
```

## Add a blog post
1. Copy a file in `src/posts/` and edit the front matter (`title`, `slug`, `date`, `cover`, `excerpt`) and the text.
2. `pip install markdown` (once), then run `python3 src/build.py`.
3. Commit and push. `main` goes live; other branches get a Vercel preview link.

Cover names available: gantt, frameworks, question, chaos, calendar, documents, launch, busy, roadmap, fracture, gap.
Regenerate covers with `python3 src/covers.py site/assets/covers`.
