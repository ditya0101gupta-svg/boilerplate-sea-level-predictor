import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years = range(1880, 2051)

    plt.plot(
    years,
    [res.slope * year + res.intercept for year in years],
    color="red"
    )

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]

    res2 = linregress(
    df_recent["Year"],
    df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = range(2000, 2051)

    plt.plot(
    years_recent,
    [res2.slope * year + res2.intercept for year in years_recent],
    color="green"
    )

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()