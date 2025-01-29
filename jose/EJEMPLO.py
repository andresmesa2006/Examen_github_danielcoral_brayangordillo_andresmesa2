#ARCHIVOS


#son para guardar la informacion del usuario (informacion ya creada)
# ------------    # si solo esta este  /  r,w,x,a,b,W       /////        en esta árte se vuelve un objeto con una clase FILE (clasificaciones)
# ---OPEN-----    # queda modo lectura /
#------------open("nombre de archivo", / "modo de lectura") ///// #---username = open("nombre de archivo", / "modo de lectura")
#
# r: para leer el archivo
# w: escribir
# x: crearlo y falla si ya existe
# a: abre el archivo modo escritura pero lo que se meta nueva va al final de la linea
# b: abrir archivo modo binario "01011010"
# W: abrir modod escritura pero sobre escribre, es decir borra todo lo que ya estaba (en python 3.10 es diferente)



#---Escronor em im archivo, va a contener la informacion que queremos guardar, 
#---archivo.write("hola mundo")

archivo = open("ejemplo_arch.txt","a") #a ---o ----w
archivo.write("mi primera linea.5 ") #o append si se pone un print se devuelve el numero de carracterers
archivo.close()

archivo = open("ejemplo_arch.txt","r")
print(archivo.read())
archivo.close()

#ARCHIVOS CSV
#COMO LISTAS PERO GUARDA DATOS DEL USUARIO Y SE MODIFICAN SE USAN PARA PROCESOS FINIACIEROS

data = []
from csv import reader, writer, DictReader, DictWriter
with open("personas.csv", "r") as file:
    lector = reader(file)                #------------------------------------
    print(lector)                        #--------ESTO LEE UNA LISTA---------->#EN UN  ARCHIVO CREADO
    for row in lector:                   #----------------DE------------------
        data.append(row)                 #--------------LISTAS----------------  
print(data)                              #------------------------------------


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#------------------------------------
#--------ESCRITURA DE DATOS--------------->#EN UN NUEVO ARCHIVO 
#------------------------------------
from csv import reader, writer, DictReader, DictWriter
dAata = [
    ["NOMBRE","APELLIDO","GRADO"],
    ["FARUT","CADENA","2"],
    ["ANDRES","SUAREZ","2"],
    ["ALEJANDRO","CADENA","1"]
]


myFile = open("personas.csv", "w", newline= '')

with myFile:
    escritor = writer(myFile)
    escritor.writerows(dAata)

                        #tipo de archivo  /   data        /  encabezados ---parametros
def write_reservations(f, reservations, headers):
    with open(f,"w", newline='') as f2:
        writer = DictWriter(f2,  fieldnames = headers )
        if header:
            writer.writeheader()
        for reservation in reservations:
            writer.writerow({
                'availability_zone': reservation["availability_zone"],
                'tenancy': reservation["tenancy"],
                'product': reservation["product"],
                'cost_hourly': reservation["cost_hourly"],
                'cost_upfront': reservation["cost_upfront"],
                'count': reservation["count"],
                'count_used': reservation["count_used"],
            })



#encabezados primera linea del archivo 
header = [
        'availability_zone',
        'tenancy',
        'product',
        'cost_hourly',
        'cost_upfront',
        'count',
        'count_used',
        ]

reservations = [
            {"availability_zone" : 2,
                 "tenancy": 3,
                 'product': 1,
                 'cost_hourly': 3500,
                 'cost_upfront':  4800,
                 "count": 45,
                 "count_used":1
            },{"availability_zone" : 3,
                 "tenancy": 3,
                 'product': 4,
                 'cost_hourly': 3700,
                 'cost_upfront':  5800,
                 "count": 25,
                 "count_used":13
            }]




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#ARCHIVOS JSON 
#COMO UN DICCIONARIO EN ESTRUCTURA 


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#importar json
import json
#abrir y leer un json file
'''

'''
#GUARDAR UN ARCHIVO JSON
dicctionary = [
    { 
        "table": 12,
        "chair": 14,
        "id": 567
        },{
        "table": 44,
        "chair": 10,
        "id": 56
    }
]
# Pasamos el diccionario a objeto tipo json
things = json.dumps(dicctionary)


# usamos open para abrir el archivo o para generarlo si no existe y abrirlo
file =  open("things.json", "w") 


# Escribimos sobre todo el archivo
file.write(things)


# Cerramos el archivo
file.close()



