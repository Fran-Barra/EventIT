import unittest
from EventIT.MapsSist.MapClass import Map
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventoClass import Evento
from EventIT.Estadisticas.Estadisticas import Estadisticas


class TestEstadisticas(unittest.TestCase):
    def test_estadisticas(self):
        a = Ubicacion(0,0)
        b = Ubicacion(10,10)
        c = Ubicacion(20,20)
        ListaUbic = [a,b,c]
        Zona1 = Zona(ListaUbic,1, 'zona1')
        d = Ubicacion(30,30)
        e = Ubicacion(40,40)
        f = Ubicacion(50,50)
        Zona2 = Zona([d,e,f],2, 'zona2')
        mapa1 = Map([Zona1,Zona2])

        datasetANSES = DatasetANSES()
        regDeEventos = RegDeEventos()

        evento1 = Evento(None, Ubicacion(10, 10), 'evento1')
        evento2 = Evento(None, Ubicacion(20, 20), 'evento2')
        regDeEventos.Set_Events().append(evento1)
        regDeEventos.Set_Events().append(evento2)
        self.assertEqual(regDeEventos.View_Events(), [evento1, evento2])

        estadisticas = Estadisticas(mapa1, datasetANSES, regDeEventos)
        estadisticas.printedRanking()


