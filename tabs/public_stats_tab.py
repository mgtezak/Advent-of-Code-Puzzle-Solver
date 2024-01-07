# Third party imports
import streamlit as st

# Local imports
# from utils.toolbox import get_completed_stat
from config import PUBLIC_COMPLETION_PLOT


def run():
    st.title("🌜🎁 Public Stats 🎁🌜")

    st.divider()
    for _ in range(2):
        st.write('')

    st.image(PUBLIC_COMPLETION_PLOT)

    st.write('')
    st.divider()
    st.write('')

    # st.write("""
    #     As is clearly visible in the following barplots, most of the solution functions uploaded so far, 
    #     execute in just a few milliseconds. 
    #     However there are a few outliers with a much longer runtime resulting in a large 
    #     difference between the mean and the median. 
    # """)
    # st.write('')
    # st.image(RUNTIME_PLOT)
    # st.divider()
