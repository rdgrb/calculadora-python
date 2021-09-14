from classes.Operacao import Operacao 

class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2