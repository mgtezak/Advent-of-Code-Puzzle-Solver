# Native
import json
from pathlib import Path

# Local
from config import TEMP_STORAGE
from base import get_session_id
from .handle_puzzle_data import get_puzzle_dir_path



def get_temp_inp_path() -> Path:
    """Get path for storing temporary inputs, based on the users unique session id."""

    return TEMP_STORAGE / f'{get_session_id()}.json'



def get_puzzle_id(year: int, day: int) -> str:
    """Combine year and day into a single indentifier."""

    return str(year*100 + day)



def get_temp_puzzle_input_db() -> dict:
    """Returns temporary puzzle inputs as dictionary."""

    path = get_temp_inp_path()
    try:
        return json.loads(path.read_text())
    except:
        return {}  

    

def get_temp_puzzle_input(year: int, day: int) -> str | None:
    """Fetches a single puzzle input as string."""

    puzzle_id = str(year*100 + day)
    db = get_temp_puzzle_input_db()
    return db.get(puzzle_id, False)



def put_temp_puzzle_input(year: int, day: int, puzzle_input: str) -> None:
    """Inserts a single puzzle input into database."""

    puzzle_id = get_puzzle_id(year, day)
    path = get_temp_inp_path()

    db = get_temp_puzzle_input_db()
    db[puzzle_id] = puzzle_input
    with path.open('w') as f:
        json.dump(db, f, indent=4)



def del_temp_puzzle_input(year: int, day: int) -> None:
    """Overwrites puzzle input entry with empty string."""

    puzzle_id = get_puzzle_id(year, day)
    db = get_temp_puzzle_input_db()
    if db.get(puzzle_id, False):
        del db[puzzle_id]



def get_my_puzzle_input(year: int, day: int) -> str:
    """Fetches a single puzzle input as string."""

    path = get_puzzle_dir_path(year, day) / 'my_input.txt'
    return path.read_text()
    


def get_example_inputs(year: int, day: int) -> list[tuple[str, int]]:
    """Retrieves example inputs for a given puzzle."""

    path = get_puzzle_dir_path(year, day) / 'example_input.json'
    if path.exists():
        return json.loads(path.read_text())
    return []



def is_example_input(year: int, day: int, puzzle_input: str | None = None) -> bool:
    """Checks whether a given puzzle input is part of the example inputs."""
    
    if puzzle_input is None:
        puzzle_input = get_temp_puzzle_input(year, day)

    example_inputs = get_example_inputs(year, day)
    if example_inputs:
        if type(example_inputs[0]) == list:
            return puzzle_input in [item[0] for item in example_inputs]
        return puzzle_input in [item['input'] for item in example_inputs]
    else:
        return False