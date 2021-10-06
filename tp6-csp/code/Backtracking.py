from TableroCSP import*
from time import*
from random import*

Estados = 0

#Funcion wrapping de backtracking, donde tambien se toma el tiempo de ejecución
def BacktrackingCSP(Size):
    global Estados
    Estados = 0
    time1 = time()
    tablero = Tablero(Size)

    Solucion = BTCSP(tablero,0)

    time2 = time()
    if Solucion != None:
        Solucion.append(time2-time1)
    
    return Solucion

#Funcion recursiva que va recorriendo las distintas soluciones, asignando valores a las variables, hasta encontrar una completa y consistente utilizando backtracking.
def BTCSP(tablero, value):
    global Estados
    lon = len(tablero.posiciones)

    if (None not in tablero.posiciones) == True:
        return [tablero.posiciones, Estados]

    for i in range(0,lon):
        PosAux = tablero.posiciones.copy()
        if value == 0:
            PosAux[value] = randint(0,lon-1)
        else:
            PosAux[value] = i
            
        if FuncionH(PosAux) == 0:
            TabAux = Tablero(lon)
            TabAux.posiciones = PosAux.copy()
            value = ValorMasRestringido(TabAux.posiciones)
            Estados = Estados + 1
            val = BTCSP(TabAux, value)
            if val != None:
                return val