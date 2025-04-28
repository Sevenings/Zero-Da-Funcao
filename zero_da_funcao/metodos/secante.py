from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz

class MetodoDaSecante(MetodoEncontrarRaiz):
    nome = 'Método da Secante'

    # TODO: Implementar
    def condicoes(self, funcao) -> bool:
        return True

    # TODO: Implementar
    def _calcular_raiz(self, funcao, tolerancia) -> float:
        return 2


