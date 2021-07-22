# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao
# 1 para Binario, 2 para ocal e 3 para Hexa

num = int(input('Digite um numero inteiro: '))
print('''Escolha a base de Conversao:')
[1] - Base Binaria
[2] - Base Octal
[3] - Base Hexa''')
base = int(input('Base: '))

if base == 1:
    print('O numero {} em binario e: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('O numero {} em octa e: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O numero {} em hexa e: {}'.format(num, hex(num)[2:].upper()))
else:
    print('Valor invalido, tente novamente!!!')
