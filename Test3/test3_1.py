import csv

with open("words.txt", newline='') as input_file:
    num_words = 0
    longest_word_length = 0
    reader = csv.reader(input_file)

    for line in input_file:
        num_words += 1
        if len(line) > longest_word_length:
            longest_word_length = len(line)


print("Number of words: " + str(num_words))
print("Longest word length: " + str(longest_word_length))
