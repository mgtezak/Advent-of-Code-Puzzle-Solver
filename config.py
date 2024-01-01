from datetime import datetime
import pytz


### Global date variables

def get_curr_max_date():
    # AoC local time (EST/UTC-5) 
    curr = datetime.now(pytz.timezone('EST'))
    year, month, day = curr.year, curr.month, curr.day
    is_december = (month == 12)
    
    MAX_YEAR = year if is_december else year - 1
    MAX_DAY = day if is_december and day < 25 else 25
    return MAX_YEAR, MAX_DAY

MAX_YEAR, MAX_DAY = get_curr_max_date()


### All file paths in one place

# Assets
SIDEBAR_IMG = 'assets/aoc_tree.png'
STYLE = 'assets/style.css'
PROGRESS_PLOT = 'assets/plots/progress_plot.png'
RUNTIME_PLOT = 'assets/plots/runtime_plot.png'


# Database
PUZZLE_INFO_DB = 'db/puzzle_info.csv'
GRID_LETTER_DB = 'db/grid_letter.json'
TEMP_PUZZLE_INPUT_DB = 'db/temp_puzzle_input.json'  # gitignore – rebooted with every new session
TEMP_SOLUTION_DB = 'db/temp_solution.csv'           # gitignore – rebooted with every new session
MY_PUZZLE_INPUT_DB = 'db/my_puzzle_input.json'      # gitignore


### Plot configuration

# Colors
TEXT_COLOR = '#FFD700'
PRIMARY_COLOR = '#FF0000'
BACKGROUND_COLOR = '#04013b'
GRID_COLOR = 'white'