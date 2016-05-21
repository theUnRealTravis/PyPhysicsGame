import pygame, sys
from pygame.locals import *


pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('PYSICS SANDBOX')

RED   = (255,   0,   0)
GREEN = (255, 255,   0)
BLUE  = (  0,   0, 255)
BLACK = (  0,   0,   0)
GREY  = (127, 127, 127)
WHITE = (255, 255, 255)


def main():

    x = 0.0
    y = 0.0
    change = 1.0
    
    while True:
        DISPLAYSURF.fill(WHITE)
        pygame.draw.rect(DISPLAYSURF, RED,(x, y, 75, 25))
        y = max(0, min(275, y + change*2))
        if change < 8:  
            change = change * 1.2
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
        
main()
