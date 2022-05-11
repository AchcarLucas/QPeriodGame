import abc

class GameInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self) -> None:
        pass

    @abc.abstractmethod
    def render(self) -> None:
        pass
