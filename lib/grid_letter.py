"""
Some puzzle answers come in the form of a two-dimensional grid of letters. 
So far I've encountered this type of output in the following puzzles: 

2016-8-2, 2018-10-1, 2019-8-2, 2021-13-2, 2022-10-2 (I suspect there might be more)

Thanks to someone who made an effort to document all the different possible letters, 
I was able to build some functions which can read any grid made up of these letters.

Credit for the alphabet grids goes to https://github.com/mstksg/advent-of-code-ocr/blob/main/src/Advent/OCR/LetterMap.hs
"""

# Native imports
import json

# Local imports
from config import GRID_LETTER_DB



LARGE_GRID = '''
  ##   #####   ####  ###### ######  ####  #    #    ### #    # #      #    # #####  #####  #    # ######
 #  #  #    # #    # #      #      #    # #    #     #  #   #  #      ##   # #    # #    # #    #      #
#    # #    # #      #      #      #      #    #     #  #  #   #      ##   # #    # #    #  #  #       #
#    # #    # #      #      #      #      #    #     #  # #    #      # #  # #    # #    #  #  #      # 
#    # #####  #      #####  #####  #      ######     #  ##     #      # #  # #####  #####    ##      #  
###### #    # #      #      #      #  ### #    #     #  ##     #      #  # # #      #  #     ##     #   
#    # #    # #      #      #      #    # #    #     #  # #    #      #  # # #      #   #   #  #   #    
#    # #    # #      #      #      #    # #    # #   #  #  #   #      #   ## #      #   #   #  #  #     
#    # #    # #    # #      #      #   ## #    # #   #  #   #  #      #   ## #      #    # #    # #     
#    # #####   ####  ###### #       ### # #    #  ###   #    # ###### #    # #      #    # #    # ######
'''[1:-1]

LARGE_LETTERS = 'ABCEFGHJKLNPRXZ'

SMALL_GRID = '''
 ##  ###   ##  #### ####  ##  #  # ###   ## #  # #     ##  ###  ###   ### #  # #   # ####
#  # #  # #  # #    #    #  # #  #  #     # # #  #    #  # #  # #  # #    #  # #   #    #
#  # ###  #    ###  ###  #    ####  #     # ##   #    #  # #  # #  # #    #  #  # #    # 
#### #  # #    #    #    # ## #  #  #     # # #  #    #  # ###  ###   ##  #  #   #    #  
#  # #  # #  # #    #    #  # #  #  #  #  # # #  #    #  # #    # #     # #  #   #   #   
#  # ###   ##  #### #     ### #  # ###  ##  #  # ####  ##  #    #  # ###   ##    #   ####
'''[1:-1]

SMALL_LETTERS = 'ABCEFGHIJKLOPRSUYZ'

GRID_LETTER_MAPS = {LARGE_GRID: LARGE_LETTERS, SMALL_GRID: SMALL_LETTERS}



def read_grid(grid):
    """Takes a grid of letters made up of '#', space & newline characters.
    Iterates through grid column-wise. Each column represents a node in the trie (or keys in the grid letter dictionary).
    Traverses the trie until the end of a letter it reached.
    Adds up and returns the resulting message.
    """
    try:
        grid = grid.split('\n')     
        m, n = len(grid), len(grid[0])

        trie_root = get_grid_letter_db()
        current_node = trie_root
        message = ''
        for col in range(n+1):
            col_slice = ''.join(grid[row][col] for row in range(m)) if col < n else ' '
            if set(col_slice) == set(' '):
                continue
            current_node = current_node[col_slice]
            if 'letter' in current_node:
                message += current_node['letter']
                current_node = trie_root

    except:
        message = 'Unfortunately could not decipher the message.'
            
    return message



def get_grid_letter_db() -> dict[str: str]:
    """Returns the grid letter database as dictionary."""

    try:
        with open(GRID_LETTER_DB, 'r') as f:
            db = json.load(f)
    except:
        db = {}

    return db


def initialize_grid_letter_db(grid_letter_maps: dict[str, str] = GRID_LETTER_MAPS) -> None:
    """Takes as input a dictionary with grids as key and the actual letters they represent as values.
    Builds a trie type data structure (https://en.wikipedia.org/wiki/Trie) where each column of the grid
    represents a node in the trie. The trie dictionary is stored in a json file.
    """

    trie_root = {}
    current_node = trie_root
    for grid, letters in grid_letter_maps.items():
        letter = iter(letters)
        grid = grid.split('\n')
        m, n = len(grid), len(grid[0])
        for col in range(n+1):
            col_slice = ''.join(grid[row][col] for row in range(m)) if col < n else ' '
            if set(col_slice) == set(' '):
                current_node['letter'] = next(letter)
                current_node = trie_root
            else:
                if col_slice not in current_node:
                    current_node[col_slice] = {}
                current_node = current_node[col_slice]

    with open(GRID_LETTER_DB, 'w') as f:
        json.dump(trie_root, f)