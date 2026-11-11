"""Original article graphics, drawn as inline SVG in the site's dusk palette.
Every function returns a <figure>. Text sizes stay at 24+ in an 800-wide box so they read on phones."""
import math

INK, SUN, PINK, BG, MUTED, GOOD = "#f7effd", "#ffc35a", "#ff4fa3", "#120824", "#d9c8ea", "#5fe6a8"
D = "Anton,'Arial Narrow',Impact,sans-serif"
L = "'Barlow Condensed','Arial Narrow',Arial,sans-serif"


def t(x, y, s, size=30, fill=INK, anchor="middle", font=D, extra=""):
    w = ' font-weight="700" letter-spacing="1.5"' if font == L else ' letter-spacing="1"'
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}{extra}>{s}</text>'


def panel(x, y, w, h, dashed=False):
    d = ' stroke-dasharray="10 8"' if dashed else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{BG}" fill-opacity=".6" stroke="#ffffff" stroke-opacity=".28" stroke-width="2"{d}/>'


def star(cx, cy, r, solid=True):
    pts = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    fill = SUN if solid else "none"
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{SUN}" stroke-width="4" stroke-linejoin="round"/>'


def fig(body, label, caption=""):
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return (
        f'<figure class="art"><svg viewBox="0 0 800 400" role="img" aria-label="{label}"><defs>'
        '<linearGradient id="aSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#160a33"/><stop offset=".55" stop-color="#3a1268"/><stop offset="1" stop-color="#8f2283"/></linearGradient>'
        '<linearGradient id="aBar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff4fa3"/><stop offset="1" stop-color="#ff8f3f"/></linearGradient>'
        '<linearGradient id="aNum" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff3b0"/><stop offset=".55" stop-color="#ffb14a"/><stop offset="1" stop-color="#ff5fa2"/></linearGradient>'
        f'</defs><rect width="800" height="400" rx="18" fill="url(#aSky)"/>{body}</svg>{cap}</figure>'
    )


def bars(title, rows, unit_px, label, caption):
    """rows: (name, value or None, value_text)"""
    out = t(400, 62, title, 34)
    for i, (name, val, txt) in enumerate(rows):
        y = 110 + i * 88
        out += t(40, y + 40, name, 32, anchor="start")
        if val is None:
            out += f'<rect x="200" y="{y}" width="480" height="56" rx="10" fill="none" stroke="{SUN}" stroke-width="3" stroke-dasharray="12 8"/>'
            out += t(440, y + 39, txt, 28, SUN, font=L)
        else:
            w = val * unit_px
            out += f'<rect x="200" y="{y}" width="{w:.0f}" height="56" rx="10" fill="url(#aBar)"/>'
            out += t(200 + w + 14, y + 40, txt, 32, SUN, anchor="start")
    return fig(out, label, caption)


def pc_gap():
    return bars("MONTHS FROM CONSOLE LAUNCH TO PC", [("GTA V", 19, "19"), ("RDR 2", 12, "12"), ("GTA VI", None, "NOT ANNOUNCED")], 480 / 19,
                "Bar chart: GTA V took 19 months to reach PC, Red Dead Redemption 2 took 12, GTA VI is not announced",
                "GTA V: September 2013 on console, April 2015 on PC. Red Dead Redemption 2: October 2018 on console, November 2019 on PC.")


def length_chart():
    return bars("MAIN STORY LENGTH IN HOURS", [("GTA V", 32, "ABOUT 32"), ("RDR 2", 50, "ABOUT 50"), ("GTA VI", 80, "ABOUT 80")], 4.6,
                "Bar chart: GTA V about 32 hours, Red Dead Redemption 2 about 50 hours, GTA VI about 80 hours",
                "GTA VI figure: one Rockstar developer's playthrough. GTA V and Red Dead Redemption 2: typical player-reported main-story times.")


def online_status():
    b = t(400, 62, "WHAT YOU GET AT LAUNCH", 34)
    b += panel(40, 100, 340, 250) + t(210, 150, "NOVEMBER 19", 28, SUN, font=L) + t(210, 222, "STORY MODE", 42)
    b += f'<circle cx="118" cy="290" r="18" fill="{GOOD}"/><path d="M109 290l7 7 12-14" fill="none" stroke="{BG}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' + t(146, 300, "CONFIRMED", 28, GOOD, anchor="start", font=L)
    b += panel(420, 100, 340, 250, dashed=True) + t(590, 150, "ONLINE MODE", 28, SUN, font=L) + t(590, 222, "NO DATE YET", 42) + t(590, 300, "NOT ANNOUNCED", 28, MUTED, font=L)
    return fig(b, "At launch on November 19: story mode confirmed, online mode has no date yet")


def fps():
    b = t(400, 62, "WHAT PREVIEWS REPORTED", 34)
    b += f'<text x="215" y="235" font-family="{D}" font-size="170" fill="url(#aNum)" text-anchor="middle">30</text>' + t(215, 280, "FPS TARGET", 30, font=L)
    b += f'<text x="570" y="220" font-family="{D}" font-size="110" fill="url(#aNum)" text-anchor="middle">1440p</text>' + t(570, 280, "RESOLUTION", 30, font=L)
    b += panel(140, 312, 520, 62, dashed=True) + t(400, 353, "60 FPS MODE: NOT CONFIRMED", 28, SUN, font=L)
    return fig(b, "Previews reported a 30 frames per second target at 1440p; a 60 fps mode is not confirmed")


def reviews_cal():
    b = t(400, 62, "REVIEW TIMING", 34)
    b += panel(110, 100, 260, 270, dashed=True) + t(240, 146, "NOVEMBER", 28, SUN, font=L)
    b += f'<text x="240" y="268" font-family="{D}" font-size="120" fill="{INK}" text-anchor="middle">18</text>' + t(240, 322, "REVIEWS?", 25, font=L) + t(240, 354, "UNCONFIRMED", 26, MUTED, font=L)
    b += f'<rect x="430" y="100" width="260" height="270" rx="14" fill="{BG}" fill-opacity=".6" stroke="url(#aBar)" stroke-width="4"/>' + t(560, 146, "NOVEMBER", 28, SUN, font=L)
    b += f'<text x="560" y="268" font-family="{D}" font-size="120" fill="url(#aNum)" text-anchor="middle">19</text>' + t(560, 322, "GAME UNLOCKS", 25, font=L) + t(560, 354, "CONFIRMED", 26, GOOD, font=L)
    return fig(b, "Calendar: reviews are reported but unconfirmed for November 18; the game unlocks November 19")


def radio():
    st = [("FLASH FM", "POP"), ("COCOTEO FM", "MODERN LATIN"), ("BACK COUNTRY RADIO", "COUNTRY"),
          ("AFROBANK FM", "AFRICAN MUSIC"), ("THE CHAMBER 106.6", "METAL"), ("DIRTY SOUTH CLASSICS", "SOUTHERN RAP")]
    b = t(400, 62, "SIX STATIONS REVEALED SO FAR", 34)
    for i, (n, g) in enumerate(st):
        x, y = 40 + (i % 2) * 370, 96 + (i // 2) * 98
        b += panel(x, y, 350, 86) + t(x + 20, y + 38, n, 24, anchor="start") + t(x + 20, y + 70, g, 24, SUN, anchor="start", font=L)
    return fig(b, "The six GTA VI radio stations revealed so far and their genres")


def map_size():
    b = t(400, 62, "HOW BIG IS LEONIDA?", 34)
    base = 330
    def sq(x, side, grad):
        f = "url(#aBar)" if grad else "none"
        s = "" if grad else f' stroke="{INK}" stroke-width="3" stroke-dasharray="10 7"'
        return f'<rect x="{x}" y="{base - side}" width="{side}" height="{side}" rx="8" fill="{f}"{s}/>'
    b += sq(40, 100, False) + t(90, 370, "RDR 2", 24, font=L) + sq(170, 173, True) + t(256, 370, "GTA VI · 3×", 24, SUN, font=L)
    b += f'<line x1="372" y1="100" x2="372" y2="375" stroke="#fff" stroke-opacity=".25" stroke-width="2"/>'
    b += sq(430, 80, False) + t(470, 370, "LOS SANTOS", 24, font=L) + sq(620, 113, True) + t(676, 370, "VICE CITY · 2×", 24, SUN, font=L)
    b += t(190, 112, "WHOLE MAP", 24, MUTED, font=L) + t(580, 112, "MAIN CITY", 24, MUTED, font=L)
    return fig(b, "Size comparison: the GTA VI map is about three times Red Dead Redemption 2's; Vice City is about twice Los Santos",
               "Squares are drawn to scale by area, using the sizes reported from preview events.")


def cast():
    groups = [("THE LEADS", ["JASON DUVAL", "LUCIA CAMINOS"]), ("LEONIDA KEYS", ["CAL HAMPTON", "BRIAN HEDER"]),
              ("VICE CITY MUSIC", ["BOOBIE IKE", "DRE'QUAN PRIEST", "REAL DIMEZ"]), ("THE HEIST PLANNER", ["RAUL BAUTISTA"])]
    b = t(400, 58, "WHO'S WHO IN GTA VI", 34)
    for i, (h, names) in enumerate(groups):
        x, y = 40 + (i % 2) * 370, 84 + (i // 2) * 152
        b += panel(x, y, 350, 140) + t(x + 20, y + 34, h, 24, SUN, anchor="start", font=L)
        for j, n in enumerate(names):
            b += t(x + 20, y + 68 + j * 31, n, 27, anchor="start")
    return fig(b, "The main GTA VI characters grouped by where they fit in the story")


def platforms():
    cols = [("PLAYS GTA VI", GOOD, ["PS5", "PS5 PRO", "XBOX SERIES X", "XBOX SERIES S"]),
            ("NOT AT LAUNCH", PINK, ["PS4", "XBOX ONE", "PC", "SWITCH 2"])]
    b = t(400, 62, "WHERE YOU CAN PLAY", 34)
    for i, (h, c, names) in enumerate(cols):
        x = 40 + i * 370
        b += panel(x, 96, 350, 280, dashed=(i == 1)) + t(x + 24, 140, h, 28, c, anchor="start", font=L)
        for j, n in enumerate(names):
            y = 190 + j * 52
            mark = (f'<path d="M{x + 26} {y - 10}l8 8 14-17" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' if i == 0
                    else f'<path d="M{x + 28} {y - 20}l18 18m0-18l-18 18" stroke="{c}" stroke-width="5" stroke-linecap="round"/>')
            b += mark + t(x + 66, y, n, 32, anchor="start")
    return fig(b, "GTA VI plays on PS5, PS5 Pro, Xbox Series X and Series S. It is not on PS4, Xbox One, PC or Switch 2 at launch")


def wanted():
    b = t(400, 62, "THE WANTED LEVEL", 34)
    for i in range(6):
        b += star(215 + i * 74, 138, 30, True)
    b += t(400, 208, "SOLID: POLICE KNOW WHO YOU ARE", 28, font=L)
    for i in range(6):
        b += star(215 + i * 74, 282, 30, False)
    b += t(400, 352, "HOLLOW: THEY KNOW THE CRIME, NOT WHO", 28, font=L)
    return fig(b, "Six solid stars mean police have identified you; hollow stars mean they know a crime happened but not who did it")
