from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, name):
        self.__Name = name

    def Get_Name(self):
        return self.__Name
