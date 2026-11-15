import json
from pathlib import Path

ROOMS_PATH = Path(__file__).parent.parent / "DATA/rooms.json"
BOOKINGS_PATH = Path(__file__).parent.parent / "DATA/bookings.json"


def load_data(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []
    except (UnicodeDecodeError, json.decoder.JSONDecodeError):
        raise

def load_rooms():
    return load_data(ROOMS_PATH)

def load_bookings():
    return load_data(BOOKINGS_PATH)
