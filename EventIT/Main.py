from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventManager import EventManger
from EventIT.EventLib.EventoClass import Evento
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.sensorLib.sensor import Sensor
from EventIT.sensorLib.RegDeSensores import RegDeSensores
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.MapsSist.MapClass import Map

regDeUsuarios = RegDeUsuarios()
datasetANSES = DatasetANSES()
regDeEventos = RegDeEventos()
eventManager = EventManger(regDeEventos)
regDeSensores = RegDeSensores()



def crear_ubicaciones():
    ParaZona1 = []
    ParaZona2 = []
    ParaZona3 = []
    ParaZona4 = []
    x_origen = 0
    x = 0
    y = 0
    cantidad_en_fila = 0
    cantidad_en_y = 0
    while cantidad_en_y <= 20:
        while cantidad_en_fila <= 20:
            if x <= 10 and y <= 10:
                ParaZona1.append(Ubicacion(x, y))
            elif 10< x <= 20 and y <= 10:
                ParaZona2.append(Ubicacion(x,y))
            elif x <= 10 and 10 < y <= 20:
                ParaZona3.append(Ubicacion(x, y))
            else:
                ParaZona4.append(Ubicacion(x,y))

            x += 1
            cantidad_en_fila += 1
        cantidad_en_fila = 0
        cantidad_en_y += 1
        x = x_origen
        y += 1

    return [ParaZona1, ParaZona2, ParaZona3, ParaZona4]

listadeubicaciones = crear_ubicaciones()
Zona1 = Zona(listadeubicaciones[0], 1, "Zona 1")
Zona2 = Zona(listadeubicaciones[1], 2, "Zona 2")
Zona3 = Zona(listadeubicaciones[2], 3, "Zona 3")
Zona4 = Zona(listadeubicaciones[3], 4, "Zona 4")
Mapa = Map([Zona1, Zona2, Zona3, Zona4])


sensor1 = Sensor(Mapa.search_ubicacion(0,0), 'Fiesta', 'sensor1')
sensor2 = Sensor(Mapa.search_ubicacion(0,11), 'Sanitario', 'sensor2')
sensor3 = Sensor(Mapa.search_ubicacion(11,0), 'Social', 'sensor3')
sensor4 = Sensor(Mapa.search_ubicacion(11,11), 'Privado', 'sensor4')

eventManager.alta_tiposDeEvento('Fiesta', regDeUsuarios.Get_Admins()['Juan'])
eventManager.alta_tiposDeEvento('Sanitario', regDeUsuarios.Get_Admins()['Juan'])
eventManager.alta_tiposDeEvento('Social', regDeUsuarios.Get_Admins()['Juan'])
eventManager.alta_tiposDeEvento('Privado', regDeUsuarios.Get_Admins()['Juan'])

evento1 = Evento('Fiesta', Mapa.search_ubicacion(0,0), 'Evento1')
evento2 = Evento('Sanitario', Mapa.search_ubicacion(0,0), 'Evento2')
evento3 = Evento('Social', Mapa.search_ubicacion(0,0), 'Evento3')
evento4 = Evento('Privado', Mapa.search_ubicacion(0,0), 'Evento4')

