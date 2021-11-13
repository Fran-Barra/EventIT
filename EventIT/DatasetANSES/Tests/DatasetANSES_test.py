import unittest
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES

class TestDatasetANSES(unittest.TestCase):
    def test_make_the_list_of_users(self):
        datasetANSES = DatasetANSES()
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[0].getName(), 'Juan.Perez')
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[1].getName(), 'Jose.Hernandez')
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[0].getTelCell(), 1150042603)
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[1].getTelCell(), 1133280846)
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[1].getCuil(), 23224040)
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[1].getUbicacion().Get_Coordinates(), (20, 20))


if __name__ == '__main__':
    unittest.main()
