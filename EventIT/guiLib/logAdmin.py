import tkinter as tk

class LogAdmin(tk.Tk):
    def __init__(self, regdeusuarios):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("350x400")
        self.wm_resizable(0,0)
        self.Create_Widgets()
        self.regdeusuarios = regdeusuarios

    def Create_Widgets(self):
        #creacion de widgets
        title = tk.Label(self, text="Log Admin")


        #impresion de widgets
        centerW = 150

        title.grid(row=1, column= centerW)
