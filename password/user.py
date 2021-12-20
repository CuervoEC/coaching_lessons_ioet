from typing import List
from dataclasses import dataclass


@dataclass
class User(object):
    user_data: List

    def get_data(self):
        return self.user_data

    def get_username(self):
        return self.user_data[0]
