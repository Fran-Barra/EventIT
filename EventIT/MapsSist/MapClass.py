from EventIT.MapsSist.ZonaClass import Zona
from typing import List

class Map:
    def __init__(self, zonas: List[Zona]):
        self.__Zonas = zonas

    def __repr__(self):
        return f"{self.__Zonas}"

    def getListaDeZonas(self):
        return self.__Zonas.copy()
