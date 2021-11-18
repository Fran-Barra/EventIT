from abc import ABC, abstractmethod
import os


class Usuario(ABC):
    @abstractmethod
    def __init__(self, name):
        self.__Name = name

    def Get_Name(self):
        return self.__Name

    def Mod_Name(self, newName: str):
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_usuarios.txt'
        #Solo la puede llamar el AMB
        with open(path,'r') as f: # codigo para borrar usuarios
            lineas = f.readlines()
            with open(path,'w') as f:
                f.write('')
                f.close()
            for linea in lineas:
                if linea.split('/')[2] != self.__Name:
                    with open(path,'a') as f:
                        f.write(linea)
                        f.close()
            f.close()
        self.__Name = newName
