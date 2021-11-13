from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.guiLib.Maingui import App


if __name__ == "__main__":
    regdeusuarios = RegDeUsuarios()
    dataAnses= DatasetANSES()
    regdeusuarios.Manage_Ciudadanos(Ciudadano("ADMIN", 1,1),True,"ADMIN")
    regdeusuarios.Manage_Admins(Administrator("ADMIN"), True,"ADMIN")

    #mainMenu
    application = App(regdeusuarios, dataAnses)


    application.mainloop()
