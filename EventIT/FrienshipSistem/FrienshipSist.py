class Frienship_Sistem:
    def __init__(self):
        self.personas_rechazadas = []

    def get_personas_rechazadas(self):
        return self.personas_rechazadas

    def EnviarSolicitud(self, ciudadanoSolicitante, ciudadanoDestinatario):
        try:
            if len(ciudadanoSolicitante.Get_ListaDeRechazos()) < 5:
                if ciudadanoSolicitante not in ciudadanoDestinatario.Get_ListaDeSolicitudes():
                    a = ciudadanoDestinatario.Mod_ListaDeSolicitudes()
                    a.append(ciudadanoSolicitante)
                else:
                    return "Ya le enviaste una solicitud a este usuario"
        except:
            return "Tu usuario fue bloqueado por el sistema"

    def AceptarSolicitud(self, ciudadanoSolicitante, ciudadanoDestinatario):
        try:
            if len(ciudadanoDestinatario.Get_ListaDeRechazos()) < 5:
                if ciudadanoSolicitante in ciudadanoDestinatario.Get_ListaDeSolicitudes():
                    ciudadanoDestinatario.Mod_ContactosDeInteres().append(ciudadanoSolicitante)
                    ciudadanoDestinatario.Mod_ListaDeSolicitudes().remove(ciudadanoSolicitante)
                    ciudadanoSolicitante.Mod_ContactosDeInteres().append(ciudadanoDestinatario)
                else:
                    return "No tienes solicitudes de este usuario"
        except:
            return "Tu usuario fue bloqueado por el sistema"

    def RechazarSolicitud(self, ciudadanoSolicitante, ciudadanoDestinatario):
        if ciudadanoSolicitante in ciudadanoDestinatario.Get_ListaDeSolicitudes():
            self.personas_rechazadas.append(ciudadanoSolicitante)
            a = ciudadanoDestinatario.Mod_ListaDeSolicitudes()
            a.remove(ciudadanoSolicitante)
            (ciudadanoSolicitante.Mod_ListaDeRechazos()).append(ciudadanoDestinatario)

        else:
            return "No tienes solicitudes de este usuario"
