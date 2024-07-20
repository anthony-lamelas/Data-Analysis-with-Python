import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']





# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(.975))
        ]



def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(15,5))
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set(xlabel = "Date",ylabel = "Page Views")
    df.plot()
    plt.show()
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df.index.year.values
    df_bar["month"] = df.index.month_name()
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15,5))
    
    ax = sns.barplot(x="year", hue="month", y="value", data=df_bar, hue_order = months, ci=None )
    ax.set(xlabel = "Years",ylabel = "Average Page Views")
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig 


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, ax = plt.subplots(1,2,figsize=(16,6))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    ax[0].set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")

    sns.boxplot(data=df_box, x='month', y='value', ax=ax[1], order=month_order)
    ax[1].set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")
    



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig




draw_line_plot()