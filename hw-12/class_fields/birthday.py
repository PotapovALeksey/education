from .field import Field
from datetime import date, datetime


class Birthday(Field):
    DATE_FORMAT = '%d.%m.%Y'

    def __init__(self, birthday: date):
        super().__init__(birthday)

    def __str__(self):
        return self.value.strftime(self.DATE_FORMAT)

    def validate(self, value):
        if value is not None and type(value) != date:
            raise ValueError('The birthday must be a date type')

    def serialize(self):
        return self.value.strftime(self.DATE_FORMAT)

    @classmethod
    def deserialize(cls, value: str):
        return datetime.strptime(value, cls.DATE_FORMAT).date()