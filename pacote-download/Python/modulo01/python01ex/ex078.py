"""
Faça um programa que leia 5 valores numéricos e guarde em uma lista. No final, mostre qual foi o maior e o menor
valor digitadoe as respectivas posições na lista
"""

inicio = 0
lista = []
maior = menor = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite o Valor na posição {cont}: ')))
    if inicio == 0:
        maior = menor = lista[cont]
        inicio = 1
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print('=' * 30)
print(f'Você Digitou os Valores: {lista}')
print(f'O maior valor encontrado foi {max(lista)} nas posições: ', end='')
for p, v in enumerate(lista):
    if v >= maior:
        maior = v
        print(f'{p}', end='... ')
print(f'\nO menor valor encontrado foi {min(lista)} nas posições: ', end='')
for p, v in enumerate(lista):
    if v <= menor:
        menor = v
        print(f'{p}', end='... ')
