import os, csv
import matplotlib.pyplot as plt
from pprint import pprint

cwd = os.getcwd()
filepath = os.path.join(cwd, "output.csv")

# author : author count
data = {}
with open(filepath) as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Author'] in data:
            data[row['Author']] += 1
        else:
            data[row['Author']] = 1

# convert data to a sorted list
data_list = [[author, value] for author, value in data.items()]
data_list = sorted(data_list, key = lambda x: x[1], reverse = True)

# get values to display on pie chart
labels = [item[0] for item in data_list[:10]]
values = [int(item[1]) for item in data_list[:10]]

# setup and show the chart
fig1, ax1 = plt.subplots()
ax1.pie(values, labels = labels, autopct = "%1.1f%%")
plt.show()
