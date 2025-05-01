import unittest

from zero_da_funcao.metodos.bissecao import MetodoDaBissecao
from zero_da_funcao.metodos.ponto_fixo import MetodoDoPontoFixo
from zero_da_funcao.metodos.newton import MetodoDeNewton
from zero_da_funcao.metodos.secante import MetodoDaSecante
from zero_da_funcao.parsing import parsing_funcao


class TestMetodosEncontrarRaiz(unittest.TestCase):
    funcao_string = '-2*x + 4'
    tolerancia = 0.1
    raiz_esperada = 2

    def test_metodo_da_bissecao(self):
        funcao_sympy = parsing_funcao(self.funcao_string)
        metodo = MetodoDaBissecao()
        raiz = metodo.calcular(funcao_sympy, self.tolerancia)
        erro = abs(raiz - self.raiz_esperada)
        self.assertLess(erro, self.tolerancia)

    def test_metodo_do_ponto_fixo(self):
        funcao_sympy = parsing_funcao(self.funcao_string)
        metodo = MetodoDoPontoFixo()
        raiz = metodo.calcular(funcao_sympy, self.tolerancia)
        erro = abs(raiz - self.raiz_esperada)
        self.assertLess(erro, self.tolerancia)

    def test_metodo_de_newton(self):
        funcao_sympy = parsing_funcao(self.funcao_string)
        metodo = MetodoDeNewton()
        raiz = metodo.calcular(funcao_sympy, self.tolerancia)
        erro = abs(raiz - self.raiz_esperada)
        self.assertLess(erro, self.tolerancia)

    def test_metodo_da_secante(self):
        funcao_sympy = parsing_funcao(self.funcao_string)
        metodo = MetodoDaSecante()
        raiz = metodo.calcular(funcao_sympy, self.tolerancia)
        erro = abs(raiz - self.raiz_esperada)
        self.assertLess(erro, self.tolerancia)



# Rodando os testes
if __name__ == '__main__':
    unittest.main()


