from .serializer import Serializer
from record import Record
from class_fields.birthday import Birthday


class CSVSerializer(Serializer):
    PHONE_SEPARATOR = '|'

    @classmethod
    def serialize(cls, row: Record):
        return {
            "phones": cls.PHONE_SEPARATOR.join(list(map(lambda phone: phone.serialize(), row.phones))),
            "name": row.name.serialize(),
            "birthday": row.birthday.serialize(),
        }

    @classmethod
    def deserialize(cls, record):
        phones = record['phones'].split(cls.PHONE_SEPARATOR) if len(record['phones']) >= 10 else []

        return Record(record['name'], Birthday.deserialize(record['birthday']), phones)
