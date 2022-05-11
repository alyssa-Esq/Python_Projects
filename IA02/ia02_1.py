import csv

sampleList = []

with open('sample.csv') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        sampleList.append(row)

for i in range(11):
    print(sampleList[i])
