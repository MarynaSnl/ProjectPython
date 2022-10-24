import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime
from pandas.tseries.offsets import DateOffset
import numpy as np

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",  index_col='date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025))  & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df.plot(subplots=True, figsize=(18, 6),  color='red'); plt.legend(loc='best'); plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019');plt.ylabel('Page Views');plt.xlabel('Date')
    fig, ax = plt.subplots(figsize=(32, 10), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize=20)
    ax.set_xlabel("Date",  fontsize=16)
    ax.set_ylabel("Page Views", fontsize=18)
    ax.set_xscale = 20
    plt.plot(df['value'], color='r')
    try:
        s1, s2 = make_ticks(df.loc[(df.index>'2016-06-30')] , 6)
    except:
        s1,s2 = df.index, df.index
    plt.xticks(s1, s2, rotation ='horizontal')    
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(18)

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig
  
def make_ticks(df_s, step_months):
    
    s2 = pd.date_range(df_s.index[0], df_s.index[-1],  freq="6M").strftime('%Y-%m')
    df["Group_k"] = df.index.str.slice(stop=7)
    df_filter = df['Group_k'].isin(s2)
    df1 = df[df_filter]
    s1 = df1.drop_duplicates (subset=['Group_k']).index
    return s1, s2

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.str.slice(start=0, stop=4)
    df_bar["month"] = df_bar.index.str.slice(start=5, stop=7)
    # Draw bar plot
    ax1 = df_bar.groupby(['year','month']).mean().unstack().plot(kind='bar',stacked=False, figsize=(8,8))
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    s2 = [datetime.strptime(x, "%m").strftime("%B") for x in sorted(df_bar.month.unique())] 
    plt.legend( s2, title = 'Month')
    fig = plt

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return ax1.get_figure()

def draw_box_plot():
    
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    ######  have error in this code
    #df_box.reset_index(inplace=True)
    #df_box['year'] = [d.year for d in df_box.date]
    #df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box["year"] = df_box.index.str.slice(start=0, stop=4)
    df_box["month"] = df_box.index.str.slice(start=5, stop=7)
    # Draw box plots (using Seaborn)
  
    sns.set_style("whitegrid")
    fig = plt.figure(figsize=(18, 6))
    ax1 = plt.subplot(1, 2, 1)
    sns.boxplot(x = 'year', y = 'value', data = df_box)
    plt.xlabel('Year')
    plt.legend([],[],frameon = False)
    ax1.set_title('Year-wise Box Plot (Trend)')
    plt.ylabel('Page Views')
    ax2= plt.subplot(1, 2, 2)
    sns.boxplot(x = 'month', y = 'value', data = df_box.sort_values ('month'))
    plt.legend(['-X^2', 'Horizontal Line'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.legend([],[],frameon = False)
    plt.ylabel('Page Views')

    s2 = [datetime.strptime(x, "%m").strftime("%b") for x in sorted(df_box.month.unique())] 
    ax2.set_xticks(np.arange(12))
    s2 = ax2.set_xticklabels(s2, rotation=180)
    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
