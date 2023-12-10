import time

### Global Variables:

curr = time.localtime(time.time())
if curr.tm_mon == 12:
    MAX_YEAR = curr.tm_year
    if curr.tm_hour > 6:
        MAX_DAY = curr.tm_mday  
    else:   # not yet 6:00 o'clock
        MAX_DAY = curr.tm_mday - 1
else:   # not yet december
    MAX_YEAR = curr.tm_year - 1
    MAX_DAY = 25


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