from base import get_curr_max_date
from pathlib import Path

### Date variables
MAX_YEAR, MAX_DAY = get_curr_max_date()


# Assets paths
SIDEBAR_IMG = 'assets/aoc_tree.png'
STYLE = Path('assets/style.css')
MLP_STYLE_PATH = 'assets/.mlpstyle'

PROGRESS_PLOT = 'assets/plots/my_progress_plot.png'
RUNTIME_PLOT = 'assets/plots/my_runtime_plot.png'
PUBLIC_COMPLETION_PLOT = 'assets/plots/completion_plot.png'
PUBLIC_COMPLETION_PLOT_2 = 'assets/plots/completion_plot_2.png'
SUBMISSION_TIMES_PLOT = 'assets/plots/submission_times_plot.png'
USER_INFO_PLOT = 'assets/plots/user_info_plot.png'
TOP100_ACCUMULATED_PLOT = 'assets/plots/top100_accumulated_plot.png'
TOP10_ACCUMULATED_PLOT = 'assets/plots/top10_accumulated_plot.png'
TOP10_ANNUAL_PLOT = 'assets/plots/top10_annual_plot.png'

GRID_TO_LETTER_DICT = Path('assets/grid_letter_dicts/grid_to_letter.json')
LETTER_TO_GRID_LARGE = Path('assets/grid_letter_dicts/letter_to_grid_large.json')
LETTER_TO_GRID_SMALL = Path('assets/grid_letter_dicts/letter_to_grid_small.json')


# Data
PUZZLE_DATA = 'data/puzzle_db.csv'
LEADERBOARD_DATA = 'data/leaderboard.csv'
COMPLETIONS_DATA = 'data/completions.csv'
EXAMPLE_GRIDS = Path('data/example_grids.json')


# Temporary storage paths
TEMP_STORAGE = Path('temp_storage')


# External paths
AOC_DIR = '/Users/mgtezak/Desktop/my_code/Advent_of_Code/'


# Color hex codes
TEXT_COLOR = '#FFD700'
PRIMARY_COLOR = '#FF0000'
BACKGROUND_COLOR = '#04013b'
GRID_COLOR = 'white'