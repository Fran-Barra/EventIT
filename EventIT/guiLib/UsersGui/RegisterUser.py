import tkinter as tk
from tkinter import messagebox
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UserManagementLib.CreateProfileClass import CreateProfile
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.guiLib.UsersGui.menuusers import  MenuUsers


class RegisterNewUserW(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, data_anses: DatasetANSES):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("350x400")
        self.wm_resizable(0, 0)
        self.data_anses = data_anses
        self.regDeUsuarios = regdeusuarios
        self.Create_Widgets()


    def Create_Widgets(self):
        # creacion de widgents
        self.title = tk.Label(self, text="Create new profile")
        self.key_name = tk.Entry(self)
        self.phone = tk.Entry(self)
        self.cuil = tk.Entry(self)
        self.register_btn = tk.Button(self, text=" Register", command= self.register_new_profile)



        # imprecion de widgets
        self.title.grid(row= 0, column=5)
        self.key_name.grid(row= 1, column= 0)
        self.key_name.insert(0, "Enter a key name")
        self.phone.grid(row=2, column= 0)
        self.phone.insert(1, "Enter a phone")
        self.cuil.grid(row=3, column=0)
        self.cuil.insert(2, "enter a cuil")
        self.register_btn.grid(row=4, column=0)

    def register_new_profile(self):
        key_name = self.key_name.get()
        phone = self.phone.get()
        cuil = self.cuil.get()
        if (self.regDeUsuarios.searchCitizen(int(phone)) != None) or (self.regDeUsuarios.searchCitizen(cuil= int(cuil)) != None):
            messagebox.showwarning(title= "Existing account", message= "An acount with this data already exist")
        else:
            if CreateProfile.Create_Profile("user", key_name, phone, cuil, self.regDeUsuarios, self.data_anses):
                self.user = self.regDeUsuarios.Get_Ciudadanos()[key_name]
                self.Open_window(MenuUsers)



    def Open_window(self, window):
        if window == MenuUsers:
            MenuUsers(self.regDeUsuarios, self.data_anses, self.user)
        self.withdraw()
