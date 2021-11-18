import tkinter as tk

class MenuUsers(tk.Tk):
    def __init__(self, regdeeventos: RegDeEventos, eventmanager: EventManger, mapa: Map):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(0,0)
        self.regdeeventos = regdeeventos
        self.eventmanager = eventmanager
        self.mapa = mapa
        self.Create_Widgets()



    def Open_Window(self, window):
        if window == RankingW:
            RankingW(self.regdeusuarios, self.dataanses, self.mapa, self.ranking, self.user)
        if window == FrienshipW:
            FrienshipW(self.regdeusuarios, self.user)
        if window == ReportW:
            ReportW(self.regdeusuarios, self.dataanses, self.regdeeventos, self.eventmanager, self.mapa, self.user)



    def Create_Widgets(self):
        #creacion de widgets
        self.boton = tk.Button(self, text="Ranking", command= lambda: self.Open_Window(RankingW))




        #impresion de widgets
        self.boton.grid(row = 0, column = 0)

