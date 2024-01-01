# Third party
import pandas as pd
import streamlit as st

# Native
import os

# Local
from config import SOLUTION_DB
from .grid_letter import read_grid


def display_solution(solution: str, runtime: float) -> None:
    """
    Displays the solution and runtime. If the solution comes as a letter grid, 
    an attempt is made to decipher it. If successful both the actual solution 
    and the grid are displayed. If not, just the grid.
    """

    if '\n' in solution:
        st.text('Visual output:\n' + solution)
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


def get_solution_db() -> pd.DataFrame:
    """Returns all solutions as pandas dataframe."""

    columns = ['id', 'year', 'day', 'part', 'solution', 'runtime']
    dtypes = [int, int, int, int, object, float]

    if not os.path.exists(SOLUTION_DB):
        pd.DataFrame(columns=columns).to_csv(SOLUTION_DB, index=False)
    
    return pd.read_csv(SOLUTION_DB, dtype=dict(zip(columns, dtypes)))



def get_solution(year: int, day: int, part: int) -> tuple[str, float] | None:
    """Fetches a single solution & runtime string tuple from database ."""

    df = get_solution_db()

    row = df[df.id == int(f'{year}{day:02}{part}')]
    if len(row) == 0:
        return None
    
    solution, runtime = row.iloc[0, [4, 5]].values
    return solution, runtime 



def put_solution(year: int, day: int, part: int, solution: str, runtime: float) -> None:
    """Stores away a single solution. Will overwrite if necessary."""

    new_entry = pd.DataFrame([dict(id=f'{year}{day:02}{part}', year=year, day=day, part=part, solution=str(solution), runtime=runtime)])
    df = get_solution_db()
    if len(df) == 0:
        df = new_entry
    else:
        df = pd.concat([df, new_entry], axis=0, ignore_index=True)
    df.to_csv(SOLUTION_DB, index=False)



def del_solution(year: int, day: int) -> None:
    """Removes a single solution entry from the database."""

    df = get_solution_db()
    df = df[~((df.year==year) & (df.day==day))]
    df.to_csv(SOLUTION_DB, index=False)