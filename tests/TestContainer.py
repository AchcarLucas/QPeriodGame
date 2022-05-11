import unittest

from src import Container

class TestContainer(unittest.TestCase):
    def test_CreateContainer(self):
        container = Container.Container(10, 10, 200, 200, (255, 255, 255))

if __name__ == '__main__':
    unittest.main()