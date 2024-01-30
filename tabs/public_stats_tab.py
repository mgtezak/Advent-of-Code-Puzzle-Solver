# Third party imports
import streamlit as st

# Local imports
from config import (PUBLIC_COMPLETION_PLOT, PUBLIC_COMPLETION_PLOT_2, SUBMISSION_TIMES_PLOT, 
                    USER_INFO_PLOT, TOP100_ACCUMULATED_PLOT, TOP10_ACCUMULATED_PLOT, TOP10_ANNUAL_PLOT)


def run():

    st.title("🌜🎁 Public Stats 🎁🌜")
    st.caption('*(Check out my original notebook on [kaggle](https://www.kaggle.com/code/michaeltezak/visualizing-advent-of-code-stats))*')
    st.divider()


    for _ in range(2):
        st.write('')
    st.subheader('Puzzle Completions')
    st.write('''
        - Last update: `2024-01-08`
        - `19,016,811` stars have been attained on Advent of Code in total
        - `9,978,376` part 1 completions
        - `9,038,435` part 2 completions
    ''')
    st.image(PUBLIC_COMPLETION_PLOT)
    st.write('''
        - Puzzle completions decrease per day as puzzles get harder
        - Puzzle completions increase per year, although 2015 and 2023 currently break this trend
        - The relatively low completions of 2023 can be explained by the recency of the event
        - The relatively high completions of 2015 can probably be explained in two ways:
            1. people are curious to see how it all started
            2. people are planning to do all of the years in chronological order, but haven't gotten very far yet 
        - There is a significant jump from 2019 to 2020 where completions double – I wonder if this can partially be explained by the Covid lockdowns (although they happened in 2020 before the event, so maybe not) 
    ''')
    st.image(PUBLIC_COMPLETION_PLOT_2)


    st.write('')
    st.divider()
    st.subheader('Submission Times')
    st.write('''
        - On average the first leaderboard entry occurs around 7 minutes for part 2 (4 minutes for part 1)
        - On average it takes a bit less than 30 minutes for the leaderboard to fill up for part 2 (16 minutes for part 1)
        - However, these numbers vary strongly across the 25 days
        - Day 22 has the highest mean submission time: 46 minutes (part 2)
        - The longest it ever took to fill up the leaderboard was day 19, 2015: 3 hours and 52 minutes
        - There are 3 leaderboard entries under 20 seconds (*highly sus if you ask me...*):
            1. 2022–3–1: 10 seconds by ostwilkens 
            2. 2023–1–1: 12 seconds by (anonymous user #640116)
            3. 2022–4–1: 16 seconds by max-sixty
    ''')    
    st.image(SUBMISSION_TIMES_PLOT)


    st.write('')
    st.divider()
    st.subheader('User Stats')
    st.write('''
        - `5,460` users in total on the leaderboard
        - Somewhat significant but weak positive correlation between having a high number of total accumulated points and being a supporter
        - Much weaker (perhaps insignificant) correlations between one's points and being a sponsor (pos) or participating anonymously (neg)
        - For the last two years there have been just as many old users on the leaderboard as new users 
    ''')    
    st.image(USER_INFO_PLOT) 
    st.write('''
        *Anonymity*
        - Anonymous AoC'ers are almost equally as likely to have high performances and to be financially supportive
        - 5 among the top 100 AoC-ers are anonymous, which is only slightly subproportional (they represent 7.8% of the total leaderboard)
        - The highest annual score ever achieved was by an anonymous user
        - Why be anonymous? Perhaps they don't seek fame at all and are just in it for the love of the game. Perhaps they don't want their bosses finding out, what they spend much of their productive energy on :-P
    ''') 
    st.image(TOP10_ANNUAL_PLOT) 
    st.image(TOP100_ACCUMULATED_PLOT)
    st.write('''
        *All-Time MVPs*
        - For most of AoC's history, **Robert Xiao** has been at the top in terms of total annually accumulated points
        - However, **betaveros** has had a very steep rise from 2017 till 2022 and if his trajectory had continued into 2023, he'd be #1 right now
        - Everybody in the the top 10 has been competing since 2017 at least
    ''')
    st.image(TOP10_ACCUMULATED_PLOT)
    st.write('')
    st.divider()