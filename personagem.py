import pygame
from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self,altura,largura,velocidade,posInicial):
        self.altura=altura
        self.largura=largura
        self.velocidade=velocidade
        self.posInicial=posInicial
        colisao=False
        sprite = ''
    def movEsquerda():
        pass
    def movDireita():
        pass
    def movCima():
        pass
    def movBaixo():
        pass