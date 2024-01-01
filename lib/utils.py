# Third party imports
import streamlit as st
import pandas as pd

# Native imports
import os

# Local imports
from config import PROGRESS_DB, SOLUTION_DB, PUZZLE_INPUT_DB
from config import MAX_YEAR, MAX_DAY
from .aoc import function_dict


def reboot_app() -> None:
    """
    Gets called upon restarting the app with an empty session state. 
    All currently stored puzzle inputs and solutions will be deleted.
    The progress db will be updated.
    """

    if os.path.exists(SOLUTION_DB):
        os.remove(SOLUTION_DB)

    if os.path.exists(PUZZLE_INPUT_DB):
        os.remove(PUZZLE_INPUT_DB)

    create_progress_db()



def reset_puzzle_solver() -> None:
    """Resets the page, so that new puzzle input can be provided."""

    st.session_state['solution'] = False



def get_valid_days(year: int) -> list[int]:
    """Returns list of currently available days for given year in reverse order."""

    return [d for d in reversed(range(1, 26)) if f'aoc{year}_day{d}_part1' in function_dict]



def get_completed_stat() -> str:
    """Returns formatted string describing the current progress."""

    df = get_progress_db()
    completed = df.completed.sum()
    total = df.shape[0]

    return f"So far I've completed {completed} ({int(completed/total*100)}%) of the available total of {total} two-part daily challenges."







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

    if not os.path.exists(PROGRESS_DB):
        create_progress_db()

    return pd.read_csv(PROGRESS_DB)



def create_progress_db() -> None:
    """Creates the database containing information about which puzzles have been solved so far."""

    data = []
    for year in range(2015, MAX_YEAR+1):
        completed = set(get_valid_days(year))
        for day in range(1, 26):
            data.append([year, day, 1 if day in completed else 0])
            if year == MAX_YEAR and day == MAX_DAY:
                break

    df = pd.DataFrame(data, columns=["year", "day", "completed"])
    df.to_csv(PROGRESS_DB, index=False)