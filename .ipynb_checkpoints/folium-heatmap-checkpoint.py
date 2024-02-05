#! /usr/bin/python3

import pandas as pd
import csv
import folium
from folium.plugins import HeatMap

# folium map object
myMap = folium.Map(location=[38.963745, 35.243322000000035],
                   zoom_start=6)

# myMap.show_in_browser()
df = pd.read_csv("earthquake_data.csv")
depremler = df[["latitude", "longitude", "mw"]]

# dataframe to list
depremler.to_csv("map_data.csv")


def CleanData():
    dataset = []

    with open("map_data.csv", "r") as rf:
        rd = csv.reader(rf)
        for row in rd:
            # print(row)
            dataset.append(row)

    raw_data = [r[1:4] for r in dataset]

    data = []

    for x in raw_data:
        try:
            # print([float(x[0]), float(x[1]), float(x[2])])
            data.append([float(x[0]), float(x[1]), float(x[2])])
        except:
            pass

    return data


data = CleanData()
HeatMap(data=data).add_to(myMap)
myMap.save("output.html")
