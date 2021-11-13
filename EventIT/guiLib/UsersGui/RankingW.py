import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES


class RegisterNewUserW(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, data_anses: DatasetANSES, user: Ciudadano):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("350x400")
        self.wm_resizable(0, 0)
        self.data_anses = data_anses
        self.regDeUsuarios = regdeusuarios
        self.user = user
        self.Create_Widgets()


    def Create_Widgets(self):
        # creacion de widgents
        pass



        # imprecion de widgets



    def Open_window(self, window):
        pass
