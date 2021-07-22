"""
Desenvolva um programa que leia 6 numeros inteiros e mostre apenas a soma daqueles que forem pares. Se o valor
digitado for impar, desconsidere
"""
num = 0
res = 0
for c in range(1, 7):
    num = int(input('Digite um valor {}: '.format(c)))
    if num % 2 == 0:
        res += num
print('O programa somou apenas numeros pares, e o resultado foi: {}'.format(res))
