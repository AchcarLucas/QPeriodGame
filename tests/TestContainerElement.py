import unittest
from src import ContainerElement
from src import ElementPackage

class TestContainer(unittest.TestCase):
    def test_CreateContainer(self):
        elementPackage = ElementPackage.ElementPackage()
        container = ContainerElement.Container(elementPackage)
        del elementPackage

if __name__ == '__main__':
    unittest.main()