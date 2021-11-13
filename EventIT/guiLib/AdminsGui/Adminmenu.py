import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.AdminClass import Administrator

class AdminMenu(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, admin: Administrator):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("350x400")
        self.wm_resizable(0,0)
        self.admin = admin
        self.regdeusuarios = regdeusuarios
        self.Create_Widgets()


    def Create_Widgets(self):
        #creacion de widgets
        pass




        #impresion de widgets



    def Open_Window(self, window):
        pass

