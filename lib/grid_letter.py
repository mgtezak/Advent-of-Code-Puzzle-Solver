# Native imports
import json

# Local imports
from config import GRID_LETTER_DB



def extract_letters_from_grid(grid: str) -> str:
    """Generator that extracts individual letters from letter grid"""

    if set(grid) != set('# \n'):
        raise ValueError("Expecting grid to be composed of #, space and newline characters")

    grid = grid.split('\n')
    m, n = len(grid), len(grid[0])

    if any(len(grid[i]) != n for i in range(m)):
        raise ValueError("Expecting rows to have uniform lengths")
    
    divisors_cols = [col for col in range(n) if all(grid[row][col] == ' ' for row in range(m))]

    if divisors_cols:
        start = 0
        for end in divisors_cols:
            letter = '\n'.join(grid[row][start:end] for row in range(m))
            start = end + 1
            yield letter        
    else:
        yield '\n'.join(grid)



def read_grid(grid) -> str:
    """Takes a grid of letters made up of '#', space & newline characters and attempts to decipher it,
    first by seperating the individual letters from each other and then by checking, whether they exist 
    in the (hopefully complete) grid letter database.
    
    The puzzles I've encountered which provide a grid letter output are: 
    2016-8-2, 2018-10-1, 2019-8-2, 2021-13-2, 2022-10-2.
    I suspect there might be more.
    """

    grid_letters = get_grid_letter_db()

    message = ''
    for letter in extract_letters_from_grid(grid):
        message += grid_letters.get(letter, '_')

    if '_' in message:
        message += ' (could not fully decipher)'

    return message



def get_grid_letter_db() -> dict[str: str]:
    """Returns the grid letter translation dictionary."""

    try:
        with open(GRID_LETTER_DB, 'r') as f:
            db = json.load(f)
    except:
        db = {}

    return db



def put_grid_letters(grid: str, letters: str) -> None:
    """Inserts one or more grid letter entries into database"""

    db = get_grid_letter_db()
    for key, value in zip(extract_letters_from_grid(grid), letters):
        db[key] = value.upper()

    with open(GRID_LETTER_DB, 'w') as f:
        json.dump(db, f, indent=4)