import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import numpy as np

def draw_plot():
    # Read data from file
    cols = ['Year', 'CSIRO Adjusted Sea Level']
    df = pd.read_csv('epa-sea-level.csv', usecols=cols)


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(32, 10), dpi=100)
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, c='r')

    # Create first line of best fit
    max_year = df["Year"].max()
    res = linregress(x, y)
    arr  = np.append(np.array(df['Year'].values), [a for a in range(df["Year"].max()+1, 2051)])
    plt.plot(arr, res.intercept + res.slope*arr, 'g', label='the line of best fit')

    # Create second line of best fit
    recent_df = df.loc[(df["Year"] >= 2000) & (df["Year"] <= max_year)]
    recent_x = recent_df['Year']  
    recent_y = recent_df['CSIRO Adjusted Sea Level']
    res_recent = linregress(recent_x, recent_y)
    arr_recent  = np.append(np.array(recent_df['Year'].values), [a for a in                 range(df["Year"].max()+1, 2051)])
    plt.plot(arr_recent, res_recent.intercept + res_recent.slope*arr_recent, 'b', label='the line of best fit from 2000 to 2050 ')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    ax.set_title("Rise in Sea Level", fontsize=20)
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return plt.gca()