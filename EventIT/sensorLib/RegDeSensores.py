from EventIT.sensorLib.sensor import Sensor
import tkinter as tk
from tkinter import messagebox


class RegDeSensores:
    def __init__(self):
        self.__sensores: list[Sensor] = []

    def __repr__(self):
        return 'RegDeSensores'

    def Set_Sensors(self, sensor: Sensor, add: bool):
        """Permite inscribirse o desinscribirse de un evento.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo"""
        if add:
            if sensor.get_name() not in list(map(lambda x:x.get_name(), self.__sensores)):
                self.__sensores.append(sensor)
            else:
                tk.messagebox.showwarning(title="Sensor invalido", text="El sensor que intenta agregar ya se encuentra en el registro")

        else:
            self.__sensores.remove(sensor)

    def View_Sensors(self)-> list[Sensor]:
        return self.__sensores.copy()

    def Search_sensor(self, name):
        for sensor in self.__sensores:
            if sensor.get_name() == name:
                return sensor
        return False

