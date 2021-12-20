import unittest

from password import User


class TestPassword(unittest.TestCase):

    def test_empty_user_data(self):
        user = User([])
        user_data = user.get_data()
        self.assertEqual(user_data, [])

    def test_get_user_username(self):
        user = User(['Roberto'])
        username = user.get_username()
        self.assertEqual(username, 'Roberto')

    def test_get_another_username(self):
        user = User(['Elisa'])
        username = user.get_username()
        self.assertEqual(username, 'Elisa')


if __name__ == '__main__':
    pass
