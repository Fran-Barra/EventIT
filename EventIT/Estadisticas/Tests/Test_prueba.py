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
    def setUp(self):
        self.u1 = Ubicacion(0, 0)
        self.u2 = Ubicacion(10, 10)
        self.u3 = Ubicacion(20, 20)
        self.ListaUbic = [self.u1, self.u2, self.u3]
        self.Zona1 = Zona(self.ListaUbic, 1, 'Zona1')
        self.u4 = Ubicacion(30, 30)
        self.u5 = Ubicacion(40, 40)
        self.u6 = Ubicacion(50, 50)
        self.Zona2 = Zona([self.u4, self.u5, self.u6], 2, 'Zona2')
        self.mapa1 = Map([self.Zona1, self.Zona2])

        self.datasetANSES = DatasetANSES()
        self.regDeEventos = RegDeEventos()

        self.evento1 = Evento(None, Ubicacion(10, 10), 'evento1')
        self.evento2 = Evento(None, Ubicacion(30, 30), 'evento2')
        self.regDeEventos.Set_Events().append(self.evento1)
        self.regDeEventos.Set_Events().append(self.evento2)

        self.juan = Ciudadano('Juan.Perez', 1150042603, 43807968)
        self.jose = Ciudadano('Jose.Hernandez', 1133280846, 23224040)

        self.evento1.Set_Attendance(self.juan, True)
        self.evento1.Set_Attendance(self.jose, True)

        self.estadisticas = Estadisticas(self.mapa1, self.datasetANSES, self.regDeEventos)

    # def test_create_the_attendees_list_with_ANSES_users(self):

    def test_add_events(self):
        self.assertEqual(self.regDeEventos.View_Events(), [self.evento1, self.evento2])

    def test_set_attendance(self):
        self.assertEqual(self.evento1.getListaDeAsistencia(), [self.juan, self.jose]) # Test de Evento.Set_Attendance()

    def test_calculate_number_of_attendees_per_zone_per_event(self):
        self.assertEqual(self.estadisticas.calculate_number_of_attendees_per_zone_per_event()[self.evento1], 2)

    def test_calculate_total_number_of_attendees(self):
        self.assertEqual(self.estadisticas.calculate_total_number_of_attendees()[self.evento1], 2)

    def test_calculate_percentage_of_atendees_of_the_zone(self):
        self.assertEqual(self.estadisticas.calculate_percentage_of_atendees_of_the_zone()[self.evento1], 100)

