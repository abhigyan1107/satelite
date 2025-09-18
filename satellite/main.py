import pgzrun
import random

WIDTH = 700
HEIGHT = 420

number_of_satelites = 20
store_of_satelites = []

def create_satelite():
    for i in range(number_of_satelites):    
        satelite = Actor("satelite")
        satelite.pos = (random.randint(50,WIDTH - 50),random.randint(50,HEIGHT - 25))
        store_of_satelites.append(satelite) 

def draw():
    screen.blit("background",(0,0))
    number = 1
    for satelite in store_of_satelites:
        satelite.draw() 
        screen.draw.text(number,(satelite.pos[0],satelite.pos[1]+25))
create_satelite()

pgzrun.go()