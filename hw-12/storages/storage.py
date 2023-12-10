from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, path: str):
        pass

    @abstractmethod
    def get_contacts_from_storage(self):
        return []

    @abstractmethod
    def update_storage(self, records: []):
        pass
