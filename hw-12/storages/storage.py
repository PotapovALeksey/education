from abc import ABC, abstractmethod


class Storage(ABC):
    def get_contacts_from_storage(self):
        return []

    def update_storage(self):
        pass
