import tkinter as tk

class LogUser(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #self.pack()
        self.Create_Widgets()

    def Create_Widgets(self):
        #creacion de widgets
        title = tk.Label(self, text="Log User")


        #impresion de widgets
        centerW = 150

        title.grid(row=1, column= centerW)