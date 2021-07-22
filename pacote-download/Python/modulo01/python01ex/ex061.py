"""
Refaça o Desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da PA usando While
"""
termo = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
loop = 0
repet = termo
while loop < 10:
    print(repet, end=' -> ')
    repet += raz
    loop += 1
print('ACABOU!')

