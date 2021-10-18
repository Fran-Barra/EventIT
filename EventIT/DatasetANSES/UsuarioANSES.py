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
