"""
Aprimore o ex086, mostrando no final:
- A soma de todos os valores pares digitados
- A soma de todos valores da terceira coluna
- O maior valor da segunda linha
"""

num = soma = soma3 = maior = 0
matriz = [[], [], []]
for c in range(0, 3):
    for l in range(0, 3):
        num = int(input(f'Digite um valor para [{c}, {l}]: '))
        matriz[c].append(num)
        if num % 2 == 0:
            soma += num
        if l == 2:
            soma3 += num
        if c == 1:
            if num > maior:
                maior = num
print('=' * 30)
for i in range(0, 3):
    for n in matriz[i]:
        print(f'[{n:^5}]', end=' ')
    print()
print('=' * 30)
print(matriz)
print(f'A soma dos numeros pares da Matriz é: {soma}')
print(f'A soma dos numeros da Terceira Coluna é: {soma3}')
print(f'O maior número da Segunda Linha é: {maior}')