import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Import the data from "fcc-forum-pageviews.csv" and set the index to the date column
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Task 2: Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

# Task 3: Create a draw_line_plot function
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df["value"], color="red")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("line_plot.png")
    return fig

# Task 4: Create a draw_bar_plot function
def draw_bar_plot():
    df["year"] = df.index.year
    df["month"] = df.index.strftime("%B")
    df_bar = df.groupby(["year", "month"])["value"].mean().unstack()
    fig = df_bar.plot(kind="bar", figsize=(10, 5)).get_figure()
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=df_bar.columns)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("bar_plot.png")
    return fig

# Task 5: Create a draw_box_plot function
def draw_box_plot():
    # Copy and modify data for monthly box plot
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))

    sns.boxplot(x="year", y="value", data=df_box, ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    sns.boxplot(x="month", y="value", data=df_box, ax=ax[1],
                order=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    # Save the plot as an image
    plt.savefig('box_plot.png')

    # Return the plot
    return fig

# Test the functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()
