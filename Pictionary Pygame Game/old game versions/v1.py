import pygame
from pygame.locals import *
pygame.init()

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,225)

my_clock=pygame.time.Clock()

screen=pygame.display.set_mode((640, 480), 0, 32)
screen.fill((0,0,0))
    
x=10
y=10
colour=WHITE
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN and K_RIGHT]:
        x+=1
        y+=1
    elif keys[pygame.K_LEFT and pygame.K_DOWN]:
        x-=1
        y+=1
    elif keys[pygame.K_UP and pygame.K_LEFT]:
        x-=1
        y-=1
    elif keys[pygame.K_RIGHT and pygame.K_UP]:
        x+=1
        y-=1
    elif keys[pygame.K_DOWN]:
        y+=1
    elif keys[pygame.K_UP]:
        y-=1
    elif keys[pygame.K_LEFT]:
        x-=1
    elif keys[pygame.K_RIGHT]:
        x+=1
    elif keys[pygame.K_F1]:
        colour=BLUE
    elif keys[pygame.K_F2]:
        colour=WHITE
    elif keys[pygame.K_F3]:
        colour=RED
    elif keys[pygame.K_F4]:
        colour=GREEN
    elif keys[pygame.K_F5]:
        colour=BLACK
    elif keys[pygame.K_F7]:
        screen.fill(BLACK)
    pygame.draw.circle(screen, colour, (x,y), 10)
    pygame.display.update()
    my_clock.tick(120)
    
pygame_quit()
