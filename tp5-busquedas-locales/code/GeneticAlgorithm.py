from math import trunc
from random import*
from time import*
from Tablero import*
from time import*

#Funcion del algoritmo genetico
def GeneticAlgorithm(poblacion):
    #Declara la variable del tamaño de la población, un porcentaje que es la elite que no se reemplaza y ordena la porblacion en funcion del fitness
    time1 = time()
    Hlist = []
    lon = len(poblacion)
    best = trunc(lon/5)
    poblacion.sort(key = lambda x:x.pares_reinas_atacadas)
    Hlist.append(poblacion[0].pares_reinas_atacadas)

    for i in range(600):
        #Agarra todos los mejores como padres y los cruza, luego reemplaza los primeros individuos despues de los mejores por los hijos
        #de los mejores
        for j in range(0,best):

            x = poblacion[j].posiciones
            y = poblacion[j+1].posiciones
            
            hijo = Cruzar(x,y)
            poblacion[j+best] = hijo
            #Si encuentra un hijo con un fitness minimo, lo devuelve junto con el contador de iteraciones 
            if hijo.pares_reinas_atacadas == 0:
                time2 = time()
                return [hijo.posiciones, i+1, hijo.pares_reinas_atacadas, time2-time1, Hlist]

        #Se ordena la poblacion otra vez para la siguiente operacion
        poblacion.sort(key = lambda x:x.pares_reinas_atacadas)
        Hlist.append(poblacion[0].pares_reinas_atacadas)

    time2 = time()
    return [poblacion[0].posiciones, i+1, poblacion[0].pares_reinas_atacadas, time2-time1, Hlist]

#Funcion para cruzar los padres y crear el nuevo hijo
def Cruzar(x,y):
    lon = len(x)
    separacion = randint(0,lon)
    rand = random()

    hijo = Tablero(lon)
    hijo.posiciones = x[0:separacion] + y[separacion:lon]
    if rand <= 0.3:
        hijo.posiciones[randint(0,lon-1)] = randint(0,lon-1)
    hijo.pares_reinas_atacadas = FuncionH(hijo.posiciones)
    return hijo