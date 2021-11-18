import os
import tkinter as tk
from tkinter import messagebox
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.UsersLib.CitizenClass import Ciudadano


class RegDeUsuarios:
    def __init__(self):
        self.__Admins = dict({})
        self.__Ciudadanos = dict({})
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_usuarios.txt'
        with open(path,'r') as f:
            for linea in f.readlines():
                if linea.split('/')[0] == 'Admin':
                    keyname = linea.split('/')[1]
                    name = linea.split('/')[2]
                    self.__Admins[keyname] = Administrator(name)

                elif linea.split('/')[0] == 'Ciudadano':
                    keyname = linea.split('/')[1]
                    name = linea.split('/')[2]
                    telCell = linea.split('/')[3]
                    cuil = linea.split('/')[4]
                    contactosDeInteres = list(linea.split('/')[5])
                    listaDeSolicitudes = list(linea.split('/')[6])
                    listaDeRechazos = list(linea.split('/')[7])
                    self.__Ciudadanos[keyname] = [Ciudadano(name, telCell, cuil), 0]
                    [self.__Ciudadanos[keyname][0].Mod_ContactosDeInteres(contacto, True) for contacto in contactosDeInteres]
                    [self.__Ciudadanos[keyname][0].Mod_ListaDeSolicitudes(ciudadano, True) for ciudadano in listaDeSolicitudes]
                    [self.__Ciudadanos[keyname][0].Mod_ListaDeRechazos(ciudadano, True) for ciudadano in listaDeRechazos]

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
        user_line = f'Admin/{keyname}/{admin.Get_Name()}/\n'
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_usuarios.txt'
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
        user_line = (f'Ciudadano/{keyname}/{ciudadano.Get_Name()}/{ciudadano.Get_Telefono()}/'
                        f'{ciudadano.Get_Cuil()}/{ciudadano.Get_ContactosDeInteres()}/'
                        f'{ciudadano.Get_ListaDeSolicitudes()}/{ciudadano.Get_ListaDeRechazos()}/\n')
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_usuarios.txt'
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

    def searchCitizen(self, telCell: int = None, cuil: int = None, name: str = None, returnKey: bool = False):
        if cuil == None and telCell == None and name == None:
            alert = tk.messagebox.showwarning(title="Falta de argumentos", text="Para buscar un ciudadano es necesario que introduzca al menos un argumento")
        ciudadanos = list(map(lambda x:x[0], list(self.__Ciudadanos.values())))
        keynames = list(self.__Ciudadanos.keys())
        zipCitizenWithHisKey = list(zip(ciudadanos, keynames))
        for ciudadano, keyname in zipCitizenWithHisKey:
            cuilAux = ciudadano.Get_Cuil() if cuil == None else cuil
            telCellAux = ciudadano.Get_Telefono() if telCell == None else telCell
            nameAux = ciudadano.Get_Name() if name == None else name
            if ciudadano.Get_Cuil() == cuilAux and ciudadano.Get_Telefono() == telCellAux and ciudadano.Get_Name() == nameAux:
                return ciudadano if not returnKey else keyname
