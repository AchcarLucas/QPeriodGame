from src import Element

class ElementPackage():
    def __init__(self):
        self.__elements = []

    def __del__(self):
        self.removeAllElement()

    def getElements(self):
        return self.__elements

    def getElementBySymbol(self, symbol) -> Element.Element:
        for element in self.__elements:
            if(element.symbol == symbol):
                return element

        return None

    def insertElement(self, element : Element.Element):
        self.__elements.append(element)

    def deleteElement(self, element : Element.Element):
        if(element in self.__elements):
            self.__elements.remove(element)
            del element

    def removeAllElement(self):
        for element in self.__elements:
            self.deleteElement(element)



