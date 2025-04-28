def processar(funcao, tolerancia, metodos):
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
        raiz = metodo.calcular(funcao, tolerancia)
        iteracoes, etapas = metodo.historico()

        resultados.append({'metodo': nome, 'raiz': raiz, 'iteracoes': iteracoes, 'etapas': etapas})

    return resultados


    
