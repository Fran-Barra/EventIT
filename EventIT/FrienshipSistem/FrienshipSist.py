class Frienship_System:
    def __init__(self, RegDeUsuarios):
        self.__RegDeUsuarios = RegDeUsuarios


    def EnviarSolicitud(self, CuilSolicitante, CuilDestinatario, CelSolicitante, CelDestinatario):
        CiudadanoSolicitante = self.__RegDeUsuarios.searchCitizen(CelSolicitante,CuilSolicitante,None)
        CiudadanoDestinatario = self.__RegDeUsuarios.searchCitizen(CelDestinatario,CuilDestinatario,None)
        if CiudadanoSolicitante not in CiudadanoDestinatario.Get_ListaDeSolicitudes():
            a = CiudadanoDestinatario.Mod_ListaDeSolicitudes()
            a.append(CiudadanoSolicitante)
        else:
            return "Ya le enviaste una solicitud a este usuario"

    def AceptarSolicitud(self, CuilSolicitante, CuilDestinatario, CelSolicitante, CelDestinatario):
        CiudadanoSolicitante = self.__RegDeUsuarios.searchCitizen(CelSolicitante,CuilSolicitante,None)
        CiudadanoDestinatario = self.__RegDeUsuarios.searchCitizen(CelDestinatario,CuilDestinatario,None)
        if CiudadanoSolicitante in CiudadanoDestinatario.Get_ListaDeSolicitudes():
            a = CiudadanoDestinatario.Mod_ContactosDeInteres()
            a.append(CiudadanoSolicitante)
            b = CiudadanoDestinatario.Mod_ListaDeSolicitudes()
            b.remove(CiudadanoSolicitante)
            c = CiudadanoSolicitante.Mod_ContactosDeInteres()
            c.append(CiudadanoDestinatario)
        else:
            return "No tienes solicitudes de este usuario"


    def RechazarSolicitud(self, CuilSolicitante, CuilDestinatario, CelSolicitante, CelDestinatario):
        CiudadanoSolicitante = self.__RegDeUsuarios.searchCitizen(CelSolicitante,CuilSolicitante,None)
        CiudadanoDestinatario = self.__RegDeUsuarios.searchCitizen(CelDestinatario,CuilDestinatario,None)
        if CiudadanoSolicitante in CiudadanoDestinatario.Get_ListaDeSolicitudes():
            a = CiudadanoDestinatario.Mod_ListaDeSolicitudes()
            a.remove(CiudadanoSolicitante)
            (CiudadanoSolicitante.Mod_ListaDeRechazos()).append(CiudadanoDestinatario)

        else:
            return "No tienes solicitudes de este usuario"
