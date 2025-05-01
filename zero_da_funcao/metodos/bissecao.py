from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz

class MetodoDaBissecao(MetodoEncontrarRaiz):
    nome = 'Método da Bissecao'
    parametros_extra = [
            {'nome': 'limite_esquerdo', 'prompt': 'Insira o limite esquerdo: '},
            {'nome': 'limite_direito', 'prompt': 'Insira o limite direito: '},
        ]

    
    def _calcular_raiz(self, funcao, tolerancia, **kwargs) -> float:
        a = kwargs.get('limite_esquerdo') or -100
        b = kwargs.get('limite_direito') or 100

        if funcao(a) * funcao(b) > 0:
            raise Exception("Intervalo não contém raiz")

        i = 0
        while ( (b-a)/2 > tolerancia ):
            if funcao(a) == 0:
                return a
            if funcao(b) == 0:
                return b
            
            x = (a + b)/2

            fx = funcao(x)

            self.armazenar_historico(x, fx)

            if fx == 0:
                return x
            elif funcao(a)*fx < 0:
                b = x
            else:
                a = x
            i += 1
        return (a+b)/2

