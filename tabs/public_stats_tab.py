# Third party imports
import streamlit as st

# Local imports
# from utils.toolbox import get_completed_stat
from config import PUBLIC_COMPLETION_PLOT,TOP_TEN_PLOT


def run():
    st.title("🌜🎁 Public Stats 🎁🌜")

    st.divider()
    for _ in range(2):
        st.write('')

    st.image(PUBLIC_COMPLETION_PLOT)

    st.write('')
    st.divider()
    st.write('')


    st.image(TOP_TEN_PLOT)
    st.divider()
