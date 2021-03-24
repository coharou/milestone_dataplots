import csv
import matplotlib.pyplot as plt

highs_jun = []
highs_jul = []
highs_aug = []

filename = 'data/tc_climate.csv'
with open(filename) as f:
    read_file = csv.reader(f, delimiter = ',')
    getData = False
    for item in read_file:
        if getData == True:
            if item[7] != '':
                if item[2].startswith("2020-06"):
                    highs_jun.append(item[7])
                if item[2].startswith("2020-07"):
                    highs_jul.append(item[7])
                if item[2].startswith("2020-08"):
                    highs_aug.append(item[7])
        getData = True

highs_jun.sort()
iJun = len(highs_jun) - 1

highs_jul.sort()
iJul = len(highs_jul) - 1

highs_aug.sort()
iAug = len(highs_aug) - 1

text_keys = ['June', 'July', 'August']
values = [int(highs_jun[iJun]), int(highs_jul[iJul]), int(highs_aug[iAug])]

plt.bar(text_keys, values, color='green')
plt.title('Highest Temperatures for Summer 2020 in Traverse City, MI')
plt.xlabel('Summer Months')
plt.ylabel('Temperatures')
plt.show()