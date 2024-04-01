import json

#fuente
aux =  "tiempo_Total en pista", "vuelta Mas Rapida", "total de vueltas"

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



tiempos = [[3610, 115, 30],
            [6150, 115, 52],
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
            [700, 119, 5],
            [6201, 118, 52],
            [6133, 114, 52],
            [1205, 118, 10],
            [6272, 122, 52],
            [6375, 135, 52],
            [6475, 144, 52],
            [5720, 151, 30],
            [6130, 11, 52]      ]
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









#tiempos2 = dict()
tiempos2 = {}


print (f"el objeto contiene {tiempos2}  es del tipo {type (tiempos2}")

"""
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


"""
exit()




















"""
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
"""

print ("*"*100)
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


