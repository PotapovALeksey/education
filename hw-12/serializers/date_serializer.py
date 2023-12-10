from .serializer import Serializer
from datetime import datetime, date


class DateSerializer(Serializer):
    DATE_FORMAT = '%d.%m.%Y'


    @classmethod
    def serialize(self, value: date):
        return value.strftime(self.DATE_FORMAT)

    @classmethod
    def deserialize(cls, value: str):
        return datetime.strptime(value, cls.DATE_FORMAT).date()