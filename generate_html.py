# -*- coding: utf-8 -*-
import json

with open("reviews.json", encoding="utf-8") as f:
    data = json.load(f)

updated_at = data["updated_at"]
restaurants = data["restaurants"]

FULL_RANKING = [
    {"rank": 1,  "name": "Park Sathorn Restaurant",       "area": "Sathorn",       "cuisine": "Thai",          "stars": 4.45, "reviews_count": 575,  "price": 400,  "capacity": 50,  "distance": 7,  "score": 94.9},
    {"rank": 2,  "name": "The Deck Bangkok",               "area": "Phrom Phong",   "cuisine": "International", "stars": 4.40, "reviews_count": 890,  "price": 450,  "capacity": 60,  "distance": 12, "score": 94.6},
    {"rank": 3,  "name": "Lazy Daisy Brunch and Bar",      "area": "Phrom Phong",   "cuisine": "Western/Brunch","stars": 4.50, "reviews_count": 1200, "price": 350,  "capacity": 45,  "distance": 12, "score": 94.6},
    {"rank": 4,  "name": "Roast Coffee & Eatery",          "area": "EmQuartier",    "cuisine": "Western/Brunch","stars": 4.30, "reviews_count": 2100, "price": 400,  "capacity": 55,  "distance": 14, "score": 93.1},
    {"rank": 5,  "name": "Savelberg",                      "area": "Phrom Phong",   "cuisine": "French",        "stars": 4.50, "reviews_count": 450,  "price": 900,  "capacity": 35,  "distance": 12, "score": 92.8},
    {"rank": 6,  "name": "Soul Food Mahanakorn",           "area": "Ekkamai",       "cuisine": "Thai",          "stars": 4.35, "reviews_count": 1800, "price": 350,  "capacity": 50,  "distance": 20, "score": 91.7},
    {"rank": 7,  "name": "After You Dessert Cafe",         "area": "Thonglor",      "cuisine": "Cafe/Dessert",  "stars": 4.25, "reviews_count": 3200, "price": 250,  "capacity": 40,  "distance": 17, "score": 91.2},
    {"rank": 8,  "name": "Peppina",                        "area": "Ekkamai",       "cuisine": "Italian",       "stars": 4.40, "reviews_count": 980,  "price": 500,  "capacity": 50,  "distance": 20, "score": 90.8},
    {"rank": 9,  "name": "The Local Restaurant",           "area": "Sukhumvit 23",  "cuisine": "Thai",          "stars": 4.35, "reviews_count": 760,  "price": 450,  "capacity": 45,  "distance": 16, "score": 90.5},
    {"rank": 10, "name": "Appia",                          "area": "Sukhumvit 31",  "cuisine": "Italian",       "stars": 4.40, "reviews_count": 520,  "price": 600,  "capacity": 40,  "distance": 18, "score": 90.3},
    {"rank": 11, "name": "Quince",                         "area": "Sukhumvit 45",  "cuisine": "International", "stars": 4.30, "reviews_count": 430,  "price": 700,  "capacity": 35,  "distance": 22, "score": 89.6},
    {"rank": 12, "name": "Meatlicious",                    "area": "Silom",         "cuisine": "BBQ/Grill",     "stars": 4.20, "reviews_count": 650,  "price": 550,  "capacity": 55,  "distance": 15, "score": 89.1},
    {"rank": 13, "name": "Somboon Seafood (Silom)",        "area": "Silom",         "cuisine": "Seafood",       "stars": 4.25, "reviews_count": 1500, "price": 500,  "capacity": 80,  "distance": 15, "score": 88.9},
    {"rank": 14, "name": "Thara Thong",                    "area": "Sathorn",       "cuisine": "Thai",          "stars": 4.15, "reviews_count": 340,  "price": 380,  "capacity": 60,  "distance": 8,  "score": 88.4},
    {"rank": 15, "name": "Baani Garden Cafe",              "area": "Thonglor",      "cuisine": "Cafe/Thai",     "stars": 4.35, "reviews_count": 280,  "price": 300,  "capacity": 40,  "distance": 17, "score": 88.1},
    {"rank": 16, "name": "Ginzado",                        "area": "Silom",         "cuisine": "Japanese",      "stars": 4.20, "reviews_count": 410,  "price": 600,  "capacity": 35,  "distance": 14, "score": 87.5},
    {"rank": 17, "name": "On Lok Yun",                     "area": "Charoen Krung", "cuisine": "Chinese/Local", "stars": 4.30, "reviews_count": 1100, "price": 150,  "capacity": 50,  "distance": 25, "score": 87.2},
    {"rank": 18, "name": "Charcoal Tandoor Grill",         "area": "Sathorn",       "cuisine": "Indian/Grill",  "stars": 4.10, "reviews_count": 380,  "price": 550,  "capacity": 45,  "distance": 9,  "score": 86.9},
    {"rank": 19, "name": "Maguro Japanese Restaurant",     "area": "Sukhumvit 26",  "cuisine": "Japanese",      "stars": 4.15, "reviews_count": 290,  "price": 500,  "capacity": 40,  "distance": 15, "score": 86.5},
    {"rank": 20, "name": "Namsaah Bottling Trust",         "area": "Silom",         "cuisine": "Thai Fusion",   "stars": 4.20, "reviews_count": 470,  "price": 450,  "capacity": 45,  "distance": 14, "score": 86.2},
    {"rank": 21, "name": "Bo.lan",                         "area": "Sukhumvit 53",  "cuisine": "Thai Fine",     "stars": 4.40, "reviews_count": 920,  "price": 1800, "capacity": 30,  "distance": 22, "score": 85.8},
    {"rank": 22, "name": "Paste Bangkok",                  "area": "Gaysorn",       "cuisine": "Thai Fine",     "stars": 4.35, "reviews_count": 680,  "price": 1200, "capacity": 35,  "distance": 20, "score": 85.4},
    {"rank": 23, "name": "Indus Restaurant",               "area": "Sukhumvit 26",  "cuisine": "Indian",        "stars": 4.10, "reviews_count": 350,  "price": 450,  "capacity": 50,  "distance": 15, "score": 84.9},
    {"rank": 24, "name": "Biscotti",                       "area": "Ploenchit",     "cuisine": "Italian",       "stars": 4.05, "reviews_count": 420,  "price": 800,  "capacity": 60,  "distance": 22, "score": 84.3},
    {"rank": 25, "name": "Vientiane Kitchen",              "area": "Ekkamai",       "cuisine": "Lao/Thai",      "stars": 4.15, "reviews_count": 560,  "price": 300,  "capacity": 70,  "distance": 20, "score": 83.9},
]

ranking_json = json.dumps(FULL_RANKING, ensure_ascii=False)

def review_card(rv):
    stars_str = "★" * rv['rating'] + "☆" * (5 - rv['rating'])
    return (
        '<div class="review-card">'
        '<div class="review-header">'
        f'<span class="review-stars">{stars_str}</span>'
        f'<span class="review-meta">{rv["author"]} &middot; {rv["date"]} &middot; <em>{rv["source"]}</em></span>'
        '</div>'
        f'<p class="review-text">"{rv["text"]}"</p>'
        '</div>'
    )

def review_section(r):
    cards = "".join(review_card(rv) for rv in r["reviews"])
    emoji = "\U0001f3c6" if r["rank"] == 1 else f'#{r["rank"]}'
    return (
        '<div class="rest-section">'
        '<div class="rest-header">'
        f'<span class="rest-rank">{emoji}</span>'
        f'<h3>{r["name"]}</h3>'
        f'<span class="rest-score">{r["score"]}/100</span>'
        '</div>'
        f'<div class="reviews-list">{cards}</div>'
        '</div>'
    )

def top5_card(r):
    bar_w = int(r['score'])
    medals = ["\U0001f947","\U0001f948","\U0001f949","4️⃣","5️⃣"]
    medal = medals[r['rank']-1]
    color = "#10b981" if r['rank']==1 else "#3b82f6" if r['rank']<=3 else "#6b7280"
    return (
        '<div class="top5-card">'
        f'<div class="top5-medal">{medal}</div>'
        '<div class="top5-info">'
        f'<div class="top5-name">{r["name"]}</div>'
        f'<div class="top5-meta">{r["area"]} | {r["cuisine"]} | ⭐{r["stars"]} ({r["reviews_count"]:,} reviews) | ฿{r["price"]}/head</div>'
        f'<div class="score-bar-bg"><div class="score-bar-fill" style="width:{bar_w}%;background:{color}"></div></div>'
        '</div>'
        f'<div class="top5-score" style="color:{color}">{r["score"]}</div>'
        '</div>'
    )

reviews_html = "".join(review_section(r) for r in restaurants)
top5_html = "".join(top5_card(r) for r in FULL_RANKING[:5])

CSS = """
:root{--gold:#f59e0b;--green:#10b981;--blue:#3b82f6;--bg:#f8fafc;--card:#fff;--border:#e2e8f0;--text:#1e293b;--muted:#64748b;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;}
.header{background:linear-gradient(135deg,#1e293b,#334155);color:#fff;padding:40px 32px;text-align:center;}
.header h1{font-size:2rem;font-weight:800;margin-bottom:6px;}
.header p{opacity:.8;font-size:.95rem;}
.update-bar{background:#f0fdf4;border-bottom:1px solid #bbf7d0;text-align:center;padding:10px;font-size:.85rem;color:#166534;}
.update-bar span{font-weight:700;}
.container{max-width:1100px;margin:0 auto;padding:32px 20px;}
.section-title{font-size:1.15rem;font-weight:700;margin:32px 0 16px;padding-bottom:8px;border-bottom:2px solid var(--border);color:var(--text);}
.hero{background:linear-gradient(135deg,#065f46,#047857);color:#fff;border-radius:16px;padding:28px;margin-bottom:32px;position:relative;overflow:hidden;}
.hero-bg-score{font-size:8rem;font-weight:900;opacity:.08;position:absolute;right:16px;top:-10px;line-height:1;}
.hero-label{font-size:.75rem;text-transform:uppercase;letter-spacing:.1em;opacity:.8;margin-bottom:6px;}
.hero h2{font-size:1.7rem;font-weight:800;margin-bottom:6px;}
.hero-meta{opacity:.9;font-size:.9rem;margin-bottom:4px;}
.hero-badge{display:inline-block;background:rgba(255,255,255,.15);border-radius:6px;padding:5px 12px;font-size:.85rem;margin-top:10px;}
.map-btn{display:inline-block;margin-top:12px;background:#fff;color:#065f46;padding:8px 18px;border-radius:8px;text-decoration:none;font-weight:700;font-size:.85rem;margin-left:8px;}
.top5-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;margin-bottom:12px;display:flex;align-items:center;gap:14px;}
.top5-medal{font-size:1.8rem;width:40px;text-align:center;flex-shrink:0;}
.top5-info{flex:1;}
.top5-name{font-weight:700;font-size:1rem;margin-bottom:3px;}
.top5-meta{font-size:.8rem;color:var(--muted);margin-bottom:6px;}
.score-bar-bg{background:#e2e8f0;border-radius:4px;height:6px;overflow:hidden;}
.score-bar-fill{height:100%;border-radius:4px;}
.top5-score{font-size:1.5rem;font-weight:900;min-width:55px;text-align:right;}
.filter-bar{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:16px 20px;margin-bottom:16px;display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end;}
.filter-group{display:flex;flex-direction:column;gap:4px;min-width:130px;}
.filter-group label{font-size:.75rem;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;}
.filter-group select{padding:7px 10px;border:1px solid var(--border);border-radius:7px;font-size:.85rem;background:#fff;color:var(--text);cursor:pointer;}
.filter-group select:focus{outline:none;border-color:var(--blue);}
.btn-reset{padding:7px 16px;background:#f1f5f9;border:1px solid var(--border);border-radius:7px;font-size:.85rem;cursor:pointer;font-weight:600;color:var(--muted);align-self:flex-end;}
.btn-reset:hover{background:#e2e8f0;}
.result-count{font-size:.82rem;color:var(--muted);align-self:flex-end;margin-left:auto;}
.table-wrap{overflow-x:auto;border-radius:10px;border:1px solid var(--border);}
table{width:100%;border-collapse:collapse;background:var(--card);font-size:.85rem;}
thead{background:#f1f5f9;}
th{padding:10px 12px;text-align:left;font-weight:600;color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap;cursor:pointer;user-select:none;}
th:hover{background:#e2e8f0;color:var(--text);}
th .si{margin-left:4px;opacity:.35;}
th.sa .si,th.sd .si{opacity:1;color:var(--blue);}
td{padding:10px 12px;border-top:1px solid var(--border);}
tr:hover{background:#f8fafc;}
.td-rank{font-size:1rem;text-align:center;}
.td-name{font-weight:600;}
.sh{color:#10b981;font-weight:800;}
.sm{color:#3b82f6;font-weight:700;}
.sl{color:#6b7280;font-weight:600;}
.no-res{text-align:center;padding:40px;color:var(--muted);font-size:.95rem;}
.weights-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;}
.weight-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px;text-align:center;}
.weight-pct{font-size:1.5rem;font-weight:800;color:var(--blue);}
.weight-label{font-size:.8rem;color:var(--muted);margin-top:2px;}
.rest-section{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;margin-bottom:16px;}
.rest-header{display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.rest-rank{font-size:1.3rem;}
.rest-header h3{flex:1;font-size:1rem;font-weight:700;}
.rest-score{font-size:1rem;font-weight:800;color:var(--green);}
.review-card{border-left:3px solid var(--gold);padding:8px 12px;margin-bottom:8px;background:#fffbeb;border-radius:0 6px 6px 0;}
.review-header{display:flex;align-items:center;gap:8px;margin-bottom:3px;flex-wrap:wrap;}
.review-stars{color:var(--gold);font-size:.95rem;}
.review-meta{font-size:.75rem;color:var(--muted);}
.review-text{font-size:.85rem;font-style:italic;}
.footer{text-align:center;padding:24px;color:var(--muted);font-size:.78rem;border-top:1px solid var(--border);margin-top:16px;}
"""

JS = """
const DATA = RANKING_JSON_PLACEHOLDER;
let cSort = {key:'score',dir:'desc'};
const areas = [...new Set(DATA.map(r=>r.area))].sort();
const cuisines = [...new Set(DATA.map(r=>r.cuisine))].sort();
areas.forEach(a=>document.getElementById('f-area').innerHTML+=`<option value="${a}">${a}</option>`);
cuisines.forEach(c=>document.getElementById('f-cuisine').innerHTML+=`<option value="${c}">${c}</option>`);
function medal(n){return n===1?'🏆':n===2?'🥈':n===3?'🥉':n;}
function sc(s){return s>=92?'sh':s>=88?'sm':'sl';}
function getFiltered(){
  const a=document.getElementById('f-area').value;
  const c=document.getElementById('f-cuisine').value;
  const p=document.getElementById('f-price').value;
  const s=document.getElementById('f-score').value;
  return DATA.filter(r=>{
    if(a&&r.area!==a)return false;
    if(c&&r.cuisine!==c)return false;
    if(p&&r.price>=parseInt(p))return false;
    if(s&&r.score<parseFloat(s))return false;
    return true;
  });
}
function getSorted(rows){
  return [...rows].sort((a,b)=>{
    let av=a[cSort.key],bv=b[cSort.key];
    if(typeof av==='string'){av=av.toLowerCase();bv=bv.toLowerCase();}
    if(av<bv)return cSort.dir==='asc'?-1:1;
    if(av>bv)return cSort.dir==='asc'?1:-1;
    return 0;
  });
}
function renderTable(){
  const rows=getSorted(getFiltered());
  document.getElementById('result-count').textContent=rows.length+' restaurant'+(rows.length!==1?'s':'');
  const tbody=document.getElementById('table-body');
  if(!rows.length){tbody.innerHTML='<tr><td colspan="10" class="no-res">No restaurants match your filters. Try resetting.</td></tr>';return;}
  tbody.innerHTML=rows.map(r=>`<tr>
    <td class="td-rank">${medal(r.rank)}</td>
    <td class="td-name">${r.name}</td>
    <td>${r.area}</td><td>${r.cuisine}</td>
    <td>⭐ ${r.stars}</td>
    <td>${r.reviews_count.toLocaleString()}</td>
    <td>฿${r.price}</td><td>${r.capacity}</td>
    <td>${r.distance} min</td>
    <td class="${sc(r.score)}">${r.score}</td>
  </tr>`).join('');
}
function updateHeaders(){
  document.querySelectorAll('th').forEach(th=>{th.classList.remove('sa','sd');const i=th.querySelector('.si');if(i)i.textContent='↕';});
  const th=document.getElementById('th-'+cSort.key);
  if(th){th.classList.add(cSort.dir==='asc'?'sa':'sd');const i=th.querySelector('.si');if(i)i.textContent=cSort.dir==='asc'?'↑':'↓';}
}
function applyFilters(){
  const v=document.getElementById('f-sort').value;
  const [k,d]=v.split('-');
  cSort={key:k,dir:d};
  updateHeaders();renderTable();
}
function sortBy(key){
  if(cSort.key===key){cSort.dir=cSort.dir==='asc'?'desc':'asc';}
  else{cSort={key,dir:(key==='name'||key==='area'||key==='cuisine')?'asc':'desc'};}
  const sel=document.getElementById('f-sort');
  const opt=key+'-'+cSort.dir;
  if([...sel.options].some(o=>o.value===opt))sel.value=opt;
  updateHeaders();renderTable();
}
function resetFilters(){
  ['f-area','f-cuisine','f-price','f-score'].forEach(id=>document.getElementById(id).value='');
  document.getElementById('f-sort').value='score-desc';
  cSort={key:'score',dir:'desc'};
  updateHeaders();renderTable();
}
renderTable();updateHeaders();
"""

JS = JS.replace("RANKING_JSON_PLACEHOLDER", ranking_json)

html_parts = [
    '<!DOCTYPE html>',
    '<html lang="en">',
    '<head>',
    '<meta charset="UTF-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<title>Team Dinner Restaurant Selection - Bangkok</title>',
    '<style>', CSS, '</style>',
    '</head>',
    '<body>',
    '<div class="header"><h1>\U0001f37d️ Team Dinner Restaurant Selection</h1><p>Data-driven ranking across 25 qualifying venues in Bangkok</p></div>',
    f'<div class="update-bar">⏱ Reviews auto-updated every 6 hours &nbsp;|&nbsp; Last update: <span>{updated_at}</span></div>',
    '<div class="container">',

    # HERO
    '<div class="hero"><div class="hero-bg-score">94.9</div>'
    '<div class="hero-label">\U0001f3c6 Top Pick — Score 94.9 / 100</div>'
    '<h2>Park Sathorn Restaurant</h2>'
    '<p class="hero-meta">\U0001f4cd Sathorn &nbsp;|&nbsp; Thai Cuisine &nbsp;|&nbsp; ⭐ 4.45 (575 reviews)</p>'
    '<p class="hero-meta">\U0001f697 7 min from office &nbsp;|&nbsp; \U0001f465 Seats up to 50 &nbsp;|&nbsp; \U0001f4b0 ฿400/head</p>'
    '<span class="hero-badge">\U0001f33f Garden \xb7 Waterfall \xb7 Live Dance Show</span>'
    '<a href="https://www.google.com/maps/search/?api=1&query=13.719795,100.551228" target="_blank" class="map-btn">\U0001f4cd View on Map</a>'
    '</div>',

    # TOP 5
    '<div class="section-title">\U0001f947 Top 5 Shortlist</div>',
    top5_html,

    # FULL RANKING
    '<div class="section-title">\U0001f4cb Full Ranking — All 25 Restaurants</div>',
    '<div class="filter-bar">',
    '<div class="filter-group"><label>Area</label><select id="f-area" onchange="applyFilters()"><option value="">All Areas</option></select></div>',
    '<div class="filter-group"><label>Cuisine</label><select id="f-cuisine" onchange="applyFilters()"><option value="">All Cuisines</option></select></div>',
    '<div class="filter-group"><label>Max Price (฿/head)</label><select id="f-price" onchange="applyFilters()"><option value="">Any Price</option><option value="300">Under ฿300</option><option value="500">Under ฿500</option><option value="700">Under ฿700</option><option value="1000">Under ฿1,000</option></select></div>',
    '<div class="filter-group"><label>Min Score</label><select id="f-score" onchange="applyFilters()"><option value="">Any Score</option><option value="92">92+</option><option value="90">90+</option><option value="88">88+</option><option value="85">85+</option></select></div>',
    '<div class="filter-group"><label>Sort By</label><select id="f-sort" onchange="applyFilters()"><option value="score-desc">Score ↓ High first</option><option value="score-asc">Score ↑ Low first</option><option value="stars-desc">Rating ↓ High first</option><option value="stars-asc">Rating ↑ Low first</option><option value="price-asc">Price ↑ Low first</option><option value="price-desc">Price ↓ High first</option><option value="distance-asc">Distance ↑ Nearest</option><option value="distance-desc">Distance ↓ Farthest</option></select></div>',
    '<button class="btn-reset" onclick="resetFilters()">&#8635; Reset</button>',
    '<span class="result-count" id="result-count">25 restaurants</span>',
    '</div>',
    '<div class="table-wrap"><table id="ranking-table"><thead><tr>',
    '<th onclick="sortBy(\'rank\')" id="th-rank"># <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'name\')" id="th-name">Restaurant <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'area\')" id="th-area">Area <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'cuisine\')" id="th-cuisine">Cuisine <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'stars\')" id="th-stars">Rating <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'reviews_count\')" id="th-reviews_count">Reviews <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'price\')" id="th-price">Price/head <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'capacity\')" id="th-capacity">Capacity <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'distance\')" id="th-distance">Distance <span class="si">↕</span></th>',
    '<th onclick="sortBy(\'score\')" id="th-score">Score <span class="si">↕</span></th>',
    '</tr></thead><tbody id="table-body"></tbody></table></div>',

    # SCORING
    '<div class="section-title">⚖️ Scoring Model Weights</div>',
    '<div class="weights-grid">',
    '<div class="weight-card"><div class="weight-pct">35%</div><div class="weight-label">Customer Rating</div></div>',
    '<div class="weight-card"><div class="weight-pct">20%</div><div class="weight-label">Group Suitability</div></div>',
    '<div class="weight-card"><div class="weight-pct">20%</div><div class="weight-label">Value for Money</div></div>',
    '<div class="weight-card"><div class="weight-pct">15%</div><div class="weight-label">Distance from Office</div></div>',
    '<div class="weight-card"><div class="weight-pct">10%</div><div class="weight-label">Review Volume</div></div>',
    '</div>',

    # REVIEWS
    '<div class="section-title">\U0001f4ac Latest Reviews — Top 3 Shortlist <small style="font-weight:400;color:var(--muted);font-size:.8rem">Auto-updated every 6 hours</small></div>',
    reviews_html,

    '</div>',
    '<div class="footer">Auto-updated every 6 hours via Make.com + GitHub Actions &nbsp;|&nbsp; Sources: TripAdvisor + Google &nbsp;|&nbsp; 2026</div>',
    '<script>', JS, '</script>',
    '</body></html>',
]

html = "\n".join(html_parts)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html generated successfully")
