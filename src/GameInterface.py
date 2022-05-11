import abc
from pygame import Surface

class GameInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, deltaTime) -> None:
        pass

    @abc.abstractmethod
    def render(self, surface : Surface) -> None:
        pass
