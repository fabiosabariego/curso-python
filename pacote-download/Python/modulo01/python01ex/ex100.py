"""
Faça um programa que tenha uma lista chamada Número e 2 funções chamadas sorteio e somaPar. A primeira função
Vai sortear 5 números e vai colocar dentro de uma lista, e a segunda função vai mostrar uma soma entre todos
os numeros pares sorteados na função anterior
"""

from random import randint
from time import sleep
numero = []

def sorteio(lista):
    print('Sorteando 5 valores na lista: ', end='')
    for c in range(0, 5):
        num = randint(0, 9)
        lista.append(num)
        print(num, end=' ')
        sleep(0.5)
    print('FIM!')


def somaPar(lista):
    res = 0
    for v in lista:
        if v % 2 == 0:
            res = res + v
    print(f'Somando os valores pares de {lista} temos {res}')


sorteio(numero)
somaPar(numero)
