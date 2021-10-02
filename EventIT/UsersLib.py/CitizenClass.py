from Users import Usuario

class Ciudadano(Usuario):
    def __init__(self, Name, telefono, cuil):
        super().__init__(Name)
        self.__Telefono = telefono
        self.__CUIL = cuil
        self.__CuentBloqueada = False
        self.__ContactosDeInteres = []
        