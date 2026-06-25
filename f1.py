import requests
from datetime import datetime

url = "https://api.openf1.org/v1/sessions?year=2026"

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

next_race = None

user_date = input("Enter date (YYYY-MM-DD): ")
user_date = datetime.strptime(user_date, "%Y-%m-%d")

for session in data:
    session_date = datetime.fromisoformat(session["date_start"])
    if session_date.date() > datetime.now().date() and session["session_type"] == "Race":
        next_race = session
        break



print(f"Next race: {next_race['country_name']} on {datetime.fromisoformat(next_race['date_start']).date()}")