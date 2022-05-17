from enum import Enum
class GameConstants(Enum):
    MAX_ATTEMPT = 5
    WIDTH_ELEMENT = 60
    HEIGHT_ELEMENT = 75

    def __int__(self):
        return self.value