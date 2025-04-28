import unittest

from zero_da_funcao.metodos.bissecao import MetodoDaBissecao
from zero_da_funcao.metodos.newton import MetodoDeNewton
from zero_da_funcao.processar import processar

class TestProcessar(unittest.TestCase):
    funcao = lambda x: 2*x + 4
    tolerancia = 0.1
    raiz_esperada = 2
    metodos = [ MetodoDeNewton(), MetodoDaBissecao() ]

    def test_processar(self):

        resultados = processar(self.funcao, self.tolerancia, self.metodos)

        print(resultados)

        resultados_esperados = [
                {
                    'metodo': 'Método de Newton',
                    'raiz': 2,
                    'iteracoes': None,
                    'etapas': None
                },
                {
                    'metodo': 'Método da Bissecao',
                    'raiz': 2,
                    'iteracoes': None,
                    'etapas': None
                },
            ]

        self.assertEqual(resultados, resultados_esperados)




# Rodando os testes
if __name__ == '__main__':
    unittest.main()


