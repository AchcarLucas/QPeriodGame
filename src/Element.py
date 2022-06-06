import pygame
import math

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

        self.__inc_delta_time = 0.0
        self.__scale_text_symbol = 1.0


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

    def setElementX(self, x):
        self.__x = x
    
    def setElementY(self, y):
        self.__x = y

    def setElementXY(self, x, y):
        self.__x = x
        self.__y = y

    def update(self, deltaTime):
        self.__inc_delta_time = self.__inc_delta_time + (deltaTime * 0.01)
        self.__scale_text_symbol = 0.6 + 0.7 * abs(math.sin(math.pi * self.__inc_delta_time * 0.1))

    def render(self, screen : GameInterface.Surface):

        color_rect = (127, 127, 127)
        color_text = (255, 255, 255)

        if(self.__state == ElementState.ElementState.ATTEMPT):
            color_rect = (0, 180, 0)
            color_text = (200, 200, 200)
        elif(self.__state == ElementState.ElementState.WON):
            color_rect = (0, 127, 0)
            color_text = (150, 150, 150)
            self.__scale_text_symbol = 1.0
        elif(self.__state == ElementState.ElementState.LOSE):
            color_rect = (60, 60, 60)
            color_text = (127, 127, 127)
            self.__scale_text_symbol = 1.0

        HEIGHT_ELEMENT = int(GameConstants.GameConstants.HEIGHT_ELEMENT)
        WIDTH_ELEMENT = int(GameConstants.GameConstants.WIDTH_ELEMENT)

        pygame.draw.rect(self.__surfaceElement, color_rect, (0, 0, HEIGHT_ELEMENT, WIDTH_ELEMENT))

        text_symbol_surface = GameFont.GameFont.arial_30.render(self.symbol, True, color_text)
        text_attempt_surface = GameFont.GameFont.arial_12.render(str(self.__attempt), True, (255, 255, 255))

        text_symbol_surface_scale = pygame.transform.scale(     text_symbol_surface, 
                                                                (
                                                                    int(text_symbol_surface.get_width() * self.__scale_text_symbol), 
                                                                    int(text_symbol_surface.get_height() * self.__scale_text_symbol)
                                                                )
                                                           )

        text_symbol_rect = text_symbol_surface_scale.get_rect(center=(HEIGHT_ELEMENT / 2, WIDTH_ELEMENT / 2))
        text_attempt_rect = text_attempt_surface.get_rect(center=(10, 10))

        self.__surfaceElement.blit(text_symbol_surface_scale, text_symbol_rect)
        self.__surfaceElement.blit(text_attempt_surface, text_attempt_rect)

        del text_symbol_surface
        del text_symbol_surface_scale

        screen.blit(self.__surfaceElement, (self.__x, self.__y))

    @staticmethod
    def generateID():
        Element.ID_UNIQUE = Element.ID_UNIQUE + 1
        return Element.ID_UNIQUE
    
# Static ID Generate
Element.ID_UNIQUE = 0