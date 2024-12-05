# External imports
import streamlit as st

# Native imports
from collections import OrderedDict

# Local imports
from config import SIDEBAR_IMG, STYLE
from utils.toolbox import reboot_app, reset_puzzle_solver
from tabs import main_puzzle_tab, personal_stats_tab, about_tab, public_stats_tab, grid_letter_tab


st.set_page_config(
    page_title="Advent-of-Code-Puzzle-Solver", 
    page_icon=":christmas_tree:", 
    layout="wide"
)


st.markdown(f'<style>{STYLE.read_text()}</style>', unsafe_allow_html=True)


def run():

    if not st.session_state:
        reboot_app()

    tabs = OrderedDict({
        '🎄 Puzzle Solutions': main_puzzle_tab,
        '⛄ Grid Decoding ': grid_letter_tab,        
        '🎁 Public Stats': public_stats_tab,
        '🦌 Personal Stats': personal_stats_tab,
        '🎅🏻 About': about_tab,
    })

    st.sidebar.image(SIDEBAR_IMG)

    current_tab = st.sidebar.radio('Content:', tabs.keys(), on_change=reset_puzzle_solver)

    for _ in range(5):
        st.sidebar.write('')

    st.sidebar.markdown('''
        <span style="font-size: 0.9em;">Links:</span>   
        <a href="https://github.com/mgtezak" style="color: #FFD700; font-weight: Normal;"> ~ My Github</a>  
        <a href="https://www.linkedin.com/in/mgtezak" style="color: #FFD700; font-weight: Normal;"> ~ My LinkedIn</a>  
    ''', unsafe_allow_html=True)

    tabs[current_tab].run()


if __name__ == '__main__':
    run()