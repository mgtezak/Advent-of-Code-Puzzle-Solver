import streamlit as st
from lib import db
from config import *


def run():
    st.title("💫🎁 Stats-n-Graphs 🎁💫")

    st.divider()
    for _ in range(2):
        st.write('')

    st.image(PROGRESS_PLOT, caption=db.get_completed_stat())

    st.write('')
    st.divider()
    st.write('')
    st.write("""
        As is clearly visible in the following barplots, most of the solution functions uploaded so far, 
        execute in just a few microseconds. 
        However there are a few outliers with a much longer runtime resulting in a large 
        difference between the mean and the median. 
    """)
    st.write('')
    st.image(RUNTIME_PLOT2)
    # st.image(PLOTS + 'runtime_year_plot.png')
    # st.image(PLOTS + 'runtime_day_plot.png')
    st.image(RUNTIME_PART_PLOT)
    st.divider()
