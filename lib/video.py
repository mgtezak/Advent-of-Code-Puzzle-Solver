# External imports
import pandas as pd

# Native imports
import os

# Local imports
from config import MAX_YEAR, VIDEO_DB



def initialize_vid_db(overwrite=False):
    if not overwrite and os.path.exists(VIDEO_DB):
        print('Video DB already exists. Set overwrite=True')
        return
    
    data = []
    for year in range(2015, MAX_YEAR+1):
        for day in range(1, 26):
            data.append([year, day, 'no link'])
    df = pd.DataFrame(data, columns=['year', 'day', 'link'])
    df.to_csv(VIDEO_DB, index=False)
    return


def get_vid_db():

    if not os.path.exists(VIDEO_DB):
        initialize_vid_db()

    df = pd.read_csv(VIDEO_DB)
    return df


def get_vid_link(year, day):
    df = get_vid_db()
    row = df.loc[(df.year==year) & (df.day==day), 'link']
    return row.iloc[0]


def add_vid_link(year, day, link):
    df = get_vid_db()
    df.loc[(df.year==year) & (df.day==day), 'link'] = link
    df.to_csv(VIDEO_DB, index=False)
    return