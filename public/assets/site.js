/* Leonida Logbook: countdown, saved checklists and progress bars. Page content is static HTML built by build.py. */
(function () {
  var RELEASE = new Date(2026, 10, 19, 0, 0, 0); // local midnight, Nov 19 2026
  var KEY = "leonida-logbook-v1";
  var $ = function (id) { return document.getElementById(id); };
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { saved = {}; }
  function persist() { try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) {} }

  var boxes = [].slice.call(document.querySelectorAll("input[data-key]"));
  boxes.forEach(function (b) { b.checked = !!saved[b.dataset.key]; });

  function updateProgress() {
    var done = 0, total = 0;
    [].forEach.call(document.querySelectorAll("[data-group]"), function (g) {
      var items = g.querySelectorAll("input[data-key]"), d = 0;
      [].forEach.call(items, function (i) { if (i.checked) d++; });
      var n = g.querySelector(".count"), bar = g.querySelector(".bar i");
      if (n) n.textContent = d + " / " + items.length;
      if (bar) bar.style.width = (items.length ? 100 * d / items.length : 0) + "%";
      if (g.dataset.group !== "prep") { done += d; total += items.length; }
    });
    if ($("totalPct")) {
      var pct = total ? Math.round(100 * done / total) : 0;
      $("totalPct").textContent = pct + "%";
      $("totalBar").style.width = pct + "%";
      $("totalNote").textContent = done + " of " + total + " items ticked. More lists unlock at launch.";
    }
  }
  document.addEventListener("change", function (e) {
    var k = e.target.dataset && e.target.dataset.key; if (!k) return;
    if (e.target.checked) saved[k] = 1; else delete saved[k];
    persist(); updateProgress();
  });
  updateProgress();

  if ($("resetBtn")) {
    var show = function (confirming) { $("resetWrap").hidden = confirming; $("resetConfirm").hidden = !confirming; };
    $("resetBtn").onclick = function () { show(true); };
    $("resetNo").onclick = function () { show(false); };
    $("resetYes").onclick = function () {
      Object.keys(saved).forEach(function (k) { if (k.indexOf("prep-") !== 0) delete saved[k]; });
      persist();
      boxes.forEach(function (b) { if (b.dataset.key.indexOf("prep-") !== 0) b.checked = false; });
      updateProgress(); show(false);
    };
  }

  [].forEach.call(document.querySelectorAll("[data-db]"), function (db) {
    var q = db.querySelector("input[type=search]"), chips = db.querySelectorAll(".chip"), rows = db.querySelectorAll("tr[data-type], .wcard[data-type]"), type = "";
    function run() {
      var t = q ? (q.value || "").toLowerCase() : "", n = 0;
      [].forEach.call(rows, function (r) {
        var ok = (!type || r.getAttribute("data-type") === type) && r.textContent.toLowerCase().indexOf(t) !== -1;
        r.hidden = !ok; if (ok) n++;
      });
      var em = db.querySelector("[data-empty]"); if (em) em.hidden = n > 0;
    }
    if (q) q.addEventListener("input", run);
    [].forEach.call(chips, function (c) { c.addEventListener("click", function () {
      type = c.getAttribute("data-type"); [].forEach.call(chips, function (x) { x.classList.toggle("on", x === c); }); run();
    }); });
  });

  var cheats = document.querySelector(".cheats");
  if (cheats) {
    var segs = document.querySelectorAll(".seg button");
    var setShow = function (v) {
      cheats.setAttribute("data-show", v);
      [].forEach.call(segs, function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-show") === v)); });
      try { localStorage.setItem("leonida-cheat-platform", v); } catch (e) {}
    };
    [].forEach.call(segs, function (b) { b.addEventListener("click", function () { setShow(b.getAttribute("data-show")); }); });
    try { var pv = localStorage.getItem("leonida-cheat-platform"); if (pv) setShow(pv); } catch (e) {}
    document.addEventListener("click", function (ev) {
      var b = ev.target.closest && ev.target.closest("[data-copy]"); if (!b) return;
      var code = b.getAttribute("data-copy");
      var done = function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1500); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(code).then(done, function () { selectCode(b); });
      else selectCode(b);
    });
    var selectCode = function (b) { var c = b.previousElementSibling; var r = document.createRange(); r.selectNodeContents(c); var s = getSelection(); s.removeAllRanges(); s.addRange(r); };
  }

  if ($("clock")) {
    var pad = function (n) { return String(n).padStart(2, "0"); };
    var tick = function () {
      var ms = RELEASE - Date.now();
      if (ms <= 0) {
        $("heroEyebrow").textContent = "Released November 19, 2026";
        $("heroTitle").textContent = "GTA VI is out now";
        $("clock").hidden = true; $("clockNote").hidden = true; return;
      }
      var s = Math.floor(ms / 1000);
      $("cd").textContent = Math.floor(s / 86400); $("ch").textContent = pad(Math.floor(s % 86400 / 3600));
      $("cm").textContent = pad(Math.floor(s % 3600 / 60)); $("cs").textContent = pad(s % 60);
    };
    tick(); setInterval(tick, 1000);
  }
})();

(function () {
  var f = document.querySelector("[data-vfinder]");
  if (!f) return;
  var q = f.querySelector("[data-vq]"), st = f.querySelector("[data-vstatus]"), tiles = f.querySelectorAll(".vtile"),
      cards = f.querySelectorAll(".wcard"), shown = f.querySelector("[data-vshown]"), empty = f.querySelector("[data-vempty]"),
      reset = f.querySelector("[data-vreset]"), on = {};
  function run() {
    var t = (q.value || "").toLowerCase().trim(), s = st.value, any = Object.keys(on).length > 0, n = 0;
    [].forEach.call(cards, function (c) {
      var ok = (!any || on[c.getAttribute("data-class")]) && (!s || c.getAttribute("data-status") === s) &&
               (!t || c.textContent.toLowerCase().indexOf(t) !== -1);
      c.hidden = !ok; if (ok) n++;
    });
    shown.textContent = n; empty.hidden = n > 0; reset.hidden = !(any || t || s);
  }
  [].forEach.call(tiles, function (b) {
    b.addEventListener("click", function () {
      var c = b.getAttribute("data-class");
      if (on[c]) delete on[c]; else on[c] = 1;
      b.setAttribute("aria-pressed", on[c] ? "true" : "false"); run();
    });
  });
  q.addEventListener("input", run); st.addEventListener("change", run);
  reset.addEventListener("click", function () {
    on = {}; q.value = ""; st.value = "";
    [].forEach.call(tiles, function (b) { b.setAttribute("aria-pressed", "false"); }); run();
  });
})();

(function () {
  var box = document.querySelector("[data-unlock]");
  if (!box) return;
  var ZONES = [
    ["New Zealand", "Pacific/Auckland"], ["Sydney, Australia", "Australia/Sydney"], ["Tokyo, Japan", "Asia/Tokyo"],
    ["Singapore", "Asia/Singapore"], ["India", "Asia/Kolkata"], ["Dubai, UAE", "Asia/Dubai"], ["Istanbul, Turkey", "Europe/Istanbul"],
    ["Central Europe", "Europe/Berlin"], ["UK and Ireland", "Europe/London"], ["Brazil (São Paulo)", "America/Sao_Paulo"],
    ["US Eastern", "America/New_York"], ["US Central", "America/Chicago"], ["Mexico City", "America/Mexico_City"],
    ["US Mountain", "America/Denver"], ["US Pacific", "America/Los_Angeles"], ["Alaska", "America/Anchorage"], ["Hawaii", "Pacific/Honolulu"]
  ];
  function offset(tz, t) {
    var p = {}; new Intl.DateTimeFormat("en-US", {timeZone: tz, hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit"})
      .formatToParts(new Date(t)).forEach(function (x) { p[x.type] = x.value; });
    return Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour % 24, +p.minute, +p.second) - t;
  }
  function unlockAt(tz) { var g = Date.UTC(2026, 10, 19); var t = g - offset(tz, g); return g - offset(tz, t); }
  var mine; try { mine = Intl.DateTimeFormat().resolvedOptions().timeZone; } catch (e) {}
  if (!mine) mine = "America/New_York";
  var sel = box.querySelector("[data-uzone]"), list = ZONES.slice();
  if (!list.some(function (z) { return z[1] === mine; })) list.unshift(["Your time zone (" + mine.replace(/_/g, " ") + ")", mine]);
  list.forEach(function (z) { var o = document.createElement("option"); o.value = z[1]; o.textContent = z[0]; if (z[1] === mine) o.selected = true; sel.appendChild(o); });
  function fmt(t, tz, withDay) {
    return new Intl.DateTimeFormat(undefined, {timeZone: tz, weekday: withDay ? "short" : undefined, month: withDay ? "short" : undefined, day: withDay ? "numeric" : undefined, hour: "numeric", minute: "2-digit"}).format(new Date(t));
  }
  var target;
  function table(viewTz) {
    var rows = ZONES.map(function (z) { return [z, unlockAt(z[1])]; }).sort(function (a, b) { return a[1] - b[1]; });
    box.parentNode.querySelector("[data-utable]").innerHTML = rows.map(function (r) {
      var me = r[0][1] === viewTz ? ' class="me"' : "";
      return "<tr" + me + "><td><b>" + r[0][0] + "</b></td><td>Thu Nov 19, 12:00 am</td><td>" + fmt(r[1], viewTz, true) + "</td></tr>";
    }).join("");
  }
  function pick() {
    var tz = sel.value; target = unlockAt(tz);
    box.querySelector("[data-uwhen]").textContent = fmt(target, mine, true) + (tz === mine ? " your time" : " your time (midnight in " + sel.options[sel.selectedIndex].text + ")");
    table(mine); tick();
  }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function tick() {
    var d = Math.max(0, target - Date.now()), s = Math.floor(d / 1000);
    box.querySelector("[data-ud]").textContent = Math.floor(s / 86400);
    box.querySelector("[data-uh]").textContent = pad(Math.floor(s / 3600) % 24);
    box.querySelector("[data-um]").textContent = pad(Math.floor(s / 60) % 60);
    box.querySelector("[data-us]").textContent = pad(s % 60);
    if (d === 0) box.querySelector("[data-unote]").textContent = "It is unlocked in this time zone. Go play.";
  }
  sel.addEventListener("change", pick); pick(); setInterval(tick, 1000);
})();
