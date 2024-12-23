# Third party imports
import streamlit as st
import numpy as np

# Native imports
from datetime import datetime, timedelta

# Local imports
from config import PUZZLE_DATA, TEMP_STORAGE, MAX_YEAR
from .handle_puzzle_data import get_puzzle_db, get_puzzle_dir_path
from .handle_puzzle_input import is_example_input
from .handle_solutions import solve
from .handle_grids import generate_grids



def display_generated_grids(letters):
    """"""
    
    for label, result, unknown in generate_grids(letters):
        st.text(f'Your message in a {label} grid:\n\n' + result)
        if unknown:
            s, are = ('s', 'are') if len(unknown) > 1 else ('', 'is')
            unknown = "".join(unknown)
            st.caption(f'Unfortunately the character{s} "{unknown}" {are} not included in this alphabet.')
        st.divider()


def display_example_inputs(example_inputs: list[tuple[str, int]]) -> None:
    """Displays example inputs."""

    if type(example_inputs[0]) == dict:
        example_inputs = reformat_example_inputs(example_inputs)
        
    st.divider()
    st.write(f'Example input{"s" if len(example_inputs) > 1 else ""}:')
    for example_input, compatibility in example_inputs:
        st.code(example_input)
        if compatibility != 3:
            st.caption(f'(Only works with part {compatibility})')
        st.divider()


def reformat_example_inputs(example_inputs):
    old_format = []
    for d in example_inputs:
        compatibility = 3 if d['part1'] and d['part2'] else 1 if d['part1'] else 2
        old_format.append([d['input'], compatibility])

    return old_format


def display_video(video_id):
    """"""

    embedded_link = f'<iframe width="960" height="540" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    st.markdown(embedded_link, unsafe_allow_html=True)



def reboot_app() -> None:
    """Temporary storage gets cleared of all files that haven't been modified for over an hour."""

    TEMP_STORAGE.mkdir(exist_ok=True)
    now = datetime.now()

    for file in TEMP_STORAGE.iterdir():
        latest_update = datetime.fromtimestamp(file.stat().st_mtime)

        if now - latest_update > timedelta(days=1):
            file.unlink()
    


def reset_puzzle_solver() -> None:
    """Resets the page, so that new puzzle input can be provided."""

    st.session_state['solution'] = False



def get_valid_days(year: int) -> list[int]:
    """Returns list of currently available days for given year."""

    return [day for day in range(1, 26) if solution_exists(year, day)]



def get_valid_years() -> list[int]:
    """Returns list of currently available years in reverse order."""

    return list(range(MAX_YEAR, 2014, -1))



def get_completed_stat() -> str:
    """Returns formatted string describing the current progress."""

    df = get_puzzle_db()
    completed = df.runtime_1.count()
    total = df.shape[0]
    pct = int(completed/total * 100)
    return f"So far I've completed {completed} ({pct}%) of the available total of {total} two-part daily challenges."



def display_fail_msg(year: int, day: int) -> None:
    """Failure message gets displayed if the solving function throws an error."""

    if is_example_input(year, day):
        st.error("""
            :man-tipping-hand: This example input only works with the other part.  
            :star: Try entering your own input.
        """)
    else:
        st.error("""
            :scream: Oops, something went wrong!  
            :thinking_face: Perhaps there's an issue with the puzzle input you provided...  
            :crossed_fingers: Check if you copied it correctly and try re-entering it.
            :email: If this doesn't help, drop me a message: mgtezak@gmail.com
        """)



def solution_exists(year: int, day: int) -> bool:
    """Checks whether or not I have solved a given puzzle yet."""

    return get_puzzle_dir_path(year, day).exists()



# def get_valid_parts(year, day):
#     if not solution_exists(year, day):
#         return []
#     if day == 25:
#         return [1]
#     return [1, 2]



def put_my_results(year: int, day: int) -> None:
    """To add a new solution, first add its solution functions, then call this function 
    and it will automatically calculate solutions and runtimes and add them to the database.
    """
    solution_1, runtime_1 = solve(year, day, 1, True)
    solution_2, runtime_2 = solve(year, day, 2, True) if day < 25 else None, np.nan
    results = [solution_1, solution_2, runtime_1, runtime_2]

    puzzle_id = year * 100 + day
    df = get_puzzle_db()
    df.loc[puzzle_id, 'solution_1':'runtime_2'] = results
    df.to_csv(PUZZLE_DATA)