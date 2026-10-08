from datetime import date
from pathlib import Path


def is_valid_date(date_text):
    try:
        return date.fromisoformat(date_text).isoformat() == date_text
    except ValueError:
        return False


def save_entry(file_name, date_text, entry_text):
    with Path(file_name).open("a", encoding="utf-8") as diary_file:
        diary_file.write(f"{date_text}|{entry_text}\n")


def find_entries(file_name, date_text):
    path = Path(file_name)

    if not path.exists():
        return []

    matches = []

    with path.open("r", encoding="utf-8") as diary_file:
        for line in diary_file:
            saved_date, separator, entry_text = (
                line.rstrip("\n").partition("|")
            )

            if separator and saved_date == date_text:
                matches.append(entry_text)

    return matches