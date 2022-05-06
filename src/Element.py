class Element(object):
    def __init__(self, name, symbol, atomic_number : int, group : int, period : int):
        self.unique_id = Element.generateID()
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.group = group
        self.period = period

    @staticmethod
    def generateID():
        Element.ID_UNIQUE = Element.ID_UNIQUE + 1
        return Element.ID_UNIQUE
    
# Static ID Generate
Element.ID_UNIQUE = 0