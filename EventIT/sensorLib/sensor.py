from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.EventLib.EventoClass import Evento
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventManager import EventManger
from EventIT.sensorLib.RegDeSensores import RegDeSensores
import tkinter as tk
from tkinter import messagebox


class Sensor:
    def __init__(self, ubicacion, tipo, name):
        self.__ubicacion: Ubicacion = ubicacion
        self.__tipo: str = tipo
        self.__name = name

    def get_name(self):
        return self.__name

    def get_ubicacion(self):
        return self.__ubicacion

    def get_tipo(self):
        return self.__tipo

    def detected_event(self, nombre, regdeeventos: RegDeEventos, eventManager: EventManger):
        if self.__tipo in eventManager.ver_tiposDeEvento():
                regdeeventos.Set_Events(Evento(self.__tipo, self.__ubicacion, nombre), True)
        else:
            tk.messagebox.showwarning(title="Tipo de evento no permitido", text="Los eventos deben ser de alguno de los tipos avalados por el EventManager")
