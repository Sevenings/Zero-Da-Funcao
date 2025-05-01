from sympy import symbols, lambdify
from sympy.parsing.sympy_parser import parse_expr

from zero_da_funcao.exceptions import FormatacaoInvalidaException

def parsing_funcao(funcao_string):
    # 1) Defina a variável simbólica
    x = symbols('x')

    # 2) Faça o parsing da string para um objeto Sympy Expr
    try:
        funcao = parse_expr(funcao_string, evaluate=True)
    except:
        raise FormatacaoInvalidaException

    return funcao

def converter_para_funcao_python(funcao_sympy):
    x = symbols('x')
    return lambdify(x, funcao_sympy, modules=['numpy'])


