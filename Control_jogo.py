import pygame
from fantasma import Fantasma
from pacman import Pacman
from personagem import Personagem
from mapa import Mapa
import os
from bloco import Bloco
class Control():

    pygame.init()
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
        self.fantasma = Fantasma(50,50,7,[500,200])
        self.blocos = pygame.sprite.Group()
        self.inimigo1 = Pacman(20,20,10,[450,400])
        self.inimigo_saiu=False
        self.inimigo2 = Pacman(20,20,10,[500,400])
        self.inimigo3 = Pacman(20,20,10,[550,400])
        self.inimigos = [self.inimigo1,self.inimigo2,self.inimigo3]

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
            if pygame.Rect.colliderect(self.fantasma.rect,x.rect) == True:
                x.kill()
                self.inimigos.remove(x)
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
        gameLoop = True 

        while gameLoop:

            self.clock.tick(self.FPS)  
            self.display.fill((0, 0, 0))
            #cria mapa

            self.create_mapa()

            #cria sprites de pacmans e do player

            for pacmans in self.inimigos:
                self.display.blit(pacmans.sprite,(pacmans.posInicial[0],pacmans.posInicial[1]))
            self.display.blit(self.fantasma.sprite,(self.fantasma.posInicial[0],self.fantasma.posInicial[1]))
            #inicia movimento dos inimigos
            if self.inimigo_saiu ==False:
                for i in range(0,3):
                    self.inimigos[i].sair()
                    if (i == 2 and pygame.sprite.spritecollideany(self.inimigos[i], self.blocos)):
                        self.inimigo_saiu=True
                        for i in self.inimigos:
                            i.colisao(self.blocos)

            #checa colisao  dos inimigos
            '''for i in self.inimigos:
                if pygame.sprite.spritecollideany(i, self.blocos):
                    i.colisao(self.blocos)
'''

            self.testar_colisao()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameLoop = False
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.fantasma.movDireita()
                    self.ultima_tecla='d'

                elif pygame.key.get_pressed()[pygame.K_a]:
                    self.fantasma.movEsquerda()
                    self.ultima_tecla='a'
                elif pygame.key.get_pressed()[pygame.K_w]:
                    self.fantasma.movCima()
                    self.ultima_tecla='w'
                elif pygame.key.get_pressed()[pygame.K_s]:

                    self.fantasma.movBaixo()
                    self.ultima_tecla='s'

            pygame.display.update()


x=Control()

