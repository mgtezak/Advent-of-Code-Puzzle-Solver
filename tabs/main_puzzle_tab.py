# Third party imports
import streamlit as st

# Native imports
from collections import OrderedDict

# Local imports
from utils.toolbox import reset_puzzle_solver, get_valid_days, get_valid_years
from utils.handle_puzzle_data import get_puzzle_info, get_puzzle_description
from .sub_tabs import interactive_tab, source_code_tab, description_tab



def run():
    st.title(f'✨🎄 Advent of Code Puzzle Solver 🎄✨')
    st.divider()

    cols = st.columns(5)
    year = cols[0].selectbox('Year:', get_valid_years(), key='year', on_change=reset_puzzle_solver)
    day = cols[1].selectbox('Day:', get_valid_days(year), key='day', on_change=reset_puzzle_solver)
    
    puzzle_info = get_puzzle_info(year, day)
    description = get_puzzle_description(year, day)

    sub_tabs = OrderedDict()

    runtimes = (puzzle_info['runtime_1'], puzzle_info['runtime_2'])
    sub_tabs['Get Your Solution'] = (interactive_tab, year, day, runtimes)
    sub_tabs['View Source Code'] = (source_code_tab, year, day)

    if (video := puzzle_info['video_id']):
        sub_tabs['Description & Approach (+Video)'] = (description_tab, description, video)
    elif description:
        sub_tabs['Description & Approach'] = (description_tab, description)
    
    st.header(puzzle_info['title'])
    st.caption(f'[*(link to the puzzle)*](https://adventofcode.com/{year}/day/{day})')

    for tab, (run_tab, *args) in zip(st.tabs(sub_tabs), sub_tabs.values()):

        with tab:
            st.write('')
            run_tab(*args)