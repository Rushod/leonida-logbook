import React, { useEffect, useMemo, useRef, useState, useCallback } from "react";
import { createRoot } from "react-dom/client";
import L from "leaflet";
import "leaflet.markercluster";
import { MapContainer, TileLayer, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet.markercluster/dist/MarkerCluster.css";
import "./map.css";

/* ---------- coordinate system ----------
   Locations use in-game metres (x east, y north). At zoom z the tile world is 1024 * 2^z px wide,
   one metre is 2^z / 32 px, and (0, 0) sits at 512 * 2^z px. lat = y, lng = x. */
const CRS = L.extend({}, L.CRS.Simple, { transformation: new L.Transformation(1 / 32, 512, -1 / 32, 512) });
const ll = (l) => L.latLng(l.y, l.x);
const ISLAND = L.latLngBounds([-8900, -9400], [9300, 2900]);
const LIMITS = L.latLngBounds([-10500, -11000], [11000, 3400]);
const TILE_BOUNDS = L.latLngBounds([-9216, -11008], [11008, 3300]);

/* ---------- categories ---------- */
const ICONS = {
  landmarks: '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.4 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
  stores: '<path d="M6 8h12l-1 12H7zM9 8a3 3 0 016 0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
  activities: '<path d="M13 2L5 13h6l-1 9 8-11h-6z"/>',
  missions: '<circle cx="12" cy="12" r="7" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="12" cy="12" r="2.6"/>',
  collectibles: '<path d="M12 3l7 9-7 9-7-9z"/>',
  vehicles: '<path d="M5 15l1.6-5h10.8L19 15v4h-2.2v-1.6H7.2V19H5zM7.5 14.2a1.2 1.2 0 100-.01M16.5 14.2a1.2 1.2 0 100-.01"/>',
  weapons: '<circle cx="12" cy="12" r="6" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v5M12 16v5M3 12h5M16 12h5" stroke="currentColor" stroke-width="2.2"/>',
};
const CATS = [
  { id: "landmarks", label: "Landmarks", color: "#4fe3e8" },
  { id: "stores", label: "Stores", color: "#ff8f3f" },
  { id: "activities", label: "Activities", color: "#ff4fa3" },
  { id: "missions", label: "Missions", color: "#ffc35a" },
  { id: "collectibles", label: "Collectibles", color: "#b48cff" },
  { id: "vehicles", label: "Vehicles", color: "#5fe6a8" },
  { id: "weapons", label: "Weapons", color: "#ff6a6a" },
];
const CAT = Object.fromEntries(CATS.map((c) => [c.id, c]));
const STATUS = {
  speculative: { label: "Speculative", note: "Mapped by the community before release. Not checked in the game." },
  official: { label: "Official", note: "Named or shown by Rockstar." },
  verified: { label: "Verified", note: "Checked in the released game." },
};

const svg = (cat, size) =>
  `<svg viewBox="0 0 24 24" width="${size}" height="${size}" fill="currentColor" aria-hidden="true">${ICONS[cat]}</svg>`;

const iconCache = {};
function pinIcon(cat, found) {
  const k = cat + (found ? "1" : "0");
  if (!iconCache[k]) {
    iconCache[k] = L.divIcon({
      className: "lm-pin-wrap",
      html: `<span class="lm-pin${found ? " is-found" : ""}" style="--c:${CAT[cat].color}">${svg(cat, 16)}</span>`,
      iconSize: [32, 38],
      iconAnchor: [16, 36],
      popupAnchor: [0, -32],
    });
  }
  return iconCache[k];
}
function clusterIcon(cluster) {
  const n = cluster.getChildCount();
  const size = n < 10 ? 38 : n < 100 ? 46 : 56;
  return L.divIcon({ className: "lm-cluster-wrap", html: `<span class="lm-cluster" style="width:${size}px;height:${size}px">${n}</span>`, iconSize: [size, size] });
}

/* ---------- storage (shared with the site's tracker) ---------- */
const KEY = "leonida-logbook-v1";
const loadFound = () => { try { return JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { return {}; } };
const saveFound = (o) => { try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} };
const fkey = (id) => "map-" + id;

/* ---------- popup ---------- */
function popupHtml(l, found) {
  const esc = (s) => String(s || "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const c = CAT[l.category], st = STATUS[l.status] || STATUS.speculative;
  const nameNote = l.nameKind === "community" ? '<span class="lm-nn">Community nickname</span>' : l.nameKind === "uncertain" ? '<span class="lm-nn">Name not certain</span>' : "";
  const img = l.image && l.image.src ? `<figure class="lm-img"><img src="${esc(l.image.src)}" alt="${esc(l.image.alt)}" loading="lazy"><figcaption>${esc(l.image.credit)}</figcaption></figure>` : "";
  const real = l.realWorld ? `<p class="lm-real"><b>Real-world counterpart</b>${esc(l.realWorld)}</p>` : "";
  const src = l.source ? `<p class="lm-src">Source: <a href="${esc(l.source.url)}" target="_blank" rel="noopener">${esc(l.source.label)}</a>${l.source.license ? " · " + esc(l.source.license) : ""}</p>` : "";
  return `<div class="lm-pop">
    <div class="lm-chips"><span class="lm-cat" style="--c:${c.color}">${svg(l.category, 12)}${c.label}</span><span class="lm-status s-${esc(l.status)}" title="${esc(st.note)}">${st.label}</span></div>
    <h3>${esc(l.name)}</h3>${nameNote}
    ${l.area ? `<p class="lm-area">${esc(l.area)}</p>` : ""}
    ${img}<p>${esc(l.description)}</p>${real}
    ${l.status === "speculative" ? `<p class="lm-warn">${st.note}</p>` : ""}
    <button type="button" class="lm-found" data-id="${esc(l.id)}">${found ? "✓ Found. Tap to undo" : "Mark as found"}</button>
    ${src}</div>`;
}

/* ---------- markers layer (imperative cluster group for performance) ---------- */
function Markers({ locations, visible, found, hideFound, active, onToggleFound, registerOpen }) {
  const map = useMap();
  const groupRef = useRef(null);
  const markersRef = useRef({});

  useEffect(() => {
    const group = L.markerClusterGroup({
      chunkedLoading: true,
      showCoverageOnHover: false,
      spiderfyOnMaxZoom: true,
      maxClusterRadius: (z) => (z >= 6 ? 30 : 60),
      iconCreateFunction: clusterIcon,
    });
    groupRef.current = group;
    map.addLayer(group);
    const onClick = (e) => {
      const b = e.target.closest && e.target.closest(".lm-found");
      if (b) onToggleFound(b.getAttribute("data-id"));
    };
    map.getContainer().addEventListener("click", onClick);
    return () => { map.removeLayer(group); map.getContainer().removeEventListener("click", onClick); };
  }, [map]);

  useEffect(() => {
    const group = groupRef.current;
    group.clearLayers();
    const ms = {};
    const list = locations.filter(visible).map((l) => {
      const isFound = !!found[fkey(l.id)];
      const m = L.marker(ll(l), { icon: pinIcon(l.category, isFound), title: l.name, alt: l.name, keyboard: true, riseOnHover: true });
      m._lm = { cat: l.category, found: isFound };
      m.bindPopup(() => popupHtml(l, !!loadFound()[fkey(l.id)]), { maxWidth: 300, minWidth: 230, autoPanPadding: [24, 80], className: "lm-popup" });
      ms[l.id] = m;
      return m;
    });
    group.addLayers(list);
    markersRef.current = ms;
  }, [locations, active, hideFound, hideFound ? found : null]);

  // Restyle found markers in place, so an open popup stays open.
  useEffect(() => {
    Object.keys(markersRef.current).forEach((id) => {
      const m = markersRef.current[id], f = !!found[fkey(id)];
      if (m._lm.found !== f) { m._lm.found = f; m.setIcon(pinIcon(m._lm.cat, f)); }
    });
  }, [found]);

  useEffect(() => {
    registerOpen((id) => {
      const m = markersRef.current[id];
      if (!m) return false;
      groupRef.current.zoomToShowLayer(m, () => m.openPopup());
      return true;
    });
  }, [registerOpen]);
  return null;
}

/* ---------- controls ---------- */
function Controls({ shellRef, fs, setFs }) {
  const map = useMap();
  useEffect(() => { setTimeout(() => map.invalidateSize(), 60); }, [fs, map]);
  const toggleFs = () => {
    const el = shellRef.current;
    if (!fs) {
      if (el.requestFullscreen) el.requestFullscreen().catch(() => {});
      setFs(true);
    } else {
      if (document.fullscreenElement && document.exitFullscreen) document.exitFullscreen().catch(() => {});
      setFs(false);
    }
  };
  useEffect(() => {
    const h = () => { if (!document.fullscreenElement) setFs(false); };
    document.addEventListener("fullscreenchange", h);
    return () => document.removeEventListener("fullscreenchange", h);
  }, [setFs]);
  return (
    <div className="lm-ctl" onPointerDown={(e) => e.stopPropagation()}>
      <button type="button" aria-label="Zoom in" onClick={() => map.zoomIn()}>+</button>
      <button type="button" aria-label="Zoom out" onClick={() => map.zoomOut()}>−</button>
      <button type="button" aria-label="Show the whole map" onClick={() => map.flyToBounds(ISLAND, { duration: 0.6 })}>
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2.2"><path d="M4 11l8-7 8 7M6 9.5V20h12V9.5" strokeLinejoin="round" /></svg>
      </button>
      <button type="button" aria-label={fs ? "Exit full screen" : "Full screen"} aria-pressed={fs} onClick={toggleFs}>
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2.2">
          {fs ? <path d="M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5" /> : <path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" />}
        </svg>
      </button>
    </div>
  );
}

function Ready({ onReady }) {
  const map = useMap();
  useEffect(() => {
    map.fitBounds(ISLAND, { padding: [8, 8] });
    map.attributionControl.setPrefix(false);
    onReady(map);
  }, [map]);
  return null;
}

/* ---------- filter panel ---------- */
function Panel({ open, setOpen, counts, active, setActive, hideFound, setHideFound, query, setQuery, results, onPick, foundCount }) {
  const toggle = (id) => setActive((a) => ({ ...a, [id]: !a[id] }));
  const all = (v) => setActive(Object.fromEntries(CATS.map((c) => [c.id, v && counts[c.id] > 0])));
  return (
    <div className={"lm-panel" + (open ? " is-open" : "")} onPointerDown={(e) => e.stopPropagation()} onWheel={(e) => e.stopPropagation()}>
      <button type="button" className="lm-panel-toggle" aria-expanded={open} aria-controls="lm-panel-body" onClick={() => setOpen(!open)}>
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2.2"><path d="M4 6h16M7 12h10M10 18h4" /></svg>
        <span>Filters</span>
        <b>{CATS.filter((c) => active[c.id] && counts[c.id]).length}</b>
      </button>
      <div id="lm-panel-body" className="lm-panel-body" hidden={!open}>
        <label className="lm-search">
          <span className="lm-sr">Search locations</span>
          <input type="search" placeholder="Search 900+ locations" value={query} onChange={(e) => setQuery(e.target.value)} autoComplete="off" />
        </label>
        {query.trim().length > 1 && (
          <ul className="lm-results">
            {results.length === 0 && <li className="lm-none">No matches</li>}
            {results.map((l) => (
              <li key={l.id}>
                <button type="button" onClick={() => onPick(l)}>
                  <span className="lm-dot" style={{ background: CAT[l.category].color }} />
                  <span><b>{l.name}</b><small>{l.area}</small></span>
                </button>
              </li>
            ))}
          </ul>
        )}
        <div className="lm-head"><h3>Categories</h3><span><button type="button" onClick={() => all(true)}>All</button><button type="button" onClick={() => all(false)}>None</button></span></div>
        <ul className="lm-cats">
          {CATS.map((c) => {
            const n = counts[c.id] || 0;
            return (
              <li key={c.id}>
                <label className={n ? "" : "is-soon"}>
                  <input type="checkbox" checked={!!active[c.id] && n > 0} disabled={!n} onChange={() => toggle(c.id)} />
                  <span className="lm-ico" style={{ "--c": c.color }} dangerouslySetInnerHTML={{ __html: svg(c.id, 14) }} />
                  <span className="lm-name">{c.label}</span>
                  <span className="lm-n">{n ? n : "Nov 19"}</span>
                </label>
              </li>
            );
          })}
        </ul>
        <label className="lm-opt"><input type="checkbox" checked={hideFound} onChange={(e) => setHideFound(e.target.checked)} /> Hide found ({foundCount})</label>
        <div className="lm-legend">
          <p><span className="lm-status s-speculative">Speculative</span> Mapped by the community from trailers and screenshots before release. Every marker today is speculative.</p>
          <p><span className="lm-status s-verified">Verified</span> Checked in the released game. Added from November 19.</p>
        </div>
      </div>
    </div>
  );
}

/* ---------- app ---------- */
function App({ dataUrl, tilesUrl }) {
  const [locations, setLocations] = useState(null);
  const [error, setError] = useState(false);
  const [active, setActive] = useState(Object.fromEntries(CATS.map((c) => [c.id, true])));
  const [hideFound, setHideFound] = useState(false);
  const [found, setFound] = useState(loadFound);
  const [query, setQuery] = useState("");
  const [open, setOpen] = useState(() => window.matchMedia("(min-width: 900px)").matches);
  const [fs, setFs] = useState(false);
  const shellRef = useRef(null);
  const openRef = useRef(null);
  const mapRef = useRef(null);

  useEffect(() => {
    fetch(dataUrl).then((r) => (r.ok ? r.json() : Promise.reject())).then(setLocations).catch(() => setError(true));
  }, [dataUrl]);

  const counts = useMemo(() => {
    const c = {};
    (locations || []).forEach((l) => { c[l.category] = (c[l.category] || 0) + 1; });
    return c;
  }, [locations]);

  const visible = useCallback((l) => active[l.category] && !(hideFound && found[fkey(l.id)]), [active, hideFound, found]);

  const onToggleFound = useCallback((id) => {
    const o = loadFound();
    if (o[fkey(id)]) delete o[fkey(id)]; else o[fkey(id)] = 1;
    saveFound(o);
    setFound({ ...o });
    const btn = document.querySelector(`.lm-found[data-id="${CSS.escape(id)}"]`);
    if (btn) btn.textContent = o[fkey(id)] ? "✓ Found. Tap to undo" : "Mark as found";
  }, []);

  const results = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!locations || q.length < 2) return [];
    return locations.filter((l) => (l.name + " " + l.area).toLowerCase().includes(q)).slice(0, 8);
  }, [query, locations]);

  const onPick = (l) => {
    setActive((a) => ({ ...a, [l.category]: true }));
    setHideFound(false);
    if (!window.matchMedia("(min-width: 900px)").matches) setOpen(false);
    setTimeout(() => { if (openRef.current) openRef.current(l.id); }, 80);
  };

  const foundCount = Object.keys(found).filter((k) => k.startsWith("map-")).length;

  return (
    <div className={"lm-shell" + (fs ? " is-fs" : "")} ref={shellRef}>
      <MapContainer
        crs={CRS}
        className="lm-map"
        center={[0, -3000]}
        zoom={1}
        minZoom={0}
        maxZoom={6}
        zoomSnap={0.25}
        zoomDelta={1}
        wheelPxPerZoomLevel={90}
        maxBounds={LIMITS}
        maxBoundsViscosity={0.9}
        zoomControl={false}
        attributionControl={true}
        preferCanvas={false}
      >
        <TileLayer
          url={tilesUrl}
          tileSize={256}
          minNativeZoom={0}
          maxNativeZoom={5}
          maxZoom={6}
          bounds={TILE_BOUNDS}
          noWrap={true}
          keepBuffer={4}
          attribution='Map &amp; data: <a href="https://map.gtadb.org" target="_blank" rel="noopener">GTA VI Mapping Community (YANIS v17) via gtadb.org</a>, <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a>. Legend removed, data adapted.'
        />
        <Ready onReady={(m) => { mapRef.current = m; }} />
        {locations && <Markers locations={locations} visible={visible} found={found} hideFound={hideFound} active={active} onToggleFound={onToggleFound} registerOpen={(fn) => { openRef.current = fn; }} />}
        <Controls shellRef={shellRef} fs={fs} setFs={setFs} />
      </MapContainer>
      <Panel open={open} setOpen={setOpen} counts={counts} active={active} setActive={setActive} hideFound={hideFound} setHideFound={setHideFound}
        query={query} setQuery={setQuery} results={results} onPick={onPick} foundCount={foundCount} />
      <div className="lm-badge" aria-hidden="true"><b>Pre-launch map</b> Community reconstruction · not official</div>
      {!locations && !error && <div className="lm-loading">Loading locations…</div>}
      {error && <div className="lm-loading">Locations could not load. Refresh the page to try again.</div>}
    </div>
  );
}

const el = document.getElementById("leonida-map");
if (el) createRoot(el).render(<App dataUrl={el.dataset.src} tilesUrl={el.dataset.tiles} />);
