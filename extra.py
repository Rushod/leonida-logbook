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

IMG_CREDIT = {}
_GTAV = "Image: GTA V render, for reference. Not yet seen in GTA VI"
_REF = "Reference image, not from GTA VI"
_REALCAR = "Real-world photo, not from GTA VI"
for _s in ["rocket-launcher", "micro-smg", "compact-smg", "pump-shotgun", "sniper-rifle", "grenade", "molotov", "smoke-grenade", "sticky-bomb", "stun-gun", "semi-auto-pistol"]:
    IMG_CREDIT[_s] = _GTAV
for _s in ["flashbang", "speargun", "golf-club"]:
    IMG_CREDIT[_s] = _REF
IMG_CREDIT["classic-sedan-reference"] = _REALCAR


def credit(slug):
    return IMG_CREDIT.get(slug, "Image: Rockstar Games")


WEAPON_CARDS += [
    ("unidentified-long-gun", "Unidentified long gun", "Rifle", False,
     "A woman carries a long, wooden-handled weapon through an abandoned house. It is not clear yet what it is."),
    ("stun-gun", "Stun gun", "Handgun", False,
     "Shown here as GTA V's stun gun. A stun gun has not been seen in GTA VI footage yet, though the game's non-lethal options make one likely."),
    ("semi-auto-pistol", "Semi-auto pistol", "Handgun", False,
     "Shown here as GTA V's pistol icon. Expect a basic pistol like this in GTA VI, with its own name and look."),
    ("micro-smg", "Micro SMG", "SMG", False,
     "Shown here as GTA V's micro SMG. The GTA VI version has not been seen yet."),
    ("compact-smg", "Compact SMG", "SMG", False,
     "Shown here as GTA V's compact SMG with a wooden grip. The GTA VI version has not been seen yet."),
    ("pump-shotgun", "Pump shotgun", "Shotgun", False,
     "Shown here as GTA V's pump shotgun. The GTA VI version has not been seen yet."),
    ("sniper-rifle", "Sniper rifle", "Rifle", False,
     "Shown here as GTA V's scoped sniper rifle. GTA VI's trailers do show scoped hunting rifles."),
    ("rocket-launcher", "Rocket launcher", "Heavy", False,
     "Shown here as GTA V's rocket launcher. A rocket launcher has not been seen in GTA VI footage yet."),
    ("grenade", "Grenade", "Throwable", False,
     "Shown here as GTA V's hand grenade. The GTA VI version has not been seen yet."),
    ("sticky-bomb", "Sticky bomb", "Throwable", False,
     "Shown here as GTA V's remote sticky bomb. The GTA VI version has not been seen yet."),
    ("molotov", "Molotov", "Throwable", False,
     "Shown here as GTA V's Molotov cocktail. The GTA VI version has not been seen yet."),
    ("smoke-grenade", "Smoke grenade", "Throwable", False,
     "Shown here as GTA V's smoke grenade. The GTA VI version has not been seen yet."),
    ("flashbang", "Flashbang", "Throwable", False,
     "Reference image of a stun grenade, not from the game. A flashbang has not been seen in GTA VI footage yet."),
    ("speargun", "Speargun", "Other", False,
     "Reference image of a speargun, not from the game. Scuba diving is a reported activity, so an underwater weapon is possible."),
    ("golf-club", "Golf club", "Other", False,
     "Placeholder photo of a golf ball, not from the game. A golf club as a melee weapon has not been shown in GTA VI yet."),
    ("red-briefcase", "Red briefcase", "Other", False,
     "A red briefcase carried at sunset in a trailer. Whether it is an item you can use is not known yet."),
]


def weapon_cards():
    types = [t for t in ["Handgun", "SMG", "Shotgun", "Rifle", "Heavy", "Throwable", "Other"] if any(c[2] == t for c in WEAPON_CARDS)]
    chips = '<button class="chip on" type="button" data-type="">All</button>' + "".join(f'<button class="chip" type="button" data-type="{t}">{t if t in ("Heavy", "Other") else t + "s"}</button>' for t in types)
    cards = "".join(
        f'<a class="wcard" href="/weapons/{f}/" data-type="{t}"><img src="/img/weapons/{f}.webp" alt="{e(n)} in GTA VI" width="640" height="360" loading="lazy" decoding="async">'
        f'<div class="wbody"><span class="wtype">{t}</span><h3>{e(n)}</h3><p>{e(d)}</p>'
        f'<p class="wname">{"Official name" if named else "Official name not revealed yet"} · {credit(f)}</p></div></a>'
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



# Vehicles seen in Rockstar's trailers and screenshots. Names are descriptive unless the name is official or shown on the vehicle.
# (slug, name, category, kind, name status, description)
OFFICIAL, ON_HULL, DESCRIPTIVE = "Official name", "Name shown on the vehicle", "Official name not revealed yet"
VEHICLE_CARDS = [
    ("shitzu-squalo", "Shitzu Squalo", "Boat", "Cabin cruiser", OFFICIAL, "A white cabin cruiser running past the Vice City skyline at dusk. It comes with the Ultimate Edition."),
    ("seashark", "Seashark", "Boat", "Jet ski", ON_HULL, "A lime-green and purple jet ski with its name across the side, carrying two riders."),
    ("lurepredator-l35p", "Lurepredator L35P", "Boat", "Fishing boat", ON_HULL, "A fishing boat with twin outboard motors and rods set up, with three people fishing off the back."),
    ("superyacht", "Superyacht", "Boat", "Yacht", DESCRIPTIVE, "A large multi-deck motor yacht cruising through open blue water."),
    ("harbour-yacht", "Harbour yacht", "Boat", "Yacht", DESCRIPTIVE, "A big motor yacht moored in a hazy harbour at sunset."),
    ("party-cruiser", "Party cruiser", "Boat", "Yacht", DESCRIPTIVE, "A sleek day cruiser packed with swimmers, with inflatables and jet skis alongside."),
    ("cabin-cruiser", "Cabin cruiser", "Boat", "Cabin cruiser", DESCRIPTIVE, "A white express cruiser flying an American flag, with a jet ski pulled up beside it."),
    ("power-catamaran", "Power catamaran", "Boat", "Cabin cruiser", DESCRIPTIVE, "A twin-hull cruising catamaran with a large cabin, seen from above."),
    ("abandoned-cruiser", "Abandoned cruiser", "Boat", "Cabin cruiser", DESCRIPTIVE, "An old cabin cruiser sitting on dry land in the undergrowth. Whether boats like this can be repaired and used is not known yet."),
    ("wooden-speedboat", "Wooden speedboat", "Boat", "Speedboat", DESCRIPTIVE, "A classic wood-deck speedboat at sunset, with a passenger aiming a gun off the back."),
    ("yellow-powerboat", "Yellow powerboat", "Boat", "Speedboat", DESCRIPTIVE, "A yellow-and-black powerboat cutting a hard turn in front of a container ship."),
    ("racing-catamaran", "Racing catamaran", "Boat", "Speedboat", DESCRIPTIVE, "A blue-and-white twin-hull racing boat skimming past the side of a ship."),
    ("sports-cruiser", "Sports cruiser", "Boat", "Speedboat", DESCRIPTIVE, "A long, dark sports boat with a tan deck, seen from above in clear water."),
    ("runabout", "Runabout", "Boat", "Speedboat", DESCRIPTIVE, "A small open boat crossing green water, seen from straight above."),
    ("bowrider", "Bowrider", "Boat", "Speedboat", DESCRIPTIVE, "An open bowrider shown in red light."),
    ("center-console", "Center-console boat", "Boat", "Fishing boat", DESCRIPTIVE, "A crowded center-console boat at a busy sandbar party, surrounded by jet skis."),
    ("bay-boat", "Bay boat", "Boat", "Fishing boat", DESCRIPTIVE, "A black-and-yellow boat with a shade top, with people climbing on and off it."),
    ("rib", "Rigid inflatable", "Boat", "Small boat", DESCRIPTIVE, "A grey rigid inflatable boat with a big outboard, carrying a group across green water."),
    ("black-rib", "Black inflatable", "Boat", "Small boat", DESCRIPTIVE, "A black rigid inflatable racing through shallow turquoise water."),
    ("patrol-boat", "Patrol boat", "Boat", "Small boat", DESCRIPTIVE, "A dark, enclosed rigid-hull boat moving fast across open water."),
    ("kayak", "Kayak", "Boat", "Small boat", DESCRIPTIVE, "An orange sit-on kayak, paddled across calm water at sunset."),
    ("airboat", "Airboat", "Boat", "Small boat", DESCRIPTIVE, "A fan-driven airboat in a cage, racing down a clear swamp channel."),
    ("jet-skis", "Jet skis", "Boat", "Jet ski", DESCRIPTIVE, "Orange and yellow jet skis parked together at the water's edge."),
    ("police-boat", "Police boat", "Boat", "Emergency", DESCRIPTIVE, "A marked police boat with blue trim and twin outboards, seen from above."),
    ("water-taxi", "Water taxi", "Boat", "Public transport", DESCRIPTIVE, "A yellow open-sided water taxi carrying passengers along a city waterway."),
    ("container-ship", "Container ship", "Boat", "Ship", ON_HULL, "A container ship with \"BTN Delmar\" on its hull, docked in the port under the cranes."),
    ("port-work-boat", "Port work boat", "Boat", "Ship", DESCRIPTIVE, "A boxy work boat moving through the port beneath the container cranes."),
    ("river-barge", "River barge", "Boat", "Ship", DESCRIPTIVE, "A low barge carrying cargo along the river at night."),
    ("cruise-ship", "Cruise ship", "Boat", "Ship", DESCRIPTIVE, "A huge cruise ship seen from the highway, behind an East 404 sign."),
    ("armored-truck", "Armored truck", "Commercial", "Armored", DESCRIPTIVE, "A Gruppe 6 armored security truck with its doors open, held up by masked robbers."),
    ("box-semi-truck", "Box semi-truck", "Commercial", "Semi-truck", DESCRIPTIVE, "A white semi-truck cab pulling a box trailer, stopped next to a red muscle car."),
    ("tanker-truck", "Tanker truck", "Commercial", "Semi-truck", DESCRIPTIVE, "A semi-truck hauling a rust-coloured tanker trailer along the highway."),
    ("beer-semi-truck", "Beer delivery semi", "Commercial", "Semi-truck", DESCRIPTIVE, "A semi-truck with a Patriot Beer trailer, rolling down the highway under red light."),
    ("red-box-truck", "Red box truck", "Commercial", "Truck", DESCRIPTIVE, "A red medium-duty truck with a box body, parked at the roadside."),
    ("beverage-truck", "Beverage truck", "Commercial", "Truck", DESCRIPTIVE, "A red delivery truck with a drinks advert on its body, parked by a store."),
    ("azteca-gold-truck", "Azteca Gold truck", "Commercial", "Truck", DESCRIPTIVE, "A cab-over box truck in yellow and green Azteca Gold livery."),
    ("cement-mixer", "Cement mixer", "Commercial", "Truck", DESCRIPTIVE, "A red cement mixer truck driving past shops on a city street."),
    ("stake-bed-truck", "Stake-bed truck", "Commercial", "Truck", DESCRIPTIVE, "A yellow-cab truck with a slatted cargo bed, partly hidden behind a passing car."),
]
VEHICLE_CARDS += [
    ("luxury-coupe", "Luxury coupe", "Car", "Coupe", DESCRIPTIVE, "A dark grey two-door luxury coupe parked at the kerb next to a parking meter."),
    ("takio-race-car", "Takio race car", "Car", "Coupe", DESCRIPTIVE, "A battered coupe in Takio race livery, lined up with other race cars. A hint that street or circuit racing is in the game."),
    ("green-luxury-convertible", "Luxury convertible", "Car", "Convertible", DESCRIPTIVE, "A pale green luxury convertible stopped beside a police car on a sunny street of cafes."),
    ("red-convertible", "Red convertible", "Car", "Convertible", DESCRIPTIVE, "A red two-door convertible with the roof up, driving past a row of portable toilets."),
    ("black-convertible", "Black convertible", "Car", "Convertible", DESCRIPTIVE, "A black convertible pulling away at night with its tail lights glowing through tyre smoke."),
    ("party-convertible", "Party convertible", "Car", "Convertible", DESCRIPTIVE, "An open convertible with a passenger dancing on the back as it drives under a highway."),
    ("maroon-hatchback", "Hatchback", "Car", "Compact", DESCRIPTIVE, "A maroon five-door hatchback driving through a city street."),
    ("abandoned-classic", "Abandoned classic", "Car", "Classic", DESCRIPTIVE, "A rusted 1950s-style car with tail fins, left to rot in an overgrown yard."),
]
VEHICLE_CARDS += [
    ("white-coupe", "White coupe", "Car", "Coupe", DESCRIPTIVE, "A white coupe pulling away from a street lined with flowers and palms. The shot is soft, so details are hard to make out."),
    ("highway-coupe", "Highway coupe", "Car", "Coupe", DESCRIPTIVE, "A dark coupe on the highway behind the barrier, seen at a distance."),
    ("exploding-coupe", "Exploding coupe", "Car", "Coupe", DESCRIPTIVE, "A coupe caught in an explosion, too blurred by the blast to see its details."),
    ("classic-sedan-reference", "Classic sedan", "Car", "Classic", DESCRIPTIVE, "A real-world 1960s American sedan, shown for reference only. A car like it may appear in GTA VI, but Rockstar has not shown it."),
    ("night-semi-truck", "Night semi-truck", "Commercial", "Semi-truck", DESCRIPTIVE, "A semi-truck under a highway at night, with only its lights and outline clear."),
    ("offshore-speedboat", "Offshore speedboat", "Boat", "Speedboat", DESCRIPTIVE, "A white speedboat bouncing through the waves, seen from far away."),
    ("sunset-speedboat", "Sunset speedboat", "Boat", "Speedboat", DESCRIPTIVE, "A low speedboat crossing the water in a red-tinted shot."),
    ("moored-speedboat", "Moored speedboat", "Boat", "Speedboat", DESCRIPTIVE, "A small dark speedboat tied up beside a dock, seen from above."),
    ("distant-cruiser", "Distant cruiser", "Boat", "Cabin cruiser", DESCRIPTIVE, "A cabin cruiser far out on dark water, seen from a long way off."),
    ("blue-fishing-boat", "Blue fishing boat", "Boat", "Fishing boat", DESCRIPTIVE, "A blue-and-white fishing boat moored at a dock at night."),
    ("swamp-airboat", "Swamp airboat", "Boat", "Small boat", DESCRIPTIVE, "An airboat gliding through golden morning fog among the reeds."),
]
VEHICLE_CARDS += [
    ("electric-scooter", "Electric scooter", "Cycle", "Scooter", DESCRIPTIVE, "A rental-style electric scooter ridden down a sunny street past mural-covered shops."),
    ("mountain-bike", "Mountain bike", "Cycle", "Bicycle", DESCRIPTIVE, "A blue and purple mountain bike with knobbly tyres, parked at a wavy rack by a tiled wall."),
    ("road-bike", "Road bike", "Cycle", "Bicycle", DESCRIPTIVE, "A thin-tyred bike parked at a wavy bike rack, half hidden behind a post."),
    ("beach-cruiser", "Beach cruiser", "Cycle", "Bicycle", DESCRIPTIVE, "A rusty red beach cruiser with wide handlebars, leaning on a bike rack."),
    ("bmx", "BMX", "Cycle", "Bicycle", DESCRIPTIVE, "A small BMX with a yellow seat, parked at a bike rack on the pavement."),
    ("bike-share-bikes", "Bike-share bikes", "Cycle", "Bike share", DESCRIPTIVE, "Blue bike-share bikes lined up at a docking station. Whether you can rent them is not known yet."),
]
VEHICLE_CARDS += [
    ("vice-city-police-cruiser", "Vice City police cruiser", "Emergency", "Police", DESCRIPTIVE, "A white Vice City Police sedan with blue stripes, splashing down a wet street lined with cafes."),
    ("sheriff-patrol-car", "Sheriff patrol car", "Emergency", "Sheriff", DESCRIPTIVE, "A white sheriff's car with green stripes and county markings, lights on."),
    ("sheriff-cruiser", "Sheriff cruiser", "Emergency", "Sheriff", DESCRIPTIVE, "A green-and-white sheriff's sedan with its headlights blazing."),
    ("sheriff-suv", "Sheriff SUV", "Emergency", "Sheriff", DESCRIPTIVE, "A mud-splattered white sheriff's SUV in a chase off-road at night."),
    ("police-suv", "Police SUV", "Emergency", "Police", DESCRIPTIVE, "A grey police SUV with blue lights, tearing through water and brush."),
    ("police-pickup", "Police pickup", "Emergency", "Police", DESCRIPTIVE, "A dark police pickup truck with a heavy push bar on the front."),
    ("damaged-police-sedan", "Damaged police sedan", "Emergency", "Police", DESCRIPTIVE, "A battered dark police sedan scraping along with sparks flying from a wheel."),
    ("police-muscle-car", "Police muscle car", "Emergency", "Police", DESCRIPTIVE, "A white muscle-style police car with its lights on, seen from above at night."),
    ("unmarked-police-car", "Unmarked police car", "Emergency", "Police", DESCRIPTIVE, "A black sedan with a hidden blue light, stopped with its doors open."),
    ("unmarked-police-suv", "Unmarked police SUV", "Emergency", "Police", DESCRIPTIVE, "A black SUV flashing red and blue lights in traffic."),
    ("armored-police-truck", "Armored police truck", "Emergency", "Police", DESCRIPTIVE, "A heavy armored police truck pushing through gunfire. Likely a sign of a high wanted level."),
    ("fire-truck", "Fire truck", "Emergency", "Fire", DESCRIPTIVE, "A lime-green fire engine with its lights on, crossing a bridge."),
    ("ambulance", "Ambulance", "Emergency", "Medical", DESCRIPTIVE, "An ambulance with its lights on, parked on a city street at night."),
    ("lifeguard-pickup", "Lifeguard pickup", "Emergency", "Lifeguard", DESCRIPTIVE, "A white-and-red lifeguard pickup parked on a crowded beach."),
]
VEHICLE_CARDS += [
    ("vice-city-police-helicopter", "Vice City police helicopter", "Aircraft", "Police helicopter", DESCRIPTIVE, "A Vice City police helicopter hovering low over dark water, with an officer in the open door."),
    ("coastal-police-helicopter", "Coastal police helicopter", "Aircraft", "Police helicopter", DESCRIPTIVE, "A green-and-white police helicopter chasing a wooden speedboat across the water at sunset."),
    ("gunship-helicopter", "Gunship helicopter", "Aircraft", "Helicopter", DESCRIPTIVE, "An olive helicopter with mounted guns, a gunner leaning out as it skims low over the swamp."),
    ("camera-helicopter", "Camera helicopter", "Aircraft", "Helicopter", DESCRIPTIVE, "A red-and-white helicopter with someone filming from the open door above the clouds."),
    ("executive-helicopter", "Executive helicopter", "Aircraft", "Helicopter", DESCRIPTIVE, "A sleek twin-engine helicopter flying against a purple evening sky."),
    ("gold-helicopter", "Gold helicopter", "Aircraft", "Helicopter", DESCRIPTIVE, "A man climbs out of a gold-and-silver helicopter high above the city lights at night."),
    ("dusk-helicopter", "Dusk helicopter", "Aircraft", "Helicopter", DESCRIPTIVE, "A blue-and-white helicopter at dusk with its red lights on. The shot is soft, so details are hard to make out."),
    ("float-helicopter", "Float helicopter", "Aircraft", "Helicopter", DESCRIPTIVE, "Artwork of a small bubble-cockpit helicopter on pontoons, fitted with a mounted minigun, flying over the city."),
]
IMG_CREDIT["float-helicopter"] = "Artwork, source unconfirmed"
VEHICLE_CARDS += [
    ("excavator", "Excavator", "Industrial", "Construction", DESCRIPTIVE, "A tracked excavator, its arm raised over a street in the middle of a gunfight."),
    ("dump-truck", "Dump truck", "Industrial", "Construction", DESCRIPTIVE, "A dark dump truck with a high steel body, stuck in traffic on a city street."),
    ("six-wheel-tipper", "Six-wheel tipper", "Industrial", "Construction", DESCRIPTIVE, "A tipper truck at a work site, with workers in hi-vis vests around it. The shot is blurry."),
    ("rubble-truck", "Rubble truck", "Industrial", "Construction", DESCRIPTIVE, "A dump truck seen from above. The shot is very blurry, so details are hard to make out."),
    ("bulldozer", "Bulldozer", "Industrial", "Construction", DESCRIPTIVE, "Shown here as GTA V's tracked bulldozer. A bulldozer has not been seen in GTA VI footage yet."),
    ("gta-v-cement-mixer", "Cement mixer (GTA V)", "Industrial", "Construction", DESCRIPTIVE, "GTA V's cement mixer, shown for comparison. For the GTA VI version, see the cement mixer under Commercial."),
]
IMG_CREDIT["bulldozer"] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
IMG_CREDIT["gta-v-cement-mixer"] = "Image: GTA V screenshot, for comparison"
VEHICLE_CARDS += [
    ("tank", "Tank", "Military", "Tank", DESCRIPTIVE, "Shown here as GTA V's desert-camo battle tank. A tank has not been seen in GTA VI footage yet, but every recent GTA has had one."),
]
IMG_CREDIT["tank"] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
VEHICLE_CARDS += [
    ("green-superbike", "Green superbike", "Bike", "Sportbike", DESCRIPTIVE, "A green-and-white superbike with race numbers, with a man in a tank top standing beside it."),
    ("white-superbike", "White superbike", "Bike", "Sportbike", DESCRIPTIVE, "A white superbike with pink wheels, parked on a neon-lit street."),
    ("yellow-sportbike", "Yellow sportbike", "Bike", "Sportbike", DESCRIPTIVE, "A woman in a leather jacket sits on a yellow sportbike outside a liquor bar at night."),
    ("lime-sportbike", "Lime sportbike", "Bike", "Sportbike", DESCRIPTIVE, "A rider on a lime-green sportbike next to a pink one at a street meet-up."),
    ("teal-sportbike", "Sportbike", "Bike", "Sportbike", DESCRIPTIVE, "Two riders on a sportbike outside a cafe, in a teal-tinted shot."),
    ("street-bike", "Street bike", "Bike", "Sportbike", DESCRIPTIVE, "A dark naked street bike parked by a wall. The shot is blurry."),
    ("touring-cruiser", "Touring cruiser", "Bike", "Cruiser", DESCRIPTIVE, "A heavy touring motorcycle ridden by a biker in a club vest."),
    ("red-cruiser", "Red cruiser", "Bike", "Cruiser", DESCRIPTIVE, "A red cruiser with a big chrome headlight, ridden under a blue sky."),
    ("chopper", "Chopper", "Bike", "Cruiser", DESCRIPTIVE, "A long-fork chopper parked at night with bikers standing around it."),
    ("tattoo-shop-motorcycle", "Tattoo shop motorcycle", "Bike", "Cruiser", DESCRIPTIVE, "A motorcycle parked outside a neon-lit tattoo shop at night."),
    ("bobber", "Bobber", "Bike", "Cruiser", DESCRIPTIVE, "Shown here as a GTA V bobber-style bike in blue and white. Not seen in GTA VI yet."),
    ("muddy-dirt-bike", "Muddy dirt bike", "Bike", "Dirt bike", DESCRIPTIVE, "A rider on a mud-caked dirt bike, splashing through the swamp."),
    ("neon-dirt-bike", "Neon dirt bike", "Bike", "Dirt bike", DESCRIPTIVE, "A pink-and-black dirt bike carrying two riders through a smoky crowd."),
    ("scrambler", "Scrambler", "Bike", "Dirt bike", DESCRIPTIVE, "An olive-green scrambler with knobbly tyres, parked by a teal garage door."),
    ("moped", "Moped", "Bike", "Scooter", DESCRIPTIVE, "A black moped ridden along a palm-lined street."),
    ("retro-scooter", "Retro scooter", "Bike", "Scooter", DESCRIPTIVE, "A mint-green retro scooter on a dark street."),
    ("mobility-scooter", "Mobility scooter", "Bike", "Scooter", DESCRIPTIVE, "A blue three-wheel mobility scooter ridden by an older man in a bright shirt."),
    ("police-motorcycle", "Police motorcycle", "Bike", "Police", DESCRIPTIVE, "Shown here as GTA V's police motorcycle. A police bike has not been seen in GTA VI footage yet."),
]
IMG_CREDIT["bobber"] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
IMG_CREDIT["police-motorcycle"] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
VEHICLE_CARDS += [
    ("vapid-ganado", "Vapid Ganado", "Car", "Muscle", OFFICIAL, "A yellow car-based pickup with a striped hood scoop, drifting along the seafront. The Ultimate Edition includes a Vapid Ganado Retro Build at Jason's safehouse."),
    ("buccaneer", "Buccaneer", "Car", "Lowrider", ON_HULL, "A green metal-flake lowrider convertible with gold trim, gold wire wheels and \"Buccaneer\" on the grille, parked by the bay."),
    ("deviant", "Deviant", "Car", "Muscle", ON_HULL, "A muscle car in a stars-and-stripes flag livery, with \"Deviant\" script on the side."),
    ("red-muscle-coupe", "Red muscle coupe", "Car", "Muscle", DESCRIPTIVE, "A 1970s-style red muscle coupe with a shaker hood, parked by a fire hydrant."),
    ("red-widebody-muscle-car", "Red modern muscle car", "Car", "Muscle", DESCRIPTIVE, "A red modern muscle coupe with a wide stance, rolling through traffic."),
    ("modern-muscle-car", "Grey modern muscle car", "Car", "Muscle", DESCRIPTIVE, "A dark grey modern muscle coupe crossing an intersection."),
    ("muscle-sedan", "Muscle sedan", "Car", "Muscle", DESCRIPTIVE, "A grey four-door muscle sedan with LED headlights, driving down a residential street."),
    ("black-muscle-car", "Black muscle car", "Car", "Muscle", DESCRIPTIVE, "A black muscle car with a gold stripe and wide tail lights. The shot is blurred."),
    ("striped-muscle-car", "Striped muscle car", "Car", "Muscle", DESCRIPTIVE, "A red muscle car with black stripes, parked in the dirt by a wooden shack. The shot is blurry."),
    ("airborne-muscle-car", "Airborne muscle car", "Car", "Muscle", DESCRIPTIVE, "A red muscle car flying through the air with its headlights blazing."),
    ("night-muscle-car", "Muscle car at night", "Car", "Muscle", DESCRIPTIVE, "A muscle car's headlights glaring through the dark. The car itself is hard to make out."),
    ("pinstriped-lowrider", "Pinstriped lowrider", "Car", "Lowrider", DESCRIPTIVE, "A blue lowrider with pinstriped paint at a busy street car meet."),
    ("blue-donk", "Blue donk", "Car", "Custom", DESCRIPTIVE, "A blue classic sedan on oversized chrome wheels, kicking up tyre smoke."),
    ("gold-front-classic", "Gold-front classic", "Car", "Classic", DESCRIPTIVE, "A classic car with a gold front end, blurred by motion as it passes."),
    ("pink-classic-convertible", "Pink classic convertible", "Car", "Classic", DESCRIPTIVE, "A faded pink 1960s-style convertible cruising past white arched buildings."),
    ("maroon-coupe", "Maroon coupe", "Car", "Classic", DESCRIPTIVE, "A maroon coupe driving along a quiet road at dusk."),
    ("patriot-race-car", "Patriot race car", "Car", "Race car", DESCRIPTIVE, "A black number 18 race car in Patriot Beer livery, racing in a pack. Along with the Takio car, a strong hint of circuit racing."),
    ("purple-hi-rider", "Purple hi-rider", "Car", "Custom", DESCRIPTIVE, "Artwork of a purple classic on lifted suspension and gold wheels, with a 305 plate."),
    ("hot-rod", "Hot rod", "Car", "Classic", DESCRIPTIVE, "Shown here as GTA V's red hot rod. Not seen in GTA VI yet."),
    ("minivan", "Minivan", "Car", "Van", DESCRIPTIVE, "Shown here as GTA V's two-tone minivan. Not seen in GTA VI yet."),
]
IMG_CREDIT["purple-hi-rider"] = "Artwork, source unconfirmed"
IMG_CREDIT["hot-rod"] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
IMG_CREDIT["minivan"] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
VEHICLE_CARDS += [
    ("red-classic-convertible", "Red classic convertible", "Car", "Classic", DESCRIPTIVE, "Jason drives a red classic convertible along a coastal road, with Lucia beside him holding a pistol."),
    ("teal-fastback", "Teal fastback", "Car", "Muscle", DESCRIPTIVE, "A teal classic fastback with a brown side stripe and a rear wing."),
    ("red-hood-classic", "Red-hood classic", "Car", "Muscle", DESCRIPTIVE, "A grey classic with a red hood and round headlights, cruising past a roadside sign."),
    ("silver-muscle-convertible", "Silver muscle convertible", "Car", "Muscle", DESCRIPTIVE, "A modern silver muscle convertible with two people inside, parked at the roadside."),
    ("pink-donk", "Pink donk", "Car", "Custom", DESCRIPTIVE, "A hot pink classic coupe on big custom wheels at a street car meet."),
    ("cream-classic", "Cream classic", "Car", "Classic", DESCRIPTIVE, "A close-up of a cream classic car rushing past. The shot is blurred."),
    ("orange-muscle-coupe", "Orange muscle coupe", "Car", "Muscle", DESCRIPTIVE, "Shown here as GTA V's orange muscle coupe with a white stripe. Not seen in GTA VI yet."),
    ("grey-classic-coupe", "Grey classic coupe", "Car", "Muscle", DESCRIPTIVE, "Shown here as GTA V's grey classic coupe. Not seen in GTA VI yet."),
]
IMG_CREDIT["orange-muscle-coupe"] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
IMG_CREDIT["grey-classic-coupe"] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
VEHICLE_CARDS += [
    ("vapid-dominator-buggy", "'67 Vapid Dominator Buggy", "Off-road", "Buggy", OFFICIAL, "A lifted classic muscle car turned mud buggy, with roof lights and racing stripes, tearing through a muddy trail. It comes with the Ultimate Edition, along with Paradise Garage."),
    ("reclaimer", "Reclaimer", "Off-road", "Pickup", ON_HULL, "A silver full-size pickup with \"Reclaimer\" across the tailgate, driving down the highway."),
    ("off-road-pickup", "Off-road pickup", "Off-road", "Pickup", DESCRIPTIVE, "A grey off-road pickup with a black hood stripe, parked next to a man in a work shirt."),
    ("grey-pickup", "Grey pickup", "Off-road", "Pickup", DESCRIPTIVE, "A big grey pickup rolling through city traffic."),
    ("silver-pickup", "Silver pickup", "Off-road", "Pickup", DESCRIPTIVE, "A silver four-door pickup crossing an intersection."),
    ("two-tone-pickup", "Two-tone pickup", "Off-road", "Pickup", DESCRIPTIVE, "A red-and-white classic pickup covered in bumper stickers, carrying two men in cowboy hats."),
    ("lifted-classic-pickup", "Lifted classic pickup", "Off-road", "Pickup", DESCRIPTIVE, "A cream lifted classic pickup with roof lights, driving down a country road."),
    ("lifted-lime-pickup", "Lifted lime pickup", "Off-road", "Pickup", DESCRIPTIVE, "A lime-green pickup on huge off-road tyres, parked under red light."),
    ("orange-pickup", "Orange pickup", "Off-road", "Pickup", DESCRIPTIVE, "An orange pickup glimpsed through a haze. The shot is very blurry."),
    ("classic-suv", "Classic SUV", "Off-road", "SUV", DESCRIPTIVE, "A dark brown boxy SUV splashing through a puddle past white arches."),
    ("white-4x4", "White 4x4", "Off-road", "SUV", DESCRIPTIVE, "A white 4x4 with people in front of it. The shot is very blurry."),
    ("military-style-4x4", "Military-style 4x4", "Off-road", "SUV", DESCRIPTIVE, "Shown here as GTA V's red military-style 4x4 with a grille guard. Not seen in GTA VI yet."),
    ("canis-4x4", "Canis 4x4", "Off-road", "SUV", DESCRIPTIVE, "A green lifted 4x4 with \"Canis\" on the grille, shown as GTA Online promo art. Not seen in GTA VI yet."),
    ("monster-truck", "Monster truck", "Off-road", "Monster truck", DESCRIPTIVE, "A monster truck in a flag livery, blurred in motion. Monster truck racing is one of the reported activities."),
    ("six-wheel-off-roader", "Six-wheel off-roader", "Off-road", "Monster truck", DESCRIPTIVE, "A large six-wheel off-road vehicle in an orange haze. The shot is very blurry."),
    ("quad-bike", "Quad bike", "Off-road", "ATV", DESCRIPTIVE, "A rider in a helmet launching a lime-green quad bike into the air."),
    ("beach-atv", "Beach ATV", "Off-road", "ATV", DESCRIPTIVE, "A red utility ATV with racks, parked on the beach."),
    ("lime-buggy", "Lime buggy", "Off-road", "Buggy", DESCRIPTIVE, "A lime-green off-road buggy kicking up dirt. The shot is blurry."),
    ("beach-bug", "Beach bug", "Off-road", "Buggy", DESCRIPTIVE, "Shown here as GTA V's orange off-road beetle with big tyres. Not seen in GTA VI yet."),
    ("beach-vehicle", "Beach vehicle", "Off-road", "Buggy", DESCRIPTIVE, "Two beachgoers walk in front of a blue vehicle on the sand. The vehicle is too blurred to identify."),
]
for _s in ["military-style-4x4", "beach-bug"]:
    IMG_CREDIT[_s] = "Image: GTA V screenshot, for reference. Not yet seen in GTA VI"
IMG_CREDIT["canis-4x4"] = "Image: GTA Online artwork, for reference. Not yet seen in GTA VI"
VEHICLE_CARDS += [
    ("mud-run-pickup", "Mud-run pickup", "Off-road", "Pickup", DESCRIPTIVE, "A lifted red pickup with roof lights and a snorkel, with a mud-covered couple leaning on it at an off-road meet."),
    ("green-pickup", "Green pickup", "Off-road", "Pickup", DESCRIPTIVE, "A green pickup on a street, behind a cyclist and a dog."),
]
VEHICLE_CARDS += [
    ("stunt-biplane", "Stunt biplane", "Aircraft", "Plane", DESCRIPTIVE, "A pink biplane in a crypto-coin livery, with a wing walker holding a smoke flare as it flies over the beach."),
    ("seaplane", "Seaplane", "Aircraft", "Plane", DESCRIPTIVE, "A white-and-yellow floatplane flying low over turquoise water near the coast."),
    ("crop-duster", "Crop duster", "Aircraft", "Plane", DESCRIPTIVE, "A crop-dusting plane banking low through a dusty sky."),
    ("light-plane", "Light plane", "Aircraft", "Plane", DESCRIPTIVE, "A small high-wing propeller plane in a pale sky."),
    ("twin-prop-plane", "Twin-prop plane", "Aircraft", "Plane", DESCRIPTIVE, "A small twin-propeller plane among the clouds. The shot is blurry."),
    ("business-jet", "Business jet", "Aircraft", "Jet", DESCRIPTIVE, "A twin-engine business jet climbing at sunset, seen from below."),
    ("private-jet", "Private jet", "Aircraft", "Jet", DESCRIPTIVE, "A private jet parked outside a hangar at dusk, with another behind it."),
    ("autograph-jet", "Autograph jet", "Aircraft", "Jet", DESCRIPTIVE, "A black-and-gold private jet with \"Autograph\" on the tail, seen through an airport lounge window."),
    ("jumbo-jet", "Jumbo jet", "Aircraft", "Jet", DESCRIPTIVE, "A four-engine airliner climbing past the clouds."),
    ("blimp", "Blimp", "Aircraft", "Airship", DESCRIPTIVE, "A white blimp floating over an island off the coast."),
]
PLURAL = {"Off-road": "Off-road", "Military": "Military", "Industrial": "Industrial", "Emergency": "Emergency", "Cycle": "Cycles", "Boat": "Boats", "Commercial": "Commercial", "Car": "Cars", "Bike": "Motorcycles", "Aircraft": "Aircraft"}
CAT_TEXT = {
    "Boat": ("Boats in Leonida", "Leonida has a long coastline, the Leonida Keys and inland swamps, so boats are a big part of getting around. Where to buy, store and dock each boat is added from launch day."),
    "Car": ("Cars in Leonida", "Cars use fuel and electric cars use charging stations. A stolen car is only yours once you register it at Pay &amp; Spray, and you start with three garage slots. See the <a href=\"/vehicles/\">vehicles guide</a> for how stealing, trackers and mod shops work."),
    "Cycle": ("Bikes and scooters", "Bicycles and electric scooters are part of Leonida's streets, and electric scooters are one of the reported vehicle types. How you rent, buy or store them is confirmed from launch day."),
    "Emergency": ("Emergency services", "Police, sheriff's deputies, firefighters, paramedics and lifeguards all work Leonida's streets and beaches. See the <a href=\"/wanted-level/\">wanted level guide</a> for how police respond and how to escape them."),
    "Aircraft": ("Helicopters and aircraft", "Helicopters and planes show up across the trailers, from police choppers to seaplanes, private jets and a stunt biplane. Which ones you can fly, buy and store is confirmed from launch day."),
    "Industrial": ("Industrial vehicles", "Construction and industrial vehicles work Leonida's building sites, docks and roads. Whether you can drive them is confirmed from launch day."),
    "Military": ("Military vehicles", "Military vehicles in past GTA games were usually found at army bases or called in at the highest wanted levels. What GTA VI has, and how to get it, is confirmed from launch day."),
    "Bike": ("Motorcycles", "Motorcycles use fuel, just like cars. Where to buy, store and modify each bike is confirmed from launch day."),
    "Off-road": ("Off-roading in Leonida", "Leonida has swamps, back roads, beaches and dirt trails. Off-roaders are among the reported vehicle types, and monster truck racing is a reported activity. Where to buy each one is confirmed from launch day."),
    "Commercial": ("Commercial vehicles", "Trucks, vans and work vehicles fill Leonida's roads and docks. Whether you can store them in a garage, and whether any are tied to jobs or missions, is confirmed from launch day."),
}


def vehicle_cards():
    cats = [c for c in ["Car", "Off-road", "Bike", "Cycle", "Emergency", "Commercial", "Industrial", "Military", "Boat", "Aircraft"] if any(v[2] == c for v in VEHICLE_CARDS)]
    chips = '<button class="chip on" type="button" data-type="">All</button>' + "".join(f'<button class="chip" type="button" data-type="{c}">{PLURAL[c]}</button>' for c in cats)
    cards = "".join(
        f'<a class="wcard" href="/vehicles/{f}/" data-type="{c}"><img src="/img/vehicles/{f}.webp" alt="{e(n)} in GTA VI" width="640" height="360" loading="lazy" decoding="async">'
        f'<div class="wbody"><span class="wtype">{c} · {k}</span><h3>{e(n)}</h3><p>{e(d)}</p>'
        f'<p class="wname">{st} · {credit(f)}</p></div></a>'
        for f, n, c, k, st, d in VEHICLE_CARDS)
    return f"""<div class="db" data-db data-cards>
  <div class="dbbar"><div class="chips">{chips}</div></div>
  <div class="wcards">{cards}</div>
  <p class="note">{len(VEHICLE_CARDS)} vehicles seen so far. Cars and bikes are coming next. Official names, stats and prices come from launch day.</p></div>"""


def vehicle_pages():
    out = []
    for f, n, c, k, st, d in VEHICLE_CARDS:
        same = [v for v in VEHICLE_CARDS if v[3] == k and v[0] != f][:3]
        if len(same) < 3:
            same += [v for v in VEHICLE_CARDS if v[0] != f and v not in same][:3 - len(same)]
        tiles = "".join(f'<a class="tile" href="/vehicles/{v[0]}/"><em>{v[3]}</em><h3>{e(v[1])}</h3></a>' for v in same)
        get = "Ultimate Edition" if f in ("shitzu-squalo", "vapid-ganado", "vapid-dominator-buggy") else "Revealed on launch day"
        stats = "".join(f"<tr><td><b>{x}</b></td><td>From November 19</td></tr>" for x in ["Top speed", "Acceleration", "Handling", "Seats", "Price"])
        extra = ""
        if f in ("shitzu-squalo", "vapid-ganado", "vapid-dominator-buggy"):
            extra = '<h2>How to get it</h2><p>It comes with the Ultimate Edition of GTA VI. See <a href="/editions/">Standard vs Ultimate</a> for the full list of what that edition adds.</p>'
        elif f == "armored-truck":
            extra = '<h2>Robberies</h2><p>Armored trucks appear in robbery scenes in the trailers. See the <a href="/robberies/">robberies guide</a> for how robberies and payouts work.</p>'
        elif st == ON_HULL:
            extra = "<h2>About the name</h2><p>The name is shown on the vehicle itself in Rockstar's footage. We will confirm it in the game on launch day.</p>"
        body = f"""
  <article class="prose">
  <span class="eyebrow">Vehicles · {PLURAL[c]} · {k}</span><h1>{e(n)}</h1>
  <p class="lede">{e(d)}</p>
  <figure class="photo"><img src="/img/vehicles/{f}.webp" alt="{e(n)}" width="640" height="360" loading="eager" decoding="async"><figcaption>{credit(f)}</figcaption></figure>
  <h2>Quick facts</h2>
  <div class="scroll"><table>
    <tr><td><b>Type</b></td><td>{c} · {k}</td></tr>
    <tr><td><b>Name</b></td><td>{st}</td></tr>
    <tr><td><b>How to get it</b></td><td>{get}</td></tr>
    <tr><td><b>Seen in</b></td><td>Rockstar's pre-launch trailers or screenshots</td></tr>
  </table></div>
  {extra}
  <h2>{CAT_TEXT[c][0]}</h2>
  <p>{CAT_TEXT[c][1]}</p>
  <h2>Stats and price</h2>
  <p>Rockstar has not published vehicle stats. We add them from the game on launch day.</p>
  <div class="scroll"><table>{stats}</table></div>
  </article>
  <div class="stack"><h2>More vehicles</h2><div class="tiles">{tiles}</div><p><a class="btn ghost" href="/vehicles/">All vehicles</a></p></div>"""
        out.append((f"/vehicles/{f}/", f"GTA 6 {n}: What We Know" + BRAND,
                    f"The {n} in GTA VI ({k.lower()}): {d} How to get it, and stats from launch day."[:300], body))
    return out


VEHICLES = page("/vehicles/", "Database", "GTA 6 vehicles list",
                "Every vehicle seen in GTA VI's trailers and screenshots so far. Tap any card for more.", "", vehicle_cards() + "<h2>Officially named so far</h2>" + db_table(VEHICLE_ROWS, "vehicles") + PREVIEW_NOTE + """
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



CARRY = {
    "Handgun": "Handguns are the concealed slot. You can carry up to two, hidden on your body, so they do not alarm people around you.",
    "Rifle": "Rifles count as long guns. You can carry two, and they are visible, so walking around with one in view makes people nervous and draws police attention.",
    "Shotgun": "Shotguns count as long guns. You can carry two, and they are visible, so carrying one openly draws attention.",
    "SMG": "It has not been confirmed whether SMGs take a handgun slot or a long-gun slot. Smaller ones may fit the concealed slot. We will confirm this on launch day.",
    "Throwable": "It has not been confirmed how throwables fit the carry limit, or how many you can hold. We will confirm this on launch day.",
    "Other": "It is not confirmed yet how this fits the carry limit. We will confirm this on launch day.",
    "Heavy": "It has not been confirmed how heavy weapons fit the carry limit. Expect them to count as long guns or stay in your vehicle's trunk. We will confirm this on launch day.",
}
EXTRA_NOTE = {
    "hawk-little-morgan": '<h2>How to get it</h2><p>It comes with the Ultimate Edition of GTA VI. See <a href="/editions/">Standard vs Ultimate</a> for everything else that edition adds.</p>',
    "nipper-38": "<h2>About the name</h2><p>\"Nipper38\" is engraved on the gun in Rockstar's official artwork. Artwork names do not always match the game, so we will confirm it in the weapon menu on launch day.</p>",
    "gold-compact-rifle": "<h2>Custom finishes</h2><p>The gold plating and white grips point to weapon finishes you can apply or buy. Whether this is a separate gun or a skin for a standard rifle will be clear on launch day.</p>",
    "neon-pistol": "<h2>Custom finishes</h2><p>The bright green finish points to weapon colours you can choose. Whether it is its own gun or a skin will be clear on launch day.</p>",
    "rifle-wall": "<h2>Where to buy guns</h2><p>Ammu-Nation sells weapons, and some branches stock guns unique to their region. Dropped weapons can be collected again from any Ammu-Nation locker.</p>",
}


def weapon_pages():
    out = []
    for f, n, t, named, d in WEAPON_CARDS:
        same = [c for c in WEAPON_CARDS if c[2] == t and c[0] != f][:3] or [c for c in WEAPON_CARDS if c[0] != f][:3]
        tiles = "".join(f'<a class="tile" href="/weapons/{c[0]}/"><em>{c[2]}</em><h3>{e(c[1])}</h3></a>' for c in same)
        get = "Ultimate Edition" if f == "hawk-little-morgan" else "Revealed on launch day"
        stats = "".join(f"<tr><td><b>{k}</b></td><td>From November 19</td></tr>" for k in ["Damage", "Fire rate", "Range", "Accuracy", "Magazine", "Price"])
        body = f"""
  <article class="prose">
  <span class="eyebrow">Weapons · {t}</span><h1>{e(n)}</h1>
  <p class="lede">{e(d)}</p>
  <figure class="photo"><img src="/img/weapons/{f}.webp" alt="{e(n)}" width="640" height="360" loading="eager" decoding="async"><figcaption>{credit(f)}</figcaption></figure>
  <h2>Quick facts</h2>
  <div class="scroll"><table>
    <tr><td><b>Type</b></td><td>{t}</td></tr>
    <tr><td><b>Name</b></td><td>{"Official" if named else "Descriptive. Rockstar has not revealed the in-game name yet"}</td></tr>
    <tr><td><b>How to get it</b></td><td>{get}</td></tr>
    <tr><td><b>Seen in</b></td><td>Rockstar's pre-launch trailers, screenshots or artwork</td></tr>
  </table></div>
  {EXTRA_NOTE.get(f, "")}
  <h2>Carrying it</h2>
  <p>{CARRY[t]} Anything you cannot carry goes in your vehicle's trunk.</p>
  <h2>Stats and price</h2>
  <p>Rockstar has not published weapon stats. We add them from the in-game weapon screen on launch day.</p>
  <div class="scroll"><table>{stats}</table></div>
  </article>
  <div class="stack"><h2>More weapons</h2><div class="tiles">{tiles}</div><p><a class="btn ghost" href="/weapons/">All weapons</a></p></div>"""
        title = f"GTA 6 {n}: What We Know" + BRAND
        desc = f"The {n.lower()} in GTA VI: {d} Carry rules, how to get it, and stats from launch day."[:300]
        out.append((f"/weapons/{f}/", title, desc, body))
    return out

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
EXTRA += weapon_pages()
EXTRA += vehicle_pages()
