import pygame
from pygame.locals import *
from random import randint
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

#Getting the word from the text file
text_file=open("the_words.txt")
word=[]
for a in text_file:
    word += [a]
word_length=len(word)

def randomizer(x):
    number=randint(0,x-1)
    return number

word_number=randomizer(word_length)
the_special_word=word[word_number]


#DEFAULT (COLOUR + TIME) 
x=10
y=10
colour=BLACK
font=pygame.font.Font("Vera.ttf",16)
'''time_surface=font.render("Draw a(n) 'SUN'", True, (0,192,0))'''

while True:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            False

    #Checks to see what keys are being pressed. Corresponding Action
    keys=pygame.key.get_pressed()
    #direction changing
    '''if pygame.mouse.get_pressed(button1):
        mouse_position=pygame.mouse.get_pos()
    print mouse_position'''
        
        
    if keys[pygame.K_DOWN]:
        y+=1
    elif keys[pygame.K_UP]:
        y-=1
    elif keys[pygame.K_LEFT]:
        x-=1
    elif keys[pygame.K_RIGHT]:
        x+=1
    #colour changing
    elif keys[pygame.K_1]:
        colour=BLUE
    elif keys[pygame.K_2]:
        colour=RED
    elif keys[pygame.K_3]:
        colour=GREEN
    elif keys[pygame.K_4]:
        colour=BLACK
    elif keys[pygame.K_5]:
        colour=WHITE
    elif keys[pygame.K_7]:
        screen.fill(WHITE)
        word_number=randomizer(word_length)
        the_special_word=word[word_number]
      
    pygame.draw.circle(screen,colour, (x,y), 10)
    pygame.display.update()
    my_clock.tick(120)

     
    time_surface=font.render("Draw a(n) "+the_special_word.strip(),True, (0,192,0))
    screen.blit(time_surface,(230,20))
    

pygame_quit()
