import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,5),4)
        self.assertEqual(calc.add(-2,3),1)
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1,5),-6)
        self.assertEqual(calc.subtract(-2,3),-5)
    def test_multiply(self):
        self.assertEqual(calc.multiply(2,5),10)
        self.assertEqual(calc.multiply(1,5),5)
        self.assertEqual(calc.multiply(-0,0),0)
    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(1,2), 0.5)
        self.assertEqual(calc.divide(3,3),1)

        with self.assertRaises(ValueError):
            calc.divide(10,0)  
        


if __name__ == '__main__':
    unittest.main() 