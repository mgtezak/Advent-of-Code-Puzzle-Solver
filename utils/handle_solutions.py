# Third party
import pandas as pd
import streamlit as st

# Native
import os
import importlib 
import time
from typing import Callable

# Local
from config import TEMP_STORAGE
from base import get_session_id
from .read_letter_grid import read_grid
from .handle_puzzle_input import get_temp_puzzle_input, get_my_puzzle_input
from .handle_puzzle_data import get_puzzle_dir_path



def get_puzzle_id(year, day, part):
    return year*1000 + day*10 + part


def get_temp_sol_path():
    return TEMP_STORAGE / f'{get_session_id()}.csv'


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

    path = get_puzzle_dir_path(year, day) / f'p{part}.py'
    if not path.exists():
        return path.read_text()
    return 'Oops, cannot find script!'




def get_temp_solution_db() -> pd.DataFrame:
    """Returns all solutions as pandas dataframe."""

    columns = ['solution', 'runtime']
    dtypes = [object, float]

    path = get_temp_sol_path()
    if not path.exists():
        print(str(path))
        return pd.DataFrame(columns=columns)
    
    return pd.read_csv(path, index_col=0, dtype=dict(zip(columns, dtypes)))



def upload_temp_solution_db(df):
    path = get_temp_sol_path()
    df.to_csv(path)



def get_temp_solution(year: int, day: int, part: int) -> tuple[str, float] | None:
    """Fetches a single solution & runtime string tuple from database."""

    puzzle_id = get_puzzle_id(year, day, part)
    df = get_temp_solution_db()
    if puzzle_id not in df.index:
        return None

    solution, runtime = df.loc[puzzle_id] 
    return solution, runtime



def put_temp_solution(year: int, day: int, part: int, solution: str, runtime: float) -> None:
    """Stores away a single solution. Will overwrite if necessary."""

    puzzle_id = get_puzzle_id(year, day, part)
    df = get_temp_solution_db()
    df.loc[puzzle_id] = [solution, runtime]
    upload_temp_solution_db(df)


def del_temp_solution(year: int, day: int) -> None:
    """Removes solutions for given year and day."""

    df = get_temp_solution_db()
    df = df[df.index // 10 != year*100 + day]
    upload_temp_solution_db(df)  