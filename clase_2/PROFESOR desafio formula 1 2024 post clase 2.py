import json
# ~ datos = {
    # ~ 'persona1': {'nota1': 90, 'nota2': 85, 'nota3': 78},
    # ~ 'persona2': {'nota1': 70, 'nota2': 75, 'nota3': 80},
    # ~ 'persona3': {'nota1': 88, 'nota2': 92, 'nota3': 85},
    # ~ # y así sucesivamente...
# ~ }

# ~ # Usando una expresión de generador y la función max con una función de clave personalizada
# ~ clave_max_nota = max(datos, key=lambda k: datos[k]['nota1'])
# ~ nota_max = datos[clave_max_nota]['nota1']

# ~ print("La persona con la nota más alta es:", clave_max_nota)
# ~ print("La nota más alta es:", nota_max)
# ~ exit()
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



tiempos = [[3610, 115, 30],
            [6100, 115, 52],
            [6153, 116, 52],
            [6140, 116, 52],
            [6141, 116, 52],
            [6160, 115, 52],
            [6099, 114, 52],
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

def primer_paso():
	tiempos_2 = {}
	'''
	for cada_piloto,cada_vector in zip(pilotos,tiempos):
		
		tiempo_total_en_pista=cada_vector[0]
		vuelta_mas_rapida=cada_vector[1]
		total_de_vueltas=cada_vector[2]
		print (f"""{cada_piloto=} 
		{tiempo_total_en_pista=}
		{vuelta_mas_rapida=}
		{total_de_vueltas=}
		""")
		tiempos_2[cada_piloto]={
								"tiempo_total_en_pista" :tiempo_total_en_pista,
								"vuelta_mas_rapida":vuelta_mas_rapida,
								"total_de_vueltas" :total_de_vueltas
								}
	'''
	for cada_piloto,(tiempo_total_en_pista,vuelta_mas_rapida,total_de_vueltas) in zip(pilotos,tiempos):
		# ~ print (f"""{cada_piloto=} 
		# ~ {tiempo_total_en_pista=}
		# ~ {vuelta_mas_rapida=}
		# ~ {total_de_vueltas=}
		# ~ """)
		tiempos_2[cada_piloto]={
								"tiempo_total_en_pista" :tiempo_total_en_pista,
								"vuelta_mas_rapida":vuelta_mas_rapida,
								"total_de_vueltas" :total_de_vueltas,
								"Escuderia"        :pilotos_escuderias[pilotos_escuderias.index(cada_piloto.upper())+1]
								}
		# ~ index_piloto= pilotos_escuderias.index(cada_piloto.upper())
		# ~ escuderia   = pilotos_escuderias[index_piloto+1]
		#_______________________________________________________
		#pilotos_escuderias[pilotos_escuderias.index(cada_piloto.upper())+1]
	for clave,valores in tiempos_2.items():
		print (f"\t'{clave}':\n{valores},")
		
	return tiempos_2
tiempos_2 = primer_paso()
"""
tiempos_2= {
		'George Russell':{'tiempo_total_en_pista': 3610, 'vuelta_mas_rapida': 115, 'total_de_vueltas': 30, 'Escuderia': 'MERCEDES'},
		'Lewis Hamilton':{'tiempo_total_en_pista': 6100, 'vuelta_mas_rapida': 115, 'total_de_vueltas': 52, 'Escuderia': 'MERCEDES'},
		'Pierre Gasly':{'tiempo_total_en_pista': 6153, 'vuelta_mas_rapida': 116, 'total_de_vueltas': 52, 'Escuderia': 'ALPINE'},
		'Esteban Ocon':{'tiempo_total_en_pista': 6140, 'vuelta_mas_rapida': 116, 'total_de_vueltas': 52, 'Escuderia': 'ALPINE'},
		'Nico Hulkenberg':{'tiempo_total_en_pista': 6141, 'vuelta_mas_rapida': 116, 'total_de_vueltas': 52, 'Escuderia': 'HAAS'},
		'Kevin Magnussen':{'tiempo_total_en_pista': 6160, 'vuelta_mas_rapida': 115, 'total_de_vueltas': 52, 'Escuderia': 'HAAS'},
		'Max Verstappen':{'tiempo_total_en_pista': 6165, 'vuelta_mas_rapida': 114, 'total_de_vueltas': 52, 'Escuderia': 'RED BULL'},
		'Sergio Pérez':{'tiempo_total_en_pista': 6130, 'vuelta_mas_rapida': 11, 'total_de_vueltas': 52, 'Escuderia': 'RED BULL'},
		'Lando Norris':{'tiempo_total_en_pista': 6175, 'vuelta_mas_rapida': 115, 'total_de_vueltas': 52, 'Escuderia': 'MCLAREN'},
		'Oscar Piastri':{'tiempo_total_en_pista': 6177, 'vuelta_mas_rapida': 114, 'total_de_vueltas': 52, 'Escuderia': 'MCLAREN'},
		'Fernando Alonso':{'tiempo_total_en_pista': 4720, 'vuelta_mas_rapida': 111, 'total_de_vueltas': 40, 'Escuderia': 'ASTON MARTIN'},
		'Lance Stroll':{'tiempo_total_en_pista': 6111, 'vuelta_mas_rapida': 114, 'total_de_vueltas': 52, 'Escuderia': 'ASTON MARTIN'},
		'Yuki Tsunoda':{'tiempo_total_en_pista': 700, 'vuelta_mas_rapida': 119, 'total_de_vueltas': 5, 'Escuderia': 'RB'},
		'Daniel Ricciardo':{'tiempo_total_en_pista': 6201, 'vuelta_mas_rapida': 118, 'total_de_vueltas': 52, 'Escuderia': 'RB'},
		'Charles Leclerc':{'tiempo_total_en_pista': 6133, 'vuelta_mas_rapida': 114, 'total_de_vueltas': 52, 'Escuderia': 'FERRARI'},
		'Carlos Sainz':{'tiempo_total_en_pista': 1205, 'vuelta_mas_rapida': 118, 'total_de_vueltas': 10, 'Escuderia': 'FERRARI'},
		'Valtteri Bottas':{'tiempo_total_en_pista': 6272, 'vuelta_mas_rapida': 122, 'total_de_vueltas': 52, 'Escuderia': 'KICK SAUBER'},
		'Guanyu Zhou':{'tiempo_total_en_pista': 700, 'vuelta_mas_rapida': 119, 'total_de_vueltas': 5, 'Escuderia': 'KICK SAUBER'},
		'Alexander Albon':{'tiempo_total_en_pista': 6475, 'vuelta_mas_rapida': 144, 'total_de_vueltas': 52, 'Escuderia': 'WILLIAMS'},
		'Logan Sargeant':{'tiempo_total_en_pista': 5720, 'vuelta_mas_rapida': 151, 'total_de_vueltas': 30, 'Escuderia': 'WILLIAMS'}
		}
"""
print ("*"*50)
###################################################################################
def buscar_ganador(tiempos_2):
	menor_tiempo=999999
	for nombre_piloto in tiempos_2.keys():
		if 	tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo and \
			tiempos_2[nombre_piloto]['total_de_vueltas'] == 52:
			menor_tiempo = tiempos_2[nombre_piloto]['tiempo_total_en_pista']
			piloto =  nombre_piloto
			# ~ print (f"""
			# ~ {piloto=}
			# ~ {menor_tiempo=}
			# ~ {(tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo )=}
			# ~ {(tiempos_2[nombre_piloto]['total_de_vueltas'] == 52)=}
			# ~ """)	
	return piloto
ganador = buscar_ganador(tiempos_2)
print (f"el piloto ganador fue {ganador}")
print (f"sus valores fueron {tiempos_2[ganador]}" )
print ("*"*50)
###################################################################################
'''
def buscar_podio(tiempos_2):
	pilotos_podio=[]
	for puesto in ["primero", "segundo", "tercero"]:
		menor_tiempo=999999
		for nombre_piloto in tiempos_2.keys():
			if 	tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo and \
				tiempos_2[nombre_piloto]['total_de_vueltas'] == 52 and \
				nombre_piloto not in pilotos_podio:
				menor_tiempo = tiempos_2[nombre_piloto]['tiempo_total_en_pista']
				piloto =  nombre_piloto
				# ~ print (f"""
				# ~ {piloto=}
				# ~ {menor_tiempo=}
				# ~ {(tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo )=}
				# ~ {(tiempos_2[nombre_piloto]['total_de_vueltas'] == 52)=}
				# ~ """)	
		# ~ print (f" {puesto} {piloto}")
		pilotos_podio.append(piloto)
	return pilotos_podio
pilotos_podio = buscar_podio(tiempos_2)
print (f"el piloto ganador fue {pilotos_podio[0]}")
print (f"sus valores fueron {tiempos_2[pilotos_podio[0]]}" )

print (f"el piloto segundo fue {pilotos_podio[1]}")
print (f"sus valores fueron {tiempos_2[pilotos_podio[1]]}" )

print (f"el piloto tercero fue {pilotos_podio[2]}")
print (f"sus valores fueron {tiempos_2[pilotos_podio[2]]}" )
print ("*"*50)
'''
def buscar_podio(tiempos_2, resultados_a_sacar ):
	for puesto in resultados_a_sacar.keys():
		menor_tiempo=999999
		for nombre_piloto in tiempos_2.keys():
			if 	tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo and \
				tiempos_2[nombre_piloto]['total_de_vueltas'] == 52 and \
				nombre_piloto not in resultados_a_sacar.values():
				menor_tiempo = tiempos_2[nombre_piloto]['tiempo_total_en_pista']
				piloto =  nombre_piloto
				# ~ print (f"""
				# ~ {piloto=}
				# ~ {menor_tiempo=}
				# ~ {(tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo )=}
				# ~ {(tiempos_2[nombre_piloto]['total_de_vueltas'] == 52)=}
				# ~ """)	
		print (f" {puesto} {piloto}")
		resultados_a_sacar[puesto]=piloto
	return resultados_a_sacar
resultados	= {"primero":"", "segundo":"", "tercero":""}
pilotos_podio_dic = buscar_podio(tiempos_2, resultados)
for puesto, piloto_nombre in pilotos_podio_dic.items():
	print (f"el piloto {puesto} fue {piloto_nombre}")
	print (f"sus valores fueron {tiempos_2[piloto_nombre]}" )
print ("*"*50)
###################################################################################

def buscar_puntos(tiempos_2, resultados_a_sacar ):
	for puesto in resultados_a_sacar.keys():
		menor_tiempo=999999
		for nombre_piloto in tiempos_2.keys():
			if 	tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo and \
				tiempos_2[nombre_piloto]['total_de_vueltas'] == 52 and \
				nombre_piloto not in resultados_a_sacar.values():
				menor_tiempo = tiempos_2[nombre_piloto]['tiempo_total_en_pista']
				piloto =  nombre_piloto
				# ~ print (f"""
				# ~ {piloto=}
				# ~ {menor_tiempo=}
				# ~ {(tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo )=}
				# ~ {(tiempos_2[nombre_piloto]['total_de_vueltas'] == 52)=}
				# ~ """)	
		print (f" {puesto} {piloto}")
		resultados_a_sacar[puesto]=piloto
	return resultados_a_sacar
def buscar_piloto_mas_rapida(tiempos_2, resultados_a_sacar={"Mas rapido":""}):
	vuelta_mas_rapida=999
	for nombre_piloto in tiempos_2.keys():
		if 	tiempos_2[nombre_piloto]['vuelta_mas_rapida'] < vuelta_mas_rapida :
			vuelta_mas_rapida = tiempos_2[nombre_piloto]['vuelta_mas_rapida']
			piloto =  nombre_piloto	
	return piloto
	
	
	
	
puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
resultados	= {}
pilotos_puntos_dic = {}
for indice, _ in enumerate(puntos):
	resultados[str(indice+1)]=""
print (f"{resultados=}")
pilotos_puesto_dic = buscar_puntos(tiempos_2, resultados)

for (puesto, piloto_nombre), cada_punto in zip(pilotos_puesto_dic.items(), puntos):
	print (f"el piloto {puesto} fue {piloto_nombre} y obtuvo {cada_punto} puntos")
	print (f"sus valores fueron {tiempos_2[piloto_nombre]}" )
	pilotos_puntos_dic[piloto_nombre]= cada_punto
print ("*"*50)


pilotos_mas_rapido = buscar_piloto_mas_rapida(tiempos_2)
print (f"piloto mas rapido {pilotos_mas_rapido}")

print (f"{pilotos_puntos_dic}")
if pilotos_mas_rapido not in pilotos_puntos_dic.keys():
	print (pilotos_puntos_dic[pilotos_mas_rapido])
	pilotos_puntos_dic[pilotos_mas_rapido] =  1
else:
	pilotos_puntos_dic[pilotos_mas_rapido] +=  1
	
for piloto_nombre, cada_punto in pilotos_puntos_dic.items():
	print (f"el {piloto_nombre} y obtuvo {cada_punto} puntos")
	print (f"sus valores fueron {tiempos_2[piloto_nombre]}" )
"""
tiempos_2 					tengo todo los datos 
pilotos_puntos_dic          los puntos ganados por orden(10) mas vuelta mas rapida
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
2) Escuderías
	F) Puntos por escuderia
	G) Podio escuderia


"""
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
def buscar_puntos(tiempos_2, resultados_a_sacar ):
	for puesto in resultados_a_sacar.keys():
		menor_tiempo=999999
		for nombre_piloto in tiempos_2.keys():
			if 	tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo and \
				tiempos_2[nombre_piloto]['total_de_vueltas'] == 52 and \
				nombre_piloto not in resultados_a_sacar.values():
				menor_tiempo = tiempos_2[nombre_piloto]['tiempo_total_en_pista']
				piloto =  nombre_piloto
				# ~ print (f"""
				# ~ {piloto=}
				# ~ {menor_tiempo=}
				# ~ {(tiempos_2[nombre_piloto]['tiempo_total_en_pista'] < menor_tiempo )=}
				# ~ {(tiempos_2[nombre_piloto]['total_de_vueltas'] == 52)=}
				# ~ """)	
		print (f" {puesto} {piloto}")
		resultados_a_sacar[puesto]=piloto
	return resultados_a_sacar

#------------------------------------------------------	
puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
resultados	= {}
pilotos_puntos_dic = {}
for indice, _ in enumerate(puntos):
	resultados[str(indice+1)]=""
print (f"{resultados=}")
#------------------------------------------------------
# ~ resultados = {"ganador":"","segundo":"","tercero":""}

pilotos_puesto_dic = buscar_puntos(tiempos_2, resultados)

for (puesto, piloto_nombre), cada_punto in zip(pilotos_puesto_dic.items(), puntos):
	print (f"el piloto {puesto} fue {piloto_nombre} y obtuvo {cada_punto} puntos")
	print (f"sus valores fueron {tiempos_2[piloto_nombre]}" )
	pilotos_puntos_dic[piloto_nombre]= cada_punto
print ("*"*50)
"""
objetos tipo funcion
	print
			input	
	if else elif
			while
	for
	def - return
objetos datos
	diccionarios 
	variables numericas y string 
			listas ni tuplas ni set
objetos operadores
	asignacion =
	aritméticos < , ==
	pertenencia   in ,not in 
			ver otros operadores 

"""






