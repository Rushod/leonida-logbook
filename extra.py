"""Activities, gameplay deep-dives, launch-ready pages, the vehicle and weapon databases, and the interactive map."""
import json
from html import escape as e
from articles2 import page, BRAND
from articles import links

PREVIEW_NOTE = '<p class="note">Based on hands-on previews. Every point gets re-tested in the finished game on launch day.</p>'


def pairs(rows):
    return '<div class="cast">' + "".join(f"<div><b>{e(a)}</b><span>{b}</span></div>" for a, b in rows) + "</div>"


# ---------------- activities ----------------
ACTIVITIES = page("/activities/", "Things to do", "GTA 6 activities and mini-games",
                  "Previews list twelve side activities in GTA VI, from pool and mini-golf to scuba diving and monster truck racing.", "", PREVIEW_NOTE + """
  <h2>The twelve reported activities</h2>
  """ + pairs([
      ("Pool", "Listed in previews. Rules and locations are added at launch."),
      ("Mini-golf", "Listed in previews. Courses are added at launch."),
      ("Kayaking", "Kayaks are among the vehicles you can use on the water."),
      ("Zoo visit", "The zoo is fully explorable. See the <a href=\"/wildlife/\">wildlife guide</a>."),
      ("Scuba diving", "Dive underwater, including down to shipwrecks."),
      ("Parachuting", "Listed in previews. Jump spots are added at launch."),
      ("Off-road racing", "Listed in previews. Race locations are added at launch."),
      ("Monster truck racing", "Listed in previews. Event locations are added at launch."),
      ("Gym workouts", "Three-exercise sessions with timing inputs. See the <a href=\"/gym/\">gym guide</a>."),
      ("Hunting", "Animals can also be studied for a checklist. See <a href=\"/wildlife/\">wildlife</a>."),
      ("Fishing", "Listed in previews. Spots and catches are added at launch."),
      ("Shipwreck treasure hunt", "Search underwater wrecks for treasure."),
  ]) + """
  <h2>What is not a full mini-game</h2>
  <p>Previews say tennis, surfing and skateboarding are not included as full activities.</p>
  <h2>More to do in Leonida</h2>
  <ul>
    <li><b>Robberies.</b> Every store can be robbed, with bigger scores at jewelry stores, small banks and gang compounds. See the <a href="/robberies/">robbery guide</a>.</li>
    <li><b>Time together.</b> Dates and shared activities improve how well Jason and Lucia work together during robberies.</li>
    <li><b>Random events.</b> Examples from previews include a stranger daring you to jump off a bridge and a suspect escaping from a police car.</li>
    <li><b>Livestream events.</b> In-game social media shows events as they happen, and you can travel to where the streamer is.</li>
    <li><b>Eating out.</b> Burger Shot and Cluckin' Bell have drive-thrus, or you can walk inside.</li>
  </ul>
  <p>Tick activities off as you try them in the <a href="/tracker/">progress tracker</a>.</p>""")

GYM = page("/gym/", "Activities", "GTA 6 gym guide: how workouts work",
           "Gym workouts in GTA VI are short sessions of three exercises with timing inputs, and strength only improves if you train three days in a row.", "", PREVIEW_NOTE + """
  <h2>How a workout works</h2>
  <ul>
    <li>A session is three exercises, tracked on a circular indicator.</li>
    <li>Squats and pull-ups use rhythm or timing inputs on the controller triggers.</li>
    <li>Poor timing drains extra stamina.</li>
    <li>Gyms have changing rooms and vending machines.</li>
  </ul>
  <h2>How to gain strength</h2>
  <p>Strength goes up after training on three consecutive in-game days. A single session is not enough.</p>
  <h2>Food and items that help</h2>
  <div class="scroll"><table>
    <tr><th>Item</th><th>Effect</th></tr>
    <tr><td><b>Protein bars</b></td><td>Boost workout gains</td></tr>
    <tr><td><b>Energy drinks</b></td><td>Boost stamina</td></tr>
    <tr><td><b>Painkillers</b></td><td>Help less each time you repeat them</td></tr>
  </table></div>
  <h2>Fighting styles</h2>
  <p>Lucia trains in kickboxing and mixed martial arts. Jason fights in a rougher street style.</p>
  <p>Gym locations get added to the <a href="/map/">interactive map</a> at launch.</p>""")

ROBBERIES = page("/robberies/", "Making money", "GTA 6 robberies: how to make money",
                 "Every store in Leonida can be robbed, and bigger scores include jewelry stores, small banks and gang compounds. How you do the job changes the payout.", "", PREVIEW_NOTE + """
  <h2>Store robberies</h2>
  <ul>
    <li><b>Get in quietly.</b> A lock-picking tool called the Snap Gun opens doors.</li>
    <li><b>Deal with the cameras.</b> You can destroy CCTV footage so it does not identify you.</li>
    <li><b>Reach the back room.</b> Clerks who run can drop the keys.</li>
    <li><b>Wear a mask</b> before you start, so witnesses and cameras cannot record your face.</li>
  </ul>
  <h2>Bigger scores</h2>
  <div class="scroll"><table>
    <tr><th>Target</th><th>What to know</th></tr>
    <tr><td><b>Jewelry stores</b></td><td>Higher value than ordinary stores</td></tr>
    <tr><td><b>Small banks</b></td><td>May pay in marked banknotes, which need a specialist fence</td></tr>
    <tr><td><b>Gang compounds</b></td><td>Listed among the high-value targets</td></tr>
  </table></div>
  <h2>Speed or greed</h2>
  <ul>
    <li><b>Blow the safe:</b> fast, but explosives lower the payout.</li>
    <li><b>Find the combination:</b> full payout, but it takes longer and police may arrive.</li>
    <li><b>Carry more bags:</b> larger bags hold more loot, and your vehicle's storage sets the limit.</li>
  </ul>
  <h2>Turning loot into cash</h2>
  <ul>
    <li>Stolen goods and stolen cars are sold to a fence. Damage lowers what a car is worth.</li>
    <li>High-end cars carry trackers that must be removed at a fence before the car can be sold or registered.</li>
    <li>Cash goes into the account Jason and Lucia share once you deposit it at an ATM. Getting arrested costs you the cash you are carrying.</li>
  </ul>
  <h2>Getting away</h2>
  <p>See the <a href="/wanted-level/">wanted level guide</a> for every reported way to lose the police.</p>""")

WILDLIFE = page("/wildlife/", "The world", "GTA 6 animals, wildlife and the zoo",
                "Every animal species in GTA VI can be studied and added to a checklist, and the zoo is fully explorable.", "", PREVIEW_NOTE + """
  <h2>The wildlife checklist</h2>
  <p>Studying an animal adds its species to a checklist, in the style of Red Dead Redemption 2. The <a href="/tracker/">progress tracker</a> gets the full species list once players have found them.</p>
  <h2>Where to see animals</h2>
  <ul>
    <li><b>The zoo</b> can be explored on foot.</li>
    <li><b>Grassrivers</b>, the wetland region, has shown alligators and flamingos in official footage.</li>
    <li><b>Hunting and fishing</b> are both listed as activities. See <a href="/activities/">all activities</a>.</li>
  </ul>
  <h2>Dogs</h2>
  <ul>
    <li>You can pet dogs, scold them, or feed them treats bought at convenience stores.</li>
    <li>You can ask an owner for permission to pet their dog. Owners and dogs may react warmly, defensively or aggressively.</li>
  </ul>
  <p>Animal locations get added to the <a href="/map/">interactive map</a> as they are found.</p>""")

MISSIONS = page("/missions/", "The story", "GTA 6 missions list",
                "The full GTA VI mission list goes live here once the game is out on November 19, 2026. This is what is known about the story's structure so far.", "", """
  <div class="empty"><b>Mission list at launch</b>Every mission is added in order as it is played and verified.</div>
  <h2>What is known</h2>
  <ul>
    <li>The story is split into chapters and took one Rockstar developer about 80 hours. See <a href="/story-length/">how long GTA 6 is</a>.</li>
    <li>It opens in the Leonida Keys, near Jason's house, before the rest of the map opens up.</li>
    <li>Previews describe missions as less restrictive than in GTA V, with more than one way to complete them.</li>
    <li>You switch between Jason and Lucia in free roam and during missions.</li>
    <li>Some tools arrive through the story. Certain cars stay locked until you have them.</li>
  </ul>
  <h2>What each mission entry will include</h2>
  <ul>
    <li>Where it starts and how to unlock it</li>
    <li>Objectives and any optional goals</li>
    <li>Rewards</li>
    <li>A tick box that saves to your <a href="/tracker/">progress tracker</a></li>
  </ul>""")

COLLECTIBLES = page("/collectibles/", "Completion", "GTA 6 collectibles and hidden items",
                    "Previews have not described a traditional collectibles set yet. Here is what is known about things to find, and how this page will work at launch.", "", """
  <div class="empty"><b>Locations at launch</b>Collectibles are added with map positions as players find them.</div>
  <h2>Things to find, from previews</h2>
  <ul>
    <li><b>Shipwreck treasure.</b> Underwater wrecks can be searched for treasure.</li>
    <li><b>Wildlife.</b> Every species can be studied for a checklist. See <a href="/wildlife/">wildlife</a>.</li>
    <li><b>Hidden areas.</b> Unexplored parts of the map stay hidden until you visit them.</li>
    <li><b>Hideouts.</b> In-game social media posts can reveal them.</li>
    <li><b>Wearable finds.</b> You can pick up and wear items from the world, such as sunglasses dropped in a fight.</li>
  </ul>
  <h2>How this page will work</h2>
  <p>Each collectible gets a location on the <a href="/map/">interactive map</a> and a tick box in the <a href="/tracker/">progress tracker</a>. Nothing is listed until it has been found in the game.</p>""")

# ---------------- databases ----------------
VEHICLE_ROWS = [
    ("'55 Vapid Stanier", "Car", "Vintage Vice City Pack, with any edition bought by launch day"),
    ("'67 Vapid Dominator Buggy", "Buggy", "Ultimate Edition, with Paradise Garage"),
    ("'95 Grotti Cheetah", "Sports car", "Ultimate Edition"),
    ("Shitzu Squalo", "Boat", "Ultimate Edition"),
    ("Vapid Ganado Retro Build", "To be confirmed", "Ultimate Edition, at Jason's safehouse"),
]
WEAPON_ROWS = [
    ("Hawk & Little Morgan Revolver", "Handgun", "Ultimate Edition"),
    ("Snap Gun", "Tool", "Lock-picking tool used in robberies"),
]


# Weapons seen in Rockstar's trailers, screenshots and artwork. Names are descriptive unless Rockstar has named the gun.
WEAPON_CARDS = [
    ("hawk-little-morgan", "Hawk & Little Morgan Revolver", "Handgun", True,
     "A long-barrel revolver with a mounted scope. It is part of the Ultimate Edition, along with personalized weapon variants."),
    ("compact-pistol", "Compact pistol", "Handgun", False,
     "A polymer-frame pistol with an extended magazine, shown lying on a table. A likely everyday sidearm."),
    ("service-pistol", "Service pistol", "Handgun", False,
     "A full-size semi-automatic with an exposed hammer, carried at the hip."),
    ("heavy-pistol", "Heavy pistol", "Handgun", False,
     "A two-tone steel pistol with a long slide, held in a gloved hand."),
    ("revolver", "Revolver", "Handgun", False,
     "A short-barrel revolver held by a character with a rose tattoo on her hand."),
    ("nipper-38", "Nipper 38", "Handgun", False,
     "A compact pistol with \"Nipper38\" engraved on the slide in Rockstar's official artwork. The in-game name may differ."),
    ("carbine-rifle", "Carbine rifle", "Rifle", False,
     "An AR-style rifle with a carry handle, aimed from a rooftop over the city at night."),
    ("short-carbine", "Short carbine", "Rifle", False,
     "A short-barrel AR-style rifle with a railed handguard, held in gloved hands."),
    ("assault-rifle", "Assault rifle", "Rifle", False,
     "An AK-style rifle carried by a masked crew under blue light."),
    ("gold-compact-rifle", "Gold compact rifle", "Rifle", False,
     "A short AK-style rifle with gold-plated metal and white grips, a sign that custom finishes exist."),
    ("rifle-wall", "Rifle wall", "Rifle", False,
     "A wall display of AK-style and AR-style rifles, suggesting a large choice of long guns."),
    ("neon-pistol", "Neon pistol", "Handgun", False,
     "A pistol finished in bright green and black, held by a character in pink gloves. Another sign that custom finishes exist."),
    ("palm-machine-pistol", "Palm-print machine pistol", "SMG", False,
     "A compact machine pistol wrapped in a blue palm-leaf print, held up by a man in tinted glasses."),
    ("camo-smg", "Camo SMG", "SMG", False,
     "A compact submachine gun in a blue camouflage finish, lying on a car seat."),
    ("smg", "Submachine gun", "SMG", False,
     "A full-size SMG with a fixed stock, held by a masked robber under red light."),
    ("double-barrel-shotgun", "Double-barrel shotgun", "Shotgun", False,
     "A long side-by-side shotgun, pointed from a boat at an alligator in the swamp."),
    ("hunting-rifle", "Hunting rifle", "Rifle", False,
     "A wood-stock rifle carried over the shoulder by a hunter in the woods."),
    ("battle-rifle", "Battle rifle", "Rifle", False,
     "A wood-and-steel semi-automatic rifle with a scope, held next to a No Trespassing sign."),
    ("bolt-action-rifle", "Bolt-action rifle", "Rifle", False,
     "A scoped bolt-action rifle with a wooden stock, held low in tall grass."),
    ("machine-gun", "Machine gun", "Heavy", False,
     "A belt-fed machine gun on a shop counter, in a store with more guns on the wall behind."),
    ("grenade-launcher", "Grenade launcher", "Heavy", False,
     "Fired out of a moving car's window during a chase, blowing a police car into the air."),
]


def weapon_cards():
    types = [t for t in ["Handgun", "SMG", "Shotgun", "Rifle", "Heavy"] if any(c[2] == t for c in WEAPON_CARDS)]
    chips = '<button class="chip on" type="button" data-type="">All</button>' + "".join(f'<button class="chip" type="button" data-type="{t}">{t if t == "Heavy" else t + "s"}</button>' for t in types)
    cards = "".join(
        f'<article class="wcard" data-type="{t}"><img src="/img/weapons/{f}.webp" alt="{e(n)} in GTA VI" width="640" height="360" loading="lazy" decoding="async">'
        f'<div class="wbody"><span class="wtype">{t}</span><h3>{e(n)}</h3><p>{e(d)}</p>'
        f'<p class="wname">{"Official name" if named else "Official name not revealed yet"} · Image: Rockstar Games</p></div></article>'
        for f, n, t, named, d in WEAPON_CARDS)
    return f"""<div class="db" data-db data-cards>
  <div class="dbbar"><div class="chips">{chips}</div></div>
  <div class="wcards">{cards}</div>
  <p class="note">{len(WEAPON_CARDS)} weapons seen so far. Official names, stats, prices and where to buy each one are added from launch day.</p></div>"""


def db_table(rows, kind):
    types = sorted({r[1] for r in rows})
    chips = '<button class="chip on" type="button" data-type="">All</button>' + "".join(f'<button class="chip" type="button" data-type="{e(t)}">{e(t)}</button>' for t in types)
    body = "".join(f'<tr data-type="{e(t)}"><td><b>{e(n)}</b></td><td>{e(t)}</td><td>{e(h)}</td></tr>' for n, t, h in rows)
    return f"""<div class="db" data-db>
  <div class="dbbar"><label class="sr" for="q-{kind}">Search {kind}</label><input id="q-{kind}" type="search" placeholder="Search {kind}" autocomplete="off"><div class="chips">{chips}</div></div>
  <div class="scroll"><table><tr><th>Name</th><th>Type</th><th>How to get it</th></tr>{body}</table></div>
  <p class="note" data-empty hidden>Nothing matches that search.</p>
  <p class="note">{len(rows)} confirmed so far. Prices, stats and locations are added from launch day.</p></div>"""


VEHICLES = page("/vehicles/", "Database", "GTA 6 vehicles list",
                "GTA VI is reported to have hundreds of vehicles. This list holds the ones named officially so far and grows from launch day.", "", db_table(VEHICLE_ROWS, "vehicles") + PREVIEW_NOTE + """
  <h2>How vehicles work</h2>
  <ul>
    <li><b>Fuel.</b> Cars and motorcycles have a fuel gauge, and electric vehicles use charging stations.</li>
    <li><b>Handling.</b> Heavier than GTA V, and you cannot steer a flipped car back onto its wheels.</li>
    <li><b>Types.</b> Supercars, off-roaders, boats, kayaks and electric scooters are all reported.</li>
  </ul>
  <h2>Owning a car</h2>
  <ul>
    <li>A stolen car is temporary until you register it. Unregistered cars eventually disappear.</li>
    <li>You start with three garage slots and can buy more garages across Leonida.</li>
    <li>The Scooter Bros app has a driver bring your personal vehicle to you.</li>
    <li>Abandoned personal vehicles are impounded. You can pay a fee to get them back.</li>
  </ul>
  <h2>Stealing a car</h2>
  <ul>
    <li>Older cars open with a slim jim or a smashed window. Modern cars need a key cloner or phone hacking tool.</li>
    <li>The WAINK phone scanner shows a car's locks, value, alarm, tracker and registration cost.</li>
    <li>High-end cars have trackers that alert police. A fence removes them.</li>
  </ul>
  <h2>Shops</h2>
  <ul>
    <li><b>Pay &amp; Spray</b> repaints, repairs, values and registers cars.</li>
    <li><b>Mod Shops</b> each offer their own modifications, including nitrous.</li>
    <li>The trunk stores extra weapons, gear and spare outfits.</li>
  </ul>""")

WEAPONS = page("/weapons/", "Database", "GTA 6 weapons list",
               "Every gun seen in GTA VI's trailers, screenshots and artwork so far. You carry two handguns and two long guns, and keep the rest in your vehicle.", "", weapon_cards() + PREVIEW_NOTE + """
  <h2>What you can carry</h2>
  <ul>
    <li>Up to two concealed handguns and two visible long guns.</li>
    <li>Extra weapons are stored in your vehicle's trunk.</li>
    <li>Walking around with a long gun in view makes people nervous and draws police attention.</li>
  </ul>
  <h2>Ammu-Nation</h2>
  <ul>
    <li>Weapons you drop are not lost. Collect them from any Ammu-Nation locker or your personal vehicle.</li>
    <li>Some branches sell weapons unique to their region.</li>
  </ul>
  <h2>Aiming and Focus</h2>
  <ul>
    <li>Aim assist is light, and you can swap shoulders instantly.</li>
    <li>Focus slows your surroundings and highlights escape routes, police and vehicle weak points.</li>
  </ul>
  <h2>Ending a fight without killing</h2>
  <div class="scroll"><table>
    <tr><th>Crosshair</th><th>Meaning</th></tr>
    <tr><td><b>White</b></td><td>A standard hit</td></tr>
    <tr><td><b>Yellow</b></td><td>The shot will incapacitate</td></tr>
    <tr><td><b>Red</b></td><td>The shot will kill</td></tr>
  </table></div>
  <ul>
    <li>Shots to the knees or arms can stop someone without killing them.</li>
    <li>You can shoot a weapon out of someone's hands, or intimidate them into running.</li>
    <li>Firing near people frightens and disorients them.</li>
  </ul>""")

# ---------------- interactive map ----------------
def map_page():
    """Full-width React Leaflet map (map-app/) above a short explainer. Everything before <!--map--> renders under the header."""
    return f"""<div class="maptitle"><div class="wrap"><span class="eyebrow">Interactive map</span><h1>GTA VI map of Leonida</h1></div></div>
<div id="leonida-map" data-src="/data/locations.json" data-tiles="/tiles/v17/{{z}}/{{z}},{{y}},{{x}}.jpg"><noscript><p class="wrap note">The interactive map needs JavaScript.</p></noscript></div>
<script src="/assets/map-app.js" defer></script>
<!--map-->
  <div class="prose"><span class="eyebrow">About this map</span><h2>A pre-launch map, clearly labelled</h2>
  <p>GTA VI is out on November 19, 2026. Until then, no one has an official map of Leonida, so this one uses the best community reconstruction available: the GTA VI Mapping Community's hand-traced map, built over several years from trailers, screenshots and other pre-release material.</p>
  <ul>
    <li><b>Every marker is speculative today.</b> The 900+ named places come from the same community project and have not been checked in the game.</li>
    <li><b>From launch day</b>, locations we check in the released game are marked Verified, and missions, collectibles, vehicles and weapons are added.</li>
    <li><b>Found markers</b> are saved in your browser, so you can track your progress as you play.</li>
  </ul>
  <h2>Credits</h2>
  <p>Map tiles and landmark data: GTA VI Mapping Community (YANIS v17), distributed by <a href="https://map.gtadb.org" rel="noopener">gtadb.org</a> under <a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener">CC BY 4.0</a>. We removed the map's legend panel, recategorised the data and rewrote the descriptions. Leonida Logbook is not affiliated with Rockstar Games or Take-Two Interactive.</p>
  </div>
  {links("/map/")}"""


EXTRA = [
    ("/map/", "GTA 6 Interactive Map of Leonida" + BRAND, "Interactive GTA VI map of Leonida with 900+ landmarks, stores and activities you can filter, search and tick off. Pre-launch community map, verified locations from launch day.", map_page()),
    ("/activities/", "GTA 6 Activities and Mini-Games: Full List" + BRAND, "The twelve side activities reported for GTA VI, from pool and mini-golf to scuba diving, plus robberies, dates and random events.", ACTIVITIES),
    ("/gym/", "GTA 6 Gym Guide: Workouts and How to Gain Strength" + BRAND, "How gym workouts work in GTA VI: three-exercise sessions, timing inputs, the three-day rule for strength and items that help.", GYM),
    ("/robberies/", "GTA 6 Robberies: How to Make Money" + BRAND, "How store robberies and bigger scores work in GTA VI: the Snap Gun, cameras, safes, marked banknotes, fences and payouts.", ROBBERIES),
    ("/wildlife/", "GTA 6 Animals, Wildlife Checklist and Zoo" + BRAND, "Every animal in GTA VI can be studied for a checklist. What is known about wildlife, the zoo, dogs, hunting and fishing.", WILDLIFE),
    ("/missions/", "GTA 6 Missions List: All Story Missions" + BRAND, "The GTA VI mission list, added in order from launch day, plus what is known about chapters and story structure.", MISSIONS),
    ("/collectibles/", "GTA 6 Collectibles and Hidden Items" + BRAND, "What there is to find in GTA VI so far: shipwreck treasure, wildlife, hidden areas and hideouts. Locations are added at launch.", COLLECTIBLES),
    ("/vehicles/", "GTA 6 Vehicles List: All Cars, Boats and Bikes" + BRAND, "Every GTA VI vehicle confirmed so far and how to get it, plus how fuel, garages, registration, trackers and mod shops work.", VEHICLES),
    ("/weapons/", "GTA 6 Weapons List and How Combat Works" + BRAND, "GTA VI weapons confirmed so far, the two-handgun and two-long-gun carry limit, Ammu-Nation lockers, Focus and non-lethal options.", WEAPONS),
]
