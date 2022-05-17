import pygame

from src import Container
from src import ElementPackage
from src import GameInterface

class ContainerElement(GameInterface.GameInterface):
    def __init__(self, container : Container.Container):
        self.__container = container
        self.elementPackage = None

    def setElementPackage(self, elementPackage : ElementPackage.ElementPackage):
        self.elementPackage = elementPackage

    def update(self, deltaTime):
        pass

    def render(self, screen : GameInterface.Surface):
        surfaceContainer = self.__container.getSurfaceContainer()
        if(self.elementPackage != None):
            elements = self.elementPackage.getElements()
            for element in elements:
                element.render(surfaceContainer)


