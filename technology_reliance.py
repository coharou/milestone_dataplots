import csv
import matplotlib.pyplot as plt

responses = []

filename = 'data/seattle_tech_use.csv'
with open(filename) as f:
    read_file = csv.reader(f, delimiter = ',')
    getData = False
    for item in read_file:
        if getData == True:
            if item[39] != '':
                responses.append(item[39])
        getData = True

computer = 0
mobile = 0
console = 0
no_access = 0

for item in responses:
    i = int(item)
    if i == 1 or i == 2:
        computer += 1
    if i == 3 or i == 4:
        mobile += 1
    if i == 5:
        console += 1
    if i == 7:
        no_access += 1

text_keys = ['Computer', 'Mobile', 'Console', 'None']
values = [computer, mobile, console, no_access]

plt.bar(text_keys, values, color='green')
plt.title('Quantity of Devices Used by Seattle, WA Residents')
plt.xlabel('Types of Devices')
plt.ylabel('Number of Responses')
plt.show()