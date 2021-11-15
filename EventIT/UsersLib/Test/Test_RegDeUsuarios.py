import unittest
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios


class TestRegDeUsuarios(unittest.TestCase):
    def setUp(self):
        self.regDeUsuarios = RegDeUsuarios()
        self.admin1 = Administrator('juan')
        self.admin2 = Administrator('jose')
        self.admin3 = Administrator('pepe')
        self.ciudadano1 = Ciudadano('lucas', 123456, 789101112)
        self.ciudadano2 = Ciudadano('joaquin', 654321, 121110987)
        self.ciudadano3 = Ciudadano('santiago', 147852, 963258741)

        self.regDeUsuarios.Manage_Admins(self.admin1, True, 'Juan')
        self.regDeUsuarios.Manage_Admins(self.admin2, True, 'Jose')

        self.regDeUsuarios.Manage_Ciudadanos(self.ciudadano1, True, 'Lucas')
        self.regDeUsuarios.Manage_Ciudadanos(self.ciudadano2, True, 'Joaquin')

        self.result1 = self.regDeUsuarios.searchCitizen(cuil=121110987)
        self.result2 = self.regDeUsuarios.searchCitizen(telCell=123456)

        self.result3 = self.regDeUsuarios.searchCitizen(name='lucas')
        self.result4 = self.regDeUsuarios.searchCitizen(name='pepe')

    def test_Manage_Admins(self):
        self.regDeUsuarios.Manage_Admins(self.admin3, True, 'Pepe')
        self.assertEqual(len(self.regDeUsuarios.Get_Admins()), 3)
        self.regDeUsuarios.Manage_Admins(self.admin3, False, 'Pepe')
        self.assertEqual(len(self.regDeUsuarios.Get_Admins()), 2)


    def test_Manage_Ciudadanos(self):
        pass

    def test_searchCitizen(self):
        self.assertEqual(self.result1, self.ciudadano2)
        self.assertEqual(self.result2, self.ciudadano1)
        self.assertEqual(self.result3, self.ciudadano1)
        self.assertEqual(self.result4, None)

