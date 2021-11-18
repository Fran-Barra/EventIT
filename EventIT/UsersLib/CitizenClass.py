from EventIT.UsersLib.Users import Usuario


class Ciudadano(Usuario):
    def __init__(self, name, telefono, cuil):
        super().__init__(name)
        self.__Telefono = telefono
        self.__CUIL = cuil
        self.__ContactosDeInteres = []
        self.__ListaDeSolicitudes = []
        self.__ListaDeRechazos = []

    def __repr__(self):
        return f"{self.Get_Name()}"

    def Get_Telefono(self):
        return self.__Telefono

    def Get_Cuil(self):
        return self.__CUIL

    def Get_ContactosDeInteres(self):
        return self.__ContactosDeInteres.copy()

    def Get_ListaDeSolicitudes(self):
        return self.__ListaDeSolicitudes.copy()
    
    def Get_ListaDeRechazos(self):
        return self.__ListaDeRechazos.copy()

    def Mod_Telefono(self, telefono: str):
        #Solo la puede llamar el AMB
        self.__Telefono = telefono

    def Mod_CUIL(self, cuil: str):
        #Solo la puede llamar el AMB
        self.__CUIL = cuil

    def Mod_ContactosDeInteres(self, ciudadano, add: bool):
        """Permite agregar o eliminar un contacto.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo
            *Solo accedible por FrienshipSistem"""
        if add:
            self.__ContactosDeInteres.append(ciudadano)
        else:
            self.__ContactosDeInteres.remove(ciudadano)

    def Mod_ListaDeSolicitudes(self, ciudadano, add: bool):
        """Permite agregar o eliminar un ciudadano a la lista de solicitudes.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo
            *Solo accedible por FrienshipSistem"""
        if add:
            self.__ListaDeSolicitudes.append(ciudadano)
        else:
            self.__ListaDeSolicitudes.remove(ciudadano)

    def Mod_ListaDeRechazos(self, ciudadano, add: bool):
        """Permite agregar o eliminar un ciudadano a la lista de rechazos.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo
            *Solo accedible por FrienshipSistem"""
        if add:
            self.__ListaDeRechazos.append(ciudadano)
        else:
            self.__ListaDeRechazos.remove(ciudadano)

        
