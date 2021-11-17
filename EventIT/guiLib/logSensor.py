import tkinter as tk

class LogSensor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(0,0)
        self.Create_Widgets()

    def Create_Widgets(self):
        #creacion de widgets
        title = tk.Label(self, text="Log Sensor")


        #impresion de widgets
        centerW = 150

        title.grid(row=1, column= centerW)
