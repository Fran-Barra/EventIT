from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.guiLib.Maingui import App


if __name__ == "__main__":
    regdeusuarios = RegDeUsuarios()
    dataAnses= DatasetANSES()
    regdeusuarios.Manage_Ciudadanos()["ADMIN"] = (Ciudadano("ADMIN", 1,1), 0)

    #mainMenu
    application = App(regdeusuarios, dataAnses)


    application.mainloop()
