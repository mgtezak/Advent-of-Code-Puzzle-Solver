# Third party
import pandas as pd

# Native
import json
import os

# Local
from config import PUZZLE_INPUT, SOLUTION, GRID_LETTER


# PUZZLE INPUT DB
def get_puzzle_input_db() -> dict:
    try:
        with open(PUZZLE_INPUT, 'r') as f:
            db = json.load(f)
    except:
        db = {}
    return db
    

def get_puzzle_input(year: int, day: int) -> str | bool:
    year, day = str(year), str(day)
    db = get_puzzle_input_db()
    if not db.get(year, False):
        return False
    return db[year].get(day, False)


def put_puzzle_input(year: int, day: int, puzzle_input: str) -> None:
    year, day = str(year), str(day)
    db = get_puzzle_input_db()
    if not db.get(year, False):
        db[year] = {}
    db[year][day] = puzzle_input
    with open(PUZZLE_INPUT, 'w') as f:
        json.dump(db, f, indent=4)


# SOLUTION DB
def get_solution_db() -> pd.DataFrame:
    """Get all solutions as pandas dataframe"""
    if not os.path.exists(SOLUTION):
        pd.DataFrame(columns=['id', 'year', 'day', 'part', 'solution', 'runtime']).to_csv(SOLUTION, index=False)
    return pd.read_csv(SOLUTION)


def get_solution(year: int, day: int, part: int) -> (int, int):
    df = get_solution_db()
    row = df[df.id == int(f'{year}{day:02}{part}')]
    if len(row) == 0:
        return False
    solution = row.iloc[0, 4]
    runtime = row.iloc[0, 5]
    return solution, runtime 


def put_solution(year: int, day: int, part: int, solution: int | str, runtime: int) -> None:
    """Stores away a single solution. Will overwrite if necessary."""
    df = get_solution_db()
    new_entry = dict(id=f'{year}{day:02}{part}', year=year, day=day, part=part, solution=solution, runtime=runtime)
    df = pd.concat([df, pd.DataFrame([new_entry])], axis=0, ignore_index=True)
    df.to_csv(SOLUTION, index=False)


def del_solution(year: int, day: int) -> None:
    df = get_solution_db()
    df = df[~((df.year==year) & (df.day==day))]
    df.to_csv(SOLUTION, index=False)


# GRID LETTER DB
def get_grid_letter_db() -> dict[str: str]:
    try:
        with open(GRID_LETTER, 'r') as f:
            db = json.load(f)
    except:
        db = {}
    return db


def put_grid_letter(grid, letter) -> None:
    db = get_grid_letter_db()
    db[grid] = letter.upper()
    with open(GRID_LETTER, 'w') as f:
        json.dump(db, f, indent=4)


# TITLE DB
