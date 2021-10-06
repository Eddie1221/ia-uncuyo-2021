**Alumno:** Eduardo Pérez

**Legajo:** 13244

**CSP**

**1-)** 

**Variables:** {Las casillas de la grilla 9x9}

**Dominio:** {1,2,3,4,5,6,7,8,9}

**Restricciones:**

-Las casillas de las filas deben tener valores distintos.

-Las casillas de las columnas deben tener valores distintos.

-Las casillas de los 9 cuadrados 3x3 deben tener valores distintos

**2-)** Empezamos con la asignación parcial que nos da el problema

![](Aspose.Words.7f216151-f765-4824-af0d-46cf3762f5f9.001.png)

|WA|NT|Q|NSW|V|SA|T|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|R|R V A|R V A|R V A|A|R V A|R V A|

Por arco de consistencia de NT -> WA y SA -> WA se elimina rojo en ambas para mantener la consistencia, Y por arco de consistencia de NSW -> V y SA -> V, se elimina azul de ambas.

|WA|NT|Q|NSW|V|SA|T|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|R|V A|R V A|R V|A|V|R V A|


Por arco de consistencia Q -> SA, NT -> SA y NSW -> SA se elimina verde de las 3.

|WA|NT|Q|NSW|V|SA|T|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|R|A|R A|R|A|V|R V A|

Por arco de consistencia Q -> NT y Q -> NSW se elimina Rojo y Azul de Q, dejando Q sin valores posibles.

|WA|NT|Q|NSW|V|SA|T|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|R|A||R|A|V|R V A|
Por lo que no es una solución consistente, demostrando así que se puede detectar la inconsistencia de la solución parcial {WA = Rojo, V = Azul} utilizando arco de consistencia.

**3-)** El peor caso del AC-3 es O(n^2\*d^3), ya que un grafo de restricciones puede tener hasta n^2 arcos (siendo n el número de variables) que se pueden encolar d veces cada uno, verificando la consistencia de cada arco a una complejidad de O(d^2), pero al ser un árbol sabemos que tiene n-1 arcos, por lo que quedaría con una complejidad temporal en el peor caso de O((n-1) \*d^2), que se simplifica a **O(n\*d^2)**.

**4-)** Si cada vez que se suprime un posible valor de Xi se tiene que encolar nuevamente el arco (Xk,Xi) entonces cada arco se puede añadir un máximo de d veces, si preprocesamos las restricciones del problema para, tal que un valor de Xi, se conoce cuáles son los valores de Xk que conforman el arco de consistencia con ese valor de Xi, podría hacerse la comprobación de consistencia de un arco en O(d), dejando la complejidad temporal del problema en O(n^2\*d^2).

**5-)** 

1) Para esto probaremos que se puede resolver un CSP con un grafo de restricciones estructurado por árbol, para ello se siguen los siguientes pasos:
1) Se elige cualquier variable como raíz y se ordena de modo que el padre de cada nodo lo preceda en el orden.
1) Para todas las variable se aplica consistencia de arco (Xi,Xj) donde Xi es el padre de Xj, quitando los valores del dominio según sea corresponda.
1) Para j desde 1 hasta n, se asigna cualquier valor de Xj consistente con el valor asignado d a su padre.

Después del paso 2, el CSP tiene 2-consistencia, por lo que la asignación del paso 3 no requiere ninguna vuelta atrás, y aplicando la comprobación de consistencia de arco en orden inverso al paso 2, nos aseguramos de que cualquier valor suprimido no afecte la consistencia de los arcos que ya han sido tratados, asegurando la n-consistencia.

1) Ya que todos los CSP para árboles estructurados se pueden ordenar del modo explicado, y comprobando la consistencia de arco en el orden mostrado asegura que el problema se podrá resolver ya que se garantiza la n-consistencia.








**6-)** Resultados de las ejecuciones con 4, 8, 10 ,12 y 15 reinas (los resultados siguen este mismo orden):

**Backtracking:**

-Tiempos de ejecución: [0.0, 0.01795172691345215, 0.17852330207824707, 0.151594877243042, 1.0132980346679688]

`	`Gráfico de cajas:

![](Aspose.Words.7f216151-f765-4824-af0d-46cf3762f5f9.002.png)

-Estados recorridos: [4, 73, 347, 161, 520]

`	`Gráfico de cajas:

![](Aspose.Words.7f216151-f765-4824-af0d-46cf3762f5f9.003.png)

**Forward Checking:**

-Tiempos de ejecución: [0.0, 0.0, 0.001993894577026367, 0.0009965896606445312, 0.005009651184082031]

`	`Gráfico de cajas:

![](Aspose.Words.7f216151-f765-4824-af0d-46cf3762f5f9.004.png)

-Estados recorridos: [4, 32, 146, 87, 299]

`	`Gráfico de cajas:

![](Aspose.Words.7f216151-f765-4824-af0d-46cf3762f5f9.005.png)
