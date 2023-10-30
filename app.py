# External imports
import streamlit as st
# from streamlit_option_menu import option_menu
from collections import OrderedDict

# Internal imports
from tabs import solver_tab, stats_tab, about_tab
from my_functions import aoc, utils, db


st.set_page_config(
    page_title="Advent-of-Code-Puzzle-Solver", 
    page_icon=":christmas_tree:", 
    layout="wide"
)

with open('assets/style.css') as style:
    st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)

if not st.session_state:
    st.snow()

TABS = OrderedDict({
    '🎄 Puzzle-Solver': solver_tab,
    '🎁 Stats-n-Graphs': stats_tab,
    '🎅🏻 About this Project': about_tab,
})

tab = st.sidebar.radio('Content', TABS.keys(), key='tab', on_change=utils.reset_puzzle_solver)

# ['✨🎄Puzzle-Solver🎄✨💫', '🕯️🎁Stats-n-Graphs🎁🕯️', '🌟🎅🏻About this Project🎅🏻🌟']

# st.title(f'✨🎄Advent of Code {year}🎄✨')

TABS[tab].run()