"""GTA V cheat codes shown on /cheats/ as the codes most likely to return in GTA VI.
Sequences are GTA V's own (PlayStation layout); Xbox sequences are derived by button mapping.
None of these is confirmed for GTA VI."""
from html import escape as e

XBOX = {"O": "B", "X": "A", "S": "X", "T": "Y", "L1": "LB", "R1": "RB", "L2": "LT", "R2": "RT"}
PS_GLYPH = {"O": ("○", "b-o"), "X": ("✕", "b-x"), "S": ("□", "b-s"), "T": ("△", "b-t")}
XB_CLASS = {"A": "b-xa", "B": "b-xb", "X": "b-xx", "Y": "b-xy"}
ARROW = {"U": "↑", "D": "↓", "L": "←", "R": "→"}

# (name, short label, effect, PS sequence, PC code, phone number)
GROUPS = [
    ("Health and abilities", [
        ("Invincibility", "God mode", "Makes you immune to damage for five minutes.", "R X R L R R1 R L X T", "PAINKILLER", "1-999-724-654-5537"),
        ("Max health and armor", "Full health", "Refills health and gives full body armor.", "O L1 T R2 X S O R S L1 L1 L1", "TURTLE", "1-999-887-853"),
        ("Recharge special ability", "Refill ability", "Fills the special ability meter.", "X X S R1 L1 X R L X", "POWERUP", "1-999-769-3787"),
    ]),
    ("Weapons and ammo", [
        ("Give weapons", "All guns", "Gives a full set of weapons with ammo.", "T R2 L L1 X R T D S L1 L1 L1", "TOOLUP", "1-999-866-587"),
        ("Explosive ammo", "Explosive bullets", "Bullets explode on impact.", "R S X L R1 R2 L R R L1 L1 L1", "HIGHEX", "1-999-4444-439"),
        ("Flaming bullets", "Fire ammo", "Bullets set targets on fire.", "L1 R1 S R1 L R2 R1 L S R L1 L1", "INCENDIARY", "1-999-462-363-4279"),
        ("Explosive melee attacks", "Explosive punches", "Punches and kicks cause a small explosion.", "R L X T R1 O O O L2", "HOTHANDS", "1-999-4684-2637"),
        ("Slow motion aim", "Dead Eye", "Slows time while aiming. Enter up to four times for slower.", "S L2 R1 T L S L2 R X", "DEADEYE", "1-999-332-3393"),
    ]),
    ("Movement", [
        ("Super jump", "High jump", "Jump several stories high.", "L L T T R R L R S R1 R2", "HOPTOIT", "1-999-467-8648"),
        ("Fast run", "Sprint faster", "Sprint much faster on foot.", "T L R R L2 L1 S", "CATCHME", "1-999-228-2463"),
        ("Fast swim", "Swim faster", "Swim much faster.", "L L L1 R R R2 L L2 R", "GOTGILLS", "1-999-468-44557"),
        ("Skyfall", "Drop from the sky", "Drops you from high in the air.", "L1 L2 R1 R2 L R L R L1 L2 R1 R2 L R L R", "SKYFALL", "1-999-759-3255"),
        ("Give parachute", "Parachute", "Puts a parachute on your back.", "L R L1 L2 R1 R2 R2 L L R L1", "SKYDIVE", "1-999-759-3483"),
        ("Moon gravity", "Low gravity", "Lowers gravity so people and cars float.", "L L L1 R1 L1 R L L1 L", "FLOATER", "1-999-356-2837"),
    ]),
    ("World and physics", [
        ("Change weather", "Weather", "Cycles to the next weather type.", "R2 X L1 L1 L2 L2 L2 S", "MAKEITRAIN", "1-999-625-348-7246"),
        ("Slippery cars", "Low grip", "Cars slide as if on ice.", "T R1 R1 L R1 L1 R2 L1", "SNOWDAY", "1-999-766-9329"),
        ("Slow motion", "Slow-mo", "Slows the whole game. Enter up to three times.", "T L R R S R2 R1", "SLOWMO", "1-999-756-966"),
        ("Drunk mode", "Drunk", "Your character stumbles and the camera sways.", "T R R L R S O L", "LIQUOR", "1-999-547-867"),
    ]),
    ("Wanted level", [
        ("Lower wanted level", "Lose a star", "Removes one wanted star each time.", "R1 R1 O R2 R L R L R L", "LAWYERUP", "1-999-5299-3787"),
        ("Raise wanted level", "Add a star", "Adds one wanted star each time.", "R1 R1 O R2 L R L R L R", "FUGITIVE", "1-999-3844-8483"),
    ]),
    ("Vehicle spawns", [
        ("Spawn Buzzard", "Attack helicopter", "Armed attack helicopter.", "O O L1 O O O L1 L2 R1 T O T", "BUZZOFF", "1-999-289-9633"),
        ("Spawn Comet", "Sports car", "Comet sports car.", "R1 O R2 R L1 L2 X X S R1", "COMET", "1-999-266-38"),
        ("Spawn Rapid GT", "Sports coupe", "Rapid GT sports car.", "R2 L1 O R L1 R1 R L O R2", "RAPIDGT", "1-999-727-4348"),
        ("Spawn stretch limo", "Limousine", "Stretch limousine.", "R2 R L2 L L R1 L1 O R", "VINEWOOD", "1-999-846-39663"),
        ("Spawn Trashmaster", "Garbage truck", "Garbage truck.", "O R1 O R1 L L R1 L1 O R", "TRASHED", "1-999-872-7433"),
        ("Spawn Sanchez", "Dirt bike", "Sanchez dirt bike.", "O X L1 O O L1 O R1 R2 L2 L1 L1", "OFFROAD", "1-999-633-7623"),
        ("Spawn PCJ-600", "Motorcycle", "PCJ-600 street bike.", "R1 R L R R2 L R S R L2 L1 L1", "ROCKET", "1-999-762-538"),
        ("Spawn BMX", "Bicycle", "BMX bicycle.", "L L R R L R S O T R1 R2", "BANDIT", "1-999-226-348"),
        ("Spawn Duster", "Crop duster", "Duster biplane.", "R L R1 R1 R1 L T T X O L1 L1", "FLYSPRAY", "1-999-359-77729"),
        ("Spawn stunt plane", "Stunt plane", "Mallard stunt plane.", "O R L1 L2 L R1 L1 L1 L L X T", "BARNSTORM", "1-999-2276-78676"),
        ("Spawn Caddy", "Golf cart", "Golf cart.", "O L1 L R1 L2 X R1 L1 O X", "HOLEIN1", "1-999-4653-461"),
    ]),
]

# (name, effect, phone, pc code or None, note)
PHONE_ONLY = [
    ("Spawn Dodo", "Dodo seaplane", "1-999-398-4628", "EXTINCT", "Unlocked through GTA V's story first"),
    ("Spawn Duke O'Death", "Armored muscle car", "1-999-3328-4227", "DEATHCAR", "Unlocked through GTA V's story first"),
    ("Spawn Kraken", "Submarine", "1-999-282-2537", "BUBBLES", "Unlocked through GTA V's story first"),
]


def chips(seq, xbox=False):
    out = []
    for t in seq.split():
        if t in ARROW:
            out.append(f'<i class="btn-k b-dir" title="{ {"U":"Up","D":"Down","L":"Left","R":"Right"}[t] }">{ARROW[t]}</i>')
        elif xbox:
            k = XBOX[t]
            out.append(f'<i class="btn-k {XB_CLASS.get(k, "b-sh")}">{k}</i>')
        elif t in PS_GLYPH:
            g, c = PS_GLYPH[t]
            name = {"O": "Circle", "X": "Cross", "S": "Square", "T": "Triangle"}[t]
            out.append(f'<i class="btn-k {c}" title="{name}">{g}</i>')
        else:
            out.append(f'<i class="btn-k b-sh">{t}</i>')
    return '<span class="btn-seq">' + "".join(out) + "</span>"


def card(name, label, effect, seq, pc, phone):
    return f"""<div class="cheat">
  <div class="cheat-h"><h3>{e(name)}</h3><span class="tag tag-v">GTA V code</span><p>{e(effect)}</p></div>
  <div class="cheat-in">
    <div data-plat="ps"><span class="plat">PS5 / PS4</span>{chips(seq)}</div>
    <div data-plat="xbox"><span class="plat">Xbox</span>{chips(seq, True)}</div>
    <div data-plat="pc"><span class="plat">PC</span><code class="pc">{pc}</code><button class="copy" type="button" data-copy="{pc}">Copy</button><small>Press ~ then type it</small></div>
    <div class="phone"><span class="plat">Phone</span>{phone}</div>
  </div></div>"""


def render():
    toc = "".join(f'<a href="#g{i}">{e(g)} <b>{len(items)}</b></a>' for i, (g, items) in enumerate(GROUPS))
    toc += f'<a href="#phone-only">Phone and PC only <b>{len(PHONE_ONLY)}</b></a>'
    groups = "".join(
        f'<section class="stack" id="g{i}"><h2>{e(g)} cheats</h2>{"".join(card(*c) for c in items)}</section>'
        for i, (g, items) in enumerate(GROUPS))
    rows = "".join(f"<tr><td><b>{e(n)}</b><br><span class=\"note\">{e(d)}</span></td><td class=\"n\">{p}</td><td><code class=\"pc\">{pc}</code></td><td>{e(note)}</td></tr>"
                   for n, d, p, pc, note in PHONE_ONLY)
    total = sum(len(i) for _, i in GROUPS) + len(PHONE_ONLY)
    return f"""
  <div class="facts">
    <div><span>GTA VI cheats confirmed</span><b>0 so far</b></div>
    <div><span>GTA V codes below</span><b>{total}</b></div>
    <div><span>Launch</span><b>Nov 19, 2026</b></div>
  </div>
  <div class="panel stack">
    <h2>Read this first</h2>
    <p>Rockstar has not announced any cheats for GTA VI. Posts calling these "leaked GTA 6 cheats" are showing GTA V's codes. They are listed here because GTA V's codes are the best guess at what might return, and so you can try them on launch day.</p>
    <ul class="tight">
      <li>Every code below is a <b>GTA V code</b>, not tested in GTA VI.</li>
      <li>In GTA V, using a cheat turns off trophies and achievements until you reload your save.</li>
      <li>Rockstar has used phone numbers for cheats before, and GTA VI has an in-game phone, but no cheat numbers are confirmed.</li>
      <li>From November 19, each code is tested in GTA VI and marked as working or not.</li>
    </ul>
  </div>
  <div class="cheat-bar">
    <div class="seg" role="group" aria-label="Show buttons for">
      <button type="button" data-show="ps" aria-pressed="true">PS5</button><button type="button" data-show="xbox" aria-pressed="false">Xbox</button><button type="button" data-show="pc" aria-pressed="false">PC</button><button type="button" data-show="all" aria-pressed="false">All</button>
    </div>
    <nav class="cheat-toc" aria-label="Cheat groups">{toc}</nav>
  </div>
  <div class="cheats" data-show="ps">{groups}
  <section class="stack" id="phone-only"><h2>Phone and PC only cheats</h2>
  <p>GTA V never gave these a button combination. Dial the number on the in-game phone, or type the code on PC.</p>
  <div class="scroll"><table><tr><th>Cheat</th><th>Phone</th><th>PC</th><th>Catch</th></tr>{rows}</table></div></section></div>"""
