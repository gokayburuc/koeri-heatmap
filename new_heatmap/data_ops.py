from pprint import pprint
from rich import print 

# read content
with open('eq_data.txt', 'r') as rf:
    data = rf.read()
    # print(data)

    # convert list
    dataset = data.split('\n')
    eqrows = dataset[7:-3]
    # pprint(eqrows)

    for r in eqrows:
        date = r[:10]
        time = r[11:20]
        enlem = r[21:29]
        boylam = r[31:39]
        print(date, time, enlem, boylam)
