from unittest.mock import Mock
from pytest_mock import mocker
from birthday_greetings.main import get_full_name, reader_csv_file, build_email_message, send_email


CSV_FILE_CONTENT = (
    ['last_name', 'first_name', 'date_of_birth', 'email'],
    [['Doe', 'John', '1982/10/08', 'john.doe@foobar.com'],
     ['Ann', 'Mary', '1975/09/11', 'mary.ann@foobar.com']]
)


def test_open_csv_file():

    result_data = reader_csv_file()

    assert result_data == CSV_FILE_CONTENT


def test_build_email_message():
    # Setup
    mock_fullname = 'luis mMoyon'
    expected_result = f'happy birthday dear {mock_fullname}'
    # Act

    result = build_email_message(mock_fullname)
    # Assert
    assert result == expected_result
    # Clean Up

def test_get_full_name():
    mock_first_name = 'luis'
    mock_last_name = 'moyón'
    expected_result = 'luis moyón'

    result = get_full_name(mock_first_name, mock_last_name)

    assert result == expected_result

def test_send_email(mocker):
    import birthday_greetings.main as birthday 
    mocked_reader_csv_file = mocker.patch('birthday_greetings.main.reader_csv_file')
    mocked_reader_csv_file.side_effect = Mock(return_value = CSV_FILE_CONTENT)
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

    send_email()

    mocked_reader_csv_file.assert_called_once()
    assert spy_get_full_name.call_count == 2
    assert spy_build_email_message.call_count == 2
    spy_get_full_name.assert_has_calls(get_full_name_calls)
    spy_build_email_message.assert_has_calls(build_email_message_calls)
