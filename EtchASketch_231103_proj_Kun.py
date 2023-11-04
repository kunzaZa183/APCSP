#etch a sketch

import pygame, sys
from pygame.locals import *

# Initialize the screen
pygame.init()
screen = pygame.display.set_mode((800,600))

#set the initial postion to start drawing
x = 350
y = 250

#draw the starting screen
screen.fill((255,255,255))
pygame.display.update()

first = True
p1 = (x,y)
line_color = (0, 255, 0)

#Event Loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        elif event.type==KEYUP:    
            
            #make p1 using the current x and y

            if event.key==K_RETURN:
                if first: 
                    p1 = (x,y)
                    first = False
                else:
                    pygame.draw.line(screen, line_color, p1, (x,y))
                    first = True
            
            #move up
            if event.key==K_UP: 
                y = y - 10

            #move down
            if event.key==K_DOWN: 
                y = y + 10

            #move left
            if event.key==K_LEFT: 
                x = x - 10

            #move right
            if event.key==K_RIGHT: 
                x = x + 10
                
            pygame.display.update()