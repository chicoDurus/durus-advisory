"""Build the Durus blog: one page per post in site/blog/, and the card grid
between the BLOG markers in site/index.html. Run: python3 src/build.py"""
import datetime as dt
import html
import json
import os
import re

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src", "posts")
SITE = os.path.join(ROOT, "site")
BLOG = os.path.join(SITE, "blog")
BASE_URL = "https://www.durusadvisory.com"

BADGE = """<svg class="brand-badge" id="brandLogo" viewBox="0 0 950 500" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M 647.02 129.55 A 210 210 0 0 0 302.98 129.55" fill="none" stroke="#D96A2C" stroke-width="6" stroke-linecap="round" stroke-dasharray="0.1 16.699"/>
        <path d="M 611.36 135.58 A 178 178 0 0 0 338.64 135.58" fill="none" stroke="#D96A2C" stroke-width="5" stroke-linecap="round" stroke-dasharray="0.1 14.021"/>
        <path d="M 647.02 370.45 A 210 210 0 0 1 302.98 370.45" fill="none" stroke="#D96A2C" stroke-width="6" stroke-linecap="round" stroke-dasharray="0.1 16.699"/>
        <path d="M 611.36 364.42 A 178 178 0 0 1 338.64 364.42" fill="none" stroke="#D96A2C" stroke-width="5" stroke-linecap="round" stroke-dasharray="0.1 14.021"/>
        <text x="475" y="270" text-anchor="middle" font-family="Domine,Georgia,serif" font-weight="700" font-size="150" letter-spacing="30" fill="#D96A2C">DURUS</text>
        <text x="483" y="330" text-anchor="middle" font-family="'IBM Plex Mono',ui-monospace,Menlo,monospace" font-weight="500" font-size="42" letter-spacing="26" fill="#EDEAE4">ADVISORY</text>
      </svg>"""

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 400'%3E%3Ccircle cx='200' cy='200' r='192' fill='%230A0A0B'/%3E"
           "%3Ccircle cx='200' cy='200' r='178' fill='none' stroke='%23D96A2C' stroke-width='4.5' stroke-linecap='round' stroke-dasharray='0.1 12.9047'/%3E"
           "%3Ccircle cx='200' cy='200' r='152' fill='none' stroke='%23D96A2C' stroke-width='4' stroke-linecap='round' stroke-dasharray='0.1 10.8775'/%3E"
           "%3Ctext x='200' y='292' text-anchor='middle' font-family='Domine,Georgia,serif' font-weight='700' font-size='250' fill='%23D96A2C' letter-spacing='-6'%3ED%3C/text%3E%3C/svg%3E")

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Domine:wght@500;600;700"
         "&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap")


def esc(s):
    return html.escape(s, quote=True)


def load_posts():
    posts = []
    for name in sorted(os.listdir(SRC)):
        if not name.endswith(".md"):
            continue
        raw = open(os.path.join(SRC, name), encoding="utf-8").read()
        m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
        meta = {}
        for line in m.group(1).splitlines():
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            meta[k.strip()] = v
        body = m.group(2).strip()
        words = len(re.findall(r"\w+", body))
        meta["minutes"] = max(1, round(words / 220))
        meta["date_obj"] = dt.date.fromisoformat(meta["date"])
        meta["date_h"] = meta["date_obj"].strftime("%-d %b %Y")
        html_body = markdown.markdown(body, extensions=["tables", "smarty"])
        html_body = html_body.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")
        meta["html"] = html_body
        posts.append(meta)
    posts.sort(key=lambda p: p["date_obj"], reverse=True)
    return posts


def nav(prefix):
    return f"""<header class="nav">
  <div class="wrap nav-in">
    <a href="{prefix}index.html" class="brand" aria-label="Durus Advisory home">
      {BADGE}
      <span class="visually-hidden">Durus Advisory</span>
    </a>
    <nav class="nav-links" aria-label="Primary">
      <a class="lnk" href="{prefix}index.html#approach">What we offer</a>
      <a class="lnk" href="{prefix}index.html#method">How we work</a>
      <a class="lnk" href="{prefix}index.html#about">About</a>
      <a class="lnk" href="{prefix}index.html#blog" aria-current="page">Blog</a>
      <a class="btn" href="https://calendly.com/durusadvisory" target="_blank" rel="noopener">Book a call <span class="arw" aria-hidden="true">↗</span></a>
    </nav>
  </div>
</header>"""


def footer(prefix):
    return f"""<footer>
  <div class="wrap foot-in">
    <span>© <span id="yr">{dt.date.today().year}</span> Durus Advisory</span>
    <div class="foot-links">
      <a href="{prefix}index.html#approach">What we offer</a>
      <a href="{prefix}index.html#method">How we work</a>
      <a href="{prefix}index.html#about">About</a>
      <a href="{prefix}index.html#blog">Blog</a>
      <a href="mailto:durus@durusadvisory.com">Email</a>
      <a href="https://linkedin.com/company/durus-advisory" target="_blank" rel="noopener">LinkedIn</a>
      <a href="https://calendly.com/durusadvisory" target="_blank" rel="noopener">Book a call</a>
    </div>
  </div>
</footer>"""


def more_card(p):
    return f"""<a class="more-card" href="{p['slug']}.html">
        <img src="../assets/covers/{p['cover']}.svg" alt="" loading="lazy">
        <div><span class="k">{p['date_h']}</span><h3>{esc(p['title'])}</h3></div>
      </a>"""


def post_page(p, newer, older):
    url = f"{BASE_URL}/blog/{p['slug']}.html"
    ld = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p["title"], "description": p["excerpt"],
        "datePublished": p["date"], "dateModified": p["date"],
        "author": {"@type": "Organization", "name": "Durus Advisory", "url": BASE_URL},
        "publisher": {"@type": "Organization", "name": "Durus Advisory", "url": BASE_URL},
        "mainEntityOfPage": url,
    }
    related = [x for x in (older, newer) if x]
    more = ""
    if related:
        more = f"""<section class="more">
    <div class="wrap">
      <h2>Keep reading</h2>
      <div class="more-grid">
      {''.join(more_card(x) for x in related)}
      </div>
    </div>
  </section>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(p['title'])} | Durus Advisory</title>
<meta name="description" content="{esc(p['excerpt'])}" />
<link rel="canonical" href="{url}" />
<meta property="og:title" content="{esc(p['title'])}" />
<meta property="og:description" content="{esc(p['excerpt'])}" />
<meta property="og:type" content="article" />
<meta property="og:url" content="{url}" />
<meta property="article:published_time" content="{p['date']}" />
<meta property="og:image" content="{BASE_URL}/og-image.png" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-96.png" type="image/png" sizes="96x96">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0A0A0B">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="../assets/post.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>

{nav('../')}

<main>
  <article>
    <header class="post-head wrap">
      <a class="back" href="../index.html#blog"><span aria-hidden="true">←</span> All posts</a>
      <h1>{esc(p['title'])}</h1>
      <div class="post-meta">
        <time datetime="{p['date']}"><b>{p['date_h']}</b></time>
        <span>{p['minutes']} min read</span>
      </div>
      <p class="post-lede">{esc(p['excerpt'])}</p>
    </header>
    <figure class="post-cover wrap">
      <img src="../assets/covers/{p['cover']}.svg" alt="" width="1600" height="1000">
    </figure>
    <div class="post-body">
{p['html']}
    </div>
  </article>

  {more}

  <section class="cta-band">
    <div class="wrap cta-in">
      <span class="eyebrow">Get in touch</span>
      <h2>Got a product that's drifting, or a roadmap stalled between strategy and delivery?</h2>
      <p>Send us a note. We'll tell you straight whether we can help.</p>
      <div class="row">
        <a class="btn" href="https://calendly.com/durusadvisory" target="_blank" rel="noopener">Book a call <span class="arw" aria-hidden="true">↗</span></a>
        <a class="btn ghost email" href="mailto:durus@durusadvisory.com">durus@durusadvisory.com</a>
      </div>
    </div>
  </section>
</main>

{footer('../')}

<script src="../assets/logo.js"></script>
<script>DurusLogo.header(document.getElementById('brandLogo'), {{ autoplay: true }});</script>
</body>
</html>
"""


def card(p, featured):
    cls = "post-card featured" if featured else "post-card"
    return f"""        <a class="{cls}" href="blog/{p['slug']}.html">
          <div class="pc-media">
            <img src="assets/covers/{p['cover']}.svg" alt="" loading="lazy">
            <div class="pc-title">
              <span class="pc-meta">{p['date_h']} · {p['minutes']} min</span>
              <h3>{esc(p['title'])}</h3>
            </div>
            <div class="pc-desc" aria-hidden="true">
              <p>{esc(p['excerpt'])}</p>
              <span class="pc-read">Read the post →</span>
            </div>
          </div>
          <p class="pc-touch">{esc(p['excerpt'])}</p>
        </a>"""


def main():
    posts = load_posts()
    os.makedirs(BLOG, exist_ok=True)
    for i, p in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i + 1 < len(posts) else None
        with open(os.path.join(BLOG, p["slug"] + ".html"), "w", encoding="utf-8") as fh:
            fh.write(post_page(p, newer, older))

    idx_path = os.path.join(SITE, "index.html")
    idx = open(idx_path, encoding="utf-8").read()
    cards = "\n".join(card(p, i == 0) for i, p in enumerate(posts))
    idx = re.sub(r"<!-- BLOG:START -->.*?<!-- BLOG:END -->",
                 lambda m: f"<!-- BLOG:START -->\n{cards}\n<!-- BLOG:END -->", idx, flags=re.S)
    open(idx_path, "w", encoding="utf-8").write(idx)

    # sitemap for search engines
    urls = [f"{BASE_URL}/"] + [f"{BASE_URL}/blog/{p['slug']}.html" for p in posts]
    lastmods = [posts[0]["date"]] + [p["date"] for p in posts]
    sm = "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod></url>" for u, d in zip(urls, lastmods))
    open(os.path.join(SITE, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')

    for p in posts:
        print(p["date"], f"{p['minutes']:>2} min", p["slug"])


if __name__ == "__main__":
    main()
