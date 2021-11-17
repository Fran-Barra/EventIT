import tkinter as tk
from tkinter import messagebox
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.UsersLib.CitizenClass import Ciudadano

class RegDeUsuarios:
    def __init__(self):
        self.__Admins = dict({})
        self.__Ciudadanos = dict({})
        with open(r'C:\Users\lucky\PycharmProjects\EventIT\EventIT\UsersLib\registro_de_usuarios.txt','w') as f:
            f.write(f'Lista de usuarios registrados: \n')
            f.close()

    def Get_Admins(self):
        return self.__Admins.copy()

    def Get_Ciudadanos(self):
        return self.__Ciudadanos.copy()

    # def Manage_Admins(self):
    #     return self.__Admins

    def Manage_Admins(self, admin: Administrator, add: bool, keyname):
        """Permite agregar o eliminar un admin del dicccionario de administradores.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo"""
        user_line = f'Keyname: {keyname}/Name: {admin.Get_Name()}\n'
        path = r'C:\Users\lucky\PycharmProjects\EventIT\EventIT\UsersLib\registro_de_usuarios.txt'
        if add:
            self.__Admins[keyname] = admin
            with open(path,'a') as f: # agregar texto sin sobreescribir
                f.write(user_line)
                f.close()
        else:
            try:
                del self.__Admins[keyname]
                with open(path,'r') as f: # codigo para borrar usuarios
                    lineas = f.readlines()
                    with open(path,'w') as f:
                        f.write('')
                        f.close()
                    for linea in lineas:
                        if linea != user_line:
                            with open(path,'a') as f:
                                f.write(linea)
                                f.close()
                    f.close()
            except KeyError:
                alert = tk.messagebox.showwarning(title="Error en el Keyname", text="El keyname que ingreso no pertenece a ningún administrador.")

    # def Manage_Ciudadanos(self):
    #     return self.__Ciudadanos

    def Manage_Ciudadanos(self, ciudadano: Ciudadano, add: bool, keyname): #Raro el tema del bloqueo
        """Permite agregar o eliminar un ciudadano del dicccionario de ciudadanos.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo"""
        user_line = (f'Keyname: {keyname}/Name: {ciudadano.Get_Name()}/Telefono Celular: {ciudadano.Get_Telefono()}/'
                        f'Cuil: {ciudadano.Get_Cuil()}/Contactos: {ciudadano.Get_ContactosDeInteres()}/'
                        f'Lista de solicitudes: {ciudadano.Get_ListaDeSolicitudes()}/Lista de rechazos: {ciudadano.Get_ListaDeRechazos()}\n')
        path = r'C:\Users\lucky\PycharmProjects\EventIT\EventIT\UsersLib\registro_de_usuarios.txt'
        if add:
            self.__Ciudadanos[keyname] = [ciudadano, 0]
            with open(path,'a') as f: # agregar texto sin sobreescribir
                f.write(user_line)
                f.close()
        else:
            del self.__Ciudadanos[keyname]
            with open(path,'r') as f: # codigo para borrar usuarios
                lineas = f.readlines()
                with open(path,'w') as f:
                    f.write('')
                    f.close()
                for linea in lineas:
                    if linea != user_line:
                        with open(path,'a') as f:
                            f.write(linea)
                            f.close()
                f.close()



    def estado_de_bloqueo(self, bloquear: bool, keyname):
        self.__Ciudadanos[keyname][1] = bloquear

    def searchCitizen(self, telCell: int = None, cuil: int = None, name: str = None):
        if cuil == None and telCell == None and name == None:
            alert = tk.messagebox.showwarning(title="Falta de argumentos", text="Para buscar un ciudadano es necesario que introduzca al menos un argumento")
        for ciudadano in list(map(lambda x:x[0], list(self.__Ciudadanos.values()))):
            cuilAux = ciudadano.Get_Cuil() if cuil == None else cuil
            telCellAux = ciudadano.Get_Telefono() if telCell == None else telCell
            nameAux = ciudadano.Get_Name() if name == None else name
            if ciudadano.Get_Cuil() == cuilAux and ciudadano.Get_Telefono() == telCellAux and ciudadano.Get_Name() == nameAux:
                return ciudadano
