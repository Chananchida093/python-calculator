import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(9, 9), 18)
    def test_add2(self):
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)


    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(1000000, 2000000), -1000000)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(300, 600), -300)
    

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(-15, 120), -1800)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(2, 100), 200)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(2000, 1000), 2)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(300, 5), 60)


    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(60, 8), 4)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(100, 25), 0)
if __name__ == '__main__':
    unittest.main()