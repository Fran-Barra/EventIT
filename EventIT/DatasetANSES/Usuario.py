from abc import ABC, abstractmethod

class Usuario(ABC):
    @abstractmethod
    def getId(self):
        pass



