#! /usr/bin/python3

# import pandas as pd
# df = pd.read_csv("earthquake_data.csv")
# depremler = df[["latitude", "altitude", "mw"]]
# print(depremler)
# print(df.columns)


import csv

dataset = []

with open("map_data.csv", "r") as rf:
    rd = csv.reader(rf)
    for row in rd:
        # print(row)
        dataset.append(row)

# print(dataset)

data = [r[1:4] for r in dataset]
print(data)

for x in data:
    try:
        print([float(x[0]), float(x[1]), float(x[2])])
    except:
        pass


def CleanData():
    dataset = []

    with open("map_data.csv", "r") as rf:
        rd = csv.reader(rf)
        for row in rd:
            # print(row)
            dataset.append(row)

    raw_data = [r[1:4] for r in dataset]

    data = []

    for x in raw_data:
        print([float(x[0]), float(x[1]), float(x[2])])
        data.append([float(x[0]), float(x[1]), float(x[2])])
    return data
