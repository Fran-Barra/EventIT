from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.guiLib.Maingui import App



regdeusuarios = RegDeUsuarios()
dataAnses= DatasetANSES()


#mainMenu
application = App(regdeusuarios, dataAnses)


application.mainloop()
