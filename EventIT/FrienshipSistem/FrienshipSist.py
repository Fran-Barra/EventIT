from tkinter import messagebox
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios

class Frienship_System:

    @staticmethod
    def EnviarSolicitud(regdeusuarios: RegDeUsuarios, CuilSolicitante= None, CuilDestinatario=None,
                        CelSolicitante=None, CelDestinatario= None, NameSolicitante= None, NameDestinatario= None):
        try:
            CiudadanoSolicitante = regdeusuarios.searchCitizen(CelSolicitante,CuilSolicitante,NameSolicitante)
            CiudadanoDestinatario = regdeusuarios.searchCitizen(CelDestinatario,CuilDestinatario,NameDestinatario)
            if len(CiudadanoSolicitante.Get_ListaDeRechazos()) < 5:
                if CiudadanoSolicitante not in CiudadanoDestinatario.Get_ListaDeSolicitudes():
                    CiudadanoDestinatario.Mod_ListaDeSolicitudes().append(CiudadanoSolicitante)
                else:
                    messagebox.showwarning(title= "Already sent", message= "You already sent a request to this user")
            else:
                messagebox.showwarning(title= "User banned", message= "Your user was banned from the system")
        except AttributeError:
            messagebox.showwarning(title="User not found", message="The user couldn't be found")
        except KeyError:
            messagebox.showwarning(title='Invalid Name', message="There are no users with this name")


    @staticmethod
    def AceptarSolicitud(regdeusuarios: RegDeUsuarios, CuilSolicitante= None, CuilDestinatario= None,
                         CelSolicitante= None, CelDestinatario= None, NameSolicitante= None, NameDestinatario= None):
        try:
            CiudadanoSolicitante = regdeusuarios.searchCitizen(CelSolicitante,CuilSolicitante,NameSolicitante)
            CiudadanoDestinatario = regdeusuarios.searchCitizen(CelDestinatario,CuilDestinatario,NameDestinatario)
            if len(CiudadanoSolicitante.Get_ListaDeRechazos()) < 5:
                if CiudadanoSolicitante in CiudadanoDestinatario.Get_ListaDeSolicitudes():
                    CiudadanoDestinatario.Mod_ContactosDeInteres().append(CiudadanoSolicitante)
                    CiudadanoDestinatario.Mod_ListaDeSolicitudes().remove(CiudadanoSolicitante)
                    CiudadanoSolicitante.Mod_ContactosDeInteres().append(CiudadanoDestinatario)
                else:
                    messagebox.showwarning(title= "No requests", message= "You do not have requests from this user")
            else:
                messagebox.showwarning(title= "User banned", message= "Your user was banned from the system")
        except AttributeError:
            messagebox.showwarning(title="User not found", message="The user couldn't be found")
        except KeyError:
            messagebox.showwarning(title='Invalid Name', message="There are no users with this name")


    @staticmethod
    def RechazarSolicitud(regdeusuarios: RegDeUsuarios, CuilSolicitante= None, CuilDestinatario= None,
                          CelSolicitante= None, CelDestinatario= None, NameSolicitante= None, NameDestinatario= None):
        try:
            CiudadanoSolicitante = regdeusuarios.searchCitizen(CelSolicitante,CuilSolicitante,NameSolicitante)
            CiudadanoDestinatario = regdeusuarios.searchCitizen(CelDestinatario,CuilDestinatario,NameDestinatario)
            if CiudadanoSolicitante in CiudadanoDestinatario.Get_ListaDeSolicitudes():
                CiudadanoDestinatario.Mod_ListaDeSolicitudes().remove(CiudadanoSolicitante)
                CiudadanoSolicitante.Mod_ListaDeRechazos().append(CiudadanoDestinatario)

            else:
                messagebox.showwarning(title= "No requests", message= "You do not have requests from this user")
        except AttributeError:
            messagebox.showwarning(title="User not found", message="The user couldn't be found")
        except KeyError:
            messagebox.showwarning(title='Invalid Name', message="There are no users with this name")

