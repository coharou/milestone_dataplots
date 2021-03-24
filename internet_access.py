import csv
import matplotlib.pyplot as plt

access = []

filename = 'data/seattle_tech_use.csv'
with open(filename) as f:
    read_file = csv.reader(f, delimiter = ',')
    getData = False
    for item in read_file:
        if getData == True:
            if item[5] != '':
                access.append(item[5])
        getData = True

hasAccess = 0
noAccess = 0

for item in access:
    if int(item) == 2:
        noAccess += 1
    if int(item) == 1:
        hasAccess += 1

acc_type = ['Yes', 'No']
acc_val = [hasAccess, noAccess]
color = ['green', 'gray']

plt.title('Percentage of Seattle, WA Residents with Internet Access')
plt.pie(acc_val, labels = acc_type, autopct = '%2.0f%%', colors = color)
plt.show()