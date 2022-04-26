import unittest

from fizz_buzz.fizz_buzz.fizz_buzz import fizz_buzz


class FizzBuzzTestClass(unittest.TestCase):

    # Previous test question (What should we validate before a multiple of 3?)

    def test_should_show_number_if_is_not_multiple_of_three(self):

        # Arrange
        number_input = 1

        # Act
        result = fizz_buzz(number_input)

        # Assert
        self.assertEqual(number_input, result)

    def test_should_show_fizz_with_multiple_of_three(self):

        # Arrange
        number_input = 3

        # Act
        result = fizz_buzz(number_input)

        # Assert
        self.assertEqual('fizz', result)

    def test_should_show_buzz_with_multiple_of_three(self):
        # Arrange
        number_input = 5

        # Act
        result = fizz_buzz(number_input)

        # Assert
        self.assertEqual('buzz', result)


if __name__ == '__main__':
    unittest.main()
