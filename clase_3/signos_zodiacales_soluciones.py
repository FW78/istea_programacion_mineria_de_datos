from datetime import datetime,date
import os
import datetime

def pausa():
    input("\tPresione ENTER para continuar")

def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')


{"Capricornio:" "Inicio":" 22 de diciembre" ,
"Fin":"20 de enero",
"Acuario:" "Inicio":" 21 de enero" ,
"Fin":"18 de febrero",
"Piscis:" "Inicio":" 19 de febrero" ,
"Fin":"20 de marzo",
"Aries:" "Inicio":" 21 de marzo" ,
"Fin":"20 de abril",
"Tauro:" "Inicio":" 21 de abril" ,
"Fin":"21 de mayo",
"Géminis:" "Inicio":" 22 de mayo" ,
"Fin":"21 de junio",
"Cáncer:" "Inicio":" 22 de junio" ,
"Fin":"22 de julio",
"Leo:" "Inicio":" 23 de julio" ,
"Fin":"23 de agosto",
"Virgo:" "Inicio":" 24 de agosto" ,
"Fin":"23 de septiembre",
"Libra:" "Inicio":" 24 de septiembre" ,
"Fin":"23 de octubre",
"Escorpión:" "Inicio":" 24 de octubre" ,
"Fin":"22 de noviembre",
"Sagitario:" "Inicio":" 23 de noviembre" ,
"Fin":"21 de diciembre"}

zodiacal =  {
            "Capricornio":  ((22,12),(20,1)),
            "Acuario":      ((21,1), (19,2)),
            "Piscis":       ((20,2) ,(20,3)),
            "Aries":        ((21,3), (20,4)),
            "Tauro":        ((21,4), (21,5)),
            "Géminis":      ((22,5), (21,6)),
            "Cáncer":       ((22,6), (22,7)),
            "Leo":          ((23,7), (23,8)),
            "Virgo":        ((24,8), (23,9)),
            "Libra":        ((24,9), (23,10)),
            "Escorpión":    ((24,10),(22,11)),
            "Sagitario":    ((23,11),(21,12))
            }

zodiacalc = {
            "mono":0,
            "pollo":1,
            "perro":2,
            "cerdo":3,
            "rata":4,
            "buey":5,
            "tigre":6,
            "conejo":7,
            "dragon":8,
            "serpiente":9,
            "caballo":10,
            "oveja":11
            }

año = 1979
dia = 29
mes = 12

for signo,valor in zodiacal.items():

    if (valor[0][1] == mes and valor[0][0]<= dia) or (valor[1][1] == mes and valor[1][0]>= dia):

        print(signo)

# ~ for animal,valor in zodiacalc.items():

    # ~ if año % 12 == valor:

        # ~ print(animal,año % 12)



# ~ if mes == 12:

    # ~ if dia >= 22:

        # ~ print("capricornio")

    # ~ else:

# ~ pausa()

# ~ ingreso = ["","",""]












# ~ print(type())

def crear_fecha():

    while True:

        limpiar()
        ingreso = input("Ingrese su fecha de nacimiento [DD/MM/AAAA]: ").strip().replace(" ","/").replace("-","/").split("/")

        print(ingreso)
        print(type(ingreso))


        try:

            fecha = date(
                            year =  int(ingreso[2]),
                            month = int(ingreso[1]),
                            day =   int(ingreso[0])
                        )
            break

        except:

            limpiar()
            print(f"Error al ingresar la fecha [{ingreso}]")
            pausa()

    return(fecha)

tipo = date.today()

if isinstance(tipo,date):

    fecha = crear_fecha()


print(fecha.day,fecha.month)
print (type(fecha))



# ~ today = datetime.date.today()
# ~ now = datetime.datetime.now()

# ~ isinstance(today, datetime.datetime)
# ~ >>> False

# ~ isinstance(now, datetime.datetime)
# ~ >>> True

# ~ isinstance(now, datetime.date)
# ~ >>> True

# ~ isinstance(now, datetime.datetime)
# ~ >>> True


# ~ "DD/MM/AAA" -----> ["DD","MM","AAAA"]






# ~ texto = "el murciegalo come fruta"


# ~ print(texto)

# ~ buscar = ""

# ~ print(buscar in texto)


