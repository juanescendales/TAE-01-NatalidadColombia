# Libreria csv para trabajar con archivos csv
import csv
import re

# Leemos el csv para ser usado posteriormente
archivoOriginalCaracCompHogar = open(
    '../DatosCSV/Caracteristicas y composicion del hogar.csv', 'r')

# Leo los datos del archivo csv
datacsv = csv.reader(archivoOriginalCaracCompHogar, delimiter=';')

# Cabecera del archivo
cabecera = next(datacsv)

identificador = ''
hijos = 0
datosNuevos = []
datosFila = ['', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '', '']

# Creo una nueva cabecera para la información procesada
cabeceraNueva = ['Codigo', 'Hijos', 'Secuencia Jefe', 'Sexo Jefe', 'Secuencia Conyuge',
                 'Sexo Conyuge', 'Tipo Union', 'Edad Jefe', 'Edad Conyuge', 'Region',
                 'Energia', 'Estrato vivienda', 'Trabajo Jefe', 'Trabajo conyuge',
                 'Ingresos totales', 'Uso tecnologia Jefe', 'Uso tecnologia conyuge',
                 'Edu Jefe', 'Edu Conyuge']

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
10 Energia
11 Estrato vivienda
12 Trabajo Jefe
13 Trabajo conyuge
14 Ingresos totales
15 Uso tecnologia Jefe
16 Uso tecnologia conyuge
17 Edu Jefe
18 Edu Conyuge
"""

# funciones utiles


def sumaIngresos(cols):
    ingresos = 0
    if (cols[25] != ' '):
        ingresos += int(cols[25])
    if (cols[35] != ' '):
        ingresos += int(cols[35])
    if (cols[37] != ' '):
        ingresos += int(cols[37])
    if (cols[39] != ' '):
        ingresos += int(cols[39])
    if (cols[41] != ' '):
        ingresos += int(cols[41])
    if (cols[53] != ' '):
        ingresos += int(cols[53])
    if (cols[76] != ' '):
        ingresos += int(cols[76])
    if (cols[81] != ' '):
        ingresos += int(cols[81])
    if (cols[86] != ' '):
        ingresos += int(cols[86])
    if (cols[88] != ' '):
        ingresos += int(cols[88])
    if (cols[90] != ' '):
        ingresos += int(cols[90])
    ingresosDiv = 0
    if (cols[44] != ' '):
        ingresosDiv += int(cols[44])
    if (cols[46] != ' '):
        ingresosDiv += int(cols[46])
    if (cols[48] != ' '):
        ingresosDiv += int(cols[48])
    if (cols[50] != ' '):
        ingresosDiv += int(cols[50])
    if (cols[52] != ' '):
        ingresosDiv += int(cols[52])
    if (cols[54] != ' '):
        ingresosDiv += int(cols[54])
    if (cols[92] != ' '):
        ingresosDiv += int(cols[92])
    if (cols[95] != ' '):
        ingresosDiv += int(cols[95])
    if (cols[97] != ' '):
        ingresosDiv += int(cols[97])
    if (cols[99] != ' '):
        ingresosDiv += int(cols[99])
    ingresos += int(ingresosDiv/12)

    # print(ingresos)
    return ingresos


# Itero las filas, obteniendo sus columnas
for cols in datacsv:
    identificadorRow = cols[0] + "-" + cols[2]

    if(identificador != identificadorRow):
        # Condicional por primera iteracion para no contar el espacio blanco
        if(identificador != ''):
            datosFila[0] = identificador
            datosFila[1] = hijos
            datosNuevos.append(datosFila)
            datosFila = ['', '', '', '', '', '',
                         '', '', '', '', '', '', '', '', '', '', '', '', '']

        hijos = 0
        identificador = identificadorRow

    if(cols[9] == '1'):
        datosFila[2] = cols[3]
        datosFila[3] = cols[6]
        datosFila[6] = cols[10]
        datosFila[7] = cols[8]
    elif(cols[9] == '2'):
        datosFila[4] = cols[3]
        datosFila[5] = cols[6]
        datosFila[8] = cols[8]
    if(cols[9] == '3'):
        hijos += 1


# Para agregar la ultima fila, por como se codifica se pierde el ultimo dato

datosFila[0] = identificador
datosFila[1] = hijos
datosNuevos.append(datosFila)
# Luego de leer y procesar el archivo, lo cerramos
archivoOriginalCaracCompHogar.close()


# Leemos el csv Salud para ser usado posteriormente
archivoOriginalSalud = open(
    '../DatosCSV/Salud.csv', 'r')

# Leo los datos del archivo csv de Salud
datacsvSalud = csv.reader(archivoOriginalSalud, delimiter=';')

# Cabecera del archivo
cabecera = next(datacsvSalud)
# print(cabecera[94])

index = 0
identificador = datosNuevos[0][0]

# Itero las filas, obteniendo sus columnas
for cols in datacsvSalud:
    identificadorRow = cols[0] + "-" + cols[2]
    if(datosNuevos[index][0] == identificadorRow and (datosNuevos[index][2] == cols[3] or datosNuevos[index][4] == cols[3])):
        if(cols[94] == '1' or cols[94] == '2'):
            datosNuevos[index][1] += 1

    if(identificador != identificadorRow):
        identificador = identificadorRow
        index += 1


# Luego de leer y procesar el archivo, lo cerramos
archivoOriginalSalud.close()

# Leemos el csv Vivienda para ser usado posteriormente
archivoOriginalVivienda = open(
    '../DatosCSV/Datos de la vivienda.csv', 'r')

# Leo los datos del archivo csv de Vivienda
datacsvVivienda = csv.reader(archivoOriginalVivienda, delimiter=';')

# Cabecera del archivo
cabecera = next(datacsvVivienda)


index = 0
identificador = datosNuevos[0][0]
# Quito el -# para ser usado en otras tablas
pattern = '[^-]*'
identificador = re.match(pattern, identificador).group()
# Itero las filas, obteniendo sus columnas
for cols in datacsvVivienda:
    identificadorRow = cols[0]

    while(identificadorRow == identificador and index < len(datosNuevos)):
        if (index < len(datosNuevos)):
            datosNuevos[index][9] = cols[4]
            datosNuevos[index][10] = cols[14]
            datosNuevos[index][11] = cols[15]

        index += 1
        if (index < len(datosNuevos)):
            identificador = re.match(pattern, datosNuevos[index][0]).group()


# Luego de leer y procesar el archivo, lo cerramos
archivoOriginalVivienda.close()

# Leemos el csv Vivienda para ser usado posteriormente
archivoOriginalTrabajo = open(
    '../DatosCSV/Fuerza de trabajo.csv', 'r')

# Leo los datos del archivo csv de Vivienda
datacsvTrabajo = csv.reader(archivoOriginalTrabajo, delimiter=';')

# Cabecera del archivo
cabecera = next(datacsvTrabajo)

index = 0
identificador = datosNuevos[0][0]
ingresos = 0

# Itero las filas, obteniendo sus columnas
for cols in datacsvTrabajo:
    identificadorRow = cols[0] + "-" + cols[2]

    if(identificador != identificadorRow):
        datosNuevos[index][14] = ingresos
        identificador = identificadorRow
        index += 1
        ingresos = 0

    if(datosNuevos[index][2] == cols[3]):
        datosNuevos[index][12] = cols[5]
        ingresos += sumaIngresos(cols)
    elif(datosNuevos[index][4] == cols[3]):
        datosNuevos[index][13] = cols[5]
        ingresos += sumaIngresos(cols)

datosNuevos[index][14] = ingresos

# Luego de leer y procesar el archivo, lo cerramos
archivoOriginalTrabajo.close()

# Leemos el csv Vivienda para ser usado posteriormente
archivoOriginalTecnologia = open(
    '../DatosCSV/Tecnologias de informacion y comunicacion.csv', 'r')

# Leo los datos del archivo csv de Vivienda
datacsvTecnologia = csv.reader(archivoOriginalTecnologia, delimiter=';')

# Cabecera del archivo
cabecera = next(datacsvTecnologia)

index = 0
identificador = datosNuevos[0][0]

# Itero las filas, obteniendo sus columnas
for cols in datacsvTecnologia:
    identificadorRow = cols[0] + "-" + cols[2]

    if(identificador != identificadorRow):
        identificador = identificadorRow
        index += 1

    if(datosNuevos[index][2] == cols[3]):
        if(cols[17] == '5'):
            datosNuevos[index][15] = 0
        elif(cols[17] == '1' or cols[17] == '2'):
            datosNuevos[index][15] = 2
        else:
            datosNuevos[index][15] = 1
    elif(datosNuevos[index][4] == cols[3]):
        if(cols[17] == '5'):
            datosNuevos[index][16] = 0
        elif(cols[17] == '1' or cols[17] == '2'):
            datosNuevos[index][16] = 2
        else:
            datosNuevos[index][16] = 1


# Luego de leer y procesar el archivo, lo cerramos
archivoOriginalTecnologia.close()


# Leemos el csv Vivienda para ser usado posteriormente
archivoOriginalEducacion = open(
    '../DatosCSV/Educacion.csv', 'r')

# Leo los datos del archivo csv de Vivienda
datacsvEducacion = csv.reader(archivoOriginalEducacion, delimiter=';')

# Cabecera del archivo
cabecera = next(datacsvEducacion)

index = 0
identificador = datosNuevos[0][0]

# Itero las filas, obteniendo sus columnas
for cols in datacsvEducacion:
    identificadorRow = cols[0] + "-" + cols[2]

    if(identificador != identificadorRow):
        identificador = identificadorRow
        index += 1

    if(datosNuevos[index][2] == cols[3]):
        if(cols[7] == '1'):
            datosNuevos[index][17] = 0
        elif(cols[7] == '2' or cols[7] == '3' or cols[7] == '4' or cols[7] == '5'):
            datosNuevos[index][17] = 1
        elif(cols[7] == '6' or cols[7] == '8' or cols[7] == '10'):
            datosNuevos[index][17] = 2
        else:
            datosNuevos[index][17] = 3

    elif(datosNuevos[index][4] == cols[3]):
        if(cols[7] == '1'):
            datosNuevos[index][18] = 0
        elif(cols[7] == '2' or cols[7] == '3' or cols[7] == '4' or cols[7] == '5'):
            datosNuevos[index][18] = 1
        elif(cols[7] == '6' or cols[7] == '8' or cols[7] == '10'):
            datosNuevos[index][18] = 2
        else:
            datosNuevos[index][18] = 3


# Luego de leer y procesar el archivo, lo cerramos
archivoOriginalEducacion.close()


# Filtrar datos por condicion
datosFiltrados = []

# Filtro 9
for dato in datosNuevos:
    if(dato[11] != '9'):
        datosFiltrados.append(dato)

# Filtrar datos por condicion
datosFiltradosPareja = []
datosFiltradosSolo = []

# Datos separados
for dato in datosFiltrados:
    if(dato[4] != ''):
        datosFiltradosPareja.append(dato)
    else:
        datosFiltradosSolo.append(dato)

# Creamos un archivo nuevo donde almacenamos el resultado
archivoNuevo = open(
    '../DatosCSVProcesados/DatosCompletosING.csv', 'w', newline='')

# Dispongo el archivo para escribir datos en el
csvwriter = csv.writer(archivoNuevo, delimiter=';')

# writing the fields
csvwriter.writerow(cabeceraNueva)

# writing the data rows
csvwriter.writerows(datosFiltrados)


# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()


# Creamos un archivo nuevo donde almacenamos el resultado
archivoNuevo = open(
    '../DatosCSVProcesados/DatosParejaING.csv', 'w', newline='')

# Dispongo el archivo para escribir datos en el
csvwriter = csv.writer(archivoNuevo, delimiter=';')

# writing the fields
csvwriter.writerow(cabeceraNueva)

# writing the data rows
csvwriter.writerows(datosFiltradosPareja)


# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()

# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()


# Creamos un archivo nuevo donde almacenamos el resultado
archivoNuevo = open(
    '../DatosCSVProcesados/DatosSolteroING.csv', 'w', newline='')

# Dispongo el archivo para escribir datos en el
csvwriter = csv.writer(archivoNuevo, delimiter=';')

# writing the fields
csvwriter.writerow(cabeceraNueva)

# writing the data rows
csvwriter.writerows(datosFiltradosSolo)


# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()
