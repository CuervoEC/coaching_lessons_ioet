import datetime

import birthday_greetings.main as birthday


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


def test_send_email(mocker):
    mocked_reader_csv_file = mocker.patch('birthday_greetings.main.reader_csv_file')
    mocked_reader_csv_file.return_value = CSV_FILE_CONTENT
    spy_get_full_name = mocker.spy(birthday, 'get_full_name')
    spy_build_email_message = mocker.spy(birthday, 'build_email_message')
    get_full_name_calls = [
        mocker.call(first_name='John', last_name='Doe'), 
        mocker.call(first_name='Mary', last_name='Ann')
    ]
    build_email_message_calls = [
        mocker.call('John Doe'), 
        mocker.call('Mary Ann')
    ]

    birthday.send_email()

    mocked_reader_csv_file.assert_called_once()
    assert spy_get_full_name.call_count == len(CSV_FILE_CONTENT[1])
    assert spy_build_email_message.call_count == len(CSV_FILE_CONTENT[1])
    spy_get_full_name.assert_has_calls(get_full_name_calls)
    spy_build_email_message.assert_has_calls(build_email_message_calls)


def test_check_next_day_is_a_birthday(mocker):

    day_str = '1999/10/10'
    birthday_str = '1999/10/09'
    mock_actual_day = mocker.patch('datetime.datetime.now')
    mock_actual_day.return_value = datetime.datetime.strptime(day_str, '%Y/%m/%d')

    result = birthday.check_next_birthday(birthday_str)

    assert result is True


def test_check_next_day_is_not_a_birthday(mocker):

    day_str = '1999/09/10'
    birthday_str = '1999/10/09'
    mock_actual_day = mocker.patch('datetime.datetime.now')
    mock_actual_day.return_value = datetime.datetime.strptime(day_str, '%Y/%m/%d')

    result = birthday.check_next_birthday(birthday_str)

    assert result is False
