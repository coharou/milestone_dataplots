import csv
import matplotlib.pyplot as plt

lows = []

filename = 'data/tc_climate.csv'
with open(filename) as f:
    read_file = csv.reader(f, delimiter = ',')
    getData = False
    for item in read_file:
        if getData == True:
            if item[8] != '':
                if item[2].startswith("2020-12") or item[2].startswith("2021-01") or item[2].startswith("2021-02"):
                    lows.append(item[8])
        getData = True

length = len(lows)
dates = range(length)

iLows = []
for item in lows:
    iLows.append(int(item))

plt.scatter(dates, iLows, color = 'green')
plt.title('Temperature vs. Winter Months')
plt.xlabel('Days of Winter')
plt.ylabel('Temperatures')
plt.show()