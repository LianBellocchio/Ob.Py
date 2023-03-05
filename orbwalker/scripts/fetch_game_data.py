import requests
import json
import os

API_KEY = "RGAPI-1d987440-b6fc-49ae-81e3-fc9ecd73a070"

BASE_URL = "https://na1.api.riotgames.com/lol/"

def get_champions():
    url = f"{BASE_URL}champions"
    response = requests.get(url, params={"api_key": API_KEY})
    champions = json.loads(response.text)["data"]
    return champions

def get_items():
    url = f"{BASE_URL}items"
    response = requests.get(url, params={"api_key": API_KEY})
    items = json.loads(response.text)["data"]
    return items

def get_spells():
    url = f"{BASE_URL}summoner-spells"
    response = requests.get(url, params={"api_key": API_KEY})
    spells = json.loads(response.text)["data"]
    return spells

def get_game_data():
    champions = get_champions()
    items = get_items()
    spells = get_spells()

    game_data = {
        "champions": champions,
        "items": items,
        "spells": spells
    }

    return game_data

if __name__ == "__main__":
    game_data = get_game_data()

    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")

    # Save game data to file
    with open("data/game_data.json", "w") as outfile:
        json.dump(game_data, outfile)

    print("Game data fetched and saved successfully.")
