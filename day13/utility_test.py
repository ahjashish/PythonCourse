import unittest
from day12.modules.util import utility


class UtilityTest(unittest.TestCase):
    def test_mult(self):
        num1 = 2
        num2 = 3
        expected = 6
        result = utility.mult(num1, num2)
        self.assertEqual(expected, result)

    def test_add(self):
        result = utility.add(5, 8)
        self.assertEqual(13, result)

    def test_divide(self):
        result = utility.add(8, 2, op='divide')
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()
