import json
import os


PUZZLE_INPUT_DB_PATH = 'db/puzzle_input.json'
SOLUTION_DB_PATH = 'db/solution.json'


# PUZZLE INPUT DB
def get_puzzle_input_db():
    try:
        with open(PUZZLE_INPUT_DB_PATH, 'r') as f:
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
    with open(PUZZLE_INPUT_DB_PATH, 'w') as f:
        json.dump(db, f, indent=4)



# SOLUTION DB
def get_solution_db():
    """Get all solutions as dict"""
    try:
        with open(SOLUTION_DB_PATH, 'r') as f:
            db = json.load(f)
    except:
        db = {}
    return db


def get_solution(year, day, part):
    """Returns a specified solution or False if non existent."""
    year, day, part = map(str, [year, day, part])
    db = get_solution_db()
    if not db.get(year, False):
        return False
    if not db[year].get(day, False):
        return False
    return db[year][day].get(part, False)


def put_solution(year, day, part, solution=None):
    """Stores away a single solution. Will overwrite if necessary."""
    year, day, part = map(str, [year, day, part])
    db = get_solution_db()
    if not db.get(year, False):
        db[year] = {}
    if not db[year].get(day, False):
        db[year][day] = {}
    db[year][day][part] = solution
    with open(SOLUTION_DB_PATH, 'w') as f:
        json.dump(db, f, indent=4)


def del_solution(year, day):
    year, day = str(year), str(day)
    db = get_solution_db()
    if not db.get(year, False):
        return
    if db[year].get(day, False):
        del db[year][day]
    with open(SOLUTION_DB_PATH, 'w') as f:
        json.dump(db, f, indent=4)



# RESET
def remove_dbs():
    os.remove(SOLUTION_DB_PATH)
    os.remove(PUZZLE_INPUT_DB_PATH)