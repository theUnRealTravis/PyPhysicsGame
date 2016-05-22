import pygame, sys
from pygame.locals import *

#Test Syncing
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
ORANGE = (255, 127,   0)
PURPLE = (127,   0, 127)
BLACK  = (  0,   0,   0)
GREY   = (127, 127, 127)
WHITE  = (255, 255, 255)

OBJECTS_LIST = []

class Brick:

    def __init__(self,x,y,width,height,color):
        self.collidedBrick = None
        self.collide = False
        self.change  = 1.0
        self.color   = color
        self.rect    = pygame.Rect(x,y,width,height)
        OBJECTS_LIST.append(self)
        
    def draw(self):
        pygame.draw.rect(WINDOW, self.color,self.rect)

    def drop(self):
        for i in OBJECTS_LIST:
            if self.rect.colliderect(i.rect) == 1 and self != i:
                self.collide = True
                self.collidedBrick = i
        if not self.collide:
            self.rect.y = max(0, min(275, self.rect.y + self.change*2))
            if self.change < 8:  
                self.change = self.change * 1.2
        else:
            if self.collidedBrick.rect.top > self.rect.top:
                self.rect.bottom = self.collidedBrick.rect.top

def main():

    brick1 = Brick(200,100,75,25,RED)
    brick2 = Brick(130,50,75,25,BLUE)

    while True:
        WINDOW.fill(WHITE)
        brick1.draw()
        brick1.drop()
        brick2.draw()
        brick2.drop()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPS_CLOCK.tick(FPS)
        
main()
