from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.ExeptionLib.UnexpectedValueClass import UnexpectedValue


class ABM():

    @classmethod
    def dar_alta(cls, type: str, name: str, tel: str, cuil: str, reg_de_usuarios: RegDeUsuarios):
        try:
            if type == "user":
                reg_de_usuarios.Manage_Ciudadanos(Ciudadano(name, tel, cuil), True, name)
            else:
                raise UnexpectedValue
        except:
            pass

    @classmethod
    def dar_baja(cls, name: str, tel: str, cuil: str, reg_de_usuarios: RegDeUsuarios):
        reg_de_usuarios.Manage_Ciudadanos(Ciudadano(name, tel, cuil), False, name)

    @classmethod
    def modificar_tel(cls, telefono, ciudadano: Ciudadano):
        ciudadano.Mod_Telefono(telefono)

    @classmethod
    def modificar_name(cls, name, ciudadano: Ciudadano):
        ciudadano.Mod_Name(name)

    @classmethod
    def modificar_cuil(cls, cuil, ciudadano: Ciudadano):
        ciudadano.Mod_CUIL(cuil)

    @classmethod
    def agregar_admin(cls, name: str, reg_de_usuarios: RegDeUsuarios, admin: Administrator):
        if name not in list(map(lambda x:x.Get_Name(), reg_de_usuarios.Get_Admins())):
            reg_de_usuarios.Manage_Admins(admin, True, name)

    @classmethod
    def bloquear_desbloquear(cls, bloq: bool, reg_de_usuarios: RegDeUsuarios, ciudadano: Ciudadano):
        if bloq:
            reg_de_usuarios.Manage_Ciudadanos(ciudadano, True, 1) # Bloqueado
        else:
            reg_de_usuarios.Manage_Ciudadanos(ciudadano, False, 0) # Desbloqueado
