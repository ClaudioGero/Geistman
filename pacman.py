import pygame
import os
from personagem import Personagem
import random
import pygame
import os
from personagem import Personagem
from pygame.locals import *
import string


class Pacman(Personagem,pygame.sprite.Sprite):
    def __init__(self,altura,largura,velocidade,posInicial) -> None:
        pygame.sprite.Sprite.__init__(self)

        super().__init__(altura,largura,velocidade,posInicial)
        vulneravel = False
        self.ultima_tecla=''
        self.sprite = pygame.transform.scale(self.getsprite(), (1024/32+10, 768/24+10))
        self.rect=Rect(self.posInicial[0],self.posInicial[1],1024/32+10, 768/24+10)
        #self.movimento_inicial=False
    def getsprite(self):
        sprite=pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\inimigo.png')
        return sprite
    def prox_movimento(self,x):
        possiveis=['a','d','s','w']
        possiveis.remove(x)
        prox=random.randrange(0,3)
        if possiveis[prox] == 'a':
            self.movEsquerda()
        elif possiveis[prox] == 'd':
            self.movDireita()
        elif possiveis[prox] == 's':
            self.movBaixo()
        elif possiveis[prox] == 'w':
            self.movCima()

    def movEsquerda(self):
        self.posInicial[0]-=self.velocidade
        self.ultima_tecla='a'
        self.update()
    def movDireita(self):
        self.posInicial[0]+=self.velocidade
        self.ultima_tecla='d'
        self.update()

    def movCima(self,blocos):
        self.posInicial[1]-=self.velocidade
        self.ultima_tecla='w'
        self.update()
        self.colisao(blocos)
    def movBaixo(self):
        self.posInicial[1]+=self.velocidade
        self.ultima_tecla='s'
        self.update()

    def update(self):
        self.rect=Rect(self.posInicial[0],self.posInicial[1],1024/32+10, 768/24+10)
    def colisao(self,blocos):
        if pygame.sprite.spritecollideany(self, blocos):
            if self.ultima_tecla=='a':
                for i in range(0,2):
                    self.posInicial[0]+=self.velocidade
                self.prox_movimento('a')

            if self.ultima_tecla=='d':
                for i in range(0,2):
                    self.posInicial[0]-=self.velocidade
                self.prox_movimento('d')

            elif self.ultima_tecla=='w':
                for i in range(0,2):
                    self.posInicial[1]+=self.velocidade
                self.prox_movimento('w')
            elif self.ultima_tecla=='s':
                for i in range(0,2):
                    self.posInicial[1]-=self.velocidade
                self.prox_movimento('s')

    def sair(self):
        self.movCima()




