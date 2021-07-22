"""
Faça um programa que leia um número qualquer e mostre o seu fatorial
"""
# Para trabalhar com Fatorial, existe uma biblioteca que já faz isso:
# from math import factorial
# Esse factorial já faz tudo que fizemos abaixo

num = int(input('Digite um Número: '))
fat = num
tot = fat
print('{}!'.format(num), end='= ')
while fat > 0:
    if fat > 1:
        print('{}'.format(fat), end=' x ')
        tot = tot * (fat - 1)
    else:
        print('{}'.format(fat), end=' = ')
    fat = fat - 1
print('{}'.format(tot))