class Ubicacion:
    def __init__(self, latitud, longitud):
        self.__Latitud = latitud
        self.__Longitud = longitud

    def Get_Coordinates(self):
        return (self.__Latitud, self.__Longitud)