"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
"""

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 40)
print('JOGOS DA MEGA SENA'.center(40))
print('-' * 40)
jogo = int (input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 6, end='')
print(f' SORTEANDO {jogo} JOGOS ', end='')
print('=-' * 6)
for c in range(0, jogo):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    print(f'Jogo {c}: {jogos[c]}')
    sleep(1)
print('-=' * 7, end='')
print(f' < BOA SORTE!! > ', end='')
print('=-' * 7)
