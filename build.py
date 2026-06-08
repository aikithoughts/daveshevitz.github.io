#!/usr/bin/env python3
"""Build _posts/*.md -> article HTML files and update index.html."""

import os
import re
import sys

try:
    import markdown
except ImportError:
    print("Run: pip install markdown", file=sys.stderr)
    sys.exit(1)

POSTS_DIR = "_posts"
TEMPLATE = "_template.html"
INDEX = "index.html"


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    close = text.index("\n---\n", 4)
    yaml_block = text[4:close]
    body = text[close + 5:]
    meta = {}
    for line in yaml_block.splitlines():
        if ": " in line:
            k, _, v = line.partition(": ")
            v = v.strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1].replace('\\"', '"')
            meta[k.strip()] = v
    return meta, body.strip()


def build():
    with open(TEMPLATE) as f:
        template = f.read()

    articles = []

    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(POSTS_DIR, fname)) as f:
            raw = f.read()

        meta, body = parse_frontmatter(raw)
        slug = meta.get("slug", fname[:-3])
        title = meta.get("title", "Untitled")
        subtitle = meta.get("subtitle", "")
        description = meta.get("description", subtitle)
        date = meta.get("date", "1970-01-01")

        content = markdown.markdown(body, extensions=["extra"])

        html = (template
                .replace("{{title}}", title)
                .replace("{{subtitle}}", subtitle)
                .replace("{{description}}", description)
                .replace("{{content}}", content))

        out = f"{slug}.html"
        with open(out, "w") as f:
            f.write(html)
        print(f"  {out}")

        articles.append({
            "slug": slug,
            "title": title,
            "description": description,
            "date": date,
        })

    articles.sort(key=lambda a: a["date"], reverse=True)
    update_index(articles)


def update_index(articles):
    with open(INDEX) as f:
        src = f.read()

    items = "\n".join(
        f'                <li>\n'
        f'                    <a href="/{a["slug"]}.html">\n'
        f'                        <span class="writing-title">{a["title"]} →</span>\n'
        f'                        <span class="writing-desc">{a["description"]}</span>\n'
        f'                    </a>\n'
        f'                </li>'
        for a in articles
    )

    updated = re.sub(
        r"<!-- ARTICLES_START -->.*?<!-- ARTICLES_END -->",
        f"<!-- ARTICLES_START -->\n{items}\n                <!-- ARTICLES_END -->",
        src,
        flags=re.DOTALL,
    )

    with open(INDEX, "w") as f:
        f.write(updated)
    print(f"  {INDEX}")


if __name__ == "__main__":
    print("Building...")
    build()
    print("Done.")
