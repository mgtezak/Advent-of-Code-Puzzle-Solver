import streamlit as st

from my_functions import aoc, utils, db


def run():
    st.title(f'✨🎄 Advent of Code Puzzle Solver 🎄✨')
    st.write('')
    cols = st.columns(5)
    year = cols[0].selectbox('Year:', list(reversed(range(2015, 2023))), key='year', on_change=utils.reset_puzzle_solver)
    day = cols[1].selectbox('Day:', utils.get_valid_days(year), key='day', on_change=utils.reset_puzzle_solver)
    
    st.write('')
    generate_tab, display_code_tab = st.tabs(['Solve the Puzzle', 'Display the Code'])

    with generate_tab:
        st.write('')

        # GET PUZZLE INPUT
        if not st.session_state.get('solution', False):

            input_provided = st.session_state.get('puzzle_memory', False)
            input_retrieved = st.session_state.get('use_prev_input', False)

            # default: no puzzle input yet provided or retrieved
            if not (input_provided or input_retrieved):    
                if db.get_puzzle_input(year, day):
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
                puzzle_input = st.session_state['puzzle_memory'].rstrip()
                if not puzzle_input:
                    st.error('You did not provide any puzzle input.')
                    st.session_state['solution'] = False
                    st.button('Try again!')
                else:
                    db.put_puzzle_input(year, day, puzzle_input)
                    db.del_solution(year, day)
                    st.session_state['solution'] = True
                    st.rerun()


        # GET SOLUTION
        else:
            col1, col2, col3 = st.columns(3)
            if col1.button('Part 1', key='solve1') or st.session_state.get('show_solution_1', False):
                solution = db.get_solution(year, day, 1)
                if solution:
                    st.write('The solution for part 1 is:')
                    utils.display_solution(*solution)
                    st.divider()
                    st.session_state['show_solution_1'] = False
                else:
                    try:
                        with st.spinner('Calculating solution...'):
                            solution, runtime = aoc.solve(year, day, 1)
                        db.put_solution(year, day, 1, solution, runtime)
                        st.session_state['show_solution_1'] = True
                    except:
                        utils.display_fail_msg()
                        st.session_state['bad_input'] = True
                    if st.session_state.get('show_solution_1', False):
                        st.rerun()

            if col2.button('Part 2', key='solve2') or st.session_state.get('show_solution_2', False):
                solution = db.get_solution(year, day, 2)
                if solution:
                    st.write('The solution for part 2 is:')
                    utils.display_solution(*solution)
                    st.divider()
                    st.session_state['show_solution_2'] = False
                else:
                    try:
                        with st.spinner('Calculating solution...'):
                            solution, runtime = aoc.solve(year, day, 2)
                        db.put_solution(year, day, 2, solution, runtime)
                        st.session_state['show_solution_2'] = True
                    except:
                        utils.display_fail_msg()
                        st.session_state['bad_input'] = True
                    if st.session_state.get('show_solution_2', False):
                        st.rerun()

            if col3.button("Change puzzle input"):
                st.session_state['solution'] = False
                st.rerun()

    with display_code_tab:
        st.write('')
        col1, col2, _ = st.columns(3)
        if col1.button('Part 1'):
            st.text(aoc.get_source_code(year, day, 1))
        if col2.button('Part 2'):            
            st.text(aoc.get_source_code(year, day, 2))
