from datetime import datetime

### Global Variables:

curr = datetime.today()
MAX_YEAR = curr.year if curr.month == 12 else curr.year - 1


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