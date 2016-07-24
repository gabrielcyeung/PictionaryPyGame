from random import randint
#COLOUR
#Some colour tuple taken with permission from DANIEL PANG
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


#determines a random number that does not execeed the list length
def randomizer(x):
    number=randint(0,x-1)
    return number

#colour changing
def colour_change(mouse_position):
    if mouse_position[1]<140.83:
        colour=RED
        return colour
    elif mouse_position[1]<161.66:
        colour=FUCHSIA
        return colour
    elif mouse_position[1]<182.49:
        colour=PURPLE
        return colour
    elif mouse_position[1]<203.32:
        colour=BLUE
        return colour
    elif mouse_position[1]<224.15:
        colour=AQUA
        return colour
    elif mouse_position[1]<244.98:
        colour=WATER
        return colour
    elif mouse_position[1]<265.81:
        colour=GREEN
        return colour
    elif mouse_position[1]<286.64:
        colour=LIME
        return colour
    elif mouse_position[1]<307.47:
        colour=YELLOW
        return colour
    elif mouse_position[1]<328.3:
        colour=ORANGE
        return colour
    elif mouse_position[1]<349.13:
        colour=BROWN
        return colour
    elif mouse_position[1]<369.93:
        colour=BLACK
        return colour
    else:
        colour=WHITE
        return colour
