# Third party
import numpy as np
import pandas as pd

# Local
from config import PUZZLE_INFO_DB
from .solution import solve



def get_puzzle_info_db() -> pd.DataFrame:
    """Returns dataframe with titles of all puzzles and my results of completed ones."""

    dtypes = dict(title=object, solution_1=object, solution_2=object, 
                  runtime_1=float, runtime_2=float, vid_link=object)
    
    return pd.read_csv(PUZZLE_INFO_DB, index_col=0, dtype=dtypes)



def get_puzzle_info(year: int, day: int) -> list:
    """Returns the title and my results of a given year and day's puzzle."""

    puzzle_id = 100 * year + day
    row = get_puzzle_info_db().loc[puzzle_id]
    puzzle_info = [None if pd.isna(x) else x for x in row]

    return puzzle_info



def get_title(year: int, day: int) -> str:
    """Retrieve title of a given year and day's puzzle."""

    return get_puzzle_info(year, day)[0]



# def get_my_solution(year: int, day: int, part: int) -> str:
#     return get_puzzle_info(year, day)[part]



def put_new_solution(year: int, day: int) -> None:
    """To add a new solution, first add its solution functions, then call this function 
    and it will automatically calculate solutions and runtimes and add them to the database.
    """
    solution_1, runtime_1 = solve(year, day, 1)
    solution_2, runtime_2 = solve(year, day, 2) if day < 25 else None, np.nan
    results = [solution_1, solution_2, runtime_1, runtime_2]

    puzzle_id = year * 100 + day
    df = get_puzzle_info_db()
    df.loc[puzzle_id, 'solution_1':'runtime_2'] = results
    


def get_vid_link(year: int, day: int) -> str | None:
    """Check if vid link exists and if so return embedded link."""

    link = get_puzzle_info(year, day)[5]
    if not link:
        return None
    
    embedded_link = f'<iframe width="960" height="540" src="{link}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    return embedded_link



def put_vid_link(year: int, day: int, link: str) -> None:
    """Add youtube link for a given year and day's puzzle to the database."""

    puzzle_id = 100 * year + day
    df = get_puzzle_info_db()
    df.loc[puzzle_id, 'video_link'] = link
    df.to_csv(PUZZLE_INFO_DB)



def del_vid_link(year: int, day: int) -> None:
    """Delete a youtube link for a given year and day's puzzle from the database."""

    puzzle_id = 100 * year + day
    df = get_puzzle_info_db()
    df.loc[puzzle_id, 'video_link'] = None
    df.to_csv(PUZZLE_INFO_DB)