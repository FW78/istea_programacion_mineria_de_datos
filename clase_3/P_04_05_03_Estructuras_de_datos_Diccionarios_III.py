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

dic={}
dic={0:[1,2,3,4,5],1:[6,7,8,9,10],2:[11,12,13,14,15]}
print ("dic:",dic)
print ("                alias")
l0=dic[0]
l1=dic[1]
l2=dic[2]
print (l0,l1,l2)
l1=[9,9,9,9,9]
print(f"{dic=}")
print (l0,l1,l2)
dic[1]=l1


print(f"{dic=}")
pausa()
limpiar()
#################################################################
print("*"*35)
import json
from datetime import date, time, datetime


'''
                verificar que exista Est.json


'''



def leer_json(jsonFile):
    with open(f"{jsonFile}.json" ,"r") as objeto_json:
        dic_py_memoria = json.load(objeto_json)
    return dic_py_memoria
#dic_py_memoria = leer_json("data2")


def grabar_json (nombre_archivo, **diccionario_Tipo):
    with open(f"{nombre_archivo}.json", "w") as obj_json:
        json.dump(diccionario_Tipo, obj_json, indent=4)

dic_Estac={}

ahora=datetime.now()
fechaEntrada = ahora.strftime('%Y-%m-%dT%H:%M:%S.%f')
print ("entrada:",fechaEntrada,type(fechaEntrada))
jsonFile="Est"
dic_Estac["A"]={"ENTRADA": fechaEntrada, "SALIDA": ""}
print(f"{dic_Estac=}")
pausa()
limpiar()
#################################################################
print("*"*35)
dic_Estac = leer_json(jsonFile)
fechaSalida=datetime.now()
nfechaEntrada= datetime.strptime(dic_Estac["A"]["ENTRADA"], '%Y-%m-%dT%H:%M:%S.%f')
print ("nueva-entrada:",nfechaEntrada,type(nfechaEntrada))
diferencia = fechaSalida - nfechaEntrada
print (f"\t\t{diferencia.days} dias")

horas=diferencia.seconds//3600
print (f"\t\t{horas} horas")
minut=diferencia.seconds//60 -horas*60
print (f"\t\t{minut} minutos")

pausa()
limpiar()
#################################################################
print("*"*35)
Id_ = [54, 65, 76]
nombres = ["Juan", "Pedro", "Maria"]
itemDictionary = dict(zip(Id_, nombres))

print(f"{itemDictionary=}")
pausa()
limpiar()
#################################################################
