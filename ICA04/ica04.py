# Incrementally adding data to a dictionary.
# Often, as we're working on a large set of input, we're collectng results
# in a dictionary (summing data over a set of keys,
# like county names, city names, or store names). We don't know in advance
# what keys will be in the dictionary, so we build it as we go.
# Let's sketch out a sample solution.

# First, create an empty dictionary to keep our sums by some key value.
sums_by_key = {}

# Assume this list of rows are like the rows of data we're reading from
# a CSV file. Let's use a simple list of sales for this program's input,
# with the store name in column 0 and value in column 2.
# Note: Just as thought we were readin from a CSV file, all the values
# are strings):
rows = [
    ['Hi-Vee', 'Rum', '2.50'],
    ['Fairway', 'Vodka', '17.50'],
    ['Hi-Vee', 'Whiskey', '7.50'],
    ['WayMart', 'Rum', '5.00'],
    ['WayMart', 'Vodka', '15.00'],
    ['Hi-Vee', 'Vodka', '12.50']
]

# Now, we'll complete this loop in class to compute the sum of the
# sales to each store.
for row in rows:
    store_name = row[0]
    #need to cast it with a float since it was originally given as a string
    sale = float(row[2])
    if store_name not in sums_by_key:
        #creates initial entry of store
        sums_by_key[store_name] = 0
    sums_by_key[store_name] += sale


index = 0
for key in sums_by_key:
    index += 1
    print("{}. {} {:.2f}".format(index, key, sums_by_key[key]))