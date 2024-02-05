from bs4 import BeautifulSoup
from requests import get
import codecs

url = 'http://www.koeri.boun.edu.tr/scripts/lst7.asp'

# get content
req = get(url)
content = req.content
text = req.text

# clear data
data = codecs.decode(content, 'latin5')  # decoding bytes into text
soup = BeautifulSoup(data, 'html.parser')  # soup object create
eq_data = soup.find('pre').text  # find content
print(eq_data)


# save as txt file 
with open('eq_data.txt', 'w') as wf:
    print(eq_data, file=wf)

# save json , csv

#
