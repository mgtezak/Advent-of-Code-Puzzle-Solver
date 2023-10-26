# External imports
import streamlit as st
from streamlit_option_menu import option_menu

# Native imports
import inspect

# Internal imports
from my_functions.solve import solve_function
from my_functions.db import *


st.set_page_config(layout='wide')

def reset():
    st.session_state['solution'] = False

def get_valid_days(year):
    return [d for d in range(1, 26) if f'aoc{year}_day{d}_part1' in solve_function]

year = st.sidebar.radio('Year:', list(range(2021, 2023)), key='year', on_change=reset)

st.title(f'Advent of Code {year}')
day = st.selectbox('Day:', get_valid_days(year), key='day', on_change=reset)

# GET PUZZLE INPUT
if not st.session_state.get('solution', False):

    input_provided = st.session_state.get('puzzle_memory', False)
    input_retrieved = st.session_state.get('use_prev_input', False)

    # default: no puzzle input yet provided or retrieved
    if not (input_provided or input_retrieved):    
        if get_puzzle_input(year, day):
            if not st.session_state.get('bad_input', False):
                st.write('Previous puzzle input detected.')
                st.button('Use previous puzzle input', key='use_prev_input')
        else:
            st.write('No previous puzzle input detected for this challenge.')
        st.write('Enter puzzle input:')
        new_puzzle_input = st.text_area('Puzzle input:', key='puzzle_memory', label_visibility='collapsed')
        st.session_state['solution'] = False
        st.button('Submit')

    elif input_retrieved:                           # puzzle input retrieved from db
        st.session_state['solution'] = True
        st.rerun()
    else:                                           # puzzle input stored in memory to be stored in db
        puzzle_input = st.session_state['puzzle_memory'].strip()
        if not puzzle_input:
            st.error('You did not provide any puzzle input.')
            st.session_state['solution'] = False
            st.button('Try again!')
        else:
            put_puzzle_input(year, day, puzzle_input)
            del_solution(year, day)
            st.session_state['solution'] = True
            st.rerun()


# GET SOLUTION
else:
    col1, col2, col3 = st.columns(3)
    puzzle_input = get_puzzle_input(year, day)
    failure_msg = """
        :scream: Oops, something went wrong!  
        :thinking_face: Perhaps there's an issue with the puzzle input you provided...  
        :crossed_fingers: Please try re-entering it.
    """

    if col1.button('Solve part 1', key='solve1') or st.session_state.get('show_solution_1', False):
        solution = get_solution(year, day, 1)
        function = solve_function[f'aoc{year}_day{day}_part1']
        if solution:
            st.write('')
            st.write('The solution for part 1 is:')
            st.subheader(solution)
            st.divider()
            with st.expander('Let me see the code!'):
                st.text(inspect.getsource(function))
            st.session_state['show_solution_1'] = False
        else:
            try:
                with st.spinner('Calculating solution...'):
                    solution = function(puzzle_input)
                put_solution(year, day, 1, solution)
                st.session_state['show_solution_1'] = True
            except:
                st.error(failure_msg)
                st.session_state['bad_input'] = True
            if st.session_state.get('show_solution_1', False):
                st.rerun()

    if col2.button('Solve part 2', key='solve2') or st.session_state.get('show_solution_2', False):
        solution = get_solution(year, day, 2)
        function = solve_function[f'aoc{year}_day{day}_part2']
        if solution:
            st.write('')
            st.write('The solution for part 2 is:')
            st.subheader(solution)
            st.divider()
            with st.expander('Let me see the code!'):
                st.text(inspect.getsource(function))
            st.session_state['show_solution_2'] = False
        else:
            try:
                with st.spinner('Calculating solution...'):
                    solution = function(puzzle_input)
                put_solution(year, day, 2, solution)
                st.session_state['show_solution_2'] = True
            except:
                st.error(failure_msg)
                st.session_state['bad_input'] = True
            if st.session_state.get('show_solution_2', False):
                st.rerun()

    if col3.button("Change puzzle input"):
        st.session_state['solution'] = False
        st.rerun()