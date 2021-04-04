import csv

# Función para procesar los datos de Tecnologias de informacion y comunicacion
# cols[3] = ORDEN (secuencia)
# cols[17] = dato P1084


def datosTecnologia(datos):

    # Leemos el csv Vivienda para ser usado posteriormente
    archivoOriginalTecnologia = open(
        '../DatosCSV/Tecnologias de informacion y comunicacion.csv', 'r')

    # Leo los datos del archivo csv de Vivienda
    datacsvTecnologia = csv.reader(archivoOriginalTecnologia, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvTecnologia)

    index = 0
    identificador = datos[0][0]

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvTecnologia:

        # Identificador directorio-orden
        identificadorRow = cols[0] + "-" + cols[2]

        if(identificador != identificadorRow):
            identificador = identificadorRow
            index += 1

        # Reinterpreto el uso de tecnolgia de Jefe y Conyuge
        # 0 no uso, 1 uso poco 2 mucho uso
        if(datos[index][2] == cols[3]):
            if(cols[17] == '5'):
                datos[index][15] = 0
            elif(cols[17] == '1' or cols[17] == '2'):
                datos[index][15] = 2
            else:
                datos[index][15] = 1
        elif(datos[index][4] == cols[3]):
            if(cols[17] == '5'):
                datos[index][16] = 0
            elif(cols[17] == '1' or cols[17] == '2'):
                datos[index][16] = 2
            else:
                datos[index][16] = 1

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalTecnologia.close()
