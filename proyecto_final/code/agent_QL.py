from snake import GAME
from pygame.math import Vector2
import numpy as np
import random
import json

class AGENT:
    def __init__(self) -> None:
        self.env = GAME()
        self.env.human = False
        self.defninirParametros()
        self.qtable = self.LoadQtable()
        self.score = []
        self.moves = []
        
    def defninirParametros(self):
        #Parametros de la ecuacion de Bellman cuando el juego no tiene obstaculos
        self.discount_rate = 0.95
        self.learning_rate = 0.01
        self.exploration_chance = 1.0
        self.exploration_decrease = 0.995
        self.min_exploration = 0.001
            
        #Recompensas
        self.rewardFruit = 10
        self.rewardCloser = 1
        self.rewardFarther = -2
        self.rewardDeath = -1000
        
        #Episodios
        self.num_episodes = 1000
        
        
    def run_game(self, switchObstacles):
        self.env = GAME()
        self.env.human = False
        self.env.run_game(switchObstacles)
        
    def LoadQtable(self, path="qvalues.json"):
        with open(path, "r") as f:
            qvalues = json.load(f)
        return qvalues
    
    def SaveQvalues(self, path="qvalues.json"):
        with open(path, "w") as f:
            json.dump(self.qtable, f)
        
    #Calcula la distancia en bloques desde la cabeza de la serpiente hasta la fruta.
    def fruit_distance(self):
        return abs(self.env.tablero.snake.body[0].x - self.env.tablero.fruit.x) + abs(self.env.tablero.snake.body[0].y - self.env.tablero.fruit.y)
    
    #Funcion que informa si hay algun afruta adyacente a la cabeza de la serpiente
    def detectFruta(self, fruta, serpiente):
        frutaAdyacente = "-"
        cabeza = serpiente.body[0]
        
        if cabeza.x-1 == fruta.pos.x and cabeza.y == fruta.pos.y:
            frutaAdyacente = "L"
        elif cabeza.x+1 == fruta.pos.x and cabeza.y == fruta.pos.y:
            frutaAdyacente = "R"
        elif cabeza.y-1 == fruta.pos.y and cabeza.x == fruta.pos.x:
            frutaAdyacente = "U"
        elif cabeza.y-1 == fruta.pos.y and cabeza.x == fruta.pos.x:
            frutaAdyacente = "D"
            
        return frutaAdyacente
    
    #Funcion que informa de los peligros inmediatos a la cabeza de la serpiente
    def detectDanger(self, tablero, serpiente):
        danger = [0,0,0,0]
        cabeza = serpiente.body[0]
        
        #Peligro a la izquierda 
        if cabeza.x-1 == 0 or Vector2(cabeza.x-1,cabeza.y) in serpiente.body[1:] or Vector2(cabeza.x-1,cabeza.y) in tablero.obst:
            danger[0] = 1
            
        #Peligro a la derecha 
        if cabeza.x+1 == tablero.cell_num-1 or Vector2(cabeza.x+1,cabeza.y) in serpiente.body[1:] or Vector2(cabeza.x+1,cabeza.y) in tablero.obst:
            danger[1] = 1

        #Peligro arriba
        if cabeza.y-1 == 0 or Vector2(cabeza.x,cabeza.y-1) in serpiente.body[1:] or Vector2(cabeza.x,cabeza.y-1) in tablero.obst:
            danger[2] = 1
            
        #Peligro abajo
        if cabeza.y+1 == tablero.cell_num-1 or Vector2(cabeza.x,cabeza.y+1) in serpiente.body[1:] or Vector2(cabeza.x,cabeza.y-1) in tablero.obst:
            danger[3] = 1
            
        return danger
    
    def getAction(self, state):
        if random.random() < self.exploration_chance:
            return random.choice([0,1,2,3])
        else:
            return np.argmax(self.qtable[str(state)])
            
            
    def getState(self, serpiente, fruta, tablero):
        danger = self.detectDanger(tablero, serpiente)
        frutaAdyacente = self.detectFruta(fruta, serpiente)
        cabeza = serpiente.body[0]
        
        dist_x = fruta.x - cabeza.x
        dist_y = fruta.y - cabeza.y
        
        if dist_x < 0:
            pos_x = 'L'  
        elif dist_x > 0:
            pos_x = 'R'
        else:
            pos_x = '='
            
        if dist_y < 0:
            pos_y = 'U'
        elif dist_y > 0:
            pos_y = 'D'
        else:
            pos_y = '='
            
            
        if serpiente.direction == Vector2(-1,0):
            direction = "L"
        elif serpiente.direction == Vector2(1,0):
             direction = "R"
        elif serpiente.direction == Vector2(0,-1):
            direction = "U"
        elif serpiente.direction == Vector2(0,1):
            direction = "D"
                
        estado = (pos_x, pos_y, danger[0], danger[1], danger[2], danger[3], direction, frutaAdyacente)
        return estado
    
    def learn(self, switchObstacles):
        #Numero de episodios que el agente jugará para entrenar
        for i in range (1,self.num_episodes+1):
            print("Episodio: "+str(i)+"/"+str(self.num_episodes))
            self.run_game(switchObstacles)
            snake = self.env.tablero.snake
            fruit = self.env.tablero.fruit
            board = self.env.tablero
            steps_without_food = 0
            moves = 0
            state = self.getState(snake, fruit, board)
            self.exploration_chance = max(self.exploration_chance * self.exploration_decrease, self.min_exploration)
            while (steps_without_food < 1000 and (snake.isDeath == False)):
                
                snake_length = len(snake.body)
                fruit_distance = self.fruit_distance()
                action = self.getAction(state)
                self.env.jugada(action)
                moves = moves + 1
                
                if snake.isDeath == True:
                    reward = self.rewardDeath
                else:
                    new_snake_length = len(snake.body)
                    if new_snake_length > snake_length:
                        steps_without_food = 0
                        reward = self.rewardFruit
                    else:
                        new_fruit_distance = self.fruit_distance()
                        if new_fruit_distance > fruit_distance:
                            reward = self.rewardFarther
                        else:
                            reward = self.rewardCloser
                            
                new_state = self.getState(snake, fruit, board)
                #Formula de Bellman
                self.qtable[str(state)][action] = (1 - self.learning_rate)\
                    * self.qtable[str(state)][action] + self.learning_rate\
                    * (reward + self.discount_rate * max(self.qtable[str(new_state)]))
                state = new_state
                
                steps_without_food = steps_without_food + 1 
                
            self.score.append(len(snake.body)-2)
            self.moves.append(moves)
            self.SaveQvalues()   
        
        print("Puntaje mas alto: "+str(max(self.score)))    
        with open('scores.json', 'w') as f:
            json.dump(self.score, f)
            
        with open('moves.json', 'w') as f:
            json.dump(self.moves, f)
    
obstaculos = True     
agent = AGENT()
agent.learn(obstaculos)