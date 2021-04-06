#
# Rellenar
#
# Autor: Juan Esteban Cendales Sora
# Técnicas en Aprendizaje Estadístico - Semestre 01 2021
# Universidad Nacional de Colombia
#


library(tidyr)
library(rlang)
library(dplyr)
library(caret)
modelo <- readRDS("./src/modelos/knn_modelo_final.rds")

validar_columnas <- function(df, columns){
  resultado = list(valido = TRUE, mensaje = "Cumple con todos los nombres de columnas")
  if (!is.data.frame(df)) {
    resultado$valido = FALSE
    resultado$mensaje = "No es un dataframe"
  }
  else if(!all(i <- rlang::has_name(df,columns))){
    resultado$valido = FALSE
    resultado$mensaje = paste("No tiene las columnas necesarias: ",paste(columns[!i], collapse=", "))
  }
  return(resultado)
   
}


generar_prediccion <- function(datos){
  #Los datos deben ser un dataframe con las columnas indicadas
  resultado <- list(prediccion = NULL, mensaje = "")
  validacion <- validar_columnas(datos,c("Edad.Jefe","Cantidad.de.personas","Ingresos.totales","Valor.Electricidad","Sexo.Jefe","Tipo.Union","Trabajo.Jefe","Uso.tecnologia.Jefe","Edu.Jefe"))
  resultado$mensaje <- validacion$mensaje
  if(validacion$valido){
    
    variables_categoricas <- datos %>% 
      select(Sexo.Jefe,Tipo.Union,Trabajo.Jefe,Uso.tecnologia.Jefe,Edu.Jefe) %>% 
      mutate_if(is.numeric,as.factor)
    
    variables_numericas <- datos %>% 
      select(c(Edad.Jefe,Cantidad.de.personas,Ingresos.totales,Valor.Electricidad))
    
    datos_codificados <- as.data.frame(cbind(variables_numericas,variables_categoricas))
    prediccion <- predict(modelo,datos_codificados)
    redondeo<- round(prediccion)
    resultado$prediccion = redondeo;
  }
  
  return(resultado)
}

#ejemplo = data.frame(list(Sexo.Jefe= 1,Tipo.Union = 2,Trabajo.Jefe = 1,Uso.tecnologia.Jefe = 0,Edu.Jefe = 1,Edad.Jefe = 44,Cantidad.de.personas = 5,Ingresos.totales = 1800000,Valor.Electricidad = 60000))
#prediccion <- generar_prediccion(ejemplo)
