from PriorityQueue import*

class AgentAstar:
    #Tiene como parametros la grilla, su posicion, el objetivo y la frontera
    def __init__(self, Enviroment):
        self.env = Enviroment
        self.pos = Enviroment.agentPos
        self.obj = Enviroment.objetivo
        self.front = []
        enqueue(self.front, self.pos, 0)
        self.env.grilla[self.pos[0]][self.pos[1]] = "F"

    #Funciones para moverse
    def up(self, Fil, Col):
        return self.env.accept_action(Fil, Col, "up")

    def down(self, Fil, Col):
        return self.env.accept_action(Fil, Col, "down")

    def right(self, Fil, Col):
        return self.env.accept_action(Fil, Col, "right")

    def left(self, Fil, Col):
        return self.env.accept_action(Fil, Col, "left")
    
    #Funcion para hacer la busqueda, imprimir la grilla y la secuencia, tambien actua como funcion wrapper para la recursividad.
    def think(self):
        Secuencia = AstarSearch(self, 0)
        self.env.grilla[self.pos[0]][self.pos[1]] = "A"
        self.env.grilla[self.obj[0]][self.obj[1]] = "X"
        print("A = Agente")
        print("X = Objetivo")
        print("O = Obstaculo")
        print("N = No explorado")
        print("F = Frontera")
        print("E = Explorado")
        self.env.print_enviroment()
        print("Estado inicial del Agente: ", self.pos)
        print("Estado Objetivo: ", self.obj)
        print(Secuencia)
        if type(Secuencia) != str:
            print("El largo de la secuencia es: ",len(Secuencia))

#Funcion auxiliar para calcula la resta de 2 estados
def Restar_Estados(Est1, Est2):
    Res = []
    Res.append(Est1[0]-Est2[0])
    Res.append(Est1[1]-Est2[1])
    return Res

#Funcion auxiliar para saber si 2 estado son adyacentes, esta se utiliza al salir de la recursividad y obtener los estados pertenecienes 
# a la secuencia deseada
def is_next(Est1, Est2):
    Resta = Restar_Estados(Est1, Est2)
    if Resta == [0,1] or Resta == [0,-1] or Resta == [1,0] or Resta == [-1,0]:
        return True

#Funcion recursiva para el algoritmo A*, implementa colas con prioridad donde, meintras menor sea la distancia recorria mas la
#heuristica del estado actual, mayor prioridad tiene en la cola, buscando asi siempre el camino mas optimo.
def AstarSearch(self, cont):

    while self.front != []:
        Estado = dequeue(self.front)
        self.env.grilla[Estado[0]][Estado[1]] = "E"

        if Estado == self.obj:
            Lista = []
            Lista.append(Estado)
            return Lista
        else:

            if self.up(Estado[0], Estado[1]) == True:
                enqueue(self.front,[Estado[0]-1,Estado[1]],cont+self.env.grilla[Estado[0]-1][Estado[1]])
                self.env.grilla[Estado[0]-1][Estado[1]] = "F"

            if self.down(Estado[0], Estado[1]) == True:
                enqueue(self.front,[Estado[0]+1,Estado[1]],cont+self.env.grilla[Estado[0]+1][Estado[1]])
                self.env.grilla[Estado[0]+1][Estado[1]] = "F"

            if self.right(Estado[0], Estado[1]) == True:
                enqueue(self.front,[Estado[0],Estado[1]+1],cont+self.env.grilla[Estado[0]][Estado[1]+1])
                self.env.grilla[Estado[0]][Estado[1]+1] = "F"

            if self.left(Estado[0], Estado[1]) == True:
                enqueue(self.front,[Estado[0],Estado[1]-1],cont+self.env.grilla[Estado[0]][Estado[1]-1])
                self.env.grilla[Estado[0]][Estado[1]-1] = "F"

            Lista = AstarSearch(self, cont+1)
            if type(Lista) != str:
                if is_next(Lista[0],Estado) == True:
                    Lista.insert(0,Estado)
                return Lista

    return "No fue posible llegar al objetivo."