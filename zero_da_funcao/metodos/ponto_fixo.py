from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz
import sympy as sp

class MetodoDoPontoFixo(MetodoEncontrarRaiz):
    def __init__(self) -> None:
        super().__init__()
        self.nome = 'Método do Ponto Fixo'
        self.parametros_extra = [
            {'nome': 'chute', 'prompt': 'Insira um chute inicial: '},
            {'nome': 'lambda_valor', 'prompt': 'Insira o valor de lambda (ex: 0.1): ', 'default': 0.1},
        ]

    def calcular(self, funcao, tolerancia, **kwargs) -> float:
        if not self.condicoes(funcao):
            raise Exception("Condição inválida")

        return self._calcular_raiz(funcao, tolerancia, **kwargs)

    def condicoes(self, funcao) -> bool:
        return True

    def _calcular_raiz(self, funcao, tolerancia, **kwargs) -> float:
        chute = float(kwargs.get('chute', 0))
        lambda_valor = float(kwargs.get('lambda_valor', 0.1))

        x = sp.Symbol('x')
        g_expr = x - lambda_valor * funcao  # g(x) = x - λ*f(x)
        g = sp.lambdify(x, g_expr, 'math')

        x_anterior = chute
        for _ in range(self.maximo_iteracoes):
            self.armazenar_historico(x_anterior, # TODO: )
            x_novo = g(x_anterior)
            if abs(x_novo - x_anterior) < tolerancia:
                return x_novo
            x_anterior = x_novo

        raise ValueError("O método não convergiu dentro do número máximo de iterações.")
