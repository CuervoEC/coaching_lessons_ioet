from birthday_greetings.main import reader_csv_file


def test_open_csv_file():
    mocker.patch('builtins.open', )
    first_line = reader_csv_file()
    assert ['last_name', 'first_name', 'date_of_birth', 'email'] == first_line

