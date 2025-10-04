import json
from datetime import datetime, timedelta

# Simulated fixture data for demonstration
fixtures = [
    {
        "date": "2024-04-01",
        "league": "Premier League",
        "home_team": "Arsenal",
        "away_team": "Chelsea",
        "time_utc": "14:00",
        "home_logo": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
        "away_logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
        "predicted_score": "2 - 1",
        "odds": {"home": 1.85, "draw": 3.4, "away": 4.2}
    }
]

# Save to fixtures.json
with open("fixtures.json", "w") as f:
    json.dump(fixtures, f, indent=4)
