import csv

pathArchivo = '../DatosCSV/Caracteristicas y composicion del hogar.csv'

nombreCabecera = "P6088"

# Leemos el csv para ser usado posteriormente
archivoOriginalCaracCompHogar = open(
    pathArchivo, 'r')

# Leo los datos del archivo csv
datacsv = csv.reader(archivoOriginalCaracCompHogar, delimiter=';')

# Cabecera del archivo
cabecera = next(datacsv)

print(cabecera.index(nombreCabecera))

# Luego de leer y procesar el archivo, lo cerramos
archivoOriginalCaracCompHogar.close()
