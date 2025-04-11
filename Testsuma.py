import unittest
from suma import Suma

class TestSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange

        operando1 = 10
        operando2 = 15

        resultadoEsperado = 25

        objSuma = Suma(operando1, operando2)

        # Act

        resultadoActual = objSuma.calcularsuma()

        # Assert

        self.assertEqual(resultadoEsperado, resultadoActual, msg = "fallo la suma")

    def test_suma_operadorNonumerico_lanzaExcepicon(self):
        objSuma = Suma(operando1 = "a", operando2 = 3)
        with self.assertRaises(ValueError):
            objSuma.calcularsuma()

if __name__ == '__main__':
    unittest.main()
