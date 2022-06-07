from birthday_greetings.main import reader_csv_file, send_email

CSV_FILE_CONTENT = (
    ['last_name', 'first_name', 'date_of_birth', 'email'],
    [['Doe', 'John', '1982/10/08', 'john.doe@foobar.com'],
     ['Ann', 'Mary', '1975/09/11', 'mary.ann@foobar.com']]
)


def test_open_csv_file():

    result_data = reader_csv_file()

    assert result_data == CSV_FILE_CONTENT


def test_send_email():
    # Setup
    mock_fullname = 'luis mMoyon'
    expected_result = f'happy birthday dear {mock_fullname}'
    # Act

    result = send_email(mock_fullname)
    # Assert
    assert result == expected_result
    # Clean Up
