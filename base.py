# Third party
import streamlit as st

# Native
import uuid
from pathlib import Path
from datetime import datetime, timedelta
import pytz
import os



def get_session_id() -> str:
    """Generates a unique session ID"""

    if 'session_id' not in st.session_state:
        st.session_state['session_id'] = str(uuid.uuid4())

    return st.session_state['session_id']



def get_curr_max_date() -> tuple[int, int]:
    """Fetches the local time for advent of code (EST/UTC-5) and returns year and day ofthe latest puzzle."""

    curr = datetime.now(pytz.timezone('EST'))
    year, month, day = curr.year, curr.month, curr.day
    is_december = (month == 12)
    
    MAX_YEAR = year if is_december else year - 1
    MAX_DAY = day if is_december and day < 25 else 25
    return MAX_YEAR, MAX_DAY


def clear_temp_storage():
    directory_path = Path('temp_storage')

    # Get current time
    now = datetime.now(pytz.timezone('EST'))

    # Define the age limit (1 hour in this case)
    age_limit = timedelta(hours=1)

    # Loop through each file in the directory
    for file in directory_path.iterdir():
        if file.is_file():  # Check if it's a file
            # Get the file's modification time
            file_mod_time = datetime.fromtimestamp(file.stat().st_mtime)

            # Check if the file is older than 1 hour
            if now - file_mod_time > age_limit:
                print(f"Deleting: {file}")
                os.remove(file)  # Delete the file
