# aixsam.dev

Link hub for the @aixsam.dev reels: every free AI tool and GitHub repo, with its comment keyword.

Add a tool: put a new entry at the top of the `TOOLS` list in `index.html`.

Setup guides: one page per tool at `tools/<slug>/index.html` (shared `tools/guide.css` + `tools/guide.js`). To add one, copy an existing guide folder, edit it, add it to `tools/index.html` and `sitemap.xml`, and set `guide:"/tools/<slug>/"` on the tool in `index.html`.

## Adding a setup guide
After adding or editing anything in `tools/<slug>/index.html`, run `python3 tools/extra.py && python3 tools/seo.py`. extra.py holds each guide's long-form text (What is it / What it can do / FAQ, facts from the tool's README): add an entry for a new guide there. seo.py adds the schema.org data (article, breadcrumbs, FAQ), the cover og:image and sitemap dates.
