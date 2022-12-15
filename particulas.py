import pygame
from pygame.locals import *
class Particula:
    def __init__(self,display,x,y):
        self.x=x
        self.y=y
        self.display=display
        self.sprite = pygame.draw.circle(self.display,'yellow', (x,y),20)
        self.rect= Rect(x,y,1024/32+10,768/24+10)
    def desenhar(self):
        self.sprite = pygame.draw.circle(self.display,'yellow', (self.x,self.y),20)
