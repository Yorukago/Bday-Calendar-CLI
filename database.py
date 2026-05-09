import json
import os
from datetime import datetime

FILENAME = os.path.expanduser("~/.local/share/bday/birthdays.json")


def _ensure_file():
    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        with open(FILENAME, "w") as f:
            json.dump({}, f)


def load_data() -> dict:
    _ensure_file()
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_data(data: dict):
    _ensure_file()
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)


def add_person(name: str, birthday: str, wishlist: str, likes: str) -> tuple[bool, str]:
    try:
        datetime.strptime(birthday, "%d-%m-%Y")
    except ValueError:
        return False, f"'{birthday}' isn't a valid date! Use DD-MM-YYYY."

    data = load_data()
    key = name.lower()

    if key in data:
        return False, f"'{name}' already exists! Use 'bday edit {name}' to update them."

    data[key] = {
        "name": name,
        "birthday": birthday,
        "wishlist": wishlist,
        "likes": likes,
    }
    save_data(data)
    return True, f"Added {name} 🎂"


def remove_person(name: str) -> tuple[bool, str]:
    data = load_data()
    key = name.lower()
    if key not in data:
        return False, f"Couldn't find '{name}'."
    del data[key]
    save_data(data)
    return True, f"Removed {name}."


def search_person(name: str) -> dict | None:
    data = load_data()
    return data.get(name.lower())


def edit_person(name: str, birthday: str | None, wishlist: str | None, likes: str | None) -> tuple[bool, str]:
    data = load_data()
    key = name.lower()
    if key not in data:
        return False, f"Couldn't find '{name}'."

    person = data[key]

    if birthday:
        try:
            datetime.strptime(birthday, "%d-%m-%Y")
        except ValueError:
            return False, f"'{birthday}' isn't a valid date! Use DD-MM-YYYY."
        person["birthday"] = birthday

    if wishlist:
        person["wishlist"] = wishlist
    if likes:
        person["likes"] = likes

    save_data(data)
    return True, f"Updated {person['name']}!"


def get_upcoming(days_ahead: int = 3) -> list[dict]:
    data = load_data()
    today = datetime.now().date()
    upcoming = []

    for person in data.values():
        try:
            bday = datetime.strptime(person["birthday"], "%d-%m-%Y").date()
        except ValueError:
            continue

        this_year = bday.replace(year=today.year)
        if this_year < today:
            this_year = bday.replace(year=today.year + 1)

        days_left = (this_year - today).days

        if days_left <= days_ahead:
            upcoming.append({**person, "days_left": days_left, "date_this_year": this_year})

    return sorted(upcoming, key=lambda x: x["days_left"])
