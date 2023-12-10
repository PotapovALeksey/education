from .serializer import Serializer
from record import Record
from .date_serializer import DateSerializer


class CSVSerializer(Serializer):
    PHONE_SEPARATOR = '|'

    @classmethod
    def serialize(cls, row: Record):
        return {
            "phones": cls.PHONE_SEPARATOR.join(list(map(lambda phone: phone.value, row.phones))),
            "name": row.name.value,
            "birthday": DateSerializer.serialize(row.birthday.value),
        }

    @classmethod
    def deserialize(cls, record):
        phones = record['phones'].split(cls.PHONE_SEPARATOR) if len(record['phones']) >= 10 else []

        return Record(record['name'], DateSerializer.deserialize(record['birthday']), phones)
