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

    # def getListOfUsuariosANSES(self):
    #     return self.__usuariosANSES

    def validarUsuario(self, user):
        cuil = user.getCuil() # chequeear que la clase usuarios tenga este metodo
        telCell = user.getTelCell()
        value = False
        for usuario in self.__usuariosANSES:
            if usuario.getCuil() == cuil and usuario.getTelCell() == telCell:
                value = True
        return value























    # def agregarUsuario(self, usuario):
    #     self.__usuariosANSES.append(usuario)
    #
    # def eliminarUsuario(self, telCel, cuil):
    #     i = 0
    #     while i < len(self.__usuariosANSES):
    #         if self.__usuariosANSES[i].getTelCel() == telCel and self.__usuariosANSES[i].getCuil() == cuil:
    #             del self.__usuariosANSES[i]
    #         i += 1




usuarios_ANSES = open('usuarios_ANSES.txt', 'r')
# print(usuarios_ANSES.read(7))
# print(usuarios_ANSES.read(3))
for linea in usuarios_ANSES.readlines(): # Lo unico que quedo mal es que el seek va siempre a la posicion 0, por lo que en la segunda iteracion empiezan a darse errores
    usuario = linea
    firstBar = usuario.index("/")
    secondBar = usuario.index("/", firstBar + 1)
    thirdBar = usuario.index("/", secondBar + 1)
    lenOfName = usuario.index("/")
    lenOfTelCell = usuario.index("/", firstBar + 1) - firstBar - 1
    lenOfCuil = usuario.index("/", secondBar + 1) - secondBar - 1

    # print(firstBar)
    # print(secondBar)
    # print(thirdBar)
    # print(usuario)
    # usuarios_ANSES.seek(0)
    # nombre = usuarios_ANSES.read(lenOfName)
    # usuarios_ANSES.seek(firstBar + 1)
    # telCell = usuarios_ANSES.read(lenOfTelCell)
    # usuarios_ANSES.seek(secondBar + 1)
    # cuil = usuarios_ANSES.read(lenOfCuil)

    nombre = usuario[: firstBar]
    telCell = usuario[firstBar + 1 : secondBar]
    cuil = usuario[secondBar + 1 : thirdBar]

    # print()
    # print(nombre)
    # print(telCell)
    # print(cuil)
    # print()



# for linea in usuarios_ANSES:
#     cantidad = len(linea)
#     print(linea, cantidad)
usuarios_ANSES.close()

