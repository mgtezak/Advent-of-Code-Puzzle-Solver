import streamlit as st

from utils.handle_puzzle_input import get_temp_puzzle_input, put_temp_puzzle_input, get_example_inputs
from utils.handle_solutions import get_temp_solution, put_temp_solution, del_temp_solution, display_solution, solve
from utils.toolbox import display_fail_msg, display_example_inputs
from utils.handle_solutions import get_source_code



def description_tab(description):
    st.write(description)



def source_code_tab(year, day):
    col1, col2, _ = st.columns(3)

    if col1.button('Part 1'):
        st.code(get_source_code(year, day, 1))

    if day < 25 and col2.button('Part 2'):            
        st.code(get_source_code(year, day, 2))



def video_tab(video_link):
    st.write()
    st.markdown(video_link, unsafe_allow_html=True)



def interactive_tab(year, day):

    # GET PUZZLE INPUT
    if not st.session_state.get('solution', False):

        input_provided = st.session_state.get('puzzle_memory', False)
        input_retrieved = st.session_state.get('use_prev_input', False)

        # default: no puzzle input yet provided or retrieved
        if not (input_provided or input_retrieved):  

            example_inputs = get_example_inputs(year, day)
            if example_inputs:
                st.write('Enter puzzle input (scroll down for example inputs):')
            else:
                st.write('Enter puzzle input:')

            st.text_area('Puzzle input:', key='puzzle_memory', label_visibility='collapsed')
            st.session_state['solution'] = False
            col1, col2 = st.columns([1, 2])
            col1.button('Submit new input')
            if get_temp_puzzle_input(year, day):
                col2.button('Use previous input', key='use_prev_input')

            if example_inputs:
                display_example_inputs(example_inputs)

        elif input_retrieved:                           # puzzle input retrieved from db
            st.session_state['solution'] = True
            st.rerun()

        else:                                           # puzzle input stored in memory to be stored in db
            puzzle_input = st.session_state['puzzle_memory'].rstrip()
            if not puzzle_input:
                st.error('You did not provide any puzzle input.')
                st.session_state['solution'] = False
                st.button('Try again!')

            else:
                put_temp_puzzle_input(year, day, puzzle_input)
                del_temp_solution(year, day)
                st.session_state['solution'] = True
                st.rerun()


    # GET SOLUTION
    else:
        col1, col2, col3 = st.columns(3)

        if col1.button('Part 1', key='solve1') or st.session_state.get('show_solution_1', False):
            solution = get_temp_solution(year, day, 1)
            if solution:
                st.write('The solution for part 1 is:')
                display_solution(*solution)
                st.session_state['show_solution_1'] = False

            else:
                try:
                    with st.spinner('Calculating solution...'):
                        solution, runtime = solve(year, day, 1)
                    put_temp_solution(year, day, 1, solution, runtime)
                    st.session_state['show_solution_1'] = True

                except:
                    display_fail_msg(year, day)

                if st.session_state.get('show_solution_1', False):
                    st.rerun()

        if day < 25 and col2.button('Part 2', key='solve2') or st.session_state.get('show_solution_2', False):
            solution = get_temp_solution(year, day, 2)
            if solution:
                st.write('The solution for part 2 is:')
                display_solution(*solution)
                st.session_state['show_solution_2'] = False

            else:
                try:
                    with st.spinner('Calculating solution...'):
                        solution, runtime = solve(year, day, 2)
                    put_temp_solution(year, day, 2, solution, runtime)
                    st.session_state['show_solution_2'] = True

                except:
                    display_fail_msg(year, day)
                    
                if st.session_state.get('show_solution_2', False):
                    st.rerun()

        if col3.button("Change puzzle input"):
            st.session_state['solution'] = False
            st.rerun()