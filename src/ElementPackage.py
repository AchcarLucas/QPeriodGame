from src import Element

class ElementPackage(object):
    def __init__(self):
        self._elements = []

    def __del__(self):
        self.removeAllElement()

    def insertElement(self, element : Element.Element):
        self._elements.append(element)

    def deleteElement(self, element : Element.Element):
        if(element in self._elements):
            self._elements.remove(element)
            del element

    def removeAllElement(self):
        for element in self._elements:
            self.deleteElement(element)



