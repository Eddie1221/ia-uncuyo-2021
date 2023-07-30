from snake import GAME
import random
import json
import numpy as np
from keras import Sequential
from collections import deque
from keras.layers import Dense
from keras.optimizers import Adam
from pygame.math import Vector2


class DQN:

    """ Deep Q Network """

    def __init__(self, env, params):

        self.env = env
        self.action_space = 4
        self.state_space = 12
        self.epsilon = params['epsilon'] 
        self.gamma = params['gamma'] 
        self.batch_size = params['batch_size'] 
        self.epsilon_min = params['epsilon_min'] 
        self.epsilon_decay = params['epsilon_decay'] 
        self.learning_rate = params['learning_rate']
        self.layer_sizes = params['layer_sizes']
        self.memory = deque(maxlen=2500)
        self.model = self.build_model()
        self.score = []
        self.moves = []


    def build_model(self):
        model = Sequential()
        for i in range(len(self.layer_sizes)):
            if i == 0:
                model.add(Dense(self.layer_sizes[i], input_shape=(self.state_space,), activation='relu'))
            else:
                model.add(Dense(self.layer_sizes[i], activation='relu'))
        model.add(Dense(self.action_space, activation='softmax'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model


    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))


    def act(self, state):

        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_space)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])


    def replay(self):

        if len(self.memory) < self.batch_size:
            return

        minibatch = random.sample(self.memory, self.batch_size)
        states = np.array([i[0] for i in minibatch])
        actions = np.array([i[1] for i in minibatch])
        rewards = np.array([i[2] for i in minibatch])
        next_states = np.array([i[3] for i in minibatch])
        dones = np.array([i[4] for i in minibatch])

        states = np.squeeze(states)
        next_states = np.squeeze(next_states)

        targets = rewards + self.gamma*(np.amax(self.model.predict_on_batch(next_states), axis=1))*(1-dones)
        targets_full = self.model.predict_on_batch(states)

        ind = np.array([i for i in range(self.batch_size)])
        targets_full[[ind], [actions]] = targets

        self.model.fit(states, targets_full, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
            
    def fruit_distance(self):
        return abs(self.env.tablero.snake.body[0].x - self.env.tablero.fruit.x) + abs(self.env.tablero.snake.body[0].y - self.env.tablero.fruit.y)
    
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
            
    def getState(self, serpiente, fruta, tablero):
        danger = self.detectDanger(tablero, serpiente)
        cabeza = serpiente.body[0]
        
        dist_x = fruta.x - cabeza.x
        dist_y = fruta.y - cabeza.y
        
        pos_xL = pos_xR = 0
        if dist_x < 0:
            pos_xL = 1  
        elif dist_x > 0:
            pos_xR = 1
            
        pos_yU = pos_yD = 0
        if dist_y < 0:
            pos_yU = 1
        elif dist_y > 0:
            pos_yD = 1
            
        directionL = directionR = directionU = directionD = 0
        if serpiente.direction == Vector2(-1,0):
            directionL = 1
        elif serpiente.direction == Vector2(1,0):
             directionR = 1
        elif serpiente.direction == Vector2(0,-1):
            directionU = 1
        elif serpiente.direction == Vector2(0,1):
            directionD = 1
                
        estado = (pos_xL, pos_xR, pos_yU, pos_yD, 
                  danger[0], danger[1], danger[2], danger[3], 
                  directionL, directionR, directionU, directionD)
        return estado


def train_dqn(episode, env):

    sum_of_rewards = []
    agent = DQN(env, params)
    for e in range(episode):
        moves = 0
        env.run_game(False)
        snake = env.tablero.snake
        fruit = env.tablero.fruit
        board = env.tablero
        state = agent.getState(snake,fruit,board)
        state = np.reshape(state, (1, agent.state_space))
        score = 0
        max_steps = 10000
        for i in range(max_steps):
            snake_length = len(snake.body)
            fruit_distance = agent.fruit_distance()
            action = agent.act(state)
            # print(action)
            prev_state = state
            env.jugada(action)
            moves = moves + 1
            next_state = agent.getState(snake,fruit,board)
            
            if snake.isDeath == True:
                done = True
                reward = -100
            else:
                done = False
                new_snake_length = len(snake.body)
                if new_snake_length > snake_length:
                    reward = 10
                else:
                    new_fruit_distance = agent.fruit_distance()
                    if new_fruit_distance > fruit_distance:
                        reward = -1
                    else:
                        reward = 1
             
            score += reward
            next_state = np.reshape(next_state, (1, agent.state_space))
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if params['batch_size'] > 1:
                agent.replay()
            if done:
                print(f'final state before dying: {str(prev_state)}')
                print(f'episode: {e+1}/{episode}, score: {score}')
                break
        agent.score.append(len(snake.body)-2)
        agent.moves.append(moves)
        sum_of_rewards.append(score)
        
    with open('1%.json', 'w') as f:
        json.dump(agent.score, f)
            
    with open('M1%.json', 'w') as f:
        json.dump(agent.moves, f)
    return sum_of_rewards

    


if __name__ == '__main__':

    params = dict()
    params['name'] = None
    params['epsilon'] = 1
    params['gamma'] = .95
    params['batch_size'] = 350
    params['epsilon_min'] = .0001
    params['epsilon_decay'] = .995
    params['learning_rate'] = 0.001
    params['layer_sizes'] = [128, 128, 128]

    results = dict()
    ep = 250

    env_infos = {'States: only walls':{'state_space':'no body knowledge'}, 'States: direction 0 or 1':{'state_space':''}, 'States: coordinates':{'state_space':'coordinates'}, 'States: no direction':{'state_space':'no direction'}}

    env = GAME()
    env.human = False
    sum_of_rewards = train_dqn(ep, env)
    results[params['name']] = sum_of_rewards