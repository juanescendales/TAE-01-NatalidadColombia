# Queremos clasificar si un hogar tiene hujos o no

# Sea T: Si el hogar tiene hijos 
# Sea N: Si el hogar no tiene hijos

library(pROC)
library(caret)

datos_model_p_clasificar <- datos_modelo_p
datos_model_p_clasificar$Hijos[datos_model_p_clasificar$Hijos!=0] <- "T"
datos_model_p_clasificar$Hijos[datos_model_p_clasificar$Hijos==0] <- "N"

split <- createDataPartition(datos_model_p_clasificar$Hijos,times=1,p=0.75,list=F)

Y <- datos_model_p_clasificar %>% select(Hijos)
X <- datos_model_p_clasificar %>% select(-(Hijos))

X_int <- scale(X  %>% select(Edad.Jefe,Edad.Conyuge,Ingresos.totales))
X_cat <- X %>% select(-c(Edad.Jefe,Edad.Conyuge,Ingresos.totales))

datos_knn <- cbind(X_int,Y)
datos_knn$Hijos <- as.factor(datos_knn$Hijos)
training <- datos_knn[split,]
testing <- datos_knn[-split,]


# Modelos de clasificación
ctrl <- trainControl(method="repeatedcv",repeats = 3)
modelo_knn <- train(Hijos~.,data=training,method = "knn",tuneGrid   = expand.grid(k = 1:10))
best_modelo_knn <- train(Hijos~.,data=training,method = "knn",tuneGrid = data.frame(k=8))
