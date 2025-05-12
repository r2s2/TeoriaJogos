def estrategiaOlhoPorOlhoA(historico_a, historico_b):
    '''Define a estratégia de cada jogador'''
        
    if len(historico_a) == 0: 
        return 'C'
    elif len(historico_b) > 0 and historico_b[-1] == 'C': 
        return 'C'
    else:
        return 'T'