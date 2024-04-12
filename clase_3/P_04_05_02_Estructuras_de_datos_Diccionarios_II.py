from  __init__ import *
import pickle
limpiar()
print (f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
║                      ╔══════╗    ╦    ╔═════╗    ╔═══╦═══╗                  ║
║                      ║      ╚╗   ║   ╔╝     ╚╗       ║                      ║
║                      ║       ║   ║   ║               ║                      ║
║                      ║       ║   ║   ║               ║                      ║
║                      ║       ║   ║   ║               ║                      ║
║                      ║       ║   ║   ║               ║                      ║
║                      ║      ╔╝   ║   ╚╗     ╔╝       ║                      ║
║                      ╚══════╝    ╩    ╚═════╝        ╩                      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m""");
pausa();limpiar();
#################################################################
print("             ahora el index de una lista no solo es un numero del 0 al fin sino que podemos usar Alfanumericos y no solo enteros")
from collections import defaultdict
Nombre_diccionario_1 ={}
#print (dir(dict))
Nombre_diccionario_1.update({
                            "clave 1":"dato_asociado 1",
                            "clave 2":"dato_asociado 2",
                            "clave 3":"dato_asociado 3",
                            "clave 4":"dato_asociado 4",
                            "clave 5":"fin"
                                })

print (type(Nombre_diccionario_1))
print (f"clave 1  {Nombre_diccionario_1['clave 1']}")
print (f"clave 2  {Nombre_diccionario_1['clave 2']}")
print (f"clave 3  {Nombre_diccionario_1['clave 3']}")
print (f"clave 4  {Nombre_diccionario_1['clave 4']}")
print (f"clave 5  {Nombre_diccionario_1['clave 5']}")
print("*"*35)
print (f"clave 100  {Nombre_diccionario_1.get('clave 100','no hay clave 100')}")
pausa()
limpiar()
#################################################################
print("*"*35)
print (f"cantidad de datos(claves principales) en el dic : {len(Nombre_diccionario_1)}")
print (f"items : {Nombre_diccionario_1.items()}")
print ("*"*60)
print (f"llaves : {Nombre_diccionario_1.keys()}")
print ("*"*60)
print (f"valores : {Nombre_diccionario_1.values()}")
print ("*"*60)
pausa()
limpiar()
#################################################################
print("*"*35)
Nombre_list_diccionario_1=[
                    {"Nombre":"Ariel","Apellido":"Garcia","Edad":47},
                    {"Nombre":"Daniela","Apellido":"Perez","Edad":48},
                    {"Nombre":"Ana","Apellido":"Gonzalez","Edad":42},
                    {"Nombre":"Juan","Apellido":"Gomez","Edad":41},
                    {"Nombre":"Pepe","Apellido":"Martin","Edad":43}
                ]

Nombre_diccionario_1 = sorted(Nombre_list_diccionario_1 ,  key=lambda Nombre_list_diccionario_1: Nombre_list_diccionario_1 ['Edad'])

#################################################################
print("*"*35)
Nombre_list_diccionario_1=[
                    {"Nombre":"Ariel","Apellido":"Garcia","Edad":47},
                    {"Nombre":"Daniela","Apellido":"Perez","Edad":48},
                    {"Nombre":"Ana","Apellido":"Gonzalez","Edad":42},
                    {"Nombre":"Juan","Apellido":"Gomez","Edad":41},
                    {"Nombre":"Pepe","Apellido":"Martin","Edad":43}
                ]

Nombre_diccionario_1 ={lista["Nombre"]:{"Apellido":lista["Apellido"],"Edad":lista["Edad"]} for lista in Nombre_list_diccionario_1 }
# ~ sorted(Nombre_list_diccionario_1 ,  key=lambda Nombre_list_diccionario_1: Nombre_list_diccionario_1 ['Edad'])

print(f"Nombre_diccionario_1:{Nombre_diccionario_1}")

for indice,clave in enumerate(Nombre_diccionario_1.keys()):
    valor=Nombre_diccionario_1[clave]
    print (f"{indice} {clave}  {valor}")

for indice,[clave,valor] in enumerate(Nombre_diccionario_1.items()):
    print (f"{indice} {clave}  {valor}")
print("*"*35)
listaKeys = [clave  for clave,valor in Nombre_diccionario_1.items()]
print(f"{listaKeys=}")

DicClaveValor = {clave :valor for clave,valor in Nombre_diccionario_1.items()}
print(f"{DicClaveValor=}")
pausa()
limpiar()
#################################################################
print("*"*35)
for x in range(4):
    newDict = {key: value for (key, value) in Nombre_list_diccionario_1[x].items() }
    print(f"{'Filtered Dictionary : '}")
    print(f"{newDict=}")


newDict = {key: value for (key, value) in Nombre_list_diccionario_1[x].items() for x in range(4) }
print(f"{'Filtered Dictionary : '}")
print(f"{newDict=}")
pausa()
limpiar()
#################################################################
print("*"*35)
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}
# Get the corresponding `celsius` values and create the new dictionary
celsius_dict = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(f"{celsius_dict=}")
pausa()
limpiar()
#################################################################
print("*"*35)
import operator
# Sort the Dict based on keys
sorted_dict = dict(sorted(Nombre_list_diccionario_1[0].items(), key=operator.itemgetter(0)))
print(f"{sorted_dict=}")

nested_dict = {'primero':{'nombre':"Ariel", "apellido":"garcia"}, 'segundo':{'nombre':"juan",'apellido':"Perez"}}
float_dict = {outer_k: {inner_v for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(f"{float_dict=}")
pausa()
limpiar()
#################################################################
print("*"*35)
models = [{'nick':'xx', 'nombre':"Ariel", 'apellido':'garcia'}, {'nick':'yyy', 'nombre':'juan', 'apellido':'Perez'}, {'nick':'zzzz', 'nombre': "Ana", 'apellido':'Gonzalez'}]
print(f"Original list of dictionaries :")
print(f"{models=}")
sorted_models = sorted(models, key = lambda x: x['nombre'])
print(f"\nSorting the List of dictionaries :")
print(f"{sorted_models=}")
pausa()
limpiar()
#################################################################
print("*"*35)

