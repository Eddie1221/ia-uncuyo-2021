import pygame as pg
import random
from pygame.math import Vector2

class SNAKE:
    def __init__(self, cell_num, cell_size, screen):
        self.cell_num = cell_num
        self.cell_size = cell_size
        self.screen = screen
        self.isDeath = False
        self.randomize()
        self.newBlock = False
        
    def randomize(self):
        self.body = [Vector2(random.randint(3,self.cell_num-3), random.randint(3,self.cell_num-3))]
        self.direction = random.choice([Vector2(1,0), Vector2(-1,0), Vector2(0,1), Vector2(0,-1)])
        self.body.append(self.body[0]-self.direction)
        
    def draw_snake(self):
        for block in self.body:
            #crear rectangulo
            block_rect = pg.Rect(block.x*self.cell_size, block.y*self.cell_size, self.cell_size, self.cell_size)
            #dibujar el rectangulo
            pg.draw.rect(self.screen, pg.Color('green'), block_rect)
            
    def move_snake(self):
        if self.newBlock == False:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
        else:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.newBlock = False
        
    def add_block(self):
        self.newBlock = True


class FRUIT:
    def __init__(self, cell_num, cell_size, screen):
        self.cell_num = cell_num
        self.cell_size = cell_size
        self.screen = screen
        self.randomize()
        
    #dibujar un cuadradro (la fruta)    
    def draw_fruit(self):
        #crear un rectangulo
        fruit_rect = pg.Rect(self.pos.x*self.cell_size, self.pos.y*self.cell_size, self.cell_size, self.cell_size)
        #dibujar el recangulo
        pg.draw.rect(self.screen, pg.Color('red'), fruit_rect)
        
    def randomize(self):
        #crear posicion de la fruta
        self.x = random.randint(0,self.cell_num-1)
        self.y = random.randint(0,self.cell_num-1)
        self.pos = Vector2(self.x, self.y)

class BOARD:
    def __init__(self, cell_num, cell_size, screen, font, obstSWITCH) -> None:
        self.cell_num = cell_num
        self.cell_size = cell_size
        self.screen = screen
        self.font = font
        self.obst = []
        if obstSWITCH == True:
            self.obst = self.generateObstacles()
            
        self.snake = SNAKE(cell_num, cell_size, screen)
        switch = True
        while switch == True:
            switch = False
            for block in self.snake.body:
                if block in self.obst:
                    switch = True
                    
            if switch == True:
                self.snake.randomize()
        
        self.fruit = FRUIT(cell_num, cell_size, screen)
        switch = True
        while switch == True:
            if self.fruit.pos in self.obst:
                switch = True
                self.fruit.randomize()
            else:
                switch = False
            
    def generateObstacles(self):
        obstacles = []
        for y in range(1,self.cell_num-1):
            for x in range(1,self.cell_num-1):
                if random.random() < 0.02:
                    if self.cheackObstacle(x,y, obstacles) == False:
                        obstacles.append(Vector2(x,y))
                    
        return obstacles
    
    #Funcion para asegurar que no hayan osbtaculos adyacentes
    def cheackObstacle(self, x, y, obstacles):
        surroundings = False
        
        if Vector2(x,y-1) in obstacles:
            surroundings = True
        if Vector2(x-1,y-1) in obstacles:
            surroundings = True
        if Vector2(x+1,y-1) in obstacles:
            surroundings = True
        if Vector2(x-1,y) in obstacles:
            surroundings = True
            
        return surroundings

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_obstacles()
        self.draw_score()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #Reposicionar la fruta
            self.fruit.randomize()
            switch = True
            while switch == True:
                if self.fruit.pos in self.obst:
                    switch = True
                    self.fruit.randomize()
                else:
                    switch = False
            
            #Crecer la serpiente
            self.snake.add_block()
            
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            
    def game_over(self):
        self.snake.isDeath = True
        
    def check_fail(self):
        #CHECK PARA CHOQUE EN LAS PAREDES
        #check para saber si la cabeza golpea la paredes laterales
        if not (0 <= self.snake.body[0].x < self.cell_num):
            self.game_over()
            
        #check para saber si la cabeza golpea la paredes superior e inferior
        if not (0 <= self.snake.body[0].y < self.cell_num):
            self.game_over()
            
        #CHEACK PARA CHOQUE CON OBSTACULOS
        if self.snake.body[0] in self.obst:
            self.game_over()
            
        #CHECK PARA CHOQUE CONTRA EL CUERPO DE LA SERPIENTE
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    def draw_score(self):
        score_text = str((len(self.snake.body)-2)*10)
        score_surface = self.font.render(score_text,False,pg.Color('white'))
        score_x = 20
        score_y = self.cell_size * self.cell_num - 40
        score_rect = score_surface.get_rect(topleft = (score_x,score_y))
        self.screen.blit(score_surface,score_rect)
        
    def draw_obstacles(self):
        for block in self.obst:
            #crear rectangulo
            block_rect = pg.Rect(block.x*self.cell_size, block.y*self.cell_size, self.cell_size, self.cell_size)
            #dibujar el rectangulo
            pg.draw.rect(self.screen, pg.Color('blue'), block_rect)
        

#Se encerró el proceso de correr el juego en la clase GAME
class GAME:
    def __init__(self) -> None:
        self.human = True
        self.tablero = None
    
    def run_game(self, switchObstacles):    
        pg.init()
        cell_size = 20
        cell_num = 30
        game_font = pg.font.Font(None,25)
        self.screen = pg.display.set_mode((cell_num*cell_size,cell_num*cell_size))
        self.clock = pg.time.Clock()

        self.tablero = BOARD(cell_num, cell_size, self.screen, game_font, switchObstacles)

        if self.human == True:
            SCREEN_UPDATE = pg.USEREVENT
            pg.time.set_timer(SCREEN_UPDATE, 150)

            #En este bucle se dibujan todos los elementos por pantalla
            while True:

                #Para cerrar el juego se necesita un "event loop" que detecte cuando se cierre la ventana
                for event in pg.event.get():
                    #detecta cuando se cierre la ventana
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()

                    if event.type == SCREEN_UPDATE:
                        self.tablero.update()
                        if self.tablero.snake.isDeath == True:
                            pg.quit()

                    #Cambiar la dirección de la serpiente
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_UP:
                            self.move_up()
                        if event.key == pg.K_DOWN:
                            self.move_down()
                        if event.key == pg.K_LEFT:
                            self.move_left()
                        if event.key == pg.K_RIGHT:
                            self.move_right()

                if self.tablero.snake.isDeath == False:
                    self.screen.fill(pg.Color('black'))
                    self.tablero.draw_elements()  
                    pg.display.update()
                    self.clock.tick(60)  #ajusta el framerate maximo a 60
                else:
                    pg.quit()
        else:
            self.tablero.update()
            self.screen.fill(pg.Color('black'))
            self.tablero.draw_elements()  
            pg.display.update()
            self.clock.tick(60)  #ajusta el framerate maximo a 60   
    
    #Función que le permite al agente realizar una acción en el juego
    def jugada(self, action):
        
        for event in pg.event.get():
            #detecta cuando se cierre la ventana
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        
        match action:
            case 0: #Izquierda
                self.move_left()
            case 1: #Derecha
                self.move_right()
            case 2: #Arriba
                self.move_up()
            case 3: #Abajo
                self.move_down()
                
        #print(self.tablero.snake.isDeath)
        if self.tablero.snake.isDeath == False:
            self.tablero.update()
            self.screen.fill(pg.Color('black'))
            self.tablero.draw_elements()  
            pg.display.update()
            self.clock.tick(500)  #ajusta el framerate maximo
        else:
            pg.quit()
            
    #Funciones de movimientos, para que el agente pueda llamarlas al jugar al snake
    def move_up(self):
        if self.tablero.snake.body[1] != self.tablero.snake.body[0] + Vector2(0,-1):
            self.tablero.snake.direction = Vector2(0,-1)
            
    def move_down(self):
        if self.tablero.snake.body[1] != self.tablero.snake.body[0] + Vector2(0,1):
            self.tablero.snake.direction = Vector2(0,1)
            
    def move_left(self):
        if self.tablero.snake.body[1] != self.tablero.snake.body[0] + Vector2(-1,0):
            self.tablero.snake.direction = Vector2(-1,0)
    
    def move_right(self):
        if self.tablero.snake.body[1] != self.tablero.snake.body[0] + Vector2(1,0):
            self.tablero.snake.direction = Vector2(1,0)