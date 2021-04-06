'''
    File name: TablaVivienda.py
    Author: Alejandro Jimenez Franco
    Date created: 05/04/2021
    Date last modified: 05/04/2021
    Python Version: 3.7
'''

import csv
import re

# Función para procesar los datos de los datos de Vivienda
# cols[4] = dato REGION
# cols[15] = dato P8520S1A1


def datosVivienda(datos):

    # Leemos el csv Vivienda para ser usado posteriormente
    archivoOriginalVivienda = open(
        '../DatosCSV/Datos de la vivienda.csv', 'r')

    # Leo los datos del archivo csv de Vivienda
    datacsvVivienda = csv.reader(archivoOriginalVivienda, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvVivienda)

    index = 0
    identificador = datos[0][0]

    # Quito el -# para ser usado en otras tablas
    pattern = '[^-]*'
    identificador = re.match(pattern, identificador).group()

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvVivienda:

        # Identificador
        identificadorRow = cols[0]

        while(identificadorRow == identificador and index < len(datos)):
            if (index < len(datos)):
                # Region
                datos[index][9] = cols[4]

                # Estrato
                datos[index][11] = cols[15]

            index += 1
            if (index < len(datos)):
                identificador = re.match(
                    pattern, datos[index][0]).group()

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalVivienda.close()
