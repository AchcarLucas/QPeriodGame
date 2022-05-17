import pygame

from src import ElementPackage
from src import GameInterface

class Container(GameInterface.GameInterface):

    def __init__(self, x, y, height, width, color):
        self.__surfaceContainer = None
        self.__x = x
        self.__y = y
        self.__height = height
        self.__width = width
        self.__color = (0, 0, 0)
        self.__createSurfaceContainer(height, width)
        self.changeSurfaceColor(color)

    def __createSurfaceContainer(self, height, width):
        self.__surfaceContainer = GameInterface.Surface((width, height))

    def getContainerHeight(self):
        return self.__height

    def getContainerWidth(self):
        return self.__width

    def getContainerX(self):
        return self.__x

    def getContainerY(self):
        return self.__y

    def changeSurfaceColor(self, color):
        self.__color = color
        if(self.__surfaceContainer != None):
            self.__surfaceContainer.fill(color)

    def getSurfaceContainer(self):
        return self.__surfaceContainer

    def cleanSurface(self, color):
        self.changeSurfaceColor(color)

    def cleanSurface(self):
        self.changeSurfaceColor(self.__color)

    def update(self, deltaTime):
        pass

    def render(self, screen : GameInterface.Surface):
        screen.blit(self.__surfaceContainer, (self.__x, self.__y))


