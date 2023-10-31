import streamlit as st
from my_functions import db

PLOTS_PATH = 'assets/'

def run():
    st.title("💫🎁 Stats-n-Graphs 🎁💫")
    for _ in range(5):
        st.write('')
    st.image(PLOTS_PATH + 'completion_plot.png', caption=db.get_completed_stat() + "   \n Note: I haven't yet uploaded any of the ones past day 10. Will update soon!")
