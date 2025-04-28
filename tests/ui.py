import unittest

from zero_da_funcao.metodos import MetodoDaBissecao
from zero_da_funcao.metodos import MetodoDoPontoFixo
from zero_da_funcao.ui import UI

class TestUI(unittest.TestCase):

    def test_ui(self):
        print('Selecionar:')
        print('Função: 2*x+4')
        print('Tolerancia: 0.1')
        print('Métodos: 1, 2')

        ui = UI()
        argumentos = ui.run()

        self.assertEqual(argumentos['funcao'], '2*x+4')
        self.assertEqual(argumentos['tolerancia'], 0.1)
        self.assertTrue(type(argumentos['metodos'][0]) == MetodoDaBissecao)
        self.assertTrue(type(argumentos['metodos'][1]) == MetodoDoPontoFixo)



# Rodando os testes
if __name__ == '__main__':
    unittest.main()


