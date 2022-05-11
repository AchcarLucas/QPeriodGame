import pygame

from src import ElementPackage
from src import GameInterface

class Container(GameInterface.GameInterface):

    def __init__(self, x, y, height, width, color):
        self.__surfaceContainer = None
        self.__x = x
        self.__y = y
        self.__createSurfaceContainer(height, width)
        self.changeSurfaceColor(color)

    def __createSurfaceContainer(self, height, width):
        self.__surfaceContainer = GameInterface.Surface((width, height))

    def changeSurfaceColor(self, color):
        if(self.__surfaceContainer != None):
            self.__surfaceContainer.fill(color)

    def getSurfaceContainer(self):
        return self.__surfaceContainer

    def update(self, deltaTime):
        pass

    def render(self, screen : GameInterface.Surface):
        screen.blit(self.__surfaceContainer, (self.__x, self.__y))


