# Third party
import pandas as pd
import streamlit as st

# Native
import os
import importlib 
import time
from typing import Callable

# Local
from config import TEMP_SOLUTION
from .read_letter_grid import read_grid
from .handle_puzzle_input import get_temp_puzzle_input, get_my_puzzle_input


def get_solving_func(year: int, day: int, part: int) -> Callable:
    module_name = f"advent_of_code.y{year}.d{day:02}.p{part}"
    module = importlib.import_module(module_name)
    return getattr(module, f'part{part}')



def solve(year: int, day: int, part: int, my_input: bool = False) -> tuple[str, float]:
    """Retrieves puzzle input and solving function for given year, day & part 
    and returns solution and runtime.
    """

    solving_func = get_solving_func(year, day, part)

    if my_input:
        puzzle_input = get_my_puzzle_input(year, day)
    else:
        puzzle_input = get_temp_puzzle_input(year, day)

    start = time.time()
    solution = str(solving_func(puzzle_input))
    runtime = time.time() - start

    return solution, runtime



def display_solution(solution: str, runtime: float) -> None:
    """Displays the solution and runtime. If the solution comes as a letter grid, 
    an attempt is made to decipher it. If successful both the actual solution 
    and the grid are displayed. If not, just the grid.
    """

    if '\n' in solution:
        st.text('Visual output:\n\n' + solution)
        letters = read_grid(solution)
        if letters:
            st.subheader(letters)
    else:
        st.subheader(solution)

    st.caption(f"Runtime: {format_runtime(runtime)}")



def format_runtime(runtime: float) -> str:
    """Returns formatted runtime either as seconds or milliseconds."""

    if runtime >= 0.01:
        return f'{runtime:.2f} seconds'
    
    return f'{int(runtime*1000)} milliseconds'



def get_source_code(year: int, day: int, part: int) -> str:
    """Retrieves the solution script for given year, day & part"""

    path = f'advent_of_code/y{year}/d{day:02}/p{part}.py'
    if not os.path.exists(path):
        return 'Oops, cannot find script!'
    
    with open(path, 'r') as f:
        script = f.read()

    return script



def get_temp_solution_db() -> pd.DataFrame:
    """Returns all solutions as pandas dataframe."""

    columns = ['solution', 'runtime']
    dtypes = [object, float]

    if not os.path.exists(TEMP_SOLUTION):
        return pd.DataFrame(columns=columns)
    
    return pd.read_csv(TEMP_SOLUTION, index_col=0, dtype=dict(zip(columns, dtypes)))



def get_temp_solution(year: int, day: int, part: int) -> tuple[str, float] | None:
    """Fetches a single solution & runtime string tuple from database."""

    puzzle_id = 1000*year + 10*day + part
    df = get_temp_solution_db()

    if puzzle_id not in df.index:
        return None

    solution, runtime = df.loc[puzzle_id] 
    return solution, runtime



def put_temp_solution(year: int, day: int, part: int, solution: str, runtime: float) -> None:
    """Stores away a single solution. Will overwrite if necessary."""

    puzzle_id = 1000*year + 10*day + part
    df = get_temp_solution_db()
    df.loc[puzzle_id] = [solution, runtime]
    df.to_csv(TEMP_SOLUTION)



def del_temp_solution(year: int, day: int) -> None:
    """Removes solutions for given year and day."""

    puzzle_ids = [1000*year + 10*day + part for part in (1, 2)]
    df = get_temp_solution_db()

    for puzzle_id in puzzle_ids:
        if puzzle_id in df.index:
            df.drop(puzzle_id, inplace=True)

    df.to_csv(TEMP_SOLUTION)    