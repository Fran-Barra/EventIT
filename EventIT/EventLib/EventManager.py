from AdminClass import Administrator
from RegDeEventosClass import RegDeEventos
from EventoClass import Evento

class EventManger:

    def __init__(self, RegDeEvento):
        self.__RegDeEventos = RegDeEvento
        self.__TipoDeEventos = []

    def alta_tiposDeEvento(self, TipoDeEvento, User):
        # El admin da de alta tipos de eventos, para que a la hora de crear eventos solo sean de los tipos de eventos aprobados.
        if User.isinstance(Administrator) and TipoDeEvento not in self.__TipoDeEventos:
            self.__TipoDeEventos.append(TipoDeEvento)

    def ver_tiposDeEvento (self):
        return self.__TipoDeEventos.copy()

    def report_evento(self, tipo, ubicacion):
        # Se guardan nuevos eventos en lista de eventos del RegDeEventos
        if tipo in self.__TipoDeEventos:
            self.__RegDeEventos.Set_Events().append(Evento(tipo, ubicacion))

    def asistir_evento(self, evento, usuario):
        # Si el evento existe en la lista de eventos, se agrega a la lista de invitados el nuevo invitado.
        if evento in self.__RegDeEventos.View_Events():
            evento.Set_Attendance().append(usuario)

    def desinscribirse_evento(self, evento, usuario):
        # Si el evento esta en la lista y el usuario figura como invitado, se lo elimina de la lista de invitados.
        if evento in self.__RegDeEventos.View_Events() and usuario in evento.Set_Attendance():
            evento.Set_Attendance().remove(usuario)

