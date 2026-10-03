import html, pathlib
R = pathlib.Path("/home/user/android_reflex/reports")
docs = [
 ("top20", "Könyvelőirodák top 20 lista.md", "Top 20 könyvelőiroda", "Kiket keressetek meg először"),
 ("konyvelo", "Könyvelőirodás lehetőség részletesen.md", "Könyvelős lehetőség", "Ajánlat, árazás, integráció, ütemterv"),
 ("interju", "Interjúterv könyvelőirodáknak.md", "Interjúterv", "Kérdéssor, sablonok, 8 hetes terv"),
 ("iparagak", "További iparágak AI.md", "További iparágak", "17 iparág pontozva, top 5"),
 ("alap", "AI üzleti lehetőségek Szegeden.md", "Alapkutatás", "AI-lehetőségek Magyarországon és Szegeden"),
]
nav = "\n".join(f'<a href="#{k}" data-k="{k}"><span class="t">{html.escape(t)}</span><span class="s">{html.escape(s)}</span></a>' for k,_,t,s in docs)
opts = "\n".join(f'<option value="{k}">{html.escape(t)}</option>' for k,_,t,_ in docs)
blobs = "\n".join(f'<script type="text/markdown" id="md-{k}">{(R/f).read_text()}</script>' for k,f,_,_ in docs)
page = f'''<title>Szegedi AI-kutatás</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: olvasó nézet – bal oldali dokumentumválasztó (asztali), felső legördülő (mobil), egy hasábos szöveg ~68 karakter */
:root {{
  --bg:#f6f7f4; --surface:#ffffff; --fg:#1d231f; --muted:#5d6a62; --line:#dde3dc;
  --accent:#1f6b52; --accent-soft:#e3efe8; --warn-bg:#fbf3df; --code-bg:#eef1ec;
  --display:"Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --body:"Source Serif 4", Georgia, "Times New Roman", serif;
  --mono:"IBM Plex Mono", ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#121614; --surface:#181d1a; --fg:#e4e9e5; --muted:#9aa8a0; --line:#2a322d;
  --accent:#6fc4a2; --accent-soft:#1d3229; --warn-bg:#2c2717; --code-bg:#1f2522; color-scheme:dark; }} }}
:root[data-theme="dark"] {{
  --bg:#121614; --surface:#181d1a; --fg:#e4e9e5; --muted:#9aa8a0; --line:#2a322d;
  --accent:#6fc4a2; --accent-soft:#1d3229; --warn-bg:#2c2717; --code-bg:#1f2522; color-scheme:dark; }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--body); font-size:17px; line-height:1.6; }}
.wrap {{ display:grid; grid-template-columns:260px minmax(0,1fr); gap:40px; max-width:1180px; margin:0 auto; padding-inline:24px; padding-block:32px; }}
aside {{ position:sticky; top:calc(env(safe-area-inset-top,0px) + 24px); align-self:start; display:flex; flex-direction:column; gap:6px; }}
.brand {{ font-family:var(--display); font-weight:700; font-size:20px; margin-block-end:4px; }}
.sub {{ font-family:var(--mono); font-size:12px; color:var(--muted); letter-spacing:.04em; text-transform:uppercase; margin-block-end:14px; }}
aside a {{ display:flex; flex-direction:column; gap:2px; padding:10px 12px; border-radius:8px; text-decoration:none; color:var(--fg); }}
aside a:hover {{ background:var(--accent-soft); }}
aside a.on {{ background:var(--accent-soft); box-shadow:inset 3px 0 0 var(--accent); }}
aside .t {{ font-family:var(--display); font-weight:500; font-size:15px; }}
aside .s {{ font-size:13px; color:var(--muted); line-height:1.35; }}
.picker {{ display:none; }}
main {{ min-width:0; background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:36px 44px; }}
article {{ max-width:70ch; }}
article h1,article h2,article h3,article h4 {{ font-family:var(--display); line-height:1.2; text-wrap:balance; }}
article h1 {{ font-size:32px; font-weight:700; margin:0 0 18px; }}
article h2 {{ font-size:23px; font-weight:700; margin:40px 0 12px; padding-block-start:18px; border-top:1px solid var(--line); }}
article h3 {{ font-size:19px; font-weight:500; margin:28px 0 8px; }}
article p, article li {{ margin:0 0 12px; }}
article a {{ color:var(--accent); text-underline-offset:2px; word-break:break-word; }}
article strong {{ font-weight:600; }}
article blockquote {{ margin:16px 0; padding:10px 16px; background:var(--warn-bg); border-radius:6px; }}
article code {{ font-family:var(--mono); font-size:.86em; background:var(--code-bg); padding:1px 5px; border-radius:4px; }}
article pre {{ background:var(--code-bg); padding:14px; border-radius:6px; overflow-x:auto; }}
article pre code {{ background:none; padding:0; }}
.tbl {{ overflow-x:auto; margin:16px 0 20px; border:1px solid var(--line); border-radius:6px; max-width:calc(100vw - 48px); }}
article:has(.tbl) {{ max-width:none; }}
article > :not(.tbl) {{ max-width:70ch; }}
table {{ border-collapse:collapse; font-size:14.5px; line-height:1.45; font-variant-numeric:tabular-nums; min-width:100%; }}
th,td {{ text-align:left; vertical-align:top; padding:8px 10px; border-bottom:1px solid var(--line); }}
th {{ font-family:var(--display); font-weight:500; background:var(--accent-soft); white-space:nowrap; }}
tr:last-child td {{ border-bottom:none; }}
hr {{ border:none; border-top:1px solid var(--line); margin:28px 0; }}
a:focus-visible, select:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
@media (max-width:860px) {{
  body {{ font-size:16px; }}
  .wrap {{ grid-template-columns:minmax(0,1fr); gap:16px; padding-inline:16px; padding-block:16px; }}
  aside {{ position:static; }}
  aside a {{ display:none; }}
  .sub {{ margin-block-end:4px; }}
  .picker {{ display:block; width:100%; font:500 16px var(--display); padding:10px 12px; border-radius:8px; border:1px solid var(--line); background:var(--surface); color:var(--fg); }}
  main {{ padding:20px 16px; }}
  article h1 {{ font-size:25px; }} article h2 {{ font-size:20px; }}
  .tbl {{ max-width:calc(100vw - 66px); }}
}}
</style>
<div class="wrap">
<aside>
  <div class="brand">Szegedi AI-kutatás</div>
  <div class="sub">2026. október · 5 anyag</div>
  <label for="picker" class="sub" hidden>Dokumentum</label>
  <select id="picker" class="picker" aria-label="Dokumentum választása">{opts}</select>
  {nav}
</aside>
<main><article id="doc"></article></main>
</div>
{blobs}
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
const keys = {[k for k,_,_,_ in docs]!r};
const art = document.getElementById('doc'), pick = document.getElementById('picker');
function show(k) {{
  if (!keys.includes(k)) k = keys[0];
  const src = document.getElementById('md-' + k).textContent;
  art.innerHTML = window.marked ? marked.parse(src) : '<pre>' + src.replace(/[&<]/g, c => c=='&'?'&amp;':'&lt;') + '</pre>';
  art.querySelectorAll('table').forEach(t => {{ const w = document.createElement('div'); w.className = 'tbl'; t.replaceWith(w); w.appendChild(t); }});
  art.querySelectorAll('a[href^="http"]').forEach(a => {{ a.target = '_blank'; a.rel = 'noopener'; }});
  document.querySelectorAll('aside a').forEach(a => a.classList.toggle('on', a.dataset.k === k));
  pick.value = k;
  try {{ localStorage.setItem('doc', k); }} catch (e) {{}}
}}
pick.addEventListener('change', () => {{ location.hash = pick.value; }});
window.addEventListener('hashchange', () => {{ show(location.hash.slice(1)); window.scrollTo(0, 0); }});
let start = location.hash.slice(1);
if (!keys.includes(start)) {{ try {{ start = localStorage.getItem('doc') || ''; }} catch (e) {{}} }}
show(start);
</script>
'''
(R/"html"/"kutatas.html").write_text(page)
print(len(page))
