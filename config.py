from datetime import datetime
import pytz

### Global Date Variables:

def get_curr_max_date():
    # AoC local time (EST/UTC-5) 
    curr = datetime.now(pytz.timezone('EST'))
    year, month, day = curr.year, curr.month, curr.day
    is_december = (month == 12)
    
    MAX_YEAR = year if is_december else year - 1
    MAX_DAY = min(day, 25) if is_december else 25
    return MAX_YEAR, MAX_DAY

MAX_YEAR, MAX_DAY = get_curr_max_date()


### All file paths in one place

# Assets
SIDEBAR_IMG = 'assets/aoc_tree.png'
STYLE = 'assets/style.css'
PROGRESS_PLOT = 'assets/plots/completion_plot.png'
RUNTIME_PLOT = 'assets/plots/runtime_plot.png'

# DB
GRID_LETTER = 'db/grid_letter.json'
PUZZLE_INPUT = 'db/puzzle_input.json'
SOLUTION = 'db/solution.csv'
PROGRESS = 'db/progress.csv'
TITLE = 'db/title.csv'
VIDEO = 'db/video.csv'