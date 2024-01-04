# Native
import json
import os

# Local
from config import TEMP_PUZZLE_INPUT



def get_temp_puzzle_input_db() -> dict:
    """Returns all puzzle inputs as dictionary."""

    try:
        with open(TEMP_PUZZLE_INPUT, 'r') as f:
            db = json.load(f)
    except:
        db = {}
        
    return db
    


def get_temp_puzzle_input(year: int, day: int) -> str | None:
    """Fetches a single puzzle input as string."""

    year, day = str(year), str(day)
    db = get_temp_puzzle_input_db()

    if not db.get(year, False):
        return None
    
    return db[year].get(day, False)



def put_temp_puzzle_input(year: int, day: int, puzzle_input: str) -> None:
    """Inserts a single puzzle input into database."""

    year, day = str(year), str(day)

    db = get_temp_puzzle_input_db()
    if not db.get(year, False):
        db[year] = {}

    db[year][day] = puzzle_input
    with open(TEMP_PUZZLE_INPUT, 'w') as f:
        json.dump(db, f, indent=4)



def del_temp_puzzle_input(year: int, day: int) -> None:
    """Overwrites puzzle input entry with empty string."""

    db = get_temp_puzzle_input_db()
    if db.get(year, False) and  db[year].get(day, False):
        del db[year][day]

    return put_temp_puzzle_input(year, day, '')



def get_my_puzzle_input(year: int, day: int) -> str:
    """Fetches a single puzzle input as string."""

    path = f'advent_of_code/y{year}/d{day:02}/my_input.txt'
    with open(path, 'r') as f:
        return f.read()
    


def get_example_inputs(year, day):
    """"""

    path = f'advent_of_code/y{year}/d{day:02}/example_input.json'
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
        
    return []


def is_example_input(year: int, day: int, puzzle_input: str|None = None) -> bool:
    """"""
    
    if puzzle_input is None:
        puzzle_input = get_temp_puzzle_input(year, day)

    example_inputs = get_example_inputs(year, day).values()
    return puzzle_input in list(zip(*example_inputs))[0]