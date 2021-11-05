from EventIT.MapsSist.MapClass import Map
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos

class Estadisticas:
    def __init__(self, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos):
        self.lista_de_zonas = map.getListaDeZonas()
        self.lista_de_ciudadanos = datasetANSES.getListOfUsuariosANSES()
        self.lista_de_eventos = regDeEventos.View_Events()

    def __repr__(self):
        return 'Estadisticas'

    def calculateRanking(self):
        """Este metodo calcula un ranking de los eventos que impactan a mas personas. Retorna un diccionario donde las keys son los eventos y los values su impacto"""
        cantidad_de_personas_por_zona = dict({})
        for zona in self.lista_de_zonas: # Agrega las zonas al dict
            cantidad_de_personas_por_zona[zona] = 0
        for ciudadano in self.lista_de_ciudadanos: # Agrega la cantidad de ciudadanos que hay en cada zona
            cantidad_de_personas_por_zona[ciudadano.getZona(self.lista_de_zonas)] += 1

        # Cambiar ZONA por el metodo que devuelva la zona del evento
        self.lista_de_eventos.sort(key=lambda x:cantidad_de_personas_por_zona[x.getZona(self.lista_de_zonas)], reverse=True) # Ordena la lista de eventos por zona, en orden desscendente de la cantidad de personas por zona
        impacto_x_evento = dict({}) # diccionario donde las keys son las zonas y los values la cantidad de personas
        for evento in self.lista_de_eventos:
            impacto_x_evento[evento] = cantidad_de_personas_por_zona[evento.getZona(self.lista_de_zonas)]
        return impacto_x_evento

    def printedRanking(self):
        """Este metodo imprime en consola un ranking de los eventos que impactan a mas personas."""
        impacto_x_evento = self.calculateRanking()
        eventos = list(impacto_x_evento.keys())
        impactos = list(impacto_x_evento.values())
        index = list(range(1,len(eventos) + 1))
        listOfImpactoXEvento = list(zip(eventos, impactos, index)) # arma una lista de tuplas, y en cada tupla esta el evento y su impacto
        rankingString = f"|\tPosicion\t|\tNombre del evento\t|\tZona\t|\tCantidad de personas\t|\n"
        for evento, impacto, index in listOfImpactoXEvento: # arma el ranking en formato string para imprmirlo
            rankingString += f"|\t\t{index}\t\t|\t\t{evento}\t\t\t|\t{evento.getZona(self.lista_de_zonas).nombre}\t|\t\t\t{impacto}\t\t\t\t|\n"


            # f"|\tPosicion\t|\tNombre del evento\t|\tZona\t|\tCantidad de personas\t|\n"
            # f"|\t\t1\t\t|\t\t{eventos[0]}\t\t\t|\t{eventos[0].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[0]}\t\t\t\t|\n"
            # f"|\t\t2\t\t|\t\t{eventos[1]}\t\t\t|\t{eventos[1].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[1]}\t\t\t\t|\n"
            # f"|\t\t3\t\t|\t\t{eventos[2]}\t\t\t|\t{eventos[2].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[2]}\t\t\t\t|\n"
            # f"|\t\t4\t\t|\t\t{eventos[3]}\t\t\t|\t{eventos[3].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[3]}\t\t\t\t|\n"
            # f"|\t\t5\t\t|\t\t{eventos[4]}\t\t\t|\t{eventos[4].getZona(self.lista_de_zonas)}\t|\t\t\t{impacto[4]}\t\t\t\t|\n"

        return rankingString
