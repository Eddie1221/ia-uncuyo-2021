from SimulatedAnnealing import*
from GeneticAlgorithm import*
from HillClimbing import*
from Tablero import*
import statistics

#Listas de HC:
TimeHC = []
EstadoHC = []

#Listas de SA:
TimeSA = []
EstadoSA = []

#Lista de GA:
TimeGA = []
EstadoGA = []

cont1 = 0
for i in range(30):
    tablero = Tablero(10)
    Solucion = HillClimbing(tablero)

    print("Estado solución: ", Solucion[0])
    print("Estado recorridos: ", Solucion[1])
    if Solucion[2] != 0:
        print("Pares de reinas atacados(H(e)): ", Solucion[2])
    else:
        cont1 = cont1 + 1

    TimeHC.append(Solucion[3])
    EstadoHC.append(Solucion[2])


cont2 = 0
for i in range(30):
    tablero2 = Tablero(10)
    Solucion = SimulatedAnnealing(tablero2)

    print("Estado solución: ", Solucion[0])
    print("Estado recorridos: ", Solucion[1])
    if Solucion[2] != 0:
        print("Pares de reinas atacados(H(e)): ", Solucion[2])
    else:
        cont2 = cont2 + 1

    TimeSA.append(Solucion[3])
    EstadoSA.append(Solucion[2])

cont3 = 0
for i in range(30):
    poblacion = []
    for i in range(200):
        tablero3 = Tablero(10)
        poblacion.append(tablero3)

    Solucion = GeneticAlgorithm(poblacion)

    print("Estado solución: ", Solucion[0])
    print("Estado recorridos: ", Solucion[1])
    if Solucion[2] != 0:
        print("Pares de reinas atacados(H(e)): ", Solucion[2])
    else:
        cont3 = cont3 + 1

    TimeGA.append(Solucion[3])
    EstadoGA.append(Solucion[2])

print("================================================")
print("Hill Climbing: ")
print("Número de soluciones encontradas Hill Climbing: ", cont1)
print("Promedio del tiempo de ejecucion: ",statistics.mean(TimeHC))
print("Desviación estandar del tiempo de ejecucion: ",statistics.stdev(TimeHC))
print("Promedio del numero de estado recorridos: ",statistics.mean(EstadoHC))
print("Deviacion estandar del numero de estados recorridos: ",statistics.stdev(EstadoHC))

print("================================================")
print("Simulated Annealing: ")
print("Número de soluciones encontradas Simulated Annealing: ", cont2)
print("Promedio del tiempo de ejecucion: ", statistics.mean(TimeSA))
print("Desviación estandar del tiempo de ejecucion: ",statistics.stdev(TimeSA))
print("Promedio del numero de estado recorridos: ",statistics.mean(EstadoSA))
print("Deviacion estandar del numero de estados recorridos: ",statistics.stdev(EstadoSA))

print("================================================")
print("Genetic Algorithm: ")
print("Número de soluciones encontradas Genetic Algorithm: ", cont3)
print("Promedio del tiempo de ejecucion: ",statistics.mean(TimeGA))
print("Desviación estandar del tiempo de ejecucion: ",statistics.stdev(TimeGA))
print("Promedio del numero de estado recorridos: ",statistics.mean(EstadoGA))
print("Deviacion estandar del numero de estados recorridos: ",statistics.stdev(EstadoGA))

print("================================================")
print("================================================")
print("Tiempos de HC:")
print(TimeHC)
print(" ")
print("Tiempos de SA:")
print(TimeSA)
print(" ")
print("Tiempos de GA:")
print(TimeGA)
print(" ")