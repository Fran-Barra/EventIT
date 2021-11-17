import unittest
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.FriendshipSistem.FrienshiSist import Frienship_System
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios



class MyTestCase(unittest.TestCase):
    def test_enviar_solicitud(self):
        Juan = Ciudadano("juan",111,123)
        tom = Ciudadano("TOM",000,999)
        RegUsr = RegDeUsuarios()
        RegUsr.Manage_Ciudadanos(Juan,True,'JUAN')
        RegUsr.Manage_Ciudadanos(tom,True,"tom")
        self.assertEqual(RegUsr.Get_Ciudadanos(),{'JUAN': [Juan, 0], 'tom': [tom, 0]})
        Friendship = Frienship_System(RegUsr)
        Friendship.EnviarSolicitud(123,999,111,000)
        self.assertEqual(tom.Get_ListaDeSolicitudes(),[Juan])


    def test_aceptar_y_rechazar(self):
        RegUsr =RegDeUsuarios()
        Marco = Ciudadano("Marcp",100,987)
        Luis = Ciudadano('Luis',200,000)
        Julio = Ciudadano("Julio",300,111)
        RegUsr.Manage_Ciudadanos(Marco,True,"Marco")
        RegUsr.Manage_Ciudadanos(Luis,True,"Luis")
        RegUsr.Manage_Ciudadanos(Julio,True,"Julio")
        sist = Frienship_System(RegUsr)
        sist.EnviarSolicitud(987,111,100,300)
        sist.EnviarSolicitud(987,000,100,200)
        sist.AceptarSolicitud(987,111,100,300)
        sist.RechazarSolicitud(987,000,100,200)
        self.assertEqual(Julio.Get_ContactosDeInteres(),[Marco])
        self.assertEqual(Marco.Get_ContactosDeInteres(),[Julio])
        self.assertEqual(Marco.Get_ListaDeRechazos(),[Luis])
        self.assertEqual(Luis.Get_ListaDeSolicitudes(),[])
        self.assertEqual(Luis.Get_ContactosDeInteres(),[])




if __name__ == '__main__':
    unittest.main()
