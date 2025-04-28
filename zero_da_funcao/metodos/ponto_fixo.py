from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz

class MetodoDoPontoFixo(MetodoEncontrarRaiz):
    nome = 'Método do Ponto Fixo'
    
    # TODO: Implementar
    def condicoes(self, funcao) -> bool:
        return True

    # TODO: Implementar
    def _calcular_raiz(self, funcao, tolerancia) -> float:
        return 2


