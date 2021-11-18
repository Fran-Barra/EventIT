from tkinter import messagebox
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios


class Frienship_System:

    @staticmethod
    def EnviarSolicitud(regdeusuarios: RegDeUsuarios, CuilSolicitante= None, CuilDestinatario=None,
                        CelSolicitante=None, CelDestinatario= None):
        try:
            CiudadanoSolicitante = regdeusuarios.searchCitizen(CelSolicitante,CuilSolicitante,None)
            CiudadanoDestinatario = regdeusuarios.searchCitizen(CelDestinatario,CuilDestinatario,None)
            if CiudadanoSolicitante not in CiudadanoDestinatario.Get_ListaDeSolicitudes():
                CiudadanoDestinatario.Mod_ListaDeSolicitudes().append(CiudadanoSolicitante)
            else:
                messagebox.showwarning(title= "already send", message= "you already sent a request to this user")
        except AttributeError:
            messagebox.showwarning(title="user not found", message="The user couldnt be found")


    @staticmethod
    def AceptarSolicitud(regdeusuarios: RegDeUsuarios, CuilSolicitante= None, CuilDestinatario= None,
                         CelSolicitante= None, CelDestinatario= None):
        try:
            CiudadanoSolicitante =  regdeusuarios.searchCitizen(CelSolicitante,CuilSolicitante,None)
            CiudadanoDestinatario = regdeusuarios.searchCitizen(CelDestinatario,CuilDestinatario,None)
            if CiudadanoSolicitante in CiudadanoDestinatario.Get_ListaDeSolicitudes():
                CiudadanoDestinatario.Mod_ContactosDeInteres().append(CiudadanoSolicitante)
                CiudadanoDestinatario.Mod_ListaDeSolicitudes().remove(CiudadanoSolicitante)
                CiudadanoSolicitante.Mod_ContactosDeInteres().append(CiudadanoDestinatario)
            else:
                messagebox.showwarning(title= "no requests", message= "there is no a request from this user")
        except AttributeError:
            messagebox.showwarning(title="user not found", message="The user couldnt be found")


    @staticmethod
    def RechazarSolicitud(regdeusuarios: RegDeUsuarios, CuilSolicitante= None, CuilDestinatario= None,
                          CelSolicitante= None, CelDestinatario= None):
        try:
            CiudadanoSolicitante = regdeusuarios.searchCitizen(CelSolicitante,CuilSolicitante,None)
            CiudadanoDestinatario = regdeusuarios.searchCitizen(CelDestinatario,CuilDestinatario,None)
            if CiudadanoSolicitante in CiudadanoDestinatario.Get_ListaDeSolicitudes():
                CiudadanoDestinatario.Mod_ListaDeSolicitudes().remove(CiudadanoSolicitante)
                CiudadanoSolicitante.Mod_ListaDeRechazos().append(CiudadanoDestinatario)

            else:
                messagebox.showwarning(title= "no requests", message= "there is no a request from this user")
        except AttributeError:
            messagebox.showwarning(title="user not found", message="The user couldnt be found")


