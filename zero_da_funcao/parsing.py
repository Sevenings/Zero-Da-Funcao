from sympy import symbols, lambdify
from sympy.parsing.sympy_parser import parse_expr

def function_parsing(funcao_string):
    # 1) Defina a variável simbólica
    x = symbols('x')

    # 2) Faça o parsing da string para um objeto Sympy Expr
    expr = parse_expr(funcao_string, evaluate=True)

    # 3) Opcional: veja o resultado
    print(expr)   # → sin(x) + x**2

    # 4) Transforme em função numérica (usando, por exemplo, numpy por baixo)
    f = lambdify(x, expr, modules=['numpy'])

    return f

