import streamlit as st


from utils.handle_solutions import get_source_code


def run(year, day):

    st.write('')
    col1, col2, _ = st.columns(3)

    if col1.button('Part 1'):
        st.code(get_source_code(year, day, 1))

    if day < 25 and col2.button('Part 2'):            
        st.code(get_source_code(year, day, 2))