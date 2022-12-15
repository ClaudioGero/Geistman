import pygame
from fantasma import Fantasma
from pacman import Pacman
from personagem import Personagem
from mapa import Mapa
import os
from bloco import Bloco
from particulas import Particula
import random

class Control():

    pygame.display.set_caption("GEIST-MAN")

    def __init__(self):
        pygame.init()
        self.font0="comic sans ms"
        self.FONT0=pygame.font.match_font(self.font0)
        self.black = (0,0,0)
        self.white=(255,255,255)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.display = pygame.display.set_mode([1024, 768]) #  768
        self.fantasma = Fantasma(50,50,10,[500,600])
        self.blocos = pygame.sprite.Group()
        self.inimigo1 = Pacman(20,20,10,[450,400])
        self.inimigo_saiu=False
        self.inimigo2 = Pacman(20,20,10,[500,400])
        self.inimigo3 = Pacman(20,20,10,[550,400])
        self.inimigos = [self.inimigo1,self.inimigo2,self.inimigo3]
        self.particula1=Particula(self.display,100,100)
        self.particula2=Particula(self.display,800,500)
        self.particula3=Particula(self.display,100,500)
        self.particula4=Particula(self.display,800,100)
        self.particulas=[self.particula1,self.particula2,self.particula3,self.particula4]
        self.mapaa=Mapa()
        self.ultima_tecla=''
        self.movimento_inicial=False

        self.menu_loop()
    def create_mapa(self):
        y=-30.3
        x=0
        map=self.mapaa.getmap()

        for i in range(0,24):
            y+=30.3
            x=0

            for j in range(0,32):
                if map[i][j] == "X":
                    self.display.blit(pygame.transform.scale(pygame.image.load("D:\Python\Thonny\Scripts\Geistman\sprites\obloco.jpg"), (1024/32+10, 768/24+10)),(x,y))
                    bloco = Bloco(x,y)
                    self.blocos.add(bloco) #testar
                    
                    self.display.blit(bloco.sprite,(x,y))


                    
                x+=(1024/32)

    def menu_loop(self):
        menuLoop = True
        while menuLoop:
            self.display.fill((0,0,0))
            
            directory_images = os.path.join(os.getcwd(), 'sprites')

            self.spritesheet0=os.path.join(directory_images, "spritesheet.png")
            self.spritesheet1=os.path.join(directory_images, "spritesheetgeist.png")
            self.geistmanLogo=os.path.join(directory_images, "logo.png")
            self.geistmanLogo=pygame.image.load(self.geistmanLogo)
            self.displayIcon=os.path.join(directory_images, "displayIcon.png")
            self.displayIcon=pygame.image.load(self.displayIcon)
            pygame.display.set_icon(self.displayIcon)

            font0 = pygame.font.Font(self.FONT0, 40)
            texto=font0.render("press any key to start",False,self.white)
            textRect = texto.get_rect()
            textRect.midtop = (512, 568)
            self.display.blit(texto, textRect)
            logoRect = self.geistmanLogo.get_rect()
            logoRect.midtop=(512,150)
            self.display.blit(self.geistmanLogo, logoRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menuLoop = False
                if event.type == pygame.KEYDOWN:

                    menuLoop = False
                    self.game_loop()

            pygame.display.update()
    def testar_colisao(self):
        for x in self.inimigos:
            if pygame.Rect.colliderect(self.fantasma.rect,x.rect) == True and x.vulneravel==True:
                x.kill()
                self.inimigos.remove(x)
            elif pygame.Rect.colliderect(self.fantasma.rect,x.rect) == True and x.vulneravel==False:
                
                pygame.quit()


        for y in self.particulas:
            if pygame.Rect.colliderect(self.fantasma.rect,y.rect) == True:
                self.particulas.remove(y)
                aleatorio=random.randrange(0,3)
                self.inimigos[aleatorio].esta_vulneravel()#==True
                #for i in self.inimigos:
                 #   print (i.vulneravel)



        if pygame.sprite.spritecollideany(self.fantasma, self.blocos):
            if self.ultima_tecla=='a':
                self.fantasma.movDireita()
            if self.ultima_tecla=='d':
                self.fantasma.movEsquerda()
            elif self.ultima_tecla=='w':
                self.fantasma.movBaixo()
            elif self.ultima_tecla=='s':
                self.fantasma.movCima()

    def game_loop(self):
        self.gameLoop = True 

        while self.gameLoop:
            #clock
            self.clock.tick(self.FPS)  
            self.display.fill((0, 0, 0))

            #cria mapa
            self.create_mapa()

            #cria sprites de pacmans e do player
            for par in self.particulas:
                par.desenhar()#funciona
            for pacmans in self.inimigos:
                self.display.blit(pacmans.sprite,(pacmans.posInicial[0],pacmans.posInicial[1]))#funciona
            self.display.blit(self.fantasma.sprite,(self.fantasma.posInicial[0],self.fantasma.posInicial[1]))#funciona
            #inicia movimento dos inimigos
            if self.inimigo_saiu ==False:#funciona
                for i in range(0,3):
                    self.inimigos[i].movCima()
                    if (i == 2 ):
                        self.inimigo_saiu=True
            #checa colisao  dos inimigos

            if self.inimigo_saiu:
                for i in self.inimigos:
                    i.colisao(self.blocos)
                    #i.prox_movimento()

            self.testar_colisao()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameLoop = False
                    pygame.quit()
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.fantasma.movDireita()
                    self.ultima_tecla='d'

                elif pygame.key.get_pressed()[pygame.K_a]:
                    self.fantasma.movEsquerda()
                    self.ultima_tecla='a'
                elif pygame.key.get_pressed()[pygame.K_w]:
                    self.fantasma.movCima()
                    self.ultima_tecla='w'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:

                        self.fantasma.movBaixo()
                        self.ultima_tecla='s'

            pygame.display.flip()


x=Control()

