from random import*
from typing import Type
#Clase tablero con posiciones vacias para asignarles valores
class Tablero:
    def __init__(self, size):
        self.posiciones = [None]*size

#Funcion para calcular las reinas atacandose y asi descartar soluciones inconsistentes 
def FuncionH(Posiciones):
    cont = 0
    lon = len(Posiciones)

    for i in range(lon):
        for j in range(i,lon):
            
            if Posiciones[i] != None and Posiciones[j] != None and type(Posiciones[i]) == int and type(Posiciones[j]) == int:
                if i != j:
                    if Posiciones[i] == Posiciones[j]:
                        cont = cont + 1
                    elif abs(i-j) == abs(Posiciones[i]-Posiciones[j]):
                        cont = cont + 1 
        
    return cont

#Funcion para encontrar el valor mas restringido de las variables no asignadas en backtracking.
def ValorMasRestringido(Posiciones):
    lon = len(Posiciones)
    MenorColumna = -1
    MenorValor = 999999
    for i in range (lon):
        PosAux = Posiciones.copy()
        if PosAux[i] == None or type(PosAux[i]) != int:
            cont = 0
            for j in range(lon):
                PosAux[i] = j
                if FuncionH(PosAux) == 0:
                    cont = cont + 1
        
            if cont < MenorValor:
                MenorColumna = i
                MenorValor = cont

    return MenorColumna

#////////////////////////////////////////////////
#///CLASES Y FUNCIONES PARA EL FOWARD CHECKING///
#////////////////////////////////////////////////
#Clase del tablero donde cada una de las posiciones es una lista con el dominio de cada una de las variables.
class TableroFC():
    def __init__(self, size):
        self.posiciones = []
        ListaAux = []
        for i in range(size):
            ListaAux.append(i)

        for i in range(size):
            self.posiciones.append(ListaAux.copy())

#Funcion para encontrar el valor mas restringido de las variables no asignadas en foward checking.
def ValorMasRestringidoFC(Posiciones):
    lon = len(Posiciones)
    MenorColumna = -1
    MenorValor = 999999
    for i in range(lon):
        if type(Posiciones[i]) != int:
            if len(Posiciones[i])<MenorValor:
                MenorValor = len(Posiciones[i])
                MenorColumna = i

    return MenorColumna