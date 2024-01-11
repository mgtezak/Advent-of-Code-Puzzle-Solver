# Third party
import pandas as pd
import numpy as np

# Native
from pathlib import Path

# Local
from config import PUZZLE_DATA



def get_puzzle_dir_path(year, day) -> Path:
    """Returns a Path object for the directory of a given year and day's puzzle."""

    return Path(f'advent_of_code/y{year}/d{day:02}')



def get_puzzle_db() -> pd.DataFrame:
    """Returns dataframe with titles of all puzzles and my results of completed ones."""

    dtypes = dict(title=object, solution_1=object, solution_2=object, 
                  runtime_1=float, runtime_2=float, vid_link=object)
    
    return pd.read_csv(PUZZLE_DATA, index_col=0, dtype=dtypes)



def get_puzzle_info(year: int, day: int) -> list:
    """Returns the title and my results of a given year and day's puzzle."""

    puzzle_id = 100 * year + day
    row = get_puzzle_db().loc[puzzle_id]
    row_dict = row.replace(np.nan, None).to_dict()
    return row_dict



def get_title(year: int, day: int) -> str:
    """Retrieve title of a given year and day's puzzle."""

    return get_puzzle_info(year, day)['title']
    


def get_vid_link(year: int, day: int) -> str | None:
    """Check if vid link exists and if so return embedded link."""

    video_id = get_puzzle_info['video_id']
    if not video_id:
        return None
    
    embedded_link = f'<iframe width="960" height="540" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    return embedded_link



def put_vid_link(year: int, day: int, link: str) -> None:
    """Add youtube link for a given year and day's puzzle to the database."""

    if '?si=' in link:
        video_id = link.split('?si=')[0].split('embed/')[1]
    if '?watch=' in link:
        video_id = link.split('?watch=')[1]

    puzzle_id = 100 * year + day
    df = get_puzzle_db()
    df.loc[puzzle_id, 'video_id'] = video_id
    df.to_csv(PUZZLE_DATA)



def del_vid_link(year: int, day: int) -> None:
    """Delete a youtube link for a given year and day's puzzle from the database."""

    puzzle_id = 100 * year + day
    df = get_puzzle_db()
    df.loc[puzzle_id, 'video_id'] = None
    df.to_csv(PUZZLE_DATA)



def get_puzzle_description(year: int, day: int) -> str | None:
    """Retrieves the content of a given puzzle's description file if it exists."""

    path = get_puzzle_dir_path(year, day) / 'description.txt'
    if path.exists():
        return path.read_text()
    return None