import pygame
from pygame.locals import *
from random import randint
pygame.init()

#COLOUR 
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
LIME=(0,255,0)
BLUE=(50,50,225)
GREEN=(0,128,0)
AQUA=(0,255,255)
WATER=(100,149,237)
FUCHSIA=(255,0,255)
PURPLE=(128,0,128)
YELLOW=(255,255,0)
ORANGE=(255,102,0)

my_clock=pygame.time.Clock()

#SCREEN DIMENSION AND BACKGROUND COLOUR
screen=pygame.display.set_mode((640, 480), 0, 32)
screen.fill(WHITE)

#FILE READING
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

#PICTURES
palette = pygame.image.load('panel.png')
palette = pygame.transform.scale(palette, (150,100))

#GAME STARTS HERE
while True:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            False
        #Draw where ever the mouse is clicked
        #Button 1 (left click) = draw w/ black
        if pygame.mouse.get_pressed()[0]:
           mouse_position=pygame.mouse.get_pos()
           pygame.draw.circle(screen,colour,(mouse_position),10)
        #Button 2 (right click) = draw/white or erase
        if pygame.mouse.get_pressed()[2]:
           mouse_position=pygame.mouse.get_pos()
           pygame.draw.circle(screen,WHITE,(mouse_position),10)

    #Checks to see what keys are being pressed. Corresponding Action
    keys=pygame.key.get_pressed() 
    #colour changing
    if keys[pygame.K_1]:
        colour=BLUE
    elif keys[pygame.K_2]:
        colour=RED
    elif keys[pygame.K_3]:
        colour=GREEN
    elif keys[pygame.K_4]:
        colour=BLACK
    elif keys[pygame.K_5]:
        colour=AQUA
    elif keys[pygame.K_6]:
        colour=WATER
    elif keys[pygame.K_7]:
        colour=FUCHSIA
    elif keys[pygame.K_8]:
        colour=PURPLE
    elif keys[pygame.K_9]:
        colour=YELLOW
    elif keys[pygame.K_0]:
        colour=ORANGE
    elif keys[pygame.K_r]:
        screen.fill(WHITE)
        word_number=randomizer(word_length)
        the_special_word=word[word_number]
    elif keys[pygame.K_s]:        
        pygame.image.save(screen,"latest_drawing.jpg")
        
        
    pygame.display.update()
    my_clock.tick(120) #120 FPS

    #Prints out the word to draw 
    time_surface=font.render("Draw a(n) "+the_special_word.strip(),True, (0,192,0))
    screen.blit(time_surface,(230,20))

    #Corner image
    screen.blit(palette, (450,340))
    

pygame_quit()
