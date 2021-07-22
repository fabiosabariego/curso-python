"""
Faça um Programa que tenha uma função chamada maior, que receba vários valores com valores inteiros. Seu programa tem que analisar todos os valores e
mostrar qual deles é o maior
"""
from time import sleep

def maior(*num):
    m = 0
    print('-=' * 20)
    print('Analisando os valores Passados...')
    for n in num:
        print(n, end=" ")
        sleep(0.4)
        if n > m:
            m = n
    print(f'foram informados {len(num)} numeros ao todo')
    print(f'O maior valor informado foi {m}')

maior(3, 5, 7, 5, 4, 2)
maior(2, 1, 9, 32, 77)
maior(2, 1)
maior()