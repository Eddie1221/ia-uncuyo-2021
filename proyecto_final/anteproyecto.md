**Juego de snake, un posible enfoque a través del aprendizaje reforzado**

**Código del proyecto:** SNAKE

**Integrantes:** Carlos Perez, Eduardo Perez

**Descripción del proyecto:**

Snake es un videojuego lanzado a mediados de los años 70, el cual saltó a la popularidad gracias a que fue incluido por defecto en los teléfonos de Nokia desde 1998. El objetivo del juego es controlar una serpiente en una grilla de tamaño predeterminado de 2 dimensiones, con el objetivo de comer la mayor cantidad de puntos posibles, por cada punto que la serpiente consuma el largo de su cuerpo se verá incrementado en una casilla, la serpiente morirá cuando choque con alguna de las paredes de la grilla, o con su propio cuerpo.

- Objetivos del proyecto: Implementar un bot que sea capaz de jugar al snake, con la finalidad de lograr un conocimiento base sobre algoritmos de aprendizaje reforzados y analizar los distintos parámetros que afectan el proyecto.

- Limitaciones: Es un área de la inteligencia artificial que no conocemos, por lo que gran parte del proyecto se basará en el estudio teórico de la misma. Además de esto el juego de Snake se presenta como un problema NP hard [2].

- Forma de evaluación de las métricas: En snake el objetivo único del juego es comer tantos puntos como sea posible, por lo que esta será la métrica que se tendrá sobre el algoritmo elegido. Paralelamente la otra métrica será nuestro entendimiento del algoritmo, con las bases y parámetros del mismo.

Los algoritmos elegidos para el proyecto serán el Q learning y posteriormente si el tiempo lo permite se estudiará resolver el problema utilizando Q learning + Deep learning (DQN), basándose en el artículo _Snake Played by a Deep Reinforcement Learning Agent[1]_.

**Justificación:**

El proyecto se centra en una de las áreas del aprendizaje automático como lo es el aprendizaje reforzado, el cual es un método de entrenamiento de machine learning basado en recompensar comportamientos deseados del modelo, y castigar los indeseados. Es por esto que este tipo de aprendizaje entra dentro de los parámetros de aplicación del proyecto, ya que presenta estos por sí mismos son una sub rama del machine learning.

**Listado de actividades a realizar:**

Tiempo total estimado: 50 días

**Actividad 1.** Investigación Teórica sobre Aprendizaje reforzado y el algoritmo a desarrollar. [14 días]

- Investigación teórica sobre el reinforced learning
- Investigación sobre el algoritmo Q learning
- Investigación sobre redes neuronales y el algoritmo de Deep Q Learning.

**Actividad 2.** Investigación práctica sobre algoritmos de aprendizaje reforzado y análisis sobre ejemplos relacionados [10 días]

- Investigación sobre implementaciones de Q learning
- Análisis del código provisto por el artículo [1]

**Actividad 3**. Implementación y análisis del juego base [5 días]

**Actividad 4**. Implementación del algoritmo elegido. [7 días]

- Implementación de Q learning para el juego de Snake

**Actividad 5**. Entrenamiento del modelo y corrección de parámetros. [7 días]

- Entrenamiento del algoritmo Q learning, con su corrección de parámetros adecuada.

**Actividad 6.** Análisis de los parámetros del problema enfocado en Deep Q Learning [5 días]

- Utilizando el algoritmo provisto por el artículo se estudiará su implementación y posibles variantes.

**Actividad 7.** Análisis de los resultados del algoritmo Q learning. [5 días]

- Análisis de los resultados del entrenamiento del algoritmo Q learning

**Actividad 8**. Análisis de resultados del Deep Q learning.[5 días]

- En caso de completarse la actividad 6, se realizará una comparación de performance entre el Q learning y el deep Q learning.

**Actividad 9.** Escritura de informe final. [7 días]

**Cronograma estimado de actividades:**

![Captura](https://user-images.githubusercontent.com/53824547/140092667-0a2d2c8f-f5d8-416c-ae5c-0e3d25397250.JPG)

**Bibliografía inicial:**

[1][https://towardsdatascience.com/snake-played-by-a-deep-reinforcement-learning-agent-53f2c4331d36?gi=d5eeed4c02d9](https://towardsdatascience.com/snake-played-by-a-deep-reinforcement-learning-agent-53f2c4331d36?gi=d5eeed4c02d9)

[2][http://cs229.stanford.edu/proj2016spr/report/060.pdf](http://cs229.stanford.edu/proj2016spr/report/060.pdf)
[3] AIMA 3rd Edition 
