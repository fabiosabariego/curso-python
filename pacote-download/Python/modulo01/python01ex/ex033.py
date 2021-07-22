# Fazer um programa que leia 3 numeros, e mostrar qual o maior e qual o menor

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

maior = n1

if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3
print('Maior: ', maior)

menor = n1
if (n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3
print('Menor: ', menor)