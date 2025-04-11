import unittest
from division import Division


class TestDivision(unittest.TestCase):
    def test_division_dosNumeros_retornaDivision(self):
        # Arrange
        operando1 = 10
        operando2 = 2
        resultadoEsperado = 5

        objDivision = Division(operando1, operando2)

        # Act
        resultadoActual = objDivision.calcular_division

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, msg="Fallo la división")

    def test_division_operandoNoNumerico_retornaMensajeError(self):
        # Arrange
        objDivision1 = Division(8, 2)
        objDivision2 = Division(10, 5)

        resultadoEsperado = "Error: Ambos operandos deben ser numéricos"

        # Act & Assert
        self.assertEqual(resultadoEsperado, objDivision1.calcular_division)
        self.assertEqual(resultadoEsperado, objDivision2.calcular_division)

    def test_division_entreCero_retornaMensajeError(self):
        # Arrange
        objDivision = Division(10, 2)
        resultadoEsperado = "Error: No se puede dividir entre cero"

        # Act
        resultadoActual = objDivision.calcular_division

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)


if __name__ == '__main__':
    unittest.main()