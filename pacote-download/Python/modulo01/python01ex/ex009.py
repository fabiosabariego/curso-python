# ------------------------- DESAFIO 009 -------------------------
# Programa para ler um numero inteiro, e mostrar a sua tabuada

num = int(input('Digite um numero: '))

x1 = num * 1
x2 = num * 2
x3 = num * 3
x4 = num * 4
x5 = num * 5
x6 = num * 6
x7 = num * 7
x8 = num * 8
x9 = num * 9
x10 = num * 10

print('A Tabela de tabuada do numero {} é:'.format(num))
print('-' * 20)
print('{} x {:2} = {}'.format(num, 1, x1))
print('{} x {:2} = {}'.format(num, 2, x2))
print('{} x {:2} = {}'.format(num, 3, x3))
print('{} x {:2} = {}'.format(num, 4, x4))
print('{} x {:2} = {}'.format(num, 5, x5))
print('{} x {:2} = {}'.format(num, 6, x6))
print('{} x {:2} = {}'.format(num, 7, x7))
print('{} x {:2} = {}'.format(num, 8, x8))
print('{} x {:2} = {}'.format(num, 9, x9))
print('{} x {:2} = {}'.format(num, 10, x10))
print('-' * 20)