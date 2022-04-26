import unittest

from fizz_buzz.fizz_buzz.fizz_buzz import fizz_buzz


class FizzBuzzTestClass(unittest.TestCase):

    def setUp(self) -> None:
        super(FizzBuzzTestClass, self).setUp()
        self.mock_data = [1, 2, 3, 4, 5]

    def test_should_show_number_if_is_not_multiple_of_three(self):

        # Arrange
        number_input = self.mock_data[0]

        # Act
        result = fizz_buzz(number_input)

        # Assert
        self.assertEqual(number_input, result)

    def test_should_show_fizz_with_multiple_of_three(self):

        # Arrange
        number_input = self.mock_data[2]

        # Act
        result = fizz_buzz(number_input)

        # Assert
        self.assertEqual('fizz', result)

    def test_should_show_buzz_with_multiple_of_three(self):
        # Arrange
        number_input = self.mock_data[4]

        # Act
        result = fizz_buzz(number_input)

        # Assert
        self.assertEqual('buzz', result)

    def tearDown(self) -> None:
        super(FizzBuzzTestClass, self).setUp()
        self.mock_data = []


if __name__ == '__main__':
    unittest.main()
