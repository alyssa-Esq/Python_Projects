import csv

num_matches = 0
total_balance = 0

with open('input.csv', 'r', newline='') as csvFile:
    reader = csv.reader(csvFile)

    for row in reader:
        if row[7] == 'ME':
            num_matches += 1
            total_balance += float(row[1])

print("Number of entries from ME: " + str(num_matches))
print("Total balances: " + str(total_balance))
print("Average balance: " + str(total_balance/num_matches))
