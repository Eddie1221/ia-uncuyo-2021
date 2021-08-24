**A)**

|Agente|Performance|Entorno|Actuadores|Sensores|
| :-: | :-: | :-: | :-: | :-: |
|Jugar al CS |Número de bajas, Vida restante|El mapa del juego, otros jugadores, coberturas del mapa|Teclado de la computadora, ratón de la computadora|La cámara del juego, el sonido del juego, el HUD del juego|
|Explorar los Océanos|Espacio explorado, características del espacio explorado, especies descubiertas|El océano, seres marinos|motor de hélice, timón |Cámara, micrófono, sensor de presión, sensor de salinidad|
|Comprar y vender tokens crypto|Beneficios generados|Aplicación de compra y venta de tokens|Cartera virtual|Valor de un token|
|Practicar el tenis contra una pared |Número de golpes a la pelota consecutivos|Espacio donde se juega, pared a la que se lanza la pelota|Raqueta de tenis, algún mecanismo de movimiento|Cámara, sensor de contacto|
|Realizar un salto de altura|Altura del salto|Zona de salto|Piernas articuladas|Sensor de altura|
|Pujar por un artículo en una subasta|Obtención del articulo|Lugar de la subasta, otras personas pujando|Bocina, brazo|Cámara, micrófono, fondos disponibles|


**D)** Desempeño del agente reflexivo simple.

||2x2|4x4|8x8|16x16|32x32|64x64|128x128|
| :- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|0.1|0|2|6|26|89|84|79|
|0.2|1|3|13|51|143|155|169|
|0.4|2|6|26|102|290|278|287|
|0.8|3|13|51|205|428|444|438|

**E)** Desempeño por agente aleatorio

||2x2|4x4|8x8|16x16|32x32|64x64|128x128|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|0.1|0|2|6|8|10|14|8|
|0.2|1|3|12|13|14|21|27|
|0.4|2|6|25|42|50|39|53|
|0.8|3|13|45|80|92|93|88|

F)

**Pregunta 2.10**

1) No, porque un agente reflexivo simple no podría saber cuándo dejar de moverse para conservar desempeño, por lo que no sería un agente racional.
1) Si, ya que, al limpiar la primera casilla, moverse a la segunda y limpiarla, podría pasar a un estado donde no hace más movimientos, manteniendo el desempeño.
1) Le permite al primer agente detenerse una vez ya no haya suciedad, conservando desempeño, siendo así un agente racional, en el caso del segundo agente ya es racional, por lo que no cambiaría la respuesta.

**Pregunta 2.11**

1) Si, ya que no se le penaliza por moverse solo tiene que recorrer el entorno limpiando para maximizar su desempeño, por lo que lo podríamos considerar racional.
1) No, no podría, en el ejercicio **E)** se muestra el desempeño de uno en distintos entornos y se puede ver que su desempeño es bastante peor al del agente reflexivo. 
1) En un entorno donde la suciedad esté lo más lejos posible de la posición inicial del agente disminuye las probabilidades de que llegue a limpiar alguna casilla resultando en un desempeño todavía más bajo
1) Si, un agente que al limpiar un espacio cambia su estado interno del entorno para no pasar por ahí de nuevo y aumentar el desempeño en un menor número de movimientos, a diferencia de un agente reflexivo simple que al no tener información de acciones pasadas podría pasar por espacios ya limpiados.
