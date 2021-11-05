# import unittest
from EventIT.MapsSist.MapClass import Map
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos


# class TestEstadisticas(unittest.TestCase):
#     def test_estadisticas(self):
a = Ubicacion(0,0)
b = Ubicacion(10,10)
c = Ubicacion(20,20)
ListaUbic = [a,b,c]
Zona1 = Zona(ListaUbic,1)
d = Ubicacion(30,30)
e = Ubicacion(40,40)
f = Ubicacion(50,50)
Zona2 = Zona([d,e,f],2)
mapa1 = Map([Zona1,Zona2])

datasetANSES = DatasetANSES()
regDeEventos = RegDeEventos()
regDeEventos.Set_Events().append('hola')
print(regDeEventos.View_Events())

 # : Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos
