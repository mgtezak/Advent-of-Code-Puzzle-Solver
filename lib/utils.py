# Third party imports
import streamlit as st
import pandas as pd

# Native imports
import os

# Local imports
from config import TEMP_PUZZLE_INPUT_DB, TEMP_SOLUTION_DB
from .puzzle import get_puzzle_info_db


def reboot_app() -> None:
    """Gets called upon restarting the app with an empty session state. 
    All temporarily stored puzzle inputs and solutions will be deleted.
    """

    if os.path.exists(TEMP_SOLUTION_DB):
        os.remove(TEMP_SOLUTION_DB)

    if os.path.exists(TEMP_PUZZLE_INPUT_DB):
        os.remove(TEMP_PUZZLE_INPUT_DB)



def reset_puzzle_solver() -> None:
    """Resets the page, so that new puzzle input can be provided."""

    st.session_state['solution'] = False



def get_valid_days(year: int) -> list[int]:
    """Returns list of currently available days for given year."""

    df = get_puzzle_info_db()
    year *= 100
    days = []
    for day in range(1, 26):
        if pd.notna(df.loc[year+day, 'solution_1']):
            days.append(day)

    return days



def get_completed_stat() -> str:
    """Returns formatted string describing the current progress."""

    df = get_puzzle_info_db()
    completed = df.solution_1.count()
    total = df.shape[0]

    return f"So far I've completed {completed} ({int(completed/total * 100)}%) of the available total of {total} two-part daily challenges."



def display_fail_msg() -> None:
    """Failure message gets displayed if the solving function throws an error."""

    st.error("""
        :scream: Oops, something went wrong!  
        :thinking_face: Perhaps there's an issue with the puzzle input you provided...  
        :crossed_fingers: Please try re-entering it.
    """)