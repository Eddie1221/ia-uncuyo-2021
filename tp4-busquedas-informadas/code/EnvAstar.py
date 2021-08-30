from random import*

#Clase del entrono para el algoritmo de A*
class EnvAstar:
    ##Tiene como parametros la grilla, la posicion del agente y el objetivo
    def __init__(self):
        self.agentPos = GeneratePos()
        self.objetivo = GeneratePos()
        self.grilla = CreateGrilla(self)

    #Imprime el ambiente cambiando los numeros de las casillas por su estado actual ("No explorado")
    def print_enviroment(self):
        for i in range(100):
            for j in range(100):
              if type(self.grilla[i][j]) == int:
                self.grilla[i][j] = "N"

        for i in range(100):
          print(self.grilla[i])

    #Funciones para aceptar las acciones
    def accept_action(self, Fil, Col, action):

        if action == "up":
            if Fil > 0 and type(self.grilla[Fil-1][Col]) == int:
                return True
            else:
                return False

        elif action == "down":
            if Fil < 99 and type(self.grilla[Fil+1][Col]) == int:
                return True
            else:
                return False

        elif action == "right":
            if Col < 99 and type(self.grilla[Fil][Col+1]) == int:
                return True
            else:
                return False

        elif action == "left":
            if Col > 0 and type(self.grilla[Fil][Col-1]) == int:
                return True
            else:
                return False

#Funcion auxiliar para calcular la heuristica desde un estado hacia el objetivo
def CalcHeuristica(Env,Fil,Col):
    Obj = Env.objetivo
    resul = (abs(Obj[0]-Fil) + abs(Obj[1]-Col))
    return resul

#Funcion para crear la grilla, en cada espacio que no es un obstaculo cacula una heuristica de un aproximado optimista de la distancia
# desde es estado hacia el objetivo, perimitiendo al agente hacer la busqueda en funcion de dichas distancias
def CreateGrilla(Env):
    Grilla = []
    for i in range (100):
        Lista = []
        for j in range (100):
            if random() <= 0.2:
                if [i,j] != Env.objetivo and [i,j] != Env.agentPos: 
                    Lista.append("O")
                else:
                    Lista.append(CalcHeuristica(Env,i,j))
            else:
                Lista.append(CalcHeuristica(Env,i,j))
        
        Grilla.append(Lista)

    return Grilla

#Funcion para generar una posicion aleatoria
def GeneratePos():
    while True:
        Fil = randint(0,99)
        Col = randint(0,99)
        return [Fil, Col]