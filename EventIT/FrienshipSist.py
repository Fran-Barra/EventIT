class Frienship_Sistem:
    def __init__(self):
        self.personas_rechazadas = []

    def get_personas_rechazadas(self):
        return self.personas_rechazadas

    def EnviarSolicitud(self, CiudadanoSolicitante, CiudadanoDestinatario):
        if CiudadanoSolicitante not in CiudadanoDestinatario.Get_ListaDeSolicitudes():
            a = CiudadanoDestinatario.Mod_ListaDeSolicitudes()
            a.append(CiudadanoSolicitante)
        else:
            return "Ya le enviaste una solicitud a este usuario"

    def AceptarSolicitud(self, CiudadanoSolicitante, CiudadanoDestinatario):
        if CiudadanoSolicitante in CiudadanoDestinatario.Get_ListaDeSolicitudes():
            a = CiudadanoDestinatario.Mod_ContactosDeInteres()
            a.append(CiudadanoSolicitante)
            b = CiudadanoDestinatario.Mod_ListaDeSolicitudes()
            b.remove(CiudadanoSolicitante)
            c = CiudadanoSolicitante.Mod_ContactosDeInteres()
            c.append(CiudadanoDestinatario)
        else:
            return "No tienes solicitudes de este usuario"

    def RechazarSolicitud(self, CiudadanoSolicitante, CiudadanoDestinatario):
        if CiudadanoSolicitante in CiudadanoDestinatario.Get_ListaDeSolicitudes():
            self.personas_rechazadas.append(CiudadanoSolicitante)
            a = CiudadanoDestinatario.Mod_ListaDeSolicitudes()
            a.remove(CiudadanoSolicitante)
            (CiudadanoSolicitante.Mod_ListaDeRechazos()).append(CiudadanoDestinatario)
        else:
            return "No tienes solicitudes de este usuario"
