import pygame
from fantasma import Fantasma
from personagem import Personagem
class Control():

    pygame.init()
    pygame.display.set_caption("Jogo do grupo 2")

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.display = pygame.display.set_mode([1024, 768])
        self.menu_loop()
        fantasma = Fantasma(50,50,0,[40,50])
        '''criar player
        criar sprites
        '''
        
    def menu_loop(self):
        menuLoop = True
        while menuLoop:
            self.display.fill((0,0,0))

            self.clock.tick(self.FPS)  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menuLoop = False

            pygame.display.update()
    def game_loop(self):
        gameLoop = True
        while gameLoop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:     
                    if event.key == pygame.K_d:
                        self.fantasma.movDireita()
                    if event.key == pygame.K_a:
                        self.fantasma.movEsquerda()
                    if event.key == pygame.K_w:
                        self.fantasma.movCima()
                    if event.key == pygame.K_s:
                        self.fantasma.movBaixo()


x=Control()

