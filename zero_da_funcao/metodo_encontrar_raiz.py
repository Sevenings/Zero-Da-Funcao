from abc import ABC, abstractmethod


class MetodoEncontrarRaiz(ABC):

    @abstractmethod
    def calcular(self, funcao, tolerancia) -> float:
        pass

    @abstractmethod
    def condicoes(self, funcao) -> bool:
        pass
    
    @abstractmethod
    def _calcular_raiz(self, funcao, tolerancia) -> float:
        pass


