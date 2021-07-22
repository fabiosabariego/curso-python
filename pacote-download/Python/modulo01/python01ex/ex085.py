"""
Crie um programa onde o usuario pode digitar 7 valores numéricos e cadastre-os em uma lista unica que mantenha
separado os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente
"""
num = 0
principal = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1} valor: '))
    if num % 2 == 0:
        principal[0].append(num)
    else:
        principal[1].append(num)
print('=' * 40)
print(f'Os Valores pares digitados foram: {sorted(principal[0])}')
print(f'Os Valores ímpares digitados foram: {sorted(principal[1])}')