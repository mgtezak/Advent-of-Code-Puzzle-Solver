# Third party imports
import streamlit as st

# Native imports
from collections import OrderedDict

# Local imports
from utils.toolbox import reset_puzzle_solver, get_valid_days, get_valid_years
from utils.handle_puzzle_data import get_title, get_vid_link, get_puzzle_description
from .sub_tabs import description_tab, interactive_tab, source_code_tab, video_tab



def run():
    st.title(f'✨🎄 Advent of Code Puzzle Solver 🎄✨')
    st.divider()

    cols = st.columns(5)
    year = cols[0].selectbox('Year:', get_valid_years(), key='year', on_change=reset_puzzle_solver)
    day = cols[1].selectbox('Day:', get_valid_days(year), key='day', on_change=reset_puzzle_solver)
    
    title = get_title(year, day)
    description = get_puzzle_description(year, day)
    video_link = get_vid_link(year, day)

    st.header(title)
    st.caption(f'[*(link to the puzzle)*](https://adventofcode.com/{year}/day/{day})')

    sub_tabs = OrderedDict([
        ('Description & Approach', (description_tab, description)), 
        ('Get Your Solution', (interactive_tab, year, day)), 
        ('View Solution Code', (source_code_tab, year, day)), 
        ('Video Explanation', (video_tab, video_link))
    ])
    
    if description is None:     # Not all puzzles have a description or video
        del sub_tabs['Description & Approach']
    if video_link is None:
        del sub_tabs['Video Explanation']

    for tab, (run_tab, *args) in zip(st.tabs(sub_tabs), sub_tabs.values()):

        with tab:
            st.write('')
            run_tab(*args)

    st.divider()