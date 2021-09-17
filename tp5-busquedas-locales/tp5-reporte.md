**Alumno:** Eduardo Pérez

**Legajo:** 13244

***Algoritmos de Búsqueda Local***

**Hill Climbing:**

**Con 4 Reinas:**

Porcentaje de soluciones optimas encontradas: 40%

Promedio del tiempo: 0.013849298159281412

Desviación estándar del tiempo: 0.01148778594039069

Promedio del número de estados recorridos: 0.7

Desviación estándar del número de estados recorridos: 0.651258728182957

Gráfico de cajas de los tiempos de ejecución:

![image](https://user-images.githubusercontent.com/88392382/133856644-7442e59b-87d6-4ed6-97df-6dde5d0ead76.png)


**Con 8 Reinas:**

Porcentaje de soluciones optimas encontradas: 26.666667%

Promedio del tiempo: 0.21397624015808106

Desviación estándar del tiempo: 0.13074480743827005

Promedio del número de estados recorridos:  1.1666666666666667

Desviación estándar del número de estados recorridos: 0.9128709291752769

Gráfico de cajas de los tiempos de ejecución: 

![image](https://user-images.githubusercontent.com/88392382/133856662-abb02836-0765-419a-ae2b-96314ae5777e.png)

**Con 10 Reinas:**

Porcentaje de soluciones optimas encontradas: 10%

Promedio del tiempo: 0.6271573781967164

Desviación estándar del tiempo: 0.21190895746060937

Promedio del número de estados recorridos: 1.5333333333333334

Desviación estándar del número de estados recorridos: 0.7760791522613609

Gráfico de cajas de los tiempos de ejecución: 

![image](https://user-images.githubusercontent.com/88392382/133856693-204e3e9f-23fd-4b6c-b0c0-64a1f7d159ba.png)

**Simulated Annealing:** 

**Con 4 Reinas:**

Porcentaje de soluciones optimas encontradas: 100%

Promedio del tiempo: 0.00033310254414876305

Desviación estándar del tiempo: 0.0004791597566826724

Promedio del número de estados recorridos: 0

Desviación estándar del número de estados recorridos: 0.0

Gráfico de cajas de los tiempos de ejecución: 

![image](https://user-images.githubusercontent.com/88392382/133856704-b605005e-ec69-4802-bc6e-72cd06a8939d.png)

**Con 8 Reinas:**

Porcentaje de soluciones optimas encontradas: 96.666667%

Promedio del tiempo: 0.005819201469421387

Desviación estándar del tiempo: 0.012732228722723041

Promedio del número de estados recorridos: 0.03333333333333333

Desviación estándar del número de estados recorridos: 0.18257418583505536

Gráfico de cajas de los tiempos de ejecución: 

![image](https://user-images.githubusercontent.com/88392382/133856716-cd8ea43f-f669-4155-bfe7-4feb7a17cbf1.png)

**Con 10 Reinas:**

Porcentaje de soluciones optimas encontradas: 100%

Promedio del tiempo: 0.028994027773539224

Desviación estándar del tiempo: 0.023725487611275055

Promedio del número de estados recorridos: 0

Desviación estándar del número de estados recorridos: 0.0

Gráfico de cajas de los tiempos de ejecución: 

![image](https://user-images.githubusercontent.com/88392382/133856728-145c40f2-3871-48e6-9253-509b2bd259fd.png)

**Genetic Algorithm:**

**Con 4 Reinas:**

Porcentaje de soluciones optimas encontradas: 100%

Promedio del tiempo: 0.0006008068720499675

Desviación estándar del tiempo: 0.0008546388960223285

Promedio del número de estados recorridos: 0

Desviación estándar del número de estados recorridos: 0.0

Gráfico de cajas de los tiempos de ejecución: 

![image](https://user-images.githubusercontent.com/88392382/133856744-617aaa1f-416b-405e-9e1c-cd392e559aff.png)


**Con 8 Reinas:**

Porcentaje de soluciones optimas encontradas: 36.666667%

Promedio del tiempo: 0.2903673013051351

Desviación estándar del tiempo: 0.1896379346325107

Promedio del número de estados recorridos:  0.6333333333333333

Desviación estándar del número de estados recorridos: 0.490132517853561

Gráfico de cajas de los tiempos de ejecución: 

![image](https://user-images.githubusercontent.com/88392382/133856771-f539cf09-2c2c-4f8b-a809-d914c38758c4.png)

**Con 10 Reinas:**

Porcentaje de soluciones optimas encontradas: 23.333333%

Promedio del tiempo: 0.44752357006072996

Desviación estándar del tiempo: 0.22624157417908672

Promedio del número de estados recorridos: 0.8666666666666667

Desviación estándar del número de estados recorridos: 0.5713464637233658

Gráfico de cajas de los tiempos de ejecución: 

![image](https://user-images.githubusercontent.com/88392382/133856778-de06273e-a761-49a0-84e0-c664130b4df0.png)

**B) Gráficos de H(e):**

**Hill Climbing:**

![image](https://user-images.githubusercontent.com/88392382/133856787-b69b063e-1e9a-44a0-8c98-e144396a0329.png)

**Simulated Annealing:**

![image](https://user-images.githubusercontent.com/88392382/133856808-c73fce4d-aa99-4d2e-86e0-ac774055c751.png)

**Genetic Algorithm:**

![image](https://user-images.githubusercontent.com/88392382/133856819-eaef32e0-939e-4fef-9b63-eb1488ddd408.png)

**C)** Considero que el algoritmo más adecuado para este problema es el simulates annealing, ya que presentó mejores resultados y tiempos de ejecución, esto se debe a que no se queda atacado en mínimos locales como el Hill climbing, y para este problema donde el resultado depende de las posiciones de las reinas con respecto a las demás, el cruce en genetic algorithm no siempre deja buenos hijos, ya al cruzar resultados buenos pueden que los genes que se toman de cada padre den un resultado peor.
