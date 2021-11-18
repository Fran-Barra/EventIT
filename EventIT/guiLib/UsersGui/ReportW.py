import tkinter as tk
from tkinter import messagebox

from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventManager import EventManger
from EventIT.MapsSist.MapClass import Map

class ReportW(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, data_anses: DatasetANSES, regdeeventos: RegDeEventos,
                 eventmanager: EventManger, mapa: Map, user: Ciudadano):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(0,0)
        self.dataanses = data_anses
        self.regdeusuarios = regdeusuarios
        self.regdeeventos = regdeeventos
        self.eventmanager = eventmanager
        self.mapa = mapa
        self.user = user
        self.Create_Widgets()


    def Create_Widgets(self):
        #creacion de widgets
        self.tipo = tk.Entry(self)
        self.ubicacion = tk.Entry(self)
        self.name = tk.Entry(self)

        self.type_ofe_btn = tk.Button(self, text="Type of events ", command= self.see_type_Events)
        self.report_e = tk.Button(self, text= "Report event", command= lambda: self.report_event())

        self.a_name = tk.Entry(self)
        self.invitados = tk.Entry(self, width= 25)

        self.asist_btn = tk.Button(self, text= "Asist to event", command= self.asistir_evento)

        #impresion de widgets
        self.tipo.insert(0, "type")
        self.tipo.grid(row=0, column = 0)
        self.ubicacion.insert(0, "latitude,longitude")
        self.ubicacion.grid(row= 0, column= 1)
        self.name.insert(0, "name")
        self.name.grid(row= 0, column= 2)


        self.type_ofe_btn.grid(row = 1, column = 0)
        self.report_e.grid(row= 1, column= 1)

        self.a_name.insert(0, "name of event")
        self.a_name.grid(row = 2, column = 0)
        self.invitados.insert(0, "invitado1,invitado2,.../none")
        self.invitados.grid(row= 2, column= 1)

        self.asist_btn.grid(row= 3, column= 0)

    def see_type_Events(self):
        type_e = self.eventmanager.ver_tiposDeEvento()
        for type in type_e:
            tk.Label(self, text= f"type: {type}").pack()

    def report_event(self):
        try:
            tipo = self.tipo.get()
            coordenadasstr = self.ubicacion.get()
            if coordenadasstr.find(",") == -1:
                messagebox.showwarning(title= "Syntax error", message= "Remember to divide latitude and longitude by: ,\n latitude,longitude")
            else:
                (lat, lon) = coordenadasstr.split(",")
                ubicacion = self.mapa.search_ubicacion(int(lat), int(lon))
                nombre = self.name.get()
                if ubicacion == False:
                    messagebox.showwarning(title= "Not found", message= "The location couldnt be found")
                else:
                    self.eventmanager.report_evento(tipo, ubicacion, nombre)
        except ValueError:
            messagebox.showwarning(title= "Wrong values", messagebox= "only numbers should be in latitude, longitude")

    def asistir_evento(self):
        evento = self.regdeeventos.Search_events(self.a_name.get())
        if evento == False:
            messagebox.showwarning(title= "Event not found", message= "there ist a event with that name")
        else:
            invitadosstr = self.invitadosget()
            if "," in invitadosstr:
                keyname_invitados = invitadosstr.split(",")

                keyname_not_in = 0
                user_not_found = False
                for keyname in keyname_invitados:
                    if keyname not in self.regdeusuarios.Get_Ciudadanos():
                        user_not_found = True
                        keyname_not_in += 1
                if keyname_not_in:
                    messagebox.showwarning(title= "Users not found", messagebox= f"We couldt found {keyname_not_in} of the users")
                else:
                    invitados = []
                    for keyname in keyname_invitados:
                        invitado = self.regdeusuarios.Get_Ciudadanos()[keyname]
                        invitados.append(invitado)
                    self.eventmanager.asistir_evento(evento, self.user, invitados)

            elif invitadosstr == "none":
                self.eventmanager.asistir_evento(evento, self.user)
            else:
                messagebox.showwarning(title="Manage guests", message= "if you dont have guests write none or remember to use ,"
                                                                       "between eack keyname")







