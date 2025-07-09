# ============ 11. CSV loading Example ============

import csv

data = []
header = []
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        data.append(row)
print("Header:", header)
print("Data:", data)