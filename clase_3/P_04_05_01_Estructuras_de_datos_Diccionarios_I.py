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
print (f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                Python dictionary Methods                    ║
║                               ---------------------------                   ║
║                                                                             ║
║         Method    Description                                               ║
║                                                                             ║
║         clear()   Removes all the elements from the dictionary              ║
║         copy()    Returns a copy of the dictionary                          ║
║         fromkeys()Returns a dictionary with the specified keys and values   ║
║         get()     Returns the value of the specified key                    ║
║         items()   Returns a list containing a tuple for each key value pair ║
║         keys()    Returns a list containing the dictionary's keys           ║
║         pop()     Removes the element at the specified position             ║
║         popitem() Removes the last inserted key-value pair                  ║
║         reverse() Reverses the order of the dictionary                      ║
║         setdefault() Returns the value of the specified key. If the key     ║
║                   does not exist: insert the key, with the specified value  ║
║         update()  Updates the dictionary with the specified key-value pairs ║
║         values()  Returns a list of all the values in the dictionary        ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                      Diccionarios                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
https://www.w3schools.com/python/python_ref_dictionary.asp
https://www.w3schools.com/python/python_dictionaries.asp
https://python-para-impacientes.blogspot.com/2014/01/cadenas-listas-tuplas-diccionarios-y.html


Diccionarios o matrices asociativas
Los diccionarios son objetos que contienen una lista de parejas de elementos.
De cada pareja un elemento es la clave, que no puede repetirse, y, el otro, un valor asociado.
La clave que se utiliza para acceder al valor tiene que ser un dato inmutable como una cadena,
El valor puede ser un número, una cadena, un valor lógico (True/False), una lista o una tupla.
Los pares clave-valor están separados por dos puntos, las parejas por comas y todo el conjunto se encierra entre llaves.
""");
pausa();
limpiar();
#################################################################
#Ejercicio_Diccionarios_Ej_00
print("             partimos de una lista a un diccionario. Podemos ver que ambos son compatibles")

lista=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
dic={}
for lugar, dato in enumerate(lista):
    print (lugar, dato)
    dic[lugar]=dato
print (f"\t\t{dic}")
print (f"\t\t{dic[9]}")
pausa();
limpiar();
#################################################################


print("             ahora el index de una lista no solo es un numero del 0 al fin sino que podemos usar Alfanumericos y no solo enteros")


Nombre_diccionario_1 =  {
                            "clave 1":"dato_asociado 1",
                            "clave 2":"dato_asociado 2",
                            "clave 3":"dato_asociado 3",
                            "clave 4":"",
                            "NOMBRE":"Ariel",
                            "APELLIDO":"Garcia",
                            "EDAD":47,
                            "TELEFONO":"+54 9 11 4475 4673",
                            "clave 5":"dato_asociado 5",
                            "clave 6":(
                                        "DATO 1",
                                        "DATO 2",
                                        ),
                            "clave 7":{
                                        "primario":"dato_asociado 7,1",
                                        "secundario":"dato_asociado 7.2",
                                        "terciario":"dato_asociado 7.3"
                                        },
                            "clave 8":"dato_asociado 8",
                            "clave 9":"dato_asociado 9",
                            "clave 10":"dato_asociado 10"
                        }
#Nombre_diccionario_2  ={'client_id': 'sensores', 'topic': 'plantaEscobar', 'channel': 4, 'msg_id': 'oficina2', 'value': '180'}
print (Nombre_diccionario_1)
print (f"clave 2  {Nombre_diccionario_1['clave 2']}")
print (f"clave 2  {Nombre_diccionario_1.get('clave 2')}")# si no esta
print (f"clave 2  {Nombre_diccionario_1.get('clave 99')}")# si no esta
print (f"clave 6  {Nombre_diccionario_1['clave 6']}")
print (f"clave 5  {Nombre_diccionario_1['clave 5']}")
print (f"clave 7  {Nombre_diccionario_1['clave 7']}")
print (f"clave 1  {Nombre_diccionario_1['clave 1']}")
print (f"clave 1  {Nombre_diccionario_1.get('clave 100','no hay clave 100')}")
#################################################################
print (f"cantidad de datos(claves principales) en el dic : {len(Nombre_diccionario_1)}")
print (f"items : {Nombre_diccionario_1.items()}")
print ("*"*60)
print (f"llaves : {Nombre_diccionario_1.keys()}")
print ("*"*60)
print (f"valores : {Nombre_diccionario_1.values()}")
print ("*"*60)

pausa()
limpiar()#(2);
#################################################################
#Ejercicio_Diccionarios_Ej_03
print (f"Agregar")
print (Nombre_diccionario_1)
print (f"Agrego un conjunto en la posicion FINAL")
Nombre_diccionario_1["clave 11"]=["dato_asociado 11","dato_asociado 11,1","dato_asociado 11,2"]
print ("*"*60)
Nombre_diccionario_1["clave 12"]=("dato_asociado 12")
print (Nombre_diccionario_1)
print ("*"*60)
Nombre_diccionario_1["clave 120"]=["dato_asociado 120000"]
print (Nombre_diccionario_1)
print ("*"*60)
Nombre_diccionario_1["clave 12"]=("dato_asociado 12", "y 12 bis")
print (type(Nombre_diccionario_1["clave 12"]))

print (Nombre_diccionario_1)
print ("*"*60)
#Nombre_diccionario_1["clave 12"].append("otro")
#print (Nombre_diccionario_1)

pausa()
limpiar()#(3);
#################################################################
#Ejercicio_Diccionarios_Ej_04
print (f"Borrar")
print (Nombre_diccionario_1)
print ("*"*60)
print (f"delEteo o borro el dato 'clave 120'")
del Nombre_diccionario_1["clave 120"]
print (Nombre_diccionario_1)
print ("*"*60)
pausa()
limpiar()#(4);
#################################################################
#Ejercicio_Diccionarios_Ej_05
print (f"Reemplazar")
print (Nombre_diccionario_1)
print (f"cambio el dato asociado a la clave 9")
Nombre_diccionario_1["clave 9"]="dato_asociado 999"
print ("*"*60)
print (Nombre_diccionario_1)



pausa()
limpiar()#(5);
#################################################################
#Ejercicio_Diccionarios_Ej_06
ventas = {
            "Arroz":10,
            "Maiz":20,
            "Trigo":30,
            "Cebada":40,
            "Centeno":50,
            "Quinoa":60,
            "Avena":70,
            "Mijo":80
}
buscar_mayor = max (zip (ventas.values(), ventas. keys()))
print ("ventas Max",buscar_mayor)
buscar_menor = min (zip (ventas.values(), ventas. keys()))
print ("ventas Min",buscar_menor)

pausa()
limpiar()#(6);
#################################################################
#Ejercicio_Diccionarios_Ej_06
ventas_suc1 = {
            "Arroz":10,
            "Trigo":30,
            "Cebada":40,
            "Quinoa":60,
            "Mijo":80
}
ventas_suc2 = {
            "Maiz":20,
            "Trigo":30,
            "Cebada":43,
            "Centeno":50,
            "Avena":70,
}
print("ventas_suc1.keys() & ventas_suc2.keys()",ventas_suc1.keys() & ventas_suc2.keys())
print("ventas_suc1.keys() - ventas_suc2.keys()",ventas_suc1.keys() - ventas_suc2.keys())

print("ventas_suc1.items() & ventas_suc2.items()",ventas_suc1.items() & ventas_suc2.items())
pausa()
limpiar()#
pausa()
limpiar()#(5)
#################################################################
#Ejercicio_Diccionarios_Ej_06
nombreKey = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 10"]
nombreValue = ["columna 1","columna 2","columna 3","columna 4","columna 5","columna 6","columna 7","columna 8","columna 9","columna 10"]
print (f"de Arrays a diccionrios")
print (f"valores Array simples 1"+str(nombreKey))
print (f"valores Array simples 2"+str(nombreValue))

Nombre_diccionario_3 = {}
Nombre_diccionario_4 = {}

Nombre_diccionario_2 = {
                        nombreKey[0]:nombreValue[0],
                        nombreKey[1]:nombreValue[1],
                        nombreKey[2]:nombreValue[2],
                        nombreKey[3]:nombreValue[3],
                        nombreKey[4]:nombreValue[4],
                        nombreKey[5]:nombreValue[5],
                        nombreKey[6]:nombreValue[6],
                        nombreKey[7]:nombreValue[7],
                        nombreKey[8]:nombreValue[8],
                        nombreKey[9]:nombreValue[9],
                        }

nombreKeyInput = input ("Ingrese el key :")
nombreValueInput = input ("Ingrese el Value : ")
Nombre_diccionario_2[nombreKeyInput]=nombreValueInput


print (f"\ndiccionario hecho a mano:\t",Nombre_diccionario_2)

#                          o

for contador in range (len(nombreKey)):
        #Nombre_diccionario_2[nombreKey[0]        = nombreValue[contador[0]]
        Nombre_diccionario_3[nombreKey[contador]] = nombreValue[contador]


print (f"\ndiccionario hecho en un bucle:\t",Nombre_diccionario_3)


#list tuple set
Nombre_diccionario_4 = dict.fromkeys(nombreKey)

print (f"\ndiccionario hecho con fromkey:\t",Nombre_diccionario_4)
for contador,Key in enumerate(Nombre_diccionario_4):
        Nombre_diccionario_4[Key] = nombreValue[contador]
        #print (f"\nDatos:\t",Key,nombreValue[contador])
print (f"\ndiccionario hecho con fromkey:\t",Nombre_diccionario_4)

Nombre_diccionario_4 = {};

for clave, valor in zip(nombreKey, nombreValue):
    #print (f"\nDatos:\t",clave,valor)
    Nombre_diccionario_4[clave]=(valor)
print (f"\ndiccionario hecho con zip:\t",Nombre_diccionario_4)
del Nombre_diccionario_3, Nombre_diccionario_4
pausa()
limpiar()#(6);
#################################################################
#Ejercicio_Diccionarios_Ej_07

print("Repetimos varios Keys para generar una lista con sus valores")

nombreKey = ["linea 1","linea 1","linea 1","linea 2","linea 3","linea 3","linea 2","linea 3","linea 4","linea 5"]
nombreValue = ["valor 1 1","valor 1 2","valor 1 3","valor 2 1","valor 3 1","valor 3 2","valor 2 2","valor 3 3","valor 4 1","valor 5 1"]

Nombre_diccionario_4 = {}
for x, y in zip(nombreKey, nombreValue):
    Nombre_diccionario_4.setdefault(x, []).append(y)
print (f"\ndiccionario hecho con zip",Nombre_diccionario_4)


from collections import defaultdict
Nombre_diccionario_3 = defaultdict(list)
for clave, valor in zip(nombreKey, nombreValue):
    Nombre_diccionario_3[clave].append(valor)
Nombre_diccionario_3=dict(Nombre_diccionario_3)
print (f"\ndiccionario hecho con defaultdict:\t",Nombre_diccionario_3)

import itertools
Nombre_diccionario_4 = { k: [i[1] for i in g] for k,g in itertools.groupby(sorted(zip(nombreKey, nombreValue)), key=lambda x:x[0]) }

print (f"\ndiccionario hecho con itertools:\t",Nombre_diccionario_4)



import pandas as pd


Nombre_diccionario_4 = pd.DataFrame(columns=['Group', 'Value'], data=list(zip(nombreKey, nombreValue)))  # Create a dataframe
print (f"\ndiccionario hecho con itertools:\t",Nombre_diccionario_4)
del Nombre_diccionario_3, Nombre_diccionario_4

from itertools import chain
from collections import defaultdict
dict1 = {'bookA': 1, 'bookB': 2, 'bookC': 3}
dict2 = {'bookC': 2, 'bookD': 4, 'bookE': 5}
dict3 = defaultdict(list)
for k, v in chain(dict1.items(), dict2.items()):
    dict3[k].append(v)

for k, v in dict3.items():
    print(k, v)

pausa()
limpiar()#(7);
#################################################################
#Ejercicio_Diccionarios_Ej_08
Nombre_diccionario_1 = {1: ["Python", 33.2, 'UP'],
                 2: ["Java", 23.54, 'DOWN'],
                 3: ["Ruby", 17.22, 'UP'],
                 10: ["Lua", 10.55, 'DOWN'],
                 5: ["Groovy", 9.22, 'DOWN'],
                 6: ["C", 1.55, 'UP']
                 }

print ("{:<8} {:<15} {:<10} {:<10}".format('clave','Item_1','Item_2','Item_3'))
for clave_primaria,x in Nombre_diccionario_1.items():
    print (f"El ",clave_primaria)
    for clave_secundaria in Nombre_diccionario_1[clave_primaria]:
        print (f"\t\ttiene ",clave_secundaria,' ',Nombre_diccionario_1[clave_primaria])





pausa()
limpiar()#(8);
#################################################################
#Ejercicio_Diccionarios_Ej_09
# input stored in variable a.
diccionario = {"nombre":"Juan", "apellido":"Perez"}
# Use of format_map() function
print ("el apellido de  {nombre} es {apellido}".format_map(diccionario))
# input stored in variable a.
a = {"x":"alfa", "y":"beta"}
# Use of format_map() function
print ("{x} {y}".format_map(a))
pausa()
limpiar()#(9);
#################################################################
#Ejercicio_Diccionarios_Ej_010
Nombre_diccionario_1 = {"Primero": "wwww","Segundo":"xxxx","Tercero":"yyyy","Cuarto":"zzzz"}
for llaves in Nombre_diccionario_1:
    print (f"Clave : {llaves} , Valor : {Nombre_diccionario_1[llaves]}")
    if Nombre_diccionario_1[llaves] == "yyyy":
        print ("Encontrado el valor asociado {llaves}")
        print (f"con una clave {llaves}")



print (f"Este diccionario contiene las siguientes claves: ", " ".join(Nombre_diccionario_1))
print (f"Ordenamos por el largo del la clave ")
for llaves in sorted(Nombre_diccionario_1, key=len):
    print (llaves, Nombre_diccionario_1[llaves])
count = {}
for llaves in Nombre_diccionario_1:
    count[llaves] = count.get(llaves, 0) + 1

print (count)
del Nombre_diccionario_1
pausa()
limpiar()#(10);
#################################################################
#Ejercicio_Diccionarios_Ej_011
Nombre_diccionario_1 = {'Abuelo_A':{'Hijos':2,'Nietos':2},
                        'Abuelo_B':{'Hijos':3,'Nietos':1},
                        'Abuelo_C':{'Hijos':3,'Nietos':[1,2,3]},
                        'Abuelo_D':{'Hijos':3},
                        'Abuelo_E':{}
                        }
for clave_primaria in Nombre_diccionario_1:
    print (f"El ",clave_primaria)
    for clave_secundaria in Nombre_diccionario_1[clave_primaria]:
        print (f"\t\ttiene ",clave_secundaria,' ',Nombre_diccionario_1[clave_primaria][clave_secundaria])

print (f"--------------------------------------------------------------------------")
for clave_primaria, listas_valores_interiores in Nombre_diccionario_1.items():
    print(clave_primaria)
    for attribute, listas_valores_interiores in Nombre_diccionario_1[clave_primaria].items():
        print('\t{}\t :\t {}'.format(attribute, listas_valores_interiores))
del Nombre_diccionario_1
pausa()
limpiar()#(11);
#################################################################
#Ejercicio_Diccionarios_Ej_012

# Input dictionary}

print (f"transpongo el diccionario");
Nombre_diccionario_1 = {    "nombres":["Juan", "Pedro","Laura","Roxana","Alberto"],
                            "profesion":["Astronauta", "Biologo","Quimica","Fisica","Cocinero"],
                            "edad":[33, 55, 45, 25, 32] };

print (" Uso de la funcion format_map()");
print ("{nombres[0]} trabaja de {profesion[0]} y tiene {edad[0]} años.".format_map(Nombre_diccionario_1));
print ("{nombres[1]} trabaja de {profesion[1]} y tiene {edad[1]} años.".format_map(Nombre_diccionario_1));
print ("{nombres[2]} trabaja de {profesion[2]} y tiene {edad[2]} años.".format_map(Nombre_diccionario_1));
print ("{nombres[3]} trabaja de {profesion[3]} y tiene {edad[3]} años.".format_map(Nombre_diccionario_1));
print ("{nombres[4]} trabaja de {profesion[4]} y tiene {edad[4]} años.".format_map(Nombre_diccionario_1));


x =  'nombre' in Nombre_diccionario_1
print (f" Es 'nombre' clave del diccionario {x}")


pausa();limpiar();

print (f"--------------------------------------------------------------------------")
print ("{:<12} {:<15} {:<10} {:<10} {:<10} {:<10}".format('clave','Item_1','Item_2','Item_3', 'Item_4', 'Item_5'))
for clave_primaria, listas_valores_interiores in Nombre_diccionario_1.items():
    Item_1, Item_2, Item_3, Item_4, Item_5 = listas_valores_interiores;
    print ("{:<12} {:<15} {:<10} {:<10} {:<10} {:<10}".format(clave_primaria, Item_1, Item_2, Item_3, Item_4, Item_5))


pausa();limpiar();

datos = {clave_primaria:listas_valores_interiores for (clave_primaria,listas_valores_interiores) in Nombre_diccionario_1.items()}
print(datos)
pausa();limpiar();

for clave_primaria, listas_valores_interiores in Nombre_diccionario_1.items():
    for listas_valores_interiores in listas_valores_interiores :
        print(clave_primaria,listas_valores_interiores)
pausa();limpiar();
print (f"\n\n\nDatos del diccionario:",Nombre_diccionario_1)
print (f"\nLongitud del diccionario:",len(Nombre_diccionario_1))
print (f"\nItems del diccionario:",Nombre_diccionario_1.items())
print (f"\nLlaves del diccionario:",Nombre_diccionario_1.keys())
print (f"\nValores del diccionario",Nombre_diccionario_1.values())
pausa();limpiar();

claves_primarias= list(Nombre_diccionario_1.keys())
print (f"\n\n\n{claves_primarias[0]}")
for contador in range(5):
    print (f"sabes que {Nombre_diccionario_1[claves_primarias[0]][contador],}\t trabaja de {Nombre_diccionario_1[claves_primarias[1]][contador]}\t y tiene {Nombre_diccionario_1[claves_primarias[2]][contador]} años.")


pausa()
limpiar()#(8);
print (f"Uso de bucles anillados");
for cont_1 in Nombre_diccionario_1:
    print (f"\n",cont_1 ,end=("\t"));
    for cont_2 in Nombre_diccionario_1[cont_1]:
        print(cont_2 ,end=("\t"));
print (f"\n")
pausa();limpiar();
# Uso de pprint
import pprint
pprint.pprint(Nombre_diccionario_1, width=1)
pausa();limpiar();
# Uso de valor
for cont_1 in Nombre_diccionario_1:
    cont_2 = Nombre_diccionario_1[cont_1]
    print(cont_1,":",cont_2)
pausa();limpiar();
# Uso de format
for cont in Nombre_diccionario_1:
    print (f"Clave : {cont} , Valor : {Nombre_diccionario_1[cont]}")
pausa();limpiar();
# Uso de sorted
for row in zip(*([key] + (value) for key, value in sorted(Nombre_diccionario_1.items()))):
    print(*row)

for clave, valor in Nombre_diccionario_1.items():
    print(clave , ":",valor)
pausa();limpiar();
# Uso de json
import json
print(json.dumps(Nombre_diccionario_1, indent = 4))
pausa()
limpiar()#(9);
#################################################################
#Ejercicio_Diccionarios_Ej_013
import operator
Weight_details = {'Sam':45, 'Irum':67,'Dolly':80, 'Bela':20}
sorted_weight = sorted(Weight_details.items(), key=operator.itemgetter(1))
print(sorted_weight)
pausa()
limpiar()#(10);
#################################################################
#Ejercicio_Diccionarios_Ej_010

Nombre_diccionario_1 = {'Lorca':'Escritor', 'Goya':'Pintor', 'Beethoven':'Musico', 'Freddie Mercury':'Cantante', 'Pablo Picasso':'Pintor', 'Leonardo Da Vinci':'genio total'}
                                                                    # declara diccionario
print(Nombre_diccionario_1)                                         # imprime dic1{'Goya': 'Pintor', 'Lorca': 'Escritor'}
print(Nombre_diccionario_1['Lorca'])                                # escritor, acceso a un valor por clave
print(Nombre_diccionario_1.get('Gala', 'no existe'))                # acceso a un valor por clave
if 'Lorca' in Nombre_diccionario_1:
     print('Lorca está')                                            # comprueba si existe una clave
print(Nombre_diccionario_1.items())                                 # obtiene una lista de tuplas clave:valor
print(Nombre_diccionario_1.keys())                                  # obtiene una lista de las claves
print(Nombre_diccionario_1.values())                                # obtiene una lista de los valores
pausa();limpiar();
Nombre_diccionario_1['Lorca'] = 'Poeta'                             # añade un pausa()
limpiar()# par clave:valor
print(Nombre_diccionario_1.items())
pausa();limpiar();
Nombre_diccionario_1['Amenabar'] = 'Cineasta'                       # añade un pausa()
limpiar()# par clave:valor
print(Nombre_diccionario_1.items())
pausa();limpiar();
Nombre_diccionario_1.update({'Caravaggio' : 'Pintor','Salvador Dalí' : 'Pintor','Claude Monet' : 'Pintor'})
                                                                    # añadir con update()
print(Nombre_diccionario_1.items())                                 # obtiene una lista de tuplas clave:valor}

pausa();limpiar();
del Nombre_diccionario_1['Amenabar']                                # borra un par clave:valor
print(Nombre_diccionario_1.items())                                 # obtiene una lista de tuplas clave:valor
print(Nombre_diccionario_1.pop('Amenabar', 'Amenabar ya no está'))  # borra par clave:valor
del Nombre_diccionario_1
pausa();limpiar();

Nombre_diccionario_1 = dict((('Item_0',5), ('Item_1',10),('Item_2',15), ('Item_3',20),('Item_4',25), ('Item_5',30),('Item_6',35), ('Item_7',40),('Item_8',45),('Item_9',50), ('Item_0',55)))
                                                                                        # declara a partir de tupla
print(Nombre_diccionario_1)
del Nombre_diccionario_1
pausa();limpiar();
Nombre_diccionario_1 = dict(Item_0=5, Item_1=10,Item_2=15, Item_3=20,Item_4=25, Item_5=30,Item_6=35, Item_7=40, Item_8=45,Item_9=50, Item_10=55,)
                                                                                        # declara a partir de cadenas simples
print(Nombre_diccionario_1)
del Nombre_diccionario_1
pausa();limpiar();
Nombre_diccionario_1 = dict([(z, z**2) for z in (0,1, 2, 3, 4, 5, 6, 7, 8, 9)])         # declara a partir patrón
print(Nombre_diccionario_1)
del Nombre_diccionario_1
pausa();limpiar();
pausa()
limpiar()#(11);
#################################################################
#Ejercicio_Diccionarios_Ej_12
artistas = {'Lorca':'Escritor', 'Goya':'Pintor', 'Beethoven':'Musico', 'Freddie Mercury':'Cantante', 'Pablo Picasso':'Pintor', 'Leonardo Da Vinci':'genio total'}   # diccionario
Nombre_diccionario_1={}
for c, v in artistas.items():
    Nombre_diccionario_1[c] = v
    print(Nombre_diccionario_1)
del Nombre_diccionario_1
pausa();limpiar();

paises = ['Chile','España','Francia','Portugal']    # declara lista
Nombre_diccionario_2={}
for i, c in enumerate(paises):
    Nombre_diccionario_2[i] = c                     # recorre lista
    print(Nombre_diccionario_2)
del Nombre_diccionario_2
pausa();limpiar();

capitales = ['Santiago','Madrid','París','Lisboa']  # declara lista
paises = ['Chile','España','Francia','Portugal']    # declara lista
Nombre_diccionario_3={}
for p, c in zip(paises, capitales):
    Nombre_diccionario_3[p] = c                     # recorre listas
    print(Nombre_diccionario_3)

gente = ['33','44','55','44']
capitales = ['Santiago','Madrid','París','Lisboa']  # declara lista
paises = ['Chile','España','Francia','Portugal']    # declara lista
Nombre_diccionario_3={}
for p, c ,g in zip(paises, capitales, gente):
    print(p, c ,g )
    Nombre_diccionario_3[p] = [c,g]                     # recorre listas
print(Nombre_diccionario_3)
del Nombre_diccionario_3
pausa()
limpiar()#(12);
#################################################################
artistas = {'Lorca':'Escritor', 'Goya':'Pintor', 'Beethoven':'Musico', 'Freddie Mercury':'Cantante', 'Pablo Picasso':'Pintor', 'Leonardo Da Vinci':'genio total'}   # diccionario
print(artistas)
print(artistas["Lorca"])
try:
    print(artistas["Sabato"])#da error xq no esta
except Exception as dato_error:
    print (f"Ocurrió un error o excepción // Exeception occured:{dato_error}")
print (f"Sabato : ",artistas.get("Sabato", "Un grande pero no esta en el dic"))

print (f"Borges : ",artistas.setdefault("Borges", "Genio Nacional"))
print(artistas)
pausa()
limpiar()#(13,"fin");
#################################################################
'''
def filter(ciudad, provincia, fecha_alta):
    return (f"SELECT * FROM clientes WHERE ciudad='{ciudad}' AND provincia='{provincia}' AND fecha_alta={fecha_alta}")
print("Formato kwargs")

def filter(**kwargs):
    query = "SELECT * FROM clientes"
    i = 0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE "
        else:
            query += " AND "
        query += "{}='{}'".format(key, value)
        i += 1
    query += ";"
    return query
    '''
#################################################################

pausa();limpiar();
print("""\033[1;37;44m\
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                            combinar Dictionarios                            ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""")
datos1 ={'Sam':45, 'Irum':67,'Dolly':80, 'Bela':20}
datos2 ={'Pepe':45, 'Luis':67,'Ana':80, 'Tito':20}
datos = {**datos1,**datos2}
print (f"{datos = }")



#################################################################

pausa();limpiar();
print("""\033[1;37;44m\
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                            Sort Dictionary by keys()                        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""")
datos ={'Sam':45, 'Irum':67,'Dolly':80, 'Bela':20}


print (f"{datos = }")
datos =sorted(datos.items())

print (f"ordenado por keys{datos = }")

#################################################################

pausa();limpiar();
print("""\033[1;37;44m\
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                            Sort Dictionary by values()    ¿reveer?          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""")
datos ={'Sam':45, 'Irum':67,'Dolly':80, 'Bela':20}
print (f"{datos = }")
datos = sorted(datos.items(),key = lambda val : val[1] )

print (f"ordenado por values{datos = }")
#################################################################
pausa();limpiar();
print("""\033[1;37;44m\
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                            diccionarios en  listas                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""")

claves=["Nombre","Apellido","direccion"]
dicc = {clave:valor + 1 for valor,clave in enumerate(claves)}
print (dicc)
#################################################################


import pickle
pausa();limpiar();
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                            diccionarios en  archivo                         ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""")

claves=["Nombre","Apellido","direccion"]
lista=[]
dic={}
seguir=True
while (seguir):
    dic={}
    for C in claves:
        dic[C]=input(f"Ingrese su {C} :")
    lista.append(dic)
    seguir=input("Continuar 0")
print (dic)
print (lista)
pausa()
print("Guardo los objetos en disco la lista")
with open("lista.pickle", "wb") as f:
    pickle.dump(lista, f)
pausa()
print("Borro la lista")
del lista
try:
    print (lista)
except:
    print("Lista de objetos no existe")
pausa()

print("Leo los objetos en disco la lista")

with open("lista.pickle", "rb") as f:
    lista = pickle.load(f)

for dicc in lista:
    print (dicc)
    for cont_1 in dicc:
        cont_2 = dicc[cont_1]
        print(cont_1,":",cont_2)
    # Uso de format
    for cont in dicc:
        print (f"Clave : {cont} , Valor : {dicc[cont]}")

'''


CADENA_KIOSKO_XX={
                    suc1:
                        {
                             caramelos:{24},
                             CHUPETINES {98}
                             alfajores:{34  },
                             chocolates:{87 },

                         }
                    suc2:
                        {
                            caramelos:{42},
                            alfajores:{ 3},
                            chocolates:{4 },
                            CHUPETINES {43}
                        }
                    suc3:
                        {
                            alfajores:{4    },
                            chocolates:{43 },
                            CHUPETINES {434}
                        }
                }


[caramelos, chupetines, alfajores,  chocolates]
[suc1 ,suc2, suc3]
}
                        }
[24,    34, 87, 98,
  42,   3,  4,  43,,
234,    4,  43, 434]


'''




















