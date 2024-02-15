from folium.plugins import HeatMap
import folium
from webbrowser import open_new
import pandas as pd


def HeatmapCreator():
    # coordinates of Turkey
    myMap = folium.Map(location=[38.963745, 35.243322000000035],
                       zoom_start=6)
    df = pd.read_csv("deprem_verisi.csv")
    depremler = df[["latitude", "longitude", "ml"]]

    HeatMap(data=depremler).add_to(myMap)
    myMap.save("output.html")
    open_new("output.html")
    pass

# # coordinates of Turkey
# myMap = folium.Map(location=[38.963745, 35.243322000000035],
#                    zoom_start=6)
# df = pd.read_csv("deprem_verisi.csv")
# depremler = df[["latitude", "longitude", "ml"]]
#
# HeatMap(data=depremler).add_to(myMap)
# myMap.save("output.html")
# open_new("output.html")
#
