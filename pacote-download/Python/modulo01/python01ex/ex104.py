"""
Faça um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico
"""

def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return num
            break
        else:
            print('\033[1;31mERRO! Digite um Número inteiro válido.')

n = leiaInt('\033[0;0mDigite um Número: ')
print(f'Você acabou de Digitar o valor {n}')