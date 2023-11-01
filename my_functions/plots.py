import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

from my_functions import db 


COMPLETION_PLOT_PATH = 'assets/completion_plot.png'
RUNTIME_PLOT_PATH = 'assets/runtime_plot.png'
RUNTIME_YEAR_PLOT_PATH = 'assets/runtime_year_plot.png'
RUNTIME_DAY_PLOT_PATH = 'assets/runtime_day_plot.png'
RUNTIME_PART_PLOT_PATH = 'assets/runtime_part_plot.png'



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



def plot_runtime():

    # Set colors
    text_color = '#FFD700'
    primary_color = '#FF0000'
    background_color = '#04013b'
    grid_color = 'white'

    # Customize the title and axes font 
    title_font = {'family': 'serif', 'color': text_color, 'size': 18, 'weight': 'bold'}
    label_font = {'family': 'serif', 'color': text_color, 'size': 12}

    # Get data and figure
    df = db.get_solution_db()
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5), width_ratios=[2, 2.5, 0.5], sharey=True)

    # Create each plot
    for x, ax in zip(['year', 'day', 'part'], [ax1, ax2, ax3]):
        sns.barplot(x=x, y='runtime', data=df, ax=ax, color=primary_color, estimator='mean', errorbar=None, label='Mean', legend=False, zorder=2)
        sns.barplot(x=x, y='runtime', data=df, ax=ax, color=text_color, estimator='median', errorbar=None, label='Median', legend=False, zorder=3)
        ax.set_title(f'Runtime vs {x.capitalize()}', fontdict=title_font)
        ax.set_xlabel(x.capitalize(), fontdict=label_font)
        ax.grid(True, linestyle='--', linewidth=0.5, color=grid_color, alpha=0.3)
        ax.set_facecolor('#04013b')
        ax.tick_params(axis='both', colors=text_color, length=0)

    fig.patch.set_facecolor(background_color)
    ax1.set_ylabel('Runtime in seconds', fontdict=label_font)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15, wspace=0.1)
    handles, labels = ax1.get_legend_handles_labels()
    legend = fig.legend(handles, labels, loc='lower center', ncol=3, facecolor=background_color)
    for text in legend.get_texts():
                text.set_color(text_color)
                text.set_font('serif')

    # Save the plot      
    plt.savefig(RUNTIME_PLOT_PATH, bbox_inches='tight', dpi=300)


def plot_runtime_year():

    # Set colors
    text_color = '#FFD700'
    primary_color = '#FF0000'
    background_color = '#04013b'
    grid_color = 'white'

    # Customize the title and axes font 
    title_font = {'family': 'serif', 'color': text_color, 'size': 18, 'weight': 'bold'}
    label_font = {'family': 'serif', 'color': text_color, 'size': 12}

    # Get data
    df = db.get_solution_db()
    _, ax = plt.subplots(figsize=(15, 5), facecolor=background_color)

    # Create plot
    plt.ylabel('Runtime in seconds', fontdict=label_font)
    sns.barplot(x='year', y='runtime', data=df, color=primary_color, estimator='mean', errorbar=None, label='Mean', zorder=2)
    sns.barplot(x='year', y='runtime', data=df, color=text_color, estimator='median', errorbar=None, label='Median', zorder=3)
    plt.title(f'Runtime vs Year', fontdict=title_font)
    plt.xlabel('Year', fontdict=label_font)
    plt.ylabel('Runtime in seconds', fontdict=label_font)
    plt.grid(True, linestyle='--', linewidth=0.5, color=grid_color, alpha=0.3)

    ax.tick_params(axis='both', colors=text_color, length=0)
    ax.set_facecolor('#04013b')
    legend = ax.legend(facecolor=background_color)
    for text in legend.get_texts():
                text.set_color(text_color)
                text.set_font('serif')

    # Save the plot      
    plt.savefig(RUNTIME_YEAR_PLOT_PATH, bbox_inches='tight', dpi=300)



def plot_runtime_day():

    # Set colors
    text_color = '#FFD700'
    primary_color = '#FF0000'
    background_color = '#04013b'
    grid_color = 'white'

    # Customize the title and axes font 
    title_font = {'family': 'serif', 'color': text_color, 'size': 18, 'weight': 'bold'}
    label_font = {'family': 'serif', 'color': text_color, 'size': 12}

    # Get data
    df = db.get_solution_db()
    _, ax = plt.subplots(figsize=(15, 5), facecolor=background_color)

    # Create plot
    plt.ylabel('Runtime in seconds', fontdict=label_font)
    sns.barplot(x='day', y='runtime', data=df, color=primary_color, estimator='mean', errorbar=None, label='Mean', zorder=2)
    sns.barplot(x='day', y='runtime', data=df, color=text_color, estimator='median', errorbar=None, label='Median', zorder=3)
    plt.title(f'Runtime vs Day', fontdict=title_font)
    plt.xlabel('Day', fontdict=label_font)
    plt.ylabel('Runtime in seconds', fontdict=label_font)
    plt.grid(True, linestyle='--', linewidth=0.5, color=grid_color, alpha=0.3)

    ax.tick_params(axis='both', colors=text_color, length=0)
    ax.set_facecolor('#04013b')
    legend = ax.legend(facecolor=background_color)
    for text in legend.get_texts():
                text.set_color(text_color)
                text.set_font('serif')

    # Save the plot      
    plt.savefig(RUNTIME_DAY_PLOT_PATH, bbox_inches='tight', dpi=300)




def plot_runtime_part():

    # Set colors
    text_color = '#FFD700'
    primary_color = '#FF0000'
    background_color = '#04013b'
    grid_color = 'white'

    # Customize the title and axes font 
    title_font = {'family': 'serif', 'color': text_color, 'size': 18, 'weight': 'bold'}
    label_font = {'family': 'serif', 'color': text_color, 'size': 12}

    # Get data
    df = db.get_solution_db()
    _, ax = plt.subplots(figsize=(7, 5), facecolor=background_color)

    # Create plot
    plt.ylabel('Runtime in seconds', fontdict=label_font)
    sns.barplot(x='part', y='runtime', data=df, color=primary_color, estimator='mean', errorbar=None, label='Mean', zorder=2)
    sns.barplot(x='part', y='runtime', data=df, color=text_color, estimator='median', errorbar=None, label='Median', zorder=3)
    plt.title(f'Runtime vs Part', fontdict=title_font)
    plt.xlabel('Part', fontdict=label_font)
    plt.ylabel('Runtime in seconds', fontdict=label_font)
    plt.grid(True, linestyle='--', linewidth=0.5, color=grid_color, alpha=0.3)

    ax.tick_params(axis='both', colors=text_color, length=0)
    ax.set_facecolor('#04013b')
    legend = ax.legend(facecolor=background_color)
    for text in legend.get_texts():
                text.set_color(text_color)
                text.set_font('serif')

    # Save the plot      
    plt.savefig(RUNTIME_PART_PLOT_PATH, bbox_inches='tight', dpi=300)

