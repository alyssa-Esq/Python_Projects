import csv
texas = []

with open('sample.csv') as csvFile:
    reader = csv.reader(csvFile)
    headers = next(reader)
    texas.append(headers)

    #aquires TX info and adds it to texas []
    for row in reader:
        if row[6] == 'TX':
            texas.append(row)

#writing to new file
with open('texas.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    for row in texas:
        writer.writerow(row)