import csv

# Función para procesar los datos de Educacion
# cols[3] = ORDEN (secuencia)
# cols[7] = dato P8587


def datosEducacion(datos):

    # Leemos el csv Vivienda para ser usado posteriormente
    archivoOriginalEducacion = open(
        '../DatosCSV/Educacion.csv', 'r')

    # Leo los datos del archivo csv de Vivienda
    datacsvEducacion = csv.reader(archivoOriginalEducacion, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvEducacion)

    index = 0
    identificador = datos[0][0]

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvEducacion:

        # Identificador directorio-orden
        identificadorRow = cols[0] + "-" + cols[2]

        if(identificador != identificadorRow):
            identificador = identificadorRow
            index += 1

        # Reinterpreto el tipo de educacion de Jefe y Conyuge
        # 0 No estudio, 1 Educacion basica, 2 Educacion profesional no completa, 3 Educacion profesional
        if(datos[index][2] == cols[3]):
            if(cols[7] == '1'):
                datos[index][17] = 0
            elif(cols[7] == '2' or cols[7] == '3' or cols[7] == '4' or cols[7] == '5'):
                datos[index][17] = 1
            elif(cols[7] == '6' or cols[7] == '8' or cols[7] == '10'):
                datos[index][17] = 2
            else:
                datos[index][17] = 3

        elif(datos[index][4] == cols[3]):
            if(cols[7] == '1'):
                datos[index][18] = 0
            elif(cols[7] == '2' or cols[7] == '3' or cols[7] == '4' or cols[7] == '5'):
                datos[index][18] = 1
            elif(cols[7] == '6' or cols[7] == '8' or cols[7] == '10'):
                datos[index][18] = 2
            else:
                datos[index][18] = 3

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalEducacion.close()
