# Third party imports
import streamlit as st

# Local imports
from lib.utils import reset_puzzle_solver, get_valid_days, display_fail_msg
from lib.puzzle_input import get_temp_puzzle_input, put_temp_puzzle_input, del_temp_puzzle_input
from lib.solution import get_temp_solution, put_temp_solution, del_temp_solution, display_solution, get_source_code, solve
from lib.puzzle import get_title, get_vid_link
from config import MAX_YEAR



def run():
    st.title(f'✨🎄 Advent of Code Puzzle Solver 🎄✨')
    st.divider()

    cols = st.columns(5)
    year = cols[0].selectbox('Year:', list(reversed(range(2015, MAX_YEAR+1))), key='year', on_change=reset_puzzle_solver)
    day = cols[1].selectbox('Day:', get_valid_days(year), key='day', on_change=reset_puzzle_solver)
    
    puzzle_title = get_title(year, day)
    st.header(puzzle_title)

    video_link = get_vid_link(year, day)

    if video_link is None:
        generate_tab, display_code_tab = st.tabs(['Solve the Puzzle', 'Display the Code'])
    else:
        generate_tab, display_code_tab, video_tab = st.tabs(['Solve the Puzzle', 'Display the Code', 'Video Explanation'])

    with generate_tab:
        st.write('')

        # GET PUZZLE INPUT
        if not st.session_state.get('solution', False):

            input_provided = st.session_state.get('puzzle_memory', False)
            input_retrieved = st.session_state.get('use_prev_input', False)

            # default: no puzzle input yet provided or retrieved
            if not (input_provided or input_retrieved):    
                if get_temp_puzzle_input(year, day):
                    col1, col2 = st.columns([3, 8])
                    col1.info('Previous puzzle input detected.')
                    st.button('Use previous puzzle input', key='use_prev_input')

                st.write('Enter puzzle input:')
                st.text_area('Puzzle input:', key='puzzle_memory', label_visibility='collapsed')
                st.session_state['solution'] = False
                st.button('Submit')

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
                        display_fail_msg()
                        del_temp_puzzle_input(year, day)

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
                        display_fail_msg()
                        del_temp_puzzle_input(year, day)

                    if st.session_state.get('show_solution_2', False):
                        st.rerun()

            if col3.button("Change puzzle input"):
                st.session_state['solution'] = False
                st.rerun()

    with display_code_tab:
        st.write('')
        col1, col2, _ = st.columns(3)

        if col1.button('Part 1'):
            st.code(get_source_code(year, day, 1))
        
        if day < 25 and col2.button('Part 2'):            
            st.code(get_source_code(year, day, 2))

    if video_link:
        with video_tab:
            st.write('')
            st.markdown(video_link, unsafe_allow_html=True)
    
    st.divider()
