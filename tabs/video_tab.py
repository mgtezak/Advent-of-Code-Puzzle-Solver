import streamlit as st


def run(video_link):
    st.write('')
    st.markdown(video_link, unsafe_allow_html=True)