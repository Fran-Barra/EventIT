from TP.UsuarioANSES import UsuarioANSES

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
            self.addUser(UsuarioANSES(name, telCell, cuil))

        usuarios_ANSES.close()

    def getListOfUsuariosANSES(self):
        return self.__usuariosANSES

    def validarUsuario(self, user):
        cuil = user.Get_Cuil()
        telCell = user.Get_Telefono()
        for usuario in self.__usuariosANSES:
            if usuario.getCuil() == cuil and usuario.getTelCell() == telCell:
                return True
        return False
