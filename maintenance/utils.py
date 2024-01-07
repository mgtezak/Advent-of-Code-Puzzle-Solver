# Third party
import pandas as pd
from bs4 import BeautifulSoup as bs

# Native
import re
import urllib

# Local
from config import PUZZLE_DATA
from utils.handle_puzzle_data import get_puzzle_db
from .plot_data import plot_current_completion_stats



def scrape_public_stats() -> None:
    """Scrapes the puzzle completion stats from the website and updates my puzzle data csv file."""

    index = []
    data = []
    columns = ['gold', 'silver']
    for year in range(2015, 2024):
        url = f'https://adventofcode.com/{year}/stats'
        page = urllib.request.urlopen(url)
        soup = bs(page, "html.parser")
        year_stats = soup.find(class_='stats').text
        for day_stats in reversed(re.findall('(\d+)\s+(\d+)\s+(\d+)', year_stats)):
            day, gold, silver = map(int, day_stats)
            index.append(year*100 + day)
            data.append((gold, silver))

    df = get_puzzle_db()
    df_stats = pd.DataFrame(index=index, data=data, columns=columns)
    df.update(df_stats)
    df.to_csv(PUZZLE_DATA)



def update_public_stats_plots() -> None:
    """Updates public data and recreates public stats plots."""
    
    scrape_public_stats()
    plot_current_completion_stats()