from EventIT.MapsSist.MapClass import Map
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos


class Estadisticas:
    def __init__(self, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos):
        self.lista_de_zonas = map.getListaDeZonas()
        self.lista_de_ciudadanos = datasetANSES.getListOfUsuariosANSES()
        self.lista_de_eventos = regDeEventos.View_Events()
        self.datasetANSES =datasetANSES

    # def calculateRanking(self):
    #     listasDeAsistenciaXEvento = dict({})
    #     for evento in self.lista_de_eventos:
    #         listasDeAsistenciaXEvento[evento] = evento.getListaDeAsistencia()
    #     for evento, asistentes in list(zip(listasDeAsistenciaXEvento.keys(), listasDeAsistenciaXEvento.values())):
    #         for asistente in asistentes:
    #             listasDeAsistenciaXEvento[evento] = list(map(lambda x:self.datasetANSES.searchUser(asistente.Get_Telefono, asistente.Get_Cuil), asistentes))
    #     return list(listasDeAsistenciaXEvento.values())

# en cada evento obtengo la lista de asistentes, la recorro y comparo la zona del evento con la zona del asistente, si son iguales incremento
# el total de asistentes de la zona del evento

    def calcularCantidadDeAsistentesXZonaXEvento(self):
        """Calcula la cantidad de asistentes que asistieron a un evento y que viven en la misma zona donde se realizo el evento"""
        cantidad_de_asistentes_x_zona_x_evento = dict({})
        for evento in self.lista_de_eventos:
            cantidad_de_asistentes_x_zona_x_evento[evento] = 0
        for evento in self.lista_de_eventos:
            for asistente in evento.getListaDeAsistencia():
                if evento.getZona(self.lista_de_zonas) == self.datasetANSES.searchUser(asistente.Get_Telefono(), asistente.Get_Cuil()).getZona(self.lista_de_zonas): #compara la zona del evento con la zona del asistente obtenida en el datasetANSES
                    cantidad_de_asistentes_x_zona_x_evento[evento] += 1
        return cantidad_de_asistentes_x_zona_x_evento



        # cantidad_de_asistentes_x_evento = dict({}) #cantidad de personas que asisten a un evento
        # for evento in self.lista_de_eventos:
        #     cantidad_de_asistentes_x_evento[evento] = len(evento.getListaDeAsistencia())
        #
        # cantidad_de_asistentes_x_evento_x_zona = dict({}) #cantidad de personas que asisten a un evento
        # for evento in self.lista_de_eventos:
        #     cantidad_de_asistentes_x_evento_x_zona[evento] = 0
        #
        #
        #
        #
        # cantidad_de_personas_por_zona = dict({})
        # for zona in self.lista_de_zonas: # Agrega las zonas al dict
        #     cantidad_de_personas_por_zona[zona] = 0
        # for ciudadano in self.lista_de_ciudadanos: # Agrega la cantidad de ciudadanos que hay en cada zona
        #     cantidad_de_personas_por_zona[ciudadano.getZona(self.lista_de_zonas)] += 1
        #
        # # Cambiar ZONA por el metodo que devuelva la zona del evento
        # self.lista_de_eventos.sort(key=lambda x:cantidad_de_personas_por_zona[x.getZona(self.lista_de_zonas)], reverse=True) # Ordena la lista de eventos por zona, en orden desscendente de la cantidad de personas por zona
        # impacto_x_evento = dict({}) # diccionario donde las keys son las zonas y los values la cantidad de personas
        # for evento in self.lista_de_eventos:
        #     impacto_x_evento[evento] = cantidad_de_personas_por_zona[evento.getZona(self.lista_de_zonas)]
        # return impacto_x_evento

    # aca tengo un diccionario que me dice en el evento, el maximo de personas de la zona que podria haber ido. Solo me falta restar las personas que no fueron
