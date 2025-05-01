def processar(funcao, tolerancia, metodos, parametros_extra):
    """
    resultados: uma lista do processamento por cada método
    resultados = [
      {
        'metodo'
        'raiz'
        'iteracoes'
        'etapas': []
      }
    ]
    """
    resultados = []
    for metodo in metodos:
        nome = metodo.nome
        parametros_extra_metodo = parametros_extra[nome]
        raiz = metodo.calcular(funcao, tolerancia, **parametros_extra_metodo)
        historico_x, historico_y = metodo.historico()

        resultados.append({'metodo': nome, 'raiz': raiz, 'historico_x': historico_x, 'historico_y': historico_y})

    return resultados


    
