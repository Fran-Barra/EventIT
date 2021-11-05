from EventIT.MapsSist.MapClass import Map
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos

class Estadisticas:
    def __init__(self, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos):
        self.lista_de_zonas = map.getListaDeZonas()
        self.lista_de_ciudadanos = datasetANSES.getListOfUsuariosANSES()
        self.lista_de_eventos = regDeEventos.View_Events()

    def calculateRanking(self):
        """Este metodo calcula un ranking de los eventos que impactan a mas personas. Retorna un diccionario donde las keys son los eventos y los values su impacto"""
        cantidad_de_personas_por_zona = dict({})
        for zona in self.lista_de_zonas:
            cantidad_de_personas_por_zona[zona] = 0
        for ciudadano in self.lista_de_ciudadanos:
            cantidad_de_personas_por_zona[ciudadano.getZona(self.lista_de_zonas)] += 1

        # Cambiar ZONA por el metodo que devuelva la zona del evento
        self.lista_de_eventos.sort(key=lambda x:cantidad_de_personas_por_zona[x.getZona(self.lista_de_zonas)], reverse=True)
        impacto_del_evento = dict({})
        for evento in self.lista_de_eventos:
            impacto_del_evento[evento] = cantidad_de_personas_por_zona[evento.getZona(self.lista_de_zonas)]
        return impacto_del_evento

    def printedRanking(self):
        """Este metodo imprime en consola un ranking de los eventos que impactan a mas personas."""
        eventos = list(self.calculateRanking().keys())
        impacto = list(self.calculateRanking().values())
        print(
            f"|\tPosicion\t|\tNombre del evento\t|\tZona\t|\tCantidad de personas\t|\n"
            f"|\t\t1\t\t|\t\t{eventos[0]}\t\t\t|\t{eventos[0].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[0]}\t\t\t\t|\n"
            f"|\t\t2\t\t|\t\t{eventos[1]}\t\t\t|\t{eventos[1].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[1]}\t\t\t\t|\n"
            f"|\t\t3\t\t|\t\t{eventos[2]}\t\t\t|\t{eventos[2].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[2]}\t\t\t\t|\n"
            f"|\t\t4\t\t|\t\t{eventos[3]}\t\t\t|\t{eventos[3].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[3]}\t\t\t\t|\n"
            f"|\t\t5\t\t|\t\t{eventos[4]}\t\t\t|\t{eventos[4].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[4]}\t\t\t\t|\n"
        )
