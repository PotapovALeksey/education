class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self):
        return str(self.value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.validate(value)
        self.__value = value

    def validate(self, value):
        pass

    def serialize(self):
        return self.value

    @staticmethod
    def deserialize(value):
        return value
