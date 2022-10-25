import pygame
import constant
import sprites
import os

class Game:
    def __init__(self):
        #interface do game
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((constant.WIDTH, constant.HEIGHT))
        pygame.display.set_caption(constant.GAMETITLE)
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.font0 = pygame.font.match_font(constant.FONT0)
        self.load_files()

    def startGame(self):
        self.allSprites = pygame.sprite.Group()
        self.run()

    def run(self):
        #loop do jogo
        self.playing = True
        while self.playing:
            self.clock.tick(constant.FPS)
            self.events()
            self.updateSprites()
            self.drawSprites()

    def events(self):
        #eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            self.isRunning = False

    def updateSprites(self):
        #atualizar sprites
        self.allSprites.update()

    def drawSprites(self):
        #desenhar sprites
        self.screen.fill(constant.BLACK)
        self.allSprites.draw(self.screen)
        pygame.display.flip()

    def load_files(self):
        #fazer upload de audio e img
        directory_images = os.path.join(os.getcwd(), 'Sprites')
        self.diretorio_audios = os.path.join(os.getcwd(), 'Audios')
        self.spritesheet0 = os.path.join(directory_images, constant.SPRITESHEET)
        self.spritesheet1 = os.path.join(directory_images, constant.SPRITESHEETGEIST)
        self.geistmanLogo = os.path.join(directory_images, constant.GEISTMANLOGO)
        self.geistmanLogo = pygame.image.load(self.geistmanLogo)
        self.displayIcon = os.path.join(directory_images, constant.DISPLAYICON)
        self.displayIcon = pygame.image.load(self.displayIcon)
        pygame.display.set_icon(self.displayIcon)

    def showText(self, text, size, color, x, y):
        #mostra um texto na tela inicial
        font0 = pygame.font.Font(self.font0, size)
        text = font0.render(text, False, color)
        textRect = text.get_rect()
        textRect.midtop = (x, y)
        self.screen.blit(text, textRect)

    def showLogo(self, x, y):
        #mostra a logo (imagem)
        logoRect = self.geistmanLogo.get_rect()
        logoRect.midtop = (x, y)
        self.screen.blit(self.geistmanLogo, logoRect)

    def showStartScreen(self):
        self.showLogo(constant.WIDTH/2, 20)
        self.showText("- Press any key to start", 32, constant.WHITE, constant.WIDTH/2, 420)
        pygame.display.flip()
        self.waitForPlayer()

    def waitForPlayer(self):
        waiting = True
        while waiting:
            self.clock.tick(constant.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.isRunning = False
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def showGameOverScreen(self):
        pass

g = Game()
g.showStartScreen()

while g.isRunning:
    g.startGame()
    g.showGameOverScreen()