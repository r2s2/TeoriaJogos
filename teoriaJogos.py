# definir função para 

import random
from olhoPorOlhoA import estrategiaOlhoPorOlhoA
# from olhoPorOlhoB import estrategiaOlhoPorOlhoB
from telaInicial import iteracoes

# Esconder a janela principal do tkinter


pontos_colaboram = 3 # quando ambos colaboram
pontos_traem = 1 #quando ambos traem
ponto_traido = 0 # 
ponto_traidor = 5
pontos_jogador_a = 0
pontos_jogador_b = 0

jogadas_jogador_a = []
jogadas_jogador_b = []


def recompensas(a,b):
    '''Retorna o valor que cada jogador receberá por rodada'''
    global pontos_jogador_a, pontos_jogador_b
    if (a == 'C' and b == 'C'):
        jogadas_jogador_a.append('C')
        jogadas_jogador_b.append('C')
        pontos_jogador_a += pontos_colaboram
        pontos_jogador_b += pontos_colaboram
    elif (a == 'C' and b == 'T'):
        jogadas_jogador_a.append('C')
        jogadas_jogador_b.append('T')
        pontos_jogador_a += ponto_traido
        pontos_jogador_b += ponto_traidor
    elif (a == 'T' and b == 'C'):
        jogadas_jogador_a.append('T')
        jogadas_jogador_b.append('C')
        pontos_jogador_a += ponto_traidor
        pontos_jogador_b += ponto_traido
    else:
        jogadas_jogador_a.append('T')
        jogadas_jogador_b.append('T')
        pontos_jogador_a += pontos_traem
        pontos_jogador_b += pontos_traem



# Jogador A - Olho por olho e B aleatório    
for i in range(iteracoes):
    # Jogador A
    jogada_a = estrategiaOlhoPorOlhoA(jogadas_jogador_a, jogadas_jogador_b)
    # Jogador B
    jogada_b = random.choice(['C', 'T'])    
    recompensas(jogada_a, jogada_b)
    # print(f'Rodada {i+1}: A = {jogada_a}, B = {jogada_b}. Pontos:  A: {pontos_jogador_a}, B: {pontos_jogador_b}')




print(f'A - olho por olho e B - aleatório: A={pontos_jogador_a}; B={pontos_jogador_b}. {iteracoes} rodadas.')
