from abc import ABC, abstractmethod

from zero_da_funcao.parsing import converter_para_funcao_python

class MetodoEncontrarRaiz(ABC):

    def __init__(self) -> None:
        self.maximo_iteracoes = 1000
        self._historico_x = []
        self._historico_fx = []
        self.parametros_extra = []
        self.nome = "Método não nomeado"

    def calcular(self, funcao, tolerancia, **kwargs) -> float:
        if not self.condicoes(funcao):
            raise Exception("Condição inválida")

        funcao_python = converter_para_funcao_python(funcao)
        return self._calcular_raiz(funcao_python, tolerancia, **kwargs)

    def historico(self):
        return self._historico_x, self._historico_fx

    def armazenar_historico(self, x, fx):
        self._historico_x.append(x)
        self._historico_fx.append(fx)

    def condicoes(self, funcao) -> bool:
        return True
    
    @abstractmethod
    def _calcular_raiz(self, funcao, tolerancia, **kwargs) -> float:
        pass


