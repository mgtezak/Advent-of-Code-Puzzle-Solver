from datetime import datetime
import pytz


def get_curr_max_date():
    """Fetches the local time for advent of code (EST/UTC-5) and returns year and day ofthe latest puzzle."""

    curr = datetime.now(pytz.timezone('EST'))
    year, month, day = curr.year, curr.month, curr.day
    is_december = (month == 12)
    
    MAX_YEAR = year if is_december else year - 1
    MAX_DAY = day if is_december and day < 25 else 25
    return MAX_YEAR, MAX_DAY