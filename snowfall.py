import csv
import matplotlib.pyplot as plt

snowfall = []

filename = 'data/tc_snow_temp.csv'
with open(filename) as f:
    read_file = csv.reader(f, delimiter = ',')
    getData = False
    for item in read_file:
        if getData == True:
            if item[4] != '':
                if item[2].startswith("2020-12") or item[2].startswith("2021-01") or item[2].startswith("2021-02"):
                    snowfall.append(item[4])
        getData = True

length = len(snowfall)
dates = range(length)

iSnow = []
for item in snowfall:
    iSnow.append(float(item))

plt.plot(iSnow, color = 'green')
plt.title('Snowfall vs. Winter Months')
plt.xlabel('Days of Winter')
plt.ylabel('Snowfall Amounts')
plt.show()