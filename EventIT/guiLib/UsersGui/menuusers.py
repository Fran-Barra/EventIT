import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.UsersLib.CitizenClass import Ciudadano


class MenuUsers(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, data_anses: DatasetANSES, user: Ciudadano):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("350x400")
        self.wm_resizable(0,0)
        self.data_anses = data_anses
        self.regDeUsuarios = regdeusuarios
        self.user = user
        self.Create_Widgets()



    def Open_Window(self, window):
        pass


    def Create_Widgets(self):
        #creacion de widgets
        self.rank_btn = tk.Button(self, text="Ranking")
        self.frien_btn = tk.Button(self, text="Friend")
        self.map_of_events_btn = tk.Button(self, text= "map")




        #impresion de widgets
        self.rank_btn.grid(row = 0, column = 0)
        self.frien_btn.grid(row = 1, column = 0)
        self.map_of_events_btn.grid(row= 2, column = 0)



