from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod #no estoy seguro si el __init__ puede ser @abstractmethod
    def __init__(self, Name):
        self.__Name = Name
