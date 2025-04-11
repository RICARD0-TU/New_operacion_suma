import unittest
from operaciones_Aritmeticas import operaciones_Aritmeticas

class TestSuma(unittest.TestCase):
    def test_suma_dosnumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15

        resultadoEsperado = 25

        objSuma = operaciones_Aritmeticas(operando1, operando2)


        # Act
        resultadoActual = objSuma.calcularSuma()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, msg="Fallo la suma")


    def test_suma_operadorNoNunerico_lanzaExcepciones(self):
        objSuma = operaciones_Aritmeticas(operando1=3, operando2="a")
        with self.assertRaises(TypeError):
            objSuma.calcularSuma()


    def test_Division_dosnumeros_retornaDivision(self):
        # Arrange
        dividendo = 10
        divisor = 15

        resultadoEsperado = dividendo / divisor

        objSuma = operaciones_Aritmeticas(dividendo, divisor)


        # Act
        resultadoActual = objSuma.caluclar_Divisio()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, msg="Fallo la Division")

        def test_division_operadorNoNunerico_lanzaExcepciones(self):
            objSuma = operaciones_Aritmeticas(operando1=3, operando2="a")
            with self.assertRaises(TypeError):
                objSuma.calcularSuma()





if __name__ == '__main__':
    unittest.main()
