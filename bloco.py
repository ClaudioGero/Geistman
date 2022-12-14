import pygame
from pygame.locals import *
class Bloco(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.transform.scale(self.getsprite(), (1024/32+10, 768/24+10))
        self.rect= Rect(x,y,1024/32+10,768/24+10)
    def getsprite(self):
        return pygame.image.load("D:\Python\Thonny\Scripts\Geistman\sprites\obloco.jpg")