import csv

newfile = 'C://Users//Elait141//Desktop//Techie Smiles//Python//data.csv'
row_count = 0
# Reading the CSV data
with open(newfile, 'r') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)
    for row in csv_reader:
        row_count += 1
        if row_count in (20,21):
            print(row_count, row)
         
'''
# How to read a particular column in a CSV file

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)
    for row in csv_reader:
        print(row[0])


with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    new_file = open('data.csv', 'w')
    writer = csv.writer(new_file)

    for data in writer:
        data[1:-1] = []
        writer.writerow(data)
# How to read selected lines in CSV file

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)
    for row in csv_reader:
        if csv_reader.line_num >5:
            print(row[0])


# How to find a particular value in CSV file

find_value = input('Enter the value to found: ')

read_file = open('data.csv', 'r')
csv_reader = csv.reader(read_file)

next(csv_reader)

for row in csv_reader:
    if find_value in row:
        print(row)


# Writing into a CSV file

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'Location'])
    csv_writer.writerow(['Alice', 28, 'New York'])
    csv_writer.writerow(['Bob', 32, 'Los Angeles'])

'''