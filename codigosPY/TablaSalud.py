'''
    File name: TablaSalud.py
    Author: Alejandro Jimenez Franco
    Date created: 05/04/2021
    Date last modified: 05/04/2021
    Python Version: 3.7
'''

import csv

# Función para procesar los datos de los datos de Salud
# cols[94] = dato P5694
# cols[4] = dato P6090


def datosSalud(datos):
    # Leemos el csv para ser usado posteriormente
    archivoOriginalSalud = open(
        '../DatosCSV/Salud.csv', 'r')

    # Leo los datos del archivo csv
    datacsvSalud = csv.reader(archivoOriginalSalud, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvSalud)

    index = 0
    identificador = datos[0][0]

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvSalud:

        # Identificar directorio-orden
        identificadorRow = cols[0] + "-" + cols[2]

        if(identificador != identificadorRow):
            identificador = identificadorRow
            index += 1

        # Añado los hijos de madres en embarazo
        if(datos[index][0] == identificadorRow and (datos[index][2] == cols[3] or datos[index][4] == cols[3])):
            if(cols[94] == '1' or cols[94] == '2'):
                datos[index][1] += 1

        # Afiliación en salud
        if(cols[3] == '1'):
            datos[index][19] = cols[4]

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalSalud.close()
