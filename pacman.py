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
        self.vulneravel = False
        self.ultima_tecla=''
        self.sprite = pygame.transform.scale(self.getsprite(), (1024/32+10, 768/24+10))
        self.rect=Rect(self.posInicial[0],self.posInicial[1],1024/32+10, 768/24+10)
        self.colide=False
    def getsprite(self):
        sprite=pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\inimigo.png')
        return sprite

    def movEsquerda(self):
        self.posInicial[0]-=self.velocidade
        self.ultima_tecla='a'
        if self.vulneravel==False:
            self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\pacmanLeft.png'), (1024/32+10, 768/24+10))
        elif self.vulneravel==True:
            self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\pacmanLeftVul.png'), (1024/32+10, 768/24+10))

        self.update()
    def movDireita(self):
        self.posInicial[0]+=self.velocidade
        self.ultima_tecla='d'
        if self.vulneravel==False:
            self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\pacmanRight.png'), (1024/32+10, 768/24+10))
        elif self.vulneravel==True:
            self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\pacmanRightVul.png'), (1024/32+10, 768/24+10))
        self.update()

    def movCima(self):
        self.posInicial[1]-=self.velocidade
        self.ultima_tecla='w'
        if self.vulneravel==False:
            self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\pacmanUp.png'), (1024/32+10, 768/24+10))
        elif self.vulneravel==True:
            self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\pacmanUpVul.png'), (1024/32+10, 768/24+10))
        self.update()
    def movBaixo(self):
        self.posInicial[1]+=self.velocidade
        self.ultima_tecla='s'
        if self.vulneravel==False:
            self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\pacmanDown.png'), (1024/32+10, 768/24+10))
        elif self.vulneravel==True:
            self.sprite = pygame.transform.scale(pygame.image.load('D:\Python\Thonny\Scripts\Geistman\sprites\pacmanDownVul.png'), (1024/32+10, 768/24+10))
        self.update()

    def update(self):
        self.rect=Rect(self.posInicial[0],self.posInicial[1],1024/32+10, 768/24+10)
    def prox_movimento(self):
        if self.colide == False:
            if self.ultima_tecla=='a':
                self.movEsquerda()
            if self.ultima_tecla=='d':
                self.movDireita()
            if self.ultima_tecla=='s':
                self.movBaixo()
            if self.ultima_tecla=='w':
                self.movCima()
        if self.colide:
            if self.ultima_tecla=='a':
                self.posInicial[0]+=self.velocidade
            if self.ultima_tecla=='d':
                self.posInicial[0]-=self.velocidade
            if self.ultima_tecla=='s':
                self.posInicial[1]-=self.velocidade
            if self.ultima_tecla=='w':
                self.posInicial[1]+=self.velocidade
            possiveis=['a','d','s','w']
            possiveis.remove(self.ultima_tecla)
            prox=random.randrange(0,3)
            if possiveis[prox] == 'a':
                self.movEsquerda()

            if possiveis[prox] == 'd':
                self.movDireita()

            if possiveis[prox] == 's':
                self.movBaixo()

            if possiveis[prox] == 'w':
                self.movCima()

            self.colide=False


    def colisao(self,blocos):
        if pygame.sprite.spritecollideany(self, blocos):
            self.colide=True
            self.prox_movimento()

        elif pygame.sprite.spritecollideany(self, blocos)==None:

            self.prox_movimento()
    def esta_vulneravel(self):

        self.vulneravel=True


