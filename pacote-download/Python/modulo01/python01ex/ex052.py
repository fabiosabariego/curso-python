"""
Faça um programa que leia um numero inteiro e diga se ele é ou não primo
"""
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n\033[mO número {} foi divisivel {} vezes!'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')