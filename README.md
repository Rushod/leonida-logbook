# Leonida Logbook

Unofficial GTA VI companion site, live at https://leonidalogbook.com.

## How it works

- `content/data.json` holds the site's lists: checklists, guide sections, cheats, gear links.
- `build.py` holds the page text and builds everything into `public/`.
- `src/site.css` and `src/site.js` are the shared styles and script.
- Cloudflare serves the `public/` folder (see `wrangler.jsonc`).

## Making a change

1. Edit `content/data.json` or `build.py`.
2. Run `python3 build.py`.
3. Commit and push to `main`. Cloudflare deploys automatically.

Do not edit files in `public/` by hand; the build overwrites them (except `og.png`).
