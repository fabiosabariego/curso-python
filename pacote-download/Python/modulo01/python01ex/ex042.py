"""
Refazer o Ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
- Equilátero -> Todos os lados iguais
- Isõsceles -> Dois lados iguais
- Escaleno -> todos lados diferentes
"""

r1 = int(input("Comprimento Reta 1: "))
r2 = int(input("Comprimento Reta 2: "))
r3 = int(input("Comprimento Reta 3: "))
maior = r1
menor = r1
medio = r1
if r2 > maior:
    maior = r2
    medio = r3
if r3 > maior:
    maior = r3
    medio = r2
if r2 < menor:
    menor = r2
    medio = r3
if r3 < menor:
    menor = r3
    medio = r2

if menor + medio <= maior:
    print('Estas medidas nao formam um triangulo!!')

else:
    print('Estas medidas formam um triangulo!!!')
    if menor == medio == maior:
        print('Este Triângulo é Equilátero, tem todos os lados iguais: C1 = {}, C2 = {} e C3 = {}'.format(r1, r2, r3))
    elif (menor == medio and menor != maior) or (medio == maior and medio != menor):
        print('Esse Triângulo é Isôsceles, tem 2 comprimentos iguais e um diferente: C1 = {}, C2 = {} e C3 = {}'.format(r1, r2, r3))
    elif menor != medio != maior:
        print('Esse Triângulo é Escaleno, todos comprimentos são diferentes: C1 = {}, C2 = {} e C3 = {}'.format(r1, r2, r3))