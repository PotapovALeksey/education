from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name: str):
        if not name:
            raise ValueError('The name is required')

        super().__init__(name)


class Phone(Field):
    def __eq__(self, other: str):
        return self.value == other

    def __init__(self, phone: str):
        result = re.match(r'^\d{10}$', phone)

        if result == None:
            raise ValueError('The phone must contain 10 digits')

        super().__init__(phone)


class Record:
    def __init__(self, name: str, phones: [Phone] = []):
        self.name = Name(name)
        self.phones = phones

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


class AddressBook(UserDict):
    def __init__(self, records: [Record] = []):
        self.data = { [record.name]: record for record in records }

    def add_record(self, record: Record):
        self.data[record.name.value] = record

        return self.data

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name: str):
        self.data.pop(name, None)

        return self.data
