import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from my_functions import db 


COMPLETION_PLOT_PATH = 'assets/completion_plot.png'


def plot_completion():

    # Set colors
    text_color = '#FFD700'
    primary_color = '#FF0000'
    background_color = '#04013b'
    grid_color = 'white'

    # Set the figure size
    fig, ax = plt.subplots(figsize=(15, 5))

    # Customize the entire figure
    fig.patch.set_facecolor(background_color)


    # Add dotted white grid lines
    ax.grid(True, linestyle='--', linewidth=0.5, color=grid_color, alpha=0.3)

    # Customize the title and axes font 
    title_font = {'family': 'serif', 'color': text_color, 'size': 18, 'weight': 'bold'}
    label_font = {'family': 'serif', 'color': text_color, 'size': 12}

    # Create the scatter plot
    df = db.get_completion_db()
    sns.scatterplot(data=df[df.completed == 1], x='day', y='year', marker='o', color=primary_color, edgecolor=primary_color, s=140, ax=ax, zorder=2, alpha=0.9)

    # Customize the plot area
    ax.set_facecolor('#04013b')
    ax.set_title('Advent of Code Challenge Completion', fontdict=title_font)
    ax.set_xlabel('Day', fontdict=label_font)
    ax.set_ylabel('Year', fontdict=label_font)
    ax.invert_yaxis()

    # Set the color of the spines (borders)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Customize ticks
    ax.tick_params(axis='both', colors=text_color, length=0)
    ax.set_xticks(np.arange(1, 26, 1))
    ax.set_xlim(0.6, 25.4)
    ax.set_yticks(np.arange(2015, 2023, 1))

    # Save the plot
    plt.savefig(COMPLETION_PLOT_PATH, bbox_inches='tight', dpi=300)