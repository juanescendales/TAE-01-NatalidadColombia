datos_iniciales <- read.csv2("./TAE-01-NatalidadColombia/DatosCSVProcesados/hijos.csv")
barplot(table(datos_iniciales$Hijos))
        