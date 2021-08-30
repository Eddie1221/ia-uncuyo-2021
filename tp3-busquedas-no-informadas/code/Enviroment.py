from random import*

#Clase del entorno, genera los obstaculos de manera automatica y aleatoria con una probabilidad de 20%
class Enviroment:
    #Tiene como parametros la grilla, la posicion del agente y el objetivo
    def __init__(self):
        self.grilla = CreateGrilla()
        self.agentPos = GeneratePos(self.grilla)
        self.objetivo = GeneratePos(self.grilla)

    #Funcion para imprimir la grilla
    def print_enviroment(self):
        for i in range(100):
            print(self.grilla[i])

    #Funcion para aceptar acicones
    def accept_action(self, Fil, Col, action):

        if action == "up":
            if Fil > 0 and self.grilla[Fil-1][Col] == "N":
                return True
            else:
                return False

        elif action == "down":
            if Fil < 99 and self.grilla[Fil+1][Col] == "N":
                return True
            else:
                return False

        elif action == "right":
            if Col < 99 and self.grilla[Fil][Col+1] == "N":
                return True
            else:
                return False

        elif action == "left":
            if Col > 0 and self.grilla[Fil][Col-1] == "N":
                return True
            else:
                return False

#Funcion auxiliar para crear la grilla
def CreateGrilla():
    Grilla = []
    for i in range (100):
        Lista = []
        for j in range (100):
            if random() <= 0.2:
                Lista.append("O")
            else:
                Lista.append("N")
        
        Grilla.append(Lista)

    return Grilla

#Funcion auxiliar para generar una posicion aleatoria de la grilla que no sea un obstaculo
def GeneratePos(grilla):
    while True:
        Fil = randint(0,99)
        Col = randint(0,99)
        if grilla[Fil][Col] == "N":
            return [Fil, Col]