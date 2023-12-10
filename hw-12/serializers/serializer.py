from abc import abstractmethod, ABC


class Serializer(ABC):
    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass