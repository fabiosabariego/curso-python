# Crie um programa que leia um numero inteiro e mostre na tela se é par ou impar

num = int(input('Digite um numero: '))
div = num % 2
if div == 0:
    print('Este numero é par!!')
else:
    print('Este Numero é Impar!!')
