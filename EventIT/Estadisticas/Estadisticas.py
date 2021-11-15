from EventIT.MapsSist.MapClass import Map
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos


class Estadisticas:
    def __init__(self, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos):
        self.lista_de_zonas = map.getListaDeZonas()
        self.lista_de_ciudadanos = datasetANSES.getListOfUsuariosANSES()
        self.lista_de_eventos = regDeEventos.View_Events()
        self.datasetANSES =datasetANSES

    def calculate_number_of_attendees_per_zone_per_event(self):
        """Calcula la cantidad de asistentes que asistieron a un evento y que viven en la misma zona donde se realizo el evento"""
        cantidad_de_asistentes_x_zona_x_evento = dict({})
        for evento in self.lista_de_eventos:
            cantidad_de_asistentes_x_zona_x_evento[evento] = 0
        for evento in self.lista_de_eventos:
            for asistente in evento.getListaDeAsistencia():
                if evento.getZona(self.lista_de_zonas) == self.datasetANSES.searchUser(asistente.Get_Telefono(), asistente.Get_Cuil()).getZona(self.lista_de_zonas): #compara la zona del evento con la zona del asistente obtenida en el datasetANSES
                    cantidad_de_asistentes_x_zona_x_evento[evento] += 1
        return cantidad_de_asistentes_x_zona_x_evento

    def calculate_total_number_of_attendees(self):
        cantidad_de_asistentes_totales_x_evento = dict({})
        for evento in self.lista_de_eventos:
            cantidad_de_asistentes_totales_x_evento[evento] = len(evento.getListaDeAsistencia())
        return cantidad_de_asistentes_totales_x_evento

    def calculate_percentage_of_atendees_of_the_zone(self):
        porcentaje_de_asistentes_de_la_zona_por_evento =dict({})
        for evento in self.lista_de_eventos:
            if self.calculate_total_number_of_attendees()[evento] != 0:
                porcentaje_de_asistentes_de_la_zona_por_evento[evento] = round((self.calculate_number_of_attendees_per_zone_per_event()[evento]/self.calculate_total_number_of_attendees()[evento]) * 100, 1)
            else:
                porcentaje_de_asistentes_de_la_zona_por_evento[evento] = 0.0
        return porcentaje_de_asistentes_de_la_zona_por_evento

    def calculate_positions_of_the_ranking(self, mayor_cantidad_de_asistentes_de_la_zona: bool = False, mayor_cantidad_de_asistentes: bool = False, mayor_porcentaje: bool = False):
        """Calcula el ranking de eventos en orden descendente segun el parametro que elija"""
        ranking = self.lista_de_eventos.copy()
        if mayor_cantidad_de_asistentes_de_la_zona or not (mayor_cantidad_de_asistentes_de_la_zona and mayor_cantidad_de_asistentes and mayor_porcentaje):
            ranking.sort(key=lambda x:self.calculate_number_of_attendees_per_zone_per_event()[x], reverse=True)# Ordena la lista de eventos poniendo en primer lugar al evento con mas asistentes de la zona
            # self.calculate_number_of_attendees_per_zone_per_event()
            return ranking
        elif mayor_cantidad_de_asistentes:
            ranking.sort(key=lambda x:self.calculate_total_number_of_attendees()[x], reverse=True)# Ordena la lista de eventos poniendo en primer lugar al evento con mas asistentes de la zona
            return ranking
        elif mayor_porcentaje:
            ranking.sort(key=lambda x:self.calculate_percentage_of_atendees_of_the_zone()[x], reverse=True)# Ordena la lista de eventos poniendo en primer lugar al evento con mas asistentes de la zona
            return ranking
