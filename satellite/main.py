import pgzrun
import random

WIDTH = 700
HEIGHT = 420

number_of_satelites = 10
store_of_satelites = []
next_satelite = 0 

lines = []

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
        screen.draw.text(str(number),(satelite.pos[0],satelite.pos[1]+25))
        number = number + 1
    for i in lines:
        screen.draw.line(i[0],i[1],(255,255,255))

create_satelite()

def on_mouse_down(pos):
    global lines , next_satelite
    if next_satelite < number_of_satelites:
        if store_of_satelites[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((store_of_satelites[next_satelite - 1].pos,store_of_satelites[next_satelite].pos))
            next_satelite += 1
        else:
            next_satelite = 0 
            lines = []


pgzrun.go()
