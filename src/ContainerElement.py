import pygame

from src import ElementPackage
from src import GameInterface

class Container(GameInterface.GameInterface):

    def __init__(self, x, y, height, width, color):
        self.__container = None
        self.__x = x
        self.__y = y
        self.__createContainer(height, width)
        self.changeColor(color)

    def __createContainer(self, height, width):
        self.__container = GameInterface.Surface((width, height))

    def changeColor(self, color):
        if(self.__container != None):
            self.__container.fill(color)

    def getContainer(self):
        return self.__container

    def update(self, deltaTime):
        pass

    def render(self, screen : GameInterface.Surface):
        screen.blit(self.__container, (self.__x, self.__y))


