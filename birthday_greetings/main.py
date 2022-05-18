import csv
import os


def reader_csv_file():
    csv_dir = os.path.dirname(__file__)
    rel_path = "birthday_data.csv"
    abs_file_path = os.path.join(csv_dir, rel_path)
    with open(abs_file_path, newline='') as csvfile:
        birthday_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        csv_list = [row for row in birthday_reader]
        return csv_list[0]


print(reader_csv_file())
