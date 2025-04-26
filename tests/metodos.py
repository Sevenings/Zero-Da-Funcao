import unittest

from zero_da_funcao.metodos.bissecao import MetodoDaBissecao
from zero_da_funcao.metodos.ponto_fixo import MetodoDoPontoFixo
from zero_da_funcao.metodos.newton import MetodoDeNewton
from zero_da_funcao.metodos.secante import MetodoDaSecante


class TestMetodosEncontrarRaiz(unittest.TestCase):
    funcao = lambda x: 2*x + 4
    tolerancia = 0.1
    raiz_esperada = 2

    def test_metodo_da_bissecao(self):
        metodo = MetodoDaBissecao()
        raiz = metodo.calcular(self.funcao, self.tolerancia)
        erro = abs(raiz - self.raiz_esperada)
        self.assertLess(erro, self.tolerancia)

    def test_metodo_do_ponto_fixo(self):
        metodo = MetodoDoPontoFixo()
        raiz = metodo.calcular(self.funcao, self.tolerancia)
        erro = abs(raiz - self.raiz_esperada)
        self.assertLess(erro, self.tolerancia)

    def test_metodo_de_newton(self):
        metodo = MetodoDeNewton()
        raiz = metodo.calcular(self.funcao, self.tolerancia)
        erro = abs(raiz - self.raiz_esperada)
        self.assertLess(erro, self.tolerancia)

    def test_metodo_da_secante(self):
        metodo = MetodoDaSecante()
        raiz = metodo.calcular(self.funcao, self.tolerancia)
        erro = abs(raiz - self.raiz_esperada)
        self.assertLess(erro, self.tolerancia)



# Rodando os testes
if __name__ == '__main__':
    unittest.main()


