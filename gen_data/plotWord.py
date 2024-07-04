#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
#import plotly.graph_objects as gOBJ
import plotly.express as px

def plotBarChart(wordCountDICT):
    #sorted_data = dict(sorted(wordCountDICT.items(), key=lambda item: item[1], reverse=True))
    sorted_data = dict(sorted(wordCountDICT.items(), key=lambda item: item[1], reverse=True)[:100])
    # Extracting data
    words = list(sorted_data.keys())
    counts = list(sorted_data.values())

    # Create the bar chart using Plotly Express
    fig = px.bar(x=words, y=counts,
                 labels={'x': 'Words', 'y': 'Frequency'},
                 title='Word Frequencies')

    # Show full x-axis
    fig.update_xaxes(tickmode='array', tickvals=list(range(len(sorted_data))),
                     ticktext=list(sorted_data.keys()))

    # Show the figure
    fig.show()

    return None


if __name__ == "__main__":
    inputFILE = "./paiwan200.json"

    with open(inputFILE, encoding="utf-8") as f:
        inputSTR = json.load(f)[0]

    wordCountDICT = {}
    for i in inputSTR.split(" "):
        if i in wordCountDICT:
            wordCountDICT[i] = wordCountDICT[i] + 1
        else:
            wordCountDICT[i] = 1
    plotBarChart(wordCountDICT)