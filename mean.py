import csv

with open("Data.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
new_list = []

for i in range(len(data)):
    num = data[i][1]
    new_list.append(float(num))

n = len(new_list)
total = 0 

for i in range(n):
    total += new_list[i]

median = total / n
print("mean is:", str(median))

