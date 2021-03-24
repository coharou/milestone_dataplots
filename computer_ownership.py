import csv
import matplotlib.pyplot as plt

computer = []
access = []

filename = 'data/austin_tech_use.csv'
with open(filename) as f:
    read_file = csv.reader(f, delimiter = ',')
    getData = False
    for item in read_file:
        if getData == True:
            if item[5] != '':
                access.append(item[1])
                computer.append(item[5])
        getData = True

comp_val = 0
acc_val = 0

for item in computer:
    comp_val += int(item)
for item in access:
    acc_val += int(item)

acc_avg = acc_val / len(access) 
comp_avg = comp_val / len(computer)

acc_type = ['Yes', 'No']
acc_values = [acc_avg, 100 - acc_avg]
color = ['green', 'gray']

plt.subplot(1, 2, 1)
plt.title('Percentage of Austin, TX Residents with Internet Access')
plt.pie(acc_values, labels = acc_type, autopct = '%2.0f%%', colors = color) 

comp_type = ['Yes', 'No']
comp_values = [comp_avg, 100 - comp_avg]

plt.subplot(1, 2, 2)
plt.title('Percentage of Austin, TX Residents with Computer Access')
plt.pie(comp_values, labels = comp_type, autopct = '%2.0f%%', colors = color) 

plt.show()