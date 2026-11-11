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

## Interactive map

- `map-app/` is a small React Leaflet app. After changing it, run `cd map-app && npm install && npm run build`, then `python3 build.py`. The bundle in `map-app/dist/` is committed, so Cloudflare needs no build step.
- Map tiles in `public/tiles/v17/` and landmark data come from the GTA VI Mapping Community (YANIS v17) via gtadb.org, licensed CC BY 4.0. Keep the credit on the map and on `/map/`.
- To refresh them: `git clone https://github.com/rolux/gtadb.org`, then
  - `python3 tools/prepare_tiles.py <checkout>/maps/tiles/6/yanis,17 public/tiles/v17` (removes the legend panel)
  - `python3 tools/import_gtadb.py <checkout>/map/data/6/landmarks.json` (writes `content/locations.json`)
- Our own locations go in `content/locations_manual.json`, using the same fields: `id, name, nameKind, category, x, y, area, description, realWorld, image, status, source`.
  - `category`: landmarks, stores, activities, missions, collectibles, vehicles, weapons
  - `status`: speculative (pre-launch community data), official (shown by Rockstar), verified (checked in the released game)
  - `x, y`: in-game metres, as used by gtadb.org
  - `image`: null, or `{"src", "alt", "credit"}`. Only use images you have the right to publish.
