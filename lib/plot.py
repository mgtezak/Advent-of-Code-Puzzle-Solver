# Third party imports
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Local imports
from .utils import get_progress_db
from .solution import get_solution_db
from config import MAX_YEAR
from config import TEXT_COLOR, PRIMARY_COLOR, BACKGROUND_COLOR, GRID_COLOR
from config import PROGRESS_PLOT, RUNTIME_PLOT


def plot_progress():

    # Set the figure size
    fig, ax = plt.subplots(figsize=(15, 5))

    # Customize the entire figure
    fig.patch.set_facecolor(BACKGROUND_COLOR)


    # Add dotted white grid lines
    ax.grid(True, linestyle='--', linewidth=0.5, color=GRID_COLOR, alpha=0.3)

    # Customize the title and axes font 
    title_font = {'family': 'serif', 'color': TEXT_COLOR, 'size': 18, 'weight': 'bold'}
    label_font = {'family': 'serif', 'color': TEXT_COLOR, 'size': 12}

    # Create the scatter plot
    df = get_progress_db()
    sns.scatterplot(data=df[df.completed == 1], x='day', y='year', marker='o', color=PRIMARY_COLOR, edgecolor=PRIMARY_COLOR, s=140, ax=ax, zorder=2, alpha=0.9)

    # Customize the plot area
    ax.set_facecolor('#04013b')
    ax.set_title('My Advent of Code Progress', fontdict=title_font)
    ax.set_xlabel('Day', fontdict=label_font)
    ax.set_ylabel('Year', fontdict=label_font)
    ax.invert_yaxis()

    # Set the color of the spines (borders)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Customize ticks
    ax.tick_params(axis='both', colors=TEXT_COLOR, length=0)
    ax.set_xticks(np.arange(1, 26, 1))
    ax.set_xlim(0.6, 25.4)
    ax.set_yticks(np.arange(2015, MAX_YEAR+1, 1))

    # Save the plot
    plt.savefig(PROGRESS_PLOT, bbox_inches='tight', dpi=300)



def plot_runtime():

    # Customize the title and axes font 
    title_font = {'family': 'serif', 'color': TEXT_COLOR, 'size': 18, 'weight': 'bold'}
    label_font = {'family': 'serif', 'color': TEXT_COLOR, 'size': 12}

    # Get data
    df = get_solution_db()

    # Create a figure, GridSpec layout and axes
    fig = plt.figure(figsize=(15, 10), facecolor=BACKGROUND_COLOR)
    gs = gridspec.GridSpec(2, 3)    # 2 rows, 3 columns
    ax1 = fig.add_subplot(gs[0, :])                 # Spans all 3 columns in the first row
    ax2 = fig.add_subplot(gs[1, :2])                # Spans first 2 columns in the second row
    ax3 = fig.add_subplot(gs[1, 2], sharey=ax2)     # Spans last column in the second row

    # Create plots
    for x, ax in zip(('day', 'year', 'part'), (ax1, ax2, ax3)):
        sns.barplot(x=x, y='runtime', data=df, ax=ax, color=PRIMARY_COLOR, estimator='mean', errorbar=None, label='Mean' if x=='day' else None, zorder=2)
        sns.barplot(x=x, y='runtime', data=df, ax=ax, color=TEXT_COLOR, estimator='median', errorbar=None, label='Median' if x=='day' else None, zorder=3)
        ax.set_title(f'Runtime vs {x.capitalize()}', fontdict=title_font)
        ax.set_xlabel(x.capitalize(), fontdict=label_font)
        ax.set_ylabel('Runtime in seconds' if ax in (ax1, ax2) else '', fontdict=label_font)
        ax.grid(True, linestyle='--', linewidth=0.5, color=GRID_COLOR, alpha=0.3)
        ax.tick_params(axis='both', colors=TEXT_COLOR, length=0)
        ax.set_facecolor(BACKGROUND_COLOR)
        for spine in ax.spines.values():
            spine.set_visible(False)

    # Add legend   
    handles, labels = ax1.get_legend_handles_labels()
    legend = ax1.legend(handles, labels, facecolor=BACKGROUND_COLOR)
    for text in legend.get_texts():
        text.set_color(TEXT_COLOR)
        text.set_font('serif')

    # Save the plot      
    plt.savefig(RUNTIME_PLOT, bbox_inches='tight', dpi=300)