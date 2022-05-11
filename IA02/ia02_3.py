# Write a program that reads each row of sample.csv and counts the number
# of times NY were found in the state column. Print the totals on the screen,
# like this (your value for N should appear in the output):

import csv
count = 0

with open('sample.csv') as csvFile:
    reader = csv.reader(csvFile)
    headers = next(reader)

    for row in reader:
        if row[6] == 'NY':
            count += 1

print("NY: total = " + str(count))
