"""
Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos
"""

peso = 0
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da pessoa {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso <= menor:
            menor = peso
print('O peso Menor é {:.1f}: '.format(menor))
print('O peso Maior é {:.1f}: '.format(maior))
