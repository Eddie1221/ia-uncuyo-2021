from math import e
from random import*
from Tablero import*
from time import*

#Funcion Simulated Annealing
def SimulatedAnnealing(tablero):
    #Declara la variable de tiempo, mejor estado, la heuristica de dicho estado, la longitud del tablero y un contador de los estados visitados
    time1 = time()
    lon = len(tablero.posiciones)
    t = 1
    cont = 1
    Hlist = []
    Hlist.append(tablero.pares_reinas_atacadas)
    while True:
        #Calcula la temperatura en funcion del tiempo, cuando esta llega a 0, el algoritmo termina
        T = Schedule(t)
        if T == 0:
            time2 = time()
            return [tablero.posiciones, cont, tablero.pares_reinas_atacadas, time2-time1, Hlist]

        #Se elige un estado vecino al azar
        i = randint(0,lon-1)
        PosicionesAux = tablero.posiciones.copy()
        ValAux = PosicionesAux[i]
            
        j = randint(0,lon-1)
        if ValAux != j:
            PosicionesAux[i] = j
                    
            NuevoH = FuncionH(PosicionesAux)
            DeltaE = tablero.pares_reinas_atacadas - NuevoH
            #Si el estado nuevo es mejor que el actual se cambia, si es peor, se cambia con una probabilida.
            #Dicha probabilidad disminuye conforme pasa el tiempo por lo que mientras mas tiempo pasa mas se cierra el problema
            #a soluciones mejores
            if DeltaE > 0:
                tablero.pares_reinas_atacadas = NuevoH
                Hlist.append(NuevoH)
                tablero.posiciones = PosicionesAux.copy()
                cont = cont + 1
            else:
                if random() <= Probability(DeltaE,T):
                    tablero.pares_reinas_atacadas = NuevoH
                    Hlist.append(NuevoH)
                    tablero.posiciones = PosicionesAux.copy()
                    cont = cont + 1
                        
        t = t + 1

        #Si encuentra una solucion optima termina la ejecucion
        if tablero.pares_reinas_atacadas == 0:
            time2 = time()
            return [tablero.posiciones, cont, tablero.pares_reinas_atacadas, time2-time1, Hlist]

#Funcion para calcular la temperatura
def Schedule(t):
    T = 1/t - 0.0001
    return T

#Funcion para calcular la probabilidad de escoger un peor estado
def Probability(DeltaE,T):
    return e**(DeltaE/T)