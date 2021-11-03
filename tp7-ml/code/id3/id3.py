import csv
from math import log
from typing import Type

#Clase nodo con el atributo escogido, el valor que tomó el atributo padre como etiqueta y una lista para los hijos. 
class Node:
    def __init__(self, Atributo):
        self.atributo = Atributo
        self.etiqueta = None
        self.hijos = []

#Funcion wrapper para imprimir el arbol.
def ImpArbol(Arbol):
    ImpArbolRecur(Arbol,0)

#Funcion recursiva para imprimir recorriendo el arbol por profundidad con la altura de cada nodo para entenderlo.
def ImpArbolRecur(Nodo, cont):
    print("//////ALTURA ",cont,"//////")
    print("ETIQUETA: ", Nodo.etiqueta)
    print("ATRIBUTO: ", Nodo.atributo)

    if len(Nodo.hijos) > 0:
        for hijo in Nodo.hijos:
            ImpArbolRecur(hijo, cont+1)
        cont = cont +1

#Funcion para obtener la mayor clase (negativos o positivos) de un conjunto de ejemplos.
def MayorClase(Ejemplos):
    MayorClase = None
    MasOcurrencias = 0

    for ejemplo in Ejemplos:
        Clase = ejemplo[-1]
        cont = 0

        for ejemploAux in Ejemplos:
            if Clase in ejemploAux:
                cont = cont + 1

        if cont > MasOcurrencias:
            MasOcurrencias = cont
            MayorClase = Clase
    return MayorClase

#Funcion que verifica si un conjunto de ejemplos tiene la misma clasificacion.
def MismaClasifiacion(Ejemplos):
    val = Ejemplos[0][-1]
    for ejemplo in Ejemplos:
        if ejemplo[-1] != val:
            return False
    return True

#Funcion para calcular el resto de un atributo.
def Resto(atributo, Ejemplos, Pos, Neg):
    #Crea una lista con los valores posibles de ese atributo.
    ValPosibles = []
    for ejemplo in Ejemplos:
        val = ejemplo[atributo]
        if not val in ValPosibles:
            ValPosibles.append(val)

    #Hace los calculos para cada valor de el atributo y calcula la sumatoria del resto
    resto = 0
    for val in ValPosibles:
        PosAtr = 0
        NegAtr = 0

        for ejemplo in Ejemplos:
            if val in ejemplo:
                if ejemplo[-1] == "yes":
                    PosAtr = PosAtr + 1
                else:
                    NegAtr = NegAtr + 1

        AuxA = PosAtr/(PosAtr + NegAtr)
        AuxB = NegAtr/(PosAtr + NegAtr)
        AuxC = (PosAtr + NegAtr)/(Pos + Neg)

        if AuxA == 0 and AuxB == 0:
            entropia = 0
        elif AuxA == 0:
            entropia = -AuxB*log(AuxB,2)
        elif AuxB == 0:
            entropia = -AuxA*log(AuxA,2)
        else:
            entropia = -AuxA*log(AuxA,2) -AuxB*log(AuxB,2)

        resto = resto + AuxC*entropia

    return resto

#Funcion que encuentra el mejor atributo
def MejorAtributo(Atributos, Ejemplos):
    Pos = 0
    Neg = 0
    
    #Cuenta los ejemplos positivos y negativos y los utiliza para calcular la entropia general
    for ejemplo in Ejemplos:
        if ejemplo[-1] == "yes":
            Pos = Pos + 1
        else:
            Neg = Neg + 1
    #Calculo de la entropia general    
    AuxA = Pos/(Pos+Neg)
    AuxB = Neg/(Pos+Neg)
    EntropiaGen = -AuxA*log(AuxA,2) -AuxB*log(AuxB,2)

    #Calcula el resto de cada atributo y luego la ganancia de cada atributo, el que tenga mejor ganancia es el mejor atributo.
    MayorGanancia = 0
    MejorAtributo = None

    for i in range (len(Atributos)):
        
        Ganancia = EntropiaGen - Resto(i, Ejemplos, Pos, Neg)
        if Ganancia > MayorGanancia:
            MayorGanancia = Ganancia
            MejorAtributo = Atributos[i]

    #devuelve el mejor atributo.
    return MejorAtributo

#Funcion que crea el arbol de decisión
def ArbolDecision(Atributos, Ejemplos, ValDefecto):
    #Si no quedan mas ejemplos devuelve el valor por defecto
    if len(Ejemplos) == 0:
        return ValDefecto
    #Si todos lo ejemplos tienen la misma clasificacion(positivo o negativo) la devuelve.
    elif MismaClasifiacion(Ejemplos):
        return Ejemplos[0][-1]
    #si ya no quedan atributos para seleccionar regresa la mayor clase
    elif len(Atributos) == 0:
        return MayorClase(Ejemplos)
    else:
        #Calcula el mejor atributo, la mayor clase y crea un nodo de arbol
        Mejor =  MejorAtributo(Atributos, Ejemplos)
        mayor = MayorClase(Ejemplos)
        arbol = Node(Mejor)

        #toma el indice de dicho atributo para buscar los valores posibles.
        indice = Atributos.index(Mejor)

        #Toma los valores posibles del atributo.
        ValPosibles = []
        for ejemplo in Ejemplos:
            val = ejemplo[indice]
            if not val in ValPosibles:
                ValPosibles.append(val)

        #Para cada valor posible toma un sub-conjunto de los ejemplos tal que los ejemplos que toma tengan ese valor.
        for value in ValPosibles:
            SubEjemplos = []

            for ejemplo in Ejemplos:
                if ejemplo[indice] == value:
                    SubEjemplos.append(ejemplo.copy())
            
            #Elimina el mejor atributo de los atributos restantes, hace los mismo con las columna de ese atributo en los ejemplos
            #para que en las siguientes iteraciones el indice coincida con el atributo
            AtributosAux = Atributos.copy()
            AtributosAux.pop(indice)
            
            for ejemplo in SubEjemplos:
                ejemplo.pop(indice)

            #utiliza recursividad para seguir creando el arbol hacia abajo con los atributos restantes y el sub-conjunto de ejemplos
            subArbol = ArbolDecision(AtributosAux, SubEjemplos, mayor)

            #Una vez tiene el subarbol, lo une al arbol original para completarlo, le pone el valor del atributo como etiqueta para poder identificar
            #al nodo padre.
            if type(subArbol) != str:
                subArbol.etiqueta = value
            else:
                Nodo = Node(subArbol)
                subArbol = Nodo
                subArbol.etiqueta = value

            arbol.hijos.append(subArbol)

        #Se devuelve el arbol.
        return arbol

dataset = open("tennis.csv")

dataset_reader = csv.reader(dataset)

ejemplos = []

for row in dataset_reader:
    ejemplos.append(row)

atributos = ejemplos[0]

ejemplos.pop(0)
atributos.pop(-1)

mayor = MayorClase(ejemplos)

Arbol = ArbolDecision(atributos, ejemplos, mayor)

ImpArbol(Arbol)
