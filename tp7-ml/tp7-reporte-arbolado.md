**Nombres y Legajos:**

Pérez Eduardo, 13244

Pérez Carlos, 13245

**TP 7 – Desafío**

**A)**

**1-)** Se eliminaron las variables: “ultima\_modificación”, “area\_sección”, “seccion” y “nombre\_seccion” de los sets.

**2-)** Se creó la variable “ratio” corresponde a el ratio de árboles con inclinación peligrosa por especie de árbol.

**3-)** No se normalizaron variables ya existentes, pero la variable creada ratio está normalizada ya que solo toma valores entre 0 y 1.

**B-)** No se utilizó set de validación.

**C-)** La puntuación obtenida en Kaggle fue de 0.71628

**D-)** Se utilizo el algoritmo de Random Forest con 600 árboles de decisión para predecir la variable “inclinacion\_peligrosa” utilizando como referencia los valores de las siguientes variables:

**Ratio:** nos dice que tan propenso es a tener una inclinación peligrosa según su especie.

**Lat** y **Long:** ya que si un árbol esta en condiciones de inclinación peligrosa, es probable que arboles cercanos estén en las mismas condiciones.

**Diámetro\_tronco:** para tener una medida de las dimensiones del árbol.

Para el set de entrenamiento, se tomó el archivo de entrenamiento del desafío, se dividió en los árboles que tienen inclinación peligrosa y los que no, luego se tomó una partición de los que no tienen inclinación peligros que mantuviera una distribución de especies igual al set original de no peligrosos y que tuviera la misma cantidad de elementos que los arboles peligrosos, para que así se asemeje mas al set que se usa de test que tiene una distribución del 50/50.




