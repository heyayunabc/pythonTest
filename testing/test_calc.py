import unittest
from pythonDemo.calc import Calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()
