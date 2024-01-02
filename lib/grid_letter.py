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



# LARGE_GRID = '''
#   ##   #####   ####  ###### ######  ####  #    #    ### #    # #      #    # #####  #####  #    # ######
#  #  #  #    # #    # #      #      #    # #    #     #  #   #  #      ##   # #    # #    # #    #      #
# #    # #    # #      #      #      #      #    #     #  #  #   #      ##   # #    # #    #  #  #       #
# #    # #    # #      #      #      #      #    #     #  # #    #      # #  # #    # #    #  #  #      # 
# #    # #####  #      #####  #####  #      ######     #  ##     #      # #  # #####  #####    ##      #  
# ###### #    # #      #      #      #  ### #    #     #  ##     #      #  # # #      #  #     ##     #   
# #    # #    # #      #      #      #    # #    #     #  # #    #      #  # # #      #   #   #  #   #    
# #    # #    # #      #      #      #    # #    # #   #  #  #   #      #   ## #      #   #   #  #  #     
# #    # #    # #    # #      #      #   ## #    # #   #  #   #  #      #   ## #      #    # #    # #     
# #    # #####   ####  ###### #       ### # #    #  ###   #    # ###### #    # #      #    # #    # ######
# '''[1:-1]

# LARGE_LETTERS = 'ABCEFGHJKLNPRXZ'



# SMALL_GRID = '''
#  ##  ###   ##  #### ####  ##  #  # ###   ## #  # #     ##  ###  ###   ### #  # #   # ####
# #  # #  # #  # #    #    #  # #  #  #     # # #  #    #  # #  # #  # #    #  # #   #    #
# #  # ###  #    ###  ###  #    ####  #     # ##   #    #  # #  # #  # #    #  #  # #    # 
# #### #  # #    #    #    # ## #  #  #     # # #  #    #  # ###  ###   ##  #  #   #    #  
# #  # #  # #  # #    #    #  # #  #  #  #  # # #  #    #  # #    # #     # #  #   #   #   
# #  # ###   ##  #### #     ### #  # ###  ##  #  # ####  ##  #    #  # ###   ##    #   ####
# '''[1:-1]

# SMALL_LETTERS = 'ABCEFGHIJKLOPRSUYZ'



# def read_grid(grid) -> str:
#     """Takes a grid of letters made up of '#', space & newline characters and attempts to decipher it,
#     first by seperating the individual letters from each other and then by checking, whether they exist 
#     in the (hopefully complete) grid letter database.
#     """

#     grid_letters = get_grid_letter_db()

#     message = ''
#     for letter in extract_letters_from_grid(grid):
#         message += grid_letters.get(letter, '_')

#     if '_' in message:
#         message += ' (could not fully decipher)'

#     return message

def read_grid(grid):
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
        if 'end' in current_node:
            message += current_node['end']
            current_node = trie_root
            
    return message



def get_grid_letter_db() -> dict[str: str]:
    """Returns the grid letter translation dictionary."""

    try:
        with open(GRID_LETTER_DB, 'r') as f:
            db = json.load(f)
    except:
        db = {}

    return db



# def extract_letters_from_grid(grid: str) -> str:
#     """Generator that seperates and extracts individual letters from letter grid"""

#     if set(grid) != set('# \n'):
#         raise ValueError("Expecting grid to be composed of #, space and newline characters")

#     grid = grid.split('\n')
#     m, n = len(grid), len(grid[0])

#     if any(len(grid[i]) != n for i in range(m)):
#         raise ValueError("Expecting rows to have uniform lengths")
    
#     divisors_cols = [col for col in range(n) if all(grid[row][col] == ' ' for row in range(m))]
#     if m == 6: # small letters
#         for i in range(len(divisors_cols)-1):
#             if divisors_cols[i+1] - divisors_cols[i] 
    
    
#     if divisors_cols:
#         start = 0
#         for end in divisors_cols + [n]:
#             letter = '\n'.join(grid[row][start:end] for row in range(m))
#             start = end + 1
#             yield letter        
#     else:
#         yield '\n'.join(grid)



# def add_grid_letters(grid: str, letters: str) -> None:
#     """Takes as arguments a two-dimensional grid and letters that it supposedly represents.
#     Inserts each grid letter into the translation dictionary and updates the json database.
#     """

#     db = get_grid_letter_db()
#     for key, value in zip(extract_letters_from_grid(grid), letters):
#         db[key] = value.upper()

#     with open(GRID_LETTER_DB, 'w') as f:
#         json.dump(db, f, indent=4)



# def initialize_grid_letter_db():
#     """Inserts the large and small alphabets into grid letter translation dictionary."""

#     add_grid_letters(LARGE_GRID, LARGE_LETTERS)
#     add_grid_letters(SMALL_GRID, SMALL_LETTERS)