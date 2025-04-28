from abc import ABC, abstractmethod


class MetodoEncontrarRaiz(ABC):

    def calcular(self, funcao, tolerancia) -> float:
        if not self.condicoes(funcao):
            raise Exception("Condição inválida")

        return self._calcular_raiz(funcao, tolerancia)

    def historico(self):
        return None, None

    @abstractmethod
    def condicoes(self, funcao) -> bool:
        pass
    
    @abstractmethod
    def _calcular_raiz(self, funcao, tolerancia) -> float:
        pass


