from RegDeUsuarios import RegDeUsuarios
from CitizenClass import Ciudadano
from AdminClass import Administrator

class ABM():

    @classmethod
    def dar_alta(cls, name: str, reg_de_usuarios: RegDeUsuarios):
        pass


    @classmethod
    def dar_baja(cls, name:str, reg_de_usuarios: RegDeUsuarios):
        del reg_de_usuarios.Manage_Ciudadanos()[name]


    @classmethod

    def modificar(cls, name: str, telefono: str, cuil: str,  modificacion_de_usuarios: Ciudadano):

        modificacion_de_usuarios.Mod_Name(name)
        modificacion_de_usuarios.Mod_Telefono(telefono)
        modificacion_de_usuarios.Mod_CUIL(cuil)

    @classmethod
    def agregar_admin(cls, name: str, reg_de_usuarios: RegDeUsuarios):
        if name not in reg_de_usuarios.Get_Admins():
            reg_de_usuarios.Manage_Admins()[name] = Administrator(name)
            # Acá agrega al usuario_admin en el diccionario y lo pone como administrador en la clase administrador

    @classmethod
    def bloquear(cls):
        pass

    @classmethod
    def desbloquear(cls):
        pass
