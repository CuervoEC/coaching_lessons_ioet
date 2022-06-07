import csv
import os


def reader_csv_file():
    csv_dir = os.path.dirname(__file__)
    rel_path = "birthday_data.csv"
    abs_file_path = os.path.join(csv_dir, rel_path)
    with open(abs_file_path, newline='') as csvfile:
        birthday_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        csv_list = [row for row in birthday_reader]
        headers = csv_list[0]
        body = csv_list[1:]
        return headers, body


def send_email(name):
    email = f'happy birthday dear {name}'
    return email


print(reader_csv_file())
