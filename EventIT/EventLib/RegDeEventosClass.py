from EventIT.EventLib.EventoClass import Evento


class RegDeEventos:
    def __init__(self):
        self.__Eventos: list[Evento] = []

    def __repr__(self):
        return 'RegDeEventos'

    def Set_Events(self):
        return self.__Eventos

    def View_Events(self)-> list[Evento]:
        return self.__Eventos.copy()
