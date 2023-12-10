from collections import UserDict
from datetime import date
from random import randint
from record import Record
from pathlib import Path
from storages.storage import Storage
from storages.csv_storage import CSVStorage

CSV_STORAGE_PATH = Path('db', 'contacts-db.csv')
FIELD_NAMES = ['name', 'birthday', 'phones']

class AddressBook(UserDict):
    def __init__(self, storage: Storage, records: list[Record] = [], pagination_size: int = 50):
        self.pagination_size = pagination_size
        self.storage = storage
        self.pagination_offset = 0

        stored_contacts = self.storage.get_contacts_from_storage()
        self.data = {record.name.value: record for record in [*stored_contacts, *records]}

        self.storage.update_storage(self.data.values())

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

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        self.storage.update_storage(self.data.values())

        return self.data

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name: str):
        self.data.pop(name, None)
        self.storage.update_storage(self.data.values())

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


# records = [Record(f'Ivan - {i}', date(year=int(f'19{randint(11, 99)}'), month=randint(1, 12), day=randint(1,28)), ['0638501099', '0671234567']) for i in range(0, 20)]

address_book = AddressBook(CSVStorage(CSV_STORAGE_PATH, FIELD_NAMES))
# address_book.add_record(Record('BREZENK', date(year=1994, month=11, day=18)))
# for item in address_book:
#     print(item)


print(address_book.search('BREZENK'))