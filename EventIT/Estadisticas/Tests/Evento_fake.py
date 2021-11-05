from EventIT.MapsSist.UbicacionClass import Ubicacion


class Evento:
    def __init__(self, tipo, ubicacion: Ubicacion):
        self.__Tipo = tipo
        self.__Ubicacion = ubicacion
        self.__ListaAsistentes = []

    def getTipo(self):
        return self.__Tipo

    def getUbicacion(self):
        return self.__Ubicacion

    def getListaDeAsistencia(self):
        return self.__ListaAsistentes.copy()

    def getZona(self, lista_de_zonas):
        for zona in lista_de_zonas:
            if self.__Ubicacion in zona: #la idea es ver si esa ubicacion es parte de la zona PROBAR
                return zona
