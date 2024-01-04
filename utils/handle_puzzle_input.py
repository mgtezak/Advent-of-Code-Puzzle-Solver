# Native
import json
import os

# Local
from config import TEMP
from base import get_session_id



def get_temp_pi_path():
    return f'{TEMP}/{get_session_id()}.json'



def get_my_pi_path(year, day):
    return f'advent_of_code/y{year}/d{day:02}/example_input.json'



def get_puzzle_id(year, day):
    return str(year*100 + day)



def get_temp_puzzle_input_db() -> dict:
    """Returns temporary puzzle inputs as dictionary."""

    path = get_temp_pi_path()
    
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}  

    

def get_temp_puzzle_input(year: int, day: int) -> str | None:
    """Fetches a single puzzle input as string."""

    puzzle_id = str(year*100 + day)
    db = get_temp_puzzle_input_db()
    return db.get(puzzle_id, False)



def put_temp_puzzle_input(year: int, day: int, puzzle_input: str) -> None:
    """Inserts a single puzzle input into database."""

    puzzle_id = get_puzzle_id(year, day)
    path = get_temp_pi_path()

    db = get_temp_puzzle_input_db()
    db[puzzle_id] = puzzle_input
    with open(path, 'w') as f:
        json.dump(db, f, indent=4)



def del_temp_puzzle_input(year: int, day: int) -> None:
    """Overwrites puzzle input entry with empty string."""

    puzzle_id = get_puzzle_id(year, day)
    db = get_temp_puzzle_input_db()
    if db.get(puzzle_id, False):
        del db[puzzle_id]



def get_my_puzzle_input(year: int, day: int) -> str:
    """Fetches a single puzzle input as string."""

    path = f'advent_of_code/y{year}/d{day:02}/my_input.txt'
    with open(path, 'r') as f:
        return f.read()
    


def get_example_inputs(year, day):
    """"""

    path = get_my_pi_path(year, day)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
        
    return {}


def is_example_input(year: int, day: int, puzzle_input: str|None = None) -> bool:
    """"""
    
    if puzzle_input is None:
        puzzle_input = get_temp_puzzle_input(year, day)

    example_inputs = get_example_inputs(year, day).values()
    if example_inputs:
        return puzzle_input in list(zip(*example_inputs))[0]
    else:
        return False