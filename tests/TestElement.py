import unittest
from src import Element

class TestElement(unittest.TestCase):
    def test_CreateElement(self):
        element = Element.Element("Hidrogênio", "H", 1, 1, 1)

    def test_ElementAttribute(self):
        element = Element.Element("Lítio", "Li", 3, 1, 2)
        self.assertEqual(element.unique_id, 2)
        self.assertEqual(element.name, "Lítio")
        self.assertEqual(element.symbol, "Li")
        self.assertEqual(element.atomic_number, 3)
        self.assertEqual(element.group, 1)
        self.assertEqual(element.period, 2)

if __name__ == '__main__':
    unittest.main()
