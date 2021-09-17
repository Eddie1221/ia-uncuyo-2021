from random import*
#Clase tablero con las posiciones de las reinas y la heuristica
class Tablero:
    def __init__(self, size):
        self.posiciones = [None]*size
        PosicionInicial(self.posiciones)
        self.pares_reinas_atacadas = FuncionH(self.posiciones)
    
def PosicionInicial(Posiciones):
    for i in range(len(Posiciones)):
        Posiciones[i] = randint(0,len(Posiciones)-1)

def FuncionH(Posiciones):
    cont = 0
    lon = len(Posiciones)

    for i in range(lon):
        for j in range(i,lon):
            if i != j:
                if Posiciones[i] == Posiciones[j]:
                    cont = cont + 1
                elif abs(i-j) == abs(Posiciones[i]-Posiciones[j]):
                    cont = cont + 1 
        
    return cont

