# Third party
import streamlit as st

# Native
import uuid
from datetime import datetime
import pytz



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