'''
    File name: TablaUsoEnergeticos.py
    Author: Alejandro Jimenez Franco
    Date created: 05/04/2021
    Date last modified: 05/04/2021
    Python Version: 3.7
'''

import csv
import numpy
import random

# Función para procesar los datos de los datos de uso energeticos del hogar
# cols[5] = dato P5510
# cols[36] = dato P5018
# cols[37] = dato P5018S1


def datosUsoEnergeticos(datos):

    # Leemos el csv para ser usado posteriormente
    archivoOriginalUsoEnergeticos = open(
        '../DatosCSV/Uso de energeticos del hogar.csv', 'r')

    # Leo los datos del archivo csv
    datacsvUsoEnergetico = csv.reader(
        archivoOriginalUsoEnergeticos, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvUsoEnergetico)

    # Sacamos los valores para posteriormente rellenar datos faltantes o en 0
    datosTransformar = []

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvUsoEnergetico:

        # valor de la electricidad
        if(cols[37] != ' '):
            datosTransformar.append(int(int(cols[36])/int(cols[37])))

    np = numpy.array(datosTransformar)

    # media de los datos
    media = int(np.mean())

    # desviacion estandar de los datos
    std = int(np.std())

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalUsoEnergeticos.close()

    # Este proceso se hace dos veces para leer los datos y sacar la media y desviacion para despues

    # Leemos el csv para ser usado posteriormente
    archivoOriginalUsoEnergeticos = open(
        '../DatosCSV/Uso de energeticos del hogar.csv', 'r')

    # Leo los datos del archivo csv
    datacsvUsoEnergetico = csv.reader(
        archivoOriginalUsoEnergeticos, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvUsoEnergetico)

    index = 0
    identificador = datos[0][0]

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvUsoEnergetico:

        # Identificador directorio-orden
        identificadorRow = cols[0] + "-" + cols[3]

        if(datos[index][0] == identificadorRow):

            # si el valor de la electicidad es vacio vamos a darle un valor random entre la media +- la desviacion estandar
            if(cols[37] != ' '):
                datos[index][22] = int(int(cols[36])/int(cols[37]))
            else:
                n = random.randint(media-std, media+std)
                if (n < 0):
                    datos[index][22] = 0
                else:
                    datos[index][22] = n

            # N usos de la lavadora si es vacio lo hacemos 0
            if(cols[5] != ' '):
                datos[index][23] = cols[5]
            else:
                datos[index][23] = 0
        index += 1

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalUsoEnergeticos.close()
