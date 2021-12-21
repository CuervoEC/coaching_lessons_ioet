from typing import List
from dataclasses import dataclass
from hashlib import blake2b


@dataclass
class User(object):
    user_data: List

    def get_data(self):
        return self.user_data

    def get_username(self):
        return self.user_data[0]

    def get_password(self):
        b_password = bytes(str(self.user_data[1]), 'utf8')
        hashed_password = blake2b(b_password).hexdigest()
        return hashed_password

    def check_valid_credentials(self, credentials: List):
        hashed_credential = blake2b(bytes(str(credentials[1]), 'utf8')).hexdigest()
        if self.get_username() == credentials[0] and self.get_password() == hashed_credential:
            return True
        return False
