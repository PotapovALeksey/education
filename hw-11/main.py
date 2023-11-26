from collections import UserDict
import re
from datetime import date


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name: str):
        self.value = name

    @Field.value.setter
    def value(self, value):
        if not value:
            raise ValueError('The name is required')

        self.__value = value


class Phone(Field):
    def __eq__(self, other: str):
        return self.value == other

    def __init__(self, phone: str):
        self.value = phone

    @Field.value.setter
    def value(self, value):
        result = re.match(r'^\d{10}$', value)

        if result is None:
            raise ValueError('The phone must contain 10 digits')

        self.__value = value


class Birthday(Field):
    def __init__(self, birthday: date):
        if birthday is not None and type(birthday) != date:
            raise ValueError('The birthday must be a date type')

        super().__init__(birthday)

    @Field.value.setter
    def value(self, value):
        self.__value = value


class Record:
    def __init__(self, name: str, birthday: date = None, phones: list[Phone] = []):
        self.name = Name(name)
        self.phones = phones
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

        return self.phones

    def remove_phone(self, phone: str):
        self.phones = list(filter(lambda item: item.value != phone, self.phones))

        return self.phones

    def edit_phone(self, old_phone, new_phone):
        idx = self.phones.index(old_phone)
        self.phones[idx].value = new_phone

        return self.phones

    def find_phone(self, phone: str):
        phones = list(filter(lambda item: item.value == phone, self.phones))

        return phones[0] if len(phones) > 0 else None

    def days_to_birthday(self):
        today = date.today()
        closest_birthday = date(year=today.year, month=self.birthday.value.month, day=self.birthday.value.day)

        if today <= closest_birthday:
            return (closest_birthday - today).days

        closest_birthday.replace(year=closest_birthday.year + 1)

        return (closest_birthday - today).days


class AddressBook(UserDict):
    def __init__(self, records: list[Record] = [], pagination_size: int = 50):
        self.pagination_size = pagination_size
        self.pagination_offset = 0

        self.data = {record.name.value: record for record in records}

    def __iter__(self):
        return self

    def __next__(self):
        records = list(self.data.values())

        start_index = self.pagination_offset * self.pagination_size
        end_index = start_index + self.pagination_size

        if start_index < len(records):
            self.pagination_offset += 1

            return records[start_index:end_index]

        raise StopIteration

    def add_record(self, record: Record):
        self.data[record.name.value] = record

        return self.data

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name: str):
        self.data.pop(name, None)

        return self.data


records = [Record(f'Alex - {i}') for i in range(0, 101)]

for record_peace in AddressBook(records):
    print('record_peace', record_peace)
    print('len(record_peace)', len(record_peace))

