import pandas as pd
import folium
from folium.plugins import HeatMap


def clean_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

    earthquakes = df[["latitude", "longitude", "mw"]]

    cleaned_data = []

    for index, row in earthquakes.iterrows():
        try:
            cleaned_data.append([float(row["latitude"]), float(
                row["longitude"]), float(row["mw"])])
        except ValueError as e:
            print(f"Error converting data: {e}")

    return cleaned_data


# Define the map object
my_map = folium.Map(location=[38.963745, 35.243322000000035], zoom_start=6)

# Clean the data
data = clean_data("earthquake_data.csv")

# Add HeatMap to the map
HeatMap(data=data).add_to(my_map)

# Save the map as an HTML file
my_map.save("output.html")
