#! /usr/bin/python3

from requests import get
from bs4 import BeautifulSoup
from time import sleep
from user_agent import RandomAgentChooser
from rich import print
import requests

# url = 'http://www.koeri.boun.edu.tr/scripts/lst7.asp'
url = 'http://www.koeri.boun.edu.tr/scripts/lst7.asp'


def CheckURLExistence(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False


# USER_AGENT = {
#     "User-Agent": "Mozilla/5.0 (X11
#                                 Ubuntu
#                                 Linux x86_64
#                                 rv: 109.0)
#     Gecko/20100101 Firefox/110.0"
# }

# INFO: Get Content


def GetContent(url):
    try:
        USER_AGENT = RandomAgentChooser()
        response = get(url=url, params=USER_AGENT)
        print(response.content)
        return response.content
    except Exception as e:
        print(e)
        pass
    finally:
        print(f"SERVER RESPONSE: {response.status_code}")

# soup operations


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

    print(earthquake_data)

    # # empty earthquake_data
    # for x in earthquake_data:
    #     if len(x) < 8:
    #         earthquake_data.remove(x)
    #     else:
    #         pass
    #
    # columns = [
    #     "date", "time", "latitude", "longitude",
    #     "deepness", "md", "ml", "mw", "place"]
    #
    # df = pd.DataFrame(earthquake_data, columns=columns)
    # df = df[5:]
    #
    # print(df.head())

    # save to csv
    # df.to_csv("earthquake_data.csv")


if __name__ == "__main__":
    sleep(3)
    content = GetContent(url)
    soup(content)
