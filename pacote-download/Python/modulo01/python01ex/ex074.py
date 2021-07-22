"""
Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla
Depois, mostre a listagem de números gerados e também indique o menor e o maior valor
"""
from random import randint
tup = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)))
print('Os valores sorteados foram: ', end='')
for c in tup:
    print(f'{c} ', end='')
print('')
print(f'O maior número sorteado foi: {max(tup)}')
print(f'O menor número sorteado foi: {min(tup)}')
