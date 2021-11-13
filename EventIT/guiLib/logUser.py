import tkinter as tk
from tkinter import messagebox
from EventIT.guiLib.UsersGui.RegisterUser import RegisterNewUserW
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.guiLib.UsersGui.menuusers import MenuUsersr


class LogUser(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, data_anses: DatasetANSES):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("350x400")
        self.wm_resizable(0,0)
        self.data_anses = data_anses
        self.regDeUsuarios = regdeusuarios
        self.Create_Widgets()



    def Create_Widgets(self):
        #creacion de widgets
        self.title = tk.Label(self, text="Log User")
        self.keyname = tk.Entry(self)
        self.logIn_btn = tk.Button(self, text="Log in", command= self.Log_in_User)
        self.regist_btn = tk.Button(self, text= "Register new user", command = lambda: self.Open_Window(RegisterNewUserW))




        #impresion de widgets
        centerW = 150

        self.title.grid(row=1, column= centerW)
        self.keyname.grid(row=2, column= centerW)
        self.keyname.insert(0, "Enter the key name")
        self.logIn_btn.grid(row=3, column= centerW)
        self.regist_btn.grid(row=4, column= centerW)

    def Log_in_User(self):
        keyName = self.keyname.get()
        if keyName in self.regDeUsuarios.Get_Ciudadanos():
            estado_de_cuenta = self.regDeUsuarios.Get_Ciudadanos()[keyName][1]
            if estado_de_cuenta == 0:
                #cuenta desbloqueada
                self.keyname = keyName
                self.user = self.regDeUsuarios.Get_Ciudadanos()[keyName]
                self.Open_Window(MenuUsersr)
            elif estado_de_cuenta == 1:
                #cuenta bloqueada
                self.mesage_estado = tk.messagebox.showwarning(message="your acount is block, try other day.",
                                                               title= "account block")
        else:
            self.Mesage = tk.messagebox.showwarning(message="keyname couldt be found, try again or crate a profile",
            title= "keyname not found")


    def Open_Window(self, window):
        if window ==  RegisterNewUserW:
            RegisterNewUserW(self.regDeUsuarios, self.data_anses)
        if window == MenuUsersr:
            MenuUsersr(self.regDeUsuarios, self.data_anses, self.user)
        self.withdraw()

