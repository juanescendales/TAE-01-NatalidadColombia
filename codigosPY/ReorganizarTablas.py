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
datosFila = ['', '', '', '', '', '', '', '', '', '', '', '', '', '']

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
                         '', '', '', '', '', '', '', '']

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
# Quito el -# para ser usado en otras tablas
pattern = '[^-]*'
identificador = re.match(pattern, identificador).group()
# Itero las filas, obteniendo sus columnas
for cols in datacsvTrabajo:
    identificadorRow = cols[0] + "-" + cols[2]
    cols[3]
    datosNuevos[index][2]
    datosNuevos[index][4]
    while(identificadorRow == identificador and index < len(datosNuevos)):
        if (index < len(datosNuevos)):
            datosNuevos[index][12] = cols[17]
            datosNuevos[index][13] = cols[17]

        index += 1
        if (index < len(datosNuevos)):
            identificador = re.match(pattern, datosNuevos[index][0]).group()


# Luego de leer y procesar el archivo, lo cerramos
archivoOriginalTrabajo.close()

# Creamos un archivo nuevo donde almacenamos el resultado
archivoNuevo = open('../DatosCSVProcesados/Datos.csv', 'w', newline='')

# Dispongo el archivo para escribir datos en el
csvwriter = csv.writer(archivoNuevo, delimiter=';')

# Creo una nueva cabecera para la información procesada
cabeceraNueva = ['Codigo', 'Hijos', 'Secuencia Jefe',
                 'Sexo Jefe', 'Secuencia Conyuge', 'Sexo Conyuge', 'Tipo Union', 'Edad Jefe', 'Edad Conyuge', 'Region', 'Energia', 'Estrato vivienda', 'Trabajo Jefe', 'Trabajo conyuge']

# writing the fields
csvwriter.writerow(cabeceraNueva)

# writing the data rows
csvwriter.writerows(datosNuevos)


# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()
