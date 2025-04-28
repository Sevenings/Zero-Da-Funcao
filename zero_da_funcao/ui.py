from zero_da_funcao.metodos.abstrata import MetodoEncontrarRaiz
from zero_da_funcao.metodos import MetodoDaBissecao, MetodoDeNewton, MetodoDoPontoFixo, MetodoDaSecante
from zero_da_funcao.parsing import parsing_funcao


class UI:
    metodos_salvos = {
            "1": MetodoDaBissecao(),
            "2": MetodoDoPontoFixo(),
            "3": MetodoDeNewton(),
            "4": MetodoDaSecante(),
            }

    def run(self):
        self.mostrar_titulo()

        print("Insira a função:")
        expressao_entrada = input("> ")
        try: 
            funcao = parsing_funcao(expressao_entrada)
        except:
            print("Formatação da função inválida, tente novamente")
            exit()

        print("Insira a tolerância:")
        tolerancia = float(input("> "))

        print("Escolha os Métodos: ")
        print("  [1] Método de Bisseção")
        print("  [2] Método do Ponto Fixo")
        print("  [3] Método do Newton")
        print("  [4] Método da Secante")
        print("ex: 1, 3, 4")
        metodos_entrada = input("> ")
        metodos = self.interpretar_metodos_entrada(metodos_entrada)

        return {
                'funcao': funcao,
                'tolerancia': tolerancia,
                'metodos': metodos
                }


    def mostrar_titulo(self):
        print("Zero da Função")
        print("--------------")
        print()
        print("Onde está o zero da função?")
        print()


    def interpretar_metodos_entrada(self, metodos_entrada: str) -> list[MetodoEncontrarRaiz]:
        metodos_string = metodos_entrada.split(',')
        for i, m in enumerate(metodos_string.copy()):
            metodos_string[i] = m.strip()

        metodos = [ self.metodos_salvos[m] for m in metodos_string ]
        return metodos

    
    def mostrar_resultados(self, resultados):
        for r in resultados:
            metodo = r.get('metodo')
            raiz = r.get('raiz')
            iteracoes = r.get('iteracoes')
            etapas = r.get('etapas')

            print('-'*len(metodo))
            print(f"{metodo}:")
            print(f"Raíz: {raiz}")
            print(f"Iterações: {iteracoes}")
            print(f"Etapas: {etapas}")
