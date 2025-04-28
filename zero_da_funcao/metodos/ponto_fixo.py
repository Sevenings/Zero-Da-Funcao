from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz

class MetodoDoPontoFixo(MetodoEncontrarRaiz):
    
    def condicoes(self, funcao) -> bool:
        return True

    def _calcular_raiz(self, funcao, tolerancia) -> float:
        return 2


