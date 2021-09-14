from classes.OperacaoFabrica import OperacaoFabrica

class Calculadora:
    def calcular(self, valor1, valor2, operador):
        operacao = OperacaoFabrica.criar(operador)

        return operacao.executar(valor1, valor2)
