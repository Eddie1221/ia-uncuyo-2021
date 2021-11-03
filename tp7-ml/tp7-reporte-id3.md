**Nombres y Legajos:**

Eduardo Pérez, 13244

Carlos Pérez, 13245

**PARTE C)**

1) **Resultados de la evaluación del algoritmo sobre el dataset tennis.csv**

![image](https://user-images.githubusercontent.com/88392382/140009259-dee18948-8068-4824-81be-2390ba5b6583.png)


2) Un árbol de decisión maneja variables de tipo real (o variables continuas) en 2 casos:

**Si hay variables continuas en los atributos de entrada:**

Para manejar esto, en lugar de crear ramas para los valores específicos que puede tomar la variable, los árboles de decisión se ramifican en intervalos de infinitos valores reales donde se pueden clasificar dichas variables continuas según el intervalo donde pertenecen.

**Si la salida del árbol una variable continua:**

En estos casos se utiliza un árbol de regresión, en este algoritmo, el intervalo de la variable de salida se divide en subintervalos, donde cada hoja se del árbol corresponde a uno de esos subintervalos, cuando termina de recorrer el árbol por cualquiera de sus caminos, el algoritmo calcula la salida como la media de todos lo valores que tomaron los ejemplos en el conjunto de entrenamiento que pertenezcan al subintervalo correspondiente con la hoja. 
