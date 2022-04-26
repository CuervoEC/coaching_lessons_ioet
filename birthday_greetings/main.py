import csv

def reader_csv_file():
    with open('birthday_data.csv', newline='') as csvfile:
        birthday_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        csv_list = [row for row in birthday_reader]
        return csv_list[0]



print(reader_csv_file())
