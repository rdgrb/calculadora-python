import unittest 
from enum import Enum

from classes.Calculadora import Calculadora 

OPERADOR_SOMA = "soma"
OPERADOR_DIVISAO = "divisao"
OPERADOR_SUBSTRACAO = "subtracao"

class TestarCalculadora(unittest.TestCase):
    def setUp(self):
        self.calcular = Calculadora().calcular

    def test_soma(self):
        """🔨 teste de soma normal (1 + 1)"""
        resultado = self.calcular(1, 1, OPERADOR_SOMA)
        self.assertEqual(resultado, 2, "resultado deverá ser 2 (1 + 1)")

    def test_subtracao(self):
        """🔨 teste de subtração normal (7 - 2)"""
        resultado = self.calcular(7, 2, OPERADOR_SUBSTRACAO)
        self.assertEqual(resultado, 5, "resultado deverá ser 5 (7 - 2)")

    def test_subtracao_com_resultado_negativo(self):
        """🔨 teste de subtração com resultado negativo (2 - 7)"""
        resultado = self.calcular(2, 7, OPERADOR_SUBSTRACAO)
        self.assertEqual(resultado, -5, "resultado deverá ser -5 (2 - 7)")

    def test_divisao(self):
        """🔨 teste de divisão normal (10 / 2)"""
        resultado = self.calcular(10, 2, OPERADOR_DIVISAO)
        self.assertEqual(resultado, 5, "resultado deverá ser 5 (10 / 2)")
    
    @unittest.expectedFailure
    def test_divisao_por_0(self):
        """🔨 teste de divisão por 0"""
        self.calcular(1, 0, OPERADOR_DIVISAO)

    @unittest.expectedFailure
    def test_operador_invalido(self):
        """🔨 teste de operador inválido"""
        self.calcular(1, 1, "abc")


if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=3, exit=False)