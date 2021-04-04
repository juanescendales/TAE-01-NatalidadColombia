# Libreria csv para trabajar con archivos csv
import csv
import re
import numpy
import random
from TablaSalud import datosSalud
from TablaCaracCompHogar import datosCaracCompHogar
from TablaSHogar import datosSHogar
from TablaUsoEnergeticos import datosUsoEnergeticos
from TablaVivienda import datosVivienda
from TablaFuerzaTrabajo import datosTrabajo
from TablaTecnologia import datosTecnologia
from TablaEducacion import datosEducacion

# Creo una nueva cabecera para la información procesada
cabeceraNueva = ['Codigo', 'Hijos', 'Secuencia Jefe', 'Sexo Jefe', 'Secuencia Conyuge',
                 'Sexo Conyuge', 'Tipo Union', 'Edad Jefe', 'Edad Conyuge', 'Region',
                 'Cantidad de personas', 'Estrato vivienda', 'Trabajo Jefe', 'Trabajo conyuge',
                 'Ingresos totales', 'Uso tecnologia Jefe', 'Uso tecnologia conyuge',
                 'Edu Jefe', 'Edu Conyuge', 'Afiliacion salud', 'N cuartos', 'N cuartos dormir',
                 'Valor Electricidad', 'N usos Lavadora']

""" Indices columna
0 Codigo
1 Hijos
2 Secuencia Jefe
3 Sexo Jefe
4 Secuencia Conyuge
5 Sexo Conyuge
6 Tipo Union
7 Edad Jefe
8 Edad Conyuge
9 Region
10 Cantidad de personas
11 Estrato vivienda
12 Trabajo Jefe
13 Trabajo conyuge
14 Ingresos totales
15 Uso tecnologia Jefe
16 Uso tecnologia conyuge
17 Edu Jefe
18 Edu Conyuge
19 Afiliacion salud
20 N cuartos
21 N cuartos dormir
22 Valor Electricidad
23 N usos Lavadora
"""

# Donde almacenaremos todos nuestros datos
datosNuevos = []

# Obtenemos los datos utiles de Caracteristicas y composicion del hogar
datosCaracCompHogar(datosNuevos)

# Obtenemos los datos utiles de Salud
datosSalud(datosNuevos)

# Obtenemos los datos utiles de Servicios del hogar
datosSHogar(datosNuevos)

# Obtenemos los datos utiles de Usos energeticos del hogar
datosUsoEnergeticos(datosNuevos)

# Obtenemos los datos utiles de Vivienda
datosVivienda(datosNuevos)

# Obtenemos los datos de Fuerza de Trabajo
datosTrabajo(datosNuevos)

# Obtenemos los datos de Uso de tecnolgia
datosTecnologia(datosNuevos)

# Obtenemos los datos de Educacion
datosEducacion(datosNuevos)

# Filtrar datos por condicion
datosFiltrados = []

# Filtro los datos de estrato si es 9 que no sabe el estrato y nos sirve esos datos y los de estrato vacio
# Filtro por las personas que no tienen una afiliacion en salud el Jefe del hogar
for dato in datosNuevos:
    if(dato[11] != '9' and dato[11] != ' ' and dato[19] != '9'):
        # Elimino la columna de secuencia Conyuge
        dato.pop(4)
        # Elimino la columna de secuencia Jefe
        dato.pop(2)

        datosFiltrados.append(dato)

# Filtrar datos por condicion
datosFiltradosPareja = []
datosFiltradosSolo = []

# Datos separados
for dato in datosFiltrados:

    # Si la informacion de conyuge es vacia separo los datos entre parejas en el hogar y solteros
    if(dato[3] != ''):
        datosFiltradosPareja.append(dato)
    else:

        datos = dato.copy()

        # Elimino la columna de Edu Conyuge
        datos.pop(16)

        # Elimino la columna de Uso tecnologia conyuge
        datos.pop(14)

        # Elimino la columna de Trabajo conyuge
        datos.pop(11)

        # Elimino la columna de Edad Conyuge
        datos.pop(6)

        # Elimino la columna de Sexo Conyuge
        datos.pop(3)

        datosFiltradosSolo.append(datos)

# Creo una nueva cabecera para la información procesada
cabeceraNueva = ['Codigo', 'Hijos', 'Sexo Jefe', 'Sexo Conyuge', 'Tipo Union', 'Edad Jefe',
                 'Edad Conyuge', 'Region', 'Cantidad de personas', 'Estrato vivienda', 'Trabajo Jefe',
                 'Trabajo conyuge', 'Ingresos totales', 'Uso tecnologia Jefe', 'Uso tecnologia conyuge',
                 'Edu Jefe', 'Edu Conyuge', 'Afiliacion salud', 'N cuartos', 'N cuartos dormir',
                 'Valor Electricidad', 'N usos Lavadora']


# Creamos un archivo nuevo donde almacenamos el resultado
archivoNuevo = open(
    '../DatosCSVProcesados/DatosCompletosING.csv', 'w', newline='')

# Dispongo el archivo para escribir datos en el
csvwriter = csv.writer(archivoNuevo, delimiter=';')

# Escribo la cabecera
csvwriter.writerow(cabeceraNueva)

# Escribo los datos
csvwriter.writerows(datosFiltrados)

# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()

# Creamos un archivo nuevo donde almacenamos el resultado
archivoNuevo = open(
    '../DatosCSVProcesados/DatosParejaING.csv', 'w', newline='')

# Dispongo el archivo para escribir datos en el
csvwriter = csv.writer(archivoNuevo, delimiter=';')

# Escribo la cabecera
csvwriter.writerow(cabeceraNueva)

# Escribo los datos
csvwriter.writerows(datosFiltradosPareja)

# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()

# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()

# Creo una nueva cabecera para la información procesada
cabeceraNueva = ['Codigo', 'Hijos', 'Sexo Jefe', 'Tipo Union', 'Edad Jefe',
                 'Region', 'Cantidad de personas', 'Estrato vivienda', 'Trabajo Jefe',
                 'Ingresos totales', 'Uso tecnologia Jefe',
                 'Edu Jefe', 'Afiliacion salud', 'N cuartos', 'N cuartos dormir',
                 'Valor Electricidad', 'N usos Lavadora']

# Creamos un archivo nuevo donde almacenamos el resultado
archivoNuevo = open(
    '../DatosCSVProcesados/DatosSolteroING.csv', 'w', newline='')

# Dispongo el archivo para escribir datos en el
csvwriter = csv.writer(archivoNuevo, delimiter=';')

# Escribo la cabecera
csvwriter.writerow(cabeceraNueva)

# Escribo los datos
csvwriter.writerows(datosFiltradosSolo)

# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()
