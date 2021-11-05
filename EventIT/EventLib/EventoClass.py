from EventIT.MapsSist.UbicacionClass import Ubicacion


class Evento:
    def __init__(self, tipo, ubicacion: Ubicacion, nombre):
        self.__Tipo = tipo
        self.__Ubicacion = ubicacion
        self.__ListaAsistentes = []
        self.__nombre = nombre

    def __repr__(self):
        return self.__nombre

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

    def Set_Attendance(self):
        #permite inscribirse o desinscribirse de un evento
        return self.__ListaAsistentes
