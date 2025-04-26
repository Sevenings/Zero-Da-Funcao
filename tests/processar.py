import unittest


from zero_da_funcao.metodos import MetodoDaBissecao, MetodoDoPontoFixo, MetodoDeNewton, MetodoDaSecante

class TestProcessar(unittest.TestCase):

    def test_processar(self):
        funcao = lambda x: 2*x + 4
        tolerancia = 0.1
        lista_metodos = [ MetodoDaSecante, MetodoDoPontoFixo, MetodoDeNewton, MetodoDaSecante]
        # Implementar o run de processar



# Rodando os testes
if __name__ == '__main__':
    unittest.main()


