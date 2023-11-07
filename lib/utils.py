import streamlit as st
import json

from config import GRID_LETTER
from lib import aoc


def reset_puzzle_solver() -> None:
    st.session_state['solution'] = False


def get_valid_days(year: int) -> list[int]:
    return [d for d in reversed(range(1, 26)) if f'aoc{year}_day{d}_part1' in aoc.function_dict]


def display_solution(solution: int | str, runtime: int) -> None:
    if type(solution) is str and '\n' in solution:
        st.text('Visual output:\n' + solution)
        letters = read_grid(solution)
        if letters:
            st.subheader(letters)
    else:
        st.subheader(solution)
    st.caption(f"Runtime: {format_runtime(runtime)}")


def read_grid(grid) -> str | False:
    '''puzzles with grid letter output: 2016-8-2, 2018-10-1, 2019-8-2, 2021-13-2, 2022-10-2'''
    with open(GRID_LETTER, 'r') as f:
        grid_letters = json.load(f)
    lines = grid.split('\n')
    letter_width = 5 if len(lines) == 6 else 8
    letters = ''
    for col in range(0, len(lines[0]), letter_width):
        letter = '\n'.join([''.join(lines[row][col:col+letter_width]) for row in range(len(lines))])
        if letter not in grid_letters:
            return False
        letters += grid_letters[letter]
    return letters


def format_runtime(runtime: int) -> str:
    if runtime >= 0.01:
        return f'{runtime:.2f} seconds'
    return f'{int(runtime*1000)} milliseconds'


def display_fail_msg() -> None:
    st.error("""
        :scream: Oops, something went wrong!  
        :thinking_face: Perhaps there's an issue with the puzzle input you provided...  
        :crossed_fingers: Please try re-entering it.
    """)
