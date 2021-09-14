from classes.Divisao import Divisao 
from classes.Soma import Soma 
from classes.Subtracao import Subtracao

operacoes = {
    "subtracao": Subtracao(),
    "soma": Soma(),
    "divisao": Divisao()
}

class OperacaoFabrica():
    def criar(operador):
        return operacoes[operador]

