#!/usr/bin/env python3
import json
from pathlib import Path

with open("reviews.json", encoding="utf-8") as f:
    data = json.load(f)

updated_at = data["updated_at"]
restaurants = data["restaurants"]

def stars(n):
    return "★" * n + "☆" * (5 - n)

def review_card(rv):
    return f"""
      <div class="review-card">
        <div class="review-header">
          <span class="review-stars">{stars(rv['rating'])}</span>
          <span class="review-meta">{rv['author']} · {rv['date']} · <em>{rv['source']}</em></span>
        </div>
        <p class="review-text">"{rv['text']}"</p>
      </div>"""

def restaurant_section(r):
    cards = "".join(review_card(rv) for rv in r["reviews"])
    emoji = "🏆&�" if r['rank'] == 1 else f"#{r['rank']}"
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

sections = "".join(restaurant_section(r) for r in restaurants)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Team Dinner Restaurant Selection — Bangkok</title>
<style>
  :root {{ --gold:#f59e0b; --green:#10b981; --blue:#3b82f6; --bg:#f8fafc; --card:#fff; --border:#e2e8f0; --text:#1e293b; --muted:#64748b; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }}
  .header {{ background:linear-gradient(135deg,#1e293b,#334155); color:#fff; padding:48px 32px 40px; text-align:center; }}
  .header h1 {{ font-size:2rem; font-weight:700; margin-bottom:8px; }}
  .pills {{ display:flex; justify-content:center; gap:10px; margin-top:16px; flex-wrap:wrap; }}
  .pill {{ background:rgba(255,255,255,.15); border-radius:999px; padding:4px 14px; font-size:.82rem; }}
  .update-bar {{ background:#f0fdf4; border-bottom:1px solid #bbf7d0; text-align:center; padding:8px; font-size:.82rem; color:#166534; }}
  .update-bar span {{ font-weight:600; }}
  .container {{ max-width:900px; margin:0 auto; padding:32px 20px; }}
  .section-title {{ font-size:1.2rem; font-weight:700; margin-bottom:20px; padding-bottom:8px; border-bottom:2px solid var(--border); }}
  .hero {{ background:linear-gradient(135deg,#065f46,#047857); color:#fff; border-radius:16px; padding:28px; margin-bottom:32px; position:relative; }}
  .hero-label {{ font-size:.8rem; font-weight:600; letter-spacing:.1em; text-transform:uppercase; opacity:.8; margin-bottom:6px; }}
  .hero h2 {{ font-size:1.7rem; font-weight:800; margin-bottom:6px; }}
  .hero-meta {{ opacity:.9; font-size:.92rem; margin-bottom:10px; }}
  .hero-score {{ font-size:3rem; font-weight:900; opacity:.12; position:absolute; right:28px; top:20px; }}
  .hero-sig {{ background:rgba(255,255,255,.15); border-radius:8px; padding:8px 12px; font-size:.88rem; display:inline-block; margin-top:8px; }}
  .map-btn {{ display:inline-block; margin-top:14px; background:#fff; color:#065f46; padding:8px 18px; border-radius:8px; text-decoration:none; font-weight:600; font-size:.88rem; }}
  .rest-section {{ background:var(--card); border:1px solid var(--border); border-radius:12px; padding:20px; margin-bottom:20px; }}
  .rest-header {{ display:flex; align-items:center; gap:12px; margin-bottom:16px; }}
  .rest-rank {{ font-size:1.4rem; }}
  .rest-header h3 {{ flex:1; font-size:1.05rem; font-weight:700; }}
  .rest-score {{ font-size:1.1rem; font-weight:800; color:var(--green); }}
  .review-card {{ border-left:3px solid var(--gold); padding:10px 14px; margin-bottom:10px; background:#fffbeb; border-radius:0 8px 8px 0; }}
  .review-header {{ display:flex; align-items:center; gap:10px; margin-bottom:4px; flex-wrap:wrap; }}
  .review-stars {{ color:var(--gold); font-size:1rem; letter-spacing:1px; }}
  .review-meta {{ font-size:.78rem; color:var(--muted); }}
  .review-text {{ font-size:.88rem; color:var(--text); font-style:italic; }}
  .footer {{ text-align:center; padding:24px; color:var(--muted); font-size:.8rem; border-top:1px solid var(--border); margin-top:20px; }}
</style>
</head>
<body>
<div class="header">
  <h1>🍜 Team Dinner Restaurant Selection</h1>
  <p>Bangkok · Data-driven ranking across 25 qualifying venues</p>
  <div class="pills">
    <span class="pill">👥 Team of 10</span>
    <span class="pill">📍 Base: Office – Asok</span>
    <span class="pill">💰 Mid-range target</span>
    <span class="pill">🔢 2 sources · 100-pt model</span>
  </div>
</div>
<div class="update-bar">🔄 Pull from TripAdvisor hourly via GitHub Actions · Last update: <span>{updated_at}</span></div>
<div class="container">
  <div class="hero">
    <div class="hero-score">94.9</div>
    <div class="hero-label">🏆 Top Pick — Score 94.9/100</div>
    <h2>Park Sathorn Restaurant</h2>
    <p class="hero-meta">📍 Sathorn · 🍽 Thai · ⭐ 4.45 (575 reviews)</p>
    <p class="hero-meta">🕒 7 min from office · 👥 Seats up to 50 · ฿400/head · ฿฿</p>
    <div class="hero-sig">✨ Garden, waterfall & dance show</div><br>
    <a href="https://www.google.com/maps/search/?api=1&query=13.719795,100.551228" target="_blank" class="map-btn">📍 View on Map</a>
  </div>
  <div class="section-title">💬 Latest Reviews — Top 3 Shortlist</div>
  {sections}
</div>
<div class="footer">Auto-updated hourly via GitHub Actions · Sources: TripAdvisor++ · 2026</div>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html generated")
