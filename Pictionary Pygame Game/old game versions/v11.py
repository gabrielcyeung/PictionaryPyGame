
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
BEIGE=(245,241,222)

my_clock=pygame.time.Clock()

#SCREEN DIMENSION AND BACKGROUND COLOUR
screen=pygame.display.set_mode((640, 480), 0, 32)
screen.fill(BEIGE)

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
bigger_font=pygame.font.Font("Vera.ttf", 30)
'''time=60
pygame.time.set_timer(USEREVENT+1, 1000) #1 second is 1000 milliseconds'''
playing=True
state=0
word_delay=0

#PICTURES
palette = pygame.image.load('panel.png')
palette = pygame.transform.scale(palette, (150,100))
logo = pygame.image.load('logo.png')
gear = pygame.image.load('gear.png')
gear = pygame.transform.scale(gear, (30,30))

'''------------------------------------------'''
while playing== True:
    
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                playing==False 

    if state==0:
        screen.blit(logo, (115,40))
        font=pygame.font.Font("Vera.ttf",16)
        title_surface=font.render("The Unofficial python game",True, WATER)
        screen.blit(title_surface,(210,200))
        start_surface=font.render("Press the 'a' key to start the game", True, GREEN)
        trigger_instruction=font.render("Press the 'i' key to get instructions", True, GREEN)
        screen.blit(start_surface, (170,230))
        screen.blit(trigger_instruction, (170,250))
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            print "a was pressed in state==0"
            screen.fill(BEIGE)
            state=1
        elif keys[pygame.K_i]:
            print "i was pressed in state==0"
            screen.fill(BEIGE)
            state=3

        pygame.display.update()
        

    if state==1:
        
        if word_delay<1500: 
            screen.blit(logo, (115,0))

            #Prints out the word to draw
            word_surface=font.render("Draw this:",True, GREEN)
            screen.blit(word_surface,(230,150))

            draw_it=bigger_font.render(the_special_word.strip(),True,GREEN)
            screen.blit(draw_it, (240, 170))
            word_delay+=1
            
        else:
            screen.fill(BEIGE)
            state=2

        #LAST UPDATE HERE

    
           
        pygame.display.update()
                                           
    if state==2:
        screen.blit(logo, (115,0))
            #Time
        #if event.type == USEREVENT+1:
                #time -= 1
        mouse_position=pygame.mouse.get_pos()
        #print mouse_position
       
        #Draw where ever the mouse is clicked               
        #black
        if pygame.mouse.get_pressed()[0]:
           pygame.draw.circle(screen,colour,(mouse_position),10)
        #white or erase
        elif pygame.mouse.get_pressed()[2]:
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
            state=1
            word_delay=0
            screen.fill(BEIGE)
        elif keys[pygame.K_s]:        
            pygame.image.save(screen,"latest_drawing.jpg")
       
        

        #Corner image
        screen.blit(gear, (600,10))
        gear_image=screen.blit(gear, (600,10))
    
        my_clock.tick(120) #120 FPS
        
        pygame.display.update()

pygame_quit()

