from .storage import Storage
from csv import DictReader, DictWriter
from pathlib import Path
from serializers.csv_serializer import CSVSerializer

class CSVStorage(Storage):
    def __init__(self, path: Path, fieldnames: [str]):
        self.path = path
        self.fieldnames = fieldnames

    def get_contacts_from_storage(self):
        contacts = []

        with open(self.path, 'r', newline='') as file:
            reader = DictReader(file, fieldnames=self.fieldnames)

            for row in reader:
                if self.is_header_row(row):
                    continue

                contacts.append(CSVSerializer.deserialize(row))

        return contacts

    def update_storage(self, records):
        with open(self.path, 'w', newline='') as file:
            writer = DictWriter(file, fieldnames=self.fieldnames)

            writer.writeheader()

            for record in records:
                writer.writerow(CSVSerializer.serialize(record))

    def is_header_row(self, row):
        for field_name in self.fieldnames:

            if row[field_name] != field_name:
                return False

        return True

