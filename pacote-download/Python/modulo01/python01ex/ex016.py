# Criar um programa que leia um numero real qualquer pelo teclado e mostre sua porção inteira

import math
num = float(input('Digite um numero Real: '))
inter = math.trunc(num)

print('A porção inteira do valor {:.2f} é {}'.format(num, inter))
