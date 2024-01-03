# Third party imports
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

# Local imports
from config import MLP_STYLE_PATH, TEXT_COLOR, PRIMARY_COLOR, PROGRESS_PLOT, RUNTIME_PLOT
from utils.handle_puzzle_data import get_puzzle_db


plt.style.use(MLP_STYLE_PATH)


def get_plot_df():
    """Prepare data for plotting by stacking solutions 1&2 and runtime 1&2,
    resulting in one row for each puzzle part.
    """
    df = get_puzzle_db()
    df.index = df.index.astype(str)
    df['year'] = df.index.str.slice(0, 4).astype(int)
    df['day'] = df.index.str.slice(4, 6).astype(int)
    df_part1 = df[['year', 'day', 'solution_1', 'runtime_1']].copy().assign(part=1)
    df_part2 = df[['year', 'day', 'solution_2', 'runtime_2']].copy().assign(part=2)
    df_part1.rename(columns={'solution_1': 'solution', 'runtime_1': 'runtime'}, inplace=True)
    df_part2.rename(columns={'solution_2': 'solution', 'runtime_2': 'runtime'}, inplace=True)
    df_stacked = pd.concat([df_part1, df_part2]).dropna().reset_index(drop=True)
    return df_stacked



def plot_my_progress(savefig=True):
    """Scatterplot with a red dot for each completed puzzle."""

    # Get data
    df = get_plot_df()

    # Create figure and plot
    ax = plt.subplots(figsize=(15, 5))[1]
    sns.scatterplot(data=df, x='day', y='year', marker='o', color=PRIMARY_COLOR, edgecolor=PRIMARY_COLOR, s=140, ax=ax, zorder=2, alpha=0.9)
    ax.set_title('My Advent of Code Progress')
    ax.set_xlabel('Day')
    ax.set_ylabel('Year')
    ax.invert_yaxis()
    ax.set_xticks(np.arange(1, 26, 1))
    ax.set_xlim(0.6, 25.4)

    # Save the plot
    if savefig:
        plt.savefig(PROGRESS_PLOT)



def plot_my_runtime(savefig=True):
    """Three barplots: runtime vs year, day & part. Two colors: red for the mean and a yellow for the median runtime."""

    # Get data
    df = get_plot_df()

    # Create figure, GridSpec layout and axes
    fig = plt.figure(figsize=(15, 10))
    gs = gridspec.GridSpec(2, 3)                    # 2 rows, 3 columns
    ax1 = fig.add_subplot(gs[0, :])                 # Spans all 3 columns in the first row
    ax2 = fig.add_subplot(gs[1, :2])                # Spans first 2 columns in the second row
    ax3 = fig.add_subplot(gs[1, 2], sharey=ax2)     # Spans last column in the second row

    # Create plots
    for x, ax in zip(('day', 'year', 'part'), (ax1, ax2, ax3)):
        sns.barplot(x=x, y='runtime', data=df, ax=ax, color=PRIMARY_COLOR, estimator='mean', errorbar=None, label='Mean' if x=='day' else None, zorder=2)
        sns.barplot(x=x, y='runtime', data=df, ax=ax, color=TEXT_COLOR, estimator='median', errorbar=None, label='Median' if x=='day' else None, zorder=3)
        ax.set_title(f'Runtime vs {x.capitalize()}')
        ax.set_xlabel(x.capitalize())
        ax.set_ylabel('Runtime in seconds' if ax in (ax1, ax2) else '')
        ax.grid(True)

    # Save the plot 
    if savefig:     
        plt.savefig(RUNTIME_PLOT)