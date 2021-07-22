"""
Crie um programa onde 4 jogadores joguem um dado e tenha um resultado aleatório. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado
"""

from random import randint
from operator import itemgetter # Biblioteca utilizada para organizar os items em um Dicionário
jogador = {}
for c in range(0, 4):
    dado = randint(1, 6)
    jogador[f'Jogador {c+1}'] = dado
print('Valores Sorteados:')
for k, v in jogador.items():
    print(f'    O {k} tirou {v}')

print('Ranking dos Jogadores:')
for k, v in sorted(jogador.items(), key=itemgetter(1), reverse = True):
    print(f'    O {k} tirou {v}')