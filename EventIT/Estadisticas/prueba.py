from EventIT.MapsSist.MapClass import Map
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos

class Estadisticas:
    def __init__(self, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos):
        self.lista_de_zonas = map.getListaDeZonas()
        self.lista_de_ciudadanos = datasetANSES.getListOfUsuariosANSES()
        self.lista_de_eventos = regDeEventos.View_Events()

    def calculatedRanking(self, lista_de_eventos):
        for evento in self.lista_de_eventos:
            evento.getListaDeAsistencia()
