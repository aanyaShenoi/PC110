import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import statistics as stats
import random as rand
import pandas as pnds
import csv

df = pnds.read_csv("data.csv")
data = df["reading_time"].tolist()

def random_mean(counter):
    dataset = []
    for i in range(0, counter):
        rand_index = rand.randint(0, len(data)-1)
        value = data[rand_index]
        dataset.append(value)

    mean = stats.mean(dataset)
    
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = stats.mean(mean_list)
    fig = pff.create_distplot([data], ["reading_time"], show_hist = False)
    fig.add_trace(pgo.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_mean = random_mean(100)
        mean_list.append(set_mean)
    show_fig(mean_list)

setup()
