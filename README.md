# daveshevitz.com

Personal site for [daveshevitz.com](https://daveshevitz.com), hosted on GitHub Pages.

## Adding a new article

1. Create a file in `_posts/` named `your-slug.md` with this frontmatter:

   ```markdown
   ---
   title: "Your title"
   subtitle: "A short subtitle shown under the title"
   description: "One sentence for the homepage card."
   slug: your-slug
   date: 2026-06-07
   ---

   Your content here...
   ```

2. Write the article body in standard markdown. Bold, italic, links, and ordered lists work as expected.

3. Run the build:

   ```bash
   python3 build.py
   ```

4. Commit and push everything — the generated `.html` files and updated `index.html` included.

The GitHub Action (`.github/workflows/build.yml`) also runs the build automatically on every push, so you can skip step 3 if you prefer.

## Special formatting

For elements that need custom styling, use raw HTML inline:

```html
<!-- Standalone italic pull quote -->
<p class="standalone">Your text here.</p>

<!-- Example block (teal left-border callout) -->
<div class="example">
<p class="label">Instead of</p>
<p>The wordy version...</p>
</div>

<!-- Story / aside block (gray left-border) -->
<div class="story">
<p>Paragraph one.</p>
<p>Paragraph two.</p>
</div>

<!-- Section divider -->
<p class="divider">* * *</p>
```

## How it works

| File | Purpose |
|---|---|
| `_posts/*.md` | Article source files |
| `_template.html` | HTML template applied to every article |
| `build.py` | Converts markdown posts to HTML; updates the article list in `index.html` |
| `.github/workflows/build.yml` | Runs `build.py` on every push to main |

Articles appear on the homepage sorted newest-first by the `date` field in frontmatter.
