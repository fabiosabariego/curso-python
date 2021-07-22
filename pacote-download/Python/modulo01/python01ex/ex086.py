"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha os valores lidos pelo teclado
no final, mostre a matriz na tela, com a formatação correta
"""

num = 0
matriz = [[], [], []]
for c in range(0, 3):
    for l in range(0, 3):
        num = int(input(f'Digite um valor para [{c}, {l}]: '))
        matriz[c].append(num)
print('=' * 30)
for i in range(0, 3):
    for n in matriz[i]:
        print(f'[{n:^5}]', end=' ')
    print()