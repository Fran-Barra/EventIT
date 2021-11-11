import unittest
from EventIT.UsersLip.CitizenClass import Ciudadano
from EventIT.FriendshipSistem.FrienshiSist import Frienship_Sistem



class MyTestCase(unittest.TestCase):
    def test_enviar_solicitud(self):
        Juan = Ciudadano("juan",555,123)
        sist = Frienship_Sistem()
        tom = Ciudadano("TOM",000,999)
        sist.EnviarSolicitud(Juan,tom)
        self.assertEqual(tom.Get_ListaDeSolicitudes(),[Juan])


    def test_aceptar_y_rechazar(self):
        Marco = Ciudadano("Marcp",000,987)
        Luis = Ciudadano('Luis',000,000)
        Julio = Ciudadano("Julio",000,111)
        sist = Frienship_Sistem()
        sist.EnviarSolicitud(Marco,Julio)
        sist.EnviarSolicitud(Marco,Luis)
        sist.AceptarSolicitud(Marco,Julio)
        self.assertEqual(Julio.Get_ListaDeSolicitudes(),[])
        self.assertEqual(Julio.Get_ContactosDeInteres(),[Marco])
        sist.RechazarSolicitud(Marco,Luis)
        self.assertEqual(sist.get_personas_rechazadas(),[Marco])

    def test_bloqueo(self):
        usr1 = Ciudadano("1",000,111)
        usr2 = Ciudadano("2",000,111)
        usr3 = Ciudadano("3",000,111)
        usr4 = Ciudadano("4",000,111)
        usr5 = Ciudadano("5",000,111)
        usr6 = Ciudadano("6",000,111)
        sist = Frienship_Sistem()
        sist.EnviarSolicitud(usr1,usr2)
        sist.EnviarSolicitud(usr1,usr3)
        sist.EnviarSolicitud(usr1,usr4)
        sist.EnviarSolicitud(usr1,usr5)
        sist.EnviarSolicitud(usr1,usr6)
        sist.RechazarSolicitud(usr1,usr2)
        sist.RechazarSolicitud(usr1,usr3)
        sist.RechazarSolicitud(usr1,usr4)
        sist.RechazarSolicitud(usr1,usr5)
        sist.RechazarSolicitud(usr1,usr6)
        self.assertEqual(len(usr1.Get_ListaDeRechazos()),5)
        sist.EnviarSolicitud(usr1,usr2)
        self.assertEqual(usr2.Get_ListaDeSolicitudes(),[])





if __name__ == '__main__':
    unittest.main()
