# -*- coding: utf-8 -*-
import json

with open("reviews.json", encoding="utf-8") as f:
    data = json.load(f)

updated_at = data["updated_at"]
restaurants = data["restaurants"]

def stars(n):
    return "\u2605" * n + "\u2606" * (5 - n)

def review_card(rv):
    return f"""
      <div class=\"review-card\">
        <div class=\"review-header\">
          <span class=\"review-stars\">{stars(rv['rating'])}</span>
          <span class=\"review-meta\">{rv['author']} &middot; {rv['date']} &middot; <em>{rv['source']}</em></span>
        </div>
        <p class=\"review-text\">\"{rv['text']}\"</p>
      </div>"""

def restaurant_section(r):
    cards = "".join(review_card(rv) for rv in r["reviews"])
    emoji = "&#127942;" if r["rank"] == 1 else f"#{r['rank']}"
    return f"""
  <div class=\"rest-section\">
    <div class=\"rest-header\">
      <span class=\"rest-rank\">{emoji}</span>
      <h3>{r['name']}</h3>
      <span class=\"rest-score\">{r['score']}/100</span>
    </div>
    <div class=\"reviews-list\">{cards}
    </div>
  </div>"""

sections = "".join(restaurant_section(r) for r in restaurants)

html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"UTF-8\">
<title>Team Dinner Restaurant Selection</title>
<style>
:root{{--gold:#f59e0b;--green:#10b981;--bg:#f8fafc;--card:#fff;--border:#e2e8f0;--text:#1e293b;--muted:#64748b;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;}}
.header{{background:linear-gradient(135deg,#1e293b,#334155);color:#fff;padding:40px 32px;text-align:center;}}
.header h1{{font-size:1.8rem;font-weight:700;margin-bottom:6px;}}
.update-bar{{background:#f0fdf4;border-bottom:1px solid #bbf7d0;text-align:center;padding:8px;font-size:.82rem;color:#166534;}}
.update-bar span{{font-weight:700;}}
.container{{max-width:900px;margin:0 auto;padding:32px 20px;}}
.section-title{{font-size:1.1rem;font-weight:700;margin-bottom:16px;padding-bottom:6px;border-bottom:2px solid var(--border);}}
.hero{{background:linear-gradient(135deg,#065f46,#047857);color:#fff;border-radius:14px;padding:24px;margin-bottom:28px;position:relative;}}
.hero h2{{font-size:1.5rem;font-weight:800;margin-bottom:4px;}}
.hero-meta{{opacity:.9;font-size:.9rem;margin-bottom:8px;}}
.hero-score{{font-size:3rem;font-weight:900;opacity:.12;position:absolute;right:24px;top:16px;}}
.map-btn{{display:inline-block;margin-top:12px;background:#fff;color:#065f46;padding:7px 16px;border-radius:8px;text-decoration:none;font-weight:600;font-size:.85rem;}}
.rest-section{{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:18px;margin-bottom:16px;}}
.rest-header{{display:flex;align-items:center;gap:10px;margin-bottom:14px;}}
.rest-rank{{font-size:1.3rem;}}
.rest-header h3{{flex:1;font-size:1rem;font-weight:700;}}
.rest-score{{font-size:1rem;font-weight:800;color:var(--green);}}
.review-card{{border-left:3px solid var(--gold);padding:8px 12px;margin-bottom:8px;background:#fffbeb;border-radius:0 6px 6px 0;}}
.review-header{{display:flex;align-items:center;gap:8px;margin-bottom:3px;flex-wrap:wrap;}}
.review-stars{{color:var(--gold);font-size:.95rem;}}
.review-meta{{font-size:.75rem;color:var(--muted);}}
.review-text{{font-size:.85rem;color:var(--text);font-style:italic;}}
.footer{{text-align:center;padding:20px;color:var(--muted);font-size:.78rem;border-top:1px solid var(--border);margin-top:16px;}}
</style>
</head>
<body>
<div class=\"header\"><h1>Team Dinner Restaurant Selection - Bangkok</h1><p>Data-driven ranking across 25 qualifying venues</p></div>
<div class=\"update-bar\">Reviews auto-updated every hour. Last update: <span>{updated_at}</span></div>
<div class=\"container\">
<div class=\"hero\">
  <div class=\"hero-score\">94.9</div>
  <div style=\"font-size:.8rem;opacity:.8;text-transform:uppercase;letter-spacing:.1em;margin-bottom:4px\">Top Pick - Score 94.9/100</div>
  <h2>Park Sathorn Restaurant</h2>
  <p class=\"hero-meta\">Sathorn | Thai | 4.45 stars (575 reviews)</p>
  <p class=\"hero-meta\">7 min from office | Seats up to 50 | 400 THB/head</p>
  <p style=\"background:rgba(255,255,255,.15);border-radius:6px;padding:6px 10px;font-size:.85rem;display:inline-block;margin-top:6px\">Garden, waterfall and dance show</p><br>
  <a href=\"https://www.google.com/maps/search/?api=1&query=13.719795,100.551228\" target=\"_blank\" class=\"map-btn\">View on Map</a>
</div>
<div class=\"section-title\">Latest Reviews - Top 3 Shortlist</div>
{sections}
</div>
<div class=\"footer\">Auto-updated hourly via GitHub Actions | Sources: TripAdvisor + Google | 2026</div>
</body></html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html generated")
