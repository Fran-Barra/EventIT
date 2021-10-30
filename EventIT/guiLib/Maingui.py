import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.Create_Widgets()

    
    def Create_Widgets(self):

        #Creacion de widgets
        self.name = tk.Label(self, text="EventIT")
        self.citizendLogBot = tk.Button(self, text="Log as citizend" """, command = logInUser.pack""")#command para llamar metodo
        self.adminLogBot = tk.Button(self, text="Log as admin")
        self.sensorLogBot = tk.Button(self, text="sensor")

        #Impresion de widgets
        centerW = 150

        self.name.grid(row=1, column= centerW)
        self.citizendLogBot.grid(row= 2, column= centerW)
        self.adminLogBot.grid(row= 3, column= centerW)
        self.sensorLogBot.grid(row= 4,column= centerW)

    


from logUser import LogUser


root = tk.Tk()
root.wm_title("EventIT")
root.wm_geometry("350x400")
root.wm_resizable(0,0)

#mainMenu
application = App(root)

#logUser
logInUser = LogUser(root)


application.mainloop()

""" @staticmethod
    def Star_Main_Window():
        mainWindow.geometry("350x400")
        title = tk.Label(mainWindow, text="EventIT")

        #no permite cambiar el tamaño de la ventana
        mainWindow.resizable(0,0)

        


        mainWindow.mainloop()




    @staticmethod
    def Log_Citizend_Window(mainWindow):
        mainWindow.withdraw()
        log_C = tk.Tk()

        keynameinput = tk.Entry()
        keynameinput.pack()
        keyname = keynameinput.get()


        log_C.mainloop()


    @staticmethod
    def Log_Admin_Window(mainWindow):
        mainWindow.withdraw()
        log_A = tk.Tk()


        log_A.mainloop()

    
    @staticmethod
    def Log_Sensor_Window(mainWindow):
        mainWindow.withdraw()
        log_S = tk.Tk()



        log_S.mainloop()







Windows.Star_Main_Window()"""