#!/usr/bin/env python3
"""Convert gtadb.org's GTA VI landmark data (CC BY 4.0) into content/locations.json.

Usage:  python3 tools/import_gtadb.py <gtadb checkout>/map/data/6/landmarks.json

Only named landmarks with a position are imported. Every imported location is marked
"speculative": it was mapped by the community from trailers, screenshots and other
pre-release material, and has not been checked in the released game.
Locations we add ourselves live in content/locations_manual.json and are merged in.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = {"label": "GTA VI Mapping Community via gtadb.org", "url": "https://map.gtadb.org", "license": "CC BY 4.0"}

STORE_TAGS = {"#gas", "#supermarket", "supermarket", "#clothes", "#guns", "#hair", "#tattoos", "#modshop",
              "#pay'n'spray", "#fastfood", "#food", "#electronics", "#vendor", "retail", "restaurant"}
ACTIVITY_TAGS = {"#tennis", "#racetrack", "#nightclub", "#stripclub", "#bar", "#drinks", "#marina", "leisure", "events"}
SKIP_TAGS = {"//may-not-exist"}

KIND = [  # first match wins; used for the description
    ("#gas", "Gas station"), ("#supermarket", "Supermarket"), ("supermarket", "Supermarket"),
    ("#clothes", "Clothing store"), ("#guns", "Gun store"), ("#hair", "Hair salon"), ("#tattoos", "Tattoo parlor"),
    ("#modshop", "Mod shop"), ("#pay'n'spray", "Pay & Spray"), ("#fastfood", "Fast food"), ("#food", "Food"),
    ("#electronics", "Electronics store"), ("#vendor", "Vendor"), ("#nightclub", "Nightclub"), ("#stripclub", "Strip club"),
    ("#bar", "Bar"), ("#drinks", "Bar"), ("#tennis", "Tennis courts"), ("#racetrack", "Racetrack"), ("#marina", "Marina"),
    ("#safehouse", "Possible safehouse"), ("#airport", "Airport"), ("#police", "Police station"), ("#hospital", "Hospital"),
    ("#jail", "Jail"), ("#train", "Train station"), ("#metro", "Metro station"), ("#metromover", "Metromover station"),
    ("#fence", "Fence"), ("hotel", "Hotel"), ("residential", "Residential building"), ("restaurant", "Restaurant"),
    ("retail", "Shop"), ("office", "Office building"), ("government", "Government building"), ("industrial", "Industrial site"),
    ("transportation", "Transport"), ("utilities", "Utilities"), ("natural", "Natural feature"), ("leisure", "Leisure spot"),
    ("events", "Event venue"), ("public", "Public building"), ("landmark", "Landmark"), ("construction", "Construction site"),
    ("agriculture", "Farmland"),
]


def category(tags):
    t = set(tags)
    if t & STORE_TAGS:
        return "stores"
    if t & ACTIVITY_TAGS:
        return "activities"
    return "landmarks"


def describe(tags):
    kind = next((label for tag, label in KIND if tag in tags), "Location")
    bits = [kind + "."]
    if "enterable" in tags:
        bits.append("Reported to have an interior you can enter.")
    if "closed" in tags:
        bits.append("Its real-world counterpart has closed.")
    if "unconfirmed" in tags:
        bits.append("The community has not confirmed this one.")
    return " ".join(bits)


def short_address(addr):
    parts = [p.strip() for p in (addr or "").split(",")]
    parts = [p for p in parts if p and p != "USA"]
    if len(parts) >= 3:  # "Name, street, City, ST zip" -> "Name, City"
        name, city = parts[0], parts[-2]
        return name if name == city else f"{name}, {city}"
    return ", ".join(parts)


def main(path):
    raw = json.loads(Path(path).read_text())
    out = []
    for key, v in raw.items():
        label, pos, real, tags = v[0], v[1], v[3], v[6] or []
        parts = [p.strip() for p in label.split(",")]
        name = parts[0]
        if name.startswith("?") or len(pos) != 2 or SKIP_TAGS & set(tags):
            continue
        if name.startswith('"') and name.endswith('"'):
            name_kind, clean = "community", name.strip('"')
        elif name.endswith("?"):
            name_kind, clean = "uncertain", name.rstrip("?").strip()
        else:
            name_kind, clean = "game", name
        out.append({
            "id": f"gtadb-{key}",
            "name": clean,
            "nameKind": name_kind,
            "category": category(tags),
            "x": round(pos[0], 1),
            "y": round(pos[1], 1),
            "area": ", ".join(parts[1:]),
            "description": describe(tags),
            "realWorld": short_address(real),
            "image": None,
            "status": "speculative",
            "source": SOURCE,
        })
    manual = ROOT / "content/locations_manual.json"
    if manual.exists():
        out += json.loads(manual.read_text())
    out.sort(key=lambda l: (l["category"], l["name"]))
    dest = ROOT / "content/locations.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
    counts = {}
    for l in out:
        counts[l["category"]] = counts.get(l["category"], 0) + 1
    print(len(out), "locations", counts)


if __name__ == "__main__":
    main(sys.argv[1])
