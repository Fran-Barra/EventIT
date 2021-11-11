from EventIT.ExeptionLib.UnexpectedValueClass import UnexpectedValue
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from tkinter import messagebox


class CreateProfile:
    @classmethod
    def Create_Profile(cls, type: str, name: str, telefono: str, cuil: str, regdeusuarios: RegDeUsuarios, datasetAnses: DatasetANSES):
        #Maneja el tipo de usuario que sera creado y llama al metodo correspondiente para dicho usuario.
        #En caso de que se ingrese un type distinto al esperado se eleva un UnexpectedValue y maneja el error 
        #avisando que algo salio mal
            try:
                if type == "admin":
                    CreateProfile.Create_Profile_Admin(name, regdeusuarios)
                elif type == "user":
                    CreateProfile.Create_Profile_Citizen(name, name, telefono, cuil, regdeusuarios, datasetAnses)
                else:
                    raise UnexpectedValue
            except UnexpectedValue:
                pass

    @classmethod
    def Create_Profile_Admin(cls, name, regdeusuarios: RegDeUsuarios):
        #Chequea que no exista un admin con ese nombre
        if name not in regdeusuarios.Get_Admins():
            #Crea el admin y lo añade al registro de usuarios
            regdeusuarios.Manage_Admins()[name] = Administrator(name)
        else:
            pass #Manejar nombre ya existente


    @classmethod
    def Create_Profile_Citizen(cls, Keyname, name, telefono, cuil, regdeusuario: RegDeUsuarios, datasetAnses):
            if CreateProfile.ValidarUsuario(cuil, telefono, datasetAnses):
                #Chequea que no existan usuarios con ese nombre clave
                if Keyname not in regdeusuario.Get_Ciudadanos():
                    #crea al usuario y lo añade al regdeusuarios
                    regdeusuario.Manage_Ciudadanos()[Keyname] = (Ciudadano(name, telefono, cuil), 0)
                else:
                    pass #Manejar nombre ya existente
            else:
                #Manejar que los datos no existen
                alert = messagebox.showwarning(title= "Data not found", message = "The data couldn be foun in ANSES")

    @classmethod
    def ValidarUsuario(cls, cuil, telefono, datasetANSES: DatasetANSES):
        for usuario in datasetANSES.getListOfUsuariosANSES():
            if usuario.getCuil() == cuil and usuario.getTelCell() == telefono:
                return True
        return False



