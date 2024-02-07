# /usr/bin/python3
import csv

import pandas

# data set oluştur
dataset = []

# csv dosyasindan verileri cek
with open("map_data.csv", "r") as rf:
    rd = csv.reader(rf)
    for row in rd:
        dataset.append(row)

    data = [r[1:4] for r in dataset]
    print(data)

    for x in data:
        try:
            print([float(x[0]), float(x[1]), float(x[2])])
        except Exception as e:
            raise e
            pass

# verileri temizle
    def CleanData():
        dataset = []

        with open("map_data.csv", "r") as rf:
            rd = csv.reader(rf)
            for row in rd:
                dataset.append(row)

        raw_data = [r[1:4] for r in dataset]

        data = []

        for x in raw_data:
            print([float(x[0]), float(x[1]), float(x[2])])
            data.append([float(x[0]), float(x[1]), float(x[2])])
        return data
