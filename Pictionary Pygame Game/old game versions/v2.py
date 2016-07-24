import pygame
from pygame.locals import *
pygame.init()

#COLOUR Variables
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(50,50,225)

my_clock=pygame.time.Clock()

screen=pygame.display.set_mode((640, 480), 0, 32)
screen.fill(WHITE)

#DEFAULT    
x=10
y=10
colour=BLACK

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            False

    #Checks to see what keys are being pressed. Corresponding Action
    keys=pygame.key.get_pressed()
    #direction changing
    if keys[pygame.K_DOWN]:
        y+=1
    elif keys[pygame.K_UP]:
        y-=1
    elif keys[pygame.K_LEFT]:
        x-=1
    elif keys[pygame.K_RIGHT]:
        x+=1
    #colour changing
    elif keys[pygame.K_F1]:
        colour=BLUE
    elif keys[pygame.K_F2]:
        colour=RED
    elif keys[pygame.K_F3]:
        colour=GREEN
    elif keys[pygame.K_F4]:
        colour=BLACK
    elif keys[pygame.K_F5]:
        colour=WHITE
    elif keys[pygame.K_F7]:
        screen.fill(WHITE)
        
    pygame.draw.circle(screen,colour, (x,y), 10)
    pygame.display.update()
    my_clock.tick(120)
    
pygame_quit()
