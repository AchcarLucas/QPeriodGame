import pygame

from src import ElementState
from src import GameConstants
from src import GameInterface

class Element(GameInterface.GameInterface):
    def __init__(self, name, symbol, atomic_number : int, group : int, period : int):
        self.unique_id = Element.generateID()
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.group = group
        self.period = period

        self.__state = ElementState.ElementState.ATTEMPT
        self.__attempt = GameConstants.GameConstants.MAX_ATTEMPT

        self.__x = 0
        self.__y = 0

        self.__createSurfaceElement()
        
    def getElementState(self) -> ElementState.ElementState:
        return self.__state

    def getElementAttempt(self):
        return self.__attempt

    def __createSurfaceElement(self):
        self.__surfaceElement = GameInterface.Surface((60, 75))
        pygame.draw.rect(self.__surfaceElement, (255, 0, 0), (0, 0, 60, 75))

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