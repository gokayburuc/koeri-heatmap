#! /usr/bin/python3
from heatmap import HeatmapCreator
import random
from requests import get
from bs4 import BeautifulSoup
from rich import print
import pandas as pd


def RandomAgentChooser():
    with open("user_agents.txt", "r") as rf:
        data = rf.readlines()
        agent = random.choice(data)
    return agent


def GetContent(url):
    try:
        USER_AGENT = RandomAgentChooser()
        response = get(url=url, params=USER_AGENT)
        return response.content
    except Exception as e:
        print(e)
        pass
    finally:
        print(f"SERVER RESPONSE: {response.status_code}")


def soup(content):
    soup = BeautifulSoup(content, "lxml")
    raw_data = soup.find("pre").text
    raw_lines = raw_data.splitlines()

    earthquake_data = []

    for line in raw_lines:
        row = {
            "date": line[0:10],
            "time": line[11:19],
            "latitude": line[21:29],
            "longitude": line[31:38],
            "deepness": line[46:50],
            "md": line[55:58],
            "ml": line[60:63],
            "mw": line[65:68],
            "place": str(line[70:120]).strip(),
        }
        earthquake_data.append(row)
    return earthquake_data


def DataFrameToCSV(data):
    columns = [
        "date", "time", "latitude", "longitude",
        "deepness", "md", "ml", "mw", "place"]
    df = pd.DataFrame(earthquakedata, columns=columns)
    df = df[7:-1]

    replacelist = ['', '-.-']
    for repitem in replacelist:
        df['latitude'] = df['latitude'].replace(repitem, 0.0)
        df['longitude'] = df['longitude'].replace(repitem, 0.0)
        df['deepness'] = df['deepness'].replace(repitem, 0.0)
        df['ml'] = df['ml'].replace(repitem, 0.0)
        df['md'] = df['md'].replace(repitem, 0.0)
        df['mw'] = df['mw'].replace(repitem, 0.0)

    df.to_csv('deprem_verisi.csv')


if __name__ == "__main__":
    url = 'http://www.koeri.boun.edu.tr/scripts/lst9.asp'
    content = GetContent(url)
    earthquakedata = soup(content)
    DataFrameToCSV(earthquakedata)
    HeatmapCreator()
