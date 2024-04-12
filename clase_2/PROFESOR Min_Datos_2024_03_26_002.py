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
def jugar_con_diccionarios():
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
	dic= {}
	for pilotos in pilotos_escuderias[::2]:
		print (f"{pilotos=}")
	for escuderia in pilotos_escuderias[1::2]:
		print (f"{escuderia=}")
	###############################################

	for piloto,escuderia in zip(pilotos_escuderias[::2],pilotos_escuderias[1::2]):
		print (f"{piloto=}    {escuderia=}")
		dic[piloto]=escuderia

	print (dic)
	dic2 = dict(zip(pilotos_escuderias[::2],pilotos_escuderias[1::2]))
	print (dic2)
# ~ jugar_con_diccionarios()
# ~ pausa()
# ~ limpiar()
def listas():
	
	lista_par=[]
	lista_impar=[]
	cont=0
	#								extención
	for dato in lista:
		if dato %2 != 0 :
			lista_impar.append(dato)
		elif dato == 0 :
			# ~ cont=cont+1
			cont+=1
		else:
			lista_par.append(dato)
		
	print (f"{lista_impar=}")
	print (f"{lista_par=}")		
	print (f"{cont=}")

	#                                one line comprenhesion list or dict

	lista_par2  =[dato for dato in lista if dato %2 == 0 and dato != 0]
	lista_impar2=[dato for dato in lista if dato %2 != 0 ]
	cont2=lista.count(0)

	print (f"{lista_impar2=}")
	print (f"{lista_par2=}")		
	print (f"{cont2=}")

	#                               lista verdadero(par) o falso(impar)

	#------------------------------------------------------------
	lista_v_f = []
	for dato in lista:
		if dato%2 != 0 :
			lista_v_f.append(False)
		else:
			lista_v_f.append(True)
	print (f"{lista_v_f=}")
	lista_v_f2 = [   False  if dato%2 != 0  else True  for dato in lista]
	print (f"{lista_v_f2=}")
	#------------------------------------------------------------
	lista_v_f4 = []
	for dato in lista:
		if dato%2 != 0 :
			lista_v_f4.append(False)
		else:
			if dato%2 == 0 and dato != 0:
				lista_v_f4.append(True)
			else:
				lista_v_f4.append(None)
			
			
	print (f"{lista_v_f4=}")
	lista_v_f5 = [   False  if dato%2 != 0 \
							else (True if dato%2 == 0 and \
							dato != 0 else None)   for dato in lista]
	print (f"{lista_v_f5=}")
	#------------------------------------------------------------



# ~ lista = [1,2,0,3,5,4,6,8,0,8,7,5,1,8,9,0,1,8]
# ~ pausa()
# ~ limpiar()listas()
# ~ pausa()
# ~ limpiar()
dato = "Ariel "
def ejemplo_de_ambitos(dato):
	print (f"{dato=}")
	dato= dato*2
	return dato
	
def menu():
	dato =8
	dato = ejemplo_de_ambitos(dato)
	print (f"{dato=}")
	return dato
regreso = menu()
print (f"{dato=}")
print (f"{regreso=}")


print ("-"*50)
dato = 10
def ejemplo_de_ambitos():
	print ("si el dato ingresa por orden superior no puede modificarse variables de 1 dato")
	print (f"{dato=}")
	# ~ dato= dato*10
	print (f"{dato=}")
ejemplo_de_ambitos()



print ("-"*50)
dato = 10
def ejemplo_de_ambitos(dato):
	print ("si el dato ingresa por parametro si puede modificarse variables de 1 dato")
	print (f"{dato=}")
	dato= dato*10
	print (f"{dato=}")
ejemplo_de_ambitos(dato)
#-------------------------------------------------

print ("-"*50)
dato = "Hola "
def ejemplo_de_ambitos():
	print ("si el dato ingresa por orden superior no puede modificarse variables de 1 dato")
	print (f"{dato=}")
	# ~ dato= dato.upper()
	print (f"{dato=}")
ejemplo_de_ambitos()


print ("-"*50)
dato = "Hola "
def ejemplo_de_ambitos(dato):
	print ("si el dato ingresa por parametro si puede modificarse variables de 1 dato")
	print (f"{dato=}")
	dato= dato.upper()
	print (f"{dato=}")
ejemplo_de_ambitos(dato)


print ("-"*50)
dato = "Hola "
secreto = "**********"
def ejemplo_de_ambitos():
	global dato
	global secreto
	print ("si el dato ingresa por orden superior no puede modificarse variables de 1 dato")
	print (f"{dato=}")
	dato= dato.upper()
	print (f"{dato=}")
	secreto*=2
	print (f"{secreto=}")
ejemplo_de_ambitos()




######################################################################
print ("*"*100)
print ("-"*50)
coleccion = [10]
def ejemplo_de_ambitos():
	print ("si el coleccion ingresa por orden superior tambien puede modificarse variables de 1 coleccion")
	print (f"{coleccion=}")
	coleccion.append(1000)
	print (f"{coleccion=}")
ejemplo_de_ambitos()



print ("-"*50)
coleccion = [10]
def ejemplo_de_ambitos(coleccion):
	print ("si el coleccion ingresa por parametro si puede modificarse variables de 1 coleccion")
	print (f"{coleccion=}")
	coleccion.append(1000)
	print (f"{coleccion=}")
ejemplo_de_ambitos(coleccion)
#-------------------------------------------------

print ("-"*50)
coleccion = ["Hola "]
def ejemplo_de_ambitos():
	print ("si el coleccion ingresa por orden superior tambien puede modificarse variables de 1 coleccion")
	print (f"{coleccion=}")
	coleccion.append ("como va todo?")
	print (f"{coleccion=}")
ejemplo_de_ambitos()


print ("-"*50)
coleccion = ["Hola "]
def ejemplo_de_ambitos(coleccion):
	print ("si el coleccion ingresa por parametro si puede modificarse variables de 1 coleccion")
	print (f"{coleccion=}")
	coleccion.append ("como va todo?")
	print (f"{coleccion=}")
ejemplo_de_ambitos(coleccion)
#-------------------------------------------------

print ("-"*50)
coleccion = {"juan":"Hola "}
def ejemplo_de_ambitos():
	print ("si el coleccion ingresa por orden superior tambien puede modificarse variables de 1 coleccion")
	print (f"{coleccion=}")
	coleccion["pepe"]= "como va todo?"
	print (f"{coleccion=}")
ejemplo_de_ambitos()


print ("-"*50)
coleccion = {"juan":"Hola "}
def ejemplo_de_ambitos(coleccion):
	print ("si el coleccion ingresa por parametro si puede modificarse variables de 1 coleccion")
	print (f"{coleccion=}")
	coleccion["pepe"]= "como va todo?"
	print (f"{coleccion=}")
ejemplo_de_ambitos(coleccion)
######################################################################

print ("-"*50)
coleccion = ["Hola "]
def ejemplo_de_ambitos(*coleccion):
	print ("si el coleccion ingresa por orden superior tambien puede modificarse variables de 1 coleccion")
	print (f"{coleccion=}")
	coleccion = list (coleccion)
	coleccion.append ("como va todo?")
	print (f"{coleccion=}")
ejemplo_de_ambitos(*coleccion)


######################################################################

print ("-"*50)
coleccion = {"juan":"Hola "}
def ejemplo_de_ambitos(**coleccion):
	print ("si el coleccion ingresa por parametro si puede modificarse variables de 1 coleccion")
	print (f"{coleccion=}")
	coleccion["pepe"]= "como va todo?"
	print (f"{coleccion=}")
ejemplo_de_ambitos(**coleccion)

######################################################################
def valores (precio, descuento=0):
	print (f"descuento del {descuento}%")
	return eval(f"{precio}/1.{descuento}")
print (valores (1000,10))
print (valores (999))



exit()

