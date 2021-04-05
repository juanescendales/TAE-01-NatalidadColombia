import csv

# Función para procesar los datos de los datos de Vivienda
# cols[3] = dato ORDEN
# cols[5] = dato P6240


def datosTrabajo(datos):
    # Leemos el csv Vivienda para ser usado posteriormente
    archivoOriginalTrabajo = open(
        '../DatosCSV/Fuerza de trabajo.csv', 'r')

    # Leo los datos del archivo csv de Vivienda
    datacsvTrabajo = csv.reader(archivoOriginalTrabajo, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvTrabajo)

    index = 0
    identificador = datos[0][0]

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvTrabajo:

        # Identificador directorio-orden
        identificadorRow = cols[0] + "-" + cols[2]

        if(identificador != identificadorRow):
            identificador = identificadorRow
            index += 1

        # Asigno al Jefe y conyuge el trabajo que desempeña
        if(datos[index][2] == cols[3]):
            datos[index][12] = cols[5]
        elif(datos[index][4] == cols[3]):
            datos[index][13] = cols[5]

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalTrabajo.close()
