# External imports
import streamlit as st
# from streamlit_option_menu import option_menu

# Internal imports
from my_functions.solve import *
from my_functions.db import *
from my_functions.utils import *
from messages import *

st.set_page_config(
    page_title="Advent-of-Code-Solver", 
    page_icon=":christmas_tree:", 
    layout="wide"
)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if not st.session_state:
    st.snow()

year = st.sidebar.radio('Year:', list(reversed(range(2019, 2023))), key='year', on_change=return_to_puzzle_input)

st.title(f'✨🎄Advent of Code {year}🎄✨')
day = st.selectbox('Day:', get_valid_days(year), key='day', on_change=return_to_puzzle_input)

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
    if col1.button('Solve part 1', key='solve1') or st.session_state.get('show_solution_1', False):
        solution = get_solution(year, day, 1)
        if solution:
            st.write('')
            st.write('The solution for part 1 is:')
            st.subheader(solution)
            st.divider()
            with st.expander('Let me see the code!'):
                st.text(get_source_code(year, day, 1))
            st.session_state['show_solution_1'] = False
        else:
            try:
                with st.spinner('Calculating solution...'):
                    solution = solve(year, day, 1)
                put_solution(year, day, 1, solution)
                st.session_state['show_solution_1'] = True
            except:
                st.error(failure_to_solve_msg)
                st.session_state['bad_input'] = True
            if st.session_state.get('show_solution_1', False):
                st.rerun()

    if col2.button('Solve part 2', key='solve2') or st.session_state.get('show_solution_2', False):
        solution = get_solution(year, day, 2)
        if solution:
            st.write('')
            st.write('The solution for part 2 is:')
            st.subheader(solution)
            st.divider()
            with st.expander('Let me see the code!'):
                st.text(get_source_code(year, day, 2))
            st.session_state['show_solution_2'] = False
        else:
            try:
                with st.spinner('Calculating solution...'):
                    solution = solve(year, day, 2)
                put_solution(year, day, 2, solution)
                st.session_state['show_solution_2'] = True
            except:
                st.error(failure_to_solve_msg)
                st.session_state['bad_input'] = True
            if st.session_state.get('show_solution_2', False):
                st.rerun()

    if col3.button("Change puzzle input"):
        st.session_state['solution'] = False
        st.rerun()