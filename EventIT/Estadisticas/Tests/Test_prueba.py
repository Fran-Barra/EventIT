import unittest
from EventIT.MapsSist.MapClass import Map
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventoClass import Evento
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.Estadisticas.prueba import Estadisticas


class TestPrueba(unittest.TestCase):
    def test_create_the_assistance_list_with_ANSES_users(self):
        u1 = Ubicacion(0, 0)
        u2 = Ubicacion(10, 10)
        u3 = Ubicacion(20, 20)
        ListaUbic = [u1, u2, u3]
        Zona1 = Zona(ListaUbic, 1, 'Zona1')
        u4 = Ubicacion(30, 30)
        u5 = Ubicacion(40, 40)
        u6 = Ubicacion(50, 50)
        Zona2 = Zona([u4, u5, u6], 2, 'Zona2')
        mapa1 = Map([Zona1, Zona2])

        datasetANSES = DatasetANSES()
        regDeEventos = RegDeEventos()

        evento1 = Evento(None, Ubicacion(10, 10), 'evento1')
        evento2 = Evento(None, Ubicacion(30, 30), 'evento2')
        regDeEventos.Set_Events().append(evento1)
        regDeEventos.Set_Events().append(evento2)
        self.assertEqual(regDeEventos.View_Events(), [evento1, evento2])

        juan = Ciudadano('Juan.Perez', 1150042603, 43807968)
        jose = Ciudadano('Jose.Hernandez', 1133280846, 23224040)

        evento1.Set_Attendance(juan, True)
        evento1.Set_Attendance(jose, True)
        self.assertEqual(evento1.getListaDeAsistencia(), [juan, jose]) # Test de Evento.Set_Attendance()

        estadisticas = Estadisticas(mapa1, datasetANSES, regDeEventos)
        result = estadisticas.haha()
        self.assertEqual(result[evento1], 2)

