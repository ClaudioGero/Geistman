from msilib.schema import Directory
import pygame
import os
from personagem import Personagem
from pygame.locals import *

class Fantasma(Personagem,pygame.sprite.Sprite):
    def __init__(self,altura,largura,velocidade,posInicial) -> None:
        pygame.sprite.Sprite.__init__(self)
        super().__init__(altura,largura,velocidade,posInicial)
        self.vulneravel = False
        self.blocked=False
        self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\geistRight.png'), (1024/32+10, 768/24+10))
        self.rect = self.sprite.get_rect()
        self.display = pygame.display.set_mode([1024, 768])
    def getsprite(self,x):
        spritee=pygame.image.load(x)
        self.sprite =pygame.transform.scale(spritee, (1024/32+10, 768/24+10))
    
    def movEsquerda(self):
        if self.blocked==False:
            self.posInicial[0]-=self.velocidade
            self.getsprite('D:\Python\Thonny\Scripts\Geistman\sprites\geistLeft.png')
            self.update()
    def movDireita(self):
        if self.blocked==False:
            self.posInicial[0]+=self.velocidade
            self.getsprite('D:\Python\Thonny\Scripts\Geistman\sprites\geistRight.png')
            self.update()
    def movCima(self):
        if self.blocked==False:
            self.posInicial[1]-=self.velocidade
            self.getsprite('D:\Python\Thonny\Scripts\Geistman\sprites\geistUp.png')
            self.update()

    def movBaixo(self):
        if self.blocked==False:
            self.posInicial[1]+=self.velocidade
            self.getsprite('D:\Python\Thonny\Scripts\Geistman\sprites\geistDown.png')
            self.update()
    def update(self):
        self.rect=Rect(self.posInicial[0],self.posInicial[1],1024/32+10, 768/24+10)
    
