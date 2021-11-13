import tkinter as tk
from tkinter import messagebox

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

    def searchCitizen(self, telCell: int = None, cuil: int = None, name: str = None):
        if cuil == None and telCell == None and name == None:
            alert = tk.messagebox.showwarning(title="Falta de argumentos", text="Para buscar un ciudadano es necesario que introduzca al menos un argumento")
        for ciudadano in self.__Ciudadanos:
            cuil = ciudadano.Get_Cuil() if cuil == None else cuil
            telCell = ciudadano.Get_Telefono() if telCell == None else telCell
            name = ciudadano.Get_Name() if name == None else name
            if ciudadano.Get_Cuil() == cuil and ciudadano.Get_Telefono() == telCell and ciudadano.Get_Name() == name:
                return ciudadano




