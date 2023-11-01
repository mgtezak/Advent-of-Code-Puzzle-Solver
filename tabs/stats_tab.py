import streamlit as st
from my_functions import db

PLOTS_PATH = 'assets/'

def run():
    st.title("💫🎁 Stats-n-Graphs 🎁💫")

    for _ in range(5):
        st.write('')

    st.image(PLOTS_PATH + 'completion_plot.png', caption=db.get_completed_stat() + "   \n Note: I haven't yet uploaded any of the ones past day 10. Will update soon!")
    
    for _ in range(5):
        st.write('')

    st.image(PLOTS_PATH + 'runtime_plot.png', caption="Most of the solution functions uploaded so far, execute in just a few microseconds. However there are a few outliers, with a much longer runtime resulting in a large difference between the mean and the median.")

    # st.image(PLOTS_PATH + 'runtime_year_plot.png')

    # st.image(PLOTS_PATH + 'runtime_day_plot.png')

    # st.image(PLOTS_PATH + 'runtime_part_plot.png', width=600)