import csv
import numpy
import random

# Función para procesar los datos de los datos de Servicios del hogar
# cols[4] = dato P5000
# cols[5] = dato P5010
# cols[58] = dato I_HOGAR
# cols[62] = dato CANT_PERSONAS_HOGAR


def datosSHogar(datos):

    # Leemos el csv para ser usado posteriormente
    archivoOriginalSHogar = open(
        '../DatosCSV/Servicios del hogar.csv', 'r')

    # Leo los datos del archivo csv
    datacsvSHogar = csv.reader(archivoOriginalSHogar, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvSHogar)

    # Sacamos los valores para posteriormente rellenar datos faltantes o en 0
    datosTransformar = []

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvSHogar:

        # Ingreso total del hogar
        n = cols[58].split(",")
        if(int(n[0]) > 0):
            datosTransformar.append(int(n[0]))

    np = numpy.array(datosTransformar)

    # media de los datos
    media = int(np.mean())

    # desviacion estandar de los datos
    std = int(np.std())

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalSHogar.close()

    # Este proceso se hace dos veces para leer los datos y sacar la media y desviacion para despues

    # Leemos el csv para ser usado posteriormente
    archivoOriginalSHogar = open(
        '../DatosCSV/Servicios del hogar.csv', 'r')

    # Leo los datos del archivo csv
    datacsvSHogar = csv.reader(archivoOriginalSHogar, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsvSHogar)

    index = 0
    identificador = datos[0][0]

    # Itero las filas, obteniendo sus columnas
    for cols in datacsvSHogar:
        # Identificar directorio-orden
        identificadorRow = cols[0] + "-" + cols[3]

        if(datos[index][0] == identificadorRow):

            # Cantidad personas en el hogar
            datos[index][10] = cols[62]

            # Ingreso total del hogar
            n = cols[58].split(",")

            num = int(n[0])

            # si el ingreso es 0 vamos a darle un valor random entre la media +- la desviacion estandar
            if(num == 0):
                n = random.randint(media-std, media+std)
                if (n < 0):
                    datos[index][14] = 0
                else:
                    datos[index][14] = n

            else:
                datos[index][14] = num

            # N cuartos
            datos[index][20] = cols[4]

            # N cuartos dormir
            datos[index][21] = cols[5]

        index += 1

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalSHogar.close()
