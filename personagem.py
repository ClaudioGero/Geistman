import pygame
from abc import ABC, abstractmethod


class Personagem(ABC,pygame.sprite.Sprite):
    def __init__(self,altura,largura,velocidade,posInicial):
        self.altura=altura
        self.largura=largura
        self.velocidade=velocidade
        self.posInicial=posInicial
    @abstractmethod
    def movEsquerda():
        pass
    @abstractmethod
    def movDireita():
        pass
    @abstractmethod
    def movCima():
        pass
    @abstractmethod
    def movBaixo():
        pass