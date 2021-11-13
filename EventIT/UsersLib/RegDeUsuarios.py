import tkinter as tk
from tkinter import messagebox
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.UsersLib.CitizenClass import Ciudadano

class RegDeUsuarios:
    def __init__(self):
        self.__Admins = dict({})
        self.__Ciudadanos = dict({})

    def Get_Admins(self):
        return self.__Admins.copy()

    def Get_Ciudadanos(self):
        return self.__Ciudadanos.copy()

    # def Manage_Admins(self):
    #     return self.__Admins

    def Manage_Admins(self, admin: Administrator, add: bool, keyname):
        """Permite agregar o eliminar un admin del dicccionario de administradores.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo"""
        if add:
            self.__Admins[keyname] = admin
        else:
            del self.__Admins[keyname]

    # def Manage_Ciudadanos(self):
    #     return self.__Ciudadanos

    def Manage_Ciudadanos(self, ciudadano: Ciudadano, add: bool, keyname):
        """Permite agregar o eliminar un ciudadano del dicccionario de ciudadanos.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo"""
        if add:
            self.__Ciudadanos[keyname] = [ciudadano, 0]
        else:
            del self.__Ciudadanos[keyname]

    def searchCitizen(self, telCell: int = None, cuil: int = None, name: str = None):
        if cuil == None and telCell == None and name == None:
            alert = tk.messagebox.showwarning(title="Falta de argumentos", text="Para buscar un ciudadano es necesario que introduzca al menos un argumento")
        for ciudadano in list(map(lambda x:x[0], list(self.__Ciudadanos.values()))):
            cuilAux = ciudadano.Get_Cuil() if cuil == None else cuil
            telCellAux = ciudadano.Get_Telefono() if telCell == None else telCell
            nameAux = ciudadano.Get_Name() if name == None else name
            if ciudadano.Get_Cuil() == cuilAux and ciudadano.Get_Telefono() == telCellAux and ciudadano.Get_Name() == nameAux:
                return ciudadano
