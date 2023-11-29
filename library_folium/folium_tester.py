import folium
from folium.plugins import HeatMap

# folium map object
# NOTE: coordinates of Turkey
myMap = folium.Map(location=[38.963745, 35.243322000000035],
                   zoom_start=6)

# TODO : add GEOJSON data


def GeoJson():
    dataset = ""
    return dataset


myMap.save("turkey.html")
