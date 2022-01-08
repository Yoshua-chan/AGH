import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import deque

edgecolor = "white"
color = "cornflowerblue"
plotcolor = "red"
width = 1 

def ratio(plot_polygon):
    df = pd.read_csv("./data/secondary_per_vocational.csv", sep="\t")
    data = np.array(df["ratio"])

    binwidth = 0.25
    bins = np.arange(0, 3.75 + binwidth, binwidth)
    xlabels = bins + (0.25/2)
    ranges = []
    for label in bins:
        if label >= 3.75:
            ranges.append("")
        else:
            ranges.append(f"[{label} ; {label+0.25})")
    
    ranges[-2] = "≥3.5"

    plt.xticks(xlabels, ranges, rotation=45, size=9)
    plt.xlim(0, 3.75)
    values, limits, _ = plt.hist(np.clip(data, 0, 3.75), bins=bins, color=color, edgecolor=edgecolor, linewidth=width)


    i = 0
    midpoints = []
    while i < len(limits) - 1:
        midpoints.append((limits[i] + limits[i+1])/2)
        i += 1

    values = deque(values)
    midpoints = deque(midpoints)

    values.appendleft(0)
    midpoints.appendleft(0)

    values.append(0)
    midpoints.append(3.75)

    if plot_polygon is True:
        plt.plot(midpoints, values, 'o--', color=plotcolor)

    plt.title("Stosunek zawodowo do średnio wykształconych")
    plt.tight_layout()
    plt.show()

def high_per_thousand(plot_polygon):
    df = pd.read_csv("./data/ed_per_thousand.csv", sep=",")
    data = np.array(df["wyzsze"])

    binwidth = 8
    bins = np.arange(0, 120 + binwidth, binwidth)
    xlabels = bins + 4 

    ranges = []
    for label in bins:
        if label >= 112:
            ranges.append("")
        else:
            ranges.append(f"[{label} ; {label+8})")
    
    ranges[-2] = "≥112"

    plt.xticks(xlabels, ranges, rotation=45, size=9)

    plt.xlim(0, 120)
    values, limits, _ = plt.hist(np.clip(data, 0, 120), bins=bins, edgecolor=edgecolor, linewidth=width, color=color)

    i = 0
    midpoints = []
    while i < len(limits) - 1:
        midpoints.append((limits[i] + limits[i+1])/2)
        i += 1

    values = deque(values)
    midpoints = deque(midpoints)

    values.appendleft(0)
    midpoints.appendleft(0)

    values[-1] = 0
    midpoints[-1] = 112

    if plot_polygon is True:
        plt.plot(midpoints, values, 'o--', color=plotcolor)

    plt.title("Liczba wyżej wykształconych na 1000 mieszkańców miejscowości")
    plt.tight_layout()
    plt.show()

def education():
    df = pd.read_csv("./data/education.csv", sep=",")
    data = np.array(df["wyz"])

    binwidth = 500
    bins = np.arange(0, max(data) + binwidth, binwidth)
    xlabels = bins + 250

    ranges = []
    for label in bins:
        if label >= 4500:
            ranges.append("")
        else:
            ranges.append(f"[{label} ; {label+500})")
    

    plt.xticks(xlabels, ranges, rotation=45, size=9)

    plt.xlim(0, 4500)
    plt.hist(np.clip(data, 0, 4000), bins=bins, edgecolor=edgecolor, linewidth=width)
    plt.title("Liczba wyżej wykształconych w miastach")
    plt.tight_layout()
    plt.show()

def categorize(max_arg: float, step: float, overflow: bool):
    values = []
    for i in range(0, int(max_arg // step)):
        print(i * step)

def main():
    ratio(False)
    high_per_thousand(True)
    education()
    # categorize(25, 0.25, 0)

main()