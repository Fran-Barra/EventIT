from EventIT.DatasetANSES.UsuarioANSES import UsuarioANSES
from EventIT.MapsSist.UbicacionClass import Ubicacion


class DatasetANSES:
    def __init__(self):
        self.__usuariosANSES = []
        self.makeListOfUsers()

    def makeListOfUsers(self):
        with open(r"C:\Users\lucky\PycharmProjects\EventIT\EventIT\DatasetANSES\usuarios_ANSES.txt", "r") as usuarios_ANSES:
            # usuarios_ANSES = open('usuarios_ANSES.txt', 'r')
            for linea in usuarios_ANSES.readlines():
                name = linea.split('/')[0]
                telCell = linea.split('/')[1]
                cuil = linea.split('/')[2]
                ubicacionString = linea.split('/')[3]
                latitud = int(ubicacionString.split(',')[0])
                longitud = int(ubicacionString.split(',')[1])
                ubicacion = Ubicacion(latitud, longitud)
                user = UsuarioANSES(name, telCell, cuil, ubicacion)
                if user not in self.__usuariosANSES:
                    self.__usuariosANSES.append(user)
            usuarios_ANSES.close()

    def getListOfUsuariosANSES(self):
        return self.__usuariosANSES

    def searchUser(self, telCell, cuil):
        for usuario in self.__usuariosANSES:
            if usuario.getCuil() == cuil and usuario.getTelCell() == telCell:
                return usuario
