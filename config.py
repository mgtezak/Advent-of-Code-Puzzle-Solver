from base import get_curr_max_date
from pathlib import Path

### Date variables
MAX_YEAR, MAX_DAY = get_curr_max_date()


# Assets paths
SIDEBAR_IMG = 'assets/aoc_tree.png'
STYLE = 'assets/style.css'
MLP_STYLE_PATH = 'assets/.mlpstyle'
PROGRESS_PLOT = 'assets/plots/progress_plot.png'
RUNTIME_PLOT = 'assets/plots/runtime_plot.png'
GRID_LETTER_DICT = 'assets/grid_letter.json'


# Main database path
PUZZLE_DATA = 'puzzle_data.csv'


# Temporary storage paths – rebooted with every new session
TEMP = 'temp_storage'
TEMP_PUZZLE_INPUT = 'temp_storage/puzzle_input.json'
TEMP_SOLUTION = 'temp_storage/solution.csv'      


# External paths
AOC_DIR = '/Users/mgtezak/Desktop/my_code/Advent_of_Code/'


# Color hex codes
TEXT_COLOR = '#FFD700'
PRIMARY_COLOR = '#FF0000'
BACKGROUND_COLOR = '#04013b'
GRID_COLOR = 'white'