import folium
from folium.plugins import HeatMap

# folium map object
# NOTE: coordinates of Turkey 
myMap = folium.Map(location=[38.963745, 35.243322000000035],
                   zoom_start=6)


myMap.save("turkey.html")
