# -*- coding: utf-8 -*-
import json

with open("reviews.json", encoding="utf-8") as f:
    data = json.load(f)

updated_at = data["updated_at"]
restaurants = data["restaurants"]