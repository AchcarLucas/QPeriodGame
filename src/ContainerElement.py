from src import ElementPackage
from src import GameInterface

class Container(GameInterface.GameInterface):

    def __init__(self, elementPackage : ElementPackage.ElementPackage):
        self._elementPackage = elementPackage;

    def update(self, deltaTime):
        pass

    def render(self, screen : GameInterface.Surface):
        pass


