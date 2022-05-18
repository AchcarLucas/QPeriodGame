import pygame
import numpy as np
import os

from src import Element
from src import ElementPackage
from src import Container
from src import ContainerElement
from src import GameConstants
from src import GameFont

class Game():
    '''
        Classe responsável por gerenciar o jogo
    '''
    def __init__(self, screenSize : (int, int), fps=60, title='Game', icon=None):
        '''
            Construtor da Classe Game, possui como parâmetro
                screenSize  ->  tupla contendo de dois valores inteiros (int, int) 
                                que corresponde a largura e altura, ex (800, 600)
                fps         ->  contendo da taxa de atualização da tela
                title       ->  contendo o titulo do jogo
                icon        ->  contendo uma surface (imagem) com o icone a ser exibido na tela
        '''
        # inicializa as variáveis da classe
        self.gameRunning = True
        self.screenSize = screenSize

        self.title = title
        self.icon = icon
        self.fps = fps

        # inicializa o game
        self.initGame()
        self.loadGame()

    def initGame(self):
        '''
            Função responsável por inicializar e configurar a tela do jogo,
            essa função não possui parâmetros
        '''
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption(self.title)

        GameFont.GameFont.initFont()

        if(self.icon != None):
            pygame.display.set_icon(self.icon)

        self.gameClock = pygame.time.Clock()

    def loadGame(self):
        elementPackage = ElementPackage.ElementPackage()
        
        # 1º Grupo
        elementPackage.insertElement(Element.Element("Hidrogênio",  "H",    1,  1, 1))
        elementPackage.insertElement(Element.Element("Lítio",       "Li",   3,  1, 2))
        elementPackage.insertElement(Element.Element("Sódio",       "Na",   11, 1, 3))
        elementPackage.insertElement(Element.Element("Potássio",    "K",    19,  1, 4))
        elementPackage.insertElement(Element.Element("Rubídio",     "Rb",   37,  1, 5))
        elementPackage.insertElement(Element.Element("Césio",       "Cs",   55,  1, 6))
        elementPackage.insertElement(Element.Element("Frâncio",     "Fr",   87,  1, 7))

        # 2º Grupo
        elementPackage.insertElement(Element.Element("Bérilio",     "Be",   4,  2, 2))
        elementPackage.insertElement(Element.Element("Magnésio",    "Mg",   12, 2, 3))
        elementPackage.insertElement(Element.Element("Cásio",       "Ca",   20, 2, 4))
        elementPackage.insertElement(Element.Element("Estrôncio",   "Sr",   38, 2, 5))
        elementPackage.insertElement(Element.Element("Bário",       "Ba",   56, 2, 6))
        elementPackage.insertElement(Element.Element("Rádio",       "Ra",   88, 2, 7))

        # 3º Grupo
        elementPackage.insertElement(Element.Element("Escândio",    "Sc",   21, 3, 4))
        elementPackage.insertElement(Element.Element("Ítrio",       "Y",    39, 3, 5))

        # 3º Grupo Lantanídeos
        elementPackage.insertElement(Element.Element("Lantânio",    "La",   57, 3, 6))
        elementPackage.insertElement(Element.Element("Cério",       "Ce",   58, 3, 6))
        elementPackage.insertElement(Element.Element("Praseodímio", "Pr",   59, 3, 6))
        elementPackage.insertElement(Element.Element("Neodímio",    "Nd",   60, 3, 6))
        elementPackage.insertElement(Element.Element("Promécio",    "Pm",   61, 3, 6))
        elementPackage.insertElement(Element.Element("Samário",     "Sm",   62, 3, 6))
        elementPackage.insertElement(Element.Element("Európio",     "Eu",   63, 3, 6))
        elementPackage.insertElement(Element.Element("Gadolídio",   "Gd",   64, 3, 6))
        elementPackage.insertElement(Element.Element("Térbio",      "Tb",   65, 3, 6))
        elementPackage.insertElement(Element.Element("Disprósio",   "Dy",   66, 3, 6))
        elementPackage.insertElement(Element.Element("Hólmio",      "Ho",   67, 3, 6))
        elementPackage.insertElement(Element.Element("Érbio",       "Er",   68, 3, 6))
        elementPackage.insertElement(Element.Element("Túlio",       "Tm",   69, 3, 6))
        elementPackage.insertElement(Element.Element("Itérbio",     "Yb",   70, 3, 6))
        elementPackage.insertElement(Element.Element("Lutécio",     "Lu",   71, 3, 6))

        # 3º Grupo Actinídeos
        elementPackage.insertElement(Element.Element("Actínio",     "Ac",   89, 3, 7))
        elementPackage.insertElement(Element.Element("Tório",       "Th",   90, 3, 7))
        elementPackage.insertElement(Element.Element("Protáctinio", "Pa",   91, 3, 7))
        elementPackage.insertElement(Element.Element("Urânio",      "U",    92, 3, 7))
        elementPackage.insertElement(Element.Element("Netúnio",     "Np",   93, 3, 7))
        elementPackage.insertElement(Element.Element("Plutônio",    "Pu",   94, 3, 7))
        elementPackage.insertElement(Element.Element("Amerício",    "Am",   95, 3, 7))
        elementPackage.insertElement(Element.Element("Cúrio",       "Cm",   96, 3, 7))
        elementPackage.insertElement(Element.Element("Berquélio",   "Bk",   97, 3, 7))
        elementPackage.insertElement(Element.Element("Califórnio",  "Cf",   98, 3, 7))
        elementPackage.insertElement(Element.Element("Einsténio",   "Es",   99, 3, 7))
        elementPackage.insertElement(Element.Element("Férmio",      "Fm",   100, 3, 7))
        elementPackage.insertElement(Element.Element("Mendelévio",  "Md",   101, 3, 7))
        elementPackage.insertElement(Element.Element("Nobélio",     "No",   102, 3, 7))
        elementPackage.insertElement(Element.Element("Laurêncio",   "Lr",   103, 3, 7))

        HEIGHT_ELEMENT = int(GameConstants.GameConstants.HEIGHT_ELEMENT)
        WIDTH_ELEMENT = int(GameConstants.GameConstants.WIDTH_ELEMENT)

        self.container = Container.Container(40, self.screenSize[1] - (20 + HEIGHT_ELEMENT) - 10, (20 + WIDTH_ELEMENT), self.screenSize[0] - 40 * 2, (127, 127, 127))
        self.containerElement = ContainerElement.ContainerElement(self.container)
        self.containerElement.setElementPackage(elementPackage)

    # função principal do jogo
    def gameMain(self):
        '''
            Loop principal do jogo, essa função não possui parâmetros
        '''
        while self.gameRunning:
            deltaTime = self.gameClock.tick(self.fps)
            self.screen.fill((50, 50, 50))

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate(deltaTime)
            self.gameRender()

            pygame.display.update()

        pygame.quit()
        
    # função de eventos
    def gameEvent(self, event):
        '''
            Função responsável por gerenciar os eventos do display
            event -> contém a estrutura do evento (veja a documentação do pygame para mais detalhes)
        '''
        if(event.type == pygame.QUIT):
            self.gameRunning = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                self.gameRunning = False

    # função de atualização
    def gameUpdate(self, deltaTime):
        '''
            Função responsável por atualizar a lógica do jogo
            deltaTime -> váriaveis que guarda o tempo que se passou entre dois frames
        '''
        self.containerElement.update(deltaTime)
        self.container.update(deltaTime)

    # função de renderização
    def gameRender(self):
        '''
            Função responsável por desenhar na tela do jogo
        '''
        self.containerElement.render(self.screen)
        self.container.render(self.screen)

game = Game((800, 600), title='Game')
game.gameMain()