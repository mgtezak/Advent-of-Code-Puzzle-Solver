# Third party
import pandas as pd

# Native
import json
import os

# Local
from config import PUZZLE_INPUT, SOLUTION, GRID_LETTER, TITLE



# PUZZLE INPUT DB
def get_puzzle_input_db() -> dict:
    """Returns all puzzle inputs as dictionary."""

    try:
        with open(PUZZLE_INPUT, 'r') as f:
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
    with open(PUZZLE_INPUT, 'w') as f:
        json.dump(db, f, indent=4)



def del_puzzle_input(year: int, day: int) -> None:
    """Overwrites puzzle input entry with empty string."""

    return put_puzzle_input(year, day, '')



# SOLUTION DB
def get_solution_db() -> pd.DataFrame:
    """Returns all solutions as pandas dataframe."""

    columns = ['id', 'year', 'day', 'part', 'solution', 'runtime']
    dtypes = [int, int, int, int, object, float]

    if not os.path.exists(SOLUTION):
        pd.DataFrame(columns=columns).to_csv(SOLUTION, index=False)
    
    return pd.read_csv(SOLUTION, dtype=dict(zip(columns, dtypes)))



def get_solution(year: int, day: int, part: int) -> tuple[str, float] | None:
    """Fetches a single solution & runtime string tuple from database ."""

    df = get_solution_db()

    row = df[df.id == int(f'{year}{day:02}{part}')]
    if len(row) == 0:
        return None
    
    solution, runtime = row.iloc[0, [4, 5]].values
    return solution, runtime 



def put_solution(year: int, day: int, part: int, solution: str, runtime: float) -> None:
    """Stores away a single solution. Will overwrite if necessary."""

    new_entry = pd.DataFrame([dict(id=f'{year}{day:02}{part}', year=year, day=day, part=part, solution=str(solution), runtime=runtime)])
    df = get_solution_db()
    if len(df) == 0:
        df = new_entry
    else:
        df = pd.concat([df, new_entry], axis=0, ignore_index=True)
    df.to_csv(SOLUTION, index=False)



def del_solution(year: int, day: int) -> None:
    """Removes a single solution entry from the database."""

    df = get_solution_db()
    df = df[~((df.year==year) & (df.day==day))]
    df.to_csv(SOLUTION, index=False)



# GRID LETTER DB
def get_grid_letter_db() -> dict[str: str]:
    """Returns the grid letter translation dictionary."""

    try:
        with open(GRID_LETTER, 'r') as f:
            db = json.load(f)
    except:
        db = {}

    return db



def put_grid_letter(grid, letter) -> None:
    """Inserts a single grid letter entry."""

    db = get_grid_letter_db()
    db[grid] = letter.upper()
    with open(GRID_LETTER, 'w') as f:
        json.dump(db, f, indent=4)



# TITLE DB
def get_title_db() -> pd.DataFrame:
    """Returns all titles as pandas dataframe."""

    if not os.path.exists(TITLE):
        pd.DataFrame(columns=['year', 'day', 'title']).to_csv(TITLE, index=False)

    return pd.read_csv(TITLE)



def get_title(year, day) -> str:
    """Fetches a single puzzle title from database."""

    df = get_title_db()
    row = df.loc[(df.year==year) & (df.day==day), 'title']
    if len(row) == 0:
        return ''
    
    return row.iloc[0]