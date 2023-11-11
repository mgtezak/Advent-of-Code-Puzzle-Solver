# External imports
import streamlit as st

# Native imports
from collections import OrderedDict

# Local imports
import tabs
from lib import utils
from config import SIDEBAR_IMG, STYLE


st.set_page_config(
    page_title="Advent-of-Code-Puzzle-Solver", 
    page_icon=":christmas_tree:", 
    layout="wide"
)

with open(STYLE, 'r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def run():

    if not st.session_state:
        st.snow()
        utils.reboot_app()

    TABS = OrderedDict({
        '🎅🏻 About this Project': tabs.about_this_project,
        '🎄 Puzzle Solver': tabs.puzzle_solver,
        '🎁 Stats-n-Graphs': tabs.stats_n_graphs,
    })

    st.sidebar.image(SIDEBAR_IMG)

    current_tab = st.sidebar.radio('Content:', TABS.keys(), on_change=utils.reset_puzzle_solver)

    for _ in range(5):
        st.sidebar.write('')

    st.sidebar.markdown('''
        <span style="font-size: 0.9em;">Links:</span>   
        <a href="https://mgtezak.github.io" style="color: #FFD700; font-weight: Normal;"> ~ My Website</a>  
        <a href="https://github.com/mgtezak" style="color: #FFD700; font-weight: Normal;"> ~ My Github</a>
    ''', unsafe_allow_html=True)

    TABS[current_tab].run()


if __name__ == '__main__':
    run()