# External imports
import streamlit as st
from collections import OrderedDict

from tabs import solver_tab, stats_tab, about_tab
from my_functions import utils


st.set_page_config(
    page_title="Advent-of-Code-Puzzle-Solver", 
    page_icon=":christmas_tree:", 
    layout="wide"
)

with open('assets/style.css') as style:
    st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)


def run():

    if not st.session_state:
        st.snow()

    TABS = OrderedDict({
        '🎅🏻 About this Project': about_tab,
        '🎄 Puzzle-Solver': solver_tab,
        '🎁 Stats-n-Graphs': stats_tab,
    })

    st.sidebar.image('assets/aoc_tree.png')

    current_tab = st.sidebar.radio('Content:', TABS.keys(), on_change=utils.reset_puzzle_solver)

    for _ in range(7):
        st.sidebar.write('')

    st.sidebar.markdown('''
        <span style="font-size: 0.9em;">Links:</span>   
        <a href="https://mgtezak.github.io" style="color: #FFD700; font-weight: Normal;"> ~ My Website</a>  
        <a href="https://github.com/mgtezak" style="color: #FFD700; font-weight: Normal;"> ~ Github</a>  
    ''', unsafe_allow_html=True)

    TABS[current_tab].run()


if __name__ == '__main__':
    run()