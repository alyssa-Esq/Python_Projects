import csv

with open('Iowa-Liquor-Sales-Ames-2020.csv') as csvFile:
    reader = csv.reader(csvFile)
    headers = next(reader)

    totalAmes = 0
    index = 0
    AmesLocations = {}

    for row in reader:
        location = row[3].upper()
        sale = float(row[21])
        volume = float(row[22])

        if location not in AmesLocations:
            AmesLocations[location] = volume
        else:
            AmesLocations[location] += volume

        totalAmes += float(sale)

    print("Total store alcohol sales by volume:")
    for location, volume in sorted(AmesLocations.items(), key=lambda x: x[1], reverse=True):
        index += 1
        print(str(index) + ". " + "{}. {:.2f}".format(location, AmesLocations[location]) + " liters")

    print("Total sales in Ames: " + str(totalAmes) + " liters")
