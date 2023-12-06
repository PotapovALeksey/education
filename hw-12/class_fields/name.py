from .field import Field


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

    def validate(self, value):
        if not value:
            raise ValueError('The name is required')

