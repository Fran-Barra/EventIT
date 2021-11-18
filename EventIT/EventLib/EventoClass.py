from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.UsersLib.CitizenClass import Ciudadano


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
            if self.__Ubicacion.Get_Coordinates() in list(map(lambda x:x.Get_Coordinates(), zona.Get_Ubicaciones())): #la idea es ver si esa ubicacion es parte de la zona PROBAR
                return zona

    def getname(self):
        return self.__nombre

    def Set_Attendance(self, ciudadano: Ciudadano, inscribirse: bool):
        """Permite inscribirse o desinscribirse de un evento.\n
            inscribirse = True, para inscribirse.\n
            inscribirse = False, para desinscribirse"""
        if inscribirse:
            self.__ListaAsistentes.append(ciudadano)
        else:
            self.__ListaAsistentes.remove(ciudadano)
            # for asistente, index in enumerate(self.__ListaAsistentes):
            #     if asistente == ciudadano:
            #         del self.__ListaAsistentes[index]


