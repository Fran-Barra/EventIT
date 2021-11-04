from EventIT.DatasetANSES.UsuarioANSES import UsuarioANSES
from EventIT.MapsSist.UbicacionClass import Ubicacion

class DatasetANSES:
    def __init__(self):
        self.__usuariosANSES = []
        self.makeListOfUsers()

    def addUser(self, user):
        if user not in self.__usuariosANSES:
            self.__usuariosANSES.append(user)

    def makeListOfUsers(self):
        usuarios_ANSES = open('usuarios_ANSES.txt', 'r')
        for linea in usuarios_ANSES.readlines():
            name = linea.split('/')[0]
            telCell = linea.split('/')[1]
            cuil = linea.split('/')[2]
            ubicacionString = linea.split('/')[3]
            latitud = ubicacionString.split(',')[0]
            longitud = ubicacionString.split(',')[1]
            ubicacion = Ubicacion(latitud, longitud)
            self.addUser(UsuarioANSES(name, telCell, cuil, ubicacion))

        usuarios_ANSES.close()

    def getListOfUsuariosANSES(self):
        return self.__usuariosANSES

a = DatasetANSES()
print(a.getListOfUsuariosANSES())
