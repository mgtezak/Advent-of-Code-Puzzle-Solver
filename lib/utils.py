# Third party imports
import streamlit as st
import pandas as pd

# Native imports
import os

# Local imports
from config import PROGRESS, SOLUTION, PUZZLE_INPUT
from lib import aoc, db


def reboot_app() -> None:
    """
    Gets called upon restarting the app with an empty session state. 
    All currently stored puzzle inputs and solutions will be deleted.
    The completion db will be updated.
    """

    if os.path.exists(SOLUTION):
        os.remove(SOLUTION)

    if os.path.exists(PUZZLE_INPUT):
        os.remove(PUZZLE_INPUT)

    create_progress_db()



def reset_puzzle_solver() -> None:
    """Resets the page, so that new puzzle input can be provided."""

    st.session_state['solution'] = False



def get_valid_days(year: int) -> list[int]:
    """Returns list of currently available days for given year in reverse order."""

    return [d for d in reversed(range(1, 26)) if f'aoc{year}_day{d}_part1' in aoc.function_dict]



def get_completed_stat() -> str:
    """Returns formatted string describing the current progress."""

    df = get_progress_db()
    completed = df.completed.sum()
    total = df.shape[0]

    return f"So far I've completed {completed} of the available total of {total} daily challenges."



def display_solution(solution: str, runtime: float) -> None:
    """
    Displays the solution and runtime. If the solution comes as a letter grid, 
    an attempt is made to decipher it. If successful both the actual solution 
    and the grid are displayed. If not, just the grid.
    """

    if '\n' in solution:
        st.text('Visual output:\n' + solution)
        letters = read_grid(solution)
        if letters:
            st.subheader(letters)
    else:
        st.subheader(solution)

    st.caption(f"Runtime: {format_runtime(runtime)}")



def read_grid(grid) -> str | bool:
    """
    Takes a grid of letters made up of '#' and ' ' and attempts to decipher it,
    first by seperating the individual letters from each other and then by checking,
    whether they exist in my (unfortunately incomplete) grid letter alphabet.
    
    The puzzles I've encountered which provide a grid letter output are: 
    2016-8-2, 2018-10-1, 2019-8-2, 2021-13-2, 2022-10-2.
    I suspect there are more.
    """

    grid_letters = db.get_grid_letter_db()
    lines = grid.split('\n')
    letter_width = 5 if len(lines) == 6 else 8
    letters = ''
    for col in range(0, len(lines[0]), letter_width):
        letter = '\n'.join([''.join(lines[row][col:col+letter_width]) for row in range(len(lines))])
        letters += grid_letters.get(letter, '*')
    if '*' in letters:
        letters += ' (could not fully decipher)'
    return letters



def format_runtime(runtime: float) -> str:
    """Returns formatted runtime either as seconds or milliseconds."""

    if runtime >= 0.01:
        return f'{runtime:.2f} seconds'
    return f'{int(runtime*1000)} milliseconds'



def display_fail_msg() -> None:
    """Failure message gets displayed if the solving function throws an error."""

    st.error("""
        :scream: Oops, something went wrong!  
        :thinking_face: Perhaps there's an issue with the puzzle input you provided...  
        :crossed_fingers: Please try re-entering it.
    """)



### The following functions are necessary/useful for maintenance but not for normal use of the app
def get_progress_db() -> pd.DataFrame:
    """Retrieves progress database."""

    if not os.path.exists(PROGRESS):
        create_progress_db()

    return pd.read_csv(PROGRESS)



def create_progress_db() -> None:
    """Creates the database containing information about which puzzles have been solved so far."""

    data = []
    for year in range(2015, 2023):
        completed = set(get_valid_days(year))
        for day in range(1, 26):
            data.append([year, day, 1 if day in completed else 0])
            
    df = pd.DataFrame(data, columns=["year", "day", "completed"])
    df.to_csv(PROGRESS, index=False)