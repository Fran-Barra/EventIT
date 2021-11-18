import unittest
from EventIT.MapsSist.MapClass import Map
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventoClass import Evento
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.Estadisticas.Estadisticas import Estadisticas


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
        self.regDeEventos.Set_Events(self.evento1, True)
        self.regDeEventos.Set_Events(self.evento2, True)

        self.juan = Ciudadano('Juan.Perez', 1150042603, 43807968)
        self.jose = Ciudadano('Jose.Hernandez', 1133280846, 23224040)

        self.evento1.Set_Attendance(self.juan, True)
        self.evento1.Set_Attendance(self.jose, True)

        # self.estadisticas = Estadisticas(self.mapa1, self.datasetANSES, self.regDeEventos)

        self.rankingString = f"|\tPosicion\t|\tNombre del evento\t|\tZona\t|\tCantidad de personas por zona\t|\tCantidad de personas totales\t|\tPorcentaje de asistentes de la zona\t|\n"
        for index, evento in enumerate(Estadisticas.calculate_positions_of_the_ranking(self.mapa1, self.datasetANSES, self.regDeEventos)): # arma el ranking en formato string para imprmirlo
            self.rankingString += f"|\t\t{index}\t\t|\t\t{evento}\t\t\t|\t{evento.getZona(self.mapa1.getListaDeZonas())}\t|" \
                                  f"\t\t\t\t{Estadisticas.calculate_number_of_attendees_per_zone_per_event(self.mapa1, self.datasetANSES, self.regDeEventos)[evento]}\t\t\t\t\t|" \
                                  f"\t\t\t\t{Estadisticas.calculate_total_number_of_attendees(self.mapa1, self.datasetANSES, self.regDeEventos)[evento]}\t\t\t\t\t|" \
                                  f"\t\t\t\t{Estadisticas.calculate_percentage_of_atendees_of_the_zone(self.mapa1, self.datasetANSES, self.regDeEventos)[evento]}\t\t\t\t\t|\n"
        # print(self.rankingString)
    # def test_create_the_attendees_list_with_ANSES_users(self):

    def test_add_events(self):
        self.assertEqual(self.regDeEventos.View_Events(), [self.evento1, self.evento2])

    def test_set_attendance_inscribirse(self):
        self.assertEqual(self.evento1.getListaDeAsistencia(), [self.juan, self.jose])

    def test_set_attendance_desinscribirse(self):
        self.evento1.Set_Attendance(self.jose, False)
        self.assertEqual(self.evento1.getListaDeAsistencia(), [self.juan])

    def test_calculate_number_of_attendees_per_zone_per_event(self):
        self.assertEqual(Estadisticas.calculate_number_of_attendees_per_zone_per_event(self.mapa1, self.datasetANSES, self.regDeEventos)[self.evento1], 2)

    def test_calculate_total_number_of_attendees(self):
        self.assertEqual(Estadisticas.calculate_total_number_of_attendees(self.mapa1, self.datasetANSES, self.regDeEventos)[self.evento1], 2)

    def test_calculate_percentage_of_atendees_of_the_zone(self):
        self.assertEqual(Estadisticas.calculate_percentage_of_atendees_of_the_zone(self.mapa1, self.datasetANSES, self.regDeEventos)[self.evento1], 100)

    def test_calculate_positions_of_the_ranking(self):
        self.assertEqual(Estadisticas.calculate_positions_of_the_ranking(self.mapa1, self.datasetANSES, self.regDeEventos), [self.evento1, self.evento2])
        self.assertEqual(Estadisticas.calculate_positions_of_the_ranking(map=self.mapa1, datasetANSES=self.datasetANSES, regDeEventos=self.regDeEventos, mayor_porcentaje=True), [self.evento1, self.evento2])

if __name__ == '__main__':
    unittest.main()
