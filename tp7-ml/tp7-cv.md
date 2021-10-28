**Nombres y Legajos:**

Pérez Eduardo, 13244

Pérez Carlos, 13245

**TP 7 – Machine Learning**

**Cross Validation**

\```{r}

set.seed(2021)

#EJERCICIO 7

#crea los dobles y guarda los indices de los elmentos de esas particiones en listas y guarda esas listas en una lista y la devuelve 

create\_folds <- function(dataframe, Nfolds){

`  `LonFolds <- ceiling(nrow(dataframe)/Nfolds)

`  `Lista <- list()

`  `folds <- split(dataframe[1], sample(rep(1:Nfolds,LonFolds)))



`  `for (x in 1:Nfolds){

`      `Lista <- append(Lista, c(folds[x]))

`  `}

`  `return(Lista)

}

#utiliza los dobles creado por la funcion anterior y hace el cross validation con arboles de decision, para esto agarra un doble y lo utiliza como testeo usando el resto como entrenamiento, hace los mismo con cada uno de los dobles, usando el algoritmo de arbol de decision n veces, n siendo el numero de dobles

cross\_validation <- function(dataframe, Nfolds){

`  `folds <- create\_folds(dataframe, Nfolds)

`  `#crea listas para guardar las metricas correspondientes en cada bucle de arvol de decision 

`  `ListAccu <- c()

`  `ListPrec <- c()

`  `ListSens <- c()

`  `ListSpec <- c()



`  `#bucle for para el cross validation

`  `for (x in 1:Nfolds){

`    `train <- dataframe[-unlist(folds[x]),]

`    `validation <- dataframe[unlist(folds[x]),]



`    `train <-train %>% mutate(inclinacion\_peligrosa=ifelse(inclinacion\_peligrosa=='1','si','no'))

`    `train$inclinacion\_peligrosa <-as.factor(train$inclinacion\_peligrosa)



`    `validation <- validation %>% mutate(inclinacion\_peligrosa=ifelse(inclinacion\_peligrosa=='1','si','no'))

`    `validation$inclinacion\_peligrosa <-as.factor(validation$inclinacion\_peligrosa)



`    `train\_formula <- formula(inclinacion\_peligrosa~ altura + circ\_tronco\_cm + lat + long)

`    `tree\_model <- rpart(train\_formula, train)



`    `prediction <- predict(tree\_model, validation, type='prob')

`    `prediction\_normal <- ifelse(prediction[,2] >=0.5,'si','no')

`    `resultados\_validation<-data.frame(inclinacion\_peligrosa=prediction\_normal)



`    `#Toma las metricas de la matriz de consunsion y la guarda en las listas

`    `Matriz <- confusionMatrix(as.factor(resultados\_validation$inclinacion\_peligrosa), as.factor(validation$inclinacion\_peligrosa))

`    `ListAccu <- append(ListAccu, Matriz$overall["Accuracy"])

`    `ListPrec <- append(ListPrec, Matriz$byClass["Precision"])

`    `ListSens <- append(ListSens, Matriz$byClass["Sensitivity"])

`    `ListSpec <- append(ListSpec, Matriz$byClass["Specifitivy"])

`  `}

`  `#calcula las medias y derivadas estandar de las metricas y las imprime

`  `print("Medias:")

`  `print("Accuracy: ")

`  `print(mean(ListAccu))



`  `print("Precision: ")

`  `print(mean(ListPrec))



`  `print("Sensitivity: ")

`  `print(mean(ListSens))



`  `print("Specifitivy: ")

`  `print(mean(ListSpec))



`  `print("")



`  `print("Desviaciones Estandar: ")

`  `print("Accuracy: ")

`  `print(sd(ListAccu))



`  `print("Precision: ")

`  `print(sd(ListPrec))



`  `print("Sensitivity: ")

`  `print(sd(ListSens))



`  `print("Specifitivy: ")

`  `print(sd(ListSpec))



}

cross\_validation(dataset\_trees,10)

\```



||Media|Desviación estándar |
| :-: | :-: | :-: |
|Accuracy|0.8879128|0.008067727|
|Precision|0.8879128|0.008067727|
|Sensitivity|1|0|
|Specifitivy|0|0|

