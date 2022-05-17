import pygame

from src import ElementState
from src import GameConstants
from src import GameInterface
from src import GameFont

class Element(GameInterface.GameInterface):
    def __init__(self, name, symbol, atomic_number : int, group : int, period : int):
        self.unique_id = Element.generateID()
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.group = group
        self.period = period

        self.__state = ElementState.ElementState.ATTEMPT
        self.__attempt = int(GameConstants.GameConstants.MAX_ATTEMPT)

        self.__x = 0
        self.__y = 0

        self.__createSurfaceElement()
        
    def getElementState(self) -> ElementState.ElementState:
        return self.__state

    def getElementAttempt(self):
        return self.__attempt

    def getRect(self):
        return self.__surfaceElement.get_rect()

    def __createSurfaceElement(self):
        HEIGHT_ELEMENT = int(GameConstants.GameConstants.HEIGHT_ELEMENT)
        WIDTH_ELEMENT = int(GameConstants.GameConstants.WIDTH_ELEMENT)

        self.__surfaceElement = GameInterface.Surface((HEIGHT_ELEMENT, WIDTH_ELEMENT))
        pygame.draw.rect(self.__surfaceElement, (255, 0, 0), (0, 0, HEIGHT_ELEMENT, WIDTH_ELEMENT))
        text_symbol_surface = GameFont.GameFont.arial_30.render(self.symbol, True, (255, 255, 255))
        self.__surfaceElement.blit(text_symbol_surface, ((HEIGHT_ELEMENT / 2) - text_symbol_surface.get_height() / 2, (WIDTH_ELEMENT / 2) - text_symbol_surface.get_width() / 2))

    def setElementX(self, x):
        self.__x = x
    
    def setElementY(self, y):
        self.__x = y

    def setElementXY(self, x, y):
        self.__x = x
        self.__y = y

    def update(self, deltaTime):
        pass

    def render(self, screen : GameInterface.Surface):
        screen.blit(self.__surfaceElement, (self.__x, self.__y))

    @staticmethod
    def generateID():
        Element.ID_UNIQUE = Element.ID_UNIQUE + 1
        return Element.ID_UNIQUE
    
# Static ID Generate
Element.ID_UNIQUE = 0