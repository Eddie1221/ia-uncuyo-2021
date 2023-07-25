from snake import GAME
import random
import json

class AGENT_RAND:
    def __init__(self) -> None:
        self.env = GAME()
        self.env.human = False
        self.num_episodes = 1000
        self.score = []
        
    def run_game(self):
        self.env = GAME()
        self.env.human = False
        self.env.run_game()
        
    def play(self):
        #Numero de episodios que el agente jugará el agente
        for i in range (1,self.num_episodes+1):
            print("Episodio: "+str(i)+"/"+str(self.num_episodes))
            self.run_game()
            snake = self.env.tablero.snake
            steps_without_food = 0
            while (steps_without_food < 1000 and (snake.isDeath == False)):
                self.env.jugada(random.choice([0,1,2,3]))
                steps_without_food = steps_without_food + 1 
                
            self.score.append(len(snake.body)-2)
            self.SaveQvalues()   
        
        print("Puntaje mas alto: "+str(max(self.score)))    
        with open('scoresRandom.json', 'w') as f:
            json.dump(self.score, f)
            
agente = AGENT_RAND()

agente.play()