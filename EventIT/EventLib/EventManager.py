from AdminClass import Administrator

class EventManger:
    def __init__(self):
        self.TiposDeEvento = []

    def altaEvento(self, TipoDeEvento, User):
        if User.isinstance(Administrator):
            return f"El administrador {User} dio de alta {TipoDeEvento}"
    def ReportEvent(self, invitados, caracteristicas):
        pass

    def AsistirEvento(self,Evento, invitados):
        pass
    
    def DesinscribirseEvento(self,Evento):
        pass

