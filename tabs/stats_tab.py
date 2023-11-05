import streamlit as st
from my_functions import db

PLOTS_PATH = 'assets/'

def run():
    st.title("💫🎁 Stats-n-Graphs 🎁💫")

    st.divider()
    for _ in range(2):
        st.write('')

    st.image(PLOTS_PATH + 'completion_plot.png', caption=db.get_completed_stat() + "   \n Note: I haven't yet uploaded any of the ones past day 10. Will update soon!")

    st.write('')
    st.divider()
    st.write('')
    s = """
    As is clearly visible in the following barplots, most of the solution functions uploaded so far, 
    execute in just a few microseconds. 
    However there are a few outliers with a much longer runtime resulting in a large 
    difference between the mean and the median.
    
    """

    # st.image(PLOTS_PATH + 'runtime_plot.png', caption=)

    st.write(s)
    st.write('')
    col1, col2 = st.columns(2)
    col1.image(PLOTS_PATH + 'runtime_year_plot.png')
    col1.image(PLOTS_PATH + 'runtime_day_plot.png')
    col2.image(PLOTS_PATH + 'runtime_part_plot.png')
    st.divider()
