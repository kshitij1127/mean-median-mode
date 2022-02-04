import csv

with open("Data.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
new_list = []

for i in range(len(data)):
    num = data[i][1]
    new_list.append(float(num))

new_list.sort()
n = len(new_list)

if(n % 2 == 0):
    median1 = float(new_list[n//2])
    median2 = float(new_list[n//2 - 1])
    median = (median1 + median2) / 2
else:
    median = float(new_list[n//2])

print("Median:", median)