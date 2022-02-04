import csv
from collections import Counter
from statistics import mode

with open('Data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
new_list = []

for i in range(len(data)):
    num = data[i][1]
    new_list.append(float(num))

new_data = Counter(new_list)
mode_data = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0,
}

for height, occurance in new_data.items():
    if (50 < float(height) < 60):
        mode_data["50-60"] += occurance
    elif (60 < float(height) < 70):
        mode_data["60-70"] += occurance
    elif (70 < float(height) < 80):
        mode_data["70-80"] += occurance

mode_range, mode_occurance = 0,0
for range, occurance in mode_data.items():
    if occurance > mode_occurance:
        mode_range, mode_occurance = [int(range.split('-')[0]), int(range.split('-')[1])], occurance

mode = float(mode_range[0] + mode_range[1]) / 2
print("mode: ", mode)