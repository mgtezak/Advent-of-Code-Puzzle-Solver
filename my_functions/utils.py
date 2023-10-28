import streamlit as st
from my_functions.aoc import function_dict


def return_to_puzzle_input():
    st.session_state['solution'] = False


def get_valid_days(year):
    return [d for d in range(1, 26) if f'aoc{year}_day{d}_part1' in function_dict]


def display_solution(solution):
    if type(solution) is str and '\n' in solution:
        st.write('')
        st.text(solution)
    else:
        st.subheader(solution)


def display_fail_msg():
    st.error("""
        :scream: Oops, something went wrong!  
        :thinking_face: Perhaps there's an issue with the puzzle input you provided...  
        :crossed_fingers: Please try re-entering it.
    """)