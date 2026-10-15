# test_calculadora.py
import unittest
from calculadora import suma, resta, multiplicacion, division


class TestCalculadora(unittest.TestCase):

    
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(10, 4), 6)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(6, 7), 42)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

 
    def test_division_entre_cero(self):
        with self.assertRaises(ValueError):
            division(5, 0)

    
    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -3), -5)

    def test_division_decimal(self):
        self.assertEqual(division(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()
