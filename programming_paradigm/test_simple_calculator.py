import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6) #for positive integers
        self.assertEqual(self.calc.add(-2,-2), -4) #for negative integers
        self.assertEqual(self.calc.add(-2, 3), 1) #for negative & positve integers
        
    def test_substract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2) #for positive integers
        self.assertEqual(self.calc.subtract(-2,-2), 0) #for negative integers
        self.assertEqual(self.calc.subtract(-3, 2), -5) #for negative & positve

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8) #for positive integers
        self.assertEqual(self.calc.multiply(-2,-2), 4) #for negative integers
        self.assertEqual(self.calc.multiply(-3, 2), -6) #for negative & positve

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2) #for positive integers
        self.assertEqual(self.calc.divide(-2,-2), 1) #for negative integers
        self.assertEqual(self.calc.divide(-6, 2), -3) #for negative & positve
        self.assertEqual(self.calc.divide(0, 2), 0) #for dividing 0 by a number
        self.assertEqual(self.calc.divide(5, 0), None) #for dividing a number by zero
