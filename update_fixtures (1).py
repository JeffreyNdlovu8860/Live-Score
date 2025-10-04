import requests
import json
from datetime import datetime, timedelta

# Fetch fixtures from Boggio Analytics Football Prediction API
API_URL = "https://boggio-analytics.com/api/fp_english_league_predictions"

try:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print("Failed to fetch data:", e)
    exit(1)

# Filter fixtures for the next 7 days
today = datetime.utcnow().date()
end_date = today + timedelta(days=7)
filtered_fixtures = []

for item in data:
    try:
        match_date = datetime.strptime(item["date"], "%Y-%m-%d").date()
        if today <= match_date <= end_date:
            fixture = {
                "date": item["date"],
                "league": item.get("league", "English League"),
                "home_team": item["home_team"],
                "away_team": item["away_team"],
                "time_utc": item.get("time", "TBD"),
                "home_logo": item.get("home_logo", ""),
                "away_logo": item.get("away_logo", ""),
                "predicted_score": item.get("predicted_score", "N/A"),
                "odds": {
                    "home": item.get("odds_home", "N/A"),
                    "draw": item.get("odds_draw", "N/A"),
                    "away": item.get("odds_away", "N/A")
                }
            }
            filtered_fixtures.append(fixture)
    except Exception as e:
        print("Error processing fixture:", e)

# Save to fixtures.json
with open("fixtures.json", "w") as f:
    json.dump(filtered_fixtures, f, indent=4)

print(f"Saved {len(filtered_fixtures)} fixtures to fixtures.json")
