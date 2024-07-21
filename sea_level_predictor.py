import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    fig, ax = plt.subplots()
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit

    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years = np.arange(1880,2050)
    ax.plot(years, slope*years + intercept, color="red")
    
    # Create second line of best fit

    df_two = df.loc[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_two["Year"], df_two["CSIRO Adjusted Sea Level"])

    years_two = np.arange(2000,2050)

    ax.plot(years_two, slope2*years_two + intercept2, color='yellow')
    plt.show()


    # Add labels and title
    ax.set(xlabel='Year', ylabel ="Sea Level(inches)", title = 'Rise in SEa')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()