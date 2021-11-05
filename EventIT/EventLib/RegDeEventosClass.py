class RegDeEventos:
    def __init__(self):
        self.__Eventos = []

    def __repr__(self):
        return 'RegDeEventos'

    def Set_Events(self):
        return self.__Eventos

    def View_Events(self):
        return self.__Eventos.copy()
