# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem formar um triangulo

r1 = int(input('Comprimento Reta 1: '))
r2 = int(input('Comprimento Reta 2: '))
r3 = int(input('Comprimento Reta 3: '))
maior = r1
menor = r1
medio = r1
if (r2 > maior):
    maior = r2
    medio = r3
if (r3 > maior):
    maior = r3
    medio = r2
if (r2 < menor):
    menor = r2
    medio = r3
if (r3 < menor):
    menor = r3
    medio = r2

if (menor + medio <= maior):
    print('Estas medidas nao formam um triangulo!!')
else:
    print('Estas medidas formam um triangulo!!!')
