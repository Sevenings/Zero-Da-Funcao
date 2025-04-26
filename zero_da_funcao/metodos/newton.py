from zero_da_funcao.metodo_encontrar_raiz import MetodoEncontrarRaiz

class MetodoDeNewton(MetodoEncontrarRaiz):
    
    def calcular(self, funcao, tolerancia) -> float:
        if not self.condicoes(funcao):
            raise Exception

        return self._calcular_raiz(funcao, tolerancia)

    def condicoes(self, funcao) -> bool:
        return True

    def _calcular_raiz(self, funcao, tolerancia) -> float:
        return 2



