from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz
import sympy as sp

class MetodoDeNewton(MetodoEncontrarRaiz):
    def __init__(self) -> None:
        super().__init__()
        self.nome = 'Método de Newton'
        self.parametros_extra = [
                {'nome': 'chute', 'prompt': 'Insira um chute inicial: '},
            ]

    def calcular(self, funcao, tolerancia, **kwargs) -> float:
        if not self.condicoes(funcao):
            raise Exception("Condição inválida")

        return self._calcular_raiz(funcao, tolerancia, **kwargs)
    
    # TODO: Implementar
    def condicoes(self, funcao_sympy) -> bool:
        return True

    def _calcular_raiz(self, funcao, tolerancia, **kwargs) -> float:
        x = sp.symbols('x')
        
        # Cria as funções numéricas f e f'
        f_num = sp.lambdify(x, funcao, modules=['numpy'])
        df_expr = sp.diff(funcao, x)
        df_num = sp.lambdify(x, df_expr, modules=['numpy'])
        
        x_n = kwargs.get('chute')

        for n in range(1, self.maximo_iteracoes+1):
            f_xn = f_num(x_n)
            df_xn = df_num(x_n)

            if df_xn == 0:
                raise ZeroDivisionError(f"Derivada zero em iteração {n}, x = {x_n}")

            # iteração de Newton:
            x_next = x_n - f_xn/df_xn
            erro = abs(x_next - x_n)

            # armazena dados da iteração
            self.armazenar_historico(x_n, f_xn)

            # critério de parada
            if erro < tolerancia:
                return x_next

            x_n = x_next

        # se chegou aqui, não convergiu
        raise ValueError(f"Não convergiu em {self.maximo_iteracoes} iterações.")
