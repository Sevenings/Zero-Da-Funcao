from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz

class MetodoDaBissecao(MetodoEncontrarRaiz):
    nome = 'Método da Bissecao'
    
    # TODO: Implementar
    def condicoes(self, funcao) -> bool:
        return True

    # TODO: Implementar
    def _calcular_raiz(self, funcao, tolerancia) -> float:
        return 2


