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
    b = t(400, 62, "GTA VI PERFORMANCE AT LAUNCH", 34)
    b += f'<text x="215" y="235" font-family="{D}" font-size="170" fill="url(#aNum)" text-anchor="middle">30</text>' + t(215, 280, "FPS, ALL CONSOLES", 26, font=L)
    b += f'<text x="570" y="220" font-family="{D}" font-size="110" fill="url(#aNum)" text-anchor="middle">1440p</text>' + t(570, 280, "PS5 + PRO RENDER", 26, font=L)
    b += panel(140, 312, 520, 62, dashed=True) + t(400, 353, "NO 60 FPS MODE, EVEN ON PS5 PRO", 28, SUN, font=L)
    return fig(b, "GTA VI runs at 30 frames per second on every console, renders internally at 1440p on PS5 and PS5 Pro, and has no 60 fps mode")


def reviews_cal():
    b = t(400, 62, "REVIEW TIMING", 34)
    b += f'<rect x="110" y="100" width="260" height="270" rx="14" fill="{BG}" fill-opacity=".6" stroke="url(#aBar)" stroke-width="4"/>' + t(240, 146, "NOVEMBER", 28, SUN, font=L)
    b += f'<text x="240" y="268" font-family="{D}" font-size="120" fill="url(#aNum)" text-anchor="middle">18</text>' + t(240, 322, "REVIEWS LIVE", 25, font=L) + t(240, 354, "HAPPENED", 26, GOOD, font=L)
    b += f'<rect x="430" y="100" width="260" height="270" rx="14" fill="{BG}" fill-opacity=".6" stroke="url(#aBar)" stroke-width="4"/>' + t(560, 146, "NOVEMBER", 28, SUN, font=L)
    b += f'<text x="560" y="268" font-family="{D}" font-size="120" fill="url(#aNum)" text-anchor="middle">19</text>' + t(560, 322, "GAME UNLOCKS", 25, font=L) + t(560, 354, "CONFIRMED", 26, GOOD, font=L)
    return fig(b, "Calendar: reviews went live on November 18; the game unlocks at local midnight on November 19")


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
    cols = [("PLAYS GTA VI", GOOD, ["PS5 / PS5 PRO", "SERIES X", "SERIES S", "XBOX ONE*"]),
            ("NOT AT LAUNCH", PINK, ["PS4", "PC", "SWITCH 2"])]
    b = t(400, 62, "WHERE YOU CAN PLAY", 34)
    for i, (h, c, names) in enumerate(cols):
        x = 40 + i * 370
        b += panel(x, 96, 350, 268, dashed=(i == 1)) + t(x + 24, 140, h, 28, c, anchor="start", font=L)
        for j, n in enumerate(names):
            y = 190 + j * 52
            mark = (f'<path d="M{x + 26} {y - 10}l8 8 14-17" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' if i == 0
                    else f'<path d="M{x + 28} {y - 20}l18 18m0-18l-18 18" stroke="{c}" stroke-width="5" stroke-linecap="round"/>')
            b += mark + t(x + 66, y, n, 32, anchor="start")
    b += t(400, 392, "* STREAMING THROUGH XBOX CLOUD GAMING", 20, MUTED, font=L)
    return fig(b, "GTA VI plays on PS5, PS5 Pro, Xbox Series X and Series S, and streams to Xbox One through the cloud. It is not on PS4, PC or Switch 2 at launch")


def wanted():
    b = t(400, 62, "THE WANTED LEVEL", 34)
    for i in range(6):
        b += star(215 + i * 74, 138, 30, True)
    b += t(400, 208, "SOLID: POLICE KNOW WHO YOU ARE", 28, font=L)
    for i in range(6):
        b += star(215 + i * 74, 282, 30, False)
    b += t(400, 352, "HOLLOW: THEY KNOW THE CRIME, NOT WHO", 28, font=L)
    return fig(b, "Six solid stars mean police have identified you; hollow stars mean they know a crime happened but not who did it")


def cloud():
    b = t(400, 62, "GTA VI ON XBOX ONE", 34)
    b += panel(40, 110, 230, 240) + t(155, 165, "YOUR XBOX ONE", 24, SUN, font=L)
    b += f'<rect x="85" y="200" width="140" height="60" rx="10" fill="none" stroke="{INK}" stroke-width="4"/><circle cx="200" cy="230" r="7" fill="{INK}"/>' + t(155, 310, "STREAMS IT", 28, font=L)
    b += f'<path d="M290 230 H500" stroke="#ff6fa0" stroke-width="6" stroke-dasharray="14 10" stroke-linecap="round"/><path d="M495 215 L515 230 L495 245" fill="none" stroke="#ff8f3f" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    b += t(395, 205, "INTERNET", 24, MUTED, font=L)
    b += f'<path d="M560 255 a40 40 0 0 1 10 -78 a55 55 0 0 1 104 -12 a42 42 0 0 1 56 40 a36 36 0 0 1 -6 50 Z" fill="none" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
    b += t(640, 310, "MICROSOFT SERVERS", 22, font=L) + t(640, 345, "RUN THE GAME", 22, SUN, font=L)
    return fig(b, "Diagram: an Xbox One streams GTA VI over the internet from Microsoft's servers, which run the game")


def preload_bar():
    b = t(400, 62, "PRELOAD IS OPEN", 34)
    b += f'<rect x="80" y="120" width="640" height="56" rx="28" fill="#120824" stroke="#ffffff" stroke-opacity=".3" stroke-width="2"/><rect x="86" y="126" width="420" height="44" rx="22" fill="url(#aBar)"/>'
    b += f'<text x="400" y="290" font-family="{D}" font-size="110" fill="url(#aNum)" text-anchor="middle">212 GB</text>'
    b += t(400, 345, "THE MOST THE GAME NEEDS, BEFORE THE DAY-ONE PATCH", 22, MUTED, font=L)
    return fig(b, "Progress bar for the GTA VI preload, with the 212 GB maximum download size")


def cheats_check():
    b = t(400, 62, "LEAKED GTA 6 CHEATS?", 34)
    b += panel(40, 100, 340, 250) + t(210, 150, "VIRAL LISTS", 28, SUN, font=L)
    b += f'<text x="210" y="262" font-family="{D}" font-size="100" fill="{INK}" text-anchor="middle">GTA V</text>' + t(210, 318, "CODES FROM 2013", 26, MUTED, font=L)
    b += f'<rect x="420" y="100" width="340" height="250" rx="14" fill="#120824" fill-opacity=".6" stroke="url(#aBar)" stroke-width="4"/>' + t(590, 150, "CONFIRMED IN GTA VI", 22, SUN, font=L)
    b += f'<text x="590" y="275" font-family="{D}" font-size="130" fill="url(#aNum)" text-anchor="middle">0</text>' + t(590, 318, "SO FAR", 26, MUTED, font=L)
    return fig(b, "Comparison: viral leaked cheat lists are GTA V codes; zero cheats are confirmed for GTA VI")


def nz_first():
    b = t(400, 62, "WHO PLAYS GTA VI FIRST", 34)
    rows = [("NEW ZEALAND", "NOV 18, 11:00 UTC", 600), ("SYDNEY", "2 HOURS LATER", 520), ("LONDON", "13 HOURS LATER", 300), ("NEW YORK", "18 HOURS LATER", 170), ("LOS ANGELES", "21 HOURS LATER", 110)]
    for i, (n, w, px) in enumerate(rows):
        y = 100 + i * 56
        fill = "url(#aBar)" if i == 0 else "#ffffff"
        op = "1" if i == 0 else ".25"
        b += t(40, y + 32, n, 24, INK if i == 0 else MUTED, anchor="start", font=L)
        b += f'<rect x="330" y="{y + 8}" width="{px * 0.3:.0f}" height="34" rx="17" fill="{fill}" fill-opacity="{op}"/>'
        b += t(770, y + 32, w, 22, SUN if i == 0 else MUTED, anchor="end", font=L)
    return fig(b, "Chart: GTA VI unlocked first in New Zealand at 11:00 UTC on November 18, hours ahead of Australia, the UK and the US")


def metascore():
    b = t(400, 62, "WHAT CRITICS SAY", 34)
    b += f'<rect x="60" y="100" width="300" height="270" rx="14" fill="{BG}" fill-opacity=".6" stroke="url(#aBar)" stroke-width="4"/>'
    b += f'<text x="210" y="265" font-family="{D}" font-size="170" fill="url(#aNum)" text-anchor="middle">99</text>' + t(210, 310, "METASCORE, PS5", 26, font=L) + t(210, 345, "98 REVIEWS, EARLY", 24, MUTED, font=L)
    b += panel(400, 100, 340, 125) + t(570, 148, "PRAISED", 26, GOOD, font=L) + t(570, 196, "WORLD · DRIVING · STORY", 22, font=L)
    b += panel(400, 245, 340, 125) + t(570, 293, "CRITICISED", 26, SUN, font=L) + t(570, 341, "CONTROLS · 30 FPS · GUNS", 22, font=L)
    return fig(b, "GTA VI has a 99 Metascore on PS5 from an early sample of 98 reviews; critics praise the world, driving and story and criticise controls, the 30 fps cap and gunplay")


def xbox_fps():
    b = t(400, 62, "GTA VI ON XBOX, TESTED", 34)
    b += panel(40, 96, 345, 278) + t(212, 140, "SERIES X", 30, SUN, font=L)
    b += f'<text x="212" y="238" font-family="{D}" font-size="96" fill="url(#aNum)" text-anchor="middle">1440p</text>'
    b += t(212, 290, "MOSTLY HOLDS 30 FPS", 25, font=L) + t(212, 332, "CLOSE TO BASE PS5", 24, GOOD, font=L)
    b += f'<rect x="415" y="96" width="345" height="278" rx="14" fill="{BG}" fill-opacity=".6" stroke="url(#aBar)" stroke-width="4"/>' + t(587, 140, "SERIES S", 30, SUN, font=L)
    b += f'<text x="587" y="238" font-family="{D}" font-size="96" fill="url(#aNum)" text-anchor="middle">720p</text>'
    b += t(587, 290, "OFTEN 25 TO 30 FPS", 25, font=L) + t(587, 332, "AROUND 20 AT WORST", 24, PINK, font=L)
    return fig(b, "Digital Foundry's Xbox results: Series X renders at about 1440p and mostly holds 30 fps; Series S renders at 720p, often runs at 25 to 30 fps and drops to about 20 at worst")


def cheats_real():
    b = t(400, 62, "GTA VI CHEATS ARE REAL", 34)
    b += f'<rect x="40" y="96" width="300" height="278" rx="14" fill="{BG}" fill-opacity=".6" stroke="url(#aBar)" stroke-width="4"/>'
    b += f'<text x="190" y="252" font-family="{D}" font-size="150" fill="url(#aNum)" text-anchor="middle">61</text>' + t(190, 300, "CHEATS IN TOTAL", 25, font=L) + t(190, 336, "PER GUIDES", 22, MUTED, font=L)
    steps = [("1", "PRESS UP: PHONE OUT"), ("2", "HOLD L1 + R1 (LB + RB)"), ("3", "ENTER THE D-PAD CODE")]
    for i, (n, s) in enumerate(steps):
        y = 96 + i * 72
        b += panel(370, y, 390, 60) + t(400, y + 41, n, 30, SUN) + t(425, y + 40, s, 23, anchor="start", font=L)
    b += panel(370, 312, 390, 62, dashed=True) + t(565, 352, "UNLOCK: BEAT THE STORY", 23, SUN, font=L)
    return fig(b, "GTA VI has 61 cheats. Press Up to take out the phone, hold L1 and R1 (LB and RB on Xbox), then enter a D-pad code. Cheats unlock after the main story")


def trophies():
    b = t(400, 62, "THE GTA VI TROPHY LIST", 34)
    b += f'<rect x="40" y="96" width="300" height="278" rx="14" fill="{BG}" fill-opacity=".6" stroke="url(#aBar)" stroke-width="4"/>'
    b += f'<text x="190" y="252" font-family="{D}" font-size="150" fill="url(#aNum)" text-anchor="middle">55</text>' + t(190, 300, "TROPHIES IN TOTAL", 25, font=L) + t(190, 336, "1,000G ON XBOX", 22, MUTED, font=L)
    tiers = [("PLATINUM", "1", INK), ("GOLD", "2", SUN), ("SILVER", "6", MUTED), ("BRONZE", "46", "#ff8f3f")]
    for i, (name, n, col) in enumerate(tiers):
        y = 96 + i * 52
        b += panel(370, y, 390, 44) + t(395, y + 31, name, 23, col, anchor="start", font=L) + t(735, y + 32, n, 28, col, anchor="end")
    b += panel(370, 312, 390, 62, dashed=True) + t(565, 352, "PLATINUM NEEDS 100%", 23, SUN, font=L)
    return fig(b, "GTA VI has 55 trophies: 1 platinum, 2 gold, 6 silver and 46 bronze, worth 1,000 Gamerscore on Xbox. The platinum needs 100% completion")


def sales_estimate():
    b = t(400, 62, "COPIES SOLD BY LAUNCH, ESTIMATED", 34)
    rows = [("GTA V", 11.2, "11.2M", "FIRST 24 HOURS, 2013"), ("GTA VI", 19.1, "19.1M", "SENSOR TOWER ESTIMATE")]
    for i, (name, val, txt, note) in enumerate(rows):
        y = 112 + i * 120
        w = val * 22
        b += t(40, y + 40, name, 32, anchor="start")
        b += f'<rect x="200" y="{y}" width="{w:.0f}" height="56" rx="10" fill="url(#aBar)"/>'
        b += t(200 + w + 14, y + 41, txt, 32, SUN, anchor="start")
        b += t(200, y + 88, note, 22, MUTED, anchor="start", font=L)
    b += t(400, 376, "NO OFFICIAL GTA VI NUMBER YET", 24, PINK, font=L)
    return fig(b, "GTA V sold 11.2 million copies in its first 24 hours. Sensor Tower estimates GTA VI sold about 19.1 million by the morning of launch day. There is no official GTA VI figure yet")

def launch_bugs():
    b = t(400, 62, "GTA VI LAUNCH WEEK: BUG CHECK", 34)
    cols = [("PLAYER CLIPS", "LOTS", ["CLIPPING AND", "MAP FALLS"]),
            ("PSN OUTAGES", "2", ["NOV 18 AND", "NOV 19"]),
            ("PATCH NOTES", "NONE", ["NO FIX", "ANNOUNCED YET"])]
    for i, (h, big, sub) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 100, 224, 270) + t(cx, 148, h, 26, SUN, font=L)
        b += f'<text x="{cx}" y="262" font-family="{D}" font-size="{96 if len(big) < 3 else 80}" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 314 + j * 30, line, 22, MUTED, font=L)
    return fig(b, "Launch-week status: many player clips of bugs, two PlayStation Network outages on November 18 and 19, and no Rockstar patch notes or fix announcement yet")


def sales_official():
    b = t(400, 62, "DAY-ONE SALES, TAKE-TWO FIGURES", 34)
    rows = [("GTA V", 0.8, "$0.8B", "FIRST DAY, SEPTEMBER 2013"), ("GTA VI", 3.79, "$3.79B", "TO END OF NOVEMBER 19, 2026")]
    for i, (name, val, txt, note) in enumerate(rows):
        y = 112 + i * 120
        w = val * 105
        b += t(40, y + 40, name, 32, anchor="start")
        b += f'<rect x="200" y="{y}" width="{w:.0f}" height="56" rx="10" fill="url(#aBar)"/>'
        b += t(200 + w + 14, y + 41, txt, 32, SUN, anchor="start")
        b += t(200, y + 88, note, 22, MUTED, anchor="start", font=L)
    b += t(400, 376, "PLUS 32.5 MILLION COPIES SOLD BEFORE RELEASE", 24, PINK, font=L)
    return fig(b, "Take-Two says GTA VI made $3.79 billion in retail sales on day one, about five times GTA V's roughly $800 million first day in 2013, and sold 32.5 million copies before release")


def easter_eggs():
    b = t(400, 62, "LAUNCH-WEEK EASTER EGGS", 34)
    cols = [("FAST & FURIOUS", "CAR", ["'95 ECLIPSE,", "VESPUCCI ISLE"], "2 OUTLETS"),
            ("DEXTER", "FLAT", ["APARTMENT ON", "WASHINGTON IS."], "REPORTED"),
            ("TOWER NEST", "EGG", ["THROW ONE FOR", "A CUTSCENE"], "PLAYER CLIP")]
    for i, (h, big, sub, tag) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 96, 224, 284) + t(cx, 140, h, 22 if len(h) > 12 else 24, SUN, font=L)
        b += f'<text x="{cx}" y="244" font-family="{D}" font-size="84" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 290 + j * 28, line, 20, MUTED, font=L)
        b += t(cx, 360, tag, 20, GOOD if tag == "2 OUTLETS" else PINK, font=L)
    return fig(b, "Three launch-week GTA VI easter eggs: a Fast and Furious 1995 Eclipse on Vespucci Island, reported by two outlets; a Dexter-style apartment on Washington Island, reported; and a nest of eggs on a tower that triggers a cutscene, from a player clip")


def dev_notes():
    b = t(400, 62, "FROM ROCKSTAR'S DEVELOPER NOTES", 34)
    cols = [("NPC ROUTINES", "1,000", ["ACTIVITY", "ANIMATION SETS"]),
            ("ONE DOOR", "MONTHS", ["ON LUCIA'S", "HIP DOOR PUSH"]),
            ("THE ASK", "NO", ["GUIDES OR", "CHECKLISTS"])]
    for i, (h, big, sub) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 100, 224, 270) + t(cx, 146, h, 24, SUN, font=L)
        size = 84 if len(big) <= 3 else 62
        b += f'<text x="{cx}" y="250" font-family="{D}" font-size="{size}" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 306 + j * 30, line, 22, MUTED, font=L)
    return fig(b, "From Rockstar's GTA VI developer notes: about 1,000 activity animation sets for background characters, months of work on Lucia pushing a door open with her hip, and a hope that players set aside guides and checklists")


def first_patch():
    b = t(400, 62, "FIRST POST-LAUNCH PATCH: 01.002.002", 34)
    cols = [("PS5 SIZE", "604", ["MB, IN THREE", "ROLLOUT WAVES"]),
            ("XBOX SIZE", "1.6", ["GB, SERIES X|S", "VERSION 1.0.2.2"]),
            ("PATCH NOTES", "7", ["FIXES, NOTES", "POSTED NOV 23"])]
    for i, (h, big, sub) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 100, 224, 270) + t(cx, 148, h, 23, SUN, font=L)
        b += f'<text x="{cx}" y="262" font-family="{D}" font-size="{96 if len(big) < 4 else 80}" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 314 + j * 30, line, 22, MUTED, font=L)
    return fig(b, "GTA VI's first post-launch patch, 01.002.002, released November 23: about 604 MB on PS5 in three rollout waves, about 1.6 GB on Xbox Series X|S as version 1.0.2.2, with Rockstar's notes listing seven fixes")


def patch_notes():
    b = t(400, 58, "PATCH 01.002.002: ROCKSTAR'S NOTES", 32)
    b += panel(40, 86, 250, 290)
    b += f'<text x="165" y="250" font-family="{D}" font-size="150" fill="url(#aNum)" text-anchor="middle">7</text>'
    b += t(165, 300, "FIXES LISTED", 26, SUN, font=L)
    b += t(165, 340, "NO FPS CHANGES", 22, PINK, font=L)
    b += panel(310, 86, 450, 290)
    fixes = ["CRASHES", "WEATHER STUCK", "AUTOSAVE", "STORY PHONE CALLS", "WANTED LEVEL", "GYM DEADLIFT BAR", "PARTNER BAG HANDOVER"]
    for i, f in enumerate(fixes):
        y = 128 + i * 36
        b += f'<circle cx="344" cy="{y - 8}" r="7" fill="{GOOD}"/>' + t(364, y, f, 24, INK, anchor="start", font=L)
    return fig(b, "Rockstar's notes for GTA VI update 01.002.002 list seven fixes: crashes, weather that stopped changing, autosave, story phone calls, wanted levels that could not be lost, the gym deadlift bar and partners not handing over bags. No frame rate or performance changes are listed")


def side_secrets():
    b = t(400, 62, "THREE SIDE SECRETS TO FIND", 34)
    cols = [("OUT AT SEA", "DOG", ["COOL DOG'S", "JET SKI RESCUE"], "OUTLET TESTED"),
            ("PORT GELLHORN", "3", ["MISSING PERSONS", "TO TRACK DOWN"], "OUTLET TESTED"),
            ("BELVILLE", "SIM?", ["A GARAGE FULL", "OF RED STRING"], "PLAYER POST")]
    for i, (h, big, sub, tag) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 96, 224, 284) + t(cx, 140, h, 24 if len(h) < 12 else 20, SUN, font=L)
        b += f'<text x="{cx}" y="244" font-family="{D}" font-size="{96 if len(big) < 4 else 80}" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 290 + j * 28, line, 20, MUTED, font=L)
        b += t(cx, 360, tag, 18, GOOD if "TESTED" in tag else PINK, font=L)
    return fig(b, "Three GTA VI side secrets: Cool Dog, who rescues you on a jet ski if you drift far out to sea, tested by GamesRadar; three missing persons to find around Port Gellhorn, tested by GamesRadar; and a Belville garage covered in simulation-theory notes, from a player post")


def playstation_record():
    b = t(400, 62, "PLAYSTATION'S BIGGEST LAUNCH", 34)
    cols = [("UNIQUE PLAYERS", "39M+", ["ON PS5 IN", "FOUR DAYS"]),
            ("HOURS PLAYED", "683M", ["ACROSS ALL", "PS5 PLAYERS"]),
            ("PER PLAYER", "17.4", ["HOURS ON", "AVERAGE"])]
    for i, (h, big, sub) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 96, 224, 250) + t(cx, 140, h, 20, SUN, font=L)
        b += f'<text x="{cx}" y="244" font-family="{D}" font-size="80" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 290 + j * 28, line, 20, MUTED, font=L)
    b += t(400, 378, "SONY FIGURES, NOVEMBER 19 TO 22, PS5 ONLY", 22, PINK, font=L)
    return fig(b, "Sony says more than 39 million unique players played GTA VI on PS5 from November 19 to 22, for a total of 683 million hours, or 17.4 hours each on average. The figures cover PS5 only")


def vice_portal():
    b = t(400, 62, "THE SECRET VICE CITY PORTAL", 34)
    cols = [("THE PUZZLE", "12", ["LPL POWER", "SUBSTATIONS"], "NO FAST TRAVEL"),
            ("THE CLUE", "1986", ["SPELLS AN OLD", "VICE CITY CHEAT"], "FOUND NOV 23"),
            ("THE TRIP", "2002", ["A PS2-STYLE", "VICE CITY SCENE"], "PLAYER VIDEO")]
    for i, (h, big, sub, tag) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 96, 224, 284) + t(cx, 140, h, 22, SUN, font=L)
        b += f'<ellipse cx="{cx}" cy="216" rx="92" ry="54" fill="none" stroke="{PINK}" stroke-opacity=".35" stroke-width="6"/>'
        b += f'<text x="{cx}" y="244" font-family="{D}" font-size="{84 if len(big) < 3 else 64}" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 290 + j * 28, line, 20, MUTED, font=L)
        b += t(cx, 360, tag, 18, PINK, font=L)
    return fig(b, "GTA VI's secret Vice City portal: a puzzle across 12 LPL power substations with no fast travel, a clue that spells a cheat from the 1986-set Vice City, and a trip to a PS2-style 2002 Vice City scene, shown so far in one player's video from November 23")


def trading_cards():
    b = t(400, 62, "GTA VI TRADING CARDS, FOR REAL", 34)
    cols = [("EACH BOX", "16", ["FOUR PACKS OF", "FOUR CARDS"]),
            ("RAREST", "1/1", ["GOLD LEGEND", "PARALLEL"]),
            ("RELEASE", "DEC", ["2026, PRICE", "NOT ANNOUNCED"])]
    for i, (h, big, sub) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 96, 224, 270)
        b += f'<rect x="{cx - 46}" y="162" width="92" height="122" rx="8" fill="none" stroke="{SUN}" stroke-opacity=".35" stroke-width="3" transform="rotate(-8 {cx} 223)"/>'
        b += t(cx, 140, h, 22, SUN, font=L)
        b += f'<text x="{cx}" y="250" font-family="{D}" font-size="84" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 306 + j * 28, line, 20, MUTED, font=L)
    b += t(400, 390, "PANINI AMERICA WITH ROCKSTAR GAMES", 18, PINK, font=L)
    return fig(b, "Panini's GTA VI Sports Trading Card Collection: four packs of four cards per box, numbered parallels down to a one-of-one Gold Legend, out in December 2026 with no price announced yet")


def hidden_hats():
    b = t(400, 62, "TWO HATS WORTH HUNTING", 34)
    cols = [("LUMMOX COUNTY", "J+L", ["A HIDDEN BLOCK,", "TWO PLUMBER CAPS"], "KOTAKU CONFIRMED", PINK),
            ("PORT GELLHORN", "$35", ["A COWBOY HAT", "AT A YARD SALE"], "CHAPTER 2", SUN)]
    for i, (h, big, sub, tag, col) in enumerate(cols):
        cx = 210 + i * 380
        b += panel(cx - 170, 96, 340, 284) + t(cx, 140, h, 24, SUN, font=L)
        if i == 0:
            b += f'<rect x="{cx - 52}" y="160" width="104" height="104" rx="10" fill="none" stroke="{SUN}" stroke-opacity=".35" stroke-width="4"/>'
        else:
            b += f'<path d="M{cx - 110} 236 Q{cx} 270 {cx + 110} 236 M{cx - 50} 236 Q{cx - 46} 168 {cx} 176 Q{cx + 46} 168 {cx + 50} 236" fill="none" stroke="{SUN}" stroke-opacity=".35" stroke-width="4"/>'
        b += f'<text x="{cx}" y="244" font-family="{D}" font-size="80" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 296 + j * 28, line, 21, MUTED, font=L)
        b += t(cx, 362, tag, 19, GOOD if "CONFIRMED" in tag else col, font=L)
    return fig(b, "Two wearable GTA VI easter eggs: a hidden block in Lummox County that drops J and L caps in the style of Mario and Luigi, confirmed by Kotaku, and a $35 cowboy hat like Arthur Morgan's at a Port Gellhorn yard sale in Chapter 2")


def xbox_glitch():
    b = t(400, 62, "THE XBOX 60 FPS GLITCH, TESTED", 34)
    cols = [("BEST CASE", "60", ["FLYING HIGH,", "LOOKING AT SKY"], GOOD),
            ("FIRST HOUR", "36", ["AVERAGE FPS,", "SERIES X"], SUN),
            ("BUSY STREETS", "30s", ["BARELY ABOVE", "THE NORMAL CAP"], PINK)]
    for i, (h, big, sub, col) in enumerate(cols):
        cx = 152 + i * 248
        b += panel(cx - 112, 96, 224, 260) + t(cx, 140, h, 22, col, font=L)
        b += f'<text x="{cx}" y="250" font-family="{D}" font-size="88" fill="url(#aNum)" text-anchor="middle">{big}</text>'
        for j, line in enumerate(sub):
            b += t(cx, 296 + j * 28, line, 20, MUTED, font=L)
    b += t(400, 386, "AND THE WHOLE GAME RUNS FASTER", 20, PINK, font=L)
    return fig(b, "Digital Foundry's test of the Xbox Quick Resume glitch: about 60 fps only when flying high and looking at the sky, about 36 fps on average over the first hour on Series X, and barely above 30 in busy streets, while the whole game runs faster than normal")
