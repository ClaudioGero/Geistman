from msilib.schema import Directory
import pygame
import os
from personagem import Personagem

from msilib.schema import Directory
import pygame
import os
from personagem import Personagem

class Fantasma(Personagem):
    def __init__(self,altura,largura,velocidade,posInicial) -> None:
        super().__init__(altura,largura,velocidade,posInicial)
        vulneravel = False
        pacMortos=0
    def getsprite(self):
        sprite=pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\player.png')
        return sprite
    def movEsquerda(self):
        self.posInicial[0]-=self.velocidade
    def movDireita(self):
        self.posInicial[0]+=self.velocidade

    def movCima(self):
        self.posInicial[1]-=self.velocidade

    def movBaixo(self):
        self.posInicial[1]+=self.velocidade





