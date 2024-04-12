import json


import os
try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione enter para continuar")
limpiar();
print(F'''{Fore.WHITE+ Style.BRIGHT + Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║    ╔═══════╗            ╦                                                   ║
║    ║                    ║                                                   ║
║    ║                    ║                                                   ║
║    ║                    ║                                                   ║
║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗                         ║
║    ║            ║       ║    ║       ║    ║                                 ║
║    ║            ║       ║    ║       ║    ║          ╔╗                     ║
║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝                     ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║              ╦     ╔═════╗     ╔═══╦═══╗   ╔═══════╗     ╔═════╗            ║
║              ║    ╔╝     ╚╗        ║       ║            ╔╝     ╚╗           ║
║              ║    ║                ║       ║            ║       ║           ║
║              ║    ╚╗               ║       ║            ║       ║           ║
║              ║     ╚═════╗         ║       ╠══════╣     ╠═══════╣           ║
║              ║           ╚╗        ║       ║            ║       ║           ║
║              ║    ╚╗     ╔╝        ║       ║            ║       ║           ║
║              ╩     ╚═════╝         ╩       ╚═══════╝    ╩       ╩           ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║                                                                             ║
║                               __________        __                          ║
║                              /                  /                           ║
║                             /                  /                            ║
║                            /                  /                             ║
║                           /____              /                              ║
║                          /                  /                               ║
║                         /                  /                                ║
║                        /                  /                                 ║
║                      _/_                _/_                                 ║
║                                                                             ║
║                                                                             ║
║                  https://formula1.lne.es/pilotos-f1/                        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
''')
pausa()
print ("""
Se acaba de correr una carrera de F1 de 52 vueltas. Sabemos que corrieron a lo sumo 20 pilotos.

Los datos estan cargados en un diccionario en donde el nombre del piloto es la clave a la que se le asocian tres valores
enteros que representan la duración de la carrera, la de la vuelta mas rapida y la cantidad de vueltas que realizó,
respectivamente.

Los dos primeros datos estan dados en segundos
Ejemplo:
    Hamilton,   6115,113,52
    Vettel,     4720,112,40

Significa que Hamilton completé la carrera en 6115 segundos, su vuelta mas rapida fue de 113 segundos y finaliz6 la
carrera ya que hizo las 52 vueltas. Vettel tuvo su vuelta mas rapida en 112 segundos pero no finalizé la carrera, ya que
completé solo 40 vueltas

Se pide, hacer un programa en Python que:

    'Se proporsionan los datos en un diccionario con listas como valores.'
    'tranformalo en un dicionario con otro diccionario anidado' en base a la aux
Ej
    origen <clave>:    <    lista   >  pasar a < clave > :<                              valor                                               >
                                                          {  <sub clave 1         :val 1>,<sub clave 2       :val 1>,<sub clave 3      :val 3>
          {"Hamilton":[6115, 113, 52], ====>  "Hamilton": {"tiempo_Total en pista":6115  ,"vuelta Mas Rapida":113   ,"total de vueltas":52    },
           "Bottas":  [3610, 115, 30], ====>  "Bottas":   {"tiempo_Total en pista":3610  ,"vuelta Mas Rapida":115   ,"total de vueltas":30    },

cada_clave='Hamilton'
                tiempo_Total en pista=6115
                vuelta Mas Rapida=113
                total de vueltas=52

0) Estructura de datos:
1) Manupulacion de datos:
    A)Genera dos listas de los pilotos que abandonaro y los que no.

    B) Quien gano, con que tiempos de vuelta y totales

    C) Genera el dicionario del podio
    podio= {
            "primero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
            "segundo":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
            "tercero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0}
            }

    D) Genera el dicionario de os 3 pilotos mas rápidos
    piloto_mas_rapido= {
                        "Apellido1":puntos1,
                        "Apellido2":puntos2,
                        "Apellido3":puntos3,
                        }

    E) Genera el diccionario de puntage obtenido por cada piloto: puntaje.
    Para simplificar, solo reciben puntos los pilotos que hayan finalizado la carrera,
    salvo que sea el piloto que hizo la vuelta mas rapida quien recibirá un punto extra haya o no finalizado la carrera.
    datos:
            puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

    En base a la lista de puntos por posición (el primero 25, el segundo 18, etc.)
2) Escuderías
    F) Puntos por escuderia
    G) Podio escuderia
3)  Menu con opciones y colores
4)  Guardan en Excel y BBDD

""")


pausa()
print ("""
Se acaba de correr una carrera de F1 de 52 vueltas. Sabemos que corrieron a lo sumo 20 pilotos.

Los datos estan cargados en un diccionario en donde el nombre del piloto es la clave a la que se le asocian tres valores
enteros que representan la duración de la carrera, la de la vuelta mas rapida y la cantidad de vueltas que realizó,
respectivamente.

Los dos primeros datos estan dados en segundos
Ejemplo:
    Hamilton,   6115,113,52
    Vettel,     4720,112,40

Significa que Hamilton completé la carrera en 6115 segundos, su vuelta mas rapida fue de 113 segundos y finaliz6 la
carrera ya que hizo las 52 vueltas. Vettel tuvo su vuelta mas rapida en 112 segundos pero no finalizé la carrera, ya que
completé solo 40 vueltas

Se pide, hacer un programa en Python que:

    'Se proporsionan los datos en un diccionario con listas como valores.'
    'tranformalo en un dicionario con otro diccionario anidado' en base a la aux
Ej
    origen <clave>:    <    lista   >  pasar a < clave > :<                              valor                                               >
                                                          {  <sub clave 1         :val 1>,<sub clave 2       :val 1>,<sub clave 3      :val 3>
          {"Hamilton":[6115, 113, 52], ====>  "Hamilton": {"tiempo_Total en pista":6115  ,"vuelta Mas Rapida":113   ,"total de vueltas":52    },
           "Bottas":  [3610, 115, 30], ====>  "Bottas":   {"tiempo_Total en pista":3610  ,"vuelta Mas Rapida":115   ,"total de vueltas":30    },
""")
pausa()

aux =  "tiempo total en pista", "vuelta mas rapida", "total de vueltas"

pilotos = [ "George Russell",
            "Lewis Hamilton",
            "Pierre Gasly",
            "Esteban Ocon",
            "Nico Hulkenberg",
            "Kevin Magnussen",
            "Max Verstappen",
            "Sergio Pérez",
            "Lando Norris",
            "Oscar Piastri",
            "Fernando Alonso",
            "Lance Stroll",
            "Yuki Tsunoda",
            "Daniel Ricciardo",
            "Charles Leclerc",
            "Carlos Sainz",
            "Valtteri Bottas",
            "Guanyu Zhou",
            "Alexander Albon",
            "Logan Sargeant",
            "Sergio Pérez"]



"""

 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']



"""



# ~ tiempos_x = dict().fromkeys(pilotos)
# ~ print (dir(dict()))


# ~ print (tiempos_x)


pausa()
limpiar()
tiempos = [[3610, 115, 30],
            [6100, 115, 52],
            [6153, 116, 52],
            [6140, 116, 52],
            [6141, 116, 52],
            [6160, 115, 52],
            [6165, 114, 52],
            [6172, 112, 52],
            [6175, 115, 52],
            [6177, 114, 52],
            [4720, 111, 40],
            [6111, 114, 52],
            [ 700, 119,  5],
            [6201, 118, 52],
            [6133, 114, 52],
            [1205, 118, 10],
            [6272, 122, 52],
            [ 700, 119,  5],
            [6475, 144, 52],
            [5720, 151, 30],
            [6130,  11, 52]      ]


#  los diccionarios no tienen index y no tienen orden
# ~ for enum, claves in enumerate(tiempos_x.keys()):
	# ~ tiempos_x[claves]={ "tiempo total en pista":tiempos[enum][0], "vuelta mas rapida":tiempos[enum][1], "total de vueltas":tiempos[enum][2]}

# ~ print (tiempos_x)
################################################################################

# ~ itemDictionary = dict(zip(pilotos, tiempos))

# ~ print(f"{itemDictionary=}")

# ~ exit()

pilotos_escuderias=["GEORGE RUSSELL","MERCEDES",
                    "LEWIS HAMILTON","MERCEDES",
                    "PIERRE GASLY","ALPINE",
                    "ESTEBAN OCON","ALPINE",
                    "NICO HULKENBERG","HAAS",
                    "KEVIN MAGNUSSEN","HAAS",
                    "MAX VERSTAPPEN","RED BULL",
                    "SERGIO PÉREZ","RED BULL",
                    "LANDO NORRIS","MCLAREN",
                    "OSCAR PIASTRI","MCLAREN",
                    "FERNANDO ALONSO","ASTON MARTIN",
                    "LANCE STROLL","ASTON MARTIN",
                    "YUKI TSUNODA","RB",
                    "DANIEL RICCIARDO","RB",
                    "CHARLES LECLERC","FERRARI",
                    "CARLOS SAINZ","FERRARI",
                    "VALTTERI BOTTAS","KICK SAUBER",
                    "GUANYU ZHOU","KICK SAUBER",
                    "ALEXANDER ALBON","WILLIAMS",
                    "LOGAN SARGEANT","WILLIAMS"]
print ("*"*100)

'''
for cada_piloto,cada_conj_tiempos in zip(pilotos, tiempos):
    tiempo_total_en_pista,vuelta_mas_rapida,total_de_vueltas=cada_conj_tiempos
    print (f"""{cada_piloto}
            {tiempo_total_en_pista=}
            {vuelta_mas_rapida=}
            {total_de_vueltas=}
           """)
'''
tiempos_2 = dict()
# ~ tiempos_2 = {}
def crear_diccionario_total():
    for cada_piloto, (tiempo_total_en_pista,vuelta_mas_rapida,total_de_vueltas) in zip(pilotos, tiempos):
        # ~ print (f"""{cada_piloto}
                # ~ {tiempo_total_en_pista=}
                # ~ {vuelta_mas_rapida=}
                # ~ {total_de_vueltas=}
               # ~ """)
        tiempos_2 [cada_piloto]={
                                "tiempo_total_en_pista":tiempo_total_en_pista,
                                "vuelta_mas_rapida":vuelta_mas_rapida,
                                "total_de_vueltas":total_de_vueltas,
                                "escuderia": pilotos_escuderias[ pilotos_escuderias.index(cada_piloto.upper())+1]
                                }
    print (f"{tiempos_2}")
    for clave_piloto , valores in tiempos_2.items():
        print (f"'{clave_piloto}':{valores},")
crear_diccionario_total()

"""

tiempos_2 = {
    'Lewis Hamilton': {'tiempo_total_en_pista': 6100, 'vuelta_mas_rapida': 115, 'total_de_vueltas': 52, 'escuderia': 'MERCEDES'},
    'Pierre Gasly': {'tiempo_total_en_pista': 6153, 'vuelta_mas_rapida': 116, 'total_de_vueltas': 52, 'escuderia': 'ALPINE'},
    'Esteban Ocon': {'tiempo_total_en_pista': 6140, 'vuelta_mas_rapida': 116, 'total_de_vueltas': 52, 'escuderia': 'ALPINE'},
    'Nico Hulkenberg': {'tiempo_total_en_pista': 6141, 'vuelta_mas_rapida': 116, 'total_de_vueltas': 52, 'escuderia': 'HAAS'},
    'Kevin Magnussen': {'tiempo_total_en_pista': 6160, 'vuelta_mas_rapida': 115, 'total_de_vueltas': 52, 'escuderia': 'HAAS'},
    'Max Verstappen': {'tiempo_total_en_pista': 6165, 'vuelta_mas_rapida': 114, 'total_de_vueltas': 52, 'escuderia': 'RED BULL'},
    'Sergio Pérez': {'tiempo_total_en_pista': 6130, 'vuelta_mas_rapida': 11, 'total_de_vueltas': 52, 'escuderia': 'RED BULL'},
    'Lando Norris': {'tiempo_total_en_pista': 6175, 'vuelta_mas_rapida': 115, 'total_de_vueltas': 52, 'escuderia': 'MCLAREN'},
    'Oscar Piastri': {'tiempo_total_en_pista': 6177, 'vuelta_mas_rapida': 114, 'total_de_vueltas': 52, 'escuderia': 'MCLAREN'},
    'Fernando Alonso': {'tiempo_total_en_pista': 4720, 'vuelta_mas_rapida': 111, 'total_de_vueltas': 40, 'escuderia': 'ASTON MARTIN'},
    'Lance Stroll': {'tiempo_total_en_pista': 6111, 'vuelta_mas_rapida': 114, 'total_de_vueltas': 52, 'escuderia': 'ASTON MARTIN'},
    'Yuki Tsunoda': {'tiempo_total_en_pista': 700, 'vuelta_mas_rapida': 119, 'total_de_vueltas': 5, 'escuderia': 'RB'},
    'Daniel Ricciardo': {'tiempo_total_en_pista': 6201, 'vuelta_mas_rapida': 118, 'total_de_vueltas': 52, 'escuderia': 'RB'},
    'Charles Leclerc': {'tiempo_total_en_pista': 6133, 'vuelta_mas_rapida': 114, 'total_de_vueltas': 52, 'escuderia': 'FERRARI'},
    'Carlos Sainz': {'tiempo_total_en_pista': 1205, 'vuelta_mas_rapida': 118, 'total_de_vueltas': 10, 'escuderia': 'FERRARI'},
    'Valtteri Bottas': {'tiempo_total_en_pista': 6272, 'vuelta_mas_rapida': 122, 'total_de_vueltas': 52, 'escuderia': 'KICK SAUBER'},
    'Guanyu Zhou': {'tiempo_total_en_pista': 700, 'vuelta_mas_rapida': 119, 'total_de_vueltas': 5, 'escuderia': 'KICK SAUBER'},
    'Alexander Albon': {'tiempo_total_en_pista': 6475, 'vuelta_mas_rapida': 144, 'total_de_vueltas': 52, 'escuderia': 'WILLIAMS'},
    'Logan Sargeant': {'tiempo_total_en_pista': 5720, 'vuelta_mas_rapida': 151, 'total_de_vueltas': 30, 'escuderia': 'WILLIAMS'}
}

"""

"""
x=   max(tiempos_2.items(), key=lambda x: x[1].get('tiempo_total_en_pista', float('-inf')))
x=  (max(tiempos_2.items(), key=lambda x: x[1]['tiempo_total_en_pista']))
# ~ print ( 'vuelta_mas_rapida': 144, 'total_de_vueltas': 52, 'escuderia': 'WILLIAMS'})
print (x)
# ~ y=  [x[z]['vuelta_mas_rapida'] for z in x.keys()]
print (x[1]['tiempo_total_en_pista'])

print (max(tiempos_2.items(), key=lambda x: x[1].get('tiempo_total_en_pista', float('-inf')))[1]["tiempo_total_en_pista"])
print (max(tiempos_2.items(), key=lambda x: x[1]['tiempo_total_en_pista'])[1]["tiempo_total_en_pista"])
exit()
"""


######################################################################################
limpiar()
print ("="*100)

def buscar(obj_cant):
	
    pilotos_={}
    for puesto in obj_cant:
        int_menor_ttp=float('inf')
        for cada_piloto in tiempos_2.keys():
            if  tiempos_2[cada_piloto]['tiempo_total_en_pista']<int_menor_ttp and \
                tiempos_2[cada_piloto]['total_de_vueltas']==52 and \
                cada_piloto not in pilotos_.values():
                int_menor_ttp= tiempos_2[cada_piloto]['tiempo_total_en_pista']
                piloto_menor_tiempo = cada_piloto
        pilotos_[puesto]=piloto_menor_tiempo
        print (f"{puesto }   {piloto_menor_tiempo}")
    return pilotos_#piloto_ganador,piloto_segundo,piloto_tercero
#---------------------------------------------------
puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
obj_cant={"Ganador":""}
dic_ = buscar(obj_cant)#    envio 1 solo obj en el diccionario (ganador)
for (lugar, nombre_piloto),cada_punto in zip(dic_.items(),puntos):
    print (F"EL piloto {lugar} es {dic_[lugar]}    puntos obtenidos    {cada_punto}")
    print (f"\t\t{tiempos_2[dic_[lugar]]}")
    print ("-"*50)
print ("^"*100)

#---------------------------------------------------
obj_cant={"Primero":"","Segundo":"","Tercero":""}

dic_ = buscar(obj_cant)#    envio 3 objs en el diccionario ("Primero","Segundo","Tercero")

for (lugar, nombre_piloto),cada_punto in zip(dic_.items(),puntos):
    print (F"EL piloto {lugar} es {dic_[lugar]}    puntos obtenidos    {cada_punto}")
    print (f"\t\t{tiempos_2[dic_[lugar]]}")
    print ("-"*50)
print ("^"*100)

#---------------------------------------------------

obj_cant = {str(index+1):"" for index ,cada_punto in enumerate (puntos) }
print (obj_cant)

dic_ = buscar(obj_cant)#    envio 10 objs en el diccionario ("1","2",..."10")
puntos_gran_premio = {}
for (lugar, nombre_piloto),cada_punto in zip(dic_.items(),puntos):
    print (F"EL piloto {lugar} es {dic_[lugar]}    puntos obtenidos    {cada_punto}")
    print (f"\t\t{tiempos_2[dic_[lugar]]}")
    puntos_gran_premio [nombre_piloto]=cada_punto
    print ("-"*50)
print ("*"*100)

limpiar()
print ("="*100)



######################################################################################
limpiar()
print ("="*100)

def buscar_v_mas_r():
    vuelta_mas_rapida=float('inf')
    for cada_piloto in tiempos_2.keys():
        if  tiempos_2[cada_piloto]['vuelta_mas_rapida']<vuelta_mas_rapida:
            vuelta_mas_rapida= tiempos_2[cada_piloto]['vuelta_mas_rapida']
            piloto_mas_rapido = cada_piloto


    return piloto_mas_rapido

"""
vuelta_mas_rapida=1

"""
piloto_mas_rapido =  buscar_v_mas_r()
print (f"piloto mas rapido fue {piloto_mas_rapido}\n\n\n\n")
if piloto_mas_rapido not in puntos_gran_premio.keys():
    puntos_gran_premio [piloto_mas_rapido]=1
else: #ya tiene puntos xq termino entre los 10 primeros
    #puntos_gran_premio [piloto_mas_rapido]=puntos_gran_premio [piloto_mas_rapido]+1
    puntos_gran_premio [piloto_mas_rapido]+=1

for cada_piloto, cada_punto in puntos_gran_premio.items():
    print (f"piloto {cada_piloto} puntos acumulados en el GP {cada_punto}  {tiempos_2[cada_piloto]} ")


######################################################################################
# ~ limpiar()
print ("="*100)
"""
print
input
while
for
if else
match case
def return
            str
            int
            float
            bool
            list
            tuple
            dict
            -------
            14
                    numpy
                    pandas


2) Escuderías
    F) Puntos por escuderia
        crear diccionario x escuderias
        sumar los puntos de los dos pilotos con la misma escuderia
    G) Podio escuderia (3)
   
        la escuderia 1ra,2da y 3ra
3)  Menu con opciones y colores
4)  Guardan en json, pkl por ultimo Excel y BBDD


"""
exit()
























tiempos_2 = {}
for cada_clave,cada_valor in tiempos_1.items():

    tiempos_2[cada_clave]={aux[0]:cada_valor[0],aux[1]:cada_valor[1],aux[2]:cada_valor[2]}


for cada_clave,cada_valor in tiempos_2.items():
    print (f"{cada_clave=}")
    for cada_sub_clave, cada_sub_valor in cada_valor.items():
        print (f"\t\t{cada_sub_clave}={cada_sub_valor}")

"""
A)Genera dos listas de los pilotos que abandonaro y los que no.
"""
lista_pilotos_fin=[]
lista_pilotos_no_fin=[]
for piloto,cada_valor in tiempos_2.items():
    if cada_valor['total de vueltas']==52:
        lista_pilotos_fin.append(piloto)
    else:#cada_valor['total de vueltas']!=52:
        lista_pilotos_no_fin.append(piloto)

print (f"los pilotos que finalizaron fueron {lista_pilotos_fin} ")
print (f"los pilotos que No finalizaron fueron {lista_pilotos_no_fin} ")
print ("*"*100)
"""
B) Quien gano, con que tiempos de vuelta y totales
"""
tiempo_menor = 9999999999999999
for piloto,cada_valor in tiempos_2.items():
    if cada_valor['total de vueltas']==52 and cada_valor['tiempo_Total en pista'] < tiempo_menor:
        tiempo_menor= cada_valor['tiempo_Total en pista']
        piloto_ganador = piloto

print (f"el piloto ganador fue {piloto_ganador} con 52 vueltas en {tiempo_menor}")
print ("*"*100)
"""
C) Genera el dicionario del podio
podio= {
        "primero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
        "segundo":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
        "tercero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0}
        }
"""
podio = {
        "primero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
        "segundo":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0},
        "tercero":{"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0}
        }
# ~ podio={}
# ~ for lugar in range(0,13):
    # ~ podio[str(lugar)]={"Apellido":"","tiempo_Total en pista":0, "vuelta Mas Rapida":0}

lista_podio=[]
for lugar in podio.keys():
    tiempo_menor = 9999999999999999
    for piloto,cada_valor in tiempos_2.items():
        if cada_valor['total de vueltas']==52 and cada_valor['tiempo_Total en pista'] < tiempo_menor and piloto not in lista_podio:
            tiempo_menor= cada_valor['tiempo_Total en pista']
            podio[lugar]={"Apellido":piloto,"tiempo_Total en pista":cada_valor['tiempo_Total en pista'], "vuelta Mas Rapida":cada_valor['vuelta Mas Rapida']}
            piloto_m =piloto
    lista_podio.append(piloto_m)
    print (f"{lista_podio=}")

for lugar,valores in podio.items():
    print(f"{lugar} {valores}")
"""
D) Genera el dicionario de os 3 pilotos mas rápidos
piloto_mas_rapido= {
                    "Apellido1":puntos1,
                    "Apellido2":puntos2,
                    "Apellido3":puntos3,
                    }
"""
print("*"*100)
piloto_mas_rapido= {}
lista_mas_rapido=[]
puntos=3
for lugar in range(3):
    vuelta_Mas_Rapida = 9999999999999999
    for piloto,cada_valor in tiempos_2.items():
        if cada_valor['vuelta Mas Rapida'] < vuelta_Mas_Rapida and piloto not in lista_mas_rapido:
            vuelta_Mas_Rapida= cada_valor['vuelta Mas Rapida']
            piloto_mas_rapido[piloto]=puntos
            piloto_m =piloto
    lista_mas_rapido.append(piloto_m)
    puntos = puntos-1
    print (f"{lista_mas_rapido=}")

for lugar,valores in piloto_mas_rapido.items():
    print(f"{lugar} {valores}")
"""


E)Genera el diccionario de puntage obtenido por cada piloto: puntaje.
Para simplificar, solo reciben puntos los pilotos que hayan finalizado la carrera,
salvo que sea el piloto que hizo la vuelta mas rapida quien recibirá un punto extra haya o no finalizado la carrera.
datos:
        puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

En base a la lista de puntos por posición (el primero 25, el segundo 18, etc.)


"""
print("*"*100)




puntos = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
llegada = {}
lista_puntos=[]
for punto_en_tabla in puntos:
    tiempo_menor = 9999999999999999
    for piloto,cada_valor in tiempos_2.items():
        if cada_valor['total de vueltas']==52 and cada_valor['tiempo_Total en pista'] < tiempo_menor and piloto not in lista_puntos:
            tiempo_menor= cada_valor['tiempo_Total en pista']
            llegada[piloto]=punto_en_tabla
            piloto_m =piloto
    lista_puntos.append(piloto_m)


for lugar,valores in llegada.items():
    print(f"{lugar} {valores}")
print(" + "*10)

piloto_mas_rapido= {}
lista_mas_rapido=[]
puntos=3
for lugar in range(3):
    vuelta_Mas_Rapida = 9999999999999999
    for piloto,cada_valor in tiempos_2.items():
        if cada_valor['vuelta Mas Rapida'] < vuelta_Mas_Rapida and piloto not in lista_mas_rapido:
            vuelta_Mas_Rapida= cada_valor['vuelta Mas Rapida']
            piloto_mas_rapido[piloto]=puntos
            piloto_m =piloto
    lista_mas_rapido.append(piloto_m)
    puntos = puntos-1
    print (f"{lista_mas_rapido=}")

for lugar,valores in piloto_mas_rapido.items():
    print(f"{lugar} {valores}")
print(" = "*10)
# ~ for lugar_LL,piloto_LL in llegada.items():
for piloto_PMR,puntos_PMR in piloto_mas_rapido.items():
    if piloto_PMR in llegada.keys():
        llegada[piloto_PMR]=llegada[piloto_PMR]+piloto_mas_rapido[piloto_PMR]
    else:
        llegada[piloto_PMR]=piloto_mas_rapido[piloto_PMR]
print(" ^ "*10)
for lugar,valores in llegada.items():
    print(f"{lugar} {valores}")
print(" = "*10)
