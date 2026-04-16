from base import get_curr_max_date
from pathlib import Path

### Date variables
MAX_YEAR, MAX_DAY = get_curr_max_date()
BASE_DIR = Path(__file__).resolve().parent


# Assets paths
SIDEBAR_IMG = BASE_DIR / 'assets/aoc_tree.png'
STYLE = BASE_DIR / 'assets/style.css'
MLP_STYLE_PATH = BASE_DIR / 'assets/.mlpstyle'

PROGRESS_PLOT = BASE_DIR / 'assets/plots/my_progress_plot.png'
RUNTIME_PLOT = BASE_DIR / 'assets/plots/my_runtime_plot.png'
PUBLIC_COMPLETION_PLOT = BASE_DIR / 'assets/plots/completion_plot.png'
PUBLIC_COMPLETION_PLOT_2 = BASE_DIR / 'assets/plots/completion_plot_2.png'
SUBMISSION_TIMES_PLOT = BASE_DIR / 'assets/plots/submission_times_plot.png'
USER_INFO_PLOT = BASE_DIR / 'assets/plots/user_info_plot.png'
TOP100_ACCUMULATED_PLOT = BASE_DIR / 'assets/plots/top100_accumulated_plot.png'
TOP10_ACCUMULATED_PLOT = BASE_DIR / 'assets/plots/top10_accumulated_plot.png'
TOP10_ANNUAL_PLOT = BASE_DIR / 'assets/plots/top10_annual_plot.png'

GRID_TO_LETTER_DICT = BASE_DIR / 'assets/grid_letter_dicts/grid_to_letter.json'
LETTER_TO_GRID_LARGE = BASE_DIR / 'assets/grid_letter_dicts/letter_to_grid_large.json'
LETTER_TO_GRID_SMALL = BASE_DIR / 'assets/grid_letter_dicts/letter_to_grid_small.json'


# Data
PUZZLE_DATA = BASE_DIR / 'data/puzzle_db.csv'
LEADERBOARD_DATA = BASE_DIR / 'data/leaderboard.csv'
COMPLETIONS_DATA = BASE_DIR / 'data/completions.csv'
EXAMPLE_GRIDS = BASE_DIR / 'data/example_grids.json'


# Temporary storage paths
TEMP_STORAGE = BASE_DIR / 'temp_storage'


# External paths
AOC_DIR = '/Users/mgtezak/Desktop/my_code/Advent_of_Code/'


# Color hex codes
TEXT_COLOR = '#FFD700'
PRIMARY_COLOR = '#FF0000'
BACKGROUND_COLOR = '#04013b'
GRID_COLOR = 'white'
