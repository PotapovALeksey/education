from collections import UserDict
from datetime import date
from csv import DictWriter, DictReader
from random import randint
from record import Record
from pathlib import Path
from storages.storage import Storage

DEFAULT_STORAGE_PATH = Path('db', 'contacts-db.csv')
FIELD_NAMES = ['name', 'birthday', 'phones']


def is_header_row(row):
    return row['name'] == 'name' and row['phones'] == 'phones' and row['birthday'] == 'birthday'


class AddressBook(UserDict):
    def __init__(self, records: list[Record] = [], storage: Storage = Storage(), pagination_size: int = 50):
        self.pagination_size = pagination_size
        self.storage = storage
        self.pagination_offset = 0

        stored_contacts = self.storage.get_contacts_from_storage()
        self.data = {record.name.value: record for record in [*stored_contacts, *records]}

        self.storage.update_storage()

    def __iter__(self):
        return self

    def __next__(self):
        records = list(self.data.values())

        start_index = self.pagination_offset * self.pagination_size
        end_index = start_index + self.pagination_size

        if start_index < len(records):
            self.pagination_offset += 1

            return records[start_index:end_index]

        iteration = StopIteration
        raise iteration

    def get_contacts_from_storage(self):
        contacts = []

        try:
            with open(self.storage_path, 'r', newline='') as file:
                reader = DictReader(file, fieldnames=FIELD_NAMES)

                for row in reader:
                    if is_header_row(row):
                        continue

                    contacts.append(Record.deserialize(row))

        except FileNotFoundError:
            pass

        return contacts

    def update_storage(self):
        with open(self.storage_path, 'w', newline='') as file:
            writer = DictWriter(file, fieldnames=FIELD_NAMES)

            writer.writeheader()

            for record in self.data.values():
                writer.writerow(record.serialize())

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        self.storage.update_storage()

        return self.data

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name: str):
        self.data.pop(name, None)
        self.storage.update_storage()

        return self.data

    @staticmethod
    def is_existing_in_phone(value: str, record: Record):
        if len(record.phones) == 0:
            return False

        return list(filter(lambda phone: value in phone.value, record.phones))

    def search(self, value: str):
        return list(filter(
            lambda record: value.casefold() in record.name.value.casefold() or self.is_existing_in_phone(value, record),
            self.data.values()
        ))


records = [Record(f'John - {i}', date(year=int(f'19{randint(11, 99)}'), month=randint(1, 12), day=randint(1,28)), ['0638501099', '0671234567']) for i in range(0, 20)]
# records = [Record('Ivan', date(year=1994, month=11, day=18))]

address_book = AddressBook()

# for item in address_book:
#     print(item)


print(len(address_book.search()))