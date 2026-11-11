/* Leonida Logbook interactive map: pan, zoom, filters, marker details, visited state. */
(function () {
  var svg = document.getElementById("map"); if (!svg) return;
  var vp = document.getElementById("vp"), info = document.getElementById("mapInfo");
  var data = JSON.parse(document.getElementById("mapData").textContent);
  var KEY = "leonida-logbook-v1", MAXK = 6, s = { x: 0, y: 0, k: 1 }, current = null;
  var byId = {}; data.markers.forEach(function (m) { byId[m.id] = m; });

  function load() { try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; } }
  function save(o) { try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }

  function apply() {
    s.k = Math.max(1, Math.min(MAXK, s.k));
    var min = 1000 - 1000 * s.k;
    s.x = Math.min(0, Math.max(min, s.x)); s.y = Math.min(0, Math.max(min, s.y));
    vp.setAttribute("transform", "translate(" + s.x + " " + s.y + ") scale(" + s.k + ")");
    var inv = "scale(" + (1 / s.k) + ")";
    [].forEach.call(svg.querySelectorAll(".inv"), function (g) { g.setAttribute("transform", inv); });
  }
  function pt(cx, cy) { var p = svg.createSVGPoint(); p.x = cx; p.y = cy; return p.matrixTransform(svg.getScreenCTM().inverse()); }
  function zoomAt(p, f) {
    var k2 = Math.max(1, Math.min(MAXK, s.k * f));
    s.x = p.x - (p.x - s.x) * (k2 / s.k); s.y = p.y - (p.y - s.y) * (k2 / s.k); s.k = k2; apply();
  }

  svg.addEventListener("wheel", function (e) { e.preventDefault(); zoomAt(pt(e.clientX, e.clientY), e.deltaY < 0 ? 1.2 : 1 / 1.2); }, { passive: false });

  var ptrs = {}, moved = false, startX = 0, startY = 0, pinch = 0, downTarget = null;
  function count() { return Object.keys(ptrs).length; }
  svg.addEventListener("pointerdown", function (e) {
    ptrs[e.pointerId] = { x: e.clientX, y: e.clientY };
    if (count() === 1) { moved = false; startX = e.clientX; startY = e.clientY; downTarget = e.target; }
    if (count() === 2) { var a = Object.keys(ptrs).map(function (k) { return ptrs[k]; }); pinch = Math.hypot(a[0].x - a[1].x, a[0].y - a[1].y); moved = true; }
  });
  window.addEventListener("pointermove", function (e) {
    var prev = ptrs[e.pointerId]; if (!prev) return;
    if (count() === 1) {
      if (Math.hypot(e.clientX - startX, e.clientY - startY) > 5) moved = true;
      if (moved) { var a = pt(prev.x, prev.y), b = pt(e.clientX, e.clientY); s.x += b.x - a.x; s.y += b.y - a.y; apply(); }
    }
    ptrs[e.pointerId] = { x: e.clientX, y: e.clientY };
    if (count() === 2) {
      var q = Object.keys(ptrs).map(function (k) { return ptrs[k]; }), d = Math.hypot(q[0].x - q[1].x, q[0].y - q[1].y);
      if (pinch > 0 && d > 0) zoomAt(pt((q[0].x + q[1].x) / 2, (q[0].y + q[1].y) / 2), d / pinch);
      pinch = d;
    }
  });
  function up(e) {
    if (!ptrs[e.pointerId]) return;
    delete ptrs[e.pointerId];
    if (!moved && downTarget && downTarget.closest) { var g = downTarget.closest(".mk"); if (g) select(g.getAttribute("data-id")); }
    if (count() < 2) pinch = 0;
  }
  window.addEventListener("pointerup", up); window.addEventListener("pointercancel", up);
  svg.addEventListener("keydown", function (e) {
    if ((e.key === "Enter" || e.key === " ") && e.target.closest) { var g = e.target.closest(".mk"); if (g) { e.preventDefault(); select(g.getAttribute("data-id")); } }
  });

  function paintDone() {
    var o = load();
    [].forEach.call(svg.querySelectorAll(".mk"), function (g) { g.classList.toggle("done", !!o[byId[g.getAttribute("data-id")].key]); });
  }
  function select(id) {
    var m = byId[id]; if (!m) return; current = id;
    [].forEach.call(svg.querySelectorAll(".mk"), function (g) { g.classList.toggle("on", g.getAttribute("data-id") === id); });
    var done = !!load()[m.key];
    info.innerHTML = "";
    var h = document.createElement("h3"); h.textContent = m.name;
    var c = document.createElement("span"); c.className = "eyebrow"; c.textContent = data.cats[m.cat];
    var p = document.createElement("p"); p.textContent = m.d;
    var b = document.createElement("button"); b.type = "button"; b.className = done ? "btn ghost" : "btn"; b.textContent = done ? "Visited. Tap to undo" : "Mark as visited";
    b.onclick = function () { var o = load(); if (o[m.key]) delete o[m.key]; else o[m.key] = 1; save(o); paintDone(); select(id); };
    var w = document.createElement("div"); w.appendChild(b);
    info.appendChild(c); info.appendChild(h); info.appendChild(p); info.appendChild(w);
  }

  [].forEach.call(document.querySelectorAll("#mapFilters input"), function (cb) {
    cb.addEventListener("change", function () {
      cb.parentNode.classList.toggle("on", cb.checked);
      [].forEach.call(svg.querySelectorAll('.mk[data-cat="' + cb.getAttribute("data-cat") + '"]'), function (g) { g.style.display = cb.checked ? "" : "none"; });
    });
  });
  var mid = { x: 500, y: 500 };
  document.getElementById("zin").onclick = function () { zoomAt(mid, 1.5); };
  document.getElementById("zout").onclick = function () { zoomAt(mid, 1 / 1.5); };
  document.getElementById("zreset").onclick = function () { s = { x: 0, y: 0, k: 1 }; apply(); };

  apply(); paintDone();
})();
