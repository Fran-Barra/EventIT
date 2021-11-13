class RegDeUsuarios:
    def __init__(self):
        self.__Admins = {}
        self.__Ciudadanos = {}

    def Get_Admins(self):
        return self.__Admins.copy()

    def Get_Ciudadanos(self):
        return self.__Ciudadanos.copy()

    def Manage_Admins(self):
        return self.__Admins

    def Manage_Ciudadanos(self):
        return self.__Ciudadanos

    def searchCitizen(self, telCell: int = 0, cuil: int = 0, name: int = None):
        for ciudadano in self.__Ciudadanos:
            if ciudadano.Get_Cuil() == cuil and ciudadano.Get_Telefono() == telCell:
                return ciudadano
        



