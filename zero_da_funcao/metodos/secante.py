from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz

class MetodoDaSecante(MetodoEncontrarRaiz):
    nome = 'Método da Secante'
    parametros_extra = [
            {'nome': 'x0', 'prompt': 'Insira valor de x0: '},
            {'nome': 'x1', 'prompt': 'Insira valor de x1: '},
            ]

    # TODO: Implementar
    def condicoes(self, funcao) -> bool:
        return True

    def _calcular_raiz(self, funcao, tolerancia, **kwargs) -> float:
        x0 = kwargs.get('x0') or 0.0
        x1 = kwargs.get('x1') or 1.0
        f_x0 = funcao(x0)
        f_x1 = funcao(x1)

        iteracao = 0

        while iteracao < self.maximo_iteracoes:
            if abs(f_x1 - f_x0) < 1e-14:
                raise Exception("Divisão por zero detectada no método da secante")

            # Fórmula do Método da Secante
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
            f_x2 = funcao(x2)

            self.armazenar_historico(x2, f_x2)

            if abs(f_x2) < tolerancia:
                return x2

            # Atualiza para próxima iteração
            x0, x1 = x1, x2
            f_x0, f_x1 = f_x1, f_x2
            iteracao += 1

        raise Exception(f"Máximo de iterações ({self.maximo_iteracoes}) atingido sem convergência.")


