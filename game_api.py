
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("SUPERCELL_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def fetch_cr_stats(tag):
    tag = tag.strip("#").upper()
    url = f"https://api.clashroyale.com/v1/players/%23{tag}"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        raise Exception("Clash Royale: Invalid tag or error")
    data = res.json()

    cards_url = f"https://api.clashroyale.com/v1/players/%23{tag}/cards"
    cards_res = requests.get(cards_url, headers=HEADERS)
    cards = cards_res.json().get("items", []) if cards_res.status_code == 200 else []

    elite = sum(1 for c in cards if c.get("maxLevel") == 15 and c.get("level") == 15)
    maxed = sum(1 for c in cards if c.get("level") == c.get("maxLevel"))

    return {
        "level": data.get("expLevel", 0),
        "trophies": data.get("trophies", 0),
        "emotes": 128,
        "gems": 2500,
        "king_tower": data.get("expLevel", 0),
        "elite_cards": elite,
        "max_cards": maxed
    }

def fetch_coc_stats(tag):
    tag = tag.strip("#").upper()
    url = f"https://api.clashofclans.com/v1/players/%23{tag}"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        raise Exception("Clash of Clans: Invalid tag or error")
    data = res.json()

    return {
        "townHallLevel": data.get("townHallLevel", 0),
        "trophies": data.get("trophies", 0),
        "warStars": data.get("warStars", 0),
        "expLevel": data.get("expLevel", 0),
        "clanName": data.get("clan", {}).get("name", "No Clan")
    }

def fetch_bs_stats(tag):
    tag = tag.strip("#").upper()
    url = f"https://api.brawlstars.com/v1/players/%23{tag}"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        raise Exception("Brawl Stars: Invalid tag or error")
    data = res.json()

    return {
        "trophies": data.get("trophies", 0),
        "highestTrophies": data.get("highestTrophies", 0),
        "brawlersUnlocked": len(data.get("brawlers", [])),
        "totalBrawlers": 72,
        "clubName": data.get("club", {}).get("name", "No Club")
    }
