from MapsSist.UbicacionClass import Ubicacion


class Evento:
    def __init__(self, tipo, ubicacion: Ubicacion):
        self.__Tipo = tipo
        self.__Ubicacion = ubicacion
        self.__ListaAsistentes = []

    def Get_Info(self):
        #retorna la informacion del evento en conjunto con una copia de los asistentes
        return (self.__Tipo, self.__Ubicacion, self.__ListaAsistentes.copy())

    def Set_Attendance(self):
        #permite inscribirse o desinscribirse de un evento
        return self.__ListaAsistentes