"""How-to pages, batch 2: BuckMe, saving, fences, Ammu-Nation, map fog,
beginner tips. Written in our own words from launch-week guides (PowerPyx,
AlcastHQ, KeenGamer, MetaForge, Beebom, VGC, eGamers and others)."""
from articles2 import page, BRAND


def cards(rows):
    return "".join(f'<div class="panel" style="max-width:66ch;margin:10px 0"><h3 style="margin:0 0 6px">{t}</h3>{body}</div>' for t, body in rows)


BUCKME = page("/buckme/", "How to", "GTA 6 BuckMe and Family Savings explained",
    "BuckMe is the phone bank. Cash on you is easy to lose, your <b>checking</b> account is safer, and <b>Family Savings</b> can never be lost, or taken back out. Hitting savings goals raises your checking limit and unlocks discounts.", "", """
  <h2>Your three kinds of money</h2>
  """ + cards([
      ("Cash on you", "<p style='margin:0'>Used for small buys under $1,000. <b>Lost if you die or get arrested.</b> Deposit it at an ATM (the BuckMe app has an ATM finder).</p>"),
      ("Checking account", "<p style='margin:0'>Pays for anything over $1,000 and for RydeMe. Mostly safe, but dying can still cost you part of it. It has a limit: once full, new payments wait as pending until you spend or save some.</p>"),
      ("Family Savings", "<p style='margin:0'>Shared by Jason and Lucia. Move money in with <b>Buck Yourself</b> in the app, from anywhere. <b>It can never be lost, and never withdrawn or spent.</b> It exists to hit the goals below.</p>"),
  ]) + """
  <h2>Family Savings goals</h2>
  <div class="scroll"><table>
    <tr><th>Saved</th><th>Checking limit</th><th>Perk</th></tr>
    <tr><td class="n">$5,000</td><td class="n">$15,000</td><td>None</td></tr>
    <tr><td class="n">$10,000</td><td class="n">$100,000</td><td>20% off RydeMe</td></tr>
    <tr><td class="n">$100,000</td><td class="n">$500,000</td><td>20% off garages</td></tr>
    <tr><td class="n">$500,000</td><td class="n">$2,000,000</td><td>10% off liveries</td></tr>
    <tr><td class="n">$1,000,000</td><td class="n">$2,000,000</td><td>None</td></tr>
  </table></div>
  <p>New goals only appear as the story moves on. You get the $2,000,000 BuckMe Black (Premium) account automatically at the start of Chapter 4 whatever you've saved (see <a href="/walkthrough/another-life/">Another Life</a>).</p>
  <p class="note">Goal figures come from PowerPyx's walkthrough and match other launch-week guides. Check your app if anything differs.</p>
  <h2>Before you have a bank account</h2>
  <p>BuckMe arrives with the <a href="/walkthrough/buck-me/">Buck Me</a> mission in Chapter 1, where you get $100 and move it into savings as a tutorial. Until then, hide cash under the floorboards in Jason's bedroom.</p>
  <h2>Tips</h2>
  <ul>
    <li><b>Deposit before anything risky:</b> robberies, chases, big missions.</li>
    <li><b>Hit $5,000 in savings before <a href="/walkthrough/tourist-trap/">Tourist Trap</a></b>, the first point of no return. The cash you're carrying is lost there.</li>
    <li>Only put in what you won't need. There's no undo.</li>
    <li>Loot bags aren't money yet. Take them to a <a href="/fences/">fence</a> before you get caught.</li>
  </ul>""")

SAVE = page("/how-to-save/", "How to", "How to save in GTA 6",
    "Pause, go to <b>Game</b>, choose <b>Save Game</b> and pick a slot. You get <b>15 manual slots</b> and one autosave. You can't save during a mission.", "", """
  <div class="facts">
    <div><span>Manual slots</span><b>15</b></div>
    <div><span>Autosave</span><b>1 slot</b></div>
    <div><span>During missions</span><b>No</b></div>
  </div>
  <h2>How to save manually</h2>
  <ol>
    <li>Press <b>Options</b> (PS5) or <b>Menu</b> (Xbox).</li>
    <li>Go to <b>Game</b> and choose <b>Save Game</b>.</li>
    <li>Pick an empty slot or overwrite an old one.</li>
  </ol>
  <p>You can save anywhere in free roam. If Save Game is greyed out, you're in a mission (or the opening prologue): finish it first.</p>
  <h2>How autosave works</h2>
  <ul>
    <li>There's one autosave slot, and each autosave replaces the last.</li>
    <li>It's separate from your 15 manual slots, so it never overwrites them.</li>
    <li><b>Watch out:</b> loading an older manual save replaces your autosave. Make a manual save of where you are now before you load an older one.</li>
  </ul>
  <h2>When to save</h2>
  <p>There's no mission replay, so manual saves are the only way back. Save before:</p>
  <ul>
    <li><a href="/walkthrough/tourist-trap/">Tourist Trap</a> and <a href="/walkthrough/checking-out/">Checking Out</a>, the two points of no return.</li>
    <li>Choices you might want to redo, like <a href="/walkthrough/dubious-provenance/">Dubious Provenance</a> or <a href="/walkthrough/making-gainz/">Making Gainz</a>.</li>
    <li><a href="/walkthrough/the-cartel-heist/">The Cartel Heist</a> and the final mission.</li>
    <li>Big deposits into Family Savings, which can't be undone.</li>
    <li>Trying cheats. Using one blocks saving for the rest of that session.</li>
  </ul>
  <p><b>A simple plan:</b> keep one slot at the start of each chapter (five), and rotate the rest after each mission so you always have a recent fallback.</p>""")

FENCES = page("/fences/", "How to", "GTA 6 fence locations: where to sell stolen goods",
    "Narcotics, jewelry and marked bills are worth nothing until a fence buys them. The best are in Vice City from Chapter 3: <b>Tyrone</b> for narcotics, <b>Yasmani</b> for jewelry and marked bills.", "", """
  <h2>Who pays best</h2>
  <div class="scroll"><table>
    <tr><th>Selling</th><th>Chapters 1-2</th><th>Chapter 3 on</th></tr>
    <tr><td>Narcotics</td><td>Donnie or Dunk (low)</td><td><b>Tyrone</b> (high)</td></tr>
    <tr><td>Jewelry</td><td>Dunk (low)</td><td><b>Yasmani</b> (high)</td></tr>
    <tr><td>Marked bills</td><td>Everyone very low</td><td><b>Yasmani</b> (high)</td></tr>
  </table></div>
  <h2>Every fence</h2>
  """ + cards([
      ("Brian, south Key Lento", "<p style='margin:0 0 6px'>From <a href='/walkthrough/lab-fees/'>Lab Fees</a>. Gone after Chapter 1.</p><p class='note' style='margin:0'>Narcotics very low · Jewelry very low · Bills very low</p>"),
      ("Donnie, south Key Lento", "<p style='margin:0 0 6px'>From <a href='/walkthrough/clean-up-after-donnie/'>Clean Up After Donnie</a>. Gone after <a href='/walkthrough/swamped/'>Swamped</a>.</p><p class='note' style='margin:0'>Narcotics low · Jewelry very low · Bills very low</p>"),
      ("Dunk, Port Gellhorn", "<p style='margin:0 0 6px'>From <a href='/walkthrough/slam-dunk/'>Slam Dunk</a>. Away for part of the story, then back.</p><p class='note' style='margin:0'>Narcotics low · Jewelry low · Bills very low</p>"),
      ("Tyrone, La Perle (Vice City)", "<p style='margin:0 0 6px'>Chapter 3 on. Best for narcotics.</p><p class='note' style='margin:0'>Narcotics high · Jewelry medium · Bills medium</p>"),
      ("Yasmani, Little Cuba (Vice City)", "<p style='margin:0 0 6px'>From <a href='/walkthrough/boobie-time/'>Boobie Time</a>. Best for jewelry and marked bills.</p><p class='note' style='margin:0'>Narcotics medium · Jewelry high · Bills high</p>"),
  ]) + """
  <h2>Car buyers</h2>
  <ul>
    <li><b>Moses</b>, Port Gellhorn: tracker-free cars, from Chapter 2.</li>
    <li><b>Pay 'N' Spray</b>: also buys stolen cars.</li>
    <li><b>Randy</b>, Balsero (Vice City): high-end cars, including ones with advanced trackers, from <a href='/walkthrough/steal-the-zorrusso-for-randy/'>Steal the Zorrusso</a>.</li>
  </ul>
  <p>See <a href="/register-cars/">how to register cars</a> if you'd rather keep one.</p>
  <h2>How fencing works</h2>
  <ul>
    <li>Once you've met a fence, they show on the map as a green icon with their initials. Hover over it to see their rates before you drive over.</li>
    <li>Early in Chapter 1 you're paid in cash, left in the mailbox outside Jason's house. Once you have BuckMe, fences pay into your account.</li>
    <li>From Chapter 3 you can sell from your garage and pick the fence.</li>
    <li>Your partner can fence for you: put the bag in your car's trunk and tell them to <b>Fence Goods</b> (the option doesn't always show).</li>
    <li>Loot bags are lost if you die, so sell big scores straight away.</li>
  </ul>
  <p>Fencing fills four lines of the <a href="/100-percent/">100% list</a>: narcotics and jewelry ($100,000 each), marked bills ($250,000) and vehicles ($200,000).</p>""")

AMMU = page("/ammu-nation/", "How to", "Where to buy body armor, a parachute and launchers in GTA 6",
    "Every Ammu-Nation sells guns, ammo, <b>body armor</b> and <b>parachutes</b>. Rocket and grenade launchers, sniper rifles and LMGs are only at the <b>Expanded</b> stores.", "", """
  <div class="facts">
    <div><span>Ammu-Nations</span><b>24</b></div>
    <div><span>Body armor</span><b>$250</b></div>
    <div><span>Launchers</span><b>Expanded only</b></div>
  </div>
  <h2>Store types</h2>
  <p>Hover over an Ammu-Nation on the map to see its stock level: <b>Limited</b>, <b>Standard</b>, <b>Hunting</b> or <b>Expanded</b>. Expanded stores carry everything. Each store also sells at least one unique weapon variant.</p>
  <h2>Body armor</h2>
  <ul>
    <li>Sold at any Ammu-Nation, about $250.</li>
    <li>It soaks up bullet damage before your health. Once it's used up, buy or find another vest.</li>
  </ul>
  <h2>Parachute</h2>
  <ul>
    <li>Sold at any Ammu-Nation. The first store in Key Lento has them on the back left wall.</li>
    <li>It uses the same slot as body armor. If you're wearing armor, select the parachute in the item wheel and press <b>R2 / RT</b> to swap.</li>
    <li>BASE jump spots also have one waiting for you.</li>
  </ul>
  <h2>Launchers and heavy weapons</h2>
  <div class="scroll"><table>
    <tr><th>Weapon</th><th>Price</th></tr>
    <tr><td>Hillinger Boomer (grenade launcher)</td><td class="n">$12,000</td></tr>
    <tr><td>Deever Tech GLR40 (grenade launcher)</td><td class="n">$15,500</td></tr>
    <tr><td>Hauners H-AT (rocket launcher)</td><td class="n">$16,000</td></tr>
  </table></div>
  <p>Only Expanded Ammu-Nations sell these, along with sniper rifles and LMGs. Woodhatch, Big Shots and Phil's Ammu-Nation are three of them.</p>
  <h2>Good to know</h2>
  <ul>
    <li>Guns you <b>buy</b> come back from the weapon locker at any Ammu-Nation if you die or get arrested. Guns taken from enemies don't, unless they're gold-icon special weapons.</li>
    <li>The Key Lento store sells a suppressor, handy for quiet takedowns.</li>
    <li>Holding each standard weapon once counts toward \"Standard issue weapons found\" on the <a href="/100-percent/">100% list</a> (50 of 66).</li>
  </ul>
  <p>See the <a href="/weapons/">weapons list</a> for everything in the game.</p>""")

FOG = page("/map-fog/", "How to", "How to clear the map fog fast in GTA 6",
    "The map starts hidden. The fastest way to reveal it is to fly a slow crop duster over each fogged area. A quick pass clears it; you don't need to land or circle. Clearing all of it unlocks the <b>The Goodtime State</b> trophy.", "", """
  <div class="facts">
    <div><span>Best plane</span><b>Bottcher Duster</b></div>
    <div><span>From</span><b>Chapter 1</b></div>
    <div><span>Takes</span><b>2-5 hours</b></div>
  </div>
  <h2>How to do it</h2>
  <ol>
    <li>Take a Paradise Taxi to an airstrip (see <a href="/fast-travel/">fast travel</a>). There's one near Key Lento in the south.</li>
    <li>Grab a crop duster: the Bottcher Duster is the pick. It's easy on fuel and doesn't draw military jets the way a fighter jet does.</li>
    <li>Fly over each fogged section once. The map reveals in small segments, so work one region at a time.</li>
    <li>Start in the south and work steadily north to avoid backtracking.</li>
    <li>Refuel or swap planes at the airstrip in Kelly County, in the middle of the map. Crop dusters respawn.</li>
  </ol>
  <h2>Tips</h2>
  <ul>
    <li>Turn on the fuel gauge in the HUD settings. It sits above the minimap. Land when it goes yellow.</li>
    <li>Save manually as you go. Autosaves are rare when you're just exploring.</li>
    <li>Driving reveals fog too, and Auto-Drive counts, if you'd rather relax.</li>
    <li>Guides put a full clear at around 2 to 5 hours, depending on route and fuel stops.</li>
  </ul>
  <p>Fly with WAiNK ready: landmarks you pass count toward the 100 WAiNK scans on the <a href="/100-percent/">100% list</a>.</p>""")

TIPS = page("/beginner-tips/", "How to", "GTA 6 beginner tips: 20 things to know first",
    "GTA VI changes a lot of habits from GTA V. Cash on you can vanish, police aren't on the minimap, and stolen cars don't stay yours. These are the tips that save the most trouble in your first hours.", "", """
  <h2>Money</h2>
  <ol>
    <li><b>Bank your cash.</b> You lose what you carry if you die or get arrested. Hide it under the floorboards in Jason's bedroom until you get BuckMe, then use ATMs. <a href="/buckme/">How BuckMe works</a>.</li>
    <li><b>Visit an ATM before anything risky.</b> It's the only way to deposit.</li>
    <li><b>Fence loot fast.</b> Loot bags are lost on death too. <a href="/fences/">Where to sell</a>.</li>
    <li><b>Don't grind early.</b> Money is tight in Chapter 1 whatever you do. The story unlocks the bank, tools and better jobs.</li>
    <li><b>Search bodies</b> after a fight for cash, ammo and guns.</li>
  </ol>
  <h2>Police</h2>
  <ol start="6">
    <li><b>Cops aren't on your minimap.</b> They find you through witnesses and cameras.</li>
    <li><b>Change your look to lose them.</b> Swap your car, outfit, hat or glasses. Keep a spare outfit in the trunk.</li>
    <li><b>A Pay 'N' Spray respray</b> stops police recognizing a known car.</li>
    <li><b>Commit crimes at night</b>, when fewer people are around to call it in. See the <a href="/wanted-level/">wanted level guide</a>.</li>
  </ol>
  <h2>Cars</h2>
  <ol start="10">
    <li><b>Scan before you steal.</b> WAiNK (hold D-pad Up, then R1/RB) shows alarms and trackers.</li>
    <li><b>Stolen cars aren't yours</b> until you register them, from Chapter 2. <a href="/register-cars/">How to register</a>.</li>
    <li><b>Watch your fuel.</b> Cars, planes and helicopters run dry. Gas stations also fix small damage cheaply.</li>
  </ol>
  <h2>Combat</h2>
  <ol start="13">
    <li><b>Use Focus.</b> Press both sticks to slow time and highlight enemies, loot, safe codes and alarmed doors. <a href="/stats/">How to raise it</a>.</li>
    <li><b>Buy your guns.</b> Bought guns come back from any Ammu-Nation's locker after death or arrest; picked-up ones don't. <a href="/ammu-nation/">What to buy where</a>.</li>
    <li><b>A yellow hitmarker means they're alive.</b> Shoot limbs to keep your <a href="/criminal-profile/">Criminal Profile</a> clean. The worst level, Irredeemable, is permanent.</li>
    <li><b>Get a suppressor</b> from the Key Lento Ammu-Nation for quiet takedowns.</li>
  </ol>
  <h2>Progress</h2>
  <ol start="17">
    <li><b>Save manually, often.</b> There's one autosave and no mission replay. <a href="/how-to-save/">How saving works</a>.</li>
    <li><b>Know the points of no return:</b> <a href="/walkthrough/tourist-trap/">Tourist Trap</a> and <a href="/walkthrough/checking-out/">Checking Out</a>.</li>
    <li><b>Scan and study as you go.</b> Vehicle scans, animal studies and WAiNK landmarks all count toward the <a href="/100-percent/">100% list</a>, and nothing on it is missable.</li>
    <li><b>Wait to rob banks</b> until you have the Dye Pack Jammer from <a href="/walkthrough/credit-check/">Credit Check</a>, or dye packs ruin the cash.</li>
  </ol>
  <p>Stuck on a mission? Every documented mission has a step-by-step page in the <a href="/walkthrough/">walkthrough</a>.</p>""")

PAGES = [
    ("/buckme/", "GTA 6 BuckMe and Family Savings Explained: Goals and Perks" + BRAND,
     "How GTA 6's BuckMe bank works: cash vs checking vs Family Savings, what you lose when you die, and every savings goal with its checking limit and perk.", BUCKME),
    ("/how-to-save/", "How to Save in GTA 6: Manual Saves and Autosave" + BRAND,
     "Pause > Game > Save Game. GTA 6 has 15 manual slots and one autosave, and you can't save during missions. When to save and the autosave trap to avoid.", SAVE),
    ("/fences/", "GTA 6 Fence Locations: Where to Sell Stolen Goods" + BRAND,
     "Every GTA 6 fence, where they are, when they unlock and what they pay for narcotics, jewelry and marked bills. Tyrone and Yasmani pay the most.", FENCES),
    ("/ammu-nation/", "GTA 6: Where to Buy Body Armor, Parachute and Rocket Launcher" + BRAND,
     "Body armor and parachutes are at every Ammu-Nation; launchers, snipers and LMGs only at Expanded stores. Prices and how to equip them.", AMMU),
    ("/map-fog/", "How to Clear the Map Fog Fast in GTA 6" + BRAND,
     "Fly a Bottcher Duster crop duster over each fogged area to reveal Leonida and unlock The Goodtime State trophy. Airstrips, route and fuel tips.", FOG),
    ("/beginner-tips/", "GTA 6 Beginner Tips: 20 Things to Know Before You Play" + BRAND,
     "20 GTA 6 beginner tips on money, police, cars, combat and saving that save the most trouble in your first hours in Leonida.", TIPS),
]
