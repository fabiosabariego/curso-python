"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar, no final mostre:
- Qual o total gasto na Compra
- Quantos produtos custam mais de R$1000,00
- Qual é o nome do produto mais barato
"""

print('-' * 50)
print('LOJA VENDAS DIFERENTES!!!'.center(50))
print('-' * 50)
nome = ''
valor = total = prod = frscan = menor = 0
cont = 'S'
barato = ''
while True:
    if cont != 'S':
        break
    else:
        nome = str(input('Nome: ')).strip()
        valor = int(input('Valor R$: '))
        cont = str(input('Continuar? [S/N]: ')).strip().upper()
        total += valor
    if valor > 1000:
        prod += 1
    if frscan != 1:
        menor = valor
        frscan = 1
    if valor < menor:
        menor = valor
        barato = nome
print(f'Valor Toral da compra é R${total:.2f}')
print(f'{prod} produtos custam mais que R$1000,00')
print(f'O produto mais barato é {barato}')