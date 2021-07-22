"""
Crie um programa que vá ler vários numeros e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares digitados, respectivamente. No final mostre o conteudo das
3 listas geradas
"""

num = []
par = []
imp = []
cnt = ''
inc = 0
while True:
    if cnt != 'N':
        num.append(int(input('Digite um Valor: ')))
        cnt = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
        if num[inc] % 2 == 0:
            par.append(num[inc])
        if num[inc] % 2 != 0:
            imp.append(num[inc])
        inc += 1
    else:
        break
print('=' * 40)
print(f'Lista Criada com valores digitados: {num}')
print(f'Lista Com os valores Pares: {par}')
print(f'Lista Com os valores Impares: {imp}')