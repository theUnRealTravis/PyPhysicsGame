import pygame, sys
from pygame.locals import *


pygame.init()

FPS       = 30
FPS_CLOCK = pygame.time.Clock()

WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('PHYSICS SANDBOX')

RED    = (255,   0,   0)
YELLOW = (255, 255,   0)
BLUE   = (  0,   0, 255)
GREEN  = (255, 255,   0)
ORANGE = (255, 127,   0)#!
PURPLE = (127,   0, 127)
BLACK  = (  0,   0,   0)
GREY   = (127, 127, 127)
WHITE  = (255, 255, 255)

OBJECTS_LIST = []

class Brick:

    def __init__(self,x,y,width,height,color):
        self.change = 1.0
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height
        self.color  = color
        OBJECTS_LIST.append(self)

    def draw(self):
        pygame.draw.rect(WINDOW, self.color,(self.x, self.y, self.width, self.height))

    def drop(self):
        self.y = max(0, min(275, self.y + self.change*2))
        if self.change < 8:  
            self.change = self.change * 1.2

def main():

    brick1 = Brick(200,150,75,25,BLACK)

    while True:
        WINDOW.fill(WHITE)
        brick1.draw()
        brick1.drop()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
        
main()
