import matplotlib.pyplot as plt
import matplotlib.patches as patches
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.MapsSist.MapClass import Map
from math import sqrt

class Graficar_Mapa:
    @classmethod
    def graficar(cls, map: Map, regdeeventos: RegDeEventos):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        Graficar_Mapa.position_events(ax, regdeeventos)
        Graficar_Mapa.map_of_zones(ax,(0,0), 10, 10, "red", int(sqrt(len(map.getListaDeZonas()))))

    @classmethod
    def position_events(cls, figura, regdeeventos: RegDeEventos):
        coordenada_x = []
        coordenada_y = []
        Eventos = regdeeventos.View_Events()
        for evento in Eventos:
            ubica_evento = evento.getUbicacion()
            y, x = ubica_evento.Get_Coordinates()
            coordenada_x.append(x)
            coordenada_y.append(y)
        figura.scatter(x= coordenada_x, y= coordenada_y)
        #return [coordenada_x, coordenada_y]




    @classmethod
    def add_zone(cls, figura, punto_origen, ancho, alto, color):
        figura.add_patch(
            patches.Rectangle(
            xy=punto_origen,
            width=ancho,
            height=alto,
            linewidth= 1,
            color= color,
            fill=False)
            )

    @classmethod
    def map_of_zones(cls, figura, punto_origen: tuple, ancho: int, alto: int, color: str, cuadrado_de: int):
        """cuadrado de indica la dimension del cuadrado, ejempo si recibe el valor 2 creara un cuadrado de 2x2, (4 zonas)."""
        cantidad_actual = 0
        cantidad_en_fila = 0
        origen = punto_origen
        x_de_origen, y_de_origen = punto_origen
        cantidad_total = cuadrado_de**2

        while cantidad_actual<cantidad_total:
            while cantidad_en_fila < cuadrado_de:
                Graficar_Mapa.add_zone(figura, origen, ancho, alto, color)
                x, y = origen
                x+= ancho
                origen = (x,y)
                cantidad_en_fila += 1
                cantidad_actual += 1


            cantidad_en_fila = 0
            x, y = origen
            origen = (x_de_origen, y+alto)


        plt.show()












