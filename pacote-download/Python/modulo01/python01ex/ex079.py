"""
Crie um programa onde o usuário possa digitar varios valores e cadastre-os em uma lista.
Caso o numero já exista la dentro, ele não será adicionado. No final serão exibidos todos os valores únicos
digitados em ordem crescente
"""

num = []
cont = ''
valor = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor in num:
        print('Esse Valor já existe, não será adicionado!')
    else:
        num.append(valor)
        print('Valor Digitado com sucesso...')
    cont = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    print('=' * 50)
    if cont == 'N':
        break
num.sort()
print(f'Você digitou os valores: {num}')