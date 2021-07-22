''' Escreva um programa que leia 2 inteiros e compare-os, mostrando a msg na tela
- O primeiro Valor e o maior
- O segundo Valor e o menor
- Nao existe valor maior, ambos sao iguais
'''

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

if n1 > n2:
    print('O primeiro Valor e o Maior, {} > {}'.format(n1, n2))
elif n2 > n1:
    print('O Segundo Valor e o Maior, {} > {}'.format(n2, n1))
elif n1 == n2:
    print('Nao existe valor maior, porque eles sao iguais, {} = {}'.format(n1, n2))
