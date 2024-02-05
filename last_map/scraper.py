import requests
from bs4 import BeautifulSoup
import pandas 

# USER AGENT
USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Get Response


def Response(url):
    try:
        response = requests.get(url)
        return response
    except Exception as e:
        raise e
    else:
        response = requests.get(url, params=USER_AGENT)
        return response

# soup data


def Soup(data):
    soup = BeautifulSoup(data, "lxml")
    rawdata = soup.find("pre")
    return rawdata.text


# data cleaning 

def DataClean(data): 
    lines = data.split()
    columns = ['tarih', 'saat','Enlem','Boylam','derinlik','MD','ML','Mw']
    df=pandas.DataFrame(columns=columns)


if __name__ == "__main__":
    url = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"
    r = Response(url=url)
    soup = Soup(r.content)
    print(soup)
    pass
