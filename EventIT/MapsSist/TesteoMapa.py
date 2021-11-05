import unittest
from ZonaClass import Zona
from UbicacionClass import Ubicacion
# from MapClass import Map

class TestMapa(unittest.TestCase):
    def test_ubic(self):
        lugar = Ubicacion(60,100)
        lugar1 = Ubicacion(50,200)
        self.assertEqual(lugar.Get_Coordinates(),(60, 100))
        self.assertEqual(lugar1.Get_Coordinates(),(50, 200))

        lugar.__Latitud = 500
        lugar.__Longitud = 1000

        self.assertEqual(lugar.Get_Coordinates(),(60, 100))
        #No se modifica la latitud ni altitud

    def test_zona(self):
        a = Ubicacion(0,0)
        b = Ubicacion(10,10)
        c = Ubicacion(20,20)
        ListaUbic = [a,b,c]
        Zona1 = Zona(ListaUbic,1, 'zona1')

        self.assertEqual(Zona1.Get_Ubicaciones(),[a,b,c])
        self.assertEqual(Zona1.Get_Ubicaciones(),ListaUbic)
        self.assertEqual(Zona1.Get_NumeroDeZona(),1)

        Zona1.__NumeroDeZona = 2

        self.assertEqual(Zona1.Get_NumeroDeZona(),1)
        #El numero de zona no se puede cambiar

    def test_todo(self):
        a = Ubicacion(0,0)
        b = Ubicacion(10,10)
        c = Ubicacion(20,20)
        ListaUbic = [a,b,c]
        Zona1 = Zona(ListaUbic,1, 'zona1')
        d = Ubicacion(30,30)
        e = Ubicacion(40,40)
        f = Ubicacion(50,50)
        Zona2 = Zona([d,e,f],2, 'zona2')
        ListZonas = [Zona1,Zona2]

        self.assertEqual(ListZonas[0].Get_Ubicaciones(),[a,b,c])
        self.assertEqual(ListZonas[1].Get_Ubicaciones(),[d,e,f])


if __name__ == '__main__':
    unittest.main()
