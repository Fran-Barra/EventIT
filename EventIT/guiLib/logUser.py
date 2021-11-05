import tkinter as tk



class LogUser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("350x400")
        self.wm_resizable(0,0)
        self.Create_Widgets()
        #self.regDeUsuarios = regdeusuarios

    def Create_Widgets(self):
        #creacion de widgets
        self.title = tk.Label(self, text="Log User")
        self.keyname = tk.Entry(self)
        self.logInBtn = tk.Button(self, text="Log in", command= LogUser.Log_in_User)
        



        #impresion de widgets
        centerW = 150

        self.title.grid(row=1, column= centerW)
        self.keyname.grid(row=2, column= centerW)
        self.keyname.insert(0, "Enter the key name")
        self.LogInBtn.grid(row=3, column= centerW)

    """def Log_in_User(self):
        keyName = self.keyname.get()
        if keyName in self.regDeUsuarios.Get_Ciudadanos():
            self.keyname = keyName
            self.Usuario = self.regDeUsuarios.Manage_Ciudadanos()[keyName]
        else:
            self.Mesage = tk.messagebox.showwarning(message="keyname couldt be found, try again or crate a profile",
            title= "keyname not found")
"""
