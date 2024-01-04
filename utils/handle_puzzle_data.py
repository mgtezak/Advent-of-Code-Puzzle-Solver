# Third party
import pandas as pd

# Native
import os
from pathlib import Path

# Local
from config import PUZZLE_DATA


def get_puzzle_dir_path(year, day):
    return Path(f'advent_of_code/y{year}/d{day:02}')


def get_puzzle_db() -> pd.DataFrame:
    """Returns dataframe with titles of all puzzles and my results of completed ones."""

    dtypes = dict(title=object, solution_1=object, solution_2=object, 
                  runtime_1=float, runtime_2=float, vid_link=object)
    
    return pd.read_csv(PUZZLE_DATA, index_col=0, dtype=dtypes)



def get_puzzle_data(year: int, day: int) -> list:
    """Returns the title and my results of a given year and day's puzzle."""

    puzzle_id = 100 * year + day
    row = get_puzzle_db().loc[puzzle_id]
    puzzle_info = [None if pd.isna(x) else x for x in row]

    return puzzle_info



def get_title(year: int, day: int) -> str:
    """Retrieve title of a given year and day's puzzle."""

    return get_puzzle_data(year, day)[0]
    


def get_vid_link(year: int, day: int) -> str | None:
    """Check if vid link exists and if so return embedded link."""

    link = get_puzzle_data(year, day)[5]
    if not link:
        return None
    
    embedded_link = f'<iframe width="960" height="540" src="{link}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    return embedded_link



def put_vid_link(year: int, day: int, link: str) -> None:
    """Add youtube link for a given year and day's puzzle to the database."""

    puzzle_id = 100 * year + day
    df = get_puzzle_db()
    df.loc[puzzle_id, 'video_link'] = link
    df.to_csv(PUZZLE_DATA)



def del_vid_link(year: int, day: int) -> None:
    """Delete a youtube link for a given year and day's puzzle from the database."""

    puzzle_id = 100 * year + day
    df = get_puzzle_db()
    df.loc[puzzle_id, 'video_link'] = None
    df.to_csv(PUZZLE_DATA)



def get_puzzle_description(year: int, day: int) -> str | None:
    """"""

    path = get_puzzle_dir_path(year, day) / 'description.txt'
    if path.exists():
        return path.read_text()
    return None