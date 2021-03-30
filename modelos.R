datos_codificados <- function(data,y){
  require(dplyr)
  #mutate(loan=replace(loan, loan=="no", 0)) %>%
  #mutate(loan=replace(loan, loan=="yes", 1))
  
  Y <- data %>% select(y)  
  X <- data %>% select(-(y))
  X_int <- X  %>% select_if(is.integer)
  X_cat <- dummy_cols(X %>% select_if(is.character),remove_selected_columns = T)
  datos <- cbind(X_int,X_cat,Y)
  
  return(datos)
}

library(MASS)
library(pscl)

# Modelo poisson

glm(hijos~ ., family="poisson", data=datos)

# Modelo Binomial Negativo

glm.nb(hijos ~ ., data = datos)

# Modelo Zero-inflated Poisson regression

zeroinfl(hijos ~ . | ., data = datos)

# Modelo Zero-inflated Binomial Negativa regression

zeroinfl(hijos ~ . | ., data = datos, dist = "negbin", EM = TRUE)
