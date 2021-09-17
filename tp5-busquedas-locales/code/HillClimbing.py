from Tablero import*
from time import*

#Funcion de Hill Climbing
def HillClimbing(tablero):
    #Declara la variable de el mejor estado, la heuristica de dicho estado y la longitud del tablero
    Hlist = []
    time1 = time()
    MejorEstado = tablero.posiciones.copy()
    MejorH = FuncionH(tablero.posiciones)
    lon = len(tablero.posiciones)
    Hlist.append(MejorH)
    for cont in range(1000):

        #Revisa todos los estados vecinos para encontrar el mejor
        for i in range(lon):
            PosicionesAux = tablero.posiciones.copy()
            ValAux = PosicionesAux[i]
            
            for j in range(lon):
                if ValAux != j:
                    PosicionesAux[i] = j
                    
                    NuevoH = FuncionH(PosicionesAux)
                    #Si el estado que se está revisando es mejor se actualiza
                    if NuevoH < MejorH:
                        MejorH = NuevoH
                        MejorEstado = PosicionesAux.copy()

        #Se cambia el estado actual por el mejor vecino y se repite el proceso hasta llegar a una solucion optima o hasta que se 
        #acaben la iteraciones y devuelva la mejor solucion encontrada
        tablero.posiciones = MejorEstado
        tablero.pares_reinas_atacadas = MejorH
        Hlist.append(MejorH)

        if tablero.pares_reinas_atacadas == 0:
            time2 = time()
            return [MejorEstado, cont+1, MejorH, time2-time1, Hlist]

    time2 = time()
    return [MejorEstado, cont+1, MejorH, time2-time1, Hlist]