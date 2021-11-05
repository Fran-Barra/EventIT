from EventIT.MapsSist.ZonaClass import Zona
from typing import List

class Map:
    def __init__(self, zonas: List[Zona]):
        self.__Zonas = zonas

    def getListaDeZonas(self):
        return self.__Zonas.copy()
