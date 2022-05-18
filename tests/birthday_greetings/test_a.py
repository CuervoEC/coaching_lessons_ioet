from birthday_greetings.main import reader_csv_file


def test_open_csv_file(mocker):
    csv_content = ['last_name', 'first_name', 'date_of_birth', 'email']
    mocker.patch('birthday_greetings.main.reader_csv_file', return_value=csv_content)
    csv_reader = reader_csv_file()
    assert csv_reader == csv_content
