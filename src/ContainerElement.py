import pygame

from src import Container
from src import ElementPackage
from src import GameInterface

class ContainerElement(GameInterface.GameInterface):
    def __init__(self, container : Container.Container):
        self.__container = container
        self.elementPackage = None
        self.__offset_x = 0
        self.__offset_y = 10

    def setElementPackage(self, elementPackage : ElementPackage.ElementPackage):
        self.elementPackage = elementPackage

    def update(self, deltaTime):
        if(self.elementPackage == None):
            return

        elements = self.elementPackage.getElements()
        
        inital_space_x = 5
        between_element_x = inital_space_x
        x = between_element_x
        y = 0

        for element in elements:
            element.update(deltaTime)
            element.setElementXY(x - self.__offset_x, y + self.__offset_y)
            x = x + element.getRect().width + between_element_x

        # limita os elementos no container  
        final_space_x = x - self.__container.getContainerWidth()

        if(self.__offset_x < 0):
            self.__offset_x = 0
        elif(self.__offset_x > final_space_x):
            self.__offset_x = final_space_x

    def render(self, screen : GameInterface.Surface):
        if(self.elementPackage == None):
            return

        self.__container.cleanSurface()
        surfaceContainer = self.__container.getSurfaceContainer()
        
        elements = self.elementPackage.getElements()
        for element in elements:
            element.render(surfaceContainer)


