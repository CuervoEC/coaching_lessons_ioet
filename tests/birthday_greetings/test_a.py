import datetime

import birthday_greetings.main as birthday
from unittest.mock import Mock, patch


CSV_FILE_CONTENT = (
    ['last_name', 'first_name', 'date_of_birth', 'email'],
    [
        ['Doe', 'John', '1982/10/08', 'john.doe@foobar.com'],
        ['Ann', 'Mary', '1975/09/11', 'mary.ann@foobar.com'],
        ['Luis', 'Lopez', '1999/10/08', 'luis.lopez@foobar.com']
    ]
)


# @pytest.fixture
# def reader_csv_file_fixture(mocker):
#     mocked_reader_csv_file = mocker.patch('birthday_greetings.main.reader_csv_file')
#     mocked_reader_csv_file.return_value = CSV_FILE_CONTENT


def test_open_csv_file():

    result_data = birthday.reader_csv_file()

    assert result_data == CSV_FILE_CONTENT


def test_build_email_message():
    # Setup
    mock_fullname = 'Luis Moyon'
    expected_result = f'happy birthday dear {mock_fullname}'
    # Act

    result = birthday.build_email_message(mock_fullname)
    # Assert
    assert result == expected_result
    # Clean Up


def test_get_full_name():
    mock_first_name = 'Luis'
    mock_last_name = 'Moyon'
    expected_result = 'Luis Moyon'

    result = birthday.get_full_name(mock_first_name, mock_last_name)

    assert result == expected_result


def test_check_next_day_is_a_birthday(mocker):

   day_str = '1999/10/08'
   birthday_str = '1999/10/09'
   datetime_mock = mocker.Mock(wraps=datetime.datetime)
   datetime_mock.now.return_value = datetime.datetime.strptime(day_str, '%Y/%m/%d')
   with patch('datetime.datetime', new=datetime_mock):
    result = birthday.check_next_birthday(birthday_str)

    assert result is True


def test_check_next_day_is_not_a_birthday(mocker):

   day_str = '1999/09/10'
   birthday_str = '1999/10/09'
   datetime_mock = mocker.Mock(wraps=datetime.datetime)
   datetime_mock.now.return_value = datetime.datetime.strptime(day_str, '%Y/%m/%d')
   with patch('datetime.datetime', new=datetime_mock):
    result = birthday.check_next_birthday(birthday_str)
    assert result is False

def test_send_birthday_reminder(mocker):
   mocked_reader_csv_file = mocker.patch('birthday_greetings.main.reader_csv_file')
   mocked_reader_csv_file.return_value = CSV_FILE_CONTENT
   day_str = '1975/09/10'
   datetime_mock = mocker.Mock(wraps=datetime.datetime)
   datetime_mock.now.return_value = datetime.datetime.strptime(day_str, '%Y/%m/%d')
   with patch('datetime.datetime', new=datetime_mock):
    result = birthday.send_birthday_reminder()
    assert result == ['happy birthday dear Mary Ann']
    