class ExceptionRechazo (Exception):

    def __init__(self, usuario, regDeUsuario):
        self.__usuario = usuario
        self.__regDeUsuario = regDeUsuario

    def bloquear(self):
        self.__regDeUsuario.Manage_Ciudadanos()[usuario] = 1
