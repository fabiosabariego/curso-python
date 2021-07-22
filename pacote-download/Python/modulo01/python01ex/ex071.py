"""
Crie um programa que Simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuario qual será o valor a
ser sacado (numero inteiro) e o programa vai verificar quantas cédulas de cada valor serão entregues. Considere
que o caixa possui cédulas de 50, 20, 10 e 1.
"""

print('=' * 40)
print('BANCO FSR'.center(40))
print('=' * 40)
valor = int(input('Que valor você gostaria de Sacar? R$'))
inc50 = inc20 = inc10 = inc1 = 0
while True:
    if valor % 50 == 0 and valor > 0:
        inc50 += 1
        valor -= 50
    elif valor % 20 == 0 and valor > 0:
        inc20 += 1
        valor -= 20
    elif valor % 10 == 0 and valor > 0:
        inc10 += 1
        valor -= 10
    elif valor % 1 == 0 and valor > 0:
        inc1 += 1
        valor -= 1
    else:
        break
print(f'Total de {inc50} Cédulas de R$50')
print(f'Total de {inc20} Cédulas de R$20')
print(f'Total de {inc10} Cédulas de R$10')
print(f'Total de {inc1} Cédulas de R$1')
print('=' * 40)
print('Volte sempre ao BANCO FSR, tenha um bom dia!!')


