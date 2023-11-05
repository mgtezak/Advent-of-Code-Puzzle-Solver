import json
import os
import pandas as pd

# from lib import utils, aoc


PUZZLE_INPUT_PATH = 'db/puzzle_input.json'
SOLUTION_PATH = 'db/solution.csv'
COMPLETION_PATH = 'db/completion.csv'


# PUZZLE INPUT DB
def get_puzzle_input_db():
    try:
        with open(PUZZLE_INPUT_PATH, 'r') as f:
            db = json.load(f)
    except:
        db = {}
    return db
    

def get_puzzle_input(year, day):
    year, day = str(year), str(day)
    db = get_puzzle_input_db()
    if not db.get(year, False):
        return False
    return db[year].get(day, False)


def put_puzzle_input(year, day, puzzle_input):
    year, day = str(year), str(day)
    db = get_puzzle_input_db()
    if not db.get(year, False):
        db[year] = {}
    db[year][day] = puzzle_input
    with open(PUZZLE_INPUT_PATH, 'w') as f:
        json.dump(db, f, indent=4)


# SOLUTION DB
def get_solution_db():
    """Get all solutions as pandas dataframe"""
    if not os.path.exists(SOLUTION_PATH):
        pd.DataFrame(columns=['id', 'year', 'day', 'part', 'solution', 'runtime']).to_csv(SOLUTION_PATH, index=False)
    return pd.read_csv(SOLUTION_PATH)


def get_solution(year, day, part):
    df = get_solution_db()
    row = df[df.id == int(f'{year}{day:02}{part}')]
    if len(row) == 0:
        return False
    solution = row.iloc[0, 4]
    runtime = row.iloc[0, 5]
    return solution, runtime 


def put_solution(year, day, part, solution, runtime):
    """Stores away a single solution. Will overwrite if necessary."""
    df = get_solution_db()
    new_entry = dict(id=f'{year}{day:02}{part}', year=year, day=day, part=part, solution=solution, runtime=runtime)
    df = pd.concat([df, pd.DataFrame([new_entry])], axis=0, ignore_index=True)
    df.to_csv(SOLUTION_PATH, index=False)


def del_solution(year, day):
    df = get_solution_db()
    df = df[~((df.year==year) & (df.day==day))]
    df.to_csv(SOLUTION_PATH, index=False)


def get_completed_stat():
    df = get_completion_db()
    completed = df.completed.sum()
    total = df.shape[0]
    return f"So far I've completed {completed} of the available total of {total} daily challenges."


### The following functions are necessary/useful for maintenance but not for normal use of the app
def get_completion_db():
    if not os.path.exists(COMPLETION_PATH):
        initialize_completion_db()
    return pd.read_csv(COMPLETION_PATH)


def initialize_completion_db():
    data = []
    for year in range(2015, 2023):
        for day in range(1, 26):
            data.append([year, day, 0])
    df = pd.DataFrame(data, columns=["year", "day", "completed"])
    df.to_csv(COMPLETION_PATH, index=False)


def put_completed(year, day):
    db = get_completion_db()
    db[(db.year == year) & (db.day == day)] = [year, day, 1]
    db.to_csv(COMPLETION_PATH, index=False)


# RESET
def remove_dbs():
    if os.path.exists(SOLUTION_PATH):
        os.remove(SOLUTION_PATH)
    if os.path.exists(PUZZLE_INPUT_PATH):
        os.remove(PUZZLE_INPUT_PATH)