class UsuarioANSES:
    def __init__(self, name, telCell, cuil):
        self.__name = name
        self.__telCell = telCell
        self.__cuil = cuil

    def getName(self):
        return self.__name

    def getTelCell(self):
        return self.__telCell

    def getCuil(self):
        return self.__cuil


# usuarios_ANSES = open('usuarios_ANSES.txt', 'r')
# for linea in usuarios_ANSES.readlines():
#     usuario = linea
#     firstBar = usuario.index("/")
#     secondBar = usuario.index("/", firstBar + 1)
#     thirdBar = usuario.index("/", secondBar + 1)
#     lenOfName = usuario.index("/")
#     lenOfTelCell = usuario.index("/", firstBar + 1) - firstBar - 1
#     lenOfCuil = usuario.index("/", secondBar + 1) - secondBar - 1
#     nombre = usuario[: firstBar]
#     telCell = usuario[firstBar + 1 : secondBar]
#     cuil = usuario[secondBar + 1 : thirdBar]
#
#
# usuarios_ANSES.close()

