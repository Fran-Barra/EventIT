



class RegDeUsuarios:
    def __init__(self):
        self.__Admins = []
        self.__Ciudadanos = {}


    def Get_Admins(self):
        return self.__Admins.copy()


    def Get_Ciudadanos(self):
        return self.__Ciudadanos.copy()

    def Manage_Admins(self):
        return self.__Admins

    def Manage_Ciudadanos(self):
        return self.__Ciudadanos
        



