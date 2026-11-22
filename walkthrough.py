"""Story mission walkthrough hub and the 100% completion checklist.

Tick boxes use the same keys here and on /tracker/, so progress is shared.
Mission list: the 91 main missions as listed by KeenGamer (order and names),
cross-checked against GTABase and VGC. 100% list: the 35 in-game requirements,
cross-checked between AlcastHQ and TheGamesWiki."""
from html import escape as e
from articles2 import BRAND
from articles import links

UPDATED = "Updated November 21, 2026"
J, L, B = "Jason", "Lucia", "Jason and Lucia"

# (name, character or None, note or None)
CHAPTERS = [
    ("Chapter 1", "Just Like Paradise", "Jason's life in the Leonida Keys, working odd jobs before Lucia is back in the picture.", [
        ("Prologue", L, "Doubles as the tutorial."),
        ("Gone Fishing", None, None), ("Gear Up", None, None), ("Just a Scratch", None, None),
        ("Lab Fees", None, None), ("Unwanted Attention", None, None), ("Pipework", None, None),
        ("Hey Arnold!", None, None), ("Island Dreams", None, None), ("Feng Shui", None, None),
        ("Coming Home", None, None), ("Buck Me", None, None), ("Clean Up After Donnie", None, None),
        ("Down to Earth", L, "Missable: the next morning, say yes to Lucia's meditation on the balcony. You can't do it after Chapter 1."),
        ("Clear Skies", None, None), ("Day Release", None, None), ("Swamped", None, None),
        ("Don Gone", None, None), ("Recalibration", None, None),
        ("Tourist Trap", None, "Point of no return. Make a manual save and move at least $5,000 into Family Savings first: you lose Jason's first house and the cash you're carrying."),
        ("Home Sweet Home", L, None), ("Discharge Time", None, None),
    ]),
    ("Chapter 2", "Paradise Lost", "Mostly Lucia's chapter, with the pair living out of a motel.", [
        ("What's in the Bag?", L, None), ("Ambulance Chaser", L, None), ("Just Moved In", L, None),
        ("Girls' Trip", L, None), ("Moses", None, None), ("Daily Driver", None, None), ("Slam Dunk", None, None),
        ("Breakfast Run", B, None),
        ("Coffee Break", None, "Finishing this unlocks Bret's target decks for Jason, which you need for 100%."),
        ("Afternoon Delight", None, None),
        ("Checking Out", None, "Point of no return. Have at least $15,000 saved and make a manual save first. The motel stops being your home."),
    ]),
    ("Chapter 3", "Tits Ass Drug Money", "The move to Vice City and the build-up to the first big score.", [
        ("Welcome to Vice City", B, None), ("Dealer's Choice", J, None), ("Meet the Heders", None, None),
        ("Dubious Provenance", None, None), ("Mami Knows Best", L, None), ("South Leonida Real Estate", L, None),
        ("Tyrone", J, None), ("Here, Kitty Kitty", None, None), ("Car Service", L, None),
        ("Top Billing", None, None), ("Boobie Time", None, None), ("First Impressions", None, None),
        ("Caught Slipping", B, None), ("Crosstown Traffic", L, "A tailing job."),
        ("Credit Check", None, "Unlocks bank jobs and payday loan jobs, both needed for 100%."),
        ("Steal the Zorrusso for Randy", None, "Also listed as \"Clonin' Keys, Makin' GS\". It starts Randy's supercar thefts."),
        ("Sinfrontera National Bank", None, None), ("Security Expert", None, None), ("Ride or Die", None, None),
        ("Company Property", None, None), ("The Missing Link", L, None), ("Safe Word", None, None),
        ("Cooties", None, None), ("Bricked Up", B, None), ("Hidden Charges", None, None),
        ("The Cartel Heist", None, "Ends Chapter 3."),
    ]),
    ("Chapter 4", "Vice City, Baby", "Bigger jobs across Vice City, leading to the airport heist.", [
        ("Ocean Beach", B, None), ("Another Life", L, None), ("Company Cars", None, None), ("Lawyer Up", None, None),
        ("Party Hard", None, None), ("Heavy Lifting", B, None), ("Photo/Shoot", None, None), ("Making Gainz", L, None),
        ("Watch It", None, None), ("Cash Injections", L, None), ("Amateur Hour", L, None), ("Dirty Work", None, None),
        ("Too Much Baggage", J, None), ("Adventures in Babysitting", None, None), ("Fresh Evidence", None, None),
        ("Power Play", None, None), ("Child's Play", None, None), ("Headliners", None, None),
        ("Close Surveillance", J, None), ("Delivery Method", J, "Jason goes undercover."), ("Team Building", L, None),
        ("Fully Catered", None, None),
        ("VCIA Takedown", None, "The airport heist. Finish the setup missions before you start it."),
        ("Sunset", B, None), ("Starting From Zero", None, "Ends Chapter 4."),
    ]),
    ("Chapter 5", "Top of the World, Ma", "The final stretch.", [
        ("Bird in the Hand", B, None), ("Taking Liberties", B, None), ("VC Baby", None, None),
        ("Doggie Bag", None, None), ("Operation Savage Glory", None, None), ("Protective Custody", B, None),
        ("The End of the Road", None, "The last mission. Make a separate save first if you want to keep a pre-ending save. Finishing it unlocks cheats and the 100% checklist."),
    ]),
]
MISSION_TOTAL = sum(len(c[3]) for c in CHAPTERS)
assert MISSION_TOTAL == 91, MISSION_TOTAL

MISSABLES = [
    ("Lucia's balcony meditation", "Chapter 1", "Offered the morning after Down to Earth. Gone after Chapter 1."),
    ("Get Shirley's Rum", "Chapter 1", "Optional job that can be missed."),
    ("Steal the Scooter", "Chapter 1", "Optional job that can be missed."),
    ("Race Against Yago", "Chapter 3", "Only open while its hourglass marker shows on the map."),
    ("This Is a Free Call From…", "Chapter 4", "Lucia. Time-limited and missable."),
]


def check(key, title, sub=None):
    small = f"<small>{sub}</small>" if sub else ""
    return f'<li><label><input type="checkbox" id="c-{key}" data-key="{key}"><span>{e(title)}{small}</span></label></li>'


def mission_sub(who, note):
    bits = []
    if who:
        bits.append(f"Play as {who}")
    if note:
        bits.append(e(note))
    return " · ".join(bits) or None


def chapter_groups(collapsible):
    """One tick-box group per chapter. On the walkthrough they fold away to hide later mission names."""
    out = ""
    for ci, (num, name, blurb, missions) in enumerate(CHAPTERS, 1):
        items = "".join(check(f"m{ci}-{mi}", m, mission_sub(w, n)) for mi, (m, w, n) in enumerate(missions))
        head = f'<div class="grouphead"><h3>{num}: {e(name)}</h3><span class="count"></span></div><div class="bar"><i></i></div>'
        if collapsible:
            out += (f'<div class="panel" data-group="m{ci}">{head}'
                    f'<details class="chap"{" open" if ci == 1 else ""}><summary>{len(missions)} missions. {e(blurb)} '
                    f'<span class="show">Show missions</span></summary><ul class="check">{items}</ul></details></div>')
        else:
            out += f'<div class="panel" data-group="m{ci}">{head}<ul class="check">{items}</ul></div>'
    return out


# (name, needed, total or None, tip)
HUNDRED = [
    ("Story & Tasks", [
        ("Story completion", "All main missions", None, "The checklist itself only appears after the credits roll."),
        ("Optional tasks", "100", None, "Car deliveries, meditations, Cal's fishing trips and stranger missions all count."),
        ("Gang operations cleared", "39", 39, "Take every key valuable at each one. Hover over the map icon to see what's still there."),
        ("Bank jobs", "22", 22, "Open after Credit Check in Chapter 3. Clear the drawers and the safe."),
        ("Payday loan jobs", "7", 7, "Also open after Credit Check. Threaten the teller, then empty the back safe."),
        ("Smash 'N' Grabs", "34", 35, "Pawn shops and jewelry stores. Don't skip the back-room safe."),
        ("Stick ups", "50", 91, "Register robberies at convenience, fast food and liquor stores."),
        ("Narcotics fenced", "$100,000", None, "Narcotics come from gang operations and cocaine flamingos."),
        ("Jewelry fenced", "$100,000", None, "From jewelry stores and their safes."),
        ("Marked bills fenced", "$250,000", None, "From banks and payday loan jobs."),
        ("Vaults hit", "8", 8, "Only at the eight large banks, after the Chapter 4 job that opens them. Follow a security van in."),
        ("Vehicles fenced", "$200,000", None, "Sell to Moses, Pay 'N' Spray or Randy. Randy pays most for sports cars."),
    ]),
    ("Exploration & Activities", [
        ("Kenton sets", "5", 7, "Treasure dives around Key Lento. Doing all seven also covers the underwater discoveries."),
        ("Collectible card sets", "15", 18, "There are 480 cards in 18 sets. Any 15 full sets count."),
        ("WAiNK locations scanned", "100", None, "Scan landmarks, curiosities and sculptures with your phone, on foot."),
        ("Underwater discoveries", "33", 33, "Shipwrecks found through Kenton's dives."),
        ("Magazines, books & comics", "30", 34, "Includes book swaps. Duplicates don't count."),
        ("Meditation spots", "15", 18, "Jason and Lucia each meditate at the spots, so each location counts twice."),
        ("Cocaine flamingos destroyed", "100", 125, "Shoot the ones with black and white beaks. Yellow-beaked flamingos don't count."),
        ("Unique playlists", "2", 2, "Scan the posters that unlock them."),
        ("Discovered styles", "70", 79, "Scan tattoo magazines with WAiNK. Luxury watches count too."),
        ("Unique races won", "30", 40, "Blue race icons on the map. Any 30 wins."),
        ("Race challenge gold medals", "10", 13, "Pick the ten you find easiest."),
        ("Shooting range gold medals", "42", 42, "Griffin Shooting Range and Rodgers Ranch. Pay the $5 waiver first."),
        ("Video games played", "4", 4, "Three at home and one arcade machine. Starting each one is enough."),
        ("Pool opponents defeated", "5", 7, "Players wait in bars, taverns and cafes."),
        ("Mini golf locations", "2", 3, "Play one game at any two courses."),
        ("Basketball hoops", "90", 100, "Score at 90 different hoops. The same hoop twice doesn't count."),
        ("Drone time trials", "42", 42, "14 locations with three trials each. Beat par on the first two to open the third."),
        ("Stunts", "300", 397, "Stunt jumps, flying under bridges, knife flights and BASE jumps all count."),
        ("Challenges", "70", 80, "You can skip the ten hardest."),
        ("Bret's target decks", "15", 15, "Jason only, after Coffee Break in Chapter 2. Hunt the animals Bret asks for, with clean kills."),
    ]),
    ("Discovery", [
        ("Base model vehicles scanned", "200", 277, "Scan passing vehicles with WAiNK. Boats and aircraft count."),
        ("Standard issue weapons found", "50", 66, "Hold each weapon once. Buy them at the bigger Ammu-Nations or take them from enemies."),
        ("Animals studied", "100", 255, "Study animals through binoculars. No hunting needed."),
    ]),
]
assert sum(len(g[1]) for g in HUNDRED) == 35


def hundred_groups():
    out = ""
    for gi, (name, rows) in enumerate(HUNDRED):
        items = "".join(check(f"h{gi}-{ri}", n, f"<b>{e(need)}{f' of {tot}' if tot else ''}</b> · {e(tip)}")
                        for ri, (n, need, tot, tip) in enumerate(rows))
        out += (f'<div class="panel" data-group="h{gi}"><div class="grouphead"><h3>{e(name)} ({len(rows)})</h3><span class="count"></span></div>'
                f'<div class="bar"><i></i></div><ul class="check">{items}</ul></div>')
    return out


per_chapter = "".join(f"<tr><td>{c[0]}: {e(c[1])}</td><td class=\"n\">{len(c[3])}</td></tr>" for c in CHAPTERS)
miss_rows = "".join(f"<tr><td><b>{e(a)}</b></td><td>{b}</td><td>{e(c)}</td></tr>" for a, b, c in MISSABLES)

WALKTHROUGH = f"""
  <div class="prose"><span class="eyebrow">Walkthrough</span><h1>GTA 6 walkthrough: every story mission</h1>
  <p class="note">{UPDATED}</p>
  <p class="lede">All {MISSION_TOTAL} main missions in GTA VI, chapter by chapter, in the order you play them. Tick each one off as you finish it, and read the warnings before the two points of no return.</p>
  <div class="facts">
    <div><span>Main missions</span><b>{MISSION_TOTAL}</b></div>
    <div><span>Chapters</span><b>5</b></div>
    <div><span>Mission replay</span><b>No</b></div>
  </div>
  <h2>Read this before you start</h2>
  <ul>
    <li><b>Spoiler-light.</b> Later chapters stay folded so mission names don't give the story away. Open only the chapter you're on.</li>
    <li><b>Two points of no return.</b> <b>Tourist Trap</b> (Chapter 1) takes away Jason's first house and the cash you carry, so bank at least $5,000 first. <b>Checking Out</b> (Chapter 2) ends your stay at the motel; have $15,000 saved. Make a manual save before both.</li>
    <li><b>No replays and no medals.</b> You can't replay a finished mission, and story missions have no gold medal goals, so nothing in a mission is lost by playing it your way.</li>
    <li><b>Nothing for 100% is missable.</b> Everything on the <a href="/100-percent/">100% checklist</a> can still be done in free roam after the story. A few optional side jobs can be missed (listed below), but none count toward 100%.</li>
    <li>Your ticks are saved in this browser and also show on the <a href="/tracker/">progress tracker</a>.</li>
  </ul>
  </div>
  <div class="stack">{chapter_groups(True)}</div>
  <div class="prose">
  <h2>Missions per chapter</h2>
  <div class="scroll"><table><tr><th>Chapter</th><th>Missions</th></tr>{per_chapter}<tr><td><b>Total</b></td><td class="n"><b>{MISSION_TOTAL}</b></td></tr></table></div>
  <h2>Missable optional jobs</h2>
  <p>These aren't part of the {MISSION_TOTAL} and don't count toward 100%, but you can't go back for them once their window closes.</p>
  <div class="scroll"><table><tr><th>Job</th><th>When</th><th>Why it's missable</th></tr>{miss_rows}</table></div>
  <h2>Why some lists show more than {MISSION_TOTAL}</h2>
  <p>The in-game story list also includes short tasks, such as moving money into savings or sending money to someone, between the real missions. Counting those gives about 109 entries. We list only the playable missions; the tasks pop up on your phone and are hard to miss.</p>
  <h2>Mission names and order</h2>
  <p class="note">Mission names and order follow the launch-week mission lists published by KeenGamer, GTABase and VGC, which agree on the missions. A couple of mid-chapter missions swap places between lists because some can be played in either order. Step-by-step guides for single missions are added as we play them.</p>
  </div>
  {links("/walkthrough/")}"""

HUNDRED_PAGE = f"""
  <div class="prose"><span class="eyebrow">Completion</span><h1>GTA 6 100% completion checklist</h1>
  <p class="note">{UPDATED}</p>
  <p class="lede">GTA VI's 100% list has <b>35 requirements</b> in three groups. Most only ask for part of a category, nothing on it is missable, and finishing it unlocks the <b>A Long Road</b> trophy. Tick each line off as you go.</p>
  <div class="facts">
    <div><span>Requirements</span><b>35</b></div>
    <div><span>Missable</span><b>None</b></div>
    <div><span>Rough time</span><b>About 200 hours</b></div>
  </div>
  <h2>How it works</h2>
  <ul>
    <li><b>The list unlocks after the story.</b> Everything you did before still counts. Find it under <b>Progress &gt; Stats &gt; 100% Completion</b>.</li>
    <li><b>The story is half the score.</b> Finishing the story is worth about 50%. The other eleven Story &amp; Tasks lines add about a quarter, and each exploration or discovery line is worth about 1%.</li>
    <li><b>It's lenient.</b> It works out at roughly 60% of everything in the game. Most stranger missions and side quests aren't required, and you only study animals, not hunt them.</li>
    <li><b>Start scanning early.</b> Vehicle scans, animal studies and WAiNK locations pile up naturally while you play the story.</li>
  </ul>
  </div>
  <div class="stack">{hundred_groups()}</div>
  <div class="prose">
  <h2>Where to start</h2>
  <ol>
    <li><b>Play the story</b> with the <a href="/walkthrough/">walkthrough</a>, scanning cars and studying animals along the way.</li>
    <li><b>Rob as you go.</b> Bank and payday loan jobs open after Credit Check in Chapter 3. Fencing the loot covers four more lines. See the <a href="/robberies/">robbery guide</a>.</li>
    <li><b>Do the all-or-nothing lines</b>: 42 shooting range golds, 42 drone trials, 33 underwater discoveries, 15 target decks and all 8 vaults.</li>
    <li><b>Finish the partial lines last</b> and pick the easiest ones: you only need 300 of 397 stunts and 70 of 80 challenges.</li>
  </ol>
  <p>Collectible locations go on the <a href="/map/">interactive map</a> as we verify them. Your ticks here are saved in this browser and show on the <a href="/tracker/">progress tracker</a>.</p>
  <p class="note">Requirements and targets as shown in the game's 100% Completion screen, reported by AlcastHQ, TheGamesWiki and PowerPyx, which agree on all 35 lines. Tips are ours. Weights are approximate.</p>
  </div>
  {links("/100-percent/")}"""

PAGES = [
    ("/walkthrough/", "GTA 6 Walkthrough: All 91 Story Missions in Order" + BRAND,
     "Every GTA VI main mission across all five chapters, in order, with tick boxes, points of no return and missable jobs. Spoiler-light.", WALKTHROUGH),
    ("/100-percent/", "GTA 6 100% Completion Checklist: All 35 Requirements" + BRAND,
     "All 35 GTA VI 100% completion requirements with targets and tips, as a checklist that saves your progress. Nothing is missable.", HUNDRED_PAGE),
]
