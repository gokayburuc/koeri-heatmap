#! /usr/bin/python3

import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from user_agent import RandomAgentChooser


url = 'http://www.koeri.boun.edu.tr/scripts/lst0.asp'
# USER_AGENT = {
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0"}
#

# INFO: Get Content
def GetContent(url):
    try:
        USER_AGENT = RandomAgentChooser()
        response = get(url=url, params=USER_AGENT)
    except Exception as e:
        print(e)
        pass
    finally:
        print(f"SERVER RESPONSE: {response.status_code}")
        if response.status_code == 200:
            print("STATUS : OK")
        elif response.status_code == 400:
            print("STATUS : BAD REQUESTS")
        elif response.status_code == 500:
            print("STATUS : INTERNAL SERVER ERROR")
        elif response.status_code == 503:
            print("STATUS : SERVICE UNAVAILABLE")

    return response.content

# INFO: Soup Object
def bs_obj(html_content):
    bs_obj = BeautifulSoup(markup=html_content, features="lxml")
    return bs_obj


if __name__ == "__main__":

    sleep(3)
    cnt = GetContent(url)

    x = bs_obj(html_content=cnt)
    earthquake_data = x.find("pre").text
    raw_lines = earthquake_data.splitlines()

    # empty dataset
    dataset = []

    for x in raw_lines:
        # INFO: enlem boylam gün zaman derinlik şiddet ve yer degerleri 
        date = x[0:10]
        time = x[11:19]
        latitude = x[21:29]
        longitude = x[31:38]
        deepness = x[46:50]
        md = x[55:58]
        ml = x[60:63]
        mw = x[65:68]
        place = x[70:120]

        # strip values
        place = place.strip()

        # data row
        data = [date, time, latitude, longitude, deepness, md, mw, ml, place]
        dataset.append(data)

        for x in dataset:
            if len(x) < 8:
                dataset.remove(x)
            else:
                pass

 # dataframe
 # TODO : column name error fix

    df = pd.DataFrame(dataset, columns=[
        "date", "time", "latitude", "longitude", "deepness", "md", "ml", "mw", "place"])

    print(df)

    df = df[5:]

    # save to csv
    df.to_csv("earthquake_data.csv")
