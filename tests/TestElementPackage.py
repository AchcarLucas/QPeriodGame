import unittest
from src import ElementPackage

class TestElement(unittest.TestCase):
    def test_CreateElementPackage(self):
        elementPackage = ElementPackage.ElementPackage()
        del elementPackage

    def test_InsertElementPackage_B(self):
        elementPackage = ElementPackage.ElementPackage()
        element = ElementPackage.Element.Element("Lítio", "Li", 3, 1, 2)
        elementPackage.insertElement(element)
        del elementPackage

if __name__ == '__main__':
    unittest.main()

