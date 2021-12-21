import unittest
from hashlib import blake2b

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

    def test_get_hash_password(self):
        user = User(['', 55555])
        user_password = user.get_password()
        self.assertEqual(user_password, blake2b(b'55555').hexdigest())

    def test_check_valid_user_credentials(self):
        user = User(['Jose', 12345])
        valid_credential = user.check_valid_credentials(['Jose', 12345])
        invalid_credential = user.check_valid_credentials(['Maria', 11111])
        self.assertTrue(valid_credential)
        self.assertFalse(invalid_credential)


if __name__ == '__main__':
    pass
