from random import*

#Clase del ambiente
class Enviroment:
    #Función para instanciar la clase
    def __init__(self, TamX, TamY, PosIniX, PosIniY, dirt_rate):
        self.floor = CreateFloor(TamY , TamX)        
        self.TamY = TamY
        self.TamX = TamX
        self.PosAgentX = PosIniX
        self.PosAgentY = PosIniY
        self.performance = 0
        GetFloorDirty(self,dirt_rate)

    #Funcion para aceptar la acción, si es de movimiento le indica al agente si puede hacerla y cambia su posición, al usar el sensor le devuelve
    #el valor de suciedad de su posicion y al limpiar cambia el valor a "L"
    def accept_action(self, action):
        if action == "up":
            if self.PosAgentY > 0:
                self.PosAgentY = self.PosAgentY - 1
                return True
            else:
                return False

        elif action == "down":
            if self.PosAgentY < self.TamY-1:
                self.PosAgentY = self.PosAgentY + 1
                return True
            else:
                return False

        elif action == "right":
            if self.PosAgentX < self.TamX-1:
                self.PosAgentX = self.PosAgentX + 1
                return True
            else:
                return False

        elif action == "left":
            if self.PosAgentX > 0:
                self.PosAgentX = self.PosAgentX - 1
                return True
            else:
                return False

        elif action == "sense":
            return self.floor[self.PosAgentY][self.PosAgentX]

        elif action == "clean":
            if self.floor[self.PosAgentY][self.PosAgentX] == "S":
                self.performance = self.performance + 1
            self.floor[self.PosAgentY][self.PosAgentX] = "L"   

    #Funcion para obtener el performance del agente
    def get_performance(self):
        return self.performance

    #Funcion para imprimir el ambiente
    def print_enviroment(self):
        for i in range(self.TamY):
            print(self.floor[i])

#Función auxiliar para crear la matriz que representa el suelo
def CreateFloor(Y, X):
    Lista = ["L"]*X

    Floor = []
    for i in range(Y):
        Floor.append(Lista.copy())

    return Floor

#Función axuliar para distribuir la suciedad de manera aleatoria
def GetFloorDirty(Env, dirt_rate):
    TotalDirt = round(Env.TamX * Env.TamY * dirt_rate)
    cont = 0

    while cont < TotalDirt:
        for i in range(Env.TamY):

            for j in range(Env.TamX):
                if Env.floor[i][j] == "L":
                    if random() <= dirt_rate:
                        Env.floor[i][j] = "S"
                        cont = cont + 1
                        if cont == TotalDirt:
                            break
            
            if cont == TotalDirt:
                break