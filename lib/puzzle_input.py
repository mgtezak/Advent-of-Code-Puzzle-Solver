# Native
import json

# Local
from config import PUZZLE_INPUT_DB


def get_puzzle_input_db() -> dict:
    """Returns all puzzle inputs as dictionary."""

    try:
        with open(PUZZLE_INPUT_DB, 'r') as f:
            db = json.load(f)
    except:
        db = {}
        
    return db
    


def get_puzzle_input(year: int, day: int) -> str | None:
    """Fetches a single puzzle input as string."""

    year, day = str(year), str(day)
    db = get_puzzle_input_db()

    if not db.get(year, False):
        return None
    
    return db[year].get(day, False)



def put_puzzle_input(year: int, day: int, puzzle_input: str) -> None:
    """Inserts a single puzzle input into database."""

    year, day = str(year), str(day)

    db = get_puzzle_input_db()
    if not db.get(year, False):
        db[year] = {}

    db[year][day] = puzzle_input
    with open(PUZZLE_INPUT_DB, 'w') as f:
        json.dump(db, f, indent=4)



def del_puzzle_input(year: int, day: int) -> None:
    """Overwrites puzzle input entry with empty string."""

    return put_puzzle_input(year, day, '')