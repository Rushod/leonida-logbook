#!/usr/bin/env python3
"""Copy the GTA VI community map tiles from a gtadb.org checkout into public/tiles/,
removing the legend panel on the right of the tile set (it contains thumbnails of
Rockstar trailer frames, which we do not republish).

Usage:  python3 tools/prepare_tiles.py <gtadb checkout>/maps/tiles/6/yanis,17 public/tiles/v17

Tiles are 256 px, named {z}/{z},{y},{x}.jpg. At zoom z the world is 1024 * 2**z px wide and
one game metre is 2**z / 32 px, with game x = 0 at 16384 / 32 * 2**z px.
"""
import shutil
import sys
from pathlib import Path

from PIL import Image

CUT_X = 3300            # game metres; everything east of this is the legend panel
OCEAN = (44, 104, 166)  # open-ocean colour of the map


def main(src, out):
    src, out = Path(src), Path(out)
    if out.exists():
        shutil.rmtree(out)
    kept = dropped = masked = 0
    for zdir in sorted(src.iterdir(), key=lambda p: int(p.name)):
        z = int(zdir.name)
        cut_px = (CUT_X + 16384) * 2 ** z / 32
        (out / str(z)).mkdir(parents=True)
        for f in zdir.glob("*.jpg"):
            _, y, x = f.stem.split(",")
            left = int(x) * 256
            if left >= cut_px:
                dropped += 1
                continue
            dest = out / str(z) / f.name
            if left + 256 > cut_px:
                im = Image.open(f).convert("RGB")
                im.paste(OCEAN, (int(cut_px - left), 0, 256, 256))
                im.save(dest, quality=85, optimize=True)
                masked += 1
            else:
                shutil.copyfile(f, dest)
            kept += 1
    print(f"kept {kept} tiles ({masked} masked at the cut), dropped {dropped}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
