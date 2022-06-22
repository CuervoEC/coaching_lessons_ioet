import csv
import datetime
import os


def reader_csv_file():
    csv_dir = os.path.dirname(__file__)
    rel_path = "birthday_data.csv"
    abs_file_path = os.path.join(csv_dir, rel_path)
    with open(abs_file_path, newline='') as csvfile:
        birthday_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        csv_list = [row for row in birthday_reader]
        header = csv_list[0]
        body = csv_list[1:]
        return header, body


def build_email_message(name):
    email = f'happy birthday dear {name}'
    return email


def get_full_name(first_name, last_name):
    return f'{first_name} {last_name}'


def send_email():
    header, body = reader_csv_file()
    first_name_index = header.index('first_name')
    last_name_index = header.index('last_name')
    for line in body:
        full_name = get_full_name(first_name=line[first_name_index], last_name=line[last_name_index])
        build_email_message(full_name)


def check_next_birthday(birthday_str):
    actual_date = datetime.datetime.now()
    birthday_date = datetime.datetime.strptime(birthday_str, '%Y/%m/%d')
    if birthday_date.month - actual_date.month == 0 and birthday_date.day - actual_date.day == 1:
        return True
    return False
