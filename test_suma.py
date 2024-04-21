import unittest
from suma import sumar
from suma import restar
from suma import multiplicar
from suma import dividir



class testSumar(unittest.TestCase):


    def test_sumar(self):
        self.assertEqual(sumar(3,2), 5)
        self.assertEqual(sumar(-1,1), 0)
        self.assertEqual(sumar(-1, -1), -2)


if __name__== '__main__':
    unittest.main()


class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()

import unittest

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()


import unittest

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-4, 2), -2)
        self.assertEqual(dividir(5, 0), "Error: No se puede dividir por cero")

if __name__ == '__main__':
    unittest.main()


