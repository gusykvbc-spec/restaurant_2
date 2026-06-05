# -*- coding: utf-8 -*-
import json

with open("reviews.json", encoding="utf-8") as f:
    data = json.load(f)

updated_at = data["updated_at"]
restaurants = data["restaurants"]

# Full ranking data (static, from scoring model)
FULL_RANKING = [
    {"rank": 1,  "name": "Park Sathorn Restaurant",       "area": "Sathorn",       "cuisine": "Thai",          "stars": 4.45, "reviews_count": 575, "price": 400,  "capacity": 50,  "distance": 7,  "score": 94.9},
    {"rank": 2,  "name": "The Deck Bangkok",               "area": "Phrom Phong",   "cuisine": "International", "stars": 4.40, "reviews_count": 890, "price": 450,  "capacity": 60,  "distance": 12, "score": 94.6},
    {"rank": 3,  "name": "Lazy Daisy Brunch and Bar",      "area": "Phrom Phong",   "cuisine": "Western/Brunch","stars": 4.50, "reviews_count": 1200,"price": 350,  "capacity": 45,  "distance": 12, "score": 94.6},
    {"rank": 4,  "name": "Roast Coffee & Eatery",          "area": "EmQuartier",    "cuisine": "Western/Brunch","stars": 4.30, "reviews_count": 2100,"price": 400,  "capacity": 55,  "distance": 14, "score": 93.1},
    {"rank": 5,  "name": "Savelberg",                      "area": "Phrom Phong",   "cuisine": "French",        "stars": 4.50, "reviews_count": 450, "price": 900,  "capacity": 35,  "distance": 12, "score": 92.8},
    {"rank": 6,  "name": "Soul Food Mahanakorn",           "area": "Ekkamai",       "cuisine": "Thai",          "stars": 4.35, "reviews_count": 1800,"price": 350,  "capacity": 50,  "distance": 20, "score": 91.7},
    {"rank": 7,  "name": "After You Dessert Cafe",         "area": "Thonglor",      "cuisine": "Cafe/Dessert",  "stars": 4.25, "reviews_count": 3200,"price": 250,  "capacity": 40,  "distance": 17, "score": 91.2},
    {"rank": 8,  "name": "Peppina",                        "area": "Ekkamai",       "cuisine": "Italian",       "stars": 4.40, "reviews_count": 980, "price": 500,  "capacity": 50,  "distance": 20, "score": 90.8},
    {"rank": 9,  "name": "The Local Restaurant",           "area": "Sukhumvit 23",  "cuisine": "Thai",          "stars": 4.35, "reviews_count": 760, "price": 450,  "capacity": 45,  "distance": 16, "score": 90.5},
    {"rank": 10, "name": "Appia",                          "area": "Sukhumvit 31",  "cuisine": "Italian",       "stars": 4.40, "reviews_count": 520, "price": 600,  "capacity": 40,  "distance": 18, "score": 90.3},
    {"rank": 11, "name": "Quince",                         "area": "Sukhumvit 45",  "cuisine": "International", "stars": 4.30, "reviews_count": 430, "price": 700,  "capacity": 35,  "distance": 22, "score": 89.6},
    {"rank": 12, "name": "Meatlicious",                    "area": "Silom",         "cuisine": "BBQ/Grill",     "stars": 4.20, "reviews_count": 650, "price": 550,  "capacity": 55,  "distance": 15, "score": 89.1},
    {"rank": 13, "name": "Somboon Seafood (Silom)",        "area": "Silom",         "cuisine": "Seafood",       "stars": 4.25, "reviews_count": 1500,"price": 500,  "capacity": 80,  "distance": 15, "score": 88.9},
    {"rank": 14, "name": "Thara Thong",                    "area": "Sathorn",       "cuisine": "Thai",          "stars": 4.15, "reviews_count": 340, "price": 380,  "capacity": 60,  "distance": 8,  "score": 88.4},
    {"rank": 15, "name": "Baani Garden Cafe",              "area": "Thonglor",      "cuisine": "Cafe/Thai",     "stars": 4.35, "reviews_count": 280, "price": 300,  "capacity": 40,  "distance": 17, "score": 88.1},
    {"rank": 16, "name": "Ginzado",                        "area": "Silom",         "cuisine": "Japanese",      "stars": 4.20, "reviews_count": 410, "price": 600,  "capacity": 35,  "distance": 14, "score": 87.5},
    {"rank": 17, "name": "On Lok Yun",                     "area": "Charoen Krung", "cuisine": "Chinese/Local", "stars": 4.30, "reviews_count": 1100,"price": 150,  "capacity": 50,  "distance": 25, "score": 87.2},
    {"rank": 18, "name": "Charcoal Tandoor Grill",         "area": "Sathorn",       "cuisine": "Indian/Grill",  "stars": 4.10, "reviews_count": 380, "price": 550,  "capacity": 45,  "distance": 9,  "score": 86.9},
    {"rank": 19, "name": "Maguro Japanese Restaurant",     "area": "Sukhumvit 26",  "cuisine": "Japanese",      "stars": 4.15, "reviews_count": 290, "price": 500,  "capacity": 40,  "distance": 15, "score": 86.5},
    {"rank": 20, "name": "Namsaah Bottling Trust",         "area": "Silom",         "cuisine": "Thai Fusion",   "stars": 4.20, "reviews_count": 470, "price": 450,  "capacity": 45,  "distance": 14, "score": 86.2},
    {"rank": 21, "name": "Bo.lan",                         "area": "Sukhumvit 53",  "cuisine": "Thai Fine",     "stars": 4.40, "reviews_count": 920, "price": 1800, "capacity": 30,  "distance": 22, "score": 85.8},
    {"rank": 22, "name": "Paste Bangkok",                  "area": "Gaysorn",       "cuisine": "Thai Fine",     "stars": 4.35, "reviews_count": 680, "price": 1200, "capacity": 35,  "distance": 20, "score": 85.4},
    {"rank": 23, "name": "Indus Restaurant",               "area": "Sukhumvit 26",  "cuisine": "Indian",        "stars": 4.10, "reviews_count": 350, "price": 450,  "capacity": 50,  "distance": 15, "score": 84.9},
    {"rank": 24, "name": "Biscotti",                       "area": "Ploenchit",     "cuisine": "Italian",       "stars": 4.05, "reviews_count": 420, "price": 800,  "capacity": 60,  "distance": 22, "score": 84.3},
    {"rank": 25, "name": "Vientiane Kitchen",              "area": "Ekkamai",       "cuisine": "Lao/Thai",      "stars": 4.15, "reviews_count": 560, "price": 300,  "capacity": 70,  "distance": 20, "score": 83.9},
]

def stars_html(n):
    filled = "★" * int(n) + ("½" if n % 1 >= 0.5 else "")
    return f'<span style="color:#f59e0b">{filled}</span> {n}'

def review_card(rv):
    stars_str = "★" * rv['rating'] + "☆" * (5 - rv['rating'])
    return f"""
      <div class="review-card">
        <div class="review-header">
          <span class="review-stars">{stars_str}</span>
          <span class="review-meta">{rv['author']} &middot; {rv['date']} &middot; <em>{rv['source']}</em></span>
        </div>
        <p class="review-text">"{rv['text']}"</p>
      </div>"""

def review_section(r):
    cards = "".join(review_card(rv) for rv in r["reviews"])
    emoji = "🏆" if r["rank"] == 1 else f"#{r['rank']}"
    return f"""
  <div class="rest-section">
    <div class="rest-header">
      <span class="rest-rank">{emoji}</span>
      <h3>{r['name']}</h3>
      <span class="rest-score">{r['score']}/100</span>
    </div>
    <div class="reviews-list">{cards}
    </div>
  </div>"""

def top5_card(r):
    bar_w = int(r['score'])
    medal = ["🥇","🥈","🥉","4️⃣","5️⃣"][r['rank']-1]
    score_color = "#10b981" if r['rank'] == 1 else "#3b82f6" if r['rank'] <= 3 else "#6b7280"
    return f"""
    <div class="top5-card">
      <div class="top5-medal">{medal}</div>
      <div class="top5-info">
        <div class="top5-name">{r['name']}</div>
        <div class="top5-meta">{r['area']} | {r['cuisine']} | ⭐{r['stars']} ({r['reviews_count']:,} reviews) | ฿{r['price']}/head</div>
        <div class="score-bar-bg"><div class="score-bar-fill" style="width:{bar_w}%;background:{score_color}"></div></div>
      </div>
      <div class="top5-score" style="color:{score_color}">{r['score']}</div>
    </div>"""

def ranking_row(r):
    medal = "🏆" if r['rank'] == 1 else ("🥈" if r['rank'] == 2 else ("🥉" if r['rank'] == 3 else str(r['rank'])))
    score_cls = "score-high" if r['score'] >= 92 else ("score-mid" if r['score'] >= 88 else "score-low")
    return f"""    <tr>
      <td class="td-rank">{medal}</td>
      <td class="td-name">{r['name']}</td>
      <td>{r['area']}</td>
      <td>{r['cuisine']}</td>
      <td>⭐ {r['stars']}</td>
      <td>{r['reviews_count']:,}</td>
      <td>฿{r['price']}</td>
      <td>{r['capacity']}</td>
      <td>{r['distance']} min</td>
      <td class="{score_cls}">{r['score']}</td>
    </tr>"""

reviews_sections = "".join(review_section(r) for r in restaurants)
top5_cards = "".join(top5_card(r) for r in FULL_RANKING[:5])
ranking_rows = "".join(ranking_row(r) for r in FULL_RANKING)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Team Dinner Restaurant Selection - Bangkok</title>
<style>
:root{{--gold:#f59e0b;--green:#10b981;--blue:#3b82f6;--bg:#f8fafc;--card:#fff;--border:#e2e8f0;--text:#1e293b;--muted:#64748b;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;}}
.header{{background:linear-gradient(135deg,#1e293b,#334155);color:#fff;padding:40px 32px;text-align:center;}}
.header h1{{font-size:2rem;font-weight:800;margin-bottom:6px;}}
.header p{{opacity:.8;font-size:.95rem;}}
.update-bar{{background:#f0fdf4;border-bottom:1px solid #bbf7d0;text-align:center;padding:10px;font-size:.85rem;color:#166534;}}
.update-bar span{{font-weight:700;}}
.container{{max-width:1000px;margin:0 auto;padding:32px 20px;}}
.section-title{{font-size:1.15rem;font-weight:700;margin:32px 0 16px;padding-bottom:8px;border-bottom:2px solid var(--border);color:var(--text);}}

/* Hero */
.hero{{background:linear-gradient(135deg,#065f46,#047857);color:#fff;border-radius:16px;padding:28px;margin-bottom:32px;position:relative;overflow:hidden;}}
.hero-bg-score{{font-size:8rem;font-weight:900;opacity:.08;position:absolute;right:16px;top:-10px;line-height:1;}}
.hero-label{{font-size:.75rem;text-transform:uppercase;letter-spacing:.1em;opacity:.8;margin-bottom:6px;}}
.hero h2{{font-size:1.7rem;font-weight:800;margin-bottom:6px;}}
.hero-meta{{opacity:.9;font-size:.9rem;margin-bottom:4px;}}
.hero-badge{{display:inline-block;background:rgba(255,255,255,.15);border-radius:6px;padding:5px 12px;font-size:.85rem;margin-top:10px;}}
.map-btn{{display:inline-block;margin-top:12px;background:#fff;color:#065f46;padding:8px 18px;border-radius:8px;text-decoration:none;font-weight:700;font-size:.85rem;margin-left:8px;}}

/* Top 5 Cards */
.top5-card{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px;margin-bottom:12px;display:flex;align-items:center;gap:14px;}}
.top5-medal{{font-size:1.8rem;width:40px;text-align:center;flex-shrink:0;}}
.top5-info{{flex:1;}}
.top5-name{{font-weight:700;font-size:1rem;margin-bottom:3px;}}
.top5-meta{{font-size:.8rem;color:var(--muted);margin-bottom:6px;}}
.score-bar-bg{{background:#e2e8f0;border-radius:4px;height:6px;overflow:hidden;}}
.score-bar-fill{{height:100%;border-radius:4px;transition:width .6s;}}
.top5-score{{font-size:1.5rem;font-weight:900;min-width:55px;text-align:right;}}

/* Full Ranking Table */
.table-wrap{{overflow-x:auto;border-radius:10px;border:1px solid var(--border);}}
table{{width:100%;border-collapse:collapse;background:var(--card);font-size:.85rem;}}
thead{{background:#f1f5f9;}}
th{{padding:10px 12px;text-align:left;font-weight:600;color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap;}}
td{{padding:10px 12px;border-top:1px solid var(--border);}}
tr:hover{{background:#f8fafc;}}
.td-rank{{font-size:1rem;text-align:center;}}
.td-name{{font-weight:600;}}
.score-high{{color:#10b981;font-weight:800;}}
.score-mid{{color:#3b82f6;font-weight:700;}}
.score-low{{color:#6b7280;font-weight:600;}}

/* Scoring Model */
.weights-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;}}
.weight-card{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:14px;text-align:center;}}
.weight-pct{{font-size:1.5rem;font-weight:800;color:var(--blue);}}
.weight-label{{font-size:.8rem;color:var(--muted);margin-top:2px;}}

/* Reviews */
.rest-section{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;margin-bottom:16px;}}
.rest-header{{display:flex;align-items:center;gap:10px;margin-bottom:14px;}}
.rest-rank{{font-size:1.3rem;}}
.rest-header h3{{flex:1;font-size:1rem;font-weight:700;}}
.rest-score{{font-size:1rem;font-weight:800;color:var(--green);}}
.review-card{{border-left:3px solid var(--gold);padding:8px 12px;margin-bottom:8px;background:#fffbeb;border-radius:0 6px 6px 0;}}
.review-header{{display:flex;align-items:center;gap:8px;margin-bottom:3px;flex-wrap:wrap;}}
.review-stars{{color:var(--gold);font-size:.95rem;}}
.review-meta{{font-size:.75rem;color:var(--muted);}}
.review-text{{font-size:.85rem;font-style:italic;}}

.footer{{text-align:center;padding:24px;color:var(--muted);font-size:.78rem;border-top:1px solid var(--border);margin-top:16px;}}
</style>
</head>
<body>

<div class="header">
  <h1>🍽️ Team Dinner Restaurant Selection</h1>
  <p>Data-driven ranking across 25 qualifying venues in Bangkok</p>
</div>

<div class="update-bar">⏱ Reviews auto-updated every hour &nbsp;|&nbsp; Last update: <span>{updated_at}</span></div>

<div class="container">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-bg-score">94.9</div>
    <div class="hero-label">🏆 Top Pick — Score 94.9 / 100</div>
    <h2>Park Sathorn Restaurant</h2>
    <p class="hero-meta">📍 Sathorn &nbsp;|&nbsp; Thai Cuisine &nbsp;|&nbsp; ⭐ 4.45 (575 reviews)</p>
    <p class="hero-meta">🚗 7 min from office &nbsp;|&nbsp; 👥 Seats up to 50 &nbsp;|&nbsp; 💰 ฿400/head</p>
    <span class="hero-badge">🌿 Garden · Waterfall · Live Dance Show</span>
    <a href="https://www.google.com/maps/search/?api=1&query=13.719795,100.551228" target="_blank" class="map-btn">📍 View on Map</a>
  </div>

  <!-- TOP 5 -->
  <div class="section-title">🥇 Top 5 Shortlist</div>
  {top5_cards}

  <!-- FULL RANKING -->
  <div class="section-title">📋 Full Ranking — All 25 Restaurants</div>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Restaurant</th>
          <th>Area</th>
          <th>Cuisine</th>
          <th>Rating</th>
          <th>Reviews</th>
          <th>Price/head</th>
          <th>Capacity</th>
          <th>Distance</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>
{ranking_rows}
      </tbody>
    </table>
  </div>

  <!-- SCORING MODEL -->
  <div class="section-title">⚖️ Scoring Model Weights</div>
  <div class="weights-grid">
    <div class="weight-card"><div class="weight-pct">35%</div><div class="weight-label">Customer Rating</div></div>
    <div class="weight-card"><div class="weight-pct">20%</div><div class="weight-label">Group Suitability</div></div>
    <div class="weight-card"><div class="weight-pct">20%</div><div class="weight-label">Value for Money</div></div>
    <div class="weight-card"><div class="weight-pct">15%</div><div class="weight-label">Distance from Office</div></div>
    <div class="weight-card"><div class="weight-pct">10%</div><div class="weight-label">Review Volume</div></div>
  </div>

  <!-- LATEST REVIEWS -->
  <div class="section-title">💬 Latest Reviews — Top 3 Shortlist <small style="font-weight:400;color:var(--muted);font-size:.8rem">Auto-updated hourly</small></div>
  {reviews_sections}

</div>

<div class="footer">Auto-updated hourly via GitHub Actions &nbsp;|&nbsp; Sources: TripAdvisor + Google &nbsp;|&nbsp; 2026</div>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html generated successfully")
