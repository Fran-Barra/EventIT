from Users import Usuario

class Ciudadano(Usuario):
    def __init__(self, name, telefono, cuil):
        super().__init__(name)
        self.__Telefono = telefono
        self.__CUIL = cuil
        self.__ContactosDeInteres = []
        self.__ListaDeSolicitudes = []
        self.__ListaDeRechazos = []
        
    def Get_Telefono(self):
        return self.__Telefono

    def Get_Cuil(self):
        return self.__CUIL

    def Get_ContactosDeInteres(self):
        return self.__ContactosDeInteres.copy()

    def Get_ListaDeSolicitudes(self):
        return self.__ListaDeSolicitudes.copy()

    def Mod_Name(self, name: str):
        #Solo la puede llamar el AMB
        self.__Name = name

    def Mod_Telefono(self, telefono: str):
        #Solo la puede llamar el AMB
        self.__Telefono = telefono

    def Mod_CUIL(self, cuil: str):
        #Solo la puede llamar el AMB
        self.__CUIL = cuil

    def Mod_ContactosDeInteres(self):
        #Solo accedible por FrienshipSistem
        return self.__ContactosDeInteres

    def Mod_ListaDeSolicitudes(self):
        #Solo accedible por FrienshipSistem
        return self.__ListaDeSolicitudes
    
    def Mod_ListaDeRechazos(self):
        #Solo accedible por FrienshipSistem
        return self.__ListaDeRechazos
        
