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

        estadisticas = Estadisticas(mapa1, datasetANSES, regDeEventos)
        result = estadisticas.printedRanking()
        expected = (
            f"|\tPosicion\t|\tNombre del evento\t|\tZona\t|\tCantidad de personas\t|\n"
            f"|\t\t1\t\t|\t\tevento1\t\t\t|\tZona1\t|\t\t\t2\t\t\t\t|\n"
            f"|\t\t2\t\t|\t\tevento2\t\t\t|\tZona2\t|\t\t\t0\t\t\t\t|\n"
            # f"|\t\t3\t\t|\t\t{eventos[2]}\t\t\t|\t{eventos[2].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[2]}\t\t\t\t|\n"
            # f"|\t\t4\t\t|\t\t{eventos[3]}\t\t\t|\t{eventos[3].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[3]}\t\t\t\t|\n"
            # f"|\t\t5\t\t|\t\t{eventos[4]}\t\t\t|\t{eventos[4].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[4]}\t\t\t\t|\n"
        )
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
