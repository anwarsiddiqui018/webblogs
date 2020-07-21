# Read each row from a given csv file and print a list of strings

import csv
with open('departments.csv', newline= '') as csvfile:
    data = csv.reader(csvfile)

    for i in data:
        print(', '.join(i))


