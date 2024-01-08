"""
Some puzzle answers come in the form of a two-dimensional grid of letters such as this:

 ##  ###   ## 
#  # #  # #  #
#  # ###  #   
#### #  # #   
#  # #  # #  #
#  # ###   ## 

The puzzles of this type I've encountered so far are: 2016-8-2, 2018-10-1, 2019-8-2, 2021-13-2, 2022-10-2 (I suspect there might be more)
I was able to build some functions which can read any grid made up of these letters.

I'm very grateful to Justin Le for putting together two grid alphabets, which made this job way easier:
https://github.com/mstksg/advent-of-code-ocr/blob/main/src/Advent/OCR/LetterMap.hs
"""

# Native imports
import json
from typing import Iterator

# Local imports
from config import GRID_TO_LETTER_DICT, LETTER_TO_GRID_LARGE, LETTER_TO_GRID_SMALL, EXAMPLE_GRIDS



def read_grid(grid: str) -> str | bool:
    """Takes a grid of letters made up of '#', space & newline characters.
    Iterates through grid column-wise. Each column represents a node in the trie (or keys in the grid letter dictionary).
    Traverses the trie until the end of a letter it reached.
    Adds up and returns the resulting message.
    """
    decoded = ''
    try:
        grid = grid.split('\n')     
        m, n = len(grid), len(grid[0])
        trie_root = get_grid_to_letter_db()
        current_node = trie_root
        for col in range(n+1):
            col_slice = ''.join(grid[row][col] for row in range(m)) if col < n else ' '
            if set(col_slice) == set(' '):
                continue
            current_node = current_node[col_slice]
            if 'letter' in current_node:
                decoded += current_node['letter']
                current_node = trie_root        
    except:
        pass

    return decoded
            


def get_grid_to_letter_db() -> dict[str: str]:
    """Returns the grid letter trie structure as dictionary."""

    return json.loads(GRID_TO_LETTER_DICT.read_text())



def get_letter_to_grid_dicts() -> Iterator[tuple[str, int, dict[str, list[str]]]]:
    """"""

    letter2grid_small = json.loads(LETTER_TO_GRID_SMALL.read_text())
    letter2grid_large = json.loads(LETTER_TO_GRID_LARGE.read_text())
    dicts = (letter2grid_small, letter2grid_large)
    labels = ('small', 'large')
    sizes = (6, 10)
    return zip(labels, sizes, dicts)



def generate_grids(letters: str) -> tuple[str, list]:
    """"""
    letters = letters.upper().strip()
    for label, size, letter_dict in get_letter_to_grid_dicts():
        result = ['' for _ in range(size)]
        unknown = set()
        for i, letter in enumerate(letters):
            if i > 0:
                for j, row in enumerate(letter_dict['space']):
                    result[j] += row
            if letter not in letter_dict:
                if letter != ' ':
                    unknown.add(letter)
                letter = 'unknown'
            for j, row in enumerate(letter_dict[letter]):
                result[j] += row

        result = '\n'.join(result)
        yield label, result, unknown
    



###########################################################################################################
###########################################################################################################
# The following is not meant for regular use of the app. It is just for me to remember how I built the grid
# letter dictionary. It also might come in useful if I ever have to add another set of grid letters.


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



def initialize_grid_letter_dict(grid_letter_maps: dict[str, str] = GRID_LETTER_MAPS) -> None:
    """Takes as input a dictionary with grids as key and the actual letters they represent as values.
    Builds a trie type data structure (https://en.wikipedia.org/wiki/Trie) where each column of the grid
    represents a node in the trie. The trie dictionary is stored in a json file.
    """

    trie_root = {}
    current_node = trie_root
    for grid, alphabet in grid_letter_maps.items():
        letter = iter(alphabet)
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

    GRID_TO_LETTER_DICT.write_text(json.dumps(trie_root))        



def initialize_letter_to_grid_dicts() -> None:
    """"""
    
    grids = (LARGE_GRID, SMALL_GRID)
    alphabets = (LARGE_LETTERS, SMALL_LETTERS)
    paths = (LETTER_TO_GRID_LARGE, LETTER_TO_GRID_SMALL)
    for grid, alphabet, path in zip(grids, alphabets, paths):
        letter2grid = {}
        letter = iter(alphabet)
        grid = grid.split('\n')
        print(grid)
        m, n = len(grid), len(grid[0])
        col_slices = ''
        for col in range(n+1):
            col_slice = ''.join(grid[row][col] for row in range(m)) if col < n else ' '
            if '#' in col_slice:
                col_slices += '\n' + col_slice
            else:
                letter2grid[next(letter)] = col_slices
                col_slices = ''       

        path.write_text(json.dumps(letter2grid, indent=2))  



def get_grids() -> dict[str, str | list[str]]:
    """"""

    return json.loads(EXAMPLE_GRIDS.read_text())



def initialize_letter_to_grid_dicts() -> None:
    grids = (LARGE_GRID, SMALL_GRID)
    alphabets = (LARGE_LETTERS, SMALL_LETTERS)
    paths = (LETTER_TO_GRID_LARGE, LETTER_TO_GRID_SMALL)
    for grid, alphabet, path in zip(grids, alphabets, paths):
        letter2grid = {}
        letter = iter(alphabet)
        grid = grid.split('\n')
        m, n = len(grid), len(grid[0])
        delimiters = [col for col in range(n) if all(grid[row][col] == ' ' for row in range(m))] + [n]
        start = 0
        for end in delimiters:
            extracted = [grid[row][start:end] for row in range(m)]
            letter2grid[next(letter)] = extracted
            start = end + 1  

        letter2grid['space'] = [' '] * m
        letter2grid['unknown'] = [' ' * delimiters[0] for _ in range(m)]
        path.write_text(json.dumps(letter2grid, indent=2))  
