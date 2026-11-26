"""How-to pages: fast travel, switching characters, Criminal Profile, stats,
registering cars, making money. Written in our own words from launch-week
guides (PowerPyx, GTABase, KeenGamer, VGC, Dot Esports and others)."""
from articles2 import page, BRAND

FAST_TRAVEL = page("/fast-travel/", "How to", "How to fast travel in GTA 6",
    "There's no map-menu teleport in GTA VI. You fast travel by calling a Paradise Taxi or booking a RydeMe ride on your phone, then paying <b>$100</b> to skip the journey.", "", """
  <div class="facts">
    <div><span>Skip fee</span><b>$100</b></div>
    <div><span>Taxi</span><b>After Gone Fishing</b></div>
    <div><span>RydeMe</span><b>After Buck Me</b></div>
  </div>
  <h2>Paradise Taxi (from the start)</h2>
  <p>Taxis are available once you finish the first Jason mission, Gone Fishing.</p>
  <ol>
    <li>Set a destination marker on the map. It works even on areas you haven't discovered.</li>
    <li>Press <b>Up</b> on the D-pad for the phone, go to <b>Contacts</b> and call <b>Paradise Taxi</b>. The cab shows as a white car on the minimap.</li>
    <li>Get in and hold <b>L2 / LT</b> to talk to the driver.</li>
    <li>Press <b>Triangle / Y</b> to pay $100 and skip the ride.</li>
  </ol>
  <p>Taxis take the cash you're carrying. You can also just ride along for the normal fare.</p>
  <h2>RydeMe (after Buck Me)</h2>
  <p>RydeMe is the rideshare app. It needs a bank account, so it arrives with the Buck Me mission in Chapter 1 (a few guides say Chapter 2; either way it's early). It charges your BuckMe balance, not your cash.</p>
  <ol>
    <li>Set a destination on the map.</li>
    <li>Open <b>RydeMe</b> on your phone and book the ride. Longer trips cost more.</li>
    <li>Get in when the driver arrives and press <b>Triangle / Y</b> to pay $100 and skip.</li>
  </ol>
  <p>If no RydeMe driver is free, call Paradise Taxi instead.</p>
  <h2>Tips</h2>
  <ul>
    <li><b>Fast travel, then call your car.</b> Skip across the map, then use the Scooter Bros app to have your own car delivered. See <a href="/register-cars/">how to register and call your car</a>.</li>
    <li><b>Switching characters</b> can move you across the map for free, if your partner is already where you want to be. See <a href="/switch-characters/">how to switch</a>.</li>
    <li>GTA+ members get premium RydeMe membership.</li>
  </ul>""")

SWITCH = page("/switch-characters/", "How to", "How to switch between Jason and Lucia",
    "Hold <b>Right</b> on the D-pad and press <b>R1 / RB</b>. Free switching unlocks near the end of Chapter 2; until then the story picks who you play.", "", """
  <div class="facts">
    <div><span>Switch</span><b>Hold Right + R1/RB</b></div>
    <div><span>Call partner</span><b>Hold Right + △/Y</b></div>
    <div><span>Unlocks</span><b>Chapter 2</b></div>
  </div>
  <h2>The buttons</h2>
  <ul>
    <li><b>Switch:</b> hold D-pad Right to open the partner menu, then press <b>R1</b> (PS5) or <b>RB</b> (Xbox).</li>
    <li><b>Bring your partner to you:</b> hold D-pad Right and press <b>Triangle / Y</b>. They drive over to you.</li>
    <li><b>Hold, don't tap.</b> A quick tap of Right sets off explosives you've placed.</li>
  </ul>
  <p>The partner menu works on foot, in cars, on boats and in aircraft. It also shows Jason and Lucia's relationship.</p>
  <h2>When can you switch?</h2>
  <p>Not at first. You play Jason through Chapter 1, with Lucia only in short story sections. Free switching opens near the end of Chapter 2: <a href="/walkthrough/breakfast-run/">Breakfast Run</a> teaches it and <a href="/walkthrough/coffee-break/">Coffee Break</a>, which follows straight on, opens it up in free roam. Guides name one or the other, so finish both.</p>
  <h2>Together or apart</h2>
  <ul>
    <li><b>Together:</b> the swap is instant. In a car it moves you between the driver's and passenger seats.</li>
    <li><b>Apart:</b> the camera pulls up over the map and drops down to the other character.</li>
    <li><b>Free chauffeur:</b> set a waypoint, switch to the passenger seat, and your partner drives you there.</li>
  </ul>
  <h2>Why can't I switch?</h2>
  <ol>
    <li><b>You're not far enough in.</b> Finish Breakfast Run and Coffee Break.</li>
    <li><b>The mission is locked to one character.</b> Some story and side missions are Jason-only or Lucia-only; the game says so before they start. From <a href="/walkthrough/making-gainz/">Making Gainz</a> until VCIA Takedown, the pair also can't be seen together in public.</li>
    <li><b>Your partner is busy.</b> A greyed-out portrait means they're doing something, such as riding in a RydeMe. Wait a moment and try again.</li>
    <li><b>You tapped instead of held</b> D-pad Right.</li>
  </ol>
  <p>You can't finish the story as just one of them: both have required missions. See the <a href="/walkthrough/">walkthrough</a> for who plays each one.</p>""")

PROFILE = page("/criminal-profile/", "How to", "GTA 6 Criminal Profile explained",
    "Your Criminal Profile rates how you commit crimes, from <b>Professional</b> to <b>Irredeemable</b>. Jason and Lucia each have their own. It mostly changes how you earn Focus, but the bottom two levels change how police treat you, and the last one is permanent.", "", """
  <h2>The five levels</h2>
  <div class="panel" style="max-width:66ch;margin:10px 0"><h3 style="margin:0 0 6px">Professional</h3><p style="margin:0 0 6px">Stealth, no violence, clean getaways. Threaten staff without hurting them, disable alarms, destroy CCTV tapes.</p><p class="note" style="margin:0"><b>Focus:</b> Stealth takedowns · <b>Police:</b> Normal</p></div><div class="panel" style="max-width:66ch;margin:10px 0"><h3 style="margin:0 0 6px">Hardened</h3><p style="margin:0 0 6px">Putting enemies down without killing them: shots to the legs or shoulders (you'll see a yellow hitmarker).</p><p class="note" style="margin:0"><b>Focus:</b> Stealth takedowns · <b>Police:</b> Normal</p></div><div class="panel" style="max-width:66ch;margin:10px 0"><h3 style="margin:0 0 6px">Violent</h3><p style="margin:0 0 6px">Killing enemies, headshots, finishing off downed enemies, killing civilians or police.</p><p class="note" style="margin:0"><b>Focus:</b> Headshots · <b>Police:</b> Normal</p></div><div class="panel" style="max-width:66ch;margin:10px 0"><h3 style="margin:0 0 6px">Psycho</h3><p style="margin:0 0 6px">Killing sprees, killing pets, lots of dead cops and civilians, driving over gravestones.</p><p class="note" style="margin:0"><b>Focus:</b> Headshots · <b>Police:</b> May shoot on sight, and you can't surrender</p></div><div class="panel" style="max-width:66ch;margin:10px 0"><h3 style="margin:0 0 6px">Irredeemable</h3><p style="margin:0 0 6px">Staying Psycho for a long time with no non-violent actions.</p><p class="note" style="margin:0"><b>Focus:</b> No passive way · <b>Police:</b> Shoot on sight, and you can't surrender. Permanent.</p></div>
  <h2>Can you change it back?</h2>
  <p>Yes, for the first four. Playing quietly and non-lethally moves you back toward Professional. <b>Irredeemable is permanent</b> for that character, so if you go on rampages, mix in some calm play before it locks.</p>
  <p>Why it exists: Rockstar's Rob Nelson calls it GTA VI's take on Red Dead Redemption 2's honour system, built so people react to how you play. <a href="/news/gta-6-rockstar-explains-no-mission-replay-criminal-profile/">What Rockstar said</a>.</p>
  <h2>How to check it</h2>
  <ul>
    <li>Open the map, press <b>L1 / LB</b> to reach the <b>Jason &amp; Lucia</b> tab and pick a character. The rating is at the top.</li>
    <li>While playing, hold D-pad Right to show the icon in the bottom-right corner.</li>
  </ul>
  <h2>Easy ways to stay Professional</h2>
  <ul>
    <li>In robberies, threaten rather than shoot, and knock guns out of guards' hands. Missions like <a href="/walkthrough/credit-check/">Credit Check</a> and <a href="/walkthrough/first-impressions/">First Impressions</a> reward this with a Professional bonus.</li>
    <li>Leave dogs alone. Hurting them pushes you toward Psycho fast.</li>
    <li>Shoot tires and engines in chases, not drivers.</li>
  </ul>
  <p class="note">Before launch, previews named the levels Professional, Aggressive, Violent, Psycho and \"Shattered\". The released game uses the five names above.</p>""")

STATS = page("/stats/", "How to", "How to train Strength, Cardio and Focus in GTA 6",
    "Jason and Lucia each have three stats. <b>Strength</b> raises max health, <b>Cardio</b> raises stamina, and <b>Focus</b> lengthens slow-motion aiming. You raise them by doing things, not by spending points.", "", """
  <div class="facts">
    <div><span>Strength</span><b>Max health</b></div>
    <div><span>Cardio</span><b>Stamina</b></div>
    <div><span>Focus</span><b>Slow-mo aiming</b></div>
  </div>
  <h2>Strength</h2>
  <ul>
    <li>Lift weights. In Chapter 1 there are free weights on the terrace of Jason's house.</li>
    <li>Gyms (fitness studios) have more equipment for a membership fee.</li>
    <li>Finish every workout. If you stop partway, the gains don't count.</li>
    <li>Strength goes up after training on three days in a row. See the <a href="/gym/">gym guide</a>.</li>
  </ul>
  <h2>Cardio</h2>
  <ul>
    <li>Treadmills and exercise bikes at gyms are the quickest.</li>
    <li>Running, cycling and swimming in the open world count too, for free.</li>
    <li>Early on, there's a heavy bag in the shed under Jason's house that you can set up for cardio.</li>
  </ul>
  <h2>Focus</h2>
  <ul>
    <li><b>Fastest:</b> at Rodgers Ranch &amp; Shooting Range (northeast edge of Port Gellhorn, Kelly County), buy the $5 waiver and play the <b>Market Range Beginner</b> challenge. It takes about five seconds and raises Focus each time; quit and restart to repeat.</li>
    <li>Golf, pool and fishing also raise it.</li>
    <li>Your <a href="/criminal-profile/">Criminal Profile</a> decides which combat actions build Focus: stealth takedowns if you're Professional or Hardened, headshots if you're Violent or worse.</li>
  </ul>
  <h2>Tips</h2>
  <ul>
    <li>Have a protein shake or bar after working out to recover faster.</li>
    <li>Train together: once both can use a gym, one character's workout finishes automatically while you train the other.</li>
    <li>Strength and Cardio can slip if you stop training for a long time. Focus doesn't drop.</li>
    <li>Check your stats in the <b>Jason &amp; Lucia</b> menu, or the Fitness app on your phone.</li>
  </ul>""")

CARS = page("/register-cars/", "How to", "How to register, store and call your car in GTA 6",
    "A stolen car disappears once you leave it. To keep one, register it as a personal vehicle: Moses does tracker-free cars from Chapter 2, and Pay 'N' Spray does cars with standard trackers from Chapter 3. Then the Scooter Bros app delivers it wherever you are.", "", """
  <div class="facts">
    <div><span>No tracker</span><b>Moses, Ch. 2</b></div>
    <div><span>Standard tracker</span><b>Pay 'N' Spray, Ch. 3</b></div>
    <div><span>First registration</span><b>Free</b></div>
  </div>
  <h2>Which cars can you register?</h2>
  <p>Scan a car with the WAiNK app (hold D-pad Up, then <b>R1 / RB</b>) to see its tracker and value.</p>
  <div class="scroll"><table>
    <tr><th>Tracker</th><th>Where to register</th><th>When</th></tr>
    <tr><td>None</td><td>Moses's garage, Port Gellhorn</td><td>Chapter 2, from the <a href="/walkthrough/moses/">Moses</a> mission</td></tr>
    <tr><td>Standard</td><td>Any Pay 'N' Spray</td><td>Early Chapter 3 (after <a href="/walkthrough/welcome-to-vice-city/">Welcome to Vice City</a>)</td></tr>
    <tr><td>Advanced</td><td>Through Randy's services</td><td>Later in the story</td></tr>
  </table></div>
  <h2>How to register a car</h2>
  <ol>
    <li>Scan it with WAiNK to check the tracker.</li>
    <li>Steal it. The Slim Jim from Moses opens most cars quietly.</li>
    <li><b>Moses:</b> drive into his garage, respray it, then choose <b>Register</b>. He won't take cars stolen right next to his garage, so bring one from further away.</li>
    <li><b>Pay 'N' Spray:</b> lose any police first, drive in, choose <b>Register</b> and pay.</li>
  </ol>
  <p>The first registration, during the Moses mission, is free. After that the fee depends on the car's value; some sports cars cost over $20,000.</p>
  <h2>Garage space</h2>
  <ul>
    <li>Each registered car takes a slot, and you start with few. Sell one or buy a garage when you're full.</li>
    <li>Buy garages in the <b>Vice City Real Estate</b> app, which unlocks in Chapter 2.</li>
    <li>Parking a stolen car in a garage stores it but doesn't register it.</li>
  </ul>
  <h2>Calling your car</h2>
  <ul>
    <li><b>Chapter 1:</b> call Joey from Coastal Auto Care and he brings Jason's truck to you.</li>
    <li><b>From Chapter 2:</b> open the <b>Scooter Bros</b> app, pick a registered car and confirm. It's delivered to the nearest road for a fee.</li>
    <li><b>Destroyed or impounded?</b> Scooter Bros can recover registered cars for a higher fee. Unregistered cars are gone for good.</li>
  </ul>
  <p>Would rather sell? Moses, Pay 'N' Spray and Randy buy stolen cars, which also counts toward the \"Vehicles fenced\" line on the <a href="/100-percent/">100% list</a>. See <a href="/make-money/">how to make money</a>.</p>""")

MONEY = page("/make-money/", "How to", "How to make money in GTA 6",
    "Money is tight early, and the story asks you to save it (you need $15,000 before leaving Chapter 2). Here are the best ways to earn at each stage, and how not to lose what you've got.", "", """
  <h2>Keep it safe first</h2>
  <p>Cash on you is lost if you're arrested or die, and the story takes it from you at <a href="/walkthrough/tourist-trap/">Tourist Trap</a>. Move money into BuckMe savings as soon as you have an account (from the <a href="/walkthrough/buck-me/">Buck Me</a> mission).</p>
  <h2>Chapter 1</h2>
  <ul>
    <li><b>Story missions.</b> Payment lands in the mailbox outside Jason's house.</li>
    <li><b>Stick-ups.</b> Rob convenience, fast food and liquor store registers. Small money, light police response. Some have a back-room safe: kick the door, make the clerk open it, or look for the code on a sticky note.</li>
    <li><b>Drugs.</b> Sell what you find to Brian at his lock-up and, after <a href="/walkthrough/clean-up-after-donnie/">Clean Up After Donnie</a>, at Donnie's trailer. Cocaine and crystal pay far more than weed.</li>
    <li><b>Treasure.</b> Sell gold doubloons from shipwrecks to Kenton (from <a href="/walkthrough/island-dreams/">Island Dreams</a>).</li>
  </ul>
  <h2>Chapter 2</h2>
  <ul>
    <li><b>Sell cars to Moses.</b> About $1,000 to $5,000 each, tracker-free only. He has a cooldown after each sale; sleeping at your safehouse resets it.</li>
    <li><b>Moses's special car jobs</b> (from <a href="/walkthrough/daily-driver/">Daily Driver</a>).</li>
    <li><b>The four Coffee Break jobs</b>, including Hit Avery Pawn and Hit Kingpin Bowling.</li>
    <li><b>Pawn shops and jewelry stores.</b> Better money, tougher security. Go in the back to cut the alarm and destroy the CCTV tape.</li>
  </ul>
  <h2>Chapter 3 and later</h2>
  <ul>
    <li><b>Gang hideouts.</b> A yellow icon appears when you're near one; check the map for what's inside first. One of the best earners.</li>
    <li><b>Randy's supercars.</b> The first one pays <b>$21,250</b>, plus $10,000 if it's undamaged. Then work through his wish list. See <a href="/walkthrough/steal-the-zorrusso-for-randy/">Steal the Zorrusso</a>.</li>
    <li><b>Banks and payday loan stores</b>, once you have the Dye Pack Jammer from <a href="/walkthrough/credit-check/">Credit Check</a>. The biggest regular payouts, and the fastest police response, so plan your escape.</li>
    <li><b>Yasmani</b> (from <a href="/walkthrough/boobie-time/">Boobie Time</a>) pays the most for jewelry and marked bills.</li>
    <li><b>Bank vaults</b> open late in Chapter 4 and are the largest scores in free roam.</li>
  </ul>
  <h2>Big story paydays</h2>
  <div class="scroll"><table>
    <tr><th>Mission</th><th>Pays</th></tr>
    <tr><td><a href="/walkthrough/afternoon-delight/">Afternoon Delight</a></td><td class="n">$10,000</td></tr>
    <tr><td><a href="/walkthrough/steal-the-zorrusso-for-randy/">Steal the Zorrusso</a></td><td class="n">$21,250 + $10,000</td></tr>
    <tr><td><a href="/walkthrough/childs-play/">Child's Play</a></td><td class="n">$30,000</td></tr>
    <tr><td><a href="/walkthrough/the-cartel-heist/">The Cartel Heist</a></td><td class="n">$120,000</td></tr>
  </table></div>
  <p>Robbing and fencing also fill eleven lines of the <a href="/100-percent/">100% checklist</a>. See the <a href="/robberies/">robbery guide</a> for how robberies work.</p>""")

PAGES = [
    ("/fast-travel/", "How to Fast Travel in GTA 6: Taxi, RydeMe and the $100 Skip" + BRAND,
     "GTA 6 has no map teleport. Call Paradise Taxi or book RydeMe, then pay $100 to skip the ride. When each unlocks and how to use them.", FAST_TRAVEL),
    ("/switch-characters/", "How to Switch Between Jason and Lucia in GTA 6" + BRAND,
     "Hold D-pad Right and press R1/RB to switch. When free switching unlocks in Chapter 2, how swaps work, and why switching sometimes won't work.", SWITCH),
    ("/criminal-profile/", "GTA 6 Criminal Profile Explained: All 5 Levels" + BRAND,
     "Professional, Hardened, Violent, Psycho and Irredeemable: what pushes you to each, how they change Focus and police, and how to change yours back.", PROFILE),
    ("/stats/", "How to Increase Strength, Cardio and Focus in GTA 6" + BRAND,
     "How to train GTA 6's three stats, including the five-second shooting range trick for Focus and free workout spots.", STATS),
    ("/register-cars/", "How to Register, Store and Call Your Car in GTA 6" + BRAND,
     "Register stolen cars with Moses or at Pay 'N' Spray, buy garage space, and call your car with Scooter Bros. Trackers and costs explained.", CARS),
    ("/make-money/", "How to Make Money in GTA 6: Best Methods by Chapter" + BRAND,
     "The best ways to make money in GTA 6 at each stage of the story, the biggest mission payouts, and how to keep your cash safe.", MONEY),
]
