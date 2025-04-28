from zero_da_funcao import UI
from zero_da_funcao import processar


if __name__ == '__main__':
    ui = UI()
    argumentos = ui.run() # argumentos em dicionário
                          # argumentos = {
                          #   'funcao'
                          #   'tolerancia'
                          #   'metodos'
                          # }

    resultados = processar(**argumentos) # resultados: uma lista do processamento por cada método
                                         # resultados = [
                                         #   {
                                         #     'metodo'
                                         #     'raiz'
                                         #     'iteracoes'
                                         #     'etapas': []
                                         #   }
                                         # ]

    ui.mostrar_resultados(resultados)
    # for r in resultados:
    #     gerar_excel(**r)
    # TODO: Implementar gerar excel


