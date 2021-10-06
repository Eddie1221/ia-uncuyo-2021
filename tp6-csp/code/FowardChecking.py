from typing import Collection
from TableroCSP import*
from time import*
from random import*

Estados = 0
#Funcion Wrapper para FC que tambien mide el timepo de ejecución
def FowardChecking(Size):
    global Estados
    Estados = 0
    time1 = time()
    tablero = TableroFC(Size)
    Solucion = FC(tablero,0)

    time2 = time()
    if Solucion != None:
        Solucion.append(time2-time1)
    
    return Solucion

#Funcion recursiva de FC, asigna los valores de las variable menos restringidas, cuando esto sucede, se eliminan los valores incompatibles del dominio del resto de variables
def FC(tablero, value):
    global Estados
    lon = len(tablero.posiciones)

    check = True
    for i in range(0,lon):
        if type(tablero.posiciones[i]) != int:
            check = False
    if check == True:
        return [tablero.posiciones, Estados]

    lonDominio = len(tablero.posiciones[value])
    for i in range(0,lonDominio):

        if lonDominio == 0:
            return None

        PosAux = ListCopy(tablero.posiciones)
        
        if value == 0:
            PosAux[value] = randint(0,lon-1)
        else:
            PosAux[value] = PosAux[value][i]
            
        TabAux = TableroFC(lon)
        TabAux.posiciones = ListCopy(PosAux)
        
        #Se eliminan los valores del dominio del resto de variables al asignar una variable especificada
        EliminarDominio(TabAux.posiciones,value)

        value = ValorMasRestringidoFC(TabAux.posiciones)
        Estados = Estados + 1
        val = FC(TabAux, value)
        if val != None:
            return val


#Funcion para eliminar el dominio de las variable cuando se le asigna un valor a otra
def EliminarDominio(Posiciones, Columna):
    for i in range(0,len(Posiciones)):
        if i != Columna and type(Posiciones[i]) != int:
            ValEliminar = []
            for j in range(0,len(Posiciones[i])):
                    if Posiciones[Columna] == Posiciones[i][j]:
                        ValEliminar.append(Posiciones[i][j])
                    elif abs(Columna - i) == abs(Posiciones[i][j]-Posiciones[Columna]):
                        ValEliminar.append(Posiciones[i][j]) 

            for j in range(0,len(ValEliminar)):
                Posiciones[i].remove(ValEliminar[j])

#Funcion para copiar una lista de listas.
def ListCopy(Posiciones):
    lon = len(Posiciones)
    lista = []
    for i in range(lon):
        if type(Posiciones[i]) == int:
            lista.append(Posiciones[i])
        else:
            lista.append(Posiciones[i].copy())

    return lista