# Third party imports
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd

# Native
from datetime import datetime

# Local imports
from config import TEXT_COLOR, PRIMARY_COLOR, BACKGROUND_COLOR, MLP_STYLE_PATH
from config import PROGRESS_PLOT, RUNTIME_PLOT, PUBLIC_COMPLETION_PLOT
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



def get_public_stats_plot_df():
    """Prepares the data for my public stats plots."""

    df = get_puzzle_db()
    original_cols = list(df.columns)
    df['year'] = df.index // 100
    df['day'] = df.index % 100
    df = df[['year', 'day'] + original_cols]
    df = df.drop(columns=['title', 'solution_1', 'solution_2', 'video_link'])
    df['only_1'] = df.gold + df.silver
    return df



def plot_current_completion_stats() -> None:
    """Make 3D plot of current completion stats."""

    df = get_public_stats_plot_df()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_title('Current Completion Statistics', fontsize=9)
    ax.set_xlim(2023, 2015)
    ax.set_ylim(25, 1)
    ax.set_zlim(0, 320_000)
    ax.set_yticks(range(1, 26))

    labelsize = 5 
    ax.set_xlabel('Year', fontsize=labelsize)
    ax.set_ylabel('Day', fontsize=labelsize)

    ax.tick_params(axis='x', labelsize=labelsize)
    ax.tick_params(axis='y', labelsize=labelsize)
    ax.tick_params(axis='z', labelsize=labelsize)
    ax.zaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))

    ax.xaxis.set_pane_color(BACKGROUND_COLOR)
    ax.yaxis.set_pane_color(BACKGROUND_COLOR)
    ax.zaxis.set_pane_color(BACKGROUND_COLOR)
    ax.grid(False)

    linestyle = {'color': TEXT_COLOR, 'linewidth': 0.3, 'linestyle': '--', 'alpha': 0.5}
    for z in np.linspace(0, 300_000, 7):
        ax.plot3D([2023.8]*2, [0, 25], [z-11000]*2, **linestyle)
        ax.plot3D([2015, 2023.8], [0]*2, [z-11000]*2, **linestyle)

    cols = ['year', 'day', 'gold', 'silver']
    max_year_both, max_day_both, max_gold_both, max_silver_both = map(int, df.loc[df.gold.idxmax(), cols])
    min_year_both, min_day_both, min_gold_both, min_silver_both = map(int, df.loc[df.gold.idxmin(), cols])
    max_year_1, max_day_1, max_gold_1, max_silver_1 = map(int, df.loc[df.only_1.idxmax(), cols])
    min_year_1, min_day_1, min_gold_1, min_silver_1 = map(int, df.loc[df.only_1.idxmin(), cols])
    max_year_diff, max_day_diff, max_gold_diff, max_silver_diff = map(int, df.loc[df.silver.idxmax(), cols])
    min_year_diff, min_day_diff, min_gold_diff, min_silver_diff = map(int, df.loc[df.silver.idxmin(), cols])

    for year in range(2023, 2014, -1):
        xs = df[df['year']==year]['year']
        ys = df[df['year']==year]['day']

        z_gold = df[df['year']==year]['gold']
        z_silver = df[df['year']==year]['silver']

        dx = dy = .8
        ax.bar3d(xs-dx/2, ys-dy/2, [0]*len(z_gold), dx, dy, z_gold, color='red')
        ax.bar3d(xs-dx/2, ys-dy/2, z_gold, dx, dy, z_silver, color=TEXT_COLOR)

    ax.set_box_aspect([1,2.77777,1])
    ax.view_init(elev=30, azim=-45)

    legend_elements = [Patch(facecolor=TEXT_COLOR, label='Both Parts'),
                    Patch(facecolor='red', label='Only Part 1')]
    ax.legend(handles=legend_elements, loc=(0.85, 0.86), fontsize=4.5)

    max_text = f'''
    Max completion of both parts (Red): 
        AoC {max_year_both} – Day {max_day_both}
        Gold: {max_gold_both:,} 
        Silver: {max_silver_both:,}

    Max completion of part 1 (Yellow & Red):
        AoC {max_year_1} – Day {max_day_1}
        Gold: {max_gold_1:,} 
        Silver: {max_silver_1:,}

    Max difference between 1 & 2 (Yellow): 
        AoC {max_year_diff} – Day {max_day_diff}
        Gold: {max_gold_diff:,} 
        Silver: {max_silver_diff:,}'''

    min_text = f'''
    Min completion of both parts (Red): 
        AoC {min_year_both} – Day {min_day_both}
        Gold: {min_gold_both:,} 
        Silver: {min_silver_both:,}

    Min completion of part 1 (Yellow & Red):
        AoC {min_year_1} – Day {min_day_1}
        Gold: {min_gold_1:,} 
        Silver: {min_silver_1:,}

    Min difference between 1 & 2 (Yellow): 
        AoC {min_year_diff} – Day {min_day_diff}
        Gold: {min_gold_diff:,} 
        Silver: {min_silver_diff:,}'''

    update = f'(Last update: {datetime.now().strftime("%Y-%m-%d")})'

    ax.text(2040, 11, 0, max_text, fontsize=4.5)
    ax.text(2009, 17, -180_000, min_text, fontsize=4.5)
    ax.text(2036, -1, 300_000, update, fontsize=4)

    plt.tight_layout()
    plt.savefig(PUBLIC_COMPLETION_PLOT)