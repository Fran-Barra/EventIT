from EventIT.EventLib.EventoClass import Evento


class RegDeEventos:
    def __init__(self):
        self.__Eventos: list[Evento] = []

    def __repr__(self):
        return 'RegDeEventos'

    def Set_Events(self, evento: Evento, add: bool):
        """Permite inscribirse o desinscribirse de un evento.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo"""
        if add:
            self.__Eventos.append(evento)
        else:
            self.__Eventos.remove(evento)

    def View_Events(self)-> list[Evento]:
        return self.__Eventos.copy()

    def Search_events(self, name):
        for evento in self.__Eventos:
            if evento.getname() == name:
                return evento
        return False

