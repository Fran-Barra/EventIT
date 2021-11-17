import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano


class FrienshipW(tk.Tk):
    def __init__(self, reg_de_usuarios: RegDeUsuarios, user: Ciudadano):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("950x400")
        self.wm_resizable(1, 1)
        self.regdeusuarios = reg_de_usuarios
        self.user = user
        self.Create_Widgets()
        self.mainloop()

    def Create_Widgets(self):
        #Creacion de widgets
        self.data = tk.Entry(self)
        self.phone_btn = tk.Button(self, text= "send by phone", command = lambda: self.send_friendship())
        self.cuil_btn = tk.Button(self, text= "send by cuil", command = lambda: self.send_friendship())
        self.keyname_btn = tk.Button(self, text= "send by key name", command = lambda: self.send_friendship())
        self.seefriends_btn = tk.Button(self, text= "see list of friends", command = lambda: self.show_friends())


        #Impresion de widgets
        self.data.grid(row= 1, column= 0)
        self.data.insert(0, "phone/cuil/key name")
        self.phone_btn.grid(row= 2, column= 0)
        self.cuil_btn.grid(row= 2, column= 1)
        self.keyname_btn.grid(row= 2, column= 2)
        self.seefriends_btn.grid(row= 3, column=1)



        #CANVAS
        self.displayinfo = tk.Canvas(self, width=600, height=400, bg="white")
        self.displayinfo.grid(row=0, column= 3, rowspan = 20)

        self.vsb = tk.Scrollbar(self, orient= "vertical", command= self.displayinfo.yview())
        self.vsb.grid(row=0, column= 4, rowspan= 20, sticky= "ns")

        self.displayinfo.config(yscrollcommand = self.vsb.set)

        self.displayframe = tk.Frame(self.displayinfo, bg="white")
        self.displayinfo.create_window((10, 0), window= self.displayframe, anchor="nw")

    def show_requests(self):
        pass

    def show_friends(self):
        for friend in self.user.Get_ContactosDeInteres():
            tk.Label(self.displayframe, text = f"user name: {friend.Get_Name()} user phone: {friend.Get_Telefono()}"
                                             f" user cuil {friend.Get_Cuil()}").pack()

    def acept_friend(self):
        pass

    def send_friendship(self):
        pass



if __name__ == "__main__":
    user1 = Ciudadano("jorge", 1, 1)
    user2 = Ciudadano("Emilio", 2, 2)

    user1.Mod_ContactosDeInteres().append(user2)

    regdeususarios = RegDeUsuarios()

    FrienshipW(regdeususarios, user1)
