from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.EventLib.EventoClass import Evento
from EventIT.EventLib.RegDeEventosClass import RegDeEventos




class Sensor:
    def __init__(self, ubicacion, tipo, name):
        self.__ubicacion: Ubicacion = ubicacion
        self.__tipo: str = tipo
        self.__name = name

    def get_name(self):
        return self.__name

    def get_ubicacion(self):
        return self.__ubicacion

    def get_tipo(self):
        return self.__tipo

    def detected_event(self, nombre, regdeeventos: RegDeEventos):
        regdeeventos.Set_Events(Evento(self.__tipo, self.__ubicacion, nombre), True)
