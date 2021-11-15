from EventIT.MapsSist.UbicacionClass import Ubicacion




class Sensor:
    def __init__(self, ubicacion, tipo):
        self.__ubicacion: Ubicacion = ubicacion
        self.__tipo: str  = tipo


    def get_ubicacion(self):
        return self.__ubicacion

    def get_tipo(self):
        return self.__tipo

    def detected_event(self):
        pass
