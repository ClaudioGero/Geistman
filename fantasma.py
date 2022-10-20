import pygame
from personagem import Personagem

class Fantasma(Personagem):
    def __init__(self,altura,largura,velocidade,posInicial) -> None:
        super().__init__(altura,largura,velocidade,posInicial)
        vulneravel = False
        pacMortos=0
        
    def movEsquerda(self):
        self.posInicial[0]-=10
    def movDireita(self):
        self.posInicial[0]+=10

    def movCima(self):
        self.posInicial[1]+=10

    def movBaixo(self):
        self.posInicial[1]-=10

