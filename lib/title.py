# Third party
import pandas as pd
# from bs4 import BeautifulSoup as bs

# Native
import os

# Local
from config import TITLE_DB


def get_title_db() -> pd.DataFrame:
    """Returns all titles as pandas dataframe."""

    if not os.path.exists(TITLE_DB):
        pd.DataFrame(columns=['year', 'day', 'title']).to_csv(TITLE_DB, index=False)

    return pd.read_csv(TITLE_DB)



def get_title(year, day) -> str:
    """Fetches a single puzzle title from database."""

    df = get_title_db()
    row = df.loc[(df.year==year) & (df.day==day), 'title']
    if len(row) == 0:
        return ''
    
    return row.iloc[0]



# def populate_title_db():
#     data = []
#     for year in range(2015, MAX_YEAR+1):
#         for day in range(1, 26):
#             if year == MAX_YEAR and day > MAX_DAY:
#                 break
#             url = f"https://adventofcode.com/{year}/day/{day}"
#             page = urllib.request.urlopen(url)
#             soup = bs(page, "html.parser")
#             data.append([year, day, soup.h2.text])
#     df = pd.DataFrame(data, columns=['year', 'day', 'title'])
#     df.to_csv(TITLE, index=False)


# def add_recent_titles():
#     new_titles = []
#     for day in range(1, 26):
#         if day > MAX_DAY:
#             break
#         url = f"https://adventofcode.com/{MAX_YEAR}/day/{day}"
#         page = urllib.request.urlopen(url)
#         soup = bs(page, "html.parser")
#         new_titles.append([MAX_YEAR, day, soup.h2.text])

#     old_df = get_title_db()
#     new_df = pd.DataFrame(new_titles, columns=['year', 'day', 'title'])
#     df = pd.concat([old_df, new_df])
#     df.to_csv(TITLE, index=False)
