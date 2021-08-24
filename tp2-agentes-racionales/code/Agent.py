from random import randint
from Enviroment import Enviroment

#Clase Agente
class Agent:
    #Funcion para instanciarla, toma un entorno como parametro.
    def __init__(self, Env):
        self.env = Env
        self.life = 1000

    #Funciones para enviar la acción deseada al entorno para recibir respuesta de si es posible o no.
    def up(self):
        return self.env.accept_action("up")

    def down(self):
        return self.env.accept_action("down")

    def right(self):
        return self.env.accept_action("right")

    def left(self):
        return self.env.accept_action("left")

    def sense(self):
        return self.env.accept_action("sense")
    
    def clean(self):
        return self.env.accept_action("clean")

    def idle(self):
        self.life = self.life - 1

    #Funcion think
    def think(self):

        #Variable de la direccion para decidir si gira a la derecha o a la izquierda
        Direccion = "der"
        while self.life > 0:
            #Codigo para sensar la posicionón y saber si está sucia, de estarlo, la limpia.
            if self.sense() == "S":
                self.clean()
                self.life = self.life - 1
                if self.life == 0:
                    return

            #Avanza hacia abajo hasta que llega al limite, sensando y limpiando por el camino
            while self.down() == True:

                self.life = self.life - 1
                if self.life == 0:
                    return

                if self.sense() == "S":
                    self.clean()
                    self.life = self.life - 1
                    if self.life == 0:
                        return

            #Luego gira avanza hacia la izquierda o derecha una vez, segun sea el valor de Dirección, si no puede moverse a una dirección cambiará
            # la variable para irse a la contraria 
            if Direccion == "der":
                if self.right() == True:
                    self.life = self.life - 1
                    if self.life == 0:
                        return
                else:
                    Direccion = "izq"
                    self.left()
                    self.life = self.life - 1
                    if self.life == 0:
                        return
            else:
                if self.left() == True:
                    self.life = self.life - 1
                    if self.life == 0:
                        return
                else:
                    Direccion = "der"
                    self.right()
                    self.life = self.life - 1
                    if self.life == 0:
                        return

            if self.sense() == "S":
                self.clean()
                self.life = self.life - 1
                if self.life == 0:
                    return

            #Avanza hacia arriba hasta que llega al limite, sensando y limpiando por el camino
            while self.up() == True:
                self.life = self.life - 1
                if self.life == 0:
                    return
                
                if self.sense() == "S":
                    self.clean()
                    self.life = self.life - 1
                    if self.life == 0:
                        return
            
            #Avanza hacia la izquierda o derecha otra vez
            if Direccion == "der":
                if self.right() == True:
                    self.life = self.life - 1
                    if self.life == 0:
                        return
                else:
                    Direccion = "izq"
                    self.left()
                    self.life = self.life - 1
                    if self.life == 0:
                        return
            else:
                if self.left() == True:
                    self.life = self.life - 1
                    if self.life == 0:
                        return
                else:
                    Direccion = "der"
                    self.right()
                    self.life = self.life - 1
                    if self.life == 0:
                        return

            if self.sense() == "S":
                self.life = self.life - 1
                if self.life == 0:
                    return

                self.clean()
                self.life = self.life - 1
                if self.life == 0:
                    return
            else:
                self.life = self.life - 1
                if self.life == 0:
                    return

    #Funcion aleatoria para el agente aleatorio, genera un numero al azar y actua en funcion de ese numero
    def random(self):
        while self.life > 0:
            Accion = randint(1,6)

            if Accion == 1:

                if self.up() ==  True:
                    self.life = self.life - 1
                    if self.life == 0:
                        return

            elif Accion == 2:

                if self.down() == True:
                    self.life = self.life - 1
                    if self.life == 0:
                        return

            elif Accion == 3:

                if self.right() == True:
                    self.life = self.life - 1
                    if self.life == 0:
                        return
            
            elif Accion == 4:

                if self.left() == True:
                    self.life = self.life - 1
                    if self.life == 0:
                        return

            elif Accion == 5:

                self.clean()

            elif Accion == 6:

                self.idle()


    