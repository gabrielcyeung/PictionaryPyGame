import pygame
from pygame.locals import *
from my_functions import randomizer
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
BROWN=(139,69,19)

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

word_number=randomizer(word_length)
the_special_word=word[word_number]


#DEFAULT (COLOUR + TIME) 
x=10
y=10
colour=BLACK
font=pygame.font.Font("Vera.ttf",16)
bigger_font=pygame.font.Font("Vera.ttf", 30)
biggest_font=pygame.font.Font("Vera.ttf",50)
'''time=60
pygame.time.set_timer(USEREVENT+1, 1000) #1 second is 1000 milliseconds'''
playing=True
state=0
word_delay=0
player_number=1
player_delay=0

#PICTURES
palette = pygame.image.load('panel.png')
palette = pygame.transform.scale(palette, (150,100))
logo = pygame.image.load('logo.png')
restart = pygame.image.load('restart.png')
restart = pygame.transform.scale(restart, (30,30))
    

'''------------------------------------------'''
while playing== True:
    
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                playing==False 

    #MAIN MENU
    if state==0:
        screen.blit(logo, (115,40))
        font=pygame.font.Font("Vera.ttf",16)
        title_surface=font.render("The Unofficial python game",True, WATER)
        screen.blit(title_surface,(210,200))
        start_surface=font.render("Press the 'a' key to start the game", True, GREEN)
        #trigger_instruction=font.render("Press the 'i' key to get instructions", True, GREEN)
        screen.blit(start_surface, (170,230))
        #screen.blit(trigger_instruction, (170,250))
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            print "a was pressed in state==0"
            screen.fill(BEIGE)
            state=1
        '''elif keys[pygame.K_i]:
            print "i was pressed in state==0"
            screen.fill(BEIGE)
            state=3'''

        pygame.display.update()
        
    if state==1:
        #Determining if it's player 1 or player 2
        if player_number%2==0:
            player="2"
        else:
            player="1"

        #Displays which player's turn it is 
        if player_delay<720:            
            screen.blit(logo, (115,0))
            player_surface=biggest_font.render("Player "+player+"'s turn", True, WATER)
            screen.blit(player_surface, (145,200))
            player_delay+=1
        else:
            screen.fill(BEIGE)
            #Holds screen for 5 minutes
            if word_delay<600:
                screen.blit(logo, (115,0))
                #Prints out the word to draw
                word_surface=font.render("Draw this:",True, WATER)
                screen.blit(word_surface,(230,150))

                draw_it=bigger_font.render(the_special_word.strip(),True,BLUE)
                screen.blit(draw_it, (240, 170))
                word_delay+=1
                
            else:
                screen.fill(BEIGE)
                state=2    
               
        pygame.display.update()
                                           
    if state==2:
        screen.blit(logo, (115,0))

        #Colour Tool Rectangles
        pygame.draw.rect(screen, BLACK, (600,120,20,270.76))
        pygame.draw.rect(screen, RED, (600,120,20,20.83))
        pygame.draw.rect(screen, FUCHSIA, (600, 140.83,20,20.83))
        pygame.draw.rect(screen, PURPLE, (600, 161.66,20,20.83))
        pygame.draw.rect(screen, BLUE, (600, 182.49,20,20.83))
        pygame.draw.rect(screen, AQUA, (600, 203.32,20,20.83))
        pygame.draw.rect(screen, WATER, (600, 224.15,20,20.83))
        pygame.draw.rect(screen, GREEN, (600, 244.98,20,20.83))
        pygame.draw.rect(screen, LIME, (600, 265.81,20,20.83))
        pygame.draw.rect(screen, YELLOW, (600, 286.64,20,20.83))
        pygame.draw.rect(screen, ORANGE, (600, 307.47,20,20.83))
        pygame.draw.rect(screen, BROWN, (600, 328.3,20,20.83))
        pygame.draw.rect(screen, BLACK, (600, 349.13,20,20.83))
        pygame.draw.rect(screen, WHITE, (600, 369.93,20,20.83))
        

        #Checks to see what keys are being pressed. Corresponding Action
        keys=pygame.key.get_pressed()
        #hot keys colour changing
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
            player_delay=0
            screen.fill(BEIGE)
            player_number+=1
        elif keys[pygame.K_s]:        
            pygame.image.save(screen,"latest_drawing.jpg")
        
        #Left clicks
        if pygame.mouse.get_pressed()[0]:
            #Check mouse position to determine what to do. Draw or change colour.
            mouse_position=pygame.mouse.get_pos()
            if mouse_position[0]>600 and mouse_position[0]<620 and mouse_position[1]>120 and mouse_position[1]<390.76:
                print "TRUE"
            else:
                print "FALSE"
                #pygame.draw.circle(screen,colour,(mouse_position),5)
                

        #Right click --> to erase
        if pygame.mouse.get_pressed()[2]:
           pygame.draw.circle(screen,BEIGE,(mouse_position),10)
           

        #Restart button
        screen.blit(restart, (600,10))
        gear_image=screen.blit(restart, (600,10))
    
        my_clock.tick(120) #120 FPS
        
        pygame.display.update()

pygame_quit()

