# Libreria csv para trabajar con archivos csv
import csv


# Leemos el csv para ser usado posteriormente
archivoOriginal = open(
    '../DatosCSV/Caracteristicas y composicion del hogar.csv', 'r')

# Leo los datos del archivo csv
datacsv = csv.reader(archivoOriginal, delimiter=';')

# Cabecera del archivo
cabecera = next(datacsv)

identificador = ''
hijos = 0
datosNuevos = []

# Itero las filas, obteniendo sus columnas
for cols in datacsv:
    identificadorRow = cols[0] + "-" + cols[2]
    if(identificador != identificadorRow):
        # Condicional por primera iteracion para no contar el espacio blanco
        if(identificador != ''):
            datosNuevos.append([identificador, hijos])

        hijos = 0
        identificador = identificadorRow
    else:
        if(cols[9] == '3'):
            hijos += 1

# Para agregar la ultima fila, por como se codifica se pierde el ultimo dato
datosNuevos.append([identificador, hijos])

# Luego de leer y procesar el archivo, lo cerramos
archivoOriginal.close()

# Creamos un archivo nuevo donde almacenamos el resultado
archivoNuevo = open('../DatosCSVProcesados/hijos.csv', 'w', newline='')

# Dispongo el archivo para escribir datos en el
csvwriter = csv.writer(archivoNuevo, delimiter=';')

# Creo una nueva cabecera para la información procesada
cabeceraNueva = ['Codigo', 'Hijos']

# writing the fields
csvwriter.writerow(cabeceraNueva)

# writing the data rows
csvwriter.writerows(datosNuevos)


# Luego de guardar todos los datos en el archivo cerramos y guardamos el archivo
archivoNuevo.close()
