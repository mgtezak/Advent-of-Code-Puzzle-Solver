# Third party imports
import streamlit as st
import numpy as np

# Native imports
from datetime import datetime, timedelta
import os

# Local imports
from config import PUZZLE_DATA, TEMP_STORAGE, MAX_YEAR
from .handle_puzzle_data import get_puzzle_db
from .handle_puzzle_input import is_example_input
from .handle_solutions import solve



def display_example_inputs(inputs):

    n = len(inputs)
    for i in range(n):
        st.divider()
        if i == 0:
            st.write(f'Example input{"s" if n > 1 else ""}:')
        example_input, compatibility = inputs[str(i)]
        st.code(example_input)
        if compatibility != 3:
            st.caption(f'(Only works with part {compatibility})')



def reboot_app() -> None:
    """Temporary storage gets cleared of all files that haven't been modified for over an hour."""

    TEMP_STORAGE.mkdir(exist_ok=True)
    now = datetime.now()

    for file in TEMP_STORAGE.iterdir():
        latest_update = datetime.fromtimestamp(file.stat().st_mtime)

        if now - latest_update > timedelta(hours=15):
            file.unlink()
    


def reset_puzzle_solver() -> None:
    """Resets the page, so that new puzzle input can be provided."""

    st.session_state['solution'] = False



def get_valid_days(year: int) -> list[int]:
    """Returns list of currently available days for given year."""

    return [day for day in range(1, 26) if solution_exists(year, day)]

def get_valid_years() -> list[int]:
    """Returns list of currently available years in reverse order."""

    return list(range(MAX_YEAR, 2014, -1))


def get_completed_stat() -> str:
    """Returns formatted string describing the current progress."""

    df = get_puzzle_db()
    completed = df.solution_1.count()
    total = df.shape[0]

    return f"So far I've completed {completed} ({int(completed/total * 100)}%) of the available total of {total} two-part daily challenges."



def display_fail_msg(year, day) -> None:
    """Failure message gets displayed if the solving function throws an error."""
    if is_example_input(year, day):

        st.error("""
            :man-tipping-hand: This example input only works with the other part.  
            :star: Try entering your own input.
        """)

    else:
        st.error("""
            :scream: Oops, something went wrong!  
            :thinking_face: Perhaps there's an issue with the puzzle input you provided...  
            :crossed_fingers: Check if you copied it correctly and try re-entering it.
            :email: If this doesn't help, drop me a message: mgtezak@gmail.com
        """)



def solution_exists(year, day):
    path = f'advent_of_code/y{year}/d{day:02}'
    return os.path.exists(path)



def get_valid_parts(year, day):
    if not solution_exists(year, day):
        return []
    if day == 25:
        return [1]
    return [1, 2]



def put_my_results(year: int, day: int) -> None:
    """To add a new solution, first add its solution functions, then call this function 
    and it will automatically calculate solutions and runtimes and add them to the database.
    """
    solution_1, runtime_1 = solve(year, day, 1, True)
    solution_2, runtime_2 = solve(year, day, 2, True) if day < 25 else None, np.nan
    results = [solution_1, solution_2, runtime_1, runtime_2]

    puzzle_id = year * 100 + day
    df = get_puzzle_db()
    df.loc[puzzle_id, 'solution_1':'runtime_2'] = results
    df.to_csv(PUZZLE_DATA)



