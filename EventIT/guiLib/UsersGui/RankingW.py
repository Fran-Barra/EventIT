import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.Estadisticas.Estadisticas import Estadisticas




class RankingW(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, dataanses: DatasetANSES, ranking: Estadisticas, user: Ciudadano):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("900x400")
        self.wm_resizable(0, 0)
        self.dataanses = dataanses
        self.regdeusuarios = regdeusuarios
        self.ranking = ranking
        self.user = user
        self.Create_Widgets()





    def Create_Widgets(self):

        # creacion de widgents
        self.rank_asis_x_zona_btn = tk.Button(self, text= "ranking por zona", command= lambda: self.show_ranking("zona"))
        self.rank_asis_max_btn = tk.Button(self, text= "ranking de asistencia max", command= lambda: self.show_ranking("max"))
        self.rank_asis_porcent_btn = tk.Button(self, text= "ranking por porcentajes", command= lambda: self.show_ranking("porcentaje"))




        # imprecion de widgets
        self.rank_asis_x_zona_btn.grid(row= 0, column= 0)
        self.rank_asis_max_btn.grid(row=1, column=0)
        self.rank_asis_porcent_btn.grid(row= 2, column= 0)


        #CANVAS
        global displayinfo
        global vsb
        global displayframe
        displayinfo = tk.Canvas(self, width=600, height=400, bg="white")
        displayinfo.grid(row=0, column= 3, rowspan = 20)


        vsb = tk.Scrollbar(self, orient= "vertical", command= displayinfo.yview())
        vsb.grid(row=0, column= 4, rowspan= 20, sticky= "ns")

        displayinfo.config(yscrollcommand = vsb.set)
        displayinfo.bind('<Configure>', lambda e: displayinfo.config(scrollregion = displayinfo.bbox("all")))

        displayframe = tk.Frame(displayinfo, bg="white")
        displayinfo.create_window((10, 0), window= displayframe, anchor="nw")




    def show_ranking(self, por):
        if por == "zona":
            ranking = self.ranking.calculate_positions_of_the_ranking(mayor_cantidad_de_asistentes_de_la_zona=True)
        elif por == "max":
            ranking = self.ranking.calculate_positions_of_the_ranking(mayor_cantidad_de_asistentes=True)
        elif por == "porcentaje":
            ranking = self.ranking.calculate_positions_of_the_ranking(mayor_porcentaje=True)
        else:
            ranking = []
        print(ranking)
        for evento in ranking:
            tk.Label(displayframe, text= f"Evento: {evento}").pack()








