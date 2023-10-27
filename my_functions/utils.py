import streamlit as st
from my_functions.solve import function_dict


def return_to_puzzle_input():
    st.session_state['solution'] = False


def get_valid_days(year):
    return [d for d in range(1, 26) if f'aoc{year}_day{d}_part1' in function_dict]
