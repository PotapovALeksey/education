import re
from .field import Field


class Phone(Field):
    def __eq__(self, other: str):
        return self.value == other

    def __init__(self, phone: str):
        super().__init__(phone)

    def validate(self, value):
        result = re.match(r'^\d{10}$', value)

        if result is None:
            raise ValueError('The phone must contain 10 digits')
