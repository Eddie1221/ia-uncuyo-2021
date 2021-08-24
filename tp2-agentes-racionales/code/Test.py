from random import*
from Enviroment import Enviroment
from Agent import Agent

x = 128

Floor = Enviroment(x,x,randint(0,x-1),randint(0,x-1),0.1)
Aspiradora = Agent(Floor)
Aspiradora.think()
print("========0.1========")
print("PERFORMANCE: ")
print(Floor.get_performance())
print("")

Floor = Enviroment(x,x,randint(0,x-1),randint(0,x-1),0.2)
Aspiradora = Agent(Floor)
Aspiradora.think()
print("========0.2========")
print("PERFORMANCE: ")
print(Floor.get_performance())
print("")

Floor = Enviroment(x,x,randint(0,x-1),randint(0,x-1),0.4)
Aspiradora = Agent(Floor)
Aspiradora.think()
print("========0.4========")
print("PERFORMANCE: ")
print(Floor.get_performance())
print("")

Floor = Enviroment(x,x,randint(0,x-1),randint(0,x-1),0.8)
Aspiradora = Agent(Floor)
Aspiradora.think()
print("========0.8========")
print("PERFORMANCE: ")
print(Floor.get_performance())
print("")