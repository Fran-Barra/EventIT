from typing import List
from EventIT.MapsSist.UbicacionClass import Ubicacion

class Zona:
    def __init__(self, ubicaciones: List[Ubicacion], numeroDeZona):
        self.__Ubicaciones = ubicaciones
        self.__NumeroDeZona = numeroDeZona

    def Get_Ubicaciones(self):
        return self.__Ubicaciones

    def Get_NumeroDeZona(self):
        return self.__NumeroDeZona
