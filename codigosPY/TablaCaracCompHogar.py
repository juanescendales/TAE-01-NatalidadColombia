import csv

# Función para procesar los datos de los datos de Caracteristicas y composicion del hogar
# cols[0] + "-" + cols[2] = dato Directorio-Orden(Secuencia P)
# cols[3] = dato ORDEN
# cols[6] = dato P6020
# cols[8] = dato P6040
# cols[9] = dato P6051
# cols[10] = dato P5502


def datosCaracCompHogar(datos):

    # Leemos el csv para ser usado posteriormente
    archivoOriginalCaracCompHogar = open(
        '../DatosCSV/Caracteristicas y composicion del hogar.csv', 'r')

    # Leo los datos del archivo csv
    datacsv = csv.reader(archivoOriginalCaracCompHogar, delimiter=';')

    # Cabecera del archivo
    cabecera = next(datacsv)

    # Identificar directorio-orden
    identificador = ''

    # N hijos
    hijos = 0

    # Creo un arreglo del tamaño de las columnas de mis nuevos datos, para facilidad
    datosFila = ['', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    # Itero las filas, obteniendo sus columnas
    for cols in datacsv:

        # Identificar directorio-orden
        identificadorRow = cols[0] + "-" + cols[2]

        if(identificador != identificadorRow):

            # Condicional por primera iteracion para no contar el espacio blanco
            if(identificador != ''):

                # Identificar directorio-orden
                datosFila[0] = identificador

                # hijos
                datosFila[1] = hijos

                datos.append(datosFila)
                datosFila = ['', '', '', '', '', '',
                             '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

            hijos = 0
            identificador = identificadorRow

        # Dependiendo del tipo de dato jefe del hogar, conyuge o hijo obtengo ciertos datos
        if(cols[9] == '1'):

            # Secuencia
            datosFila[2] = cols[3]

            # Sexo Jefe
            datosFila[3] = cols[6]

            # Tipo union
            datosFila[6] = cols[10]

            # Edad Jefe
            datosFila[7] = cols[8]

        elif(cols[9] == '2'):

            # Secuencia
            datosFila[4] = cols[3]

            # Sexo Jefe
            datosFila[5] = cols[6]

            # Edad Jefe
            datosFila[8] = cols[8]

        if(cols[9] == '3'):
            # Conteo hijos
            hijos += 1

    # Para agregar la ultima fila, por como se codifica se pierde el ultimo dato

    # Identificar directorio-orden
    datosFila[0] = identificador

    # hijos
    datosFila[1] = hijos

    datos.append(datosFila)

    # Luego de leer y procesar el archivo, lo cerramos
    archivoOriginalCaracCompHogar.close()
